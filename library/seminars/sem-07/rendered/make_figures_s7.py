#!/usr/bin/env python3
"""Принципиальные схемы деки Семинара 7 (круг 2026-10-12, техника в инструменте).

    teoriya-protsess-trigger-shagi.png   n03  триггер → шаг → шаг → результат
    teoriya-dannye-spiskom.png           n04  список из трёх, узел исполняется трижды
    k1-shema-tri-uzla.png                n09  форма → шаг модели → строка в таблице
    k2-shema-izvlechenie.png             n14  то же, средний узел отдаёт три поля
    k3-shema-dve-vetki.png               n19  у среднего узла второй выход, обе ветки в таблицу
    vyhod-shema-pyat-uzlov.png           n27  процесс занятия целиком

**Почему схемы инструменто-агностичны.** §3 концепции: первый слой подачи —
принципиальная схема без имён вендора, второй — снимок живого холста. Поэтому на
этих шести картинках нет ни одного имени блока n8n: имена стоят рядом, в таблицах
параметров на самих слайдах, и меняются вместе с инструментом, а схема — нет.

**Почему пять схем из шести растут одна из другой.** Кейсы 1→2→3 и выход занятия —
это ОДИН процесс на четырёх стадиях, и зал обязан опознавать стадию за полсекунды:
«тот же, плюс одно». Геометрия держится общей осью `ROW` и общей функцией узла
(`node`), а не копией координат в каждой рисовалке — разъехаться им нечем.

Холст 1600×420 px для схем, которые стоят на слайде ВМЕСТЕ с таблицей параметров
(`deck_kit.figure` ужимает картинку целиком, и широкая переживает это без
предупреждения «СХЕМА ЗАЖАТА»), 1600×520 — для схемы выхода, которая стоит одна.

Запуск: `python3 make_figures_s7.py` (из `rendered/`).
"""
from fig_toolkit import *

CW = 1600
ROW = 150          # ось главного ряда узлов
NH = 54            # полувысота узла


def node(d, cx, cy, w, top, bottom, *, fill=SURF, stroke=LIGHT, tcol=DEEP,
         bcol=MUTE, tsz=26, bsz=19, wd=3, where="узел"):
    """Узел процесса: прямоугольник со скруглением, имя и пояснение под ним.
    Один вид на все схемы — именно поэтому стадии опознаются как «тот же, плюс
    одно», а не сличаются построчно."""
    d.rounded_rectangle([cx - w / 2, cy - NH, cx + w / 2, cy + NH], radius=14,
                        fill=fill, outline=stroke, width=wd)
    ft, fb = f(tsz, True), f(bsz)
    th = tsz + bsz + 9
    y = cy - th / 2
    clabel(d, cx, y, top, tsz, tcol, True, where=where, limit=w - 24)
    if bottom:
        clabel(d, cx, y + tsz + 7, bottom, bsz, bcol, where=where + "-низ", limit=w - 20)


def trig(d, cx, cy, w, top, bottom, **kw):
    """Триггер — тот же узел золотым контуром: начало процесса видно по цвету,
    без отдельной формы и без подписи «это триггер»."""
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
        elif kind == "node":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=SURF, outline=LIGHT, width=3)
        elif kind == "err":
            d.rounded_rectangle([x, y - 16, x + 56, y + 16], radius=8,
                                fill=W, outline=RED, width=3)
        x += 70
        d.text((x, y - 13), T(txt), font=f(20), fill=DEEP)
        x += d.textlength(T(txt), font=f(20)) + 54


# ── n03: процесс = триггер + шаги ───────────────────────────────────────────

def f_protsess():
    im, d = canvas(400)
    trig(d, 200, ROW, 330, T("триггер"), T("с него всё начинается"))
    node(d, 620, ROW, 300, T("шаг"), T("что-то делает с данными"))
    node(d, 1000, ROW, 300, T("шаг"), T("и отдаёт дальше"))
    node(d, 1400, ROW, 300, T("результат"), T("запись, письмо, ответ"))
    for x1, x2 in ((365, 470), (770, 850), (1150, 1250)):
        arrow(d, x1, ROW, x2, ROW, col=MID)
    clabel(d, 820, ROW + 92, T("выход одного — вход следующего"), 22, LIGHT, True,
           where="подпись оси")
    d.rounded_rectangle([34, ROW + 150, CW - 34, ROW + 226], radius=12,
                        fill=SURF, outline=GOLD, width=3)
    clabel(d, CW / 2, ROW + 172, T("Без триггера процесса нет: он просто не начнётся."),
           24, GOLDINK, True, where="правило n03")
    save(im, "teoriya-protsess-trigger-shagi.png")


# ── n04: данные ходят списком ──────────────────────────────────────────────

