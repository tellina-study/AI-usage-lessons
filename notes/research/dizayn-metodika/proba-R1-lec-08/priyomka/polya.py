# -*- coding: utf-8 -*-
"""ПЕРЕНЕСЕНО → `tools/presentation-build/promah_polya.py` (порог 1.14; две копии разошлись бы).

Эта обёртка оставлена, чтобы прежняя команда продолжала работать; считающего
кода здесь нет. Шапка нового места содержит таблицу замера, обоснование порога
и ПРОВЕРЕННУЮ ПРОГОНОМ оговорку: таблица порога снята прежней меркой по одной
кромке, а код считает по обеим — числа Лекции 6 и Лекции 7 ею не проходят.

Запуск:  python3 polya.py <файл.pptx> [ещё.pptx ...]
"""
import runpy
import sys
from pathlib import Path

NOVOE_MESTO = (Path(__file__).resolve().parents[5]
               / "tools" / "presentation-build" / "promah_polya.py")
print(f"→ {NOVOE_MESTO}", file=sys.stderr)
runpy.run_path(str(NOVOE_MESTO), run_name="__main__")
