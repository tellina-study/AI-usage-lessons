#!/usr/bin/env python3
"""Run-level string extraction / substitution for translating a rendered deck.

Used for decks whose build script is stale or hand-edited (sem-01, sem-02):
instead of forking a 1000+ line builder, the EN deck is produced by swapping
every text run of the RU deck for its translation. Layout, palette, images and
slide count stay byte-identical to the approved RU render, so the EN deck can
never drift structurally from the RU one.

    extract:  python3 pptx_i18n.py extract <deck.pptx> <strings.json>
    apply:    python3 pptx_i18n.py apply <deck.pptx> <strings.en.json> <out.pptx>

strings.json is a list of {"key", "slide", "where", "ru"}; the translator adds
an "en" field to each entry. `apply` refuses to run if any entry is missing an
"en" value, so a partial translation can never silently ship half-Russian.
"""
import json
import sys

from pptx import Presentation


def _frames(shapes):
    """Yield every text frame on a slide, descending into groups and tables."""
    for sh in shapes:
        if sh.shape_type == 6:  # GROUP
            yield from _frames(sh.shapes)
            continue
        if sh.has_text_frame:
            yield sh.text_frame
        if getattr(sh, "has_table", False):
            for row in sh.table.rows:
                for cell in row.cells:
                    yield cell.text_frame


def _runs(prs):
    """Yield (key, slide_no, where, run, para_no) for every non-empty run.

    para_no groups runs that share one paragraph: a paragraph split across runs
    (a colour-accented first letter, say) must be translated as a whole and then
    redistributed across its runs, not run by run.
    """
    for i, slide in enumerate(prs.slides, 1):
        for where, frames in (("body", _frames(slide.shapes)),
                              ("notes", [slide.notes_slide.notes_text_frame]
                               if slide.has_notes_slide else [])):
            n = para_no = 0
            for frame in frames:
                for para in frame.paragraphs:
                    runs = [r for r in para.runs if r.text.strip()]
                    if not runs:
                        continue
                    para_no += 1
                    for run in runs:
                        n += 1
                        yield f"s{i:02d}.{where}.{n:03d}", i, where, run, para_no


def extract(src, out):
    prs = Presentation(src)
    items = [{"key": k, "slide": i, "where": w, "para": p, "ru": r.text, "en": ""}
             for k, i, w, r, p in _runs(prs)]
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=1)
    print(f"{src}: {len(items)} runs -> {out}")


def apply(src, table, out):
    with open(table, encoding="utf-8") as fh:
        en = {e["key"]: e["en"] for e in json.load(fh)}
    prs = Presentation(src)
    missing, done = [], 0
    for key, _, _, run, _ in _runs(prs):
        text = en.get(key)
        if not text:
            missing.append(key)
            continue
        run.text = text
        done += 1
    if missing:
        sys.exit(f"{len(missing)} runs have no translation, first: {missing[:5]}")
    prs.save(out)
    print(f"{src}: {done} runs translated -> {out}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["extract"]:
        extract(*sys.argv[2:4])
    elif sys.argv[1:2] == ["apply"]:
        apply(*sys.argv[2:5])
    else:
        sys.exit(__doc__)
