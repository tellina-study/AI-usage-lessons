#!/usr/bin/env python3
"""Текст, наехавший на ТЕКСТ, — класс, которого не видит ни одна проверка деки.

Зачем отдельный файл. `check_tracks_pdf.py` сверяет строки с РАМКАМИ ФИГУР: он
ловит фигуру, которая режет текст, и строку, вылезшую за дно залитой карточки.
Текст поверх текста он пропускает по построению — там нет фигуры, там две
надписи. Сборочные сторожа (`ПЕРЕПОЛНЕНИЕ`, `ШИРЕ РАМКИ`) меряют каждый блок
поодиночке и про соседей не знают вовсе. До сих пор этот класс искали глазами,
и в круге 4 это сказано прямо.

Два разных дефекта, и мерить их надо по-разному.

* НАЛОЖЕНИЕ — две надписи встали в одно место: рамки перекрыты и по ширине, и
  по высоте БОЛЬШЕ ЧЕМ НАПОЛОВИНУ. Так выглядит только настоящее столкновение.
* СЛИПЛИСЬ — строки идут стопкой (перекрытие по высоте небольшое), но шаг стал
  плотнее, чем позволяют чернила.

Почему «стопкой» решается ГЕОМЕТРИЕЙ, а не принадлежностью к блоку PDF. Первая
версия этой проверки спрашивала у `pymupdf`, лежат ли строки в одном блоке, и
считала одноблочные соседними строками абзаца. Блок `pymupdf` — не абзац: он
сгребает в себя соседние по месту куски из разных колонок и ячеек. На этой деке
такая версия выдала 90 находок, из них настоящих ноль — она сортировала по
высоте ячейки разных столбцов и объявляла «шагом» расстояние между словами
«Скилл» и «инструкций», стоящими в разных колонках таблицы. Признак блока
выброшен целиком; остались только рамки строк, которые ни от какой группировки
не зависят.

Почему перекрытие рамок само по себе не дефект. Рамка строки у Liberation Sans
≈ 1,117 кегля (выносные вверх и вниз), поэтому ЛЮБОЙ межстрочный плотнее этого
даёт формальное пересечение рамок, ничего при этом не задевая: между нижней
выносной одной строки и верхней следующей лежит пустота. Замерено на этой деке:
заголовки дивайдеров идут межстрочным 1,05 при кегле 34 — рамки пересекаются на
2,2 pt, а на картинке строки стоят чисто и с запасом. Правило «любое пересечение
рамок есть дефект» объявило бы дефектными все шесть дивайдеров деки и не нашло
бы сверх того ничего.

    python3 check_text_overlap_pdf.py /tmp/out/sem-05.pdf
    python3 check_text_overlap_pdf.py --self-test

Код возврата 1, если что-то найдено.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent

CROSS_TOL = 1.0     # pt — ниже этого пересечение считаем кромкой отрисовки
STACK_FRAC = 0.5    # доля высоты строки: перекрытие больше — надписи в одном
                    # месте, меньше — строки идут стопкой
INK_RATIO = 0.95    # доля кегля: шаг плотнее — свои строки задевают друг друга


def lines_of(page):
    """[(рамка, кегль, текст)] — только непустые строки. Индекс блока НЕ
    возвращается намеренно: см. преамбулу, на нём проверка уже один раз
    сломалась."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if txt:
                out.append((ln["bbox"], ln["spans"][0]["size"], txt))
    return out


def check_page(page, pno):
    msgs = []
    lines = lines_of(page)
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            (ax0, ay0, ax1, ay1), sa, ta = lines[i]
            (bx0, by0, bx1, by1), sb, tb = lines[j]
            ox = min(ax1, bx1) - max(ax0, bx0)
            oy = min(ay1, by1) - max(ay0, by0)
            if ox <= CROSS_TOL or oy <= CROSS_TOL:
                continue                      # не пересекаются — не наш случай
            hmin = min(ay1 - ay0, by1 - by0)
            if hmin <= 0:
                continue
            if oy > hmin * STACK_FRAC:
                msgs.append(
                    f"НАЛОЖЕНИЕ [стр. {pno}]: «{ta[:28]}» и «{tb[:28]}» перекрыты "
                    f"на {ox:.1f}×{oy:.1f} pt ({oy / hmin:.0%} высоты строки) — "
                    f"это две надписи в одном месте")
                continue
            # строки идут стопкой: дефект не в самом перекрытии, а в шаге
            top, bot = (ay0, by0) if ay0 <= by0 else (by0, ay0)
            size = sa if ay0 <= by0 else sb
            pitch = bot - top
            if size > 0 and pitch < size * INK_RATIO:
                msgs.append(
                    f"СЛИПЛИСЬ [стр. {pno}]: «{ta[:26]}» / «{tb[:26]}» — шаг "
                    f"{pitch:.1f} pt при кегле {size:.1f} ({pitch / size:.2f} кегля, "
                    f"порог {INK_RATIO}); выносные задевают следующую строку")
    return msgs


