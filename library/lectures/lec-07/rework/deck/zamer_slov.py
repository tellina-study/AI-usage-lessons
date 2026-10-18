#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Счёт слов видимого слоя кадра — по файлам кадров, а не по собранному PDF.

Зачем. Требование владельца (2026-10-14, #229) — «очень много текста, надо
сократить в пользу структуры и читаемости» — проверяется числом: медиана
видимого текста на кадр и потолок. Отчёт сборки этого числа не даёт: он считает
кегль и высоту, а не слова, и кадр из восьми плашек по три слова у него выглядит
так же, как абзац на двести.

Видимый слой берётся тем же извлечением, что и проверка запретов
(`scan_deck_visible.visible_lines`) — один источник, чтобы «видимое» в двух
замерах не разъехалось. Markdown-разметка снимается, ссылки сводятся к видимому
тексту, служебные поля фронтматтера не считаются вовсе.

    python3 zamer_slov.py                    # вся дека
    python3 zamer_slov.py --sec 1 2 3        # только эти разделы
    python3 zamer_slov.py --sec 3 --top 10   # самые тяжёлые кадры раздела
"""
import argparse
import re
import statistics
import sys
from pathlib import Path

import yaml

from scan_deck_visible import visible_lines

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"

MD = [
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),    # ссылка → видимый текст
    (re.compile(r"[*_`#>|]+"), " "),                  # разметка
    (re.compile(r"^\s*[-–—]\s*"), " "),               # маркер буллита
]


def words(text):
    for rx, rep in MD:
        text = rx.sub(rep, text)
    return len([w for w in text.split() if re.search(r"[\w\d]", w)])


def section_of(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", raw, re.S)
    if not m:
        return None
    meta = yaml.safe_load(m.group(1)) or {}
    return str(meta.get("section") or "")


def notes_words(path):
    raw = path.read_text(encoding="utf-8")
    m = re.search(r"##\s*Заметки лектора\s*\n(.*?)(?=\n##\s|\Z)", raw, re.S)
    return words(m.group(1)) if m else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sec", nargs="*", default=None, help="номера разделов")
    ap.add_argument("--top", type=int, default=0, help="показать N самых тяжёлых")
    ap.add_argument("--notes", action="store_true", help="колонка заметок")
    a = ap.parse_args()

    rows = []
    for f in sorted(SLIDES.glob("s*.md")):
        sec = section_of(f)
        if sec is None:
            continue
        if a.sec and sec.split(".")[0] not in a.sec:
            continue
        n = sum(words(t) for _, t in visible_lines(f))
        rows.append((n, f.name, sec.split(".")[0], notes_words(f) if a.notes else 0))

    if not rows:
        print("кадров не найдено")
        return 1
    nums = [r[0] for r in rows]
    shown = sorted(rows, reverse=True)[:a.top] if a.top else sorted(rows, key=lambda r: r[1])
    for n, name, sec, nw in shown:
        tail = f"  заметки {nw}" if a.notes else ""
        print(f"{n:4d}  [{sec}]  {name}{tail}")
    print(f"\nкадров {len(nums)} · медиана {statistics.median(nums):g} · "
          f"среднее {statistics.mean(nums):.0f} · максимум {max(nums)} · "
          f">120 слов {sum(1 for n in nums if n > 120)} · "
          f">160 слов {sum(1 for n in nums if n > 160)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
