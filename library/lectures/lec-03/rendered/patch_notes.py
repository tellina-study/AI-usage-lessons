"""Patch slides/*.md «## Speaker notes» for the 26 ref-slides (issue #171):
inject [N] markers at NOTES_ANCHORS + append the «Источники:» block.
Idempotent: skips a file that already carries «Источники:».
Run: python3 patch_notes.py   (from rendered/)
"""
import re
from pathlib import Path

import refs_lec03 as R

SLIDES = Path(__file__).resolve().parents[1] / "slides"
NOTES_RE = re.compile(r'(## Speaker notes\s*\n)(.*?)(\n*---\s*)?\Z', re.DOTALL)


def main():
    total_missed = []
    patched = 0
    for sid in R.SLIDE_REFS:
        files = list(SLIDES.glob(f"{sid}-*.md"))
        if not files:
            print(f"!! {sid}: no md")
            continue
        f = files[0]
        md = f.read_text(encoding="utf-8")
        m = NOTES_RE.search(md)
        if not m:
            print(f"!! {sid}: no Speaker notes section")
            continue
        head, body, tail = m.group(1), m.group(2), (m.group(3) or "")
        if "Источники:" in body:
            print(f".. {sid}: already patched, skip")
            continue
        body = body.rstrip()
        # 1) inject [N] markers
        body2, missed = R.inject_notes_markers(body, sid)
        for a in missed:
            total_missed.append((sid, a))
        # 2) append sources block
        block = R.notes_sources_block(sid)
        new_body = f"{body2}\n\n{block}\n"
        new_md = md[:m.start()] + head + new_body + tail
        f.write_text(new_md, encoding="utf-8")
        patched += 1
        print(f"ok {sid}: +{len(R.SLIDE_REFS[sid])} refs, "
              f"{len(R.NOTES_ANCHORS.get(sid, [])) - len(missed)}/"
              f"{len(R.NOTES_ANCHORS.get(sid, []))} markers")
    print(f"\npatched {patched} files")
    if total_missed:
        print("!! UNMATCHED NOTES ANCHORS:")
        for sid, a in total_missed:
            print(f"   {sid}: {a!r}")


if __name__ == "__main__":
    main()
