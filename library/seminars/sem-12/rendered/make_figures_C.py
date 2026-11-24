#!/usr/bin/env python3
"""Программная схема Кейса C Семинара 12 («Определение запрещённого»).
Тулкит — общий `tools/seminar-build/fig_toolkit.py` (canon
`tools/seminar-production/README.md` §7), по образцу `make_figures_B.py`
этого же занятия — рисовалка обслуживает только слайды Кейса C
(`slides/n40-n53`), слайды других кейсов пишут параллельные сессии своими
рисовалками, этот файл их не трогает.

Одна фигура:

    case-c-shema-postanovka.png  n43 — схема С1: сплошное — загрузка и
                                  описание (Кейс B, уже собрано); пунктирное
                                  золотое — премодерация: три флага (этот
                                  кейс строит); серым, за контуром —
                                  публикация/отложено до человека.

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_C.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403


def case_c_shema_postanovka():
    im = Image.new("RGB", (1700, 500), W)
    d = ImageDraw.Draw(im)
    head(d, "Узел, который строит этот кейс: можно публиковать?", sz=30)
    d.text((40, 64),
            "снимок уже загружен и описан — вопрос в том, можно ли его публиковать",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    box(d, 40, y1, 420, h1, ["Загрузка + описание", "Кейс B, уже собрано"], SURF,
        tc=DEEP, sz=20, outline=LIGHT, where="узел-описание")
    arrow(d, 460, y1 + h1 / 2, 550, y1 + h1 / 2, col=LIGHT, wd=4)

    box(d, 550, y1, 560, h1, ["Премодерация: три флага", "курение · еда/напитки · слайды"], W,
        tc=DEEP, sz=19, outline=GOLD, where="узел-премодерация")
    arrow(d, 1110, y1 + h1 / 2, 1200, y1 + h1 / 2, col=GOLD, wd=4, dash=True)

    box(d, 1200, y1, 460, h1,
        ["Публикация", "или отложено до человека"], SOFT_GREY,
        tc=GREY_TX, sz=20, outline=GREY_FILL, where="узел-исход")

    save(im, "case-c-shema-postanovka.png")


if __name__ == "__main__":
    case_c_shema_postanovka()
    if WARN:
        print("WARN:", *WARN, sep="\n  ")
    report()
