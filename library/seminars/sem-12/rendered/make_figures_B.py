#!/usr/bin/env python3
"""Программные схемы и фотокомпозиты Кейса B Семинара 12 («Описание и поиск
по фотографиям»). Тулкит — общий `tools/seminar-build/fig_toolkit.py` (canon
`tools/seminar-production/README.md` §7), по образцу `make_figures_k2.py`/
`make_figures_k3.py` этого же занятия — та же рисовалка обслуживает только
слайды Кейса B (`slides/n25-n39`); слайды других кейсов пишут параллельные
сессии своими рисовалками, этот файл их не трогает.

Три фигуры:

    case-b-shema-postanovka.png  n27 — схема С1: сплошное — архив фотографий
                                  уже существует (снимки лежат, Ольга ищет
                                  руками); пунктирное золотое — то, что
                                  строит этот кейс: запись о фотографии.
                                  Серым, за контуром — узел «поиск по
                                  записи», который строит кейс D дальше, не
                                  этот.
    case-b-light-hard.png        — лёгкий и трудный случай (§8.11): НАСТОЯЩИЕ
                                  снимки корпуса B, лёгкий — один крупный
                                  сюжет, трудный — групповая сцена, где
                                  деталь тонет в человеке. Подписи —
                                  фактические наблюдения, не вердикт модели.
    case-b-confab-example.png    — пример выдумки свободного рассказа:
                                  НАСТОЯЩИЙ снимок + утверждение модели,
                                  которого на снимке нет (заполняется после
                                  получения vision-результатов).

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_B.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent                     # .../sem-12/rendered
ZAMERY_B = HERE.parent / "stend" / "zamery-B"
CORPUS = ZAMERY_B / "corpus-cache"


def case_b_shema_postanovka():
    im = Image.new("RGB", (1700, 500), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в архиве встаёт запись о фотографии", sz=30)
    d.text((40, 64),
            "снимки уже лежат в архиве — вопрос в том, что о каждом из них запомнить, "
            "чтобы потом найти",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    box(d, 40, y1, 460, h1, ["Архив фотографий", "снимки уже лежат"], SURF,
        tc=DEEP, sz=21, outline=LIGHT, where="узел-архив")
    arrow(d, 500, y1 + h1 / 2, 590, y1 + h1 / 2, col=LIGHT, wd=4)

    box(d, 590, y1, 520, h1, ["Запись о фотографии", "строит этот кейс"], W,
        tc=DEEP, sz=21, outline=GOLD, where="узел-запись")
    arrow(d, 1110, y1 + h1 / 2, 1200, y1 + h1 / 2, col=GOLD, wd=4, dash=True)

    box(d, 1200, y1, 460, h1, ["Поиск по записи", "кейс D, дальше"], SOFT_GREY,
        tc=GREY_TX, sz=21, outline=GREY_FILL, where="узел-поиск")

    y2, h2 = 320, 150
    box(d, 590, y2, 520, h2,
        ["Три способа записи:", "рассказ · теги детектора · поля по схеме"],
        SURF, tc=DEEP, sz=19, outline=GOLD, where="узел-методы")
    arrow(d, 850, y2, 850, y1 + h1, col=GOLD, wd=4, dash=True)

    save(im, "case-b-shema-postanovka.png")


def _paste_fit(im, path, x, y, w, h):
    photo = Image.open(path).convert("RGB")
    pw, ph = photo.size
    scale = max(w / pw, h / ph)
    photo = photo.resize((int(pw * scale), int(ph * scale)))
    pw, ph = photo.size
    left, top = (pw - w) // 2, (ph - h) // 2
    photo = photo.crop((left, top, left + w, top + h))
    im.paste(photo, (int(x), int(y)))


def case_b_light_hard():
    """Лёгкий — один крупный сюжет (кофе по-восточному, людей почти нет).
    Трудный — компьютерный класс: предметная деталь (три ноутбука, наушники,
    кружка, маркер, книги) тонет за семью людьми на переднем плане — ЭТО и
    есть трудность, не поломка корпуса (разметка §8.11). Оба снимка
    `deck_allowed: true` в razmetka.json.

    Холст 1988×700 (отношение 2,84), не 1700×830 (2,05) — правка #351,
    пересчитано под потолок высоты схемы на кадре (4,30″): при этом
    отношении фигура на кадре берёт всю отведённую ширину 12,23″, а не
    72% от нёй, как при прежних пропорциях. Две панели шире и ниже —
    для двухпанельного сопоставления это естественнее прежнего, подписям
    тоже просторнее."""
    im = Image.new("RGB", (1988, 700), W)
    d = ImageDraw.Draw(im)
    head(d, "Лёгкий и трудный случай для описания", sz=30)

    pw, ph = 904, 502
    gx1, gx2, gy = 60, 1024, 100
    _paste_fit(im, CORPUS / "8cb7d659e2d0a541.jpg", gx1, gy, pw, ph)
    _paste_fit(im, CORPUS / "d50064dfabf0fbd5.jpg", gx2, gy, pw, ph)

    d.rectangle([gx1, gy, gx1 + pw, gy + ph], outline=LIGHT, width=4)
    d.rectangle([gx2, gy, gx2 + pw, gy + ph], outline=GOLD, width=4)

    box(d, gx1, gy + ph + 14, pw, 54, ["ЛЁГКИЙ — один крупный сюжет: поднос с кофе"],
        SURF, tc=DEEP, sz=18, outline=LIGHT, where="подпись-лёгкий")
    box(d, gx2, gy + ph + 14, pw, 54,
        ["ТРУДНЫЙ — компьютерный класс: предметы тонут в людях"],
        W, tc=GOLDINK, sz=18, outline=GOLD, where="подпись-трудный")

    save(im, "case-b-light-hard.png")


def case_b_confab_example():
    """Настоящий снимок + вердикт: рассказ приписывает еду снимку, где разметка
    прямо говорит «Еды в кадре нет». Снимок `2ebe189cf7049839` — deck_allowed:
    true (лицо в профиль, не крупно)."""
    im = Image.new("RGB", (1700, 700), W)
    d = ImageDraw.Draw(im)
    head(d, "Выдумка рассказа: проверено по кадру", sz=30)

    pw, ph = 620, 480
    gx, gy = 60, 110
    _paste_fit(im, CORPUS / "2ebe189cf7049839.jpg", gx, gy, pw, ph)
    d.rectangle([gx, gy, gx + pw, gy + ph], outline=GOLD, width=4)

    tx = gx + pw + 50
    tw = 1700 - tx - 40
    box(d, tx, gy, tw, 150,
        ["Поле «food_or_drink_present»: true", "(модель о еде в кадре)"],
        W, tc=RED, sz=20, outline=RED, where="вердикт-поле")
    box(d, tx, gy + 170, tw, 150,
        ["Разметка-истина:", "«Еды в кадре нет, экранов нет»"],
        SURF, tc=DEEP, sz=20, outline=LIGHT, where="вердикт-истина")
    box(d, tx, gy + 340, tw, 140,
        ["Проверено по кадру:", "еды на снимке действительно нет — выдумка подтверждена"],
        WARM, tc=GOLDINK, sz=18, outline=GOLD, where="вердикт-итог")

    save(im, "case-b-confab-example.png")


def main():
    case_b_shema_postanovka()
    case_b_light_hard()
    case_b_confab_example()
    print("готово:", sorted(p.name for p in OUT.glob("case-b-*.png")))


if __name__ == "__main__":
    main()
