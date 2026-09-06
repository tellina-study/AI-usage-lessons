#!/usr/bin/env python3
"""Lecture 2 EN notes-pages PDF wrapper (issue #188).

`tools/presentation-build/notes_pages_pdf.py` derives every filename from
`lecture_dir.name` (e.g. "lec-02" -> rendered/lec-02.pptx, rendered/
lec-02.pdf, rendered/lec-02-notes.pdf) and hardcodes a few RU-language
literals in the page header/fallback text ("слайд N", "(без заголовка)",
"(нет заметок для этого слайда)", "Источники:"). For the EN deck we need
it to read lec-02-en.pptx / lec-02-en.pdf and write lec-02-notes-en.pdf,
with an EN header/fallback vocabulary.

Technique (same family as lec-03's own make_notes_pdf.py wrapper, see
notes/mcp-limitations.md [#171-1]): build a scratch directory that
mirrors the lecture folder, symlink the EN pptx/pdf under the bare
RU-expected names the tool looks for, patch the handful of RU literal
strings in a copy of the tool's source, then call its own build()
unmodified otherwise (positional slide<->notes matching, pagination,
footer numbering all stay exactly as tested in [#170-4b]).
"""
import re
import shutil
import sys
import tempfile
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[4] / "tools" / "presentation-build"
LECDIR = Path(__file__).resolve().parent.parent  # library/lectures/lec-02
LEC_ID = "lec-02"


def _en_title() -> str:
    en_yaml = LECDIR / "deck.en.yaml"
    if en_yaml.exists():
        in_deck = False
        for raw in en_yaml.read_text(encoding="utf-8").splitlines():
            line = raw.rstrip("\n")
            if re.match(r"^\s*#", line) or not line.strip():
                continue
            if re.match(r"^deck:\s*$", line):
                in_deck = True
                continue
            if in_deck:
                if re.match(r"^\S", line) and not re.match(r"^deck:", line):
                    break
                m = re.match(r'^\s+title:\s*(.+?)\s*$', line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    return "Lecture 2. How Modern Large Language Models Work"


def main():
    with tempfile.TemporaryDirectory() as tmp:
        scratch = Path(tmp) / LEC_ID
        scratch_rendered = scratch / "rendered"
        scratch_rendered.mkdir(parents=True)

        # EN-titled deck.yaml so lecture_title() picks up the EN name.
        (scratch / "deck.yaml").write_text(
            f'deck:\n  title: "{_en_title()}"\n', encoding="utf-8")

        # Symlink EN artifacts under the bare names build() expects.
        (scratch_rendered / f"{LEC_ID}.pptx").symlink_to(
            LECDIR / "rendered" / f"{LEC_ID}-en.pptx")
        (scratch_rendered / f"{LEC_ID}.pdf").symlink_to(
            LECDIR / "rendered" / f"{LEC_ID}-en.pdf")

        # Patch the tool's RU literals to EN in a throwaway copy of its
        # source, then load and run that copy's build() directly.
        src = (TOOLS_DIR / "notes_pages_pdf.py").read_text(encoding="utf-8")
        src_en = (
            src
            .replace('f"слайд {slide_no}"', 'f"slide {slide_no}"')
            .replace('"(без заголовка)"', '"(no title)"')
            .replace('"(нет заметок для этого слайда)"',
                     '"(no notes for this slide)"')
            .replace('b.lstrip().startswith("Источники:")',
                     'b.lstrip().startswith(("Sources:", "Источники:"))')
        )
        mod_path = Path(tmp) / "notes_pages_pdf_en.py"
        mod_path.write_text(src_en, encoding="utf-8")

        sys.path.insert(0, str(TOOLS_DIR))  # tool's own deps (pymupdf etc.)
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "notes_pages_pdf_en", mod_path)
        Npatched = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(Npatched)

        Npatched.build(scratch, 150, None)

        produced = scratch_rendered / f"{LEC_ID}-notes.pdf"
        final_out = LECDIR / "rendered" / f"{LEC_ID}-notes-en.pdf"
        shutil.copy(produced, final_out)
        print(f"[ok] {final_out}")


if __name__ == "__main__":
    main()
