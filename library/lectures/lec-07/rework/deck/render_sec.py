#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Рендер ОДНОГО-ТРЁХ разделов деки + замер страницы так, как её видит зал.

Зачем отдельно от `render_parts.py`: тот собирает всю деку (107 кадров, часами
и под риском упереться в память — `notes/mcp-limitations.md` [#229-2]). Сессии,
которая правит три раздела, нужен свой кусок и число по нему.

ЭТОТ ПРОГОН НЕ ПОКАЗЫВАЕТ ПРЕДУПРЕЖДЕНИЙ СБОРКИ — НИ НА КАКОМ ВХОДЕ.
Он оборачивает каждую сборку в `report.snapshot()` / `report.restore()`
(см. ниже) и `report.blocking()` не зовёт вовсе: его дело — замер слов, а
не приёмка. Молчание здесь не значит «предупреждений нет», и сказано это
вслух потому, что на нём уже ошиблись: сессия Входа прочла молчание этого
прогона как «сборка дала ноль предупреждений», объявила дефектом сторож
высоты и отправила на его поиски сессию ядра. Сторож работал — на том
входе он давал `[высота] 9,06" > 5,72"`, просто показать его было некому.
Блокирующие берут отдельной сборкой: `python3 build_lec07.py --only sNN`.

Замер идёт по СОБРАННОМУ PDF, а не по файлу кадра: плашки, столбцы, подписи
схем и подвал лежат во фронтматтере, и счёт по разделу «Видимый текст слайда»
их не видит — на этом ошиблись дважды (замер оркестратора 112 против 183 по
PDF). Норма круга #229: медиана ≤ 90 слов на страницу, ни одной тяжелее 140.

    python3 render_sec.py 1 2 3            # собрать и замерить
    python3 render_sec.py 1 --zamer        # замерить готовый PDF, не собирая
"""
import argparse
import re
import statistics
import subprocess
import sys
from pathlib import Path

import yaml

import build_lec07 as B
from deckkit import render as rnd, report, slidefile

HERE = Path(__file__).resolve().parent
PARTS = HERE / "parts-sec"


def ids_of(secs):
    out = []
    for f in slidefile.slide_files(B.SLIDES_DIR):
        m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        meta = yaml.safe_load(m.group(1)) if m else {}
        sec = str((meta or {}).get("section") or "")
        if sec.split(".")[0] in secs:
            out.append((f.name.split("-")[0], f.name))
    return out


def zamer(pdf, names=None):
    import fitz
    d = fitz.open(pdf)
    v = [len(p.get_text().split()) for p in d]
    for i, n in enumerate(v):
        label = names[i][1] if names and i < len(names) else f"стр.{i + 1}"
        flag = "  ← тяжелее 140" if n > 140 else ""
        print(f"{n:4d}  {label}{flag}")
    print(f"\nстраниц {len(v)} · медиана {statistics.median(v):g} · "
          f"среднее {statistics.mean(v):.0f} · максимум {max(v)} · "
          f"тяжелее 140 — {sum(1 for x in v if x > 140)} · "
          f"тяжелее 90 — {sum(1 for x in v if x > 90)}")
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("secs", nargs="+")
    ap.add_argument("--zamer", action="store_true", help="не собирать заново")
    ap.add_argument("--size", type=int, default=15)
    ap.add_argument("--timeout", type=int, default=560)
    a = ap.parse_args()

    pairs = ids_of(set(a.secs))
    if not pairs:
        print("кадров не найдено")
        return 1
    tag = "-".join(sorted(a.secs))
    out_pdf = HERE / f"sec-{tag}.pdf"

    if not a.zamer:
        PARTS.mkdir(exist_ok=True)
        pdfs = []
        ids = [i for i, _ in pairs]
        for k in range(0, len(ids), a.size):
            part = ids[k:k + a.size]
            out = PARTS / f"sec{tag}-{k // a.size + 1:02d}.pptx"
            keep = report.snapshot()
            B.build(only=",".join(part), out=out)
            report.restore(keep)
            if rnd.render(out, PARTS / f"snaps{tag}-{k // a.size + 1:02d}",
                          timeout=a.timeout):
                print(f"кусок {k // a.size + 1}: рендер не вышел")
                return 1
            pdfs.append(str(out.with_suffix(".pdf")))
            print(f"кусок {k // a.size + 1}: {len(part)} кадров готово")
        r = subprocess.run(
            ["bash", "-lc",
             ". /home/harness/.local/lo-portable-env.sh && "
             f"pdfunite {' '.join(pdfs)} '{out_pdf.absolute()}'"],
            timeout=180, capture_output=True, text=True)
        if r.returncode:
            print(f"склейка: код {r.returncode}\n{r.stderr[-400:]}")
            return 1
        print(f"склеено: {out_pdf}\n")

    zamer(out_pdf, pairs)
    print("\nПредупреждений сборки этот прогон не показывает — ни одного, "
          "ни на каком входе:\nэто замер слов, а не приёмка. Блокирующие "
          "берут отдельной сборкой\n(`python3 build_lec07.py --only sNN`) "
          "либо сводом `python3 priyomka.py`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
