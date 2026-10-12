# -*- coding: utf-8 -*-
"""РЕГРЕССИЯ НА ДВУХ ДОСТАВЛЕННЫХ ДЕКАХ — подстановкой ядра, без правки дек.

Что здесь доказывается и как.

Общее ядро обязано дать ТО ЖЕ, что дают действующие сборщики. Обычный способ
это проверить — перевести деку на ядро и посмотреть, — на этапе 1 запрещён:
доставленные деки и их сборщики не правятся вовсе. Поэтому проверка идёт
ПОДСТАНОВКОЙ: действующий сборщик загружается как есть, его собственные
низкоуровневые имена подменяются на имена ядра, дека собирается снова и
сравнивается с доставленным файлом по СОДЕРЖИМОМУ (`regress.py`).

Подстановка — не хитрость, а самая строгая из доступных проверок. Она
прогоняет ядро по НАСТОЯЩИМ входам: 111 файлов кадров Лекции 7 и 101
Лекции 6, со всеми их крайними случаями, которых ни одна проба не выдумает.
Расхождение в любой из 1566 + 2202 фигур выходит наружу.

ЧТО ПОДМЕНЯЕТСЯ (по слоям, снизу вверх):

  мера        `metrics`   — вся, целиком, у обеих дек
  примитивы   `prims`     — фигуры, надписи, картинки, у обеих
  разметка    `markup`    — `**`/`*`, ссылки, заметки, у обеих
  читатель    `slidefile` — у Лекции 7 (у Лекции 6 читатель переплетён с
                            её собственным кешем и разбором подписей)
  таблицы     `tables`    — у Лекции 6 (у Лекции 7 таблиц нет)
  плашки      `plates`    — у обеих, своим набором чисел
  столбцы     `columns`   — у Лекции 7
  кадры       `media`     — у Лекции 7

ЧТО НЕ ПОДМЕНЯЕТСЯ И ПОЧЕМУ — названо здесь, а не умолчано:

* `scheme` у Лекции 7. Ядро взяло схему Лекции 6 (подобранный кегль шага,
  золото на шаге модели, проверка тесного бокса), и это осознанный отказ от
  версии Лекции 7 с фиксированными 11,5 пт. Подставить её значит заведомо
  получить расхождение — то самое, которое перевод Лекции 7 и даст на
  этапе 2. Схема проверена ЧИСЛЕННО на всех схемах Лекции 6
  (`--compare-units`).
* Раскладки кадра (`content` / `cover` / `divider`) и подвал. Это
  раскладка деки, а не ядро: см. `README.md`, раздел «Что остаётся за декой».
* `flow` у Лекции 6. Поток переплетён с её разбором подписей и строкой
  сетки курса; его части (`para_h`, `fit_blocks`, `two_columns`) проверены
  численно тем же `--compare-units`.

Запуск:
    python3 -m deckkit.regress_decks --lec07
    python3 -m deckkit.regress_decks --lec06 --lec06-root <путь к rendered>
    python3 -m deckkit.regress_decks --compare-units --lec06-root <…>
"""
import argparse
import importlib.util
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from . import (markup, media, metrics, plates, prims, regress,
               report, scheme, slidefile, tables)

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent.parent
WORK = Path(os.environ.get("DECKKIT_WORK",
                           Path(os.environ["HOME"]) / "deckkit-work"))
LEC07 = REPO / "library/lectures/lec-07/rework/deck"
# Доставленная (ДО перевода на ядро) дека Лекции 7 берётся из git, а не с
# диска: после перевода сборщик пишет по тому же пути, то есть файл на диске
# — уже результат, а не эталон. `c5e319c3` — последний коммит, тронувший
# артефакт до перевода; сравнение «с самим собой» на нём проверено.
LEC07_REF_COMMIT = "c5e319c3"
LEC07_REF_PATH = "library/lectures/lec-07/rework/deck/lec-07-karkas.pptx"
LEC06_DEFAULT = Path("/tmp/lec06-ref/library/lectures/lec-06/rendered")


