#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кадр аналитики: столбцы и линии для деки курса. Шаблон, не разовая картинка.

Заведено по указанию владельца курса (issue #244, 2026-10-17): «сделай
столбчатую сортированную диаграмму по государствам, график с динамикой и
небольшой подвал с комментарием… заведи шаблон слайда с аналитикой и
диаграммами (а может два) и используй их». Шаблон файла кадра лежит рядом —
`../../templates/kadr-analitiki.md`; этот модуль рисует то, что на нём стоит.

ЧТО ЭТОТ МОДУЛЬ ДЕРЖИТ, ЧЕГО НЕ ДЕРЖИТ НИ ОДИН РАЗОВЫЙ ПРОГОН

1. **Кегли задаются в точках СЛАЙДА, а не в пикселях картинки.** Это главная
   ловушка, и она уже стоила деке кадра: `rework/deck/make_chart_s86.py`
   описывает, как подписи, набранные пятнадцатым кеглем в фигуре шириной 7",
   сели на кадр восемью с половиной. Здесь логический размер холста задаётся
   в тех же точках, которыми картинка встанет на слайд (1 логический пиксель
   = 1 точка на слайде), а чёткость даёт `devicePixelRatio`. Значит число в
   `kegl=11` — это одиннадцать точек НА ЭКРАНЕ, и проверять его можно до
   сборки.
2. **Знаменатель — часть подписи столбца, а не легенда.** Доля без
   знаменателя на кадре не принимается (`CLAUDE.md` § Baseline /
   Counterfactual Mandate), а диаграмма — ровно то место, где знаменатель
   теряется первым. Поэтому `stolbtsy` берёт подпись второй строкой под
   каждым столбцом и рисует её всегда.
3. **Единица называется один раз и на картинке.** `edinitsa` уходит в
   подзаголовок. Столбцы разных единиц в один ряд не ставятся: у `stolbtsy`
   единица одна на всю диаграмму, и это не удобство, а запрет — ряд из
   случаев, решений и исследований без подписи единицы и есть та пара из
   разных выборок, на которой круг спотыкался трижды.
4. **Запятая в десятичной дроби, а не точка.** Chart.js пишет `1.7`;
   по-русски это `1,70`. Чинится только функцией-переводчиком, поэтому
   спецификация уходит на QuickChart НЕ строгим JSON, а текстом JS (сервис
   разбирает его как JS). Отсюда `_JS` ниже: значение, которое выводится без
   кавычек. Проверено: без этого на кадре стоят `1.7` и ось с точками.

ПАЛИТРА — курсовая (Ocean): глубокий `#21295C`, средний `#065A82`, светлый
`#1C7293`, бирюза `#028090`, золото `#F0AB00` на выделенном столбце.

ЧЕГО ЗДЕСЬ НЕТ. Нет вывода в PPTX: картинка кладётся в `assets/` и ставится
на кадр полем `media:` обычного файла кадра — сборщик деки не правится, и
новый тип кадра не заводится. Это сознательно: тип кадра живёт в сборщике
двух дек, а шаблон аналитики нужен один и сейчас.

СЕТЬ. Рисует QuickChart (`quickchart.io`) — тот же инструмент, что назван в
`README.md` §стек. Картинка сохраняется в репозиторий, поэтому сборка деки
сети уже не требует: без сети не пересобрать картинку, но дека собирается.

    python3 analitika.py --samoproverka     # нарисовать образцы в /tmp
"""
from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEEP, MID, LIGHT, TEAL, GOLD = "#21295C", "#065A82", "#1C7293", "#028090", "#F0AB00"
SETKA, TEKST = "#D7DEE7", "#21295C"
BASE = "https://quickchart.io/chart"
TAYMAUT = 60


# ─────────────────────────── черчение ───────────────────────────

_METKA, _KONETS = "@@JS@@", "@@/JS@@"


def _JS(tekst):
    """Значение, которое уйдёт в спецификацию БЕЗ кавычек — функция JS."""
    return _METKA + tekst + _KONETS


def _v_js(spec):
    """Спецификация → текст JS: как `json.dumps`, но помеченные значения
    выводятся функциями.

    Метка ЗАКРЫВАЮЩАЯ, и это не украшение. Первая редакция искала до
    ближайшей кавычки — и ломалась на первой же функции, внутри которой
    есть строка: подписи значений («60 млн случаев») приходят массивом JS,
    кавычки в нём экранированы, и разбор обрывался на первой из них.
    Поймано прогоном, а не рассуждением."""
    import json as _json
    s = _json.dumps(spec, ensure_ascii=False)
    return re.sub(r'"' + re.escape(_METKA) + r'(.*?)' + re.escape(_KONETS)
                  + r'"', lambda m: _json.loads('"' + m.group(1) + '"'),
                  s, flags=re.S)


# Перевод числа в русскую запись: «1,70» вместо «1.7», «1 614» вместо «1614».
# ДВА переводчика, а не один с догадкой. Деление оси считает каждое число
# по отдельности и не знает шага соседей, поэтому «дробная или целая шкала»
# обязан объявить тот, кто её заводит: иначе на одной оси выходят «1,80» и
# «1» рядом — замерено на первом прогоне.
_TSELYE = _JS("function(v){var s=String(v);"
              "var ch=s.split('.');"
              "return ch[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,' ')"
              "+(ch[1]?','+ch[1]:'');}")
_DROBI = _JS("function(v){return Number(v).toFixed(2).replace('.',',');}")


def _perevodchik(drobnaya):
    return _DROBI if drobnaya else _TSELYE


def _zapas_sprava(gorizontal, kegl, podpisi, znach, drobnaya):
    """Сколько места оставить справа под подпись значения у лежачих столбцов.

    Мерится по самой длинной подписи в половину кегля на знак — грубо, но
    в ту сторону, в какую ошибаться безопасно: лишний воздух справа кадр не
    портит, обрезанная подпись портит."""
    if not gorizontal:
        return 10
    if podpisi:
        dlina = max(len(str(s)) for s in podpisi)
    else:
        dlina = max(len(f"{z:.2f}" if drobnaya else str(z)) for z in znach)
    return min(150, max(34, int(dlina * kegl * 0.62)))


# ПОЛ КЕГЛЯ ПОДПИСЕЙ ДИАГРАММЫ (#293, Этап D, П6-б.5). Прожарка: «подписи
# осей и значений на пределе читаемости — пол для подписей значений 12–13 пт
# В ТОЧКАХ СЛАЙДА (`analitika.py` это умеет — задать в ШАБЛОНЕ, не per-кадр)».
#
# Шаблон это и правда умел, и ровно поэтому умолчание здесь было ошибкой, а
# не мелочью: кегли тут уже заданы в точках слайда (см. п. 1 шапки модуля),
# то есть `kegl=11` означало одиннадцать точек на экране — НИЖЕ пола видимого
# слоя курса (12 пт, `deckkit/floor.py`), и ни один сторож этого не видел,
# потому что подпись уехала в пиксели картинки и для сборки её больше нет.
# Три кадра аналитики Лекции 7 так и стояли: два на 11 пт, один на 10,5.
#
# Умолчание поднято до 13 — середины названного прожаркой окна 12–13, — а
# `KEGL_POL` ниже делает пол ПРОВЕРЯЕМЫМ: кегль мельче просто не принимается.
# Отказом, а не тихим подъёмом: рисунок, молча набранный не тем кеглем, — это
# та же подмена, против которой заведён весь этот модуль.
KEGL_POL = 12          # пол видимого слоя курса, в точках СЛАЙДА
KEGL_PODPISEY = 13     # умолчание для подписей осей и значений
KEGL_ZAGOLOVKA = 15    # умолчание для заголовка диаграммы


def _osnova(kegl, pochemu=None):
    """Общее для обоих видов: шрифт, цвет текста, прозрачный фон выключен."""
    _pol(kegl, "подпись оси или значения", pochemu)
    return {
        "font": {"size": kegl, "family": "sans-serif"},
        "color": TEKST,
    }


def _pol(kegl, chto, pochemu=None):
    """Пол кегля подписи. Отказ, а не поправка: см. комментарий выше.

    `pochemu` — ОБЪЯВЛЕННОЕ исключение: причина, по которой этот рисунок
    кегль не держит. Заведено не для удобства, а потому, что одно такое
    место в деке Лекции 7 действительно есть и проверено замером: кадр
    `s12a` (охват скрининговых программ) ставит пять стран по два-три
    столбца в полосу высотой 216 точек, и подпись значения крупнее 11
    логических пунктов там ЛОЖИТСЯ НА СОСЕДНИЙ СТОЛБЕЦ — проверено
    рендером при 13 пт, подписи наехали друг на друга и на столбцы. Поднять
    полосу нельзя: её высоту (3,00") назначает тип кадра, а пропорция
    картинки от этого жёстко задана.

    Тихо опустить пол там нельзя, молча отказать — тоже: второе оставило бы
    деку с нечитаемой диаграммой, первое вернуло бы ровно ту слепую зону,
    ради которой этот пол и заведён. Поэтому исключение ОБЪЯВЛЯЕТСЯ в месте
    вызова и печатается в прогоне — его видно и его можно оспорить."""
    if float(kegl) >= KEGL_POL - 1e-9:
        return
    if not pochemu:
        raise ValueError(
            f"{chto} набрана {kegl} пт — ниже пола видимого слоя "
            f"{KEGL_POL} пт в точках слайда. Диаграмма с такой подписью с "
            "задних рядов не читается; поднимите кегль, сократите ряды — "
            "или объявите исключение параметром `kegl_nizhe_pola=\"причина\"`")
    print(f"[пол диаграммы] {chto} набрана {kegl} пт при поле {KEGL_POL} — "
          f"исключение ОБЪЯВЛЕНО: {pochemu}")


def stolbtsy(zagolovok, ryady, edinitsa, *, zoloto=None, kegl=KEGL_PODPISEY,
             kegl_zagolovka=KEGL_ZAGOLOVKA, drobnaya=False, gorizontal=False,
             podpisi_znacheniy=None):
    """Сортированные столбцы. `ryady` — [(имя, число, подпись-знаменатель), …].

    Подпись-знаменатель идёт ВТОРОЙ СТРОКОЙ под именем столбца и рисуется
    всегда: диаграмма — первое место, где знаменатель теряется. `zoloto` —
    индекс столбца, который надо выделить золотом (или None).

    `podpisi_znacheniy` — готовые строки вместо чисел у концов столбцов
    («60 млн случаев», «53 млн решений»). Нужны там, где единица у каждого
    столбца СВОЯ: иначе единица уезжает в подпись слева, подпись становится
    двухстрочной, а в полосе высотой три дюйма двухстрочная подпись не
    помещается — замерено на кадре потока.

    `gorizontal=True` кладёт столбцы набок. Это не вкусовщина: подпись из
    двух строк под вертикальным столбцом Chart.js разворачивает на сорок
    пять градусов, как только она шире слота, — замерено на обоих кадрах
    этого круга. Лёжа подпись читается строкой и места берёт столько,
    сколько ей нужно.
    """
    ryady = list(ryady)
    podpisi = [[im, pod] if pod else [im] for im, _, pod in ryady]
    znach = [z for _, z, _ in ryady]
    cveta = [GOLD if zoloto == i else MID for i in range(len(ryady))]
    perevod = _perevodchik(drobnaya)
    # Ось ЧИСЕЛ у лежачих столбцов — горизонтальная, ось ИМЁН — вертикальная;
    # переводчик числа обязан переехать вместе с ней, иначе имена уходят в
    # него, а числа остаются без запятой.
    os_chisel, os_imyon = ("x", "y") if gorizontal else ("y", "x")
    if podpisi_znacheniy:
        import json as _json
        gotovye = _json.dumps(list(podpisi_znacheniy), ensure_ascii=False)
        perevod = _JS("function(v,c){return %s[c.dataIndex];}" % gotovye)
    return {
        "type": "bar",
        "data": {"labels": podpisi,
                 "datasets": [{"data": znach, "backgroundColor": cveta,
                               "borderWidth": 0,
                               "datalabels": {"color": TEKST,
                                              "anchor": "end", "align": "right" if gorizontal else "end",
                                              "offset": 2,
                                              "formatter": perevod,
                                              "font": {"size": kegl,
                                                       "weight": "bold"}}}]},
        "options": {
            "plugins": {
                "legend": {"display": False},
                "title": {"display": True, "text": [zagolovok, edinitsa],
                          "color": TEKST,
                          "font": {"size": kegl_zagolovka, "weight": "bold"}},
                "datalabels": {"display": True},
            },
            "indexAxis": "y" if gorizontal else "x",
            # Справа место ПОД ПОДПИСЬ ЗНАЧЕНИЯ: у лежачих столбцов она стоит
            # за концом самого длинного столбца и без запаса обрезается краем
            # картинки — поймано глазом дважды («60» у верхнего столбца, потом
            # «60 мл» вместо «60 млн случаев»), прогоном не ловится. Запас
            # считается по самой длинной подписи, а не назначается числом:
            # второй раз он обрезался именно потому, что число было назначено.
            "layout": {"padding": {"top": 2, "bottom": 0,
                                   "right": _zapas_sprava(gorizontal, kegl,
                                                          podpisi_znacheniy,
                                                          znach, drobnaya)}},
            "scales": {
                os_imyon: {"ticks": {**_osnova(kegl), "maxRotation": 0,
                                     "autoSkip": False},
                           "grid": {"display": False}},
                os_chisel: {"ticks": {**_osnova(kegl), "callback": perevod},
                            "grid": {"color": SETKA},
                            "beginAtZero": True},
            },
        },
    }


def gruppy(zagolovok, imena_grupp, ryady, edinitsa, *, kegl=KEGL_PODPISEY,
           kegl_nizhe_pola=None,
           kegl_zagolovka=KEGL_ZAGOLOVKA, podpisi_znacheniy=None, gorizontal=True,
           dolya_gruppy=0.78, dolya_stolbtsa=0.80, legenda=True):
    """Сгруппированные столбцы: ОДНА ГРУППА — ОДНА ЕДИНИЦА СРАВНЕНИЯ
    (страна, цех, регион), внутри неё по столбцу на каждую величину.

    ЗАЧЕМ ОТДЕЛЬНО ОТ `stolbtsy`. У `stolbtsy` одна строка — одна величина, и
    строки сортируются по длине. Для обзора «как дела в стране X» эта форма
    не годится и была возвращена прожаркой (§10.1 и §11.4
    `trebovaniya-k-soderzhaniyu-forma.md`): десять строк вида «Лёгкое · США»,
    «Лёгкое · Великобритания», отсортированных по значению, визуально
    ранжируют величины с РАЗНЫМИ основаниями счёта и не дают прочесть ни одну
    страну целиком. Здесь строка — страна, и всё, что про неё известно,
    стоит в одном ряду; сортировка внутри группы не применяется вовсе,
    порядок величин одинаков у всех групп, поэтому глаз сравнивает по
    столбцу, а не по длине.

    `legenda=False` снимает легенду — нужно там, где высота полосы кадра
    задана типом (у `analitika` она 3,00", и логический холст обязан быть
    880×216 точек, иначе картинка ужимается по ширине и кегль подписей
    уезжает ниже пола видимого слоя). Освободившиеся ~25 точек идут группам;
    взамен имя величины ставится В САМУ ПОДПИСЬ столбца («Лёгкое — 18,7% из
    12,8 млн»), и тогда столбец читается без сверки с легендой вовсе.

    `imena_grupp` — подписи оси (страны), в том порядке, в каком их читать.
    `ryady` — `[(имя величины, [значение на каждую группу…], цвет), …]`;
    `None` на месте значения означает, что величины у этой группы НЕТ, и
    столбец не рисуется вовсе. Нулём отсутствие не обозначается никогда:
    ноль читается как измеренная величина, а «программы нет» — это не ноль
    охвата, это другое утверждение, и называть его надо словами на кадре.

    `podpisi_znacheniy` — `{(индекс ряда, индекс группы): "текст"}`: готовая
    подпись у конца конкретного столбца. Через неё на кадр попадает
    ЗНАМЕНАТЕЛЬ, у каждой группы свой («18,7% из 12,8 млн»), — то самое, без
    чего доля на кадре не принимается (`CLAUDE.md` § Baseline /
    Counterfactual Mandate). Не задана — печатается само число с процентом.

    Имена величин уходят в ЛЕГЕНДУ: у `stolbtsy` легенда выключена, потому
    что там ряд один, здесь рядов несколько и различать их нечем больше.
    """
    imena_grupp = list(imena_grupp)
    podpisi_znacheniy = podpisi_znacheniy or {}
    nabory = []
    for i, (imya, znach, cvet) in enumerate(ryady):
        assert len(znach) == len(imena_grupp), (imya, len(znach))
        gotovye = [podpisi_znacheniy.get((i, g)) for g in range(len(znach))]
        nabory.append({
            "label": imya,
            "data": [None if z is None else z for z in znach],
            "backgroundColor": cvet,
            "borderWidth": 0,
            # Просвет между группами и между столбцами внутри группы:
            # без него подпись значения одного столбца встаёт вплотную к
            # столбцу соседнего ряда и читается как его подпись.
            "categoryPercentage": dolya_gruppy,
            "barPercentage": dolya_stolbtsa,
            "datalabels": {
                "color": TEKST,
                "anchor": "end",
                "align": "right" if gorizontal else "end",
                "offset": 2,
                # Пустая подпись у отсутствующей величины: `null` в данных
                # Chart.js столбца не рисует, но подпись — рисует, и без
                # этого на месте «программы нет» печаталось «null».
                "formatter": _JS(
                    "function(v,c){var g=%s;if(v===null||v===undefined)"
                    "return '';return g[c.dataIndex]||(String(v)"
                    ".replace('.',',')+'%%');}"
                    % _spisok_js(gotovye)),
                "font": {"size": kegl, "weight": "bold"},
            },
        })
    os_chisel, os_imyon = ("x", "y") if gorizontal else ("y", "x")
    dliny = [s for s in podpisi_znacheniy.values()] or ["00,0%"]
    return {
        "type": "bar",
        "data": {"labels": imena_grupp, "datasets": nabory},
        "options": {
            "plugins": {
                "legend": {"display": legenda, "position": "top",
                           "labels": {**_osnova(kegl, kegl_nizhe_pola), "boxWidth": kegl,
                                      "boxHeight": kegl, "padding": 8}},
                "title": {"display": True, "text": [zagolovok, edinitsa],
                          "color": TEKST,
                          "font": {"size": kegl_zagolovka, "weight": "bold"}},
                "datalabels": {"display": True},
            },
            "indexAxis": "y" if gorizontal else "x",
            "layout": {"padding": {"top": 2, "bottom": 0,
                                   "right": min(190, max(40, int(
                                       max(len(s) for s in dliny)
                                       * kegl * 0.62)))}},
            "scales": {
                os_imyon: {"ticks": {**_osnova(kegl, kegl_nizhe_pola), "maxRotation": 0,
                                     "autoSkip": False},
                           "grid": {"display": False}},
                os_chisel: {"ticks": {**_osnova(kegl, kegl_nizhe_pola),
                                      "callback": _perevodchik(False)},
                            "grid": {"color": SETKA},
                            "beginAtZero": True},
            },
        },
    }


def _spisok_js(spisok):
    """Список строк как литерал JS: `null` там, где подписи нет."""
    import json
    return "[" + ",".join(
        "null" if s is None else json.dumps(s, ensure_ascii=False)
        for s in spisok) + "]"


def linii(zagolovok, podpisi_x, ryady, edinitsa, *, kegl=KEGL_PODPISEY,
          kegl_zagolovka=KEGL_ZAGOLOVKA, drobnaya=False):
    """Линии динамики. `ryady` — [(имя, [значения], цвет), …].

    Имя ряда идёт в легенду: у двух линий разной величины подписать каждую
    точку нельзя, а без имени линии не различить. Легенда снизу — сверху её
    место занимает заголовок.
    """
    perevod = _perevodchik(drobnaya)
    nabory = []
    for i, (imya, znach, cvet) in enumerate(ryady):
        nabory.append({
            "label": imya, "data": list(znach),
            "borderColor": cvet, "backgroundColor": cvet,
            "borderWidth": 2.5, "pointRadius": 3, "fill": False,
            "tension": 0.25,
        })
    return {
        "type": "line",
        "data": {"labels": list(podpisi_x), "datasets": nabory},
        "options": {
            "plugins": {
                "legend": {"position": "bottom",
                           "labels": {**_osnova(kegl),
                                      "boxWidth": 14, "boxHeight": 8,
                                      "usePointStyle": False}},
                "title": {"display": True, "text": [zagolovok, edinitsa],
                          "color": TEKST,
                          "font": {"size": kegl_zagolovka, "weight": "bold"}},
                "datalabels": {"display": False},
            },
            "layout": {"padding": {"top": 2, "right": 10, "bottom": 0}},
            "scales": {
                "x": {"ticks": {**_osnova(kegl)}, "grid": {"display": False}},
                "y": {"ticks": {**_osnova(kegl), "callback": perevod},
                      "grid": {"color": SETKA}, "beginAtZero": True},
            },
        },
    }


# ─────────────────────────── вывод ───────────────────────────

def narisovat(spec, put, *, shirina_pt, vysota_pt, chetkost=2):
    """Спецификация → PNG. Размеры задаются В ТОЧКАХ СЛАЙДА.

    Логический холст QuickChart берётся равным размеру картинки на слайде в
    точках, поэтому `kegl=11` в спецификации выше — это одиннадцать точек на
    экране, а не в пикселях файла. `chetkost` множит только число пикселей.
    """
    put = Path(put)
    put.parent.mkdir(parents=True, exist_ok=True)
    adres = (f"{BASE}?w={int(shirina_pt)}&h={int(vysota_pt)}&v=4"
             f"&devicePixelRatio={chetkost}&bkg=white&c="
             + urllib.parse.quote(_v_js(spec)))
    with urllib.request.urlopen(adres, timeout=TAYMAUT) as r:
        telo = r.read()
    if not telo.startswith(b"\x89PNG"):
        raise RuntimeError(f"QuickChart вернул не PNG: {telo[:200]!r}")
    put.write_bytes(telo)
    return put


def ryadom(levaya, pravaya, put, *, zazor_pt=10, chetkost=2):
    """Две картинки в одну, бок о бок, с белым зазором между ними.

    Нужно там, где на кадре две диаграммы: поле `media:` у файла кадра одно,
    и двух картинок сборщик деки не возьмёт. Высоты выравниваются по большей.
    """
    from PIL import Image
    a, b = Image.open(levaya).convert("RGB"), Image.open(pravaya).convert("RGB")
    z = int(zazor_pt * chetkost)
    h = max(a.height, b.height)
    holst = Image.new("RGB", (a.width + z + b.width, h), "white")
    holst.paste(a, (0, (h - a.height) // 2))
    holst.paste(b, (a.width + z, (h - b.height) // 2))
    put = Path(put)
    put.parent.mkdir(parents=True, exist_ok=True)
    holst.save(put)
    return put


def _samoproverka():
    """Доказать, что обе формы рисуются и что кегль задан в точках слайда."""
    tmp = Path("/tmp/analitika-samoproverka")
    s = stolbtsy("Проба столбцов", [("Корея", 1.70, "88 из 549"),
                                    ("Россия", 0.39, "57 из 57"),
                                    ("США", 0.18, "61 из 1 614")],
                 "на миллион населения", zoloto=0, drobnaya=True)
    l = linii("Проба линий", [2010, 2015, 2020, 2025],
              [("первый ряд", [7, 11, 23, 56], MID),
               ("второй ряд", [1, 6, 114, 335], LIGHT)], "штук в год")
    a = narisovat(s, tmp / "stolbtsy.png", shirina_pt=265, vysota_pt=250)
    b = narisovat(l, tmp / "linii.png", shirina_pt=265, vysota_pt=250)
    c = ryadom(a, b, tmp / "ryadom.png")
    from PIL import Image
    for p in (a, b, c):
        im = Image.open(p)
        print(f"  {p.name}: {im.width}×{im.height} пикс, {p.stat().st_size} Б")
    print("самопроверка: обе формы нарисованы, свод собран")
    return 0


if __name__ == "__main__":
    sys.exit(_samoproverka() if "--samoproverka" in sys.argv else
             print(__doc__) or 0)