def f_spiskom():
    im, d = canvas(460)
    node(d, 230, ROW, 340, T("предыдущий шаг"), T("отдал три заявки"))
    # список из трёх элементов — три узких карточки одна под другой
    for i in range(3):
        y = 72 + i * 78
        d.rounded_rectangle([470, y, 760, y + 58], radius=10, fill=PALE,
                            outline=LIGHT, width=2)
        clabel(d, 615, y + 16, T("элемент") + f" {i + 1}", 22, DEEP, True,
               where=f"элемент {i + 1}", limit=250)
    clabel(d, 615, 320, T("список, даже когда элемент один"), 20, MUTE,
           where="подпись списка")
    arrow(d, 400, ROW, 460, ROW, col=MID)
    node(d, 1080, ROW, 360, T("следующий шаг"), T("один узел на холсте"))
    for i in range(3):
        y = 101 + i * 78
        arrow(d, 760, y, 890, ROW if i == 1 else y, col=LIGHT)
    for i in range(3):
        y = 101 + i * 78
        d.rounded_rectangle([1300, y - 22, 1566, y + 22], radius=8, fill=W,
                            outline=TEAL, width=2)
        clabel(d, 1433, y - 17, T("выполнение") + f" {i + 1}", 20, TEAL, True,
               where=f"выполнение {i + 1}", limit=240)
    arrow(d, 1260, ROW, 1294, ROW, col=TEAL)
    d.rounded_rectangle([34, 360, CW - 34, 440], radius=12, fill=WARM,
                        outline=GOLD, width=4)
    clabel(d, CW / 2, 383, T("Узел выполняется по разу на каждый элемент списка."),
           26, GOLDINK, True, where="правило n04")
    save(im, "teoriya-dannye-spiskom.png")


# ── Сквозной процесс: четыре стадии одной геометрии ────────────────────────

def protsess(stage):
    """Схемы n09 / n14 / n19 / n27. `stage` = 1..4, и каждая следующая
    добавляет к предыдущей ровно одно: поля на выходе (2), вторую ветку (3),
    повтор и публикацию (4). Координаты общие — расхождению взяться негде."""
    h = 440 if stage >= 3 else 400
    im, d = canvas(h)
    row = ROW if stage < 3 else 118
    trig(d, 190, row, 310, T("форма"), T("заявка с сайта"))

    mid_top = T("шаг модели") if stage == 1 else T("извлечение полей")
    mid_bot = T("пометка темы") if stage == 1 else T("тема · срочность · контакт")
    node(d, 700, row, 440, mid_top, mid_bot, stroke=TEAL, wd=4, where="средний узел")
    arrow(d, 345, row, 475, row, col=MID)

    if stage == 1:
        node(d, 1330, row, 420, T("строка в таблице"), T("один столбец"))
        arrow(d, 920, row, 1115, row, col=MID)
    elif stage == 2:
        node(d, 1330, row, 420, T("строка в таблице"), T("три столбца"))
        arrow(d, 920, row, 1115, row, col=MID)
        for i, pole in enumerate(("тема", "срочность", "контакт")):
            y = 250 + i * 52
            clabel(d, 1330, y, "· " + T(pole), 22, TEAL, True,
                   where=f"поле {i + 1}", limit=400)
    else:
        err_row = row + 196
        node(d, 1330, row, 420, T("строка в таблице"), T("три столбца"))
        node(d, 1330, err_row, 420, T("та же таблица"), T("тема = не разобрано"),
             stroke=RED, fill=W, tcol=DEEP, where="ветка отказа")
        arrow(d, 920, row, 1115, row, col=MID)
        clabel(d, 1017, row - 40, T("успех"), 21, MID, True, where="метка успеха")
        # второй выход того же узла — вниз и вправо
        arrow(d, 700, row + NH, 700, err_row, col=RED)
        arrow(d, 700, err_row, 1115, err_row, col=RED)
        clabel(d, 860, err_row - 40, T("отказ вызова"), 21, RED, True,
               where="метка отказа")
        d.rounded_rectangle([475, row - NH - 86, 925, row - NH - 24], radius=10,
                            fill=WARM, outline=GOLD, width=3)
        clabel(d, 700, row - NH - 76, T("повтор: 3 попытки, пауза 2 с"), 21,
               GOLDINK, True, where="плашка повтора", limit=420)

    if stage == 4:
        d.rounded_rectangle([34, h - 76, CW - 34, h - 16], radius=12, fill=SURF,
                            outline=LIGHT, width=3)
        clabel(d, CW / 2, h - 66, T("Боевые прогоны идут по опубликованной версии."),
               24, DEEP, True, where="подпись публикации")

    items = [("trig", "триггер"), ("node", "шаг")]
    if stage >= 3:
        items.append(("err", "ветка отказа"))
    legend(d, h - (118 if stage == 4 else 46), items)

    # Имя передаётся С РАСШИРЕНИЕМ: `fig_toolkit.save` отдаёт его прямо в
    # `Image.save`, а тот выводит формат из расширения и без него падает.
    save(im, {1: "k1-shema-tri-uzla.png", 2: "k2-shema-izvlechenie.png",
              3: "k3-shema-dve-vetki.png", 4: "vyhod-shema-pyat-uzlov.png"}[stage])


def main():
    import sys
    if "--lang" in sys.argv:
        set_lang(sys.argv[sys.argv.index("--lang") + 1])
    f_protsess()
    f_spiskom()
    for s in (1, 2, 3, 4):
        protsess(s)
    report()


if __name__ == "__main__":
    main()
