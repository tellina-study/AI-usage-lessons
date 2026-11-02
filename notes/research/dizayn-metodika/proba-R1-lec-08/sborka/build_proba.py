#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Тонкая обёртка над `build_lec07.build()` для пробы методики вёрстки на
ПРОИЗВОЛЬНОМ каталоге кадров (issue проба R1, notes/research/dizayn-metodika/
proba-R1-lec-08/). Не свой сборщик — импорт + вызов + CLI. Своя логика
раскладки, разбор YAML и примитивы здесь НЕ пишутся: всё это уже есть в
`build_lec07.py` и в пакете `deckkit`, которые эта обёртка только зовёт.

Каталог кадров этой пробы — `kadry/` рядом (не `library/lectures/lec-07/
rework/deck/slides/`), выпуск — `rendered/proba-R1.pptx`.

Запуск:
    python3 build_proba.py                 # только PPTX
    python3 build_proba.py --render         # ещё PDF + PNG-снимки
    python3 build_proba.py --only s01,s02   # частичная сборка (свой файл)
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # .../proba-R1-lec-08/sborka
PROBA_ROOT = HERE.parent                                # .../proba-R1-lec-08
KADRY_DIR = PROBA_ROOT / "kadry"
RENDERED_DIR = PROBA_ROOT / "rendered"
OUT_PPTX = RENDERED_DIR / "proba-R1.pptx"
OUT_PPTX_ONLY = RENDERED_DIR / "proba-R1-chastichnaya.pptx"
SNAPS_DIR = RENDERED_DIR / "snapshots"

# repo root: .../proba-R1-lec-08/sborka -> proba-R1-lec-08 -> dizayn-metodika
# -> research -> notes -> <repo root>
REPO_ROOT = HERE.parents[4]
LEC07_DECK = REPO_ROOT / "library" / "lectures" / "lec-07" / "rework" / "deck"

# `build_lec07.py` живёт как модуль верхнего уровня (его собственные
# внутренние импорты — `from selftest_lec07 import selftest` — так его и
# ищут). Сам он при импорте добавляет `tools/presentation-build` в sys.path
# (через свой собственный `HERE.parents[4]`), поэтому `deckkit` становится
# доступен сразу после `import build_lec07` — отдельно добавлять его в
# sys.path здесь не нужно и не делается, чтобы не задваивать чужую логику.
sys.path.insert(0, str(LEC07_DECK))

from build_lec07 import build  # noqa: E402  (чужой модуль верхнего уровня)

from deckkit import floor as deckkit_floor  # noqa: E402
from deckkit import render as rnd  # noqa: E402
from deckkit import report as deckkit_report  # noqa: E402
from deckkit import slidefile as deckkit_slidefile  # noqa: E402


def adapt_imena_kadrov(prefix="r1"):
    """Даёт читателю кадров увидеть имена `<prefix>-NN-*.md` — НАХОДКА ПРОБЫ,
    а не улучшение.

    Разнарядка (`03-RAZNARYADKA.md` §1, столбец «кадр») называет файлы
    кадров `r1-01-divider` … `r1-16-karta`. Исполнить это имя дословно
    доступным ядром НЕЛЬЗЯ, и ровно по двум причинам, обе в
    `deckkit.slidefile.slide_files`:

    1. каталог кадров глобится `s*.md` — ни один файл на `r1-` в него не
       попадает, и сборка молча насчитывает НОЛЬ кадров (о чём шапка этой
       же обёртки предупреждает в `--only`);
    2. номер кадра берётся из имени файла до ПЕРВОГО дефиса
       (`f.name.split("-")[0]`) — у всех шестнадцати это одно и то же `r1`,
       то есть они сложились бы в одну группу «шестнадцать файлов на один
       номер», и в деку пошёл бы ОДИН.

    Переименовать файлы под `sNN-` значило бы не исполнить разнарядку;
    править `deckkit` — трогать общий пакет двух сданных дек. Поэтому
    подмена ровно читателя файлов и ровно на этот прогон, тем же приёмом
    и по той же причине, что `raise_floor` выше подменяет `floor.VIS_PT`:
    порядок кадров — по ИМЕНИ файла, номер кадра — из поля `id`
    фронтматтера (`read_slide` и так читает его оттуда, см. `sl.sid`).
    Своей раскладки, своего разбора YAML и своих примитивов здесь
    по-прежнему нет.
    """
    old = deckkit_slidefile.slide_files

    def slide_files(slides_dir, only=None):
        files = sorted(Path(slides_dir).glob(f"{prefix}-*.md"), key=lambda f: f.name)
        if not files:                      # каталог не этой пробы — чужой читатель
            return old(slides_dir, only)
        if only:
            want = {x.strip() for x in str(only).split(",") if x.strip()}
            files = [f for f in files
                     if f.name in want or f.stem in want
                     or "-".join(f.stem.split("-")[:2]) in want]
        return files

    deckkit_slidefile.slide_files = slide_files
    print(f"читатель кадров подменён обёрткой: имена `{prefix}-NN-*.md` вместо "
          "`sNN-*.md` (см. `adapt_imena_kadrov`)")


