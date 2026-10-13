#!/usr/bin/env python3
"""Принципиальные схемы деки Семинара 7 (круг 2026-10-12, техника в инструменте).

    teoriya-protsess-trigger-shagi.png   n03  триггер → шаг → шаг → результат
    teoriya-dannye-spiskom.png           n04  список из трёх, узел исполняется трижды
    k1-shema-pyat-uzlov.png              n09  форма → извлечение → справочник → строка → экран
    k2-shema-trudnye-zayavki.png         n14  тот же процесс, разобранный на трудных заявках
    k3-shema-dve-vetki.png               n19  у извлечения второй выход, у отказа свой экран
    vyhod-shema-protsess.png             n27  процесс занятия целиком

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
# Общий тулкит схем живёт в `tools/seminar-build/` — одна копия на курс
# (прежде он копировался в папку каждого занятия и копии расходились).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

CW = 1600
ROW = 150          # ось главного ряда узлов
NH = 54            # полувысота узла


def node(d, cx, cy, w, top, bottom, *, fill=SURF, stroke=LIGHT, tcol=DEEP,
         bcol=MUTE, tsz=26, bsz=19, wd=3, where="узел", num=None):
    """Узел процесса: прямоугольник со скруглением, имя и пояснение под ним.
    Один вид на все схемы — именно поэтому стадии опознаются как «тот же, плюс
    одно», а не сличаются построчно.

    `num` — номер шага в кружке у левого верхнего угла. Те же номера стоят в
    вводной на форме и в разделах экрана результата: соответствие «что я вижу»
    ↔ «какой это узел» зал не додумывает (владелец, 2026-10-12)."""
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
        elif kind == "vocab":
            # Своя запись: иначе золотая рамка справочника читается как «ещё один
            # триггер» — находка прожарки по самим картинкам.
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
    im, d = canvas(400)
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
    добавляет к предыдущей ровно одно: трудные заявки (2), вторую ветку с
    повтором (3), публикацию (4). Координаты общие — расхождению взяться негде.

    Пять узлов на первой же схеме — это не усложнение, а состав решения
    (владелец, 2026-10-12): справочник не даёт пустой темы, экран результата
    показывает всю дорогу в том же окне, без походов в журнал и таблицу."""
    h = 470 if stage >= 3 else 400
    im, d = canvas(h)
    row = ROW if stage < 3 else 150

    trig(d, 150, row, 250, T("форма"), T("заявка с сайта"), num=1)
    node(d, 470, row, 330, T("извлечение"), T("схема с перечислением"),
         stroke=TEAL, wd=4, where="извлечение", num=2)
    # Подключённый узел модели: на холсте это отдельная коробка под шагом, и
    # зал считает узлы по тому, что видит (находка прожарки P0-2).
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

    if stage == 2:
        # Стадия 2 ОБЯЗАНА отличаться от стадии 1: прежде это был побайтово тот
        # же файл при обещании «подсвечен справочник» (находка прожарки).
        # Подсветка — золотое кольцо вокруг справочника и подпись новой пометки.
        d.rounded_rectangle([820 - 168, row - NH - 14, 820 + 168, row + NH + 14],
                            radius=18, outline=GOLD, width=5)
        clabel(d, 820, row + NH + 26, T("+ пометка «ещё в заявке»"), 21, GOLDINK,
               True, where="пометка стадии 2", limit=360)
    if stage < 3:
        pass
    else:
        err_row = row + 180
        node(d, 820, err_row, 330, T("строка «не разобрано»"), T("status = not_parsed"), tsz=22,
             stroke=RED, fill=W, tcol=DEEP, where="ветка отказа")
        node(d, 1250, err_row, 300, T("экран"), T("«не разобрана»"),
             stroke=RED, fill=W, tcol=DEEP, where="экран отказа")
        arrow(d, 985, err_row, 1095, err_row, col=RED)
        arrow(d, 470, row + NH, 470, err_row, col=RED)
        arrow(d, 470, err_row, 650, err_row, col=RED)
        clabel(d, 700, row - 42, T("успех"), 21, MID, True, where="метка успеха")
        clabel(d, 520, err_row - 54, T("отказ вызова"), 21, RED, True,
               where="метка отказа")
        d.rounded_rectangle([305, row - NH - 84, 635, row - NH - 24], radius=10,
                            fill=WARM, outline=GOLD, width=3)
        clabel(d, 470, row - NH - 74, T("повтор: 3 попытки"), 21, GOLDINK, True,
               where="плашка повтора", limit=310)
        if stage == 4:
            d.rounded_rectangle([34, h - 72, CW - 34, h - 16], radius=12, fill=SURF,
                                outline=LIGHT, width=3)
            clabel(d, CW / 2, h - 62, T("Боевые прогоны идут по опубликованной версии."),
                   24, DEEP, True, where="подпись публикации")

    items = [("trig", "триггер"), ("node", "шаг"), ("vocab", "сверка со списком")]
    if stage >= 3:
        items.append(("err", "ветка отказа"))
    legend(d, h - (112 if stage == 4 else (46 if stage >= 3 else 34)), items)

    # Имя передаётся С РАСШИРЕНИЕМ: `fig_toolkit.save` отдаёт его прямо в
    # `Image.save`, а тот выводит формат из расширения и без него падает.
    save(im, {1: "k1-shema-shest-uzlov.png", 2: "k2-shema-trudnye-zayavki.png",
              3: "k3-shema-dve-vetki.png", 4: "vyhod-shema-protsess.png"}[stage])


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