def _load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


# ════════════════════════════════════════════════════════════════════
# Лекция 7
# ════════════════════════════════════════════════════════════════════


def _scheme_sids(deck_dir):
    """Кадры, на которых схема ДЕЙСТВИТЕЛЬНО рисуется. Поле `scheme:` стоит
    в 26 файлах, но в девяти оно пустое (`{}`) — считать по гребёнке по
    файлам значило бы записать в разряд 2 девять кадров, которых там нет."""
    out = set()
    for f in slidefile.slide_files(deck_dir / "slides"):
        sl = slidefile.read_slide(f)
        if sl is not None and scheme.scheme_of(sl, scheme.DEFAULT):
            out.add(sl.sid)
    return out


def run_lec07(deck_dir=LEC07, work=WORK):
    """Лекция 7 ПОСЛЕ перевода на ядро (issue #229, этап 2).

    До перевода здесь стояла подстановка: действующий сборщик загружался как
    есть, его низкоуровневые имена подменялись именами ядра, и дека обязана
    была совпасть с доставленной до знака. Эта проверка СДЕЛАЛА свою работу
    и больше не существует — подменять нечего, дека собирается ядром.

    Её место занимает проверка приёмки этапа 2, и она строже, чем «совпало»:
    расхождения с доставленной декой РАЗБИРАЮТСЯ по разрядам, и третьего
    разряда быть не должно.

      разряд 1 — снятие `<p:style>`: тень темы, которую прежний сборщик
                 искал не там, где она лежит (`notes/mcp-limitations.md`
                 [#223-8]). Утверждена владельцем как правка к лучшему;
      разряд 2 — кадры со схемой: ядро взяло схему Лекции 6 (подобранный
                 кегль, одна высота бокса, золото на шаге модели), и это
                 названо заранее в `README.md`;
      разряд 3 — ВСЁ ОСТАЛЬНОЕ. Это дефект перевода, а не его следствие.

    Возвращает число расхождений разряда 3 — то есть ноль на чистом
    переводе."""
    work.mkdir(parents=True, exist_ok=True)
    ref = work / "lec07-delivered.pptx"
    try:
        blob = subprocess.run(
            ["git", "-C", str(REPO), "show",
             f"{LEC07_REF_COMMIT}:{LEC07_REF_PATH}"],
            capture_output=True, check=True, timeout=120).stdout
        ref.write_bytes(blob)
    except Exception as e:                           # noqa: BLE001
        print(f"нет эталона: {LEC07_REF_COMMIT}:{LEC07_REF_PATH} — {e}")
        return 2
    m = _load("b07", deck_dir / "build_lec07.py")
    report.reset()
    tables.reset_caches()
    out = work / "lec07-deckkit.pptx"
    t = time.time()
    n = m.build(out=out)
    dt = time.time() - t
    sch = _scheme_sids(deck_dir)
    sids = [f.name.split("-")[0]
            for f in slidefile.slide_files(deck_dir / "slides")]
    cls = {1: 0, 2: 0, 3: []}
    for where, a, b in regress.compare(regress.fingerprint(ref),
                                      regress.fingerprint(out),
                                      limit=10 ** 9):
        if where.endswith(".p_style"):
            cls[1] += 1
            continue
        mm = re.match(r"\.slides\[(\d+)\]", where)
        sid = sids[int(mm.group(1))] if mm else "?"
        if sid in sch:
            cls[2] += 1
        else:
            cls[3].append((sid, where, a, b))
    print(f"Лекция 7 на ядре: кадров {n}, {dt:.2f} c, блокирующих "
          f"{len(report.blocking())}, всего предупреждений "
          f"{len(report.WARNINGS)}")
    for w in report.WARNINGS[:10]:
        print("   " + w)
    print(f"  разряд 1, снятие тени темы: {cls[1]} фигур")
    print(f"  разряд 2, кадры со схемой ({len(sch)}): {cls[2]} расхождений")
    print(f"  разряд 3, всё остальное: {len(cls[3])}")
    for sid, where, a, b in cls[3][:20]:
        print(f"    {sid} {where}\n        доставлено: {a}\n        на ядре : {b}")
    print("Лекция 7: " + ("ПЕРЕВОД ЧИСТЫЙ — третьего разряда нет"
                          if not cls[3] else "ЕСТЬ ДЕФЕКТ ПЕРЕВОДА"))
    return len(cls[3])


