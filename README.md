# O lancheiro the big nezinho

Aplicação mínima em Flask para cardápio, envio de pedidos à cozinha e dashboard protegido do dono.

## Executar localmente

Copie `.env.example` para `.env` e preencha os valores locais, sem compartilhar esse arquivo. Alternativamente, defina as variáveis na sessão do terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OWNER_PASSWORD='sua-senha-local'
$env:SECRET_KEY='sua-chave-local'
python app.py
```

Acesse `http://localhost:5000/`. O cardápio fica em `/`, a cozinha em `/cozinha` e o login/dashboard em `/login` e `/dono`.

`/cozinha` permanece público por decisão operacional: é a tela compartilhada que a equipe usa para receber e finalizar pedidos, enquanto apenas o dashboard do dono exige autenticação.

O banco SQLite é criado em `data/lancheiro.db` e não é compartilhado automaticamente entre aparelhos.

## Configuração no Render

Antes de criar ou executar o deploy, abra o serviço no Render, entre em **Environment** e adicione:

- `OWNER_PASSWORD`: uma senha forte escolhida por você;
- `SECRET_KEY`: uma chave longa e aleatória para as sessões;
- `FLASK_ENV`: `production`.

Salve as variáveis e faça um novo deploy. O Render não recebe o `.env` local, pois ele é ignorado pelo Git. Se `OWNER_PASSWORD` não estiver configurada, o login exibirá uma orientação para corrigir a configuração sem revelar qualquer segredo.

Para persistência real, configure um volume ou banco externo; esta versão usa SQLite local simples.
