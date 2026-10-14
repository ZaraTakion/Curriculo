# Validação dos currículos

Execute em um ambiente com Python, `python-docx`, LibreOffice Writer e `poppler-utils`:

```bash
python -m pip install python-docx==1.2.0
python scripts/build_resumes.py
python scripts/validate_release.py
```

O script de construção gera dois DOCX editáveis e dois PDFs derivados dos respectivos documentos Word. Não usa APIs externas. Os links e o texto são provenientes dos arquivos em `src/`.

O validador checa, para **cada idioma**, a presença do Markdown, DOCX e PDF; integridade ZIP/XML do DOCX; extração do nome; URLs dos quatro projetos; paridade de todo o texto com as fontes Markdown, e-mail selecionável para ATS, PDF sem senha, com exatamente uma página e texto selecionável; links clicáveis para os projetos e e-mail. Toda alteração de conteúdo deve regerar **ambos** os formatos.

O pipeline GitHub Actions primeiro valida os quatro arquivos já commitados contra as fontes Markdown. Se estiverem antigos, falha antes da regeneração. Em seguida, gera e valida novos artefatos para o job. Não faz commits automáticos; atualize e versione os binários junto com alterações editoriais.

Testes de arquivo não substituem a revisão editorial de qualificações, datas e dados pessoais.
