# O lancheiro the big nezinho

Aplicação mínima em Flask para cardápio, envio de pedidos à cozinha e dashboard protegido do dono.

## Executar localmente

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OWNER_PASSWORD='troque-esta-senha'
$env:SECRET_KEY='uma-chave-local'
python app.py
```

Acesse `http://localhost:5000/`. O cardápio fica em `/`, a cozinha em `/cozinha` e o login/dashboard em `/login` e `/dono`.

`/cozinha` permanece público por decisão operacional: é a tela compartilhada que a equipe usa para receber e finalizar pedidos, enquanto apenas o dashboard do dono exige autenticação.

O banco SQLite é criado em `data/lancheiro.db` e não é compartilhado automaticamente entre aparelhos. Em Render, configure `OWNER_PASSWORD`, `SECRET_KEY` e, para persistência real, um volume ou banco externo; esta versão usa armazenamento local simples.
