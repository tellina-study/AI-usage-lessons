#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дека Лекции 9 («Фронтир, который сам становится лабораторией», issue #310)
на общем ядре `deckkit` (issue #229).

Написан по образцу `tools/presentation-build/deckkit/refdeck.py` (образцовая
раскладка ядра) и `library/lectures/lec-08/rework-v5/deck/build_lec08_v5.py`
(самый свежий настоящий сборщик на этом же ядре, тот же словарь типов
`hero_cover`/`hero_closing`/`schema_matrix`/`schema_pipeline`/
`schema_timeline`/`schema_layered`) — но geometрия и раскладка здесь свои,
под материал этой лекции: раскладка кадра — дело деки, не ядра
(`deckkit/README.md`, «Что остаётся за декой»).

СВЕРКА ФРОНТМАТТЕРА (сделана перед написанием этого файла, см. финальный
отчёт сессии оркестратору): поля `id`/`type`/`title`/`source`/`media`/
`media_hero`/`media_caption`/`blocks:`/`scheme:`/`columns:`/`matrix_empty`/
`headline_number:` читает ЯДРО напрямую (`slidefile.py`, `plates.py`,
`scheme.py`, `tables.py`, `titles.py`). Три расхождения найдены и закрыты
ЗДЕСЬ, в раскладке деки, а не правкой ядра и не правкой файлов кадров:

1. **`columns:` пишет `label`, ядро (`columns.columns_of`) читает `head`.**
   Та же находка, что `notes/mcp-limitations.md` [#301-1] (там деки писали
   `header`, здесь — `label`; причина одна и та же: неизвестный ключ
   внутри `columns` ядро молча отбрасывает). Обходится здесь —
   `columns_from()` ниже читает `label` САМ и строит словарь `{"head":
   ..., "items": [...]}`, который уже умеет `columns.draw_columns`; саму
   `columns.columns_of` эта дека не зовёт вовсе (она и типы ограничивает
   одним `comparison`, которого в словаре этой лекции нет).
2. **`table:` (`headers:`/`rows:`) — поле ВООБЩЕ НЕ ЧИТАЕТСЯ ядром.**
   Список полей фронтматтера, которые знает `slidefile`/`plates`/`scheme`/
   `tables`, кончается на `matrix_empty`/`headline_number` — отдельного
   `table:` там нет. У ядра есть готовый примитив отрисовки таблицы
   (`tables.draw_table`), просто он ждёт список списков, а не словарь
   `{headers, rows}`. `table_from()` ниже — тонкий переводчик одного в
   другое, ровно тот класс кода, для которого эта работа и остаётся за
   декой.
3. **`.svg`/`.webp` в `media:`.** `deckkit.media.img_ar`/`norm_image`
   открывают файл через PIL, а PIL не умеет ни то, ни другое (SVG — не
   растр; WEBP у `python-pptx` в списке поддерживаемых форматов нет вовсе
   — проверено здесь эмпирически: `add_picture` на `.webp` падает
   `ValueError: unsupported image format … got 'WEBP'`). Ровно находка
   `notes/mcp-limitations.md` [#289-1], но здесь ДВА формата, не один, и
   рабочий путь для SVG — не LibreOffice-экспорт, а `rsvg-convert`: он
   реально установлен и проверен в этой сессии
   (`render-bootstrap.sh`), в отличие от прошлой сессии issue #289, где его
   не было. `resolve_media()` ниже конвертирует оба формата в кешированный
   PNG ДО того, как путь уходит в `media.img_ar`/`draw_media`/`place_hero` —
   сами эти функции не трогаются, они и дальше получают путь к обычному
   растру.

Остальные поля файлов кадров (`local_id`, `section`, `assertion`,
`media_needed`, `media_note`, `graf`, `in_bucket`, `status`,
`learning_outcomes`) — служебные метаданные Phase 1-5, на экран НЕ
выводятся ни одной строкой: это по замыслу (`slidefile.py`, шапка модуля),
их место в `deck.yaml` и в отчёте сборки, а не на кадре.

`title` против `assertion`: во фронтматтере `title` у обложки несёт
префикс («Лекция 9. Фронтир…»), у `assertion` префикса нет. На ЭКРАН идёт
только `title` (заголовок содержательного кадра рисует именно его —
`heading()` ниже, как и в `refdeck.heading`/`build_lec08_v5.heading`);
`assertion` остаётся в `deck.yaml` и в отчётах критиков. Префикс «Лекция 9.»
на обложке — это НЕ лозунг (правило §5.12 «заголовок называет предмет, а
не достоинство») и на кадре `s01` не рисуется вовсе: обложка собирается
отдельным видимым телом (`## Видимый текст слайда`), а не из `title`.
Единственная правка поля `title`, сделанная в рамках этой задачи, — в
`s01-cover.md` фронтматтере он и до правки совпадал с тем, что требуется
(«Лекция 9. Фронтир, который сам становится лабораторией» как служебное
имя файла; видимый текст кадра — отдельно), поэтому `title` НЕ трогался ни
на одном из 69 файлов. Трогалась только заметка (см. ниже).

ТОЧЕЧНАЯ ПРАВКА КОНТЕНТА (единственная, разрешённая брифом): в
`s01-cover.md`, раздел «Заметки лектора», снято предложение «Военной и
оборонной темы в материале нет.» — по правилу владельца «вычищать любые
упоминания военной темы целиком, включая формулировки «а мы её не
смотрим»». Остальной текст заметок не тронут.

Запуск:
  python3 build_lec09.py                 — собрать PPTX (по умолчанию)
  python3 build_lec09.py --render        — ещё PDF и PNG, с таймаутом
  python3 build_lec09.py --only s01,s14  — собрать ТОЛЬКО эти кадры — в
                                            ОТДЕЛЬНЫЙ файл
                                            (lec-09-partial.pptx), выпуск
                                            не трогается (см.
                                            `notes/mcp-limitations.md`
                                            [#229-14])
"""
import argparse
import os
import re
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

HERE = Path(__file__).resolve().parent              # .../lec-09/rendered
LEC_ROOT = HERE.parent                               # .../lec-09
REPO_ROOT = HERE.parents[3]                           # корень репозитория
sys.path.insert(0, str(REPO_ROOT / "tools" / "presentation-build"))

from deckkit import (arhitektura, columns, floor, markup, media, metrics,  # noqa: E402
                     plates, polosy, prims, report, scheme, slidefile,
                     tables, timeline, titles, wrap)
from deckkit import axis as _axis                      # noqa: E402
from deckkit import render as rnd                     # noqa: E402
from deckkit.theme import (DEEP, GOLD, LIGHT, MID, SURFACE, TEAL,  # noqa: E402
                           WHITE, SLIDE_H, SLIDE_W)

# ─── ПОЛ КЕГЛЯ ВИДИМОГО СЛОЯ: 15 пт, решение владельца 29.10.2026 ───
# Фаза 6 (issue #317) — переделка деки под это решение: приёмка
# (`rework/metodika-podachi-review-priyomka.md`) и ревью кадра
# (`rework/metodika-podachi-review-kadr.md`) нашли пол деки нетронутым
# (12,0 пт на 680 из 1205 run'ов). Поднято ЗДЕСЬ, по образцу
# `library/lectures/lec-08/rework-v5/deck/build_lec08_v5.py` — пакет
# читает `VIS_PT` в момент вызова (`floor.py`, docstring), поэтому дека
# поднимает свой пол, не двигая порог соседним лекциям.
floor.VIS_PT = 15.0

SLIDES_DIR = LEC_ROOT / "slides"
ASSET_CACHE = HERE / "assets-cache"       # .svg/.webp → .png, кешировано
OUT = HERE / "lec-09-pilot.pptx"
SNAPS = HERE / "snapshots"

# ════════════════════════════════════════════════════════════════════
# геометрия этой деки
# ════════════════════════════════════════════════════════════════════
MX = 0.55
FULL_W = SLIDE_W - 2 * MX                # 12,23"
TITLE_Y, TITLE_H = 0.40, 0.92
BODY_TOP = 1.46
FOOT_BOT = 7.44                          # нижняя грань полосы подвала
# Потолок поднят 0,50"→0,65" ВМЕСТЕ с кеглем подвала (11→15 пт, см. ниже):
# на 15 пт самый длинный источник деки (`s09`, 110 знаков) не влезает в
# одну строку и уходит на две — 0,58" по оценке сборщика, выше старого
# потолка 0,50". Найдено первой же пересборкой после подъёма `FOOT_PT`
# (`[высота] s09/подвал`). 0,65" — с запасом на ту же вторую строку у
# любого другого кадра с похожим по длине источником.
FOOT_H_MAX = 0.65
# Подвал — ступень 0 лестницы кегля (`01-YAZYK-KADRA.md` §2.2: «Подпись /
# источник / подвал» = 15 пт), не отдельное исключение из пола — поднят с
# 11,0 тем же решением владельца, что и тело/плашки/схема ниже.
FOOT_PT, FOOT_LS = 15.0, 1.12
FOOT_GAP = 0.12                          # просвет между телом и подвалом
MEDIA_W = 4.30                           # слот боковой иллюстрации
MEDIA_H_CAP = 3.40
COL_GAP = 0.34
# 0,20"→0,13": после подъёма пола тело-рассказ («Что переехало» / «Честный
# пробел») на `case_study`-кадрах (4 плашки + боковое фото) стало зажато
# ниже 15 пт на 13 кадрах (Фаза 6, issue #317) — просвет между блоками
# геометрически возвращает телу место без правки содержания; найденное
# практикой других дек нижнее приличное значение для просвета блок-блок.
GAP = 0.13
HERO_TOP = 0.10
WRAP_GAP = 0.10
BODY_PT = 15.0                            # номинал тела — пол проекции мерит по нему
TICK_W, TICK_H = 1.05, 0.055
SUB_H, SUB_GAP = 0.52, 0.05               # подзаголовок под числом-заголовком
DIVIDER_IMG_W, DIVIDER_IMG_H = 4.60, 3.60

# Словарь типов этой лекции (deck.yaml): hero_cover/hero_closing — hero;
# divider — раздельный кадр; qa — отдельный Q&A; остальные шесть —
# содержательные (рисуют плашки/схему/столбцы/таблицу).
CONTENT_TYPES = {"norm", "case_study", "schema_matrix", "schema_pipeline",
                 "schema_layered", "schema_timeline", "hero_closing"}

# Золото плашки — `1C7293` (LIGHT), не умолчательный GOLD: находка
# прожарки 2026-10-14, золото `F0AB00` на белом/поверхности даёт 1,99:1 /
# 1,85:1 при пороге WCAG AA 3,0 для крупного текста (`plates.py`, docstring
# `PlateStyle.value_key_color`). Палитра курса не меняется — золото
# остаётся обводкой плашки и акцентной чертой; меняется только цвет
# КЛЮЧЕВОГО ЗНАЧЕНИЯ внутри плашки.
#
# `max_per_row=2`, не умолчательные 4: первая сборка (визуальный цикл,
# итерация 1) дала 23 БЛОКИРУЮЩИХ предупреждения, почти все — `[ширина]`
# на плашках разборов (`s19`/`s20`/`s21`/`s31`/`s32`/`s42`/`s44`/`s45`/
# `s52`/`s53`): форма разбора этой лекции (§5.13 — цена ошибки →
# классический режим → модель → устройство) кладёт в `value`/`note`
# целые фразы и цепочки «вход → … → выход», а не короткие «5 500 ч»
# лекций 6/7, и четыре таких плашки в ряд на кадре с боковой
# иллюстрацией (узкий `body_w`) не держат ни одно слово из вложенных
# цепочек. Две плашки в ряд удваивают ширину КАЖДОЙ без изменения
# смысла — и структура разбора естественно читается как ДВЕ пары
# («цена ошибки» + «цена ошибки-2», «классика» + «модель»), поэтому
# 2×2 не ломает форму, а совпадает с ней.
#
# `label_pt`/`note_pt`/`value_lo`/`value_floor` — четыре поля `PlateStyle`,
# отмеченные в `plates.py` как «пол видимого слоя» (`label_pt`, `note_pt`,
# `value_floor`) либо как нижняя граница диапазона подбора кегля значения
# (`value_lo`) — тот же приём, что `build_lec08_v5.PLATES`. Решение
# владельца 29.10.2026: пол поднят с 12 до 15, здесь — ровно там, где он
# был прибит константой этого стиля.
PLATES = replace(plates.DEFAULT, value_key_color=LIGHT, max_per_row=2,
                 label_pt=15.0, note_pt=15.0, value_lo=15.0,
                 value_floor=15.0)

# `ai_by_word=False`: шаг модели угадывается по слову «модель» ненадёжно
# (находка Лекции 7 — 4 ложных золота из 5), а ни один `scheme:` этой
# лекции не объявляет `ai:`/`ai_by_word` явно. Безопасный выбор — не
# угадывать вовсе; требование «золото ≥1× на кадр» (§ палитра) закрывается
# `gold_tick`, а не схемой.
#
# `step_rows=4`, не умолчательные 3: `s40` держит шаг «Пары «параметры →
# результат» как обучающие примеры» — на 3 отведённых строках он не влезал
# (`[высота]` 0,89" при рамке 0,77"), на 4 — влезает.
#
# `step_lo`/`lab_pt`/`cap_pt` — отмечены в `scheme.py` «пол видимого слоя»,
# подняты с 12 до 15 тем же решением владельца; `step_hi` (потолок диапазона
# подбора кегля шага) поднят с 13,5 до 16, иначе у подбора нет хода вверх
# выше прежнего предела — тот же приём, что `build_lec08_v5.SCHEME`.
SCHEME = scheme.SchemeStyle(ai_by_word=False, step_rows=4,
                            step_hi=16.0, step_lo=15.0, lab_pt=15.0,
                            cap_pt=15.0)

# Столбцы: форма не принимает объект стиля, кегли лежат голыми константами
# модуля и читаются в момент вызова. Поднимаем их тем же приёмом — атрибут
# модуля, без правки общего пакета (у соседних лекций порог остаётся
# прежним) — тот же приём, что `build_lec08_v5.columns.HEAD_PT`.
columns.HEAD_PT = 15.0
columns.ITEM_HI, columns.ITEM_LO, columns.ITEM_FLOOR = 16.0, 15.0, 15.0

# Парные полосы (форма №21 каталога, `polosy:`) — ПОПЫТКА второй формы
# разбора случая, рядом с «сеткой из 4 плашек» (`PLATES` выше), сделанная и
# ОТКЛОНЁННАЯ в этой переделке (issue #317, Фаза 6). Разбор всех 13
# `case_study`-кадров деки на пригодность:
#
# 1. У 12 из 13 классическая сторона либо «не существует» (COROB-X,
#    Starcloud, Suncatcher — задача новая, классического аналога нет
#    вовсе), либо названа словами без опубликованного числа (SPOC, LeoLabs,
#    Dragon, Astrobee, Raptor, Claude/JPL, AIFS/AIGEFS, генеративный дизайн)
#    — выдумать число значило бы нарушить Baseline/Counterfactual Mandate
#    (`CLAUDE.md`) и содержание кадра, которое эта задача не трогает.
# 2. Единственный кадр, где обе стороны уже стоят ЧИСЛОМ в ОДНОЙ единице
#    без изобретения, — `s19` (AEGIS, «24% попаданий» / «93% попаданий»).
#    Опробовано здесь: сборка дала СВОЙ БЛОКИРУЮЩИЙ отказ формы —
#    `check_polosy` отказывается рисовать ОДНУ пару без соседних («строка
#    одна — пара без соседних пар это кадр одного сравнения, и он читается
#    `figure:` либо осью»). Форма №21 по замыслу — аггрегатор НЕСКОЛЬКИХ
#    сравнений на одной шкале (образец `PERENOS-PRIYOMOV.md` §2.3: три
#    строки «изображение / минута озвучки / эпизод микродрамы» на одном
#    кадре), а не альтернативная раскладка ОДНОГО разбора случая. У этой
#    лекции каждый `case_study`-кадр несёт ровно одну пару — форма №21
#    структурно не подходит роли «разбор случая» этой лекции НИ НА ОДНОМ
#    кадре, независимо от наличия чисел. `s19` возвращён на `PLATES`
#    (см. `git log` этого файла — попытка и откат в одном issue #317).
#
# Импорт и стиль оставлены (не вырезаны) — `polosy:` остаётся доступным
# полем фронтматтера для БУДУЩЕГО кадра этой или другой лекции, который
# действительно агрегирует несколько сравнений на одной шкале (например,
# накопительная сводка нескольких кейсов раздела — не этот кадр и не эта
# задача). Поля стиля подняты до пола 15 пт тем же приёмом, что
# `PLATES`/`SCHEME` выше, на случай такого кадра — тот же приём, что
# `build_lec08_v5.POLOSY`.
POLOSY = polosy.PolosyStyle(lab_pt=15.0, val_pt=15.0, mn_pt=15.0,
                            leg_pt=15.0, tick_pt=15.0, unit_pt=15.0,
                            cap_pt=15.0)

# ─── Фаза 7 (issue #317): две новые формы ───────────────────────────
# Владелец, глядя на деку Фазы 6: «где диаграммы, схемы, графики, воронки,
# тренды? нет вообще» — Фаза 6 подключила только плашки/схему-ряды/
# столбцы/таблицы/полосы (см. докстринг файла выше), а каталог форм
# (`02-KATALOG-FORM*.md`) шире. `ARH` — та же архитектура-с-разбором-
# внутри-боксов (`arhitektura.py`), что `build_lec08_v5.ARH`; тот же приём
# подъёма пола, что `PLATES`/`SCHEME`/`POLOSY` выше.
ARH = arhitektura.ArhStyle(role_pt=15.0, head_lo=15.0, line_lo=15.0,
                           line_hi=16.0, vyn_pt=15.0)

# `timeline:` — стадии процесса на одной линии (для keystone-кадра s09:
# цепочка «шахта DARPA → архитектура → лунная труба» читается ПОЛОЖЕНИЕМ
# привязки на линии, не абзацем текста). Тот же приём подъёма пола, что
# `build_lec08_v5._TIME`.
_TIME = replace(timeline.DEFAULT, unit_pt=15.0, cap_pt=15.0, stage_pt=15.0,
                head_pt=15.0, txt_pt=15.0, lab_pt=15.0, val_pt=15.0,
                srok_txt_pt=15.0, end_pt=15.0)

# `scheme: kind: shkala` — засечки на одной прямой (`axis.py`), для трендов
# введения (s02 цена/кг, s03 число спутников): величина ВИДНА положением
# засечки на линии, а не читается в карточке. Модуль уже встроен в
# `scheme.py` (`KINDS["shkala"] = axis`), но собственные `height`/`check`/
# `draw` модуля зовутся БЕЗ декиного стиля (`mod.height(sch, w)` — тот же
# безымянный вызов, которым `scheme_h`/`check_scheme`/`draw_scheme` зовут
# ЛЮБОЙ `kind`) и уходят на `axis.DEFAULT` (пол 12 пт). Обёртки ниже — тот
# же приём, что `build_lec08_v5._obyortki`: подменяем МОДУЛЬНЫЕ алиасы
# декиным стилем, не трогая ни `scheme.py`, ни `axis.py`.
_AXIS = replace(_axis.DEFAULT, lab_pt=15.0, unit_pt=15.0, cap_pt=15.0,
                end_pt=15.0)


def _obyortki(mod, st, h_fn, c_fn, d_fn):
    """Тонкая обёртка модуля формы — с декиным стилем вместо его
    умолчания. Три алиаса, ровно те, что зовёт `scheme.py` через `KINDS`."""
    mod.height = lambda d, w: h_fn(d, w, st)
    mod.check = lambda sid, d, w: c_fn(sid, d, w, st)
    mod.draw = lambda s, sid, d, x, y, w, tag=None: d_fn(
        s, sid, d, x, y, w, st, tag=tag)


_obyortki(_axis, _AXIS, _axis.axis_h, _axis.check_axis, _axis.draw_axis)

# `TBL_ROW_MIN` 0,40"→0,32": найдено на `s62`/`s63` (14 строк со шляпкой —
# `s63`, сводная сетка «тип задачи × модальность», 13 разборов). При кегле
# на самом полу (`TBL_FLOOR=8,0`) ОДНОСТРОЧНАЯ ячейка естественно высотой
# 0,34" — МЕНЬШЕ умолчательного `TBL_ROW_MIN=0,40`, то есть пол, а не
# содержимое, навязывал этим строкам лишние 0,06" каждой (14 × 0,06 = 0,84"
# — именно то, чего не хватало телу-выводу под таблицей). Большинство строк
# этих двух таблиц — короткие одиночные имена/категории («AEGIS»,
# «классификация», «изображение»), не абзацы: естественная высота у них и
# так выше нового пола (0,32 < 0,34), то есть он НЕ навязывает усадку там,
# где контент этого не позволяет — двустрочная ячейка продолжает мериться
# по строкам, а не по полу. Поднято атрибутом модуля, не правкой
# `tables.py`: порог остаётся 0,40 для всех остальных дек курса.
tables.TBL_ROW_MIN = 0.28


def fit_table_height(tbl, hi, avail_h, w):
    """Кегль таблицы, подобранный по ВЫСОТЕ, а не только по ширине столбца.

    `tables.tbl_size` меряет только ширину столбцов — у таблицы `s62`/`s63`
    (9 и 13 строк) ширина столбцов укладывается уже на 15 пт, а строки all
    равно не влезают по ВЫСОТЕ (`table_geom` даёт 7,15"/7,43" при пределе
    5,36"). Эта функция — тот же перебор «от большего кегля вниз», что
    `metrics.fit_size`, но критерий — сумма высот строк, а не ширина
    столбца; на каждом шаге всё равно зовёт `tbl_size`, чтобы не выбрать
    кегль, при котором слово рвётся переносом."""
    size = hi
    while size > tables.TBL_FLOOR:
        sz = tables.tbl_size(tbl, size, w)
        _w, heights, _rows = tables.table_geom(tbl, sz, w)
        if sum(heights) <= avail_h:
            return sz
        size -= 0.5
    return tables.TBL_FLOOR

CONTENT_TYPES_WITH_FIELDS = ("blocks", "scheme", "columns", "table",
                             "matrix_empty", "headline_number", "polosy",
                             "arhitektura", "timeline")


# ════════════════════════════════════════════════════════════════════
# .svg / .webp → .png (кеш), [#289-1]-класс дефект: PIL/python-pptx их не
# берут, а ядро про это молчит — снимок просто не рисуется без единого
# предупреждения. Решается ЗДЕСЬ, до того как путь попадёт в media.*.
# ════════════════════════════════════════════════════════════════════
_RSVG_BIN = "/home/harness/.local/render-extras/sysroot/usr/bin/rsvg-convert"
_RSVG_LIB = "/home/harness/.local/render-extras/sysroot/usr/lib/x86_64-linux-gnu"


def _convert_svg(path, out):
    env = dict(os.environ)
    env["LD_LIBRARY_PATH"] = _RSVG_LIB + (
        ":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")
    r = subprocess.run([_RSVG_BIN, "-w", "1600", str(path), "-o", str(out)],
                       env=env, capture_output=True, text=True)
    if r.returncode:
        report.warn(f"[кадр] {path.name}: rsvg-convert упал — {r.stderr[-300:]}")
        return False
    return True


def _convert_webp(path, out):
    from PIL import Image
    try:
        im = Image.open(path)
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        im.save(out, "PNG")
        return True
    except Exception as e:                            # noqa: BLE001
        report.warn(f"[кадр] {path.name}: конвертация .webp упала — {e}")
        return False


def convert_if_needed(path):
    """`.svg`/`.webp` → кешированный `.png` рядом, в `assets-cache/`.
    Любой другой формат возвращается нетронутым."""
    ext = path.suffix.lower()
    if ext not in (".svg", ".webp"):
        return path
    out = ASSET_CACHE / (path.stem + ".png")
    if out.exists() and out.stat().st_mtime >= path.stat().st_mtime:
        return out
    ASSET_CACHE.mkdir(parents=True, exist_ok=True)
    ok = _convert_svg(path, out) if ext == ".svg" else _convert_webp(path, out)
    return out if ok and out.exists() else path


def resolve_media(meta, root, sid):
    """`media.media_path` плюс конвертация форматов, которые PIL/python-pptx
    не берут. Остаётся тонкой обёрткой: сама `media.media_path` не правится."""
    p = media.media_path(meta, root, sid)
    if p is None:
        return None
    return convert_if_needed(p)


# ════════════════════════════════════════════════════════════════════
# общие части кадра
# ════════════════════════════════════════════════════════════════════


def gold_tick(s, sid, x, y):
    prims.rect(s, x, y, TICK_W, TICK_H, GOLD, count="акцент")
    report.GOLD_SEEN.add(sid)


def draw_chip_scale(s, x, y, w):
    """s51: несимметричные столбики «чипов в космосе сейчас» vs «в одном
    земном AI-датацентре» — `media_needed` этого кадра заказывал ровно
    такую картинку («намеренно несимметричные столбики»), а Фаза 6 её не
    построила: кадр оставался почти пустым под вступительной плашкой
    (находка QA-прохода 2026-11-02, U7). Числа настоящие: Starcloud-1 — 1
    чип Nvidia H100 (s52), Suncatcher — 4 TPU на спутник (s53); «десятки
    тысяч» для земного AI-датацентра — отраслевой порядок величины, не
    точное число, поэтому столбики НЕ в линейном масштабе и подписаны как
    таковые (не рисуем ложную точность)."""
    bar_h = 0.30
    rows = [
        ("В космосе сейчас", "5 чипов", "1×H100 (Starcloud-1) + 4×TPU "
         "(Suncatcher) — s52/s53", 0.55, GOLD, DEEP),
        ("В одном земном AI-датацентре", "десятки тысяч GPU",
         "типовой размер современного обучающего кластера", w, TEAL, TEAL),
    ]
    cy = y
    for label, num, cap, bw, bar_col, text_col in rows:
        # `text_col` != `bar_col` для золотой строки: GOLD-текст на белом
        # фоне не держит WCAG AA (1,99:1 при пороге 3,0 — тот же дефект,
        # по которому вся дека уже увела `value_key_color` плашек на LIGHT,
        # см. PLATES выше). Золото остаётся только заливкой столбика —
        # там это заливка фигуры, не прогон текста, контрастный сторож её
        # не меряет.
        prims.text_runs(s, x, cy, w, 0.34, [
            {"text": f"{label}: ", "size": 15, "color": DEEP},
            {"text": num, "size": 18, "bold": True, "color": text_col},
            {"text": f" — {cap}", "size": 15.0, "color": LIGHT,
             "italic": True},
        ], ls=1.15, tag="s51/строка-сравнения")
        prims.rect(s, x, cy + 0.40, max(bw, 0.12), bar_h, bar_col,
                   radius=True, count="столбик")
        cy += 0.40 + bar_h + 0.34
    prims.text_box(s, x, cy + 0.04, w, 0.35,
                   "Столбики не в линейном масштабе — разница составляет "
                   "порядки, не проценты.", size=15.0, italic=True,
                   color=LIGHT, tag="s51/сноска")
    return cy + 0.40 - y


def heading(s, sl, width=None, color=DEEP):
    """Заголовок кадра — лестницей (`deckkit.titles`), с `headline_number`
    (s08/s61/s64 этой деки) там, где он объявлен и непуст."""
    if not sl.title:
        report.warn(f"[заголовок] {sl.sid}: поле `title` пусто")
        return BODY_TOP
    w = FULL_W if width is None else width
    tag = f"{sl.sid}/заголовок"
    num = titles.headline_of(sl)
    if num:
        nf, _nl, sf, _sl2 = titles.fit_headline(num, sl.title, w, TITLE_H,
                                                SUB_H, tag=tag)
        nh = metrics.est_h(num, nf, w, 1.06, True)
        prims.text_box(s, MX, TITLE_Y, w, nh, num, size=nf, bold=True,
                       color=color, ls=1.06, tag=f"{tag}-число")
        sh = metrics.est_h(sl.title, sf, w, 1.14)
        prims.text_box(s, MX, TITLE_Y + nh + SUB_GAP, w, sh, sl.title,
                       size=sf, color=MID, ls=1.14, tag=f"{tag}-подзаголовок")
        bottom = TITLE_Y + nh + SUB_GAP + sh
    else:
        sz, _n = titles.fit_title(sl.title, w, TITLE_H, tag=tag)
        prims.text_box(s, MX, TITLE_Y, w, TITLE_H, sl.title, size=sz,
                       bold=True, color=color, ls=1.08, tag=tag)
        bottom = TITLE_Y + metrics.est_h(sl.title, sz, w, 1.08, True)
    sl.tick_y = bottom + 0.07
    return max(BODY_TOP, sl.tick_y + TICK_H + 0.12)


def source_runs(sl):
    src = str(sl.meta.get("source") or "").strip()
    cap = str(sl.meta.get("media_caption") or "").strip()
    if cap and (sl.meta.get("media_hero") or sl.meta.get("media_document")):
        src = f"{src} · {cap}" if src and src != "—" else cap
    if not src or src == "—":
        return []
    return [{"text": vis, "size": FOOT_PT, "italic": True,
             "color": MID if url else LIGHT, "url": url}
            for vis, url in markup.source_parts(src)]


def foot_geom(sl):
    """Высота подвала по ФАКТИЧЕСКОМУ источнику, не фиксом 0,50".

    Фикс на первой сборке держал нижнюю границу тела на 6,82" даже там, где
    источник — одна короткая строка или вовсе «—»: `s62`/`s63` (большие
    таблицы, source — одна фраза) и большинство разборов (`source` — одна
    работа) получали в подвал ту же высоту, что кадр с четырёхсегментным
    перечнем источников. `body_bot()` ниже возвращает РЕАЛЬНЫЙ низ тела —
    на пустом источнике это 7,32", на «Сетка дана Лекцией 1» (`s63`) —
    около 7,2", и освобождённые 0,3-0,5" уходят телу/таблице, а не лежат
    пустым запасом в подвале.

    Тот же приём, что `build_lec08_v5.foot_geom`/`body_bot` — перенесён
    сюда, потому что без него плотные кадры этой лекции (накопительные
    таблицы `s62`/`s63`) не укладывались даже на полу кегля."""
    key = "подвал"
    if key not in sl._cache:
        runs = source_runs(sl)
        flat = "".join(r["text"] for r in runs)
        if flat:
            e = metrics.est_h(flat, FOOT_PT, FULL_W, FOOT_LS, italic=True)
            h = min(e, FOOT_H_MAX)
            if e > FOOT_H_MAX + 0.02:
                report.warn(
                    f"[высота] {sl.sid}/подвал: источник не влезает в "
                    f"подвал — {len(flat)} знаков, оценка {e:.2f}\" против "
                    f"{FOOT_H_MAX:.2f}\"")
        else:
            h = 0.0
        y = FOOT_BOT - h
        sl._cache[key] = (y, h, y - FOOT_GAP)
    return sl._cache[key]


def body_bot(sl):
    return foot_geom(sl)[2]


def footer(s, sl):
    """Подвал: источник живыми ссылками. Ни один кадр этой лекции не несёт
    `media_caption` (решение О17/О18 — «источники фотографий на слайде не
    подписывать», соблюдено уже в файлах кадров), поэтому вторая половина
    этой функции у `refdeck.footer`/`build_lec08_v5.footer` здесь мертва по
    входу, а не по правке — оставлена на случай, если такое поле появится
    позже."""
    runs = source_runs(sl)
    if not runs:
        return
    y, h, _bot = foot_geom(sl)
    prims.text_runs(s, MX, y, FULL_W, max(h, 0.3), runs, ls=FOOT_LS,
                    tag=f"{sl.sid}/подвал", quiet=True)


def check_prims(sl, kind):
    for f, name in (("blocks", "плашки"), ("scheme", "схема"),
                    ("columns", "столбцы"), ("table", "таблица"),
                    ("matrix_empty", "матрица"), ("polosy", "полосы"),
                    ("arhitektura", "архитектура"), ("timeline", "таймлайн")):
        if sl.meta.get(f):
            report.warn(
                f"[{name}] {sl.sid}: поле `{f}` объявлено на кадре типа "
                f"«{kind}» — оно рисуется только на содержательных кадрах")


def place_hero_centered(s, sl, img, body_bot_y, *, target=0.42, w_cap=9.0):
    """Hero-иллюстрация (§5.9, ≥40% площади) по ВЕРТИКАЛЬНОЙ СЕРЕДИНЕ тела,
    шириной, выведенной из СОБСТВЕННОГО отношения сторон снимка — не из
    чужого магического числа. У `build_lec08_v5.cover` ширина (8,64")
    посчитана руками под ОДИН конкретный снимок 16:9; здесь то же самое
    уравнение (`w² / ar = target·SLIDE_W·SLIDE_H`) решается заново для
    КАЖДОГО hero-кадра по его собственному `ar`, потому что `s01` этой
    лекции квадратный (1000×1000, ar=1,0), а `s68` — 16:9 (2500×1406,
    ar≈1,778): общего числа для обоих не существует.

    `target=0.42`, не 0.40 — тот же запас, чтобы порог не задевался
    впритык при любой разумной пропорции снимка."""
    ar = media.img_ar(img, sl.sid) or (16 / 9)
    w = min(w_cap, (target * SLIDE_W * SLIDE_H * ar) ** 0.5)
    box_h = w / ar + 2 * media.HERO_PAD
    y_top = max(HERO_TOP, HERO_TOP + (body_bot_y - HERO_TOP - box_h) / 2)
    x_box, bot = media.place_hero(s, sl.sid, sl.meta, img, SLIDE_W - MX,
                                  y_top, body_bot_y, w)
    return x_box, bot, y_top


def columns_from(sl):
    """Поле `columns` → список столбцов для `columns.draw_columns`.

    Переводчик, не повторная реализация: деки этой лекции пишут `label`
    внутри `left`/`right` (`s16`, `s24`), а `columns.columns_of` читает
    `head` — тот же класс расхождения, что `notes/mcp-limitations.md`
    [#301-1] (там было `header`). `columns.columns_of` здесь не зовётся
    вовсе: она к тому же ограничивает поле типом `comparison`, которого в
    словаре этой лекции нет (здесь `columns` стоит на `norm` и
    `schema_matrix`)."""
    raw = sl.meta.get("columns")
    if not isinstance(raw, dict) or "left" not in raw or "right" not in raw:
        return None
    sides = ["left"] + (["mid"] if "mid" in raw else []) + ["right"]
    cols = []
    for side in sides:
        c = raw.get(side) or {}
        if not isinstance(c, dict):
            report.warn(f"[столбцы] {sl.sid}: `{side}` не словарь")
            return None
        label = str(c.get("label") or c.get("head") or "").strip()
        items = [str(i).strip() for i in (c.get("items") or [])
                if str(i).strip()]
        cols.append({"head": label, "items": items})
    return cols


def table_from(sl):
    """Поле `table` (`headers:`/`rows:`) → список списков для
    `tables.draw_table`. Этого поля НЕ знает ни `slidefile`, ни любой
    другой модуль ядра — список полей фронтматтера в `deckkit/README.md`
    кончается на `matrix_empty`/`headline_number`. У ядра есть готовая
    отрисовка таблицы (`tables.draw_table`), ей не хватает только перевода
    словаря `{headers, rows}` в список списков — переводчик здесь, а не в
    ядре: это раскладка одной лекции, а не общее свойство файла кадра."""
    raw = sl.meta.get("table")
    if not isinstance(raw, dict):
        return None
    headers = [str(h) for h in (raw.get("headers") or [])]
    rows = raw.get("rows") or []
    if not headers or not rows:
        report.warn(f"[таблица] {sl.sid}: поле `table` без headers/rows — "
                    "не рисуется")
        return None
    return [headers] + [[str(c) for c in r] for r in rows]


# ════════════════════════════════════════════════════════════════════
# четыре раскладки: обложка · закрытие(через content) · дивайдер · Q&A ·
# содержательный кадр
# ════════════════════════════════════════════════════════════════════


def cover(p, sl, root):
    """`hero_cover` — s01. Hero-снимок по центру тела (см.
    `place_hero_centered`), видимое тело обложки — `slidefile.body_blocks`,
    как у `refdeck.cover`."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "hero_cover")
    bb = body_bot(sl)
    img = resolve_media(sl.meta, root, sl.sid)
    hero = img is not None
    ty, gy, tw = 1.70, 1.28, FULL_W
    if hero:
        x_box, _bot, y_top = place_hero_centered(s, sl, img, bb)
        tw = x_box - COL_GAP - MX
        ty = max(1.10, y_top + 0.30)
        gy = max(0.40, ty - 0.42)
    else:
        report.warn(f"[кадр] {sl.sid}: hero_cover без снимка — §5.9 не "
                    "может быть выполнен")
    runs = []
    for i, (kind, t) in enumerate(slidefile.body_blocks(sl)):
        sz = {"head": 34.0, "cap": 15.0}.get(kind, 17.0)
        for j, r in enumerate(markup.inline_runs(
                t, sz, DEEP if kind != "cap" else LIGHT)):
            r.setdefault("italic", kind == "cap")
            r["newpara"] = bool(i and j == 0)
            if r["newpara"]:
                r["space_before"] = 12
            runs.append(r)
    if runs:
        prims.text_runs(s, MX, ty, tw, (bb - ty) if hero else 4.20,
                        runs, ls=1.22, tag=f"{sl.sid}/обложка")
    prims.rect(s, MX, gy, 1.60, 0.07, GOLD, count="акцент")
    report.GOLD_SEEN.add(sl.sid)
    footer(s, sl)
    return s


_NAMED_ITEM = re.compile(r"(?=\*\*[^*]+\*\*\s+—\s)")


def split_named_items(t):
    """Разрез абзаца «**ИМЯ** — текст **ИМЯ2** — текст2 …» на отдельные
    строки по границе каждого именованного пункта — ЧИСТО РАСКЛАДКА, слова
    не меняются и не добавляются, меняется только то, где `text_runs`
    ставит разрыв абзаца.

    Зачем это здесь: `slidefile.body_blocks` режет тело на абзацы только по
    ПУСТОЙ строке файла, а перечень разборов раздела на `s14`/`s26`/`s37`/
    `s49` («По порядку: **AEGIS** — … **SPOC** — … **COROB-X** — …
    **LeoLabs** — …») в файле стоит четырьмя строками ПОДРЯД, без пустых
    строк между ними (так читается с листа и так утверждён владельцем на
    Phase 5 — трогать файл этой задаче не разрешено). Без разреза здесь
    абзацный разбор схлопывает перенос строки в пробел
    (`blk.replace("\\n", " ")`) и отдаёт раскладке одну длинную строку —
    первая сборка так и показала: «AEGIS — … SPOC — … COROB-X — … LeoLabs
    — …» сплошным текстом, который зал читает как абзац, а не как список."""
    parts = [p.strip() for p in _NAMED_ITEM.split(t) if p.strip()]
    return parts if len(parts) > 1 else [t]


def divider(p, sl, root):
    """`divider` — s14/s26/s37/s49. Левая цветная полоса держит
    идентичность раздела; фотография раздела (не hero — у дивайдеров этой
    лекции `media_hero` не объявлен ни разу) встаёт боковой колонкой
    справа, текст — слева от неё, тем же путём, что боковая иллюстрация
    содержательного кадра."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.rect(s, 0, 0, 0.17, SLIDE_H, MID, count="полоса")
    check_prims(sl, "divider")
    bb = body_bot(sl)
    img = resolve_media(sl.meta, root, sl.sid)
    body_x = MX + 0.22
    body_w = FULL_W - 0.22
    img_box = None
    if img:
        mw, mh = media.media_box_size(media.img_ar(img, sl.sid),
                                      DIVIDER_IMG_W, DIVIDER_IMG_H)
        body_w = FULL_W - 0.22 - mw - COL_GAP
        img_box = (body_x + body_w + COL_GAP, 0.95, mw, mh)
    y = 1.05
    for kind, t in slidefile.body_blocks(sl):
        if kind == "head":
            sz = metrics.fit_size(t, body_w, 1.05, hi=30.0, lo=20.0,
                                  floor=16.0, bold=True, ls=1.10,
                                  tag=f"{sl.sid}/дивайдер-имя")
            h = metrics.est_h(t, sz, body_w, 1.10, True)
            prims.text_box(s, body_x, y, body_w, h, t, size=sz, bold=True,
                           color=DEEP, ls=1.10, tag=f"{sl.sid}/дивайдер-имя")
            y += h + 0.10
            gold_tick(s, sl.sid, body_x, y)
            y += 0.30
        else:
            runs = []
            for i, part in enumerate(split_named_items(t)):
                piece = markup.inline_runs(part, 15.5, DEEP)
                if i:
                    piece[0]["newpara"] = True
                    piece[0]["space_before"] = 6
                runs.extend(piece)
            h = metrics.runs_h(runs, body_w, 1.24)
            prims.text_runs(s, body_x, y, body_w, h + 0.04, runs, ls=1.24,
                            tag=f"{sl.sid}/дивайдер-тело")
            y += h + 0.18
        if y > bb - 0.2:
            report.warn(f"[высота] {sl.sid}/дивайдер: текст дошёл до "
                        f"подвала — {y:.2f}\" при пределе {bb:.2f}\"")
            break
    if img_box:
        media.draw_media(s, sl.sid, img, *img_box)
    footer(s, sl)
    return s


def qa(p, sl, root):
    """`qa` — s69, единственный кадр. Отдельный Q&A-кадр по паттерну курса
    (не merged в закрытие) — большое центрированное слово в коробке мотива,
    золото рядом снизу."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "qa")
    text = sl.title or "Вопросы"
    box_w, box_h = 7.4, 2.7
    box_x, box_y = (SLIDE_W - box_w) / 2, (SLIDE_H - box_h) / 2 - 0.25
    prims.ocean_box(s, box_x, box_y, box_w, box_h)
    sz = metrics.fit_size(text, box_w - 0.6, 1.5, hi=48.0, lo=32.0,
                          floor=28.0, bold=True, ls=1.05,
                          tag=f"{sl.sid}/qa")
    prims.text_box(s, box_x + 0.3, box_y + (box_h - 1.5) / 2, box_w - 0.6,
                   1.5, text, size=sz, bold=True, color=DEEP,
                   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.05,
                   tag=f"{sl.sid}/qa-текст")
    prims.rect(s, box_x + box_w / 2 - 0.8, box_y + box_h - 0.14, 1.6, 0.07,
              GOLD, count="акцент")
    report.GOLD_SEEN.add(sl.sid)
    footer(s, sl)
    return s


def content(p, sl, root):
    """Содержательный кадр: заголовок · плашки · схема · столбцы · таблица
    · тело · подвал. `hero_closing` (s68) идёт сюда же, не через `cover`:
    `media_hero` на нём читается тем же путём, что на любом другом
    содержательном кадре, и это даёт ему доступ к плашкам/схеме (которых у
    s68 нет, но у будущего hero-кадра этой лекции могли бы быть).

    ПЛАШКИ/СХЕМА/СТОЛБЦЫ/ТАБЛИЦА РИСУЮТСЯ ДО боковой иллюстрации и НА ПОЛНУЮ
    ширину кадра (не на суженную боковым снимком `body_w`) — правка
    визуального цикла, итерация 2. Разборы этой лекции (`case_study`) несут
    и 4 плашки, и боковую фотографию одновременно; первая сборка сужала
    плашки до ширины боковой колонки СРАЗУ, и значения вида «вход
    NavCam-стереопара → Rockster → признаки → random forest → ChemCam» не
    укладывались ни на каком кегле (`[ширина]`, 10 кадров). Боковой снимок
    при этом не обязан начинаться на той же высоте, что плашки: он занимает
    место ПОСЛЕ них, рядом с телом-рассказом «Что переехало»/«Честный
    пробел», а не рядом с числовой сводкой."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    if str(sl.meta.get("type") or "") == "case_study":
        # Силуэт-метка роли (ревью кадра #317 §5-6): «Стадия: …» (`norm`) и
        # «Пример: …» (`case_study`) делят один и тот же рецепт «4 плашки
        # 2×2» — взгляд без чтения текста их не различает (главная находка
        # §5-6 ревью). Ни форма №21 (`polosy`, см. отказ выше — она держит
        # НЕСКОЛЬКО сравнений на одной шкале, а не альтернативную раскладку
        # ОДНОГО разбора), ни №26/№33 содержательно не подошли ВСЕМ 13
        # кадрам этой роли: 12 из 13 несут классическую сторону без
        # числа («не существует» либо названа словами), выдумывать его
        # нарушило бы Baseline/Counterfactual Mandate. Правка, меняющая
        # ГЕОМЕТРИЮ плашек, рискует переоткрыть находки `[высота]`
        # (`s19`/`s22`/`s24`), которые пересборка под пол 15 пт уже дала на
        # этом и без того плотном бюджете. Полоса слева — минимальный
        # ДЕЙСТВИТЕЛЬНО силуэтный маркер (тот же приём, что уже держит
        # идентичность раздела у `divider()` ниже), нулевой по высоте и не
        # отнимающий ширины у тела (0,17" при поле `MX=0,55"`): ТИЛ, а не
        # МИД дивайдера — секундарный акцент палитры, почти не занятый в
        # остальной деке (находка §4 ревью кадра: 3 прогона тила на 1205).
        prims.rect(s, 0, 0, 0.17, SLIDE_H, TEAL, count="полоса")
    bb = body_bot(sl)
    img = resolve_media(sl.meta, root, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    col_bot, body_w_top = bb, FULL_W
    if hero:
        # `media_hero_target` — опциональное поле (добавление #317,
        # Фаза 9: 5 новых кадров «большая иллюстрация + разбор», которым
        # нужна площадь больше дефолтных 42% §5.9). Ни один из прежних 71
        # кадров деки это поле не объявляет — без него `place_hero_centered`
        # ведёт себя ТОЧНО как раньше (умолчание 0,42 внутри неё самой).
        raw_target = sl.meta.get("media_hero_target")
        raw_wcap = sl.meta.get("media_hero_wcap")
        kw = {}
        if raw_target:
            kw["target"] = float(raw_target)
        if raw_wcap:
            kw["w_cap"] = float(raw_wcap)
        x_box, col_bot, _y_top = place_hero_centered(s, sl, img, bb, **kw)
        body_w_top = x_box - COL_GAP - MX
        y = heading(s, sl, width=body_w_top)
    else:
        y = heading(s, sl)

    is_content = str(sl.meta.get("type") or "norm") in CONTENT_TYPES
    if not is_content:
        check_prims(sl, str(sl.meta.get("type") or "?"))

    # `polosy:` (форма №21, см. docstring `POLOSY` выше) вместо плашек —
    # НЕ рядом с ними: на кадре, который объявил `polosy`, поле `blocks`
    # не стоит (сверено на `s19` при написании этой правки), и разбор
    # случая несёт ровно ОДНУ форму цены/классики/модели, не две.
    pol = polosy.polosy_of(sl, POLOSY) if is_content else None
    if pol:
        polosy.check(sl.sid, pol, body_w_top)
        y += polosy.draw(s, sl.sid, pol, MX, y, body_w_top,
                         tag=f"{sl.sid}/полосы") + GAP
        pl = []
    else:
        pl = plates.plates_of(sl, PLATES) if is_content else []
    if pl:
        y += plates.draw_plates(s, sl.sid, pl, MX, y, body_w_top, PLATES) + GAP
    sch = scheme.scheme_of(sl, SCHEME) if is_content else None
    if sch:
        scheme.check_scheme(sl.sid, sch, body_w_top, SCHEME)
        y += scheme.draw_scheme(s, sl.sid, sch, MX, y, body_w_top, SCHEME) + GAP

    # Архитектура (устройство механизма, разбор ВНУТРИ боксов) — Фаза 7,
    # issue #317: s18 (SLAM трёх уровней), s30 (контроллер + тёплый старт +
    # предсказательная компенсация), s41 (внимание на сетке погоды).
    arh = arhitektura.arhitektura_of(sl, ARH) if is_content else None
    if arh:
        arhitektura.check_arhitektura(sl.sid, arh, body_w_top, ARH)
        y += arhitektura.draw_arhitektura(s, sl.sid, arh, MX, y,
                                          body_w_top, ARH) + GAP

    # Таймлайн (стадии процесса на одной линии) — Фаза 7: s09 keystone,
    # цепочка DARPA Subterranean Challenge → LAMP 2.0 → COROB-X.
    tml = timeline.timeline_of(sl) if is_content else None
    if tml:
        timeline.check_timeline(sl.sid, tml, body_w_top, _TIME)
        y += timeline.draw_timeline(s, sl.sid, tml, MX, y, body_w_top,
                                    _TIME) + GAP

    cols = columns_from(sl) if is_content else None
    tbl = table_from(sl) if is_content else None

    # Кадр-ТОЛЬКО-таблица (`s11`/`s12`/`s58`/`s59`/`s62`/`s63`/`s66`: ни
    # плашек, ни схемы, ни столбцов) с коротким телом — те же 1-2 жирных
    # вывода-констатации, что в остальной деке даёт «Что переехало» —
    # читаются ДО большой таблицы, не после: это вступительная констатация
    # к реестру/сетке/словарю ниже, а не комментарий к уже увиденному. На
    # `s62`/`s63` это и единственный способ физически дать телу место —
    # 13-строчная таблица при любом кегле съедает всё, что осталось ПОСЛЕ
    # неё, но перед ней есть целая высота заголовка с запасом."""
    body_drawn = False
    pure_table = bool(tbl) and not pl and not sch and not cols
    if pure_table and slidefile.body_blocks(sl):
        runs, first = [], True
        for kind, t in slidefile.body_blocks(sl):
            sz = {"head": 18.0, "cap": 15.0, "bullet": 15.0}.get(kind, 15.0)
            # Разрыв МЕЖДУ абзацами — без него `s63` набрал два отдельных
            # предложения («…не существуют.» + «Два «—» — …») слитно,
            # впритык, без пробела между точкой и следующим словом.
            if not first:
                runs.append({"text": "", "size": sz, "newpara": True,
                             "space_before": 6})
            first = False
            for r in markup.inline_runs(t, sz, LIGHT if kind == "cap"
                                        else DEEP):
                if kind == "cap":
                    r["italic"] = True
                if kind == "head":
                    r["bold"] = True
                runs.append(r)
        if runs:
            # Бюджет по высоте — ПО ОСТАТКУ, не фиксом: таблица `s11`
            # (карта вечера, 4 строки) не нуждается почти ни в чём, а
            # `s62`/`s63` (14 строк со шляпкой) стоят на физическом полу
            # и нуждаются в каждой своей десятой дюйма. Фиксированный
            # бюджет 0,60" душил `s11` («[кегль] ужат до 0.71» — за
            # рабочим пределом), хотя у него было 3-4" свободных; меряем
            # минимум, который таблице нужен НА ПОЛУ кегля, и отдаём телу
            # всё, что сверх него и общего отступа.
            _mw, min_heights, _mr = tables.table_geom(
                tbl, tables.TBL_FLOOR, body_w_top)
            min_table_h = sum(min_heights)
            intro_budget = max(0.45, min(1.40,
                               (col_bot - y) - min_table_h - 0.12))
            metrics.fit_runs(runs, body_w_top - 0.08, intro_budget, ls=1.20,
                             tag=f"{sl.sid}/тело-вступление", proj_base=None)
            floor.check_runs(runs, f"{sl.sid}/тело-вступление")
            h = metrics.runs_h(runs, body_w_top - 0.08, 1.20)
            prims.text_runs(s, MX + 0.04, y, body_w_top - 0.08, h, runs,
                            ls=1.20, tag=f"{sl.sid}/тело-вступление")
            y += h + 0.12
            body_drawn = True

    if cols:
        # Таблица, идущая СЛЕДОМ за столбцами на одном кадре (`s24`:
        # «что дало/потребовало» + накопительная карта стадии), не
        # получает места, если столбцы берут весь свой потолок МАХ_Н —
        # первая сборка дала на `s24` таблицу 1,88" при пределе 1,76" и
        # отрицательный остаток под тело. Прижатие к голому МИН_Н (1,55")
        # лечило это чересчур сильно: перечень столбца садился на 9,0 пт
        # (`[пол]`, ниже порога 12 пт) там, где таблица снизу маленькая
        # (3 строки). Резерв под таблицу считается ПО НЕЙ САМОЙ — на
        # разумном кегле 12 пт, не на голом потолке/полу столбцов.
        if tbl:
            # Единственный кадр лекции с ОБОИМИ полями — `s24`. Ни
            # голый потолок (3,40", первая сборка — таблица 1,88" при
            # пределе 1,76"), ни голый `MIN_H` (1,55", вторая сборка —
            # перечень столбца 9,0 пт, ниже пола видимого слоя) не
            # годятся: первый не даёт места ни таблице, ни абзацу-итогу
            # следом («В сумме: …»), второй душит столбец сильнее, чем
            # нужно его собственному контенту (4 коротких пункта на
            # сторону, но у правой — одна длинная фраза). 2,20" —
            # измеренный перебором (`1,55→9,0 пт`, `1,80→9,5`, `2,00→
            # 11,5`, `2,20→ без находок`) наименьший потолок, на котором
            # столбец больше не падает ниже пола, и после него на
            # таблицу (1,68" на 12 пт) и абзац-итог остаётся ~1,5" —
            # с запасом.
            cap = 2.20
        else:
            cap = columns.MAX_H
        ch = max(columns.MIN_H, min(col_bot - y, cap))
        columns.draw_columns(s, sl.sid, cols, MX, y, body_w_top, ch, pary=True)
        y += ch + GAP
    if tbl:
        tag = f"{sl.sid}/таблица"
        # Резерв под тело, идущее СЛЕДОМ за таблицей (`s62`/`s63`: по два
        # жирных вывода-констатации после матрицы) — без него
        # `fit_table_height` честно подбирает кегль, при котором таблица
        # сама влезает впритык, и на вывод под ней не остаётся вовсе
        # (первая версия этой правки: «места под тело не осталось,
        # −0,15"»). Резерв — на 2 коротких жирных строки, не на абзац.
        true_avail = col_bot - y
        has_tail = bool(slidefile.body_blocks(sl)) and not body_drawn
        reserve = 0.60 if has_tail else 0.0
        avail_tbl = max(0.60, true_avail - reserve)
        size = fit_table_height(tbl, BODY_PT, avail_tbl, body_w_top)
        tables.check_cols(tbl, size, body_w_top, tag)
        _w, heights, _rows = tables.table_geom(tbl, size, body_w_top)
        th = sum(heights)
        if th > true_avail + 0.04:
            report.warn(f"[высота] {tag}: таблица не влезает даже на полу "
                        f"кегля {tables.TBL_FLOOR:.0f} пт — {th:.2f}\" при "
                        f"пределе {true_avail:.2f}\"")
        th = tables.draw_table(s, MX, y, tbl, size, body_w_top, tag)
        y += th + GAP

    # Боковая (НЕ hero) иллюстрация — только теперь, рядом с оставшимся
    # телом-рассказом, а не рядом с плашками/схемой/таблицей выше.
    body_w, media_bot, draw_img = body_w_top, 0.0, None
    if not hero and img:
        mw, mh = media.media_box_size(
            media.img_ar(img, sl.sid), sl.media_w or MEDIA_W,
            min(MEDIA_H_CAP, col_bot - y))
        body_w = body_w_top - mw - COL_GAP
        draw_img = (MX + body_w + COL_GAP, y, mw, mh)
        media_bot = y + mh

    avail = col_bot - y
    if body_drawn:
        pass
    elif avail > 0.35:
        runs, first = [], True
        for kind, t in slidefile.body_blocks(sl):
            sz = {"head": 20.0, "cap": 15.0, "bullet": 15.0}.get(kind, 15.0)
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
        if runs:
            wrapped, y_bot = None, media_bot + WRAP_GAP
            if not hero and img and y < media_bot:
                wrapped = wrap.fit_runs_wrap(
                    runs, body_w - 0.08, media_bot - y, FULL_W - 0.08,
                    col_bot - y_bot, body_w - 0.08, avail, ls=1.26,
                    tag=f"{sl.sid}/тело", proj_base=BODY_PT)
            pushed = None
            if not wrapped and not hero and img and y < media_bot:
                pushed = wrap.fit_pushed(
                    runs, FULL_W - 0.08, col_bot - y_bot, body_w - 0.08,
                    avail, ls=1.26, tag=f"{sl.sid}/тело", proj_base=BODY_PT)
            if wrapped or pushed:
                top = wrapped[2] if wrapped else []
                bot = wrapped[3] if wrapped else runs
                box_y = y if wrapped else y_bot
                prims.ocean_box(s, MX - 0.14, box_y - 0.10, FULL_W + 0.28,
                                bb - box_y + 0.10)
                if top:
                    prims.text_runs(s, MX + 0.04, y, body_w - 0.08,
                                    media_bot - y, top, ls=1.26,
                                    tag=f"{sl.sid}/тело-рядом")
                prims.text_runs(s, MX + 0.04, y_bot, FULL_W - 0.08,
                                col_bot - y_bot, bot, ls=1.26,
                                tag=f"{sl.sid}/тело-под")
                floor.check_runs(top + bot, f"{sl.sid}/тело")
            else:
                metrics.fit_runs(runs, body_w - 0.08, avail, ls=1.26,
                                 tag=f"{sl.sid}/тело", proj_base=BODY_PT)
                floor.check_runs(runs, f"{sl.sid}/тело")
                # Коробка мотива — по НАСТОЯЩЕЙ высоте текста после
                # подбора, не по всему остатку кадра `avail`: короткое
                # тело (`s13` — два жирных абзаца, схема уже забрала
                # большую часть высоты) в коробке на весь остаток давало
                # пустой ocean_box на половину слайда («Визуальный
                # баланс», `tools/presentation-build/README.md` — 30%+
                # пустоты выглядит как недостающий контент).
                h_text = min(avail, metrics.runs_h(runs, body_w - 0.08, 1.26))
                prims.ocean_box(s, MX - 0.14, y - 0.10, body_w + 0.28,
                                h_text + 0.20)
                prims.text_runs(s, MX + 0.04, y, body_w - 0.08, h_text,
                                runs, ls=1.26, tag=f"{sl.sid}/тело")
                # s51: обещанный сравнительный визуал («media_needed»),
                # никогда не построенный в Фазе 6 — находка U7 QA-прохода
                # 2026-11-02. Кадр без него почти пуст (одна плашка на
                # весь кадр); под ней достаточно места для столбиков.
                if sl.sid == "s51":
                    draw_chip_scale(s, MX, y + h_text + 0.45, body_w - 0.08)
    elif slidefile.body_blocks(sl):
        report.warn(f"[высота] {sl.sid}/тело: места под тело не осталось "
                    f"({avail:.2f}\") — примитивы съели кадр")
    if draw_img:
        media.draw_media(s, sl.sid, img, *draw_img)
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


BUILDERS = {"hero_cover": cover, "divider": divider, "qa": qa}


# ════════════════════════════════════════════════════════════════════
# сборка деки
# ════════════════════════════════════════════════════════════════════


def build(slides_dir, out, *, root=None, only=None):
    root = root or slides_dir
    p = prims.new_deck()
    n = 0
    for f in slidefile.slide_files(slides_dir, only):
        sl = slidefile.read_slide(f)
        if sl is None:
            continue
        sl.media_w = None
        kind = str(sl.meta.get("type") or "norm").strip()
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
    ap.add_argument("--render", action="store_true",
                    help="ещё PDF и PNG (soffice+pdftoppm, с таймаутом)")
    ap.add_argument("--only", default=None,
                    help="собрать только эти sNN (через запятую) — в "
                    "ОТДЕЛЬНЫЙ файл lec-09-partial.pptx")
    args = ap.parse_args()

    # [#229-14]: частичная сборка НЕ пишет в путь выпуска.
    out = (HERE / "lec-09-partial.pptx") if args.only else OUT

    report.reset()
    n = build(SLIDES_DIR, out, root=LEC_ROOT, only=args.only)
    blocking = report.report(n, out_name=out.name)

    if not args.only:
        from pptx import Presentation
        prs = Presentation(str(out))
        media.check_hero_order(prs, partial=bool(args.only))
        from deckkit import contrast
        rows = contrast.check(prs, tag=out.name)
        bad = [r for r in rows if r["ok"] is False]
        print(f"\nконтраст видимого слоя: прогонов {len(rows)}, ниже "
              f"порога {len(bad)} на {len({r['page'] for r in bad})} кадрах")

    if args.render:
        rc = rnd.render(out, SNAPS)
        if rc:
            return rc

    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