# ════════════════════════════════════════════════════════════════════
# Лекция 6
# ════════════════════════════════════════════════════════════════════


def _ls(kw):
    """Переходник имён: у Лекции 6 межстрочный зовётся `line_spacing`."""
    if "line_spacing" in kw:
        kw["ls"] = kw.pop("line_spacing")
    if kw.get("tag") is None:
        kw["tag"] = ""
    return kw


def patch_lec06(mod):
    """Подменить в сборщике Лекции 6 всё, что ушло в ядро.

    Подменяется модуль ПРИМИТИВОВ (`build_lec06_p1`, он же `mod.b`), который
    сборщик круга 4 держит импортом, — и оттого правка достаёт сразу до всех
    трёх файлов: `build_v4`, `probe_v4` и примитивной половины `p1`."""
    prims.STRIP_THEME_STYLE = True       # у Лекции 6 это и было её правилом
    b, pr = mod.b, mod.pr

    # ── мера ────────────────────────────────────────────────────────
    b.text_w = lambda text, size, bold=False: metrics.text_w(text, size, bold)
    b.n_lines = (lambda text, size, w_in, bold=False:
                 metrics.n_lines(text, size, w_in, bold))
    b._est_height = (lambda text, size, width_in, line_spacing, bold=False:
                     metrics.est_h(text, size, width_in, line_spacing, bold))
    b.LH, b.SAFE = metrics.LH, metrics.SAFE

    def fit_size(text, w, h, *, hi=18.0, lo=11.0, line_spacing=1.22,
                 bold=False, floor=9.0, tag=None):
        return metrics.fit_size(text, w, h, hi=hi, lo=lo, floor=floor,
                                ls=line_spacing, bold=bold, tag=tag or "")
    b.fit_size = fit_size

    # ── примитивы ───────────────────────────────────────────────────
    b.no_shadow = prims.no_shadow
    b.rect = (lambda s, x, y, w, h, fill, *, stroke=None, stroke_pt=0.0,
              radius=False, radius_adj=0.14:
              prims.rect(s, x, y, w, h, fill, stroke=stroke,
                         stroke_pt=stroke_pt, radius=radius,
                         radius_adj=radius_adj))
    b.ocean_box = (lambda s, x, y, w, h, *, fill=None, stroke=None,
                   stroke_pt=1.5, radius_pt=12.0:
                   prims.ocean_box(
                       s, x, y, w, h,
                       **{k: v for k, v in
                          (("fill", fill), ("stroke", stroke)) if v is not None},
                       stroke_pt=stroke_pt, radius_pt=radius_pt))
    b.text_box = (lambda s, x, y, w, h, text, **kw:
                  prims.text_box(s, x, y, w, h, text, **_ls(kw)))
    b.text_runs = (lambda s, x, y, w, h, runs, **kw:
                   prims.text_runs(s, x, y, w, h, runs, **_ls(kw)))
    b.arrow_r = (lambda s, x, y, w, h, fill=None:
                 prims.arrow(s, x, y, w, h, fill if fill is not None
                             else prims.MID))
    b.setup_pres = prims.new_deck
    b.blank = prims.blank
    b.set_bg = prims.set_slide_bg
    b.speaker_notes = prims.speaker_notes
    b.add_image = (lambda s, p, *a, **k:
                   prims.add_image(s, media.norm_image(p, mod.DERIVED),
                                   *a, **k))
    b.add_image_cover = (lambda s, p, *a, **k:
                         prims.add_image_cover(
                             s, media.norm_image(p, mod.DERIVED), *a, **k))

    # ── разметка и ссылки ───────────────────────────────────────────
    b.md_chunks = markup.md_chunks
    b.plain = markup.plain
    b.runs_md = markup.runs_md
    b.bold_head = markup.bold_head
    mod.link_parts = markup.link_parts
    mod.source_parts = markup.source_parts
    mod.short_url = markup.short_url
    mod._abs_url = markup.abs_url
    mod.apply_links = (lambda tb, runs, tag="":
                       prims.apply_links(tb, runs, tag))
    mod.notes_with_links = (lambda slide, text:
                            markup.notes_with_links(slide, text))

    # ── таблицы: целиком из ядра ────────────────────────────────────
    mod._rows = tables.rows_of
    mod.col_words = tables.col_words
    mod.col_min = tables.col_min
    mod.col_want = tables.col_want
    mod.table_widths = tables.table_widths
    mod.tbl_size = tables.tbl_size
    mod.tbl_ok = tables.tbl_ok
    mod._table_geom = tables.table_geom
    mod.check_cols = (lambda table, size, w, tag:
                      tables.check_cols(table, size, w, tag))
    pr.table_geom = tables.table_geom
    pr.draw_table = (lambda s, x, y, table, size, w, tag:
                     tables.draw_table(s, x, y, table, size, w, tag))
    mod.TBL_PAD, mod.TBL_TIGHT = tables.TBL_PAD, tables.TBL_TIGHT
    mod.TBL_FLOOR, mod.TBL_DROP = tables.TBL_FLOOR, tables.TBL_DROP

    # ── плашки, набор «ровно как в доставленной деке» ───────────────
    st = plates.LEC06
    mod.plates_of = lambda md: plates.plates_of(md, st)
    mod.plate_gold = lambda pl: plates.gold_idx(pl, st)
    mod.plate_h = lambda p, pw: plates.plate_h(p, pw, st)
    mod.plates_h = lambda pl, w: plates.plates_h(pl, w, st)
    mod.draw_plates = (lambda s, pl, x, y, w, tag:
                       plates.draw_plates(s, tag, pl, x, y, w, st, tag=tag))

    # Предупреждения ядра дописываются в список сборщика: его отчёт их
    # печатает, и без этого они потерялись бы молча.
    b.WARNINGS = report.WARNINGS
    b.MISSING_MEDIA = report.MISSING_MEDIA
    tables.reset_caches()
    return mod


