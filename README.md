# Currículo / Résumé — Rodrigo Araújo Maciel Pinheiro

Documentos bilíngues para oportunidades de **Desenvolvedor Back-End Python Júnior**. Os projetos destacados são acadêmicos ou pessoais; não são apresentados como experiência de trabalho contratada.

## Currículos para baixar

| Idioma | PDF para candidaturas | DOCX editável | Texto-fonte |
| --- | --- | --- | --- |
| Português (BR) | [PDF](Rodrigo_Pinheiro_2026_PTBR.pdf) | [DOCX](Rodrigo_Pinheiro_2026_PTBR.docx) | [Markdown](src/curriculo_pt.md) |
| English | [PDF](Rodrigo_Pinheiro_2026_EN.pdf) | [DOCX](Rodrigo_Pinheiro_2026_EN.docx) | [Markdown](src/resume_en.md) |

Os documentos são gerados automaticamente com DOCX + LibreOffice e devem ter **uma página por idioma**, texto selecionável e links clicáveis. O PR de lançamento só será integrado depois que os quatro arquivos estiverem presentes na branch e o validador estiver aprovado.

## Projetos documentados

- **[Chamados API](https://github.com/ZaraTakion/chamados-api)** — Django REST Framework, autenticação, autorização, auditoria e notificações.
- **[Task Manager API](https://github.com/ZaraTakion/task-manager-backend)** — FastAPI, Pydantic, SQLite, testes automatizados.
- **[UPA Portal Acadêmico](https://github.com/ZaraTakion/upa-portal-academico)** — API Django REST Framework e aplicação React.

As melhorias técnicas dos projetos estão integradas às respectivas branches principais, como documentam os [PRs Chamados #33](https://github.com/ZaraTakion/chamados-api/pull/33), [Task Manager #2](https://github.com/ZaraTakion/task-manager-backend/pull/2) e [UPA #19](https://github.com/ZaraTakion/upa-portal-academico/pull/19).

## Gerar e validar os documentos

Requisitos: Python 3, `python-docx`, LibreOffice Writer e `poppler-utils`.

```bash
python -m pip install python-docx==1.2.0
python scripts/build_resumes.py
python scripts/validate_release.py
```

`build_resumes.py` usa os dois arquivos-fonte em `src/` para gerar DOCX/PDF. `validate_release.py` verifica integridade, extração de texto, páginas e links dos documentos. O [GitHub Actions](.github/workflows/validate-resumes.yml) automatiza a geração e a verificação.

Mais informações: [Critérios de validação](docs/VALIDACAO.md) e [Conferência antes de candidaturas](docs/REVISAO_E_PUBLICACAO.md).

**Privacidade:** este repositório é público. Revise seus dados de contato e formação antes de distribuir. Não adicione CPF, endereço completo, telefone privado ou dados de terceiros.
