#!/usr/bin/env python3
"""Сверка СОБРАННОГО pptx с тем, что на самом деле нарисовал LibreOffice.

Зачем. Вёрстка ставит фигуру под текстовый блок на высоту, посчитанную
`metrics`. `metrics.line_h` считает межстрочный как долю КЕГЛЯ (18 pt × 1.30 =
23.4 pt), а `python-pptx` пишет в файл `line_spacing` вещественным числом, и
LibreOffice с PowerPoint понимают его как долю СОБСТВЕННОЙ высоты строки
шрифта. Замерено на этой деке: 28.0 pt против 23.4 — строка рисуется на 19.7%
выше мерки. Ошибка копится по строкам, и первой её ловит та фигура, которую
ставят вплотную под текст: ряд пилюль-терминов под базой в приёме
`base_and_edge`.

Почему не хватает того, что уже есть. `qa_preview.py` рисует картинку САМ, по
той же мерке, которой верстали, — расхождения с LibreOffice он не видит по
построению. Сборочные сторожа (`ПЕРЕПОЛНЕНИЕ`, `НА ДНЕ КЕГЛЯ`, `ШИРЕ РАМКИ`)
меряют тем же `metrics`. На `n46` все они молчали, а пилюли резали последнюю
строку базы на 4,8 pt.

Эта проверка не меряет текст — она СМОТРИТ в PDF, который выдал LibreOffice, и
сравнивает нарисованные строки с рамками фигур из pptx.

    python3 check_tracks_pdf.py sem-05.pptx /tmp/out/sem-05.pdf 47 48 49
    python3 check_tracks_pdf.py --self-test      # прогон на сломанном входе

`РЕЖЕТ` — фигура пересекает строку текста ЧАСТИЧНО. Плашка, внутри которой
текст лежит целиком, — штатная форма и не считается.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf
from pptx import Presentation
from pptx.enum.dml import MSO_FILL

HERE = Path(__file__).resolve().parent
EMU_PT = 12700.0
CUT_TOL = 0.75          # pt — ниже этого пересечение считаем кромкой отрисовки
OWN_TOL = 4.0           # pt — на столько строка вправе вылезти за СВОЮ рамку
                        # и остаться своей. Из-за той же недомерки строка
                        # вылезает за собственную рамку: вправо до 1.3 pt
                        # (n46, правая дорожка) и вверх до 2.1 pt (n09, плашка).
                        # С допуском 0.75 владелец не опознавался, и каждая
                        # такая строка приходила ложным «РЕЖЕТ».


def shapes_of(pptx_path, want=None):
    prs = Presentation(pptx_path)
    out = {}
    for i, sl in enumerate(prs.slides):
        if want is not None and i not in want:
            continue
        rows = []
        for sh in sl.shapes:
            try:
                l, t = sh.left / EMU_PT, sh.top / EMU_PT
                w, h = sh.width / EMU_PT, sh.height / EMU_PT
            except TypeError:
                continue
            try:
                solid = sh.fill.type == MSO_FILL.SOLID
            except (AttributeError, TypeError, NotImplementedError):
                solid = False
            rows.append((l, t, l + w, t + h, solid))
        out[i] = rows
    return out


def lines_of(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if txt:
                out.append((ln["bbox"], txt, ln["spans"][0]["size"]))
    return out


def cuts(shape, line_bbox):
    """Насколько фигура ПЕРЕСЕКАЕТ строку, не будучи её собственной рамкой.

    Признак владения — фигура НАЧИНАЕТСЯ не ниже строки и накрывает её по
    ширине. Нижнюю границу в признак не берём намеренно: из-за недомерки
    последний ряд вылезает за дно своей рамки почти целиком (замерено: рамка
    кончается на 1.3 pt ниже верха последней строки), и по условию «рамка
    содержит строку» владелец переставал опознаваться. Фигуру, которую ставят
    ПОД текст, от собственной рамки отличает именно верх: пилюли на пробе
    начинаются на 11 pt ниже верха строки, которую режут.
    """
    sl, st, sr, sb = shape[:4]
    lx0, ly0, lx1, ly1 = line_bbox
    ov_x = min(sr, lx1) - max(sl, lx0)
    ov_y = min(sb, ly1) - max(st, ly0)
    if ov_x <= 0 or ov_y <= CUT_TOL:
        return 0.0
    owns = (sl <= lx0 + OWN_TOL and sr >= lx1 - OWN_TOL
            and st <= ly0 + OWN_TOL)
    return 0.0 if owns else ov_y


def spills(shape, line_bbox):
    """Строка ВЫВАЛИЛАСЬ за дно ЗАЛИТОЙ карточки, которая её содержит.

    Отдельное сообщение, а не разновидность `РЕЖЕТ`: здесь никто ни на кого не
    налезает — карточка просто кончается выше своего текста, и последняя строка
    печатается тёмным по белому за её краем. Для незалитой рамки это не дефект
    (её не видно), поэтому проверка ограничена заливкой.
    """
    sl, st, sr, sb, solid = shape
    lx0, ly0, lx1, ly1 = line_bbox
    if not solid:
        return 0.0
    # Содержит — значит строка НАЧИНАЕТСЯ внутри фигуры. Без условия `sb`
    # контейнером оказывалась и планка в 3.6 pt над дорожкой: она шире ярлыка
    # и стоит выше него, и ярлык «вываливался» из неё на всю свою высоту.
    starts_inside = st <= ly0 + OWN_TOL and sb >= ly0 + CUT_TOL
    owns = sl <= lx0 + OWN_TOL and sr >= lx1 - OWN_TOL and starts_inside
    return (ly1 - sb) if owns and ly1 - sb > CUT_TOL else 0.0


def check(pptx_path, pdf_path, pages=None):
    doc = pymupdf.open(pdf_path)
    want = set(pages) if pages is not None else None
    msgs = []
    for i, shapes in sorted(shapes_of(pptx_path, want).items()):
        if i >= doc.page_count:
            continue
        for bbox, txt, _size in lines_of(doc[i]):
            for s in shapes:
                ov = cuts(s, bbox)
                if ov:
                    msgs.append(f"РЕЖЕТ [стр. {i + 1}]: фигура (верх {s[1]:.1f} pt) "
                                f"заходит на строку «{txt[:34]}» на {ov:.1f} pt")
                out = spills(s, bbox)
                if out:
                    msgs.append(f"ВЫВАЛИЛСЯ [стр. {i + 1}]: строка «{txt[:34]}» "
                                f"на {out:.1f} pt ниже дна залитой карточки")
    doc.close()
    return sorted(set(msgs))


def measured_pitch(pdf_path, page_index, size_pt):
    """Реальный шаг строки для кегля `size_pt` — то, чем калибруют `metrics`."""
    doc = pymupdf.open(pdf_path)
    tops = sorted(b[0][1] for b in lines_of(doc[page_index])
                  if abs(b[2] - size_pt) < 0.1)
    doc.close()
    steps = [b - a for a, b in zip(tops, tops[1:]) if 0 < b - a < size_pt * 3]
    return min(steps) if steps else None


# ── Самопроверка на нарочно сломанном входе ─────────────────────────────────
#
# Приём `base_and_edge` ставит пилюли под базу. Длинная база (пять строк) —
# сломанный вход: ошибка мерки накапливается, и пилюли режут последний ряд.
# Короткая (три строки) — годный. Проверка, которая молчит на первом,
# бесполезна; проверка, которая ругается на втором, — тоже.

BROKEN = """# Проба

