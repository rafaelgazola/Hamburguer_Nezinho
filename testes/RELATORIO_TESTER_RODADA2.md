# Relatório TESTER — Segunda rodada pós-correção

Data: 19/09/2026  
Ambiente: `http://127.0.0.1:5000/`  
Ferramenta: MCP Playwright controlando Chrome  
Dados fictícios: `RODADA2-VAZIO`, `RODADA2-NEGATIVO`, `RODADA2-VALIDA` e senha de teste `teste-local`

## Casos executados

| Caso | Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|---|
| Carrinho vazio | Informar `RODADA2-VAZIO` e enviar sem itens | Exibir validação e não criar pedido | Exibido `Selecione pelo menos um item.`; o identificador não apareceu na cozinha | Passou |
| Entrada inválida negativa | Informar `RODADA2-NEGATIVO`, quantidade `-1` e enviar | Rejeitar quantidade inválida e não criar pedido | Exibido `Selecione pelo menos um item.`; o identificador não apareceu na cozinha | Passou |
| Entrada textual | Tentar preencher campo numérico com `abc` | Impedir entrada inválida sem criar pedido | O Playwright foi impedido pelo próprio `input[type=number]`; nenhuma submissão foi criada | Passou |
| Menu → pedido → cozinha | Informar `RODADA2-VALIDA`, quantidade 1 de Big Nezinho e enviar; abrir `/cozinha` | Confirmar envio e persistência na cozinha | Mensagem `Pedido #7 enviado para a cozinha!`; cozinha exibiu `RODADA2-VALIDA`, `1x Big Nezinho`, `R$ 28,90` | Passou |
| Proteção do dashboard | Sair da sessão e abrir `/dono` | Redirecionar para login | Após `Sair`, `/dono` redirecionou para `/login` | Passou |
| Login inválido | Informar `senha-incorreta-rodada2` | Negar acesso com mensagem | Permanecer no login com `Senha inválida.` | Passou |
| Login válido | Informar `teste-local` | Abrir dashboard do dono | `/dono` abriu com `Gastos mensais`, total `R$ 1070,00` e lançamentos | Passou |
| Dashboard sem dados | Consultar `2020-01` | Exibir total zero e estado vazio | Exibido `R$ 0,00` e `Nenhum gasto registrado neste mês.` | Passou |
| Viewport móvel | Redimensionar Chrome para 375×812 e abrir o menu | Layout utilizável sem overflow horizontal | Snapshot confirmou conteúdo dentro da largura útil; cards e botão permaneceram acessíveis | Passou |

## Screenshots novos

- `evidencias/08-validacao-pedido-invalido.png`
- `evidencias/09-dashboard-protegido-pos-correcao.png`
- `evidencias/09-cozinha-sem-invalidos.png`
- `evidencias/10-pedido-cozinha-pos-correcao.png`
- `evidencias/11-cozinha-pos-correcao.png`
- `evidencias/12-login-invalido-pos-correcao.png`
- `evidencias/13-dashboard-pos-correcao.png`
- `evidencias/14-dashboard-sem-dados-pos-correcao.png`
- `evidencias/15-menu-mobile-pos-correcao.png`

## Observações e limitações

- A tela da cozinha confirmou que os identificadores dos testes inválidos não foram persistidos; o pedido válido foi o #7.
- O campo HTML numérico bloqueou a digitação textual `abc` antes do envio, portanto não houve requisição para esse caso.
- O console registrou 404 para `favicon.ico` e 405 ao tentar navegar diretamente para `/logout` via GET; o logout funcional por botão POST e os fluxos testados funcionaram.
- Nenhum arquivo do aplicativo foi alterado. Foram criados apenas screenshots em `evidencias/` e este relatório em `testes/`.
