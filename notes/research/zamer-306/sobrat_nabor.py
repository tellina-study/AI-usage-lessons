#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Прогон ОДНОГО набора замера #306 через настоящую сборку.

    python3 sobrat_nabor.py nabor-1
    python3 sobrat_nabor.py nabor-1 nabor-2 nabor-3 nabor-4

Для каждого набора: собирает `s01..s05-kadrN.md` из `nabor-N/` настоящим
`build_lec07.build()`, печатает ВСЕ предупреждения сборки, рендерит PDF и
PNG тем же прогоном, которым собираются деки курса (`deckkit.render`), и
прогоняет `nalozhenie_bbox.py` по собранному PDF. Числа — только отсюда,
не с исходников (см. `CLAUDE.md` § измерение по собранному).

Пишет также `nabor-N/nabor-N.pdf` — артефакт для слепой оценки владельца
(без заголовка набора на кадрах, без меток происхождения).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/harness/harness-projects/256/.worktrees/folder-288/session-0b2adb13-7ee7af40")
DECK_DIR = REPO / "library" / "lectures" / "lec-07" / "rework" / "deck"
PB_DIR = REPO / "tools" / "presentation-build"
ZAMER_DIR = REPO / "notes" / "research" / "zamer-306"

sys.path.insert(0, str(PB_DIR))
sys.path.insert(0, str(DECK_DIR))


def sobrat(nabor):
    import build_lec07 as b
    from deckkit import render as rnd
    from deckkit import report

    sd = ZAMER_DIR / nabor
    out_pptx = sd / f"{nabor}.pptx"
    report.reset()
    n = b.build(only=None, out=out_pptx, slides_dir=sd)
    warnings = list(report.WARNINGS)
    blocking = [w for w in warnings if w.startswith(report.BLOCKING)]
    other = [w for w in warnings if not w.startswith(report.BLOCKING)]

    print(f"\n{'=' * 70}\n{nabor}: собрано кадров {n} → {out_pptx.name}")
    print(f"блокирующих: {len(blocking)} · прочих: {len(other)}")
    for w in warnings:
        print("  " + w)

    rc = rnd.render(out_pptx, sd / "snaps", dpi=150)
    overlaps = None
    if rc == 0:
        pdf = out_pptx.with_suffix(".pdf")
        r = subprocess.run(
            [sys.executable, str(PB_DIR / "nalozhenie_bbox.py"), str(pdf)],
            capture_output=True, text=True)
        print(r.stdout)
        if r.stderr:
            print(r.stderr, file=sys.stderr)
        for line in r.stdout.splitlines():
            if line.strip().startswith("страниц"):
                # "страниц 5 · наложений 2 · порог ..."
                try:
                    overlaps = int(line.split("наложений")[1].split("·")[0].strip())
                except Exception:
                    overlaps = None
    else:
        print(f"{nabor}: рендер не вышел (код {rc}) — наложения не измерены")

    result = {
        "nabor": nabor,
        "kadrov": n,
        "blokiruyushchikh": len(blocking),
        "prochikh": len(other),
        "warnings": warnings,
        "nalozheniy": overlaps,
    }
    (sd / "otchet-sborki.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    naborees = sys.argv[1:] or ["nabor-1", "nabor-2", "nabor-3", "nabor-4"]
    all_res = []
    for nb in naborees:
        all_res.append(sobrat(nb))
    print("\n\n" + "=" * 70 + "\nСВОДКА\n" + "=" * 70)
    for r in all_res:
        print(f"{r['nabor']}: кадров {r['kadrov']} · блокирующих "
              f"{r['blokiruyushchikh']} · прочих {r['prochikh']} · "
              f"наложений {r['nalozheniy']}")
