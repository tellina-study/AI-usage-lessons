#!/usr/bin/env python3
"""Программные схемы Семинара 12, Кейс A («Распознавание документов»),
слайды n10-n23.

Источники чисел и фактов — `stend/zamery-A/README.md` (целиком) и
`stend/zamery-A/zhurnal.md`. Корпус — 30 форм FUNSD `testing_data`
(`stend/zamery-A/korpus/vyborka.json`), не копируется сюда.

    python3 make_figures_a.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent

W_PX = 1700


# ── n12 — схема постановки (правило С1) ─────────────────────────────────────
# Сплошное — поток, уже работающий: заявка приходит сканом, уходит Ольге,
# процесс отвечает. Пунктирная золотая стрелка указывает на узел «извлечь
# значения полей» — единственный шаг, который этот кейс решает заново.
def a_shema_postanovka():
    im = Image.new("RGB", (W_PX, 420), W)
    d = ImageDraw.Draw(im)
    head(d, "Куда в потоке заявки встаёт решение, чем читать поля", sz=26)
    d.text((40, 58),
            "приём скана и передача Ольге уже работают — вопрос в том, чем "
            "вынимать из него значения полей",
            font=f(18), fill=LIGHT)

    y1, h1 = 120, 120
    nodes = [
        ("Заявка приходит сканом", "учебный центр, входящая форма"),
        ("Процесс читает поля", "имя, телефон, дата, число страниц"),
        ("Карточка уходит Ольге", "поля заполнены, заявка в учёте"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=19,
            outline=LIGHT, where=f"постановка-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 290, 110
    goal_w = node_w + 60
    goal_x = xs[1] + node_w / 2 - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Решаем сегодня:", "зрением, распознаванием букв или гибридом"],
        W, tc=DEEP, sz=19, outline=GOLD, where="постановка-цель")
    arrow(d, goal_x + goal_w / 2, y2, xs[1] + node_w / 2, y1 + h1,
          col=GOLD, wd=4, dash=True)

    save(im, "a-shema-postanovka.png")


# ── n15 — механика: скан → тайлы → токены → цена ────────────────────────────
def a_mekhanika():
    im = Image.new("RGB", (W_PX, 440), W)
    d = ImageDraw.Draw(im)
    head(d, "Как читает скан модель-зрение", sz=26)
    d.text((40, 58), "модель: openai/gpt-4o-mini, вызов image_url data-URL, "
            "температура — дефолт провайдера", font=f(17), fill=LIGHT)

    y1, h1 = 110, 130
    nodes = [
        ("Скан формы", "PNG, полное разрешение"),
        ("Разбивка на тайлы", "кадр режется на патчи"),
        ("Патчи → токены", "каждый патч — входной токен"),
        ("Ответ + цена", "JSON полей + $/вызов"),
    ]
    gap = 36
    n = len(nodes)
    node_w = (W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        fc = GOLD if i == n - 1 else SURF
        box(d, xs[i], y1, node_w, h1, [title, sub], fc, tc=DEEP, sz=18,
            outline=LIGHT, where=f"механика-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2 = 280
    box(d, 40, y2, W_PX - 80, 110,
        ["Чем крупнее скан — тем больше тайлов и тем дороже вызов",
         "измерено: $3,85 на 1000 форм (30 реальных вызовов, не оценка)"],
        WARM, tc=DEEP, sz=19, outline=GOLD, where="механика-цена")

    save(im, "a-mekhanika.png")


if __name__ == "__main__":
    a_shema_postanovka()
    a_mekhanika()
    report()
