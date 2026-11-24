#!/usr/bin/env python3
"""Программные схемы Семинара 12, Кейс A («Распознавание документов»),
слайды n10-n23(+n15a).

Источники чисел и фактов — `stend/zamery-A/README.md` (целиком) и
`stend/zamery-A/zhurnal.md`. Корпус — 30 форм FUNSD `testing_data`
(`stend/zamery-A/korpus/vyborka.json`), не копируется сюда.

    python3 make_figures_a.py

`a_shema_postanovka`/`a_mekhanika` (n11/n14) — НЕ трогать при правках этого
файла (issue #351, бриф переделки кейса A): третья функция `a_primer_skanov`
(n15a) добавлена рядом, по образцу `_paste_fit`/`case_b_light_hard` из
`make_figures_B.py` этого же занятия (двухпанельная раскладка — реальный
скан + рамка вокруг интересующей области + подпись под каждой панелью).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent

W_PX = 1700

# Те же сканы FUNSD testing_data, по тому же пути, что уже используют
# `run_ocr.py::IMG_DIR` и `measure_vision.py::IMG_DIR` этого стенда — не
# новый источник, а существующая договорённость замера (korpus_vyborka.py
# тоже читает отсюда). Не коммитится и не кешируется в репозитории —
# пересобирается рецептом stend/zamery-A/README.md («Как пересобрать»).
FUNSD_IMG_DIR = Path("/tmp/s12-corpora/funsd/dataset/testing_data/images")


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


# ── n15a — два настоящих скана: лёгкий и трудный случай ─────────────────────
def _funsd_crop(path, crop_box, zoom, highlight_box, outline):
    """Кроп исходного скана с рамкой вокруг настоящей пары подпись+значение
    (координаты — из разметки `annotations/{id}.json`, не на глаз)."""
    im = Image.open(path).convert("RGB")
    c = im.crop(crop_box)
    c = c.resize((c.width * zoom, c.height * zoom), Image.LANCZOS)
    x0, y0, x1, y1 = highlight_box
    ox0, oy0 = crop_box[0], crop_box[1]
    hb = ((x0 - ox0) * zoom, (y0 - oy0) * zoom, (x1 - ox0) * zoom, (y1 - oy0) * zoom)
    ImageDraw.Draw(c).rectangle(hb, outline=outline, width=5)
    return c


def a_primer_skanov():
    """Лёгкий — 86220490 (факс Lorillard Tobacco, машинопись целиком):
    вопрос `To:` box=[168,261,192,276], ответ `Mike Mozina`
    box=[271,260,354,277] (`annotations/86220490.json`, id 0/12).
    Трудный — 92380595 (уведомление о вручении): вопрос `ATTN:`
    box=[88,228,126,241], ответ «MR. ARTHUR STEVENS, ESQ A. J. STEVENS»
    box=[131,216,398,240] (`annotations/92380595.json`, id 3/39) — имя
    получателя дописано от руки поверх напечатанного текста, §8.11 канона."""
    im = Image.new("RGB", (2350, 600), W)
    d = ImageDraw.Draw(im)
    head(d, "Два настоящих скана FUNSD testing_data", sz=28)
    d.text((40, 62),
            "лёгкий случай — машинописный бланк; трудный — рукописная вставка поверх напечатанного",
            font=f(18), fill=LIGHT)

    easy = _funsd_crop(FUNSD_IMG_DIR / "86220490.png", (100, 230, 500, 330), 3,
                        (168, 258, 356, 279), LIGHT)
    hard = _funsd_crop(FUNSD_IMG_DIR / "92380595.png", (0, 130, 450, 270), 2,
                        (78, 206, 432, 248), GOLD)

    target_h = 300
    easy = easy.resize((int(easy.width * target_h / easy.height), target_h))
    hard = hard.resize((int(hard.width * target_h / hard.height), target_h))

    gx1, gy = 50, 110
    gx2 = gx1 + easy.width + 50
    im.paste(easy, (gx1, gy))
    im.paste(hard, (gx2, gy))
    d.rectangle([gx1, gy, gx1 + easy.width, gy + target_h], outline=LIGHT, width=4)
    d.rectangle([gx2, gy, gx2 + hard.width, gy + target_h], outline=GOLD, width=4)

    cap_y = gy + target_h + 14
    box(d, gx1, cap_y, easy.width, 70,
        ["ЛЁГКИЙ — 86220490: «To:» / «Mike Mozina»",
         "подпись и значение — одним шрифтом, на машинке"],
        SURF, tc=DEEP, sz=16, outline=LIGHT, where="подпись-лёгкий")
    box(d, gx2, cap_y, hard.width, 70,
        ["ТРУДНЫЙ — 92380595: «ATTN:» / «A. J. STEVENS»",
         "имя дописано от руки поверх напечатанного «MR. ARTHUR STEVENS»"],
        W, tc=GOLDINK, sz=16, outline=GOLD, where="подпись-трудный")

    save(im, "a-primer-skanov.png")


if __name__ == "__main__":
    a_shema_postanovka()
    a_mekhanika()
    a_primer_skanov()
    report()
