# Relatório TESTER — Smoke test de autenticação local

Data: 19/09/2026  
Ferramenta: Flask `test_client` e `py_compile`  
Navegador: não utilizado  
Escopo: validação local sem alterar o código

## Cenário 1 — `OWNER_PASSWORD=1234`

| Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|
| Compilar `app.py` | Compilação sem erro | `py_compile` concluído sem erro | Passou |
| Acessar `/dono` sem sessão | Redirecionar para login | HTTP 302 com destino contendo `/login` | Passou |
| Enviar login com senha `1234` | Autenticar e redirecionar ao dashboard | HTTP 302 para `/dono` | Passou |
| Acessar `/dono` após login | Dashboard responder | HTTP 200 | Passou |
| Acessar `/` | Menu continuar respondendo | HTTP 200 | Passou |
| Acessar `/cozinha` | Tela da cozinha continuar respondendo | HTTP 200 | Passou |

Resultado do comando: `AUTH_MENU_KITCHEN_SMOKE_OK`.

## Cenário 2 — sem `OWNER_PASSWORD`

| Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|
| Acessar `/` | Página pública responder | HTTP 200 | Passou |
| Acessar `/login` | Página orientar a configuração da variável | HTTP 200; conteúdo contém `OWNER_PASSWORD` | Passou |
| Acessar `/dono` sem senha configurada | Continuar protegido | HTTP 302 para `/login?next=/dono` | Passou |
| Verificar segredo `1234` no conteúdo retornado | Não expor senha | Nenhuma ocorrência de `1234` | Passou |
| Verificar chave padrão `local-development-key` | Não expor segredo | Nenhuma ocorrência | Passou |

Resultado do comando: `MISSING_PASSWORD_SMOKE_OK`.

## Limitações

- Os testes foram locais e não validam o ambiente publicado.
- `OWNER_PASSWORD=1234` foi usado somente como variável de processo durante o primeiro comando; não foi gravado em arquivo.
- Nenhum arquivo do aplicativo foi alterado; este relatório é o único arquivo criado nesta rodada.
