import os
import sqlite3
from datetime import datetime
from functools import wraps
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DATABASE = Path(os.environ.get("DATABASE_PATH", DATA_DIR / "lancheiro.db"))
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(32))
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("FLASK_ENV") == "production",
)


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL CHECK(price >= 0)
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'recebido',
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL REFERENCES orders(id),
            menu_item_id INTEGER NOT NULL REFERENCES menu_items(id),
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            unit_price REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount >= 0),
            expense_date TEXT NOT NULL
        );
        """
    )
    if conn.execute("SELECT COUNT(*) FROM menu_items").fetchone()[0] == 0:
        conn.executemany(
            "INSERT INTO menu_items(name, description, price) VALUES (?, ?, ?)",
            [
                ("Big Nezinho", "Hambúrguer artesanal, queijo e molho da casa", 28.90),
                ("Batata Crocante", "Porção individual com molho especial", 14.00),
                ("Refrigerante", "Lata 350 ml", 6.00),
            ],
        )
    if conn.execute("SELECT COUNT(*) FROM expenses").fetchone()[0] == 0:
        month = datetime.now().strftime("%Y-%m")
        conn.executemany(
            "INSERT INTO expenses(description, amount, expense_date) VALUES (?, ?, ?)",
            [("Compra de insumos", 850.00, f"{month}-05"), ("Embalagens", 220.00, f"{month}-10")],
        )
    conn.commit()
    conn.close()


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("owner_logged_in"):
            flash("Faça login para acessar o dashboard.", "error")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
def menu():
    conn = get_db()
    items = conn.execute("SELECT * FROM menu_items ORDER BY id").fetchall()
    conn.close()
    return render_template("menu.html", items=items)


@app.post("/pedido")
def create_order():
    customer_name = request.form.get("customer_name", "").strip() or "Cliente"
    quantities = {}
    conn = get_db()
    try:
        item_fields = [(key, value) for key, value in request.form.items() if key.startswith("item_")]
        for key, value in item_fields:
            item_id_text = key[5:]
            if not item_id_text.isdigit() or int(item_id_text) <= 0 or not value.isdigit():
                flash("Os itens do pedido são inválidos.", "error")
                return redirect(url_for("menu"))
            quantity = int(value)
            if quantity < 0:
                flash("A quantidade dos itens é inválida.", "error")
                return redirect(url_for("menu"))
            if quantity > 0:
                quantities[int(item_id_text)] = quantity
        if not quantities:
            flash("Selecione pelo menos um item válido.", "error")
            return redirect(url_for("menu"))
        placeholders = ",".join("?" for _ in quantities)
        rows = conn.execute(f"SELECT * FROM menu_items WHERE id IN ({placeholders})", list(quantities)).fetchall()
        if len(rows) != len(quantities):
            flash("Um ou mais itens selecionados não existem.", "error")
            return redirect(url_for("menu"))
        total = sum(row["price"] * quantities[row["id"]] for row in rows)
        if total <= 0:
            flash("O pedido precisa ter itens válidos.", "error")
            return redirect(url_for("menu"))
        cursor = conn.execute(
            "INSERT INTO orders(customer_name, total, created_at) VALUES (?, ?, ?)",
            (customer_name, total, datetime.now().isoformat(timespec="seconds")),
        )
        for row in rows:
            conn.execute(
                "INSERT INTO order_items(order_id, menu_item_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                (cursor.lastrowid, row["id"], quantities[row["id"]], row["price"]),
            )
        conn.commit()
        order_id = cursor.lastrowid
    except sqlite3.Error:
        conn.rollback()
        flash("Não foi possível registrar o pedido.", "error")
        return redirect(url_for("menu"))
    finally:
        conn.close()
    flash(f"Pedido #{order_id} enviado para a cozinha!", "success")
    return redirect(url_for("menu"))


@app.route("/cozinha")
def kitchen():
    conn = get_db()
    orders = conn.execute(
        "SELECT * FROM orders WHERE status != 'finalizado' ORDER BY id DESC"
    ).fetchall()
    order_items = {}
    for order in orders:
        order_items[order["id"]] = conn.execute(
            "SELECT oi.quantity, mi.name FROM order_items oi JOIN menu_items mi ON mi.id = oi.menu_item_id WHERE oi.order_id = ?",
            (order["id"],),
        ).fetchall()
    conn.close()
    return render_template("kitchen.html", orders=orders, order_items=order_items)


@app.post("/cozinha/<int:order_id>/finalizar")
def finish_order(order_id):
    conn = get_db()
    conn.execute("UPDATE orders SET status = 'finalizado' WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("kitchen"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        configured_password = os.environ.get("OWNER_PASSWORD")
        if not configured_password:
            flash("Configure OWNER_PASSWORD antes de entrar.", "error")
        elif request.form.get("password") == configured_password:
            session["owner_logged_in"] = True
            return redirect(request.args.get("next") or url_for("dashboard"))
        else:
            flash("Senha inválida.", "error")
    return render_template("login.html")


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dono")
@login_required
def dashboard():
    month = request.args.get("month") or datetime.now().strftime("%Y-%m")
    conn = get_db()
    expenses = conn.execute(
        "SELECT * FROM expenses WHERE substr(expense_date, 1, 7) = ? ORDER BY expense_date DESC", (month,)
    ).fetchall()
    total = sum(row["amount"] for row in expenses)
    conn.close()
    return render_template("dashboard.html", expenses=expenses, total=total, month=month)


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
