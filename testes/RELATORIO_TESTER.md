# Relatório TESTER — O lancheiro the big nezinho

Data: 19/09/2026  
Ambiente: servidor local Flask em `http://127.0.0.1:5000/`  
Ferramenta: MCP Playwright controlando Chrome  
Dados: fictícios (`Mesa 7`, senha de teste `teste-local`)

## Casos executados

| Caso | Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|---|
| Menu interativo | Abrir `/` e consultar produtos | Menu, preços, quantidades e identificação de mesa disponíveis | Exibidos Big Nezinho, Batata Crocante, Refrigerante, campos de quantidade e nome/mesa | Passou |
| Carrinho/pedido vazio | Informar `Mesa Teste Vazia` sem itens e enviar | Sistema impedir envio e informar o problema | Mensagem `Selecione pelo menos um item.` exibida; nenhum pedido vazio criado | Passou |
| Envio do pedido | Informar Mesa 7, quantidade 2 de Big Nezinho e enviar | Pedido persistido e confirmação de envio à cozinha | Mensagem `Pedido #5 enviado para a cozinha!` exibida | Passou |
| Cozinha | Abrir `/cozinha` após envio | Pedido enviado aparecer na tela da cozinha | Pedido #5 apareceu como `Mesa 7`, `2x Big Nezinho`, total `R$ 57,80` | Passou |
| Dashboard protegido | Abrir `/dono` sem sessão autenticada | Redirecionar para login | Redirecionado para `/login?next=/dono` | Passou |
| Login inválido | Informar `senha-incorreta` | Negar acesso e informar erro | Permaneceu no login com `Senha inválida.` | Passou |
| Login válido/dashboard | Informar `teste-local` | Acessar dashboard com gastos mensais | `/dono` abriu com título `Gastos mensais`, total `R$ 1070,00` e dois lançamentos | Passou |
| Dashboard sem dados | Consultar mês `2020-01` | Mostrar total zero e estado vazio sem erro | Exibido `Total de 2020-01 R$ 0,00` e `Nenhum gasto registrado neste mês.` | Passou |
| Responsividade móvel | Redimensionar Chrome para 375x812 e abrir `/` | Conteúdo legível, sem sobreposição e utilizável | Todos os campos, cards e botão ficaram dentro da largura útil; snapshot confirmou caixas sem overflow horizontal | Passou |

## Evidências

- `evidencias/01-menu-desktop.png`
- `evidencias/02-pedido-enviado.png`
- `evidencias/03-cozinha-pedido-persistido.png`
- `evidencias/04-login-invalido.png`
- `evidencias/05-dashboard-login-valido.png`
- `evidencias/06-dashboard-sem-dados.png`
- `evidencias/07-menu-mobile-375px.png`

## Limitações e observações

- Os testes usaram a base SQLite local existente, que já continha pedidos/gastos fictícios; por isso os números exibidos refletem esse estado inicial.
- O navegador registrou um erro 404 para `http://127.0.0.1:5000/favicon.ico`. Não afetou os fluxos testados.
- Não foi feito teste em Render/publicação, pois o escopo deste agente é a verificação local pelo Playwright.
- Nenhum arquivo do aplicativo foi alterado. Foram criados apenas este relatório, `.gitkeep` em `testes/` e `evidencias/`, e os screenshots em `evidencias/`.
