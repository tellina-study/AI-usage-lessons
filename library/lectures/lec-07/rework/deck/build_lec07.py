#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дека Лекции 7 (каркас) на общем ядре `deckkit`. Issue #229, этап 2.

Прежде здесь лежали 2154 строки, из которых мера текста, примитивы,
разметка, читатель файла кадра, полоса плашек, схема и столбцы были
написаны заново — при том, что то же самое было написано заново и в деке
Лекции 6. Теперь всё это живёт в `tools/presentation-build/deckkit/`
(README рядом с пакетом), а здесь остаётся ровно то, что принадлежит ЭТОЙ
лекции и никакой другой:

  * геометрия кадра — поля, верх тела, подвал, колонка иллюстрации. У двух
    настоящих дек эти числа разные, и сводить их не надо: это раскладка под
    разный материал, а не настройка инструмента;
  * три раскладки — обложка, дивайдер, содержательный кадр: что на кадре
    стоит и в каком порядке;
  * подбор ширины боковой иллюстрации `fit_media` — пробная сборка кадра,
    которой у ядра нет и быть не должно: она про то, чем ЭТА дека готова
    поступиться;
  * самопроверка на раскладке этой деки.

ЧТО ПЕРЕВОД ИЗМЕНИЛ В ВИДИМОМ — два места, оба названы заранее в
`deckkit/README.md` и утверждены владельцем:

  1. СНЯТА ТЕНЬ ТЕМЫ. Прежний сборщик искал `effectRef` внутри `spPr`, где
     его нет: он лежит в `<p:style>`, соседе `spPr`. Поиск был холостым, и
     на 112 автофигурах первых двадцати кадров оставалась мягкая тень темы
     (`notes/mcp-limitations.md` [#223-8]). Ядро удаляет сам `<p:style>` —
     тени больше нет ни на одной фигуре деки.
  2. ПЕРЕНАБРАНЫ СХЕМЫ. Прежняя схема набирала шаги фиксированными 11,5 пт
     и переносила решение «влезает ли» на предупреждение после факта. Ядро
     ПОДБИРАЕТ один кегль на всю схему, даёт боксам одну высоту, выделяет
     шаг модели золотом и проверяет тесный бокс. Схем в деке 17 (поле
     `scheme:` стоит в 26 файлах, но в девяти из них оно пустое — `{}`).

Что остальное не двинулось — проверяется не на слово: `deckkit.regress`
сравнивает СОДЕРЖИМОЕ собранного pptx с доставленным (фигуры, геометрия в
EMU, прогоны, заметки), и всякое расхождение обязано попасть в один из этих
двух разрядов. Третьего разряда нет.

Запуск:
  python3 build_lec07.py                 — только PPTX (по умолчанию)
  python3 build_lec07.py --selftest      — проверки на сломанном входе
  python3 build_lec07.py --render        — ещё PDF и PNG, частями, с таймаутом
  python3 build_lec07.py --only s01,s11  — собрать только эти кадры

Рендер убран из обычного прогона не для удобства: `soffice --convert-to pdf`
на деках этого курса дважды вешал машину на часы
(`notes/mcp-limitations.md` [#223-6], [#229-2]). Предупреждения считаются при
сборке PPTX и от рендера не зависят.
"""
import argparse
import sys
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

from deckkit import (columns, floor, flow, markup, media, metrics,  # noqa: E402
                     plates, prims, render as rnd, report, scheme,
                     slidefile, tables, titles, twocol, wrap)
from deckkit.theme import (DEEP, GOLD, LIGHT, MID, OUTLINE,  # noqa: E402
                           SLIDE_H, SLIDE_W, WHITE)

SLIDES_DIR = HERE / "slides"
LEC_ROOT = HERE.parent.parent                      # library/lectures/lec-07
OUT = HERE / "lec-07-karkas.pptx"
SNAPS = HERE / "snapshots"

# ════════════════════════════════════════════════════════════════════
# геометрия ЭТОЙ деки
# ════════════════════════════════════════════════════════════════════
MX = 0.55                              # поле слева и справа
FULL_W = SLIDE_W - 2 * MX              # 12,23"
TITLE_Y, TITLE_H = 0.40, 0.92
BODY_TOP = 1.46
FOOT_BOT = 7.44        # нижняя кромка подвала; ниже — край слайда
FOOT_H = 0.50          # высота подвала на две строки — та, что была
FOOT_Y = FOOT_BOT - FOOT_H
BODY_BOT = FOOT_Y - 0.12
FOOT_LS = 1.12
FOOT_GAP = 0.12        # просвет между низом тела и подвалом
FOOT_MAX_H = 0.75      # предел высоты подвала: три строки на 12 пт (0,693")
                       # плюс допуск. Выше — это уже не ссылка, а абзац, и
                       # он отнимает у тела дюйм; подвал всё равно вырастет
                       # (резать строку источника сборка не вправе), но
                       # скажет об этом.
MEDIA_W = 4.30
MEDIA_W_FLOOR = 2.60   # уже этого иллюстрация становится значком
COL_GAP = 0.34
GAP = 0.20
TICK_W, TICK_H = 1.05, 0.055
SUB_H = 0.52           # полоса подзаголовка под числом-заголовком
SUB_GAP = 0.05         # просвет между числом и подзаголовком
BODY_COL_GAP = 0.40    # между двумя колонками тела (`deckkit.twocol`)

CONTENT_TYPES = {"case", "norm", "comparison", "summary", "map", "question"}

# Кадр-свидетельство. Ширина найдена перебором по сборщику с шагом 0,01":
# ниже 7,57" площадь падает под требуемые §5.9 сорок процентов, выше 7,59"
# правый столбец перестаёт укладываться. Чистое окно — ТРИ сотых дюйма, и
# это измеренный факт про сам кадр s105: обязательная иллюстрация в 40%
# площади и четыре примитива рядом помещаются только впритык.
HERO_W = 7.58
HERO_TOP = 0.10        # верх кадра: выше заголовка, у самой кромки слайда
HERO_GAP = 0.06        # просвет между кадром и телом под ним
# Просвет между НИЗОМ боковой иллюстрации и первой строкой тела, вернувшего
# себе полную ширину. Взят равным отбивке между блоками (7 пт ≈ 0,097"):
# разрез идёт по границе блока, и шов между двумя надписями обязан читаться
# тем же просветом, что и обычная граница блоков внутри одной.
WRAP_GAP = 0.10
# Выключатель проверки «коробка накрывает снимок целиком» — ТОЛЬКО для пробы
# (`selftest_lec07.probe_box_over_media`). Проба на саму проверку иначе
# невозможна: она обязана собрать тот же кадр дважды и показать разницу, а
# «разницу» не с чем сравнивать, пока второго режима нет. Тот же приём и по
# той же причине, что `wrap.ENABLED`.
WRAP_NEEDS_BOX_OVER_MEDIA = True
BODY_PT = 15.0         # номинальный кегль тела этой деки
FOOT_PT = 12.0         # строка источника. Пол видимого слоя (`floor.py`):
                       # было 11,0 — 15 939 знаков деки, самый крупный её
                       # класс ниже порога проекции
# Обложка. Своя ширина: рядом с кадром стоит сплошной текст, а не колонка
# плашек. При отношении 1,5 (снимок s01) ширина 7,79" даёт 40,5% площади —
# порог взят с запасом в полпроцента, — а текстовому столбцу остаётся ровно
# 4,00", в которые заголовок обложки на 34 пт укладывается двумя строками.
COVER_HERO_W = 7.79
COVER_HERO_TEXT_Y = 1.10
COVER_HERO_GOLD_Y = 0.68

# ── наборы единиц ядра ──────────────────────────────────────────────
# Плашки: `plates.LEC07` — это `DEFAULT` с выключенными тремя
# предупреждениями Лекции 6. ГЕОМЕТРИЯ У НИХ ОДНА И ТА ЖЕ, различие только
# в том, молчать или говорить, — и выбор здесь измерен, а не сделан для
# тишины.
#
# Те три предупреждения считают строки подписи, значения и оговорки и
# говорят «полоса выросла за счёт тела». У Лекции 6 оговорка плашки зажата
# по пределу в две строки, и перебор там означал настоящий наезд (`s38a`).
# У Лекции 7 оговорка — предложение по замыслу полосы «было · стало · к
# чему привело», высота плашки считается по НАСТОЯЩЕМУ числу строк, и
# названное следствие не наступает: на всей деке ни одного блокирующего
# предупреждения, тела укладываются везде.
#
# Прогон с `DEFAULT` сделан, и его итог записан здесь, а не спрятан: 35
# предупреждений на 26 кадрах. Из них 30 — про оговорку длиннее трёх строк
# (порог чужого набора), а ПЯТЬ стоят разбора содержанием и выписаны
# находкой для переделки: четыре подписи плашки в четыре строки капителью
# (`s32/1`, `s42/1`, `s48/1`, `s49/3`) и одно значение, в котором лежит
# фраза, а не число (`s37/3`: «независимость: доступа к первому заключению
# второго читателя лишают…» — четыре строки на 10 пт). Это правка текста
# кадров, то есть работа переделки, а не перевода на ядро.
PLATES = plates.LEC07

# Схема: арифметика ядра (подобранный кегль, одна высота бокса, золото на
# шаге модели, проверка тесного бокса), числа — этой деки. Три из них не
# «вкус», а измеренная нужда:
#   step_hi = 11,5 — кегль, на который дека разложена. Выше брать нельзя:
#     бокс вырастет и отожмёт тело на семнадцати кадрах. Подбор от этого не
#     обесценивается — он работает ВНИЗ, а именно это и было сломано.
#   step_rows = 5 — у Лекции 6 шаг конвейера фраза в три строки, у Лекции 7
#     на `s70` это карточка участника: имя строкой и описание под ним, пять
#     строк при 11,5 пт (замерено). Предел три загнал бы кегль на дно и всё
#     равно оставил наезд.
#   row_gap / box_extra / cap_pt — просветы и подпись этой деки.
#   ai_by_word = False — шаг модели в этой деке ОБЪЯВЛЯЕТСЯ, а не угадывается
#     по словам. Замерено на всех 17 схемах: шаблон золотит пять шагов, и
#     четыре из пяти — мимо («Отказ от модели бизнеса» — модель БИЗНЕСА;
#     «Распечатка вывода модели и момент её показа» — документ на столе;
#     «Разработчик… обновления модели» — участник надзора; «План изменений
#     модели» — механизм надзора). При этом ровно те две схемы, где шаг
#     модели настоящий и в них весь смысл, шаблон НЕ находит: у `s18`
#     («без модели» / «с моделью») и `s62` («было» / «стало») слово стоит в
#     подписи ряда, а шаг назван по делу — «Автономное чтение», «черновик».
#     Выписано находкой: пометить эти два шага — работа переделки, не
#     перевода. Явное `ai: true` стоит на одном шаге `s95`, где схема и есть
#     сравнение «до / после» и шаблон был прав.
# ПОЛ ВИДИМОГО СЛОЯ (круг #229, `deckkit/floor.py`). Прежде здесь стояли
# `step_hi=11.5, step_lo=8.5, lab_pt=11.5, cap_pt=10.5` — то есть ВСЯ схема
# набиралась ниже порога проекции курса, и ни одно предупреждение этого не
# называло. Поднято до пола; цена названа и замерена в `README.md` деки:
# бокс шага вырос, и на кадрах, где схема и так шла впритык, высоту теперь
# забирает она, а не тело. Это и есть обмен, который правило покупает.
# НАБОР КЛЕТКИ ПРОГОНАМИ (круг #229, `deckkit/tables.py`). Прежде `**` внутри
# ячейки красил её полужирной ЦЕЛИКОМ, и накопительная карта стадии — своё
# полужирным, пройденное светлым в одной клетке — была невыполнима: три
# сессии подряд обошли это скобками, каждая сочтя свойством жанра. Ядро по
# умолчанию оставлено прежним: Лекция 6 сдана и прочитана залу с полужирной
# клеткой, её отпечаток держит регрессия (замерено: включение двигает кадры
# 75 и 88 доставленной деки). Эта лекция включает флаг сама.
tables.CELL_RUNS = True

SCHEME = scheme.SchemeStyle(ai_by_word=False,
                            step_hi=13.5, step_lo=12.0, step_rows=5,
                            lab_w=1.55, lab_gap=0.0, lab_pt=12.0,
                            step_pad=0.09, step_ls=1.12,
                            box_min_h=0.50, box_extra=0.26,
                            arrow_w=0.20, arrow_h=0.15, gap=0.05,
                            nogap=0.16, row_gap=0.16,
                            cap_pt=12.0, cap_ls=1.12, cap_gap=0.04)


# ════════════════════════════════════════════════════════════════════
# общие части кадра
# ════════════════════════════════════════════════════════════════════


def gold_tick(s, x, y, sid):
    prims.rect(s, x, y, TICK_W, TICK_H, GOLD)
    report.GOLD_SEEN.add(sid)


def heading(s, sl, color=DEEP, width=None):
    """Заголовок кадра — ЛЕСТНИЦЕЙ (`deckkit.titles`), а не подгонкой под
    высоту рамки, плюс необязательное ЧИСЛО вместо фразы.

    Возвращает верх тела. Прежде он был всегда `BODY_TOP`, и это держалось
    на том, что заголовок в одну строку. Теперь верх СЧИТАЕТСЯ: кадр с
    числом-заголовком и кадр с заголовком, который не влез в строку,
    отдают телу меньше — и отдают его честно, а не кладут золотую черту
    поверх второй строки."""
    if not sl.title:
        report.warn(f"[заголовок] {sl.sid}: поле `title` пусто")
        return BODY_TOP
    w = FULL_W if width is None else width
    tag = f"{sl.sid}/заголовок"
    num = titles.headline_of(sl)
    if num:
        nf, _nl, sf, _sl = titles.fit_headline(num, sl.title, w, TITLE_H,
                                               SUB_H, tag=tag)
        nh = metrics.est_h(num, nf, w, 1.06, True)
        prims.text_box(s, MX, TITLE_Y, w, nh, num, size=nf, bold=True,
                       color=color, ls=1.06, tag=f"{tag}-число")
        sh = metrics.est_h(sl.title, sf, w, 1.14)
        prims.text_box(s, MX, TITLE_Y + nh + SUB_GAP, w, sh, sl.title,
                       size=sf, color=MID, ls=1.14, tag=f"{tag}-подзаголовок")
        bottom = TITLE_Y + nh + SUB_GAP + sh
    else:
        sz, _lines = titles.fit_title(sl.title, w, TITLE_H, tag=tag)
        prims.text_box(s, MX, TITLE_Y, w, TITLE_H, sl.title, size=sz,
                       bold=True, color=color, ls=1.08, tag=tag)
        bottom = TITLE_Y + metrics.est_h(sl.title, sz, w, 1.08, True)
    # Акцент садится под НАСТОЯЩУЮ высоту заголовка, а не под рамку в 0,92":
    # у однострочного заголовка рамка на полдюйма выше текста, и акцент,
    # поставленный по рамке, попадал под коробку мотива. Рисует его не
    # заголовок, а `content` последним ходом — иначе коробка мотива
    # закрашивала акцент собой, а проверка `[золото]` при этом молчала.
    #
    # ЗАЖИМА СВЕРХУ БОЛЬШЕ НЕТ, и это и была вся поломка золотой черты:
    # `min(…, BODY_TOP - 0.17)` держал её на 1,29" при двухстрочном
    # заголовке, то есть ВНУТРИ второй строки — зал видел подчёркнутым
    # первое слово этой строки («держит», «модели», «арбитражем», «фазе»).
    # Теперь черта всегда под настоящим низом заголовка, а тело уступает
    # ей место.
    sl.tick_y = bottom + 0.07
    return max(BODY_TOP, sl.tick_y + TICK_H + 0.12)


def source_runs(sl):
    """Прогоны строки источника. Отдельно от `footer` затем, что ту же
    строку надо ИЗМЕРИТЬ до того, как начнётся раскладка тела: её высота
    решает, где кончается тело."""
    src = str(sl.meta.get("source") or "").strip()
    cap = str(sl.meta.get("media_caption") or "").strip()
    if cap and sl.meta.get("media_hero"):
        src = f"{src} · {cap}" if src and src != "—" else cap
    if not src or src == "—":
        return []
    return [{"text": vis, "size": FOOT_PT, "italic": True,
             "color": MID if url else LIGHT, "url": url}
            for vis, url in markup.source_parts(src)]


def foot_geom(sl):
    """`(верх подвала, его высота, низ тела)` — по НАСТОЯЩЕЙ длине источника.

    Прежде высота подвала была числом (0,50" = две строки на 11 пт), и
    длинный источник просто не влезал: шесть кадров деки выдавали
    блокирующее `[высота] подвал`, а на экране строка уезжала под нижнюю
    кромку. Поднятие подвала до пола видимого слоя (11 → 12 пт) добавило бы
    к этим шести ещё, и починить это числом нельзя: источники у кадров
    разной длины, а общее число подвала — это либо отрезанная строка, либо
    отнятая у тела высота на всех ста двадцати двух кадрах.

    Поэтому подвал считается по своему содержимому и растёт ВВЕРХ от
    нижней кромки слайда, а тело кончается там, где начался подвал. Кадр с
    коротким источником остаётся ровно той же геометрии, что был."""
    key = "foot"
    if key not in sl._cache:
        runs = source_runs(sl)
        flat = "".join(r["text"] for r in runs)
        h = max(FOOT_H, metrics.est_h(flat, FOOT_PT, FULL_W, FOOT_LS,
                                      italic=True)) if flat else FOOT_H
        if h > FOOT_MAX_H:
            report.warn(
                f"[высота] {sl.sid}/подвал: источник занял {h:.2f}\" — "
                f"больше предела {FOOT_MAX_H:.2f}\" ({len(flat)} знаков). "
                "Подвал вырастет и заберёт эту высоту у тела; ссылка такой "
                "длины — место заметок лектора, а не экрана")
        y = FOOT_BOT - h
        sl._cache[key] = (y, h, y - FOOT_GAP)
    return sl._cache[key]


def body_bot(sl):
    """Низ тела этого кадра — см. `foot_geom`."""
    return foot_geom(sl)[2]


def footer(s, sl):
    """Подвал: источник живыми ссылками. Подпись обязательного hero идёт
    сюда же последним сегментом — место источника в деке одно, и подпись к
    снимку-свидетельству такой же источник, как работа, из которой взято
    число (§5.9 требует её видимой, но не требует ставить под картинкой)."""
    src = str(sl.meta.get("source") or "").strip()
    cap = str(sl.meta.get("media_caption") or "").strip()
    if cap and sl.meta.get("media_hero"):
        src = f"{src} · {cap}" if src and src != "—" else cap
    if not src or src == "—":
        return
    runs = source_runs(sl)
    if not runs:
        return
    _y, h, _bot = foot_geom(sl)
    prims.text_runs(s, MX, FOOT_BOT - h, FULL_W, h, runs, ls=FOOT_LS,
                    tag=f"{sl.sid}/подвал", quiet=True)


def check_prims(sl, kind):
    """Примитив объявлен на кадре, который его не рисует. Молчать нельзя:
    сессия раздела написала бы полосу плашек и не узнала, что её нет."""
    for f, name in (("blocks", "плашки"), ("scheme", "схема"),
                    ("columns", "столбцы")):
        if sl.meta.get(f):
            report.warn(
                f"[{name}] {sl.sid}: поле `{f}` объявлено на кадре типа "
                f"«{kind}» — оно рисуется только на содержательных кадрах")


# ════════════════════════════════════════════════════════════════════
# три раскладки
# ════════════════════════════════════════════════════════════════════


def cover(p, sl, root):
    s = prims.blank(p)
    bbot = body_bot(sl)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    check_prims(sl, "cover")
    img = media.media_path(sl.meta, root, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    ty, gy = 1.70, 1.28
    if hero:
        x_box, _ = media.place_hero(s, sl.sid, sl.meta, img, SLIDE_W - MX,
                                    HERO_TOP, bbot, COVER_HERO_W)
        tw = x_box - COL_GAP - MX
        ty, gy = COVER_HERO_TEXT_Y, COVER_HERO_GOLD_Y
    elif img:
        tw = 7.10
        media.draw_media(s, sl.sid, img, MX + tw + 0.40, 0.60,
                         SLIDE_W - MX * 2 - tw - 0.40, SLIDE_H - 1.60)
    else:
        tw = FULL_W
    runs = []
    # Абзац начинает ПЕРВЫЙ прогон строки, а не пустой прогон-разделитель
    # после предыдущей: разделитель нёс кегль ПРЕДЫДУЩЕЙ строки, а мера
    # берёт по абзацу максимум — и абзац тела за заголовком в 34 пт мерился
    # как набранный 34-м. На полной ширине обложки это пряталось, а на узком
    # столбце рядом с hero вылезло сразу: оценка 10,34" на тексте, которому
    # нужно 5,49".
    for i, (kind, t) in enumerate(slidefile.body_blocks(sl)):
        sz = {"head": 34.0, "cap": 12.5}.get(kind, 17.0)
        for j, r in enumerate(markup.inline_runs(
                t, sz, DEEP if kind != "cap" else LIGHT)):
            r.setdefault("italic", kind == "cap")
            r["newpara"] = bool(i and j == 0)
            if r["newpara"]:
                r["space_before"] = 12
            runs.append(r)
    if runs:
        prims.text_runs(s, MX, ty, tw, bbot - ty if hero else 4.20, runs,
                        ls=1.22, anchor=MSO_ANCHOR.TOP,
                        tag=f"{sl.sid}/обложка")
    prims.rect(s, MX, gy, 1.60, 0.07, GOLD)
    report.GOLD_SEEN.add(sl.sid)
    footer(s, sl)
    return s


def divider(p, sl, root):
    s = prims.blank(p)
    foot_y = foot_geom(sl)[0]
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    prims.rect(s, 0, 0, 0.17, SLIDE_H, MID)
    check_prims(sl, "divider")
    img = media.media_path(sl.meta, root, sl.sid)
    tw = 7.30 if img else FULL_W
    if img:
        mw, mh = media.media_box_size(media.img_ar(img, sl.sid),
                                      SLIDE_W - MX * 2 - tw - 0.40,
                                      SLIDE_H - 2.40)
        media.draw_media(s, sl.sid, img, SLIDE_W - MX - mw, 1.00, mw, mh)
    y = 1.05
    for kind, t in slidefile.body_blocks(sl):
        if kind == "head":
            sz = metrics.fit_size(t, tw, 1.05, hi=30.0, lo=20.0, floor=16.0,
                                  bold=True, ls=1.10,
                                  tag=f"{sl.sid}/дивайдер-имя")
            h = metrics.est_h(t, sz, tw, 1.10, True)
            prims.text_box(s, MX + 0.22, y, tw, h, t, size=sz, bold=True,
                           color=DEEP, ls=1.10, tag=f"{sl.sid}/дивайдер-имя")
            y += h + 0.10
            prims.rect(s, MX + 0.22, y, 1.30, 0.065, GOLD)
            report.GOLD_SEEN.add(sl.sid)
            y += 0.30
        elif kind == "cap":
            h = metrics.est_h(t, 12.0, tw, 1.14)
            prims.text_box(s, MX + 0.22, y, tw, h, t, size=12.0, italic=True,
                           color=LIGHT, ls=1.14,
                           tag=f"{sl.sid}/дивайдер-подпись")
            y += h + 0.14
        else:
            h = metrics.est_h(t, 15.5, tw - 0.22, 1.24)
            prims.text_runs(s, MX + 0.22, y, tw - 0.22, h + 0.04,
                            markup.inline_runs(t, 15.5, DEEP), ls=1.24,
                            tag=f"{sl.sid}/дивайдер-тело")
            y += h + 0.18
        if y > foot_y - 0.2:
            report.warn(f"[высота] {sl.sid}/дивайдер: текст дошёл до подвала "
                        f"— {y:.2f}\" при пределе {foot_y:.2f}\"")
            break
    footer(s, sl)
    return s


def content(p, sl, root):
    """Содержательный кадр: заголовок · плашки · схема · столбцы · тело ·
    подвал. Тело идёт одним прогоном с иерархией кеглей внутри."""
    s = prims.blank(p)
    bbot = body_bot(sl)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    img = media.media_path(sl.meta, root, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    # `col_bot` — низ КОЛОНКИ примитивов. Без hero это низ тела кадра; с hero
    # колонка кончается там же, где кадр-свидетельство, а тело уходит под него
    # во всю ширину. Иначе 40% площади под кадр и четыре примитива рядом
    # физически не совмещаются: замерено, левая колонка не доберёт 1,5".
    col_bot = bbot
    media_bot = 0.0        # низ боковой иллюстрации; 0 — её нет
    draw_img = None        # отложенный вызов `draw_media`: (x, y, w, h)
    if hero:
        # Кадр-свидетельство встаёт ПЕРВЫМ и забирает своё место целиком: от
        # него считается ширина заголовка и всего остального, а не наоборот.
        x_box, col_bot = media.place_hero(s, sl.sid, sl.meta, img,
                                          SLIDE_W - MX, HERO_TOP, bbot,
                                          HERO_W)
        body_w = x_box - COL_GAP - MX
        y = heading(s, sl, width=body_w)
    else:
        y = heading(s, sl)
        body_w = FULL_W
        if img:
            mw, mh = media.media_box_size(media.img_ar(img, sl.sid),
                                          sl.media_w or MEDIA_W,
                                          min(3.40, bbot - y))
            body_w = FULL_W - mw - COL_GAP
            # Снимок ВЫЧИСЛЯЕТСЯ здесь, а РИСУЕТСЯ ниже. Решение «обтекать
            # или нет» принимается после подбора кегля, а коробка мотива в
            # режиме обтекания идёт во всю ширину — то есть и под снимком.
            # Нарисованный раньше, снимок оказался бы ею накрыт.
            draw_img = (MX + body_w + COL_GAP, y, mw, mh)
            media_bot = y + mh

    is_content = str(sl.meta.get("type") or "case") in CONTENT_TYPES
    pl = plates.plates_of(sl, PLATES) if is_content else []
    if pl:
        y += plates.draw_plates(s, sl.sid, pl, MX, y, body_w, PLATES) + GAP

    sch = scheme.scheme_of(sl, SCHEME)
    if sch:
        scheme.check_scheme(sl.sid, sch, body_w, SCHEME)
        y += scheme.draw_scheme(s, sl.sid, sch, MX, y, body_w, SCHEME) + GAP

    cols = columns.columns_of(sl)
    avail = col_bot - y
    if cols:
        # Столбцы берут не фиксированную высоту, а ОСТАТОК за вычетом того,
        # что нужно телу: иначе кадр с противопоставлением И телом выдавал
        # телу 0,75" и ломался предупреждением там, где места хватало. На
        # кадре с hero тело стоит НЕ под столбцами, а под иллюстрацией во всю
        # ширину, и вычитать его высоту из колонки нечего.
        need = 0.0
        if not hero:
            for kind, t in slidefile.body_blocks(sl):
                need += metrics.est_h(
                    t, {"head": 15.0, "cap": 11.0}.get(kind, 13.0),
                    body_w - 0.08, 1.26, kind == "head") + 0.08
        ch = max(columns.MIN_H,
                 min(avail - (need + GAP if need else 0.0), columns.MAX_H))
        columns.draw_columns(s, sl.sid, cols, MX, y, body_w, ch)
        y += ch + GAP
        avail = col_bot - y

    text_w, box_h = body_w, 0.0
    if not hero and img and y >= media_bot:
        # Боковая иллюстрация занимает правый столбец не до низа кадра, а на
        # свои 3,40" — ниже там пусто. Тело, начавшееся ПОД ней, сужать не за
        # чем: это тот же ход, что сделан для кадра-свидетельства ниже. Без
        # него s18 ужимал тело до 0,58 рабочего кегля при простаивающей
        # справа полосе 4,30×2,0".
        text_w = FULL_W
    if hero:
        # Тело уходит во всю ширину под кадр-свидетельство. Обычный просвет
        # `GAP`, дописанный последним примитивом левой колонки, здесь
        # снимается: полоса начинается от низа КАДРА, а не от низа колонки,
        # иначе кадр и колонка отталкивают тело вниз дважды.
        y = max(col_bot, y - GAP) + HERO_GAP
        text_w = FULL_W
        # Абзацный отступ ЗДЕСЬ не вычитается: его считает `metrics.runs_h` —
        # одна мера на всю деку. Пока он вычитался по месту, поправка стояла
        # в трёх ветках из многих, и кадры без иллюстрации шли мимо неё.
        avail = bbot - y
        # Коробка мотива рисуется по МЕСТУ, а текст меряется по бюджету:
        # иначе последняя строка ложится на нижнюю скруглённую грань.
        box_h = bbot - y + 0.10

    # ── ТАБЛИЦА: вторая раскладка тела, и выбор между ними не вкусовой ──
    # `body_ordered` — единица СТРОКА, порядок сохранён, и среди видов есть
    # `table`; `body_blocks` — единица АБЗАЦ, с иерархией кеглей внутри тела
    # (заголовок 20 · тело 15 · подпись 12), и таблиц она не знает. Перевести
    # одну на другую нельзя — ядро говорит это прямым текстом в своём
    # README, — поэтому кадр, получивший матрицу, ОТДАЁТ иерархию кеглей
    # внутри тела. Уступка названа и принята: по новой ветке идут только
    # кадры с таблицей в теле, вся остальная дека остаётся на прогоне.
    #
    # `apply_matrix_empty` зовётся на КАЖДОМ кадре, а не только на табличном:
    # заявленная `matrix_empty: true` без таблицы в теле — расхождение
    # фронтматтера с телом, и сказать о нём обязан именно тот кадр, у
    # которого таблицы нет.
    heading_ord, ordered = slidefile.body_ordered(sl)
    tables.apply_matrix_empty(sl.sid, sl.meta, ordered)
    if any(k == "table" for k, _ in ordered) and avail > 0.35:
        size = flow.fit_blocks(ordered, text_w - 0.08, avail,
                               tag=f"{sl.sid}/тело")
        # Коробка мотива рисуется по НАСТОЯЩЕЙ высоте блоков, а не по всему
        # бюджету. Прогон ужимается до рамки сам, и рамка ему впору; поток же
        # возвращает свою высоту, и коробка «на весь бюджет» ставила бы
        # нижнюю скруглённую грань вплотную к последней строке — на снимке
        # s21 грань шла прямо под буквами. Подбор кегля работает вверх, пока
        # блоки влезают, поэтому запас сверху тут не появится сам.
        used = flow.blocks_h(ordered, size, text_w - 0.08)
        prims.ocean_box(s, MX - 0.14, y - 0.10, text_w + 0.28,
                        box_h if hero else min(used + 0.30,
                                               bbot - y + 0.10))
        # `accent=DEEP`, а не умолчание ядра: `runs_md` (раскладка-поток)
        # читает `**` как АКЦЕНТ и красит его в `MID`, а `inline_runs`
        # (прогон, которым набрана вся остальная дека) — как полужирный, цвет
        # тот же. Без этой передачи два кадра с таблицей говорили бы
        # полужирным другим цветом, чем сто четыре остальных: замерено на
        # снимке s21, где выделенные термины вышли бирюзовыми.
        flow.flow(s, ordered, MX + 0.04, y, text_w - 0.08, size,
                  f"{sl.sid}/тело", accent=DEEP)
        if draw_img:
            media.draw_media(s, sl.sid, img, *draw_img)
        gold_tick(s, MX, sl.tick_y or (TITLE_Y + 0.98), sl.sid)
        footer(s, sl)
        return s

    blocks = slidefile.body_blocks(sl)
    if blocks and avail > 0.35:
        runs, first = [], True
        for kind, t in blocks:
            sz = {"head": 20.0, "cap": 12.0, "bullet": 15.0}.get(kind, 15.0)
            if not first:
                runs.append({"text": "", "size": sz, "newpara": True,
                             "space_before": 7})
            first = False
            for r in markup.inline_runs(t, sz, LIGHT if kind == "cap"
                                        else DEEP):
                if kind == "cap":
                    r["italic"] = True
                if kind == "head":
                    r["bold"] = True
                runs.append(r)
        # ── ОБТЕКАНИЕ: тело начинается РЯДОМ со снимком ───────────────
        # Условие ровно одно и проверяемое: снимок есть, он боковой, и
        # первая строка тела стоит ВЫШЕ его нижнего края. Кадр с полосой
        # плашек под это условие не попадает — он и так отжат ниже снимка
        # и полную ширину получает веткой `y >= media_bot` выше.
        #
        # Коробка мотива здесь во всю ширину и на всю высоту тела: угол,
        # который занимает снимок, она закрывает собой, а снимок ложится
        # НА неё — белой карточкой на подложке. Два прямоугольника буквой
        # «Г» дали бы шов из двух обводок посреди кадра, а настоящей
        # Г-образной фигуры со скруглением у мотива нет.
        #
        # ── И ВОТ ГДЕ ЭТО ЛОМАЛОСЬ (кадр 84 деки, `s75`) ──────────────
        # «Снимок ложится НА коробку белой карточкой» верно ровно тогда,
        # когда снимок лежит В КОРОБКЕ ЦЕЛИКОМ. Снимок ставится от верха
        # тела, СЧИТАННОГО ДО примитивов (`draw_img` берёт `y` сразу после
        # заголовка), а коробка — от верха тела ПОСЛЕ них. На кадре с
        # полосой плашек это разные высоты: на `s75` снимок начинался на
        # 1,61", коробка — на 3,59", и верхняя грань коробки проходила
        # ПОПЕРЁК снимка. Замер по собранному PDF: перехлёст 288×50 пт,
        # правый верхний угол коробки срезан снимком, первая строка тела
        # осталась одна с дырой под собой.
        #
        # Поэтому обтекание берётся только тогда, когда коробка накрывает
        # снимок целиком. Не накрывает — кадр уходит на `fit_pushed`
        # (тело целиком под снимком, коробка от его нижней грани) либо на
        # обычную узкую колонку: обе раскладки грань снимка не пересекают
        # ни при каком содержимом.
        wrapped, y_bot = None, media_bot + WRAP_GAP
        box_holds_media = (not WRAP_NEEDS_BOX_OVER_MEDIA
                           or (draw_img is not None
                               and draw_img[1] >= y - 0.10))
        if not hero and img and y < media_bot and box_holds_media:
            wrapped = wrap.fit_runs_wrap(
                runs, body_w - 0.08, media_bot - y, FULL_W - 0.08,
                col_bot - y_bot, text_w - 0.08, avail, ls=1.26,
                tag=f"{sl.sid}/тело")
        pushed = None
        if not wrapped and not hero and img and y < media_bot:
            # Рядом со снимком не поместился ни один блок — тело уходит
            # под него целиком. Та же проверка «кегль не падает».
            pushed = wrap.fit_pushed(
                runs, FULL_W - 0.08, col_bot - y_bot, text_w - 0.08, avail,
                ls=1.26, tag=f"{sl.sid}/тело")
        if wrapped or pushed:
            # Коробка мотива начинается там, где начинается ТЕКСТ: при
            # обтекании от верха тела, при уходе под снимок — от первой
            # строки под ним. Иначе под снимком оставался бы пустой
            # подкрашенный поясок там, где текста уже нет.
            top = wrapped[2] if wrapped else []
            bot = wrapped[3] if wrapped else runs
            box_y = y if wrapped else y_bot
            prims.ocean_box(s, MX - 0.14, box_y - 0.10, FULL_W + 0.28,
                            bbot - box_y + 0.10)
            if top:
                prims.text_runs(s, MX + 0.04, y, body_w - 0.08,
                                media_bot - y, top, ls=1.26,
                                tag=f"{sl.sid}/тело-рядом")
            prims.text_runs(s, MX + 0.04, y_bot, FULL_W - 0.08,
                            col_bot - y_bot, bot, ls=1.26,
                            tag=f"{sl.sid}/тело-под")
        else:
            # ── ТЕЛО В ДВЕ КОЛОНКИ ───────────────────────────────────────
            # Только там, где рядом нет иллюстрации: при боковом снимке
            # ширина и так разрезана, а вторая пара колонок внутри узкой
            # половины даёт строку в тридцать знаков. Берётся по тому же
            # правилу, что и обтекание: ТОЛЬКО если кегль от этого не
            # падает (`deckkit.twocol`). Кадр с объявленным
            # противопоставлением (`columns:`) пропускается — у него уже
            # есть два столбца, и вторые под ними читались бы как
            # продолжение первых.
            two = None
            cw = (text_w - 0.08 - BODY_COL_GAP) / 2
            if not hero and not img and not cols and len(blocks) >= 3:
                two = twocol.fit_two(runs, cw, avail, text_w - 0.08, avail,
                                     ls=1.26, tag=f"{sl.sid}/тело")
            if two:
                _k, _i, left, right = two
                used = twocol.used_h(left, right, cw)
                prims.ocean_box(s, MX - 0.14, y - 0.10, text_w + 0.28,
                                box_h if hero else min(used + 0.30,
                                                       bbot - y + 0.10))
                prims.text_runs(s, MX + 0.04, y, cw, avail, left, ls=1.26,
                                tag=f"{sl.sid}/тело-лев")
                prims.text_runs(s, MX + 0.04 + cw + BODY_COL_GAP, y, cw,
                                avail, right, ls=1.26,
                                tag=f"{sl.sid}/тело-прав")
                prims.rect(s, MX + 0.04 + cw + BODY_COL_GAP / 2 - 0.005, y,
                           0.01, min(used, avail), OUTLINE, count="линейка")
            else:
                metrics.fit_runs(runs, text_w - 0.08, avail, ls=1.26,
                                 tag=f"{sl.sid}/тело")
                # Коробка — по НАСТОЯЩЕЙ высоте текста, а не по всему
                # бюджету. Коробка «до подвала» на коротком теле и есть
                # полупустая коробка, которой у Лекции 6 один кадр из ста,
                # а здесь было двадцать один; табличная ветка кадра так
                # считала с самого начала, прогонная — нет.
                used = metrics.runs_h(runs, text_w - 0.08, 1.26)
                prims.ocean_box(s, MX - 0.14, y - 0.10, text_w + 0.28,
                                box_h if hero else min(used + 0.30,
                                                       bbot - y + 0.10))
                prims.text_runs(s, MX + 0.04, y, text_w - 0.08, avail, runs,
                                ls=1.26, tag=f"{sl.sid}/тело")
        floor.check_runs(runs, f"{sl.sid}/тело")
    elif blocks:
        report.warn(f"[высота] {sl.sid}/тело: места под тело не осталось "
                    f"({avail:.2f}\") — примитивы съели кадр")
    if draw_img:
        media.draw_media(s, sl.sid, img, *draw_img)
    gold_tick(s, MX, sl.tick_y or (TITLE_Y + 0.98), sl.sid)
    footer(s, sl)
    return s


BUILDERS = {"cover": cover, "divider": divider}


# ════════════════════════════════════════════════════════════════════
# сборка
# ════════════════════════════════════════════════════════════════════


def fit_media(sl, root, w0=MEDIA_W):
    """Самая широкая боковая колонка, при которой кадр ещё собирается чисто.

    Тот же ход, каким `metrics.fit_size` подбирает кегль: не назначить размер
    и посмотреть, что вышло, а найти наибольший, который держится.
    Понадобился он на `s18` — две плашки, конвейер на два ряда и три абзаца.
    Там и работает: после перевода на ядро схема `s18` стала выше, слот в
    4,30" упёрся в блокирующее предупреждение, и подбор увёл колонку на
    3,70", где кадр собирается чисто. Разница между «снимок не влезает» и
    «слот назначен шире нужного» видна только замером.

    `w0` — откуда начинать поиск; меняет его только проба, которой нужно
    доказать сам механизм, а не нынешний исход (см. `selftest_lec07`).

    Пробная сборка идёт в отдельную презентацию, а состояние отчёта
    снимается и возвращается: проба не имеет права попасть в отчёт."""
    if str(sl.meta.get("type")) not in CONTENT_TYPES:
        return
    if not media.media_path(sl.meta, root, sl.sid) or sl.meta.get("media_hero"):
        return
    keep = report.snapshot()
    chosen, w = None, w0
    while w >= MEDIA_W_FLOOR - 1e-9:
        sl.media_w = w
        report.WARNINGS[:] = []
        report.PRIM.clear()
        report.GOLD_SEEN.clear()
        try:
            content(prims.new_deck(), sl, root)
        except Exception:                            # noqa: BLE001
            break
        if not report.blocking():
            chosen = w
            break
        w = round(w - 0.10, 2)
    report.restore(keep)
    sl.media_w = chosen or MEDIA_W
    if chosen is None:
        report.warn(
            f"[кадр] {sl.sid}: боковая иллюстрация не умещается ни при какой "
            f"ширине до {MEDIA_W_FLOOR:.2f}\" — кадру нечего ей отдать")


def build(only=None, out=OUT, slides_dir=None, root=None):
    sd = slides_dir or SLIDES_DIR
    root = root or LEC_ROOT
    p = prims.new_deck()
    n = 0
    for f in slidefile.slide_files(sd, only):
        sl = slidefile.read_slide(f)
        if sl is None:
            continue
        fit_media(sl, root)
        kind = str(sl.meta.get("type") or "case").strip()
        s = BUILDERS.get(kind, content)(p, sl, root)
        markup.notes_with_links(s, sl.notes)
        if sl.sid not in report.GOLD_SEEN:
            report.warn(f"[золото] {sl.sid}: золотого акцента на кадре нет")
        n += 1
    metrics.font_gaps()
    p.save(str(out))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    if a.selftest:
        from selftest_lec07 import selftest
        return selftest()
    n = build(only=a.only)
    # Проверки по СОХРАНЁННОМУ файлу: hero по порядку деки и пол контраста.
    # Зовутся здесь, а не из `build`, нарочно — см. `render.verify_built`:
    # обе про деку целиком, а `build` зовут однокадровые пробы.
    # `quiet=False`: строка контраста печатается КАЖДУЮ сборку, а не только
    # когда порог провален. Та же причина, по которой `report.report` всегда
    # печатает долю площади hero: молчание о «65 ниже порога» неотличимо от
    # молчания о том, что контраст вообще не мерился.
    rnd.verify_built(OUT, partial=bool(a.only))
    report.report(n, OUT.name)
    rnd.verify_links(OUT)
    if a.render:
        rnd.render(OUT, SNAPS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
