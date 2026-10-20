#!/usr/bin/env python3
"""Схема шва С7→С8 — n02 Семинара 8 (issue #274): входное состояние,
унаследованное с прошлого занятия, напечатанное КАК ЕСТЬ.

**СУПЕРСЕДИРОВАНО голосовой правкой владельца 2026-10-20 (issue #274):**
n02 больше не использует эту программную схему — владелец явно попросил
вместо «страшненькой» программной схемы настоящий скриншот из n8n, который
уже есть в репозитории. Нашёлся: `sem-07/rendered/figures/obzor-k1.png` —
реальный, аннотированный снимок живого холста процесса классификации
(тот же процесс, вход которого описывает эта схема), скопирован в
`sem-08/rendered/figures/shov-s7-obzor-klassifikatsii.png` и используется
слайдом `slides/n02-shov-s7-s8.md` напрямую. Эта рисовалка и её вывод
(`shov-s7-s8.png`) оставлены в репозитории как задокументированная история
(программная схема была верной и честной — просто владелец предпочёл
настоящий скрин), не как действующий источник фигуры n02.

    shov-s7-s8.png   форма → извлечение (+ модель) → справочник → строка →
                     экран, плюс ветка отказа: повтор на узле извлечения →
                     отдельная строка «не разобрано» → отдельный экран.

Это ТОЧКА СТАРТА, не решение: на этой схеме нет ни одного узла, которого
не было бы на стенде Семинара 7 к концу занятия. Геометрия, подписи и
цвета — ПОБУКВЕННО та же схема, что уже стоит на выходном слайде
Семинара 7 (`sem-07/rendered/make_figures_s7.py`, функция `protsess`,
стадии 3–4 — шесть узлов успешного пути плюс ветка отказа), без строки
«Боевые прогоны идут по опубликованной версии»: это утверждение о
публикации, а не о составе процесса, и на n02 (ARCHITECTURE.md §2, шов)
речи о публикации нет ни в assertion, ни в speaker notes — только о том,
что никто ничего не трогал с прошлого занятия.

Источник состава узлов — `sem-07/stend/student.json` (узлы `form` →
`extract`+`model` → `vocab` → запись → экран, плюс `retryOnFail`/
`maxTries: 3` на `extract` и вторая ветка на `status = not_parsed`),
подтверждено прямым чтением файла, не пересказом.

Правило «чужая папка семинара не правится» не даёт импортировать
`make_figures_s7.py` из sem-07 отсюда — рисовалка скопирована СВОИМ
файлом в `sem-08/rendered/`, геометрия и текст те же.

Запуск: `python3 make_figures_n02.py` (из `rendered/` папки Семинара 8).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

CW = 1600
ROW = 150
NH = 54


def node(d, cx, cy, w, top, bottom, *, fill=SURF, stroke=LIGHT, tcol=DEEP,
         bcol=MUTE, tsz=26, bsz=19, wd=3, where="узел", num=None):
    """Узел процесса — тот же вид, что на всех схемах курса (один взгляд —
    один язык): прямоугольник со скруглением, имя и пояснение под ним,
    номер шага в кружке у левого верхнего угла."""
    d.rounded_rectangle([cx - w / 2, cy - NH, cx + w / 2, cy + NH], radius=14,
                        fill=fill, outline=stroke, width=wd)
    if num is not None:
        bx, by, r = cx - w / 2, cy - NH, 17
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=stroke, outline=W, width=3)
        clabel(d, bx, by - 11, str(num), 21, W, True, where=f"номер {num}")
    ft, fb = f(tsz, True), f(bsz)
    th = tsz + bsz + 9
    y = cy - th / 2
    clabel(d, cx, y, top, tsz, tcol, True, where=where, limit=w - 24)
    if bottom:
        clabel(d, cx, y + tsz + 7, bottom, bsz, bcol, where=where + "-низ", limit=w - 20)


def trig(d, cx, cy, w, top, bottom, **kw):
    """Триггер — тот же узел золотым контуром: начало процесса видно по
    цвету, без отдельной формы и без подписи «это триггер»."""
    kw.setdefault("stroke", GOLD)
    kw.setdefault("fill", WARM)
    kw.setdefault("wd", 5)
    node(d, cx, cy, w, top, bottom, **kw)


def canvas(h=420):
    im = Image.new("RGB", (CW, h), W)
    return im, ImageDraw.Draw(im)


def legend(d, y, items):
    """Легенда одной строкой: образец — подпись, образец — подпись."""
    x = 34
    for kind, txt in items:
        if kind == "trig":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=WARM, outline=GOLD, width=4)
        elif kind == "vocab":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=W, outline=GOLD, width=3)
        elif kind == "node":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=SURF, outline=LIGHT, width=3)
        elif kind == "err":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=W, outline=RED, width=3)
        x += 70
        d.text((x, y - 13), T(txt), font=f(20), fill=DEEP)
        x += d.textlength(T(txt), font=f(20)) + 54


def shov():
    """Входное состояние С7→С8: шесть узлов успешного пути плюс ветка
    отказа. Побуквенно геометрия и текст `protsess(stage=3/4)` из
    `sem-07/rendered/make_figures_s7.py`, минус строка о публикации."""
    h = 500
    im, d = canvas(h)
    row = 150

    trig(d, 150, row, 250, T("форма"), T("заявка с сайта"), num=1)
    node(d, 470, row, 330, T("извлечение"), T("схема с перечислением"),
         stroke=TEAL, wd=4, where="извлечение", num=2)
    node(d, 470, row + 150, 300, T("модель"), T("подключена к шагу"),
         stroke=TEAL, wd=3, tsz=23, bsz=18, where="модель", num=3)
    d.line([470, row + NH, 470, row + 150 - 42], fill=TEAL, width=4)
    node(d, 820, row, 300, T("справочник"), T("не из списка → «другое»"),
         stroke=GOLD, fill=WARM, wd=4, tcol=DEEP, where="справочник", num=4)
    node(d, 1140, row, 280, T("строка"), T("в таблице"), where="строка", num=5)
    node(d, 1450, row, 260, T("экран"), T("результата"),
         stroke=TEAL, wd=4, where="экран", num=6)
    for x1, x2 in ((275, 300), (635, 665), (970, 995), (1280, 1315)):
        arrow(d, x1, row, x2, row, col=MID)

    err_row = row + 180
    node(d, 820, err_row, 330, T("строка «не разобрано»"), T("status = not_parsed"), tsz=22,
         stroke=RED, fill=W, tcol=DEEP, where="ветка отказа")
    node(d, 1250, err_row, 300, T("экран"), T("«не разобрана»"),
         stroke=RED, fill=W, tcol=DEEP, where="экран отказа")
    arrow(d, 985, err_row, 1095, err_row, col=RED)
    arrow(d, 290, row, 290, err_row, col=RED)
    arrow(d, 290, err_row, 650, err_row, col=RED)
    clabel(d, 700, row - 42, T("успех"), 21, MID, True, where="метка успеха")
    clabel(d, 290, row + 96, T("отказ"), 21, RED, True, where="метка отказа")
    d.rounded_rectangle([305, row - NH - 84, 635, row - NH - 24], radius=10,
                        fill=WARM, outline=GOLD, width=3)
    clabel(d, 470, row - NH - 74, T("повтор: 3 попытки"), 21, GOLDINK, True,
           where="плашка повтора", limit=310)

    items = [("trig", "триггер"), ("node", "шаг"), ("vocab", "сверка со списком"),
             ("err", "ветка отказа")]
    legend(d, h - 26, items)

    save(im, "shov-s7-s8.png")


def main():
    import sys
    if "--lang" in sys.argv:
        set_lang(sys.argv[sys.argv.index("--lang") + 1])
    shov()
    report()


if __name__ == "__main__":
    main()
