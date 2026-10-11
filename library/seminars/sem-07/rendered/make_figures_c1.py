#!/usr/bin/env python3
"""Схемы кейса A ступени 1 Семинара 7 — граф цепочки и тот же граф с погасшей
проверкой.

    c1-graf-tsepochki.png        механика: письмо → classify → ◇проверка → draft
                                 → очередь человека → клиент; ветка «нет» уводит
                                 письмо человеку целиком
    c1-graf-pogasshiy-romb.png   тот же граф, ромб погашен: проверки нет, метка
                                 идёт дальше, ответ уходит клиенту

**Почему две схемы рисует одна функция.** Второй экран обязан читаться как ПЕРВЫЙ
с одним снятым узлом — полсекунды на опознание разницы, не построчное сличение
двух картинок. Единственный способ это гарантировать — одна геометрия на обе:
`graph(dead=…)` рисует те же координаты, те же коробки и те же стрелки, а
`dead=True` меняет только состояние ромба, цвет пути и три подписи. Разъехаться
они не могут, потому что второй копии координат не существует.

Холст 1600×520 px. 1600 px = 12,23″ рабочей ширины слайда (та же мерка, что в
`sem-06/rendered/make_figures_*.py`), то есть 130,8 px·дюйм⁻¹; пол кегля деки
7,5 pt = 13,6 px, минимальный кегль здесь 19 px ≈ 10,5 pt — с запасом. Пропорция
3,08:1 выбрана под слайд, где кроме схемы стоит ещё таблица: `deck_kit.figure`
ужимает схему ЦЕЛИКОМ, когда высоты не хватает, и широкая схема переживает это
без предупреждения «СХЕМА ЗАЖАТА».

Запуск: `python3 make_figures_c1.py` (из `rendered/`).
"""
from fig_toolkit import *

CW, CH = 1600, 520

R1 = 118        # ось первого ряда
R2 = 312        # ось второго ряда
DEAD = GREY_FILL
DEADTX = GREY_TX


def rect(d, x1, y1, x2, y2, *, fill=SURF, stroke=LIGHT, w=3, r=14):
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill, outline=stroke, width=w)


def oval(d, x1, y1, x2, y2, *, fill=MID, stroke=None, w=3):
    d.ellipse([x1, y1, x2, y2], fill=fill, outline=stroke, width=w)


def diamond(d, cx, cy, hw, hh, *, fill=WARM, stroke=GOLD, w=6):
    d.polygon([(cx, cy - hh), (cx + hw, cy), (cx, cy + hh), (cx - hw, cy)],
              fill=fill, outline=stroke, width=w)


def two_lines(d, cx, cy, top, bottom, *, tsz=26, bsz=19, tcol=W, bcol=W, tb=True):
    """Имя узла и под ним пояснение — по центру коробки."""
    ft, fb = f(tsz, tb), f(bsz)
    th = tsz + bsz + 10
    y = cy - th / 2
    d.text((cx - d.textlength(top, font=ft) / 2, y), top, font=ft, fill=tcol)
    d.text((cx - d.textlength(bottom, font=fb) / 2, y + tsz + 8), bottom, font=fb, fill=bcol)


def strike(d, x, y, txt, fo, col, dash=False):
    d.text((x, y), txt, font=fo, fill=col)
    w = d.textlength(txt, font=fo)
    d.line([x - 3, y + fo.size * 0.62, x + w + 3, y + fo.size * 0.62], fill=col, width=3)


