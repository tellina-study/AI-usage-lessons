#!/usr/bin/env python3
"""Лестница дуги С7–С12: девять ступеней и то, какое занятие какую закрывает.

Возвращена по просьбе владельца (2026-10-13): «у нас в каком-то из первых
вариантов была очень красивая лестница кейсов по семинарам, давай в начало
добавим». Исходная рисовалась в `make_figures_mostik.py` отклонённой деки v3;
геометрия взята оттуда, содержание переписано под нынешнее устройство дуги.

Два отличия от прежней. **Подписаны занятия, а не только ступени** — лестница
стала картой шести семинаров, а не украшением. И **сегодняшних ступеней одна,
а не три**: прежняя дека обещала закрыть три за занятие, нынешняя честно
закрывает нижнюю.

Запуск: `python3 make_figures_lestnitsa.py` (из `rendered/`).
"""
# Общий тулкит схем живёт в `tools/seminar-build/` — одна копия на курс
# (решение владельца 2026-10-12: «сделай общий сборщик для семинаров»).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

# Ступень → (текст, занятие). Порядок снизу вверх.
STUPENI = [
    ("Хватит одного вызова: ответ модели, поиск по своим документам", "до С7"),
    ("Цепочка: шаги в известном порядке, данные между ними", "С7 · сегодня"),
    ("Маршрут: путь задаёт категория входа", "С8"),
    ("Параллель: независимые проверки одного входа", "С9"),
    ("Цикл: повтор по элементам, проверка выхода", "С10"),
    ("Подпроцесс: дирижёр и несколько исполнителей", "С10"),
    ("Агент: порядок шагов выбирает сам", "С11"),
    ("Несколько агентов вместе", "С12"),
    ("Выключить: вернуться к ручному процессу", "С12"),
]
SEGODNYA = 1   # индекс сегодняшней ступени


def lestnitsa():
    W, H = 2400, 760
    im = Image.new("RGB", (W, H), W_ := (255, 255, 255))
    d = ImageDraw.Draw(im)
    pitch, rh, x_right = 74, 62, 2060

    def x_left(i): return 120 + i * 92
    def y_top(i):  return 650 - i * pitch

    # Ломаная по внешнему углу каждой ступени — то, что делает из девяти строк
    # лестницу. Идёт в 7 px слева от края коробки и в 4 px выше верхней грани:
    # по самим краям она уходит под коробку ступенью ниже и оставляет засечки.
    pts = [(x_left(0) - 7, 712)]
    for i in range(9):
        pts.append((x_left(i) - 7, y_top(i) - 4))
        if i < 8:
            pts.append((x_left(i + 1) - 7, y_top(i) - 4))
    d.line(pts, fill=LIGHT, width=3, joint="curve")

    for i, (text, zan) in enumerate(STUPENI):
        x, y = x_left(i), y_top(i)
        w = x_right - x
        today = (i == SEGODNYA)
        past = (i < SEGODNYA)
        if today:
            fill, line, wd, tx = WARM, GOLD, 5, DEEP
        elif past:
            fill, line, wd, tx = SURF, LIGHT, 3, MUTE
        else:
            fill, line, wd, tx = W_, GREY_FILL, 3, GREY_TX
        d.rounded_rectangle([x, y, x + w, y + rh], radius=14, fill=fill,
                            outline=line, width=wd)
        clabel(d, x + 26 + (w - 52) / 2, y + 16, T(text), 29, tx, b=today,
               where=f"ступень {i}", limit=w - 56)
        # Занятие — отдельной меткой справа, вне коробки: это карта дуги.
        col = GOLDINK if today else (MUTE if past else GREY_TX)
        clabel(d, x_right + 150, y + 18, T(zan), 27, col, b=today,
               where=f"занятие {i}", limit=290)

    clabel(d, 1200, 22, T("выше — сложнее процесс; каждое занятие закрывает свою ступень"),
           26, MUTE, where="подпись оси")
    save(im, "lestnitsa-dugi.png")


if __name__ == "__main__":
    lestnitsa()
    report()
