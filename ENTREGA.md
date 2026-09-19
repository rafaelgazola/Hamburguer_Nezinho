# Entrega — O lancheiro the big nezinho

## Funcionalidades

- Menu interativo para cliente/garçom.
- Pedido persistido em SQLite e exibido na cozinha.
- Login do dono e dashboard de gastos mensais.
- Configuração local e básica para Render.

## Como executar

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OWNER_PASSWORD="sua-senha"
$env:SECRET_KEY="sua-chave"
py app.py
```

Acesse `http://localhost:5000/`.

## Validação

Fluxos principais e casos inválidos passaram no Chrome via MCP Playwright. Evidências estão em `evidencias/`.

## Limitações

O SQLite fica local e não compartilha dados automaticamente entre aparelhos nem garante durabilidade no Render. Não houve publicação nem link real; a publicação permanece pendente. A rota `/cozinha` é pública por decisão operacional documentada.

## Atualização

O acesso local do dono foi corrigido por variável em `.env` ignorado pelo Git. O design foi aprimorado com identidade visual profissional de hamburgueria e responsividade. Login, logout e dashboard foram validados no Chrome via MCP Playwright. A senha local é apenas para desenvolvimento; use uma credencial forte no Render.