def check(pdf_path, pages=None):
    doc = pymupdf.open(pdf_path)
    want = set(pages) if pages is not None else None
    msgs = []
    for i, page in enumerate(doc):
        if want is not None and i not in want:
            continue
        msgs += check_page(page, i + 1)
    doc.close()
    return sorted(set(msgs))


# ── Самопроверка на нарочно сломанном входе ─────────────────────────────────
#
# Четыре пробы, по паре на каждое сообщение. Годные пробы здесь важнее
# сломанных: проверка, которая ругается на дивайдер с межстрочным 1,05,
# закроет собой настоящие находки — она уже «нашла» бы шесть штук на этой деке.

def _probe(out_pptx, *, kind):
    from pptx import Presentation as P
    from pptx.util import Inches
    sys.path.insert(0, str(HERE))
    import deck_kit as K
    prs = P()
    prs.slide_width, prs.slide_height = Inches(K.W_IN), Inches(K.H_IN)
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    K.set_bg(sl, K.WHITE)
    if kind == "cross_broken":
        # две отдельные надписи на одном месте
        K.text_box(sl, 1.0, 1.0, 6.0, 0.5, "Первая надпись этой пробы", size=20)
        K.text_box(sl, 1.4, 1.0, 6.0, 0.5, "Вторая надпись этой пробы", size=20)
    elif kind == "cross_clean":
        K.text_box(sl, 1.0, 1.0, 6.0, 0.5, "Первая надпись этой пробы", size=20)
        K.text_box(sl, 1.0, 2.0, 6.0, 0.5, "Вторая надпись этой пробы", size=20)
    elif kind == "ink_broken":
        # шаг 0,80 кегля — выносные заходят на следующую строку
        K.text_box(sl, 1.0, 1.0, 6.0, 3.0,
                   [f"Строка пробы номер {i}" for i in (1, 2, 3, 4)],
                   size=20, spacing=0.80)
    elif kind == "ink_clean":
        # 1,05 — ровно тот межстрочный, которым набраны дивайдеры деки
        K.text_box(sl, 1.0, 1.0, 6.0, 3.0,
                   [f"Строка пробы номер {i}" for i in (1, 2, 3, 4)],
                   size=20, spacing=1.05)
    prs.save(out_pptx)


def self_test():
    script = HERE.parents[3] / "tools" / "presentation-build" / "pptx_to_png.sh"
    cases = (("чужие налезли: две надписи на месте одной", "cross_broken", True, "НАЛОЖЕНИЕ"),
             ("чужие врозь: надписи на разной высоте", "cross_clean", False, "НАЛОЖЕНИЕ"),
             ("свои слиплись: межстрочный 0,80", "ink_broken", True, "СЛИПЛИСЬ"),
             ("свои чисто: межстрочный 1,05 (как дивайдеры)", "ink_clean", False, "СЛИПЛИСЬ"))
    ok = True
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        for name, kind, want_hit, msg_kind in cases:
            pptx = d / f"probe-{kind}.pptx"
            _probe(str(pptx), kind=kind)
            subprocess.run([str(script), str(pptx), str(d), "150", "1", "1"],
                           check=True, capture_output=True)
            msgs = [m for m in check(str(pptx.with_suffix(".pdf")), pages=[0])
                    if m.startswith(msg_kind)]
            hit = bool(msgs)
            ok = ok and hit == want_hit
            mark = "✓" if hit == want_hit else "✗ ПРОВЕРКА МЁРТВАЯ"
            print(f"{mark} {name:44} → {msgs[0][:74] if msgs else 'чисто'}")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--self-test":
        return self_test()
    msgs = check(args[0], [int(x) - 1 for x in args[1:]] or None)
    for m in msgs:
        print("⚠", m)
    print(f"— наложений текста на текст: {len(msgs)}")
    return 1 if msgs else 0


if __name__ == "__main__":
    sys.exit(main())