def raise_floor(new_vis_pt=15.0, old_vis_pt=12.0):
    """Поднимает `deckkit.floor.VIS_PT` ПЕРЕД сборкой — решение владельца
    2026-10-29. Порог читается модулями `plates`/`tables`/`columns`/…
    В МОМЕНТ ВЫЗОВА `floor.pt(...)` (через `_floor(given)`, см. `floor.py`),
    а не защёлкивается при импорте — значит присваивание атрибуту модуля
    ДО вызова `build()` действует на весь этот прогон. Печатает замеренное
    значение до и после, а не просто «присвоил», потому что сама обёртка
    не доверяет чтению кода без исполнения."""
    before = deckkit_floor.VIS_PT
    deckkit_floor.VIS_PT = new_vis_pt
    after = deckkit_floor.VIS_PT
    if after == new_vis_pt and before == old_vis_pt:
        print(f"пол кегля поднят обёрткой: {before:.1f} → {after:.1f} пт "
              "(решение владельца 2026-10-29)")
    elif after == new_vis_pt:
        print(f"пол кегля поднят обёрткой: было {before:.1f} (НЕ {old_vis_pt:.1f}, "
              f"как ожидалось) → {after:.1f} пт")
    else:
        print(f"ПОДНЯТЬ ПОЛ НЕ УДАЛОСЬ: после присвоения `deckkit_floor.VIS_PT = "
              f"{new_vis_pt}` модуль всё равно отдаёт {after:.1f} пт — значит кто-то "
              "захватил значение по себе, а не читает атрибут модуля в момент "
              "вызова; обходить это не через `deckkit`, а записать в отчёт честно")
    return before, after


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--render", action="store_true",
                     help="после сборки PPTX сделать PDF + PNG-снимки")
    ap.add_argument("--only", default=None,
                     help="список id через запятую, напр. s01,s02 — ВНИМАНИЕ: "
                          "`deckkit.slidefile.slide_files` жёстко глобит "
                          "`s*.md` и фильтрует по ИМЕНИ ФАЙЛА до первого "
                          "дефиса, не по полю `id` фронтматтера — файлы кадров "
                          "обязаны начинаться на `s`, иначе соберётся 0 кадров")
    ap.add_argument("--krug", default="r1", choices=("r1", "r2"),
                    help="какой круг пробы собирать: r1 (каталог kadry/) "
                         "или r2 (каталог kadry-r2/, переделка по потолку)")
    ap.add_argument("--vis-pt", type=float, default=15.0,
                     help="новый пол кегля видимого слоя (по умолчанию 15.0)")
    a = ap.parse_args()

    RENDERED_DIR.mkdir(parents=True, exist_ok=True)
    krug = a.krug
    kadry_dir = KADRY_DIR if krug == "r1" else PROBA_ROOT / "kadry-r2"
    out_pptx = RENDERED_DIR / f"proba-{krug.upper()}.pptx"
    out_only = RENDERED_DIR / f"proba-{krug.upper()}-chastichnaya.pptx"
    snaps_dir = RENDERED_DIR / ("snapshots" if krug == "r1" else "snapshots-r2")
    snaps_dir.mkdir(parents=True, exist_ok=True)

    adapt_imena_kadrov(prefix=krug)
    before, after = raise_floor(new_vis_pt=a.vis_pt)

    out = out_pptx if not a.only else out_only
    n = build(only=a.only, out=out, slides_dir=kadry_dir, root=PROBA_ROOT)
    if a.only:
        print(f"[частичная сборка] выпуск {out_pptx.name} НЕ ТРОНУТ")

    # Полный отчёт (предупреждения, в т.ч. `[кегль]`) — та же функция,
    # которую зовёт `build_lec07.main()`, не свой пересказ.
    deckkit_report.report(n, out.name)

    # Те же проверки, что в `build_lec07.main()`: по СОХРАНЁННОМУ файлу.
    rnd.verify_built(out, partial=True)
    rnd.verify_links(out)

    if a.render:
        code = rnd.render(out, snaps_dir)
        if code:
            print(f"рендер вернул код {code} — PDF/PNG могли не получиться")
            return code
    return 0


if __name__ == "__main__":
    sys.exit(main())
