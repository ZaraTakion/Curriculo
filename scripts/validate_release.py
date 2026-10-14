#!/usr/bin/env python3
"""Validate bilingual DOCX/PDF deliverables offline (requires poppler-utils)."""
from __future__ import annotations

import subprocess
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ("takion-campus", "chamados-api", "biya-landing", "task-manager-backend")
NAME = "RODRIGO ARAÚJO MACIEL PINHEIRO"


def command(*argv: str) -> str:
    result = subprocess.run(
        argv, text=True, capture_output=True, encoding="utf-8", errors="replace", check=True
    )
    return result.stdout


def validate(language: str, source_file: str) -> None:
    stem = f"Rodrigo_Pinheiro_2026_{language}"
    docx, pdf = ROOT / f"{stem}.docx", ROOT / f"{stem}.pdf"
    source = ROOT / "src" / source_file
    for item in (docx, pdf, source):
        if not item.is_file() or item.stat().st_size <= 0:
            raise ValueError(f"Missing/empty: {item.name}")

    raw = source.read_text(encoding="utf-8")
    assert NAME in raw.upper(), "Full name missing in Markdown"
    for slug in PROJECTS:
        assert f"https://github.com/ZaraTakion/{slug}" in raw, f"Missing source project {slug}"

    try:
        with ZipFile(docx) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
            relationships = archive.read("word/_rels/document.xml.rels").decode("utf-8")
    except (BadZipFile, KeyError, ET.ParseError) as exc:
        raise ValueError("Invalid DOCX") from exc

    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    text = " ".join("".join(item.text or "" for item in paragraph.iter(f"{namespace}t"))
                    for paragraph in root.iter(f"{namespace}p"))
    assert NAME in text.upper(), "Full name not extractable in DOCX"
    for slug in PROJECTS:
        assert slug in relationships, f"Missing clickable DOCX link to {slug}"

    info = command("pdfinfo", str(pdf))
    assert any(
        line.startswith("Pages:") and line.split(":", 1)[1].strip() == "1"
        for line in info.splitlines()
    ), "PDF must have exactly one page"
    assert not any(
        line.startswith("Encrypted:") and line.split(":", 1)[1].strip() == "yes"
        for line in info.splitlines()
    ), "PDF must not be encrypted"
    extracted = command("pdftotext", str(pdf), "-")
    assert NAME in extracted.upper(), "Full name not extractable from PDF"
    assert "rm20022101@gmail.com" in extracted, "Contact email must be extractable for ATS"
    assert len(extracted.strip()) >= 650, "Insufficient extractable PDF text"
    def normalize(value):
        return " ".join(unicodedata.normalize("NFKC", value).split())
    for line in raw.splitlines():
        if not line.strip():
            continue
        expected = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        expected = re.sub(r"^(?:#+ |\- )", "", expected).replace("**", "")
        assert normalize(expected) in normalize(text), f"DOCX content differs from Markdown source: {expected}"
        assert normalize(expected) in normalize(extracted), f"PDF content differs from Markdown source: {expected}"
    links = command("pdfinfo", "-url", str(pdf))
    for slug in PROJECTS:
        assert f"https://github.com/ZaraTakion/{slug}" in links, f"Missing clickable PDF link to {slug}"
    assert "mailto:" in links, "Missing clickable e-mail link"
    print(f"[PASS] {language}: source + DOCX + one-page searchable linked PDF")


def main() -> int:
    failures = 0
    for language, source in (("PTBR", "curriculo_pt.md"), ("EN", "resume_en.md")):
        try:
            validate(language, source)
        except (AssertionError, ValueError, OSError, subprocess.CalledProcessError) as exc:
            print(f"[FAIL] {language}: {exc}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
