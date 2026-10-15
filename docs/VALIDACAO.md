# Validação dos currículos

Execute em um ambiente com Python, `python-docx`, LibreOffice Writer e `poppler-utils`:

```bash
python -m pip install python-docx==1.2.0
python scripts/build_resumes.py
python scripts/validate_release.py
```

O script de construção gera dois DOCX editáveis e dois PDFs derivados dos respectivos documentos Word. Não usa APIs externas. Os links e o texto são provenientes dos arquivos em `src/`.

O validador checa, para **cada idioma**, a presença do Markdown, DOCX e PDF; integridade ZIP/XML do DOCX; extração do nome; URLs dos três projetos; PDF sem senha, com exatamente uma página e texto selecionável; links clicáveis para os projetos e e-mail. Toda alteração de conteúdo deve regerar **ambos** os formatos.

O pipeline GitHub Actions gera e valida os quatro documentos. Em pull requests originados neste mesmo repositório, o job também pode adicionar os binários gerados à branch do PR. Em caso de falha de permissão para escrita, consulte os artefatos do job e não faça merge enquanto os downloads do README estiverem faltando.

Testes de arquivo não substituem a revisão editorial de qualificações, datas e dados pessoais.

## Revisão para indicação de outubro de 2026

Fontes PT/EN atualizadas para Chamados API, Takion Campus e Biya. Gerador fixa A4 e remove bordas herdadas do estilo Title. Validador exige uma página e links clicáveis de projetos, e-mail, portfólio e LinkedIn. Os dois DOCX também devem ser renderizados e conferidos visualmente antes de entrega. Currículos sem imagens, colunas ou tabelas de layout para manter a leitura por ferramentas ATS.
