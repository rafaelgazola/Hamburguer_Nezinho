# Revisão

## Concluído

- `/dono` exige autenticação.
- `OWNER_PASSWORD` e `SECRET_KEY` são variáveis de ambiente.
- `.env`, SQLite, cache e ambientes virtuais estão no `.gitignore`.
- Pedidos inválidos são rejeitados; SQLite usa rollback e fechamento no fluxo de pedido.
- `Procfile` usa `gunicorn --bind 0.0.0.0:$PORT app:app`.
- Rotas usam `url_for` e `requirements.txt` está presente.

## Pendências

- SQLite local não garante persistência compartilhada ou durável no Render; usar volume persistente ou banco externo para produção.
- `/cozinha` permanece pública por decisão operacional e deve ser protegida se a URL não for controlada.
- Tratamento de fechamento/rollback ainda pode ser uniformizado nas demais operações SQLite.
- Completar no briefing o terceiro critério, tempo disponível e fora do escopo.

## Rodada de autenticação e design

- `.env` permanece ignorado e a senha local não aparece nos templates.
- Dashboard, logout, cookies de sessão e responsividade foram verificados.
- Para produção, substituir a senha local curta por uma senha longa e aleatória nas variáveis do Render.
- SQLite local continua sendo limitação para persistência compartilhada no Render.
