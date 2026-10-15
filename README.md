# Currículo / Résumé — Rodrigo Araújo Maciel Pinheiro

Documentos bilíngues para oportunidades de **Desenvolvedor Back-End Python Júnior**. Os projetos destacados são acadêmicos ou pessoais; não são apresentados como experiência de trabalho contratada.

## Currículos para baixar

| Idioma | PDF para candidaturas | DOCX editável | Texto-fonte |
| --- | --- | --- | --- |
| Português (BR) | [PDF](Rodrigo_Pinheiro_2026_PTBR.pdf) | [DOCX](Rodrigo_Pinheiro_2026_PTBR.docx) | [Markdown](src/curriculo_pt.md) |
| English | [PDF](Rodrigo_Pinheiro_2026_EN.pdf) | [DOCX](Rodrigo_Pinheiro_2026_EN.docx) | [Markdown](src/resume_en.md) |

Os documentos são gerados automaticamente com DOCX + LibreOffice/soffice e devem ter **uma página A4 por idioma**, texto selecionável e links clicáveis. O PR de lançamento só será integrado depois que os quatro arquivos estiverem presentes na branch e o validador estiver aprovado.

## Projetos documentados

- **[Chamados API](https://github.com/ZaraTakion/chamados-api)** — Django REST, JWT, autorização, histórico e notificações com outbox transacional. Demonstração local.
- **[Takion Campus](https://github.com/ZaraTakion/takion-campus)** — evolução do UPA Portal Acadêmico, com Django REST, React e fluxos por perfil.
- **[Biya Parallel Worlds](https://github.com/ZaraTakion/biya-landing)** — interface React/TypeScript, galeria e conteúdo PT/EN.

Projetos pessoais e acadêmicos, sem alegação de emprego formal, clientes pagos ou métricas de negócio. FastAPI permanece como competência complementar documentada no [Task Manager API](https://github.com/ZaraTakion/task-manager-backend).

Cada currículo inclui contato, [portfólio PT](https://portfolio.zaratakion.workers.dev/), [portfólio EN](https://portfolio.zaratakion.workers.dev/en/), GitHub e LinkedIn. Formação: Sistemas para Internet, UNIESP, concluído em 2026. Idiomas informados: português nativo, inglês básico e espanhol intermediário.

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