def run_lec06(rendered=LEC06_DEFAULT, work=WORK):
    rendered = Path(rendered)
    ref = rendered / "lec-06-v4.pptx"
    if not ref.exists():
        print(f"нет доставленного файла {ref} — укажите --lec06-root")
        return 2
    work.mkdir(parents=True, exist_ok=True)
    derived = work / "derived06"
    if not derived.exists():
        import shutil
        src = rendered / "_derived-v4"
        if src.exists():
            shutil.copytree(src, derived, copy_function=shutil.copy2)
        else:
            derived.mkdir(parents=True)
    sys.path.insert(0, str(rendered))
    cwd = os.getcwd()
    os.chdir(rendered)                   # сборщик читает пути от себя
    try:
        mod = _load("b06_sub", rendered / "build_v4.py")
        mod.DERIVED = derived            # производные кадров — НЕ в репозиторий
        patch_lec06(mod)
        report.reset()
        t = time.time()
        sids = mod.all_sids()
        deck, built = mod.build_deck(sids)
        dt = time.time() - t
    finally:
        os.chdir(cwd)
    out = work / "lec06-deckkit.pptx"
    deck.save(str(out))
    print(f"Лекция 6 на ядре: слайдов {len(built)} из {len(sids)}, {dt:.2f} c, "
          f"блокирующих {len(report.blocking())}, всего предупреждений "
          f"{len(report.WARNINGS)}")
    for w in report.WARNINGS[:10]:
        print("   " + w)
    return regress.check(ref, out, label="Лекция 6, ядро против доставленной")


