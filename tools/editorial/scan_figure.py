#!/usr/bin/env python3
"""scan_figure.py — замер оборотов сопоставления по СОБРАННОЙ деке.

Зачем отдельный инструмент, если есть греп. У деки курса видимый слой слайда
захардкожен в `rendered/slides_band*.py`, и текст там разрезан на строковые
литералы. Оборот, переехавший через перенос строки, грепом по исходнику не
ловится вовсе: на зоне `slides_band1.py` Лекции 5 исходник дал 6 находок, а
собранная дека на тех же тринадцати слайдах — 7 головных плюс 16 хвостовых.
Греп по `.py` годится, чтобы найти, где править; он не годится, чтобы
отчитаться, сколько осталось (`tools/editorial/README.md`).

Видимый слой и заметки докладчика считаются ОТДЕЛЬНО и намеренно. Это две
разные работы: на экране фигура часто несущая — заголовок, построенный на
честном противопоставлении, бывает сильнее любой замены, — а в заметках,
которые суть проза, она почти всегда машинный шов. Сводить их в одно число
значит потерять, какая работа осталась.

Шаблоны — из канона (`tools/editorial/README.md`), с обязательной границей
слова: без `\\b` шаблон ловит хвост любого слова на «-не» («на стороне, а
хук…»), и отрицания в такой фразе нет. На Семинаре 5 мусором оказалась почти
четверть находок.

Использование:
    python3 tools/editorial/scan_figure.py library/lectures/lec-05/rendered/lec-05.pptx
    python3 tools/editorial/scan_figure.py <pptx> --show        # с цитатами
    python3 tools/editorial/scan_figure.py <pptx> --slides 1-13  # по диапазону

Код возврата всегда 0: это измеритель, а не гейт. Порога «сколько допустимо»
не существует — остаток решается чтением, потому что часть оборотов несёт
само содержание (цитаты, формулировки заданий, инструкции из двух терминов).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS = {
    "головное «не X, а Y»": re.compile(r"\bне\b[^,.;:!?]{2,45},\s+а\s+", re.I),
    "хвостовое «…, а не …»": re.compile(r",\s+а\s+не\b", re.I),
    "«дело не в»": re.compile(r"\bдело\s+не\s+в\b", re.I),
    "«с одной стороны»": re.compile(r"\bс\s+одной\s+стороны\b", re.I),
}


def parse_slides(spec: str | None, total: int) -> set[int]:
    if not spec:
        return set(range(1, total + 1))
    out: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def extract(pptx: Path):
    """[(номер слайда, видимый текст, текст заметок)] в порядке показа."""
    try:
        from pptx import Presentation
    except ImportError:
        sys.exit(
            "нужен python-pptx: PYTHONPATH=/home/harness/harness-control-data/"
            "accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/"
            "site-packages"
        )
    pres = Presentation(str(pptx))
    rows = []
    for i, slide in enumerate(pres.slides, start=1):
        body = "\n".join(
            sh.text_frame.text for sh in slide.shapes if sh.has_text_frame
        )
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text
        rows.append((i, body, notes))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pptx", type=Path)
    ap.add_argument("--slides", help="например 1-13 или 4,7,9-12")
    ap.add_argument("--show", action="store_true", help="печатать сами находки")
    args = ap.parse_args()

    if not args.pptx.exists():
        sys.exit(f"нет файла: {args.pptx}")

    rows = extract(args.pptx)
    wanted = parse_slides(args.slides, len(rows))
    rows = [r for r in rows if r[0] in wanted]

    layers = {"видимый слой": 1, "заметки докладчика": 2}
    print(f"{args.pptx.name} — слайдов в замере: {len(rows)} из {len(extract(args.pptx))}\n")

    for layer_name, idx in layers.items():
        words = sum(len(r[idx].split()) for r in rows)
        print(f"── {layer_name} ── {words} слов")
        for label, rx in PATTERNS.items():
            hits = [(r[0], m.group(0)) for r in rows for m in rx.finditer(r[idx])]
            per_k = len(hits) / words * 1000 if words else 0.0
            print(f"   {label:28} {len(hits):4}   {per_k:5.2f} на 1000 слов")
            if args.show and hits:
                for num, frag in hits:
                    print(f"        слайд {num:2}: …{frag.strip()}…")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
