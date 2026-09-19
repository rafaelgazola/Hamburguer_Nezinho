# Relatório TESTER — Validação das regras Git

Data: 19/09/2026  
Ferramenta: Git (`git check-ignore --no-index -v`)  
Escopo: somente validação de ignore; nenhum navegador utilizado

## Resultados

| Ação | Resultado esperado | Resultado observado | Status |
|---|---|---|---|
| Verificar `.env` | Deve ser ignorado | Ignorado por `.gitignore:2:.env` | Passou |
| Verificar `data/lancheiro.db` | Deve ser ignorado | Ignorado por `.gitignore:7:data/*.db` | Passou |
| Verificar `local.sqlite` | Deve ser ignorado | Ignorado por `.gitignore:8:*.sqlite` | Passou |
| Verificar `__pycache__/` | Deve ser ignorado | Ignorado por `.gitignore:12:__pycache__/` | Passou |
| Verificar `.venv/` | Deve ser ignorado | Ignorado por `.gitignore:14:.venv/` | Passou |
| Verificar `.playwright-mcp/` | Deve ser ignorado | Ignorado por `.gitignore:25:.playwright-mcp/` | Passou |
| Verificar `app.py` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `templates/base.html` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `static/style.css` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `requirements.txt` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `Procfile` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `README.md` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `evidencias/` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |
| Verificar `testes/` | Não deve ser ignorado | `git check-ignore` não encontrou regra | Passou |

## Limitações

- A verificação confirma somente as regras do `.gitignore`; não valida conteúdo, permissões ou histórico de commits.
- Nenhum arquivo do aplicativo ou `.gitignore` foi alterado.
- O único arquivo criado nesta rodada foi este relatório em `testes/`.
