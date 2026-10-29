#!/usr/bin/env python3
"""Схема постановки Кейса 4 — `k4-shema-postanovka.png`.

ПЕРЕПИСАНА ЦЕЛИКОМ 2026-10-29 (issue #303): кейс переопределён владельцем, прежняя
схема («ход процесса защищён кодом, аргумент решения — нет», сравнение суммы с
порогом) описывала СНЯТУЮ постановку и больше не подходит ни одному слайду. Старое
название файла (`k4-shema-upravlenie-dannye.png`) тоже снято вместе с ним — чтобы
устаревшая картинка не осталась лежать рядом с новым текстом слайда и не уехала в
сборку по случайному совпадению имени (находка П4 сверки волны 2, та же ошибка
другим путём).

Правило С1 канона (`tools/seminar-production/README.md` §3.1): сплошными линиями —
то, что в процессе уже есть, пунктиром — то, что этот кейс строит и меряет.

  СПЛОШНОЕ — заявка на возврат приходит, решающая модель читает её текст вместе со
             списком клиентов и правилом «в базе и курс не старше 30 дней», выдаёт
             одно из трёх решений.
  ПУНКТИР  — защитный слой: механическая проверка и классификатор встают ДО модели
             (две карточки на пунктирной рамке), усиление промта встроено В САМ
             вызов модели (пунктирная стрелка внутрь карточки модели).

Числа замера на схеме нет ни одного — такты результата (n49–n52) вскрывают их
отдельно; слой постановки объясняет устройство, не исход.

Запуск: `python3 make_figures_k4.py` (из `rendered/`).
"""
from make_figures_common import *

H = 760
ROW1_Y, ROW1_H = 150, 190   # сплошной поток: заявка -> модель -> решение
ROW2_Y, ROW2_H = 420, 230   # пунктирный слой защиты


def postanovka():
    im = Image.new("RGB", (CW, H), W)
    d = ImageDraw.Draw(im)
    txt(d, 60, 14, "Куда встаёт защита от инъекции", 34, MID, b=True,
        limit=CW - 120, where="заголовок")
    txt(d, 60, 62, "решение о возврате принимает модель — защита встаёт до неё или "
        "внутри самого вызова", 26, LIGHT, limit=CW - 120, where="подзаголовок")

    # ── верхний поток: что уже есть, сплошное ───────────────────────────────
    cy1 = ROW1_Y + ROW1_H / 2
    node(d, 60, ROW1_Y, 460, ROW1_H, "Заявка на возврат",
         "текст клиента + ФИО", tsz=30, stroke=TEAL, where="шаг 1")
    node(d, 620, ROW1_Y, 620, ROW1_H, "Решающая модель",
         "читает текст заявки + список клиентов + правило «30 дней»",
         tsz=30, stroke=TEAL, where="шаг 2")
    card(d, 1340, ROW1_Y, 1000, ROW1_H, fill=W, stroke=GOLD, sw=6)
    ctxt(d, 1840, ROW1_Y + 40, "Решение", 32, DEEP, b=True, limit=940,
         where="шаг 3 · название")
    wrapped(d, 1366, ROW1_Y + 96, "возврат / отказ / менеджер", 27, GOLD,
            948, center=1840, where="шаг 3 · варианты")

    for x1, x2 in ((520, 620), (1240, 1340)):
        arrow(d, x1, cy1, x2, cy1, col=TEAL, wd=5)

    # ── нижний слой: что строим и меряем в этом кейсе, пунктир ──────────────
    card(d, 60, ROW2_Y, 1620, ROW2_H, fill=SURF, stroke=GOLD, sw=4)
    ctxt(d, 870, ROW2_Y + 24, "Защита — пунктиром, этот кейс её строит и меряет",
         29, DEEP, b=True, limit=1560, where="слой защиты · название")

    card(d, 110, ROW2_Y + 76, 480, 130, fill=W, stroke=TEAL, sw=4)
    ctxt(d, 350, ROW2_Y + 96, "Механическая проверка", 26, DEEP, b=True,
         limit=440, where="защита 1 · название")
    wrapped(d, 130, ROW2_Y + 136, "регулярные выражения, до модели", 24, LIGHT,
            440, center=350, where="защита 1 · пояснение")

    card(d, 630, ROW2_Y + 76, 480, 130, fill=W, stroke=TEAL, sw=4)
    ctxt(d, 870, ROW2_Y + 96, "Классификатор на входе", 26, DEEP, b=True,
         limit=440, where="защита 2 · название")
    wrapped(d, 650, ROW2_Y + 136, "отдельная дешёвая модель, до решающей", 24,
            LIGHT, 440, center=870, where="защита 2 · пояснение")

    card(d, 1150, ROW2_Y + 76, 480, 130, fill=W, stroke=TEAL, sw=4)
    ctxt(d, 1390, ROW2_Y + 96, "Усиление промта", 26, DEEP, b=True, limit=440,
         where="защита 3 · название")
    wrapped(d, 1170, ROW2_Y + 136, "инструкция внутри самого вызова модели", 24,
            LIGHT, 440, center=1390, where="защита 3 · пояснение")

    # Пунктирные стрелки от защит 1 и 2 — в модель (встают ПЕРЕД ней); от
    # защиты 3 — тоже в модель, но подпись называет её другим путём: меняет
    # сам вызов, а не перехватывает заявку до него.
    arrow(d, 350, ROW2_Y + 76, 850, ROW1_Y + ROW1_H, col=GOLD, wd=5, dash=True)
    arrow(d, 870, ROW2_Y + 76, 930, ROW1_Y + ROW1_H, col=GOLD, wd=5, dash=True)
    arrow(d, 1390, ROW2_Y + 76, 1050, ROW1_Y + ROW1_H, col=GOLD, wd=5, dash=True)

    card(d, 1720, ROW2_Y, 620, ROW2_H, fill=W, stroke=LIGHT, sw=4)
    wrapped(d, 1740, ROW2_Y + 24, "Усиление промта переписывает системную "
            "часть запроса решающей модели — без нового узла.", 25, DEEP,
            580, center=2030, where="слой защиты · оговорка")
    wrapped(d, 1740, ROW2_Y + 130, "Механика и классификатор — отдельные "
            "узлы: могут остановить заявку до модели.", 24, LIGHT,
            580, center=2030, where="слой защиты · оговорка 2")

    save(im, "k4-shema-postanovka.png")


