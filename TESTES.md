# Testes

## Resultado

Executados no Chrome via MCP Playwright. A segunda rodada passou em todos os casos:

- menu → pedido → cozinha;
- persistência do pedido;
- carrinho vazio, quantidade inválida e ID inexistente;
- dashboard protegido sem login;
- login válido e inválido;
- dashboard com e sem dados;
- viewport móvel de 375×812.

Pedido válido `RODADA2-VALIDA` foi persistido. Entradas inválidas não criaram pedidos.

Relatórios detalhados: `testes/RELATORIO_TESTER.md` e `testes/RELATORIO_TESTER_RODADA2.md`.

Evidências: arquivos PNG em `evidencias/`, incluindo `08-validacao-pedido-invalido.png`, `09-dashboard-protegido-pos-correcao.png` e `15-menu-mobile-pos-correcao.png`.

Limitação observada: requisição de `favicon.ico` retorna 404, sem impacto funcional.

## Verificação de autenticação e design

Executada no Chrome via MCP Playwright:

- senha inválida bloqueada;
- senha local configurada no `.env` autenticou corretamente;
- dashboard protegido sem sessão;
- logout redireciona para login;
- senha não aparece no HTML público;
- dashboard, menu e login verificados em 375×812.

Relatório: `testes/RELATORIO_TESTER_VERIFICACAO_FINAL.md`.
Evidências: `evidencias/19-login-valido-dashboard-desktop.png`, `evidencias/20-logout-redirecionamento.png`, `evidencias/21-dashboard-mobile-375x812.png` e `evidencias/22-menu-mobile-375x812.png`.