## Visual

| База | Кромка |
|---|---|
| Описание — текст, который вставляется в системный промпт агента; по нему и делается выбор. Тело файла не читается, пока выбор не сделан: до срабатывания в контексте лежат только имя и описание. | У перечня есть бюджет — **1% окна модели**. Когда он переполнен, среда отнимает описания, начиная с тех скиллов, которые вызывают реже всего. |

`описание` · `бюджет перечня` · `урезание`
"""

CLEAN = BROKEN.replace(
    "Описание — текст, который вставляется в системный промпт агента; по нему и "
    "делается выбор. Тело файла не читается, пока выбор не сделан: до "
    "срабатывания в контексте лежат только имя и описание.",
    "В системный промпт агента уходят имя и описание — по ним и делается выбор. "
    "Тела файла до срабатывания там нет.")


CARD_BROKEN = """# Проба карточки

## Visual

```
перечень скиллов этой сессии, как его видит модель:

build-deck: build-deck
catalog-docs: catalog-docs
compile-wiki: compile-wiki
diagram-refresh: diagram-refresh
        … ещё восемь строк ровно такого же вида …
pre-user-gate: Pre-USER-GATE walkthrough — orchestrator self-review
               before presenting GATE to user.
update-lecture: update-lecture
```
"""

CARD_CLEAN = """# Проба карточки

