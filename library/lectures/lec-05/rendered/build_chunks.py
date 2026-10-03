"""Рендер деки почанково: LibreOffice на нагруженной машине не вытягивает
56 слайдов за один заход (notes/mcp-limitations.md [#212-1]/[#212-2]).
Собирает части по N слайдов с ГЛОБАЛЬНОЙ нумерацией страниц 1..56."""
import os
import sys
from pathlib import Path
REND = Path(__file__).resolve().parent
sys.path.insert(0, str(REND))
from _helpers import setup_pres, page_number      # noqa: E402
import build_lec05 as B                           # noqa: E402

CHUNK = int(sys.argv[1]) if len(sys.argv) > 1 else 14
OUT = Path(os.environ.get('LEC05_CHUNK_DIR', '/tmp/lec05-chunks')); OUT.mkdir(parents=True, exist_ok=True)
total = len(B.ORDER)
for ci, start in enumerate(range(0, total, CHUNK), start=1):
    part = B.ORDER[start:start + CHUNK]
    p = setup_pres()
    for fn in part:
        fn(p)
    for i, slide in enumerate(p.slides, start=start + 1):
        page_number(slide, i, total)
    f = OUT / f"part-{ci:02d}.pptx"
    p.save(str(f))
    print(f"{f} — slides {start+1}..{start+len(part)}")