H2 = 843
ROWS_Y = (182, 326, 470, 614, 758)   # пять центров строк-листьев, сверху вниз
LEAF_W, LEAF_H = 420, 128
DEC_W, DEC_H = 400, 120


def klassy():
    """Классы корпуса как дерево из трёх признаков — `k4-shema-klassy-dereva.png`.

    Та же таблица пяти классов уже стоит на кадре n48 текстом; дерево
    добавляет то, чего текстовая таблица не показывает, — ПОРЯДОК, в котором
    признак за признаком разводит 64 заявки на пять классов. Числа — те же,
    что в `stend/zamery-k4-novyy/README.md`, раздел «Корпус заявок».
    """
    im = Image.new("RGB", (CW, H2), W)
    d = ImageDraw.Draw(im)
    txt(d, 60, 14, "Как три признака разводят 64 заявки на пять классов", 34,
        MID, b=True, limit=CW - 120, where="заголовок")
    txt(d, 60, 62, "каждый класс отличается от соседнего ровно одним "
        "признаком", 26, LIGHT, limit=CW - 120, where="подзаголовок")

    def leaf(i, letter, count, polozhen):
        cy = ROWS_Y[i]
        x = 1980
        gold = polozhen
        card(d, x, cy - LEAF_H / 2, LEAF_W, LEAF_H, fill=W if gold else SURF,
             stroke=GOLD if gold else LIGHT, sw=5 if gold else 3)
        ctxt(d, x + 90, cy - 34, letter, 44, GOLD if gold else MID, b=True,
             limit=120, where=f"класс {letter} · буква")
        wrapped(d, x + 150, cy - 40, f"{count} заявок", 27,
                DEEP, LEAF_W - 170, where=f"класс {letter} · число")
        wrapped(d, x + 150, cy, "возврат положен" if polozhen else "возврат не положен",
                22, GOLD if gold else LIGHT, LEAF_W - 170,
                where=f"класс {letter} · вердикт")
        return x, cy

    leafs = {}
    leafs["C"] = leaf(0, "C", 8, False)
    leafs["D"] = leaf(1, "D", 20, False)
    leafs["A"] = leaf(2, "A", 12, True)
    leafs["B"] = leaf(3, "B", 10, False)
    leafs["E"] = leaf(4, "E", 14, False)

    def decision(x, cy, text):
        node(d, x, cy - DEC_H / 2, DEC_W, DEC_H, text, "", tsz=26, stroke=TEAL,
             sw=4, where=f"развилка · {text}")
        return x, cy

    def branch(x1, y1, x2, y2, label):
        arrow(d, x1, y1, x2, y2, col=LIGHT, wd=4)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ctxt(d, mx, my - 34, label, 23, DEEP, b=True, limit=140,
             where=f"ветка · {label}")

    # Начало
    sx, sy = 60, 421
    node(d, sx, sy - 70, 220, 140, "64 заявки", "", tsz=28, stroke=GOLD, sw=5,
         where="начало")

    d1x, d1y = decision(380, 421, "Клиент в базе?")
    branch(sx + 220, sy, d1x, d1y, "")

    d2x, d2y = decision(840, 254, "Манипулирует текстом?")
    branch(d1x + DEC_W, d1y - 20, d2x, d2y, "нет")
    branch(d2x + DEC_W, d2y - 72, leafs["C"][0], leafs["C"][1], "нет")
    branch(d2x + DEC_W, d2y + 72, leafs["D"][0], leafs["D"][1], "да")

    d3x, d3y = decision(840, 614, "Курс в последние 30 дней?")
    branch(d1x + DEC_W, d1y + 20, d3x, d3y, "да")
    branch(d3x + DEC_W, d3y - 72, leafs["A"][0], leafs["A"][1], "да")

    d4x, d4y = decision(1400, 686, "Манипулирует текстом?")
    branch(d3x + DEC_W, d3y + 20, d4x, d4y, "нет")
    branch(d4x + DEC_W, d4y - 72, leafs["B"][0], leafs["B"][1], "нет")
    branch(d4x + DEC_W, d4y + 72, leafs["E"][0], leafs["E"][1], "да")

    save(im, "k4-shema-klassy-dereva.png")