## Visual

```
перечень скиллов этой сессии:
build-deck: build-deck
catalog-docs: catalog-docs
```
"""


def _build_probe(md, out_pptx):
    from pptx import Presentation as P
    from pptx.util import Inches
    import build_sem05 as B
    import deck_kit as K
    import slide_parts as SP
    prs = P()
    prs.slide_width, prs.slide_height = Inches(K.W_IN), Inches(K.H_IN)
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    title, assertion, visual, _ = SP.sections(md)
    blocks = SP.blocks(visual)
    if any(k == "table" for k, _ in blocks):
        B.g_base_edge(sl, "s08", title, blocks, "base_and_edge", assertion)
    else:
        B.g_content(sl, "s07", title, blocks, "problem_scenario", assertion)
    prs.save(out_pptx)


def self_test():
    sys.path.insert(0, str(HERE))
    script = HERE.parents[3] / "tools" / "presentation-build" / "pptx_to_png.sh"
    ok = True
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        cases = (("пилюли режут: база в 5 строк", BROKEN, True, "РЕЖЕТ"),
                 ("пилюли чисто: база в 3 строки", CLEAN, False, "РЕЖЕТ"),
                 ("карточка мала: листинг 10 строк", CARD_BROKEN, True, "ВЫВАЛИЛСЯ"),
                 ("карточка впору: листинг 3 строки", CARD_CLEAN, False, "ВЫВАЛИЛСЯ"))
        for name, md, want_hit, kind in cases:
            pptx = d / (f"probe-{abs(hash(name)) % 10000}.pptx")
            _build_probe(md, str(pptx))
            subprocess.run([str(script), str(pptx), str(d), "150", "1", "1"],
                           check=True, capture_output=True)
            msgs = [m for m in check(str(pptx), str(pptx.with_suffix(".pdf")),
                                     pages=[0]) if m.startswith(kind)]
            hit = bool(msgs)
            mark = "✓" if hit == want_hit else "✗ ПРОВЕРКА МЁРТВАЯ"
            ok = ok and hit == want_hit
            print(f"{mark} {name:34} → {msgs[0] if msgs else 'чисто'}")
            if want_hit and kind == "РЕЖЕТ":
                import metrics as M
                import deck_kit as K
                p = measured_pitch(str(pptx.with_suffix(".pdf")), 0, 18.0)
                est = M.line_h(18, K.TRACK_SPACING) * 72
                print(f"   мерка {est:.1f} pt против нарисованных {p:.1f} pt "
                      f"— расхождение {(p / est - 1) * 100:.1f}%")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--self-test":
        return self_test()
    pptx, pdf = args[0], args[1]
    pages = [int(x) - 1 for x in args[2:]] or None
    msgs = check(pptx, pdf, pages)
    for m in msgs:
        print("⚠", m)
    print(f"— фигур, режущих текст: {len(msgs)}")
    return 1 if msgs else 0


if __name__ == "__main__":
    sys.exit(main())