# ════════════════════════════════════════════════════════════════════
# численное сравнение единиц, которые подстановкой не достать
# ════════════════════════════════════════════════════════════════════


def compare_units(rendered=LEC06_DEFAULT):
    """Сравнить ЧИСЛА ядра с числами сборщика там, где подстановка не идёт.

    Это не замена регрессии, а её дополнение в двух местах, которые
    подстановкой не достаются: у Лекции 6 — поток и схема (они переплетены с
    её разбором подписей), у Лекции 7 — ничего, её поток и есть ядро.
    Сравнивается то, от чего зависит геометрия: высота схемы, подобранный
    кегль шага, кегль тела, место разреза на колонки."""
    rendered = Path(rendered)
    sys.path.insert(0, str(rendered))
    cwd = os.getcwd()
    os.chdir(rendered)
    bad = 0
    try:
        mod = _load("b06_units", rendered / "build_v4.py")
        b, pr = mod.b, mod.pr
        sids = mod.all_sids()
        n_sch = n_flow = 0
        for sid in sids:
            md = b.load_slide_md(sid)
            heading, blocks, caps = mod.parse_body(sid)
            w = mod.FULL_W
            sch = mod.scheme_of(md)
            if sch:
                n_sch += 1
                mine = scheme.scheme_h(sch, w, scheme.LEC06)
                his = mod.scheme_h(sch, w)
                if abs(mine - his) > 1e-9:
                    bad += 1
                    print(f"  схема {sid}: ядро {mine:.4f}\" против "
                          f"{his:.4f}\"")
                m_f = scheme.step_size(sch, w, scheme.LEC06)
                h_f = mod._step_size(sch, w)
                if m_f != h_f:
                    bad += 1
                    print(f"  кегль шага {sid}: ядро {m_f} против {h_f}")
            if blocks:
                n_flow += 1
                from . import flow as kflow
                saved = list(b.WARNINGS)
                mine = kflow.fit_blocks(blocks, w, mod.BODY_H, tag=sid)
                his = mod.fit_blocks(blocks, w, mod.BODY_H, tag=sid)
                b.WARNINGS[:] = saved
                if mine != his:
                    bad += 1
                    print(f"  кегль тела {sid}: ядро {mine} против {his}")
                mi = kflow.split_two(blocks, mine, (w - mod.COL_GAP) / 2,
                                     mod.BODY_H)
                hi = mod.split_two(blocks, his, (w - mod.COL_GAP) / 2,
                                   mod.BODY_H)
                if mi != hi:
                    bad += 1
                    print(f"  разрез на колонки {sid}: ядро {mi} против {hi}")
        print(f"численно сверено: схем {n_sch}, тел {n_flow}; расхождений "
              f"{bad}")
    finally:
        os.chdir(cwd)
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--lec07", action="store_true")
    ap.add_argument("--lec06", action="store_true")
    ap.add_argument("--compare-units", action="store_true")
    ap.add_argument("--lec06-root", default=str(LEC06_DEFAULT))
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args(argv)
    rc = 0
    if a.lec07 or a.all:
        rc |= bool(run_lec07())
    if a.lec06 or a.all:
        rc |= bool(run_lec06(a.lec06_root))
    if a.compare_units or a.all:
        rc |= bool(compare_units(a.lec06_root))
    if not (a.lec07 or a.lec06 or a.compare_units or a.all):
        ap.error("нужен хотя бы один из --lec07 / --lec06 / --compare-units "
                 "/ --all")
    return rc


if __name__ == "__main__":
    sys.exit(main())
