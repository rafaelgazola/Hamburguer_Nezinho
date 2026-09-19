# Relatório TESTER — Verificação final com MCP Playwright

Data: 19/09/2026  
Aplicação: O lancheiro the big nezinho  
Ambiente: `http://127.0.0.1:5000/`  
Ferramenta: MCP Playwright controlando Chrome  
Viewport móvel: 375×812  
Senha de teste: `1234`

## Casos executados

| Caso | Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|---|
| Abrir menu | Acessar `/` | Menu interativo com produtos, quantidades e botão de pedido | Menu carregou com Big Nezinho, Batata Crocante, Refrigerante e envio para cozinha | Passou |
| Abrir login do dono | Clicar em `Dono` após limpar a sessão | Abrir `/login?next=/dono` | Tela `Login do dono` exibida com campo de senha | Passou |
| Senha inválida | Informar `senha-errada` e enviar | Negar acesso e mostrar erro | Permaneceu no login com `Senha inválida.` | Passou |
| Senha válida | Informar `1234` e enviar | Autenticar e abrir dashboard | Redirecionou para `/dono` | Passou |
| Dashboard desktop | Observar o dashboard autenticado | Mostrar gastos mensais de forma clara e profissional | Exibiu título `Gastos mensais`, total `R$ 1070,00`, cards/lista de gastos, navegação e rodapé | Passou |
| Logout/redirecionamento | Clicar em `Sair` | Encerrar sessão e retornar ao login | Redirecionou para `/login`; nova tentativa em `/dono` voltou a exigir autenticação | Passou |
| Senha no HTML público | Inspecionar `outerHTML` de `/` e `/login` | A senha `1234` não deve aparecer | `containsPassword: false` nas duas páginas | Passou |
| Menu móvel | Redimensionar Chrome para 375×812 e abrir `/` | Layout utilizável, sem sobreposição horizontal | Cabeçalho, cards, campos e botão permaneceram dentro da largura útil | Passou |
| Dashboard móvel | Autenticar e redimensionar Chrome para 375×812 | Dashboard legível e utilizável | Total, lançamentos, consulta de mês e botão `Sair` ficaram organizados e acessíveis | Passou |

## Screenshots criados nesta rodada

- `evidencias/16-menu-desktop-verificacao.png`
- `evidencias/17-login-inicial-verificacao.png`
- `evidencias/18-login-invalido-verificacao.png`
- `evidencias/19-login-valido-dashboard-desktop.png`
- `evidencias/20-logout-redirecionamento.png`
- `evidencias/21-dashboard-mobile-375x812.png`
- `evidencias/22-menu-mobile-375x812.png`

As capturas solicitadas de login válido, dashboard desktop e dashboard mobile estão, respectivamente, em `19-login-valido-dashboard-desktop.png` e `21-dashboard-mobile-375x812.png` (o login válido é capturado na tela autenticada do dashboard).

## Limitações

- A base SQLite local já continha gastos fictícios; os valores exibidos refletem esse estado.
- O teste foi feito localmente, sem publicação no Render.
- Nenhum arquivo do aplicativo foi alterado. Foram criados somente este relatório em `testes/` e os screenshots listados em `evidencias/`.