def voronka():
    """Кем остановлена атака — воронкой, `k4-shema-voronka-atak.png`.

    Та же Таблица 3 README уже стоит текстом на n50; воронка добавляет то,
    чего таблица не показывает, — ПОСЛЕДОВАТЕЛЬНОСТЬ: заявка проходит узлы
    по очереди, и у каждого узла есть шанс её остановить. Числа — конфигурации
    `0` и `prc`, классы D+E (34 заявки с манипуляцией), README раздел
    «Таблица 3 — чем именно остановлена атака».
    """
    H3 = 560
    im = Image.new("RGB", (CW, H3), W)
    d = ImageDraw.Draw(im)
    txt(d, 60, 14, "34 атаки проходят через слои по очереди", 34, MID, b=True,
        limit=CW - 120, where="заголовок")
    txt(d, 60, 62, "у каждого слоя — свой шанс остановить, до решающей модели "
        "включительно", 26, LIGHT, limit=CW - 120, where="подзаголовок")

    def row(y, title, steps, final_gold):
        ctxt(d, 230, y - 10, title, 27, DEEP, b=True, limit=360,
             where=f"строка · {title}")
        x = 420
        w = 300
        remaining = 34
        # Старт — одинаковый блок «34 атаки» у ОБОИХ рядов (правка владельца,
        # issue #299): без него верхний ряд показывал только «осталось 7» и
        # 27 остановленных исчезали молча, а нижний ряд убыль показывал —
        # ряды были несопоставимы ровно там, где вся суть в их сопоставлении.
        plashka(d, x, y - 60, w, 130, "34", "атаки", tone="base", nsz=46,
                lsz=23, where=f"{title} · старт")
        arrow(d, x + w, y + 5, x + w + 110, y + 5, col=LIGHT, wd=4)
        x += w + 110
        for i, (name, stopped) in enumerate(steps):
            card(d, x, y - 55, w, 120, fill=SURF, stroke=TEAL, sw=3)
            wrapped(d, x + 16, y - 46, name, 22, DEEP, w - 32, center=x + w / 2,
                    where=f"{title} · узел {name}")
            ctxt(d, x + w / 2, y + 4, f"осталось {remaining - stopped}", 23,
                 MID, b=True, limit=w - 24, where=f"{title} · остаток после {name}")
            remaining -= stopped
            x += w + 110
            if i < len(steps) - 1:
                arrow(d, x - 110, y + 5, x, y + 5, col=LIGHT, wd=4)
        arrow(d, x - 110, y + 5, x, y + 5, col=GOLD if final_gold else LIGHT, wd=5)
        plashka(d, x, y - 60, 300, 130, str(remaining), "прошло насквозь",
                nsz=46, lsz=23, tone="glavnoe" if final_gold else "chislo",
                where=f"{title} · итог")

    row(200, "Без единой защиты", [("Решающая модель", 27)], final_gold=False)
    row(400, "Три защиты вместе", [("Механика", 28), ("Классификатор", 1),
                                    ("Решающая модель", 5)], final_gold=True)

    card(d, 60, 480, CW - 120, 66, fill=SURF, stroke=LIGHT, sw=3)
    wrapped(d, 100, 494, "Механика одна останавливает те же 28 атак, что и "
            "в связке со всеми тремя — остальное доделывает сама модель.",
            25, DEEP, CW - 200, center=CW / 2, where="строка вывода")

    save(im, "k4-shema-voronka-atak.png")


if __name__ == "__main__":
    postanovka()
    klassy()
    voronka()
    pt_report("схемы Кейса 4")
    audit_sources()
