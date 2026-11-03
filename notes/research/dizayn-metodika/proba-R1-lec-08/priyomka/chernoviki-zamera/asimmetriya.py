# -*- coding: utf-8 -*-
"""ПЕРЕНЕСЕНО → `tools/presentation-build/asimmetriya_kadra.py` (две копии разошлись бы).

Эта обёртка оставлена, чтобы прежняя команда продолжала работать; считающего
кода здесь нет. Три НЕУДАЧНЫХ показателя этой папки (`1-kraya.py`,
`2-drozh.py`, `3-polosy.py`) и первая редакция рабочего (`4-otstupy.py`)
никуда не переносятся: они ценны как запись неудачи — см. `README.md` рядом.

Запуск:  python3 asimmetriya.py <файл.pptx> [ещё.pptx ...]
"""
import runpy
import sys
from pathlib import Path

NOVOE_MESTO = (Path(__file__).resolve().parents[6]
               / "tools" / "presentation-build" / "asimmetriya_kadra.py")
print(f"→ {NOVOE_MESTO}", file=sys.stderr)
runpy.run_path(str(NOVOE_MESTO), run_name="__main__")
