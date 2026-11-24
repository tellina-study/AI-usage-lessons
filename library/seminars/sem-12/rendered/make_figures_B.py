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

Правило заголовка (круг 3, #351 — третий повтор дубля, после `case_b_corpus_overview`
и кейса A в этом же занятии): заголовок кадра даёт сам кадр (frontmatter/`# Title`
слайда) — ни одна функция здесь не зовёт `head()` для своего собственного текста
заголовка. Фигура рисует только то, чего на кадре больше нигде нет: подпись-ссылку
на данные, подписи панелей, вердикты. Повторная проверка перед добавлением новой
функции — искать `head(d, "` в этом файле: если находится, это дубль.

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


_GROUP_LABEL = {
    "G1": "класс", "G2": "лекция", "G3": "семинар", "G4": "залы",
    "G5": "выступление", "G6": "совещание", "G7": "у доски", "G8": "кружки",
    "G9": "библиотека", "G10": "лаборатория", "G11": "мастерская",
    "G12": "амфитеатр",
}

# Снимок примера записи — подобран сессией правки #351 (чистый, без строгой
# выдумки: намеренно другой снимок, чем confab-example ниже, чтобы n28
# показывал устройство трёх записей, а не повторял провал рассказа заранее).
# Переживает добор 40 → 101 (круг 3, #351): снимок и его записи в опросниках
# не менялись, обновились только счётчики групп вокруг него.
_WORKED_EXAMPLE_ID = "94043f06b44df043"