def graph(dead):
    """Один граф на две схемы. `dead=True` — проверка снята."""
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)

    path = RED if dead else MID          # цвет пути, по которому идёт письмо
    gate_fill = DEAD if dead else WARM
    gate_line = DEADTX if dead else GOLD
    gate_tx = DEADTX if dead else GOLDINK

    # ── ряд 1: письмо → classify → проверка → (нет) человеку целиком ────────
    rect(d, 24, R1 - 45, 214, R1 + 45)
    two_lines(d, 119, R1, "письмо", "от клиента", tsz=25, bsz=18, tcol=DEEP, bcol=MUTE)

    oval(d, 282, R1 - 46, 542, R1 + 46, fill=MID)
    two_lines(d, 412, R1, "classify", "вернуть метку", tsz=26, bsz=19)

    diamond(d, 768, R1, 170, 78, fill=gate_fill, stroke=gate_line)
    # Крест рисуется ДО подписи: иначе он ложится поверх букв, и зал читает
    # «что-то зачёркнуто» вместо «зачёркнута ПРОВЕРКА МЕТКИ» — пропадает ровно
    # то слово, ради которого экран стоит в деке.
    if dead:
        # Крест рисуется во всю ширину ромба, подложка закрывает его середину:
        # остаются четыре луча по углам и читаемая подпись между ними. Без
        # подложки крест проходит сквозь буквы, и зал видит «что-то зачёркнуто»
        # вместо «зачёркнута ПРОВЕРКА МЕТКИ». Сама подпись при этом тоже
        # перечёркнута — одной тонкой линией на слово.
        xmark(d, 768, R1, 74, col=RED, wd=8)
        d.rectangle([768 - 114, R1 - 34, 768 + 114, R1 + 32], fill=DEAD)
    for i, word in enumerate(("метка", "в списке?")):
        y = R1 - 28 + i * 30
        clabel(d, 768, y, word, 22, gate_tx, True, where=f"ромб {i + 1}", limit=210)
        if dead:
            half = d.textlength(word, font=f(22, True)) / 2
            d.line([768 - half - 4, y + 14, 768 + half + 4, y + 14], fill=RED, width=3)

    rect(d, 1196, R1 - 45, 1576, R1 + 45,
         fill=DEAD if dead else SURF, stroke=DEADTX if dead else LIGHT)
    two_lines(d, 1386, R1, "человеку целиком", "разбирает письмо сам",
              tsz=24, bsz=18,
              tcol=DEADTX if dead else DEEP, bcol=DEADTX if dead else MUTE)

    arrow(d, 214, R1, 274, R1, col=path)
    arrow(d, 542, R1, 592, R1, col=path)
    arrow(d, 944, R1, 1188, R1, col=DEADTX if dead else LIGHT, dash=dead)
    clabel(d, 1066, R1 - 36, "нет", 21, DEADTX if dead else LIGHT, True, where="ветка нет")
    if dead:
        clabel(d, 1066, R1 + 14, "эта ветка молчит", 19, DEADTX, where="ветка мертва")

    # ── вниз, во второй ряд ─────────────────────────────────────────────────
    arrow(d, 768, R1 + 78, 768, R2 - 46, col=path)
    d.text((786, R1 + 96), "да" if not dead else "без проверки",
           font=f(21, True), fill=path)
    if dead:
        d.text((786, R1 + 122), "«другое» идёт дальше", font=f(19), fill=RED)

    # ── ряд 2: draft → очередь человека → клиент ────────────────────────────
    oval(d, 560, R2 - 46, 950, R2 + 46, fill=MID)
    two_lines(d, 755, R2, "draft", "письмо + метка + база знаний", tsz=26, bsz=19)

    rect(d, 1010, R2 - 45, 1310, R2 + 45,
         fill=DEAD if dead else SURF, stroke=DEADTX if dead else LIGHT)
    two_lines(d, 1160, R2, "очередь человека",
              "подтверждают не читая" if dead else "подтвердить или поправить",
              tsz=23, bsz=17,
              tcol=DEADTX if dead else DEEP, bcol=RED if dead else MUTE)

    rect(d, 1370, R2 - 45, 1576, R2 + 45,
         fill=W, stroke=RED if dead else LIGHT)
    two_lines(d, 1473, R2, "клиент", "получает ответ", tsz=25, bsz=18,
              tcol=RED if dead else DEEP, bcol=RED if dead else MUTE)

    arrow(d, 950, R2, 1002, R2, col=path)
    arrow(d, 1310, R2, 1362, R2, col=path)

    # ── подвал: ромб одной строкой кода ─────────────────────────────────────
    rect(d, 24, R2 - 42, 520, R2 + 42, fill=SURF, stroke=DEADTX if dead else LIGHT, w=2)
    d.text((46, R2 - 28),
           "строки проверки нет:" if dead else "ромб — одна строка кода:",
           font=f(20, True), fill=RED if dead else DEEP)
    code = "if label not in ALLOWED: stop()"
    fo = f(19, False, True)
    if dead:
        strike(d, 46, R2 + 4, code, fo, DEADTX)
    else:
        d.text((46, R2 + 4), code, font=fo, fill=MID)

    if dead:
        clabel(d, 1473, R2 + 62, "ответ без решения", 19, RED, True, where="цена 1")
        clabel(d, 1473, R2 + 86, "ушёл как есть", 19, RED, where="цена 2")

    # ── легенда ─────────────────────────────────────────────────────────────
    ly = 452
    oval(d, 30, ly - 17, 92, ly + 17, fill=MID)
    d.text((104, ly - 13), "овал — вызов модели", font=f(20), fill=DEEP)
    rect(d, 400, ly - 17, 462, ly + 17, r=8)
    d.text((474, ly - 13), "прямоугольник — код", font=f(20), fill=DEEP)
    diamond(d, 800, ly, 36, 19, fill=WARM, stroke=GOLD, w=4)
    d.text((848, ly - 13), "ромб — проверка без модели", font=f(20), fill=DEEP)
    if dead:
        d.text((1240, ly - 13), "серое — не работает", font=f(20, True), fill=DEADTX)

    return im


save(graph(False), "c1-graf-tsepochki.png")
save(graph(True), "c1-graf-pogasshiy-romb.png")
report()