def case_b_corpus_overview():
    """Строка настоящих миниатюр (по одной на группу корпуса, где в группе
    есть снимок с `deck_allowed: true`) + одна фотография целиком с тем, что
    о ней записал каждый из трёх способов — устройство, не выдумка (та — на
    `case_b_confab_example`, другой снимок намеренно).

    Группы и выбор снимка на миниатюру читаются из `razmetka-101.json`
    КАЖДЫЙ прогон заново (первый `deck_allowed: true` в порядке файла), а
    не зашиты списком id — добор 40 → 101 снимок (`s12-korpus-foto-100`,
    круг 3 #351) подтвердил это: фигура пересобралась с новыми снимками и
    двенадцатью группами вместо восьми без единой правки кода.
    `_WORKED_EXAMPLE_ID` — единственное намеренное исключение: конкретный
    разобранный снимок, не меняющийся при росте корпуса.

    Холст 1988×700 (отношение 2,84), как у `case_b_light_hard` — тот же
    расчёт под потолок высоты схемы на кадре (4,30″, правка #351 round 2:
    первая версия на 1988×1000 сжималась сборкой до 63% ширины и вылезала
    за рабочее поле — "СХЕМА ЗАЖАТА"/"НЕ ПОМЕСТИЛОСЬ")."""
    raz = json.loads((ZAMERY_B / "razmetka-101.json").read_text(encoding="utf-8"))
    op = json.loads((ZAMERY_B / "opisaniya-101.json").read_text(encoding="utf-8"))
    entries = [e for e in raz["entries"] if e.get("in_corpus")]
    by_id = {e["id"]: e for e in entries}
    op_by_id = {e["id"]: e for e in op["entries"]}

    thumbs = []
    for g in sorted({e["group"] for e in entries}):
        cand = next((e["id"] for e in entries
                     if e["group"] == g and e.get("deck_allowed")), None)
        if cand:
            thumbs.append((g, cand))

    n = len(thumbs)
    im = Image.new("RGB", (1988, 700), W)
    d = ImageDraw.Draw(im)
    d.text((40, 24),
            f"{n} групп корпуса из {len({e['group'] for e in entries})} — каждая фотография "
            "получает три записи ниже",
            font=f(24), fill=DEEP)

    gap, margin = 16, 40
    tw = (1988 - 2 * margin - (n - 1) * gap) / n
    th = 170
    ty = 64
    for i, (g, pid) in enumerate(thumbs):
        tx = margin + i * (tw + gap)
        _paste_fit(im, CORPUS / f"{pid}.jpg", tx, ty, tw, th)
        d.rectangle([tx, ty, tx + tw, ty + th], outline=LIGHT, width=3)
        clabel(d, tx + tw / 2, ty + th + 6, _GROUP_LABEL.get(g, g), 15, col=DEEP, b=True)

    wy = ty + th + 40
    photo_w = photo_h = 380
    _paste_fit(im, CORPUS / f"{_WORKED_EXAMPLE_ID}.jpg", margin, wy, photo_w, photo_h)
    d.rectangle([margin, wy, margin + photo_w, wy + photo_h], outline=GOLD, width=4)

    e = by_id[_WORKED_EXAMPLE_ID]
    o = op_by_id[_WORKED_EXAMPLE_ID]
    fl = o["fields"]
    tags = " · ".join(t["class"] for t in o["yolo_tags"])

    col_x = margin + photo_w + 30
    col_w = 1988 - col_x - margin
    row_h, row_gap = 90, 13
    ry = wy
    box(d, col_x, ry, col_w, row_h,
        ["Разметка человека:",
         "говорящий с микрофоном, экран со слайдом (лого Creative Commons,",
         "текст), ноутбук в кадре — еды и слушателей нет"],
        SURF, tc=DEEP, sz=16, outline=LIGHT, where="разметка")
    ry += row_h + row_gap
    box(d, col_x, ry, col_w, row_h,
        ["Рассказ:",
         "«человек выступает с речью, держа микрофон; на экране — логотип",
         "Creative Commons и надпись про мероприятие»"],
        W, tc=DEEP, sz=16, outline=LIGHT, where="рассказ")
    ry += row_h + row_gap
    box(d, col_x, ry, col_w, row_h,
        ["Поля:",
         f"event_type: {fl['event_type']} · people_count: {fl['people_count']} · "
         f"food: {str(fl['food_or_drink_present']).lower()} · "
         f"screen: {str(fl['screen_or_slide_visible']).lower()}"],
        SURF, tc=DEEP, sz=16, m=True, outline=LIGHT, where="поля")
    ry += row_h + row_gap
    box(d, col_x, ry, col_w, row_h,
        ["Теги YOLO:",
         f"{tags}",
         "— экран (класс «tv») в кадре виден, но не назван ни одним тегом"],
        WARM, tc=GOLDINK, sz=16, outline=GOLD, where="теги")

    save(im, "case-b-corpus-example.png")


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
    тоже просторнее. Заголовок не рисуется фигурой — его даёт кадр n31
    (правка #351 круг 3: снят дубль, что уже числился за `case_b_corpus_overview`)."""
    im = Image.new("RGB", (1988, 700), W)
    d = ImageDraw.Draw(im)

    pw, ph = 904, 540
    gx1, gx2, gy = 60, 1024, 40
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
    true (лицо в профиль, не крупно).

    Холст 1700×600 (отношение 2,83, было 1700×700/2,43) — правка #351
    round 2: при 2,43 фигура на кадре n33 сжималась сборкой до ~70% ширины
    («СХЕМА ЗАЖАТА») после того, как под неё добавили плашку вывода.
    Заголовок не рисуется фигурой — его даёт кадр n33 (правка #351 круг 3)."""
    im = Image.new("RGB", (1700, 600), W)
    d = ImageDraw.Draw(im)

    pw, ph = 600, 470
    gx, gy = 60, 40
    _paste_fit(im, CORPUS / "2ebe189cf7049839.jpg", gx, gy, pw, ph)
    d.rectangle([gx, gy, gx + pw, gy + ph], outline=GOLD, width=4)

    tx = gx + pw + 50
    tw = 1700 - tx - 40
    box(d, tx, gy, tw, 130,
        ["Поле «food_or_drink_present»: true", "(модель о еде в кадре)"],
        W, tc=RED, sz=19, outline=RED, where="вердикт-поле")
    box(d, tx, gy + 145, tw, 130,
        ["Разметка:", "«Еды в кадре нет, экранов нет»"],
        SURF, tc=DEEP, sz=19, outline=LIGHT, where="вердикт-разметка")
    box(d, tx, gy + 290, tw, 120,
        ["Проверено по кадру:", "еды на снимке действительно нет — выдумка подтверждена"],
        WARM, tc=GOLDINK, sz=17, outline=GOLD, where="вердикт-итог")

    save(im, "case-b-confab-example.png")


def main():
    # case_b_shema_postanovka() больше не вызывается с круга #351: n28 несёт
    # настоящие снимки (case_b_corpus_overview) вместо абстрактной схемы —
    # функция оставлена в файле, не удалена, если понадобится где-то ещё.
    case_b_corpus_overview()
    case_b_light_hard()
    case_b_confab_example()
    print("готово:", sorted(p.name for p in OUT.glob("case-b-*.png")))


if __name__ == "__main__":
    main()
