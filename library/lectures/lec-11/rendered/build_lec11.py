#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дека Лекции 11 («ИИ на заводе: глубина вмешательства и скорость
насыщения», issue #353, содержание — #350/#352) на общем ядре `deckkit`
(issue #229).

Написан по образцу `tools/presentation-build/deckkit/refdeck.py` (образцовая
раскладка ядра) и `library/lectures/lec-09/rendered/build_lec09.py` (самый
свежий настоящий сборщик на этом ядре — геометрия и приём подъёма пола до
15 пт скопированы оттуда буквально), но геометрия и раскладка — свои, под
материал ЭТОЙ лекции: раскладка кадра — дело деки, не ядра
(`deckkit/README.md`, «Что остаётся за декой»).

ПРЕДЫСТОРИЯ. Прежний `deck.yaml` и весь `rendered/` удалены коммитом
`5640476fa2` — это были артефакты старой оси «дискретное/процессное
производство» (issue #338), не совместимые с новым содержанием главы
(issue #350: ось «глубина вмешательства ИИ × скорость насыщения»). 45 файлов
слайдов написаны заново семью параллельными сессиями и прошли независимую
проверку оркестратора (валидный фронтматтер, ровно 2 H2-заголовка, 0 хитов
тайминга/методологии/scaffold-маркеров, все media-пути существуют на диске).
`deck.yaml` собран заново (issue #353) — механический перенос id/file/type/
section/assertion/media из фронтматтера, без придумывания нового содержания.

СВЕРКА ФРОНТМАТТЕРА (сделана перед написанием этого файла): поля `id`/
`type`/`title`/`source`/`media`/`media_hero`/`media_caption`/`blocks:`/
`scheme:`/`columns:`/`matrix_empty`/`arhitektura:`/`figure:`/`itog:` читает
ЯДРО напрямую. Расхождения найдены и закрыты ЗДЕСЬ, в раскладке деки, а не
правкой ядра и не правкой файлов кадров:

1. **`media:` — три разных конвенции пути одновременно.** Большинство
   файлов пишут путь относительно `lec-11/rendered/` (`assets/screenshots/
   foo.jpg` — реальные файлы лежат именно там, `rendered/assets/
   screenshots/`), но `s02`/`s45` пишут путь ОТ КОРНЯ РЕПОЗИТОРИЯ
   (`library/lectures/lec-11/rendered/assets/screenshots/foo.jpg`).
   `media.media_path(meta, root, sid)` умеет только ОДНО правило: абсолютный
   путь — как есть, иначе `root / m`. Чужому правилу молча вернулось бы
   `[кадр]: файла нет`. `resolve_media()` ниже — тонкий переводчик:
   пробует `REPO_ROOT / m`, затем `HERE / m` (= `rendered/` + относительный
   путь), и, если нашёл файл, подставляет в `meta["media"]` УЖЕ абсолютный
   путь — тогда `media.media_path` берёт его веткой «абсолютный, как есть»
   и дальше не трогается вовсе.
2. **`columns:` этой лекции пишет `head` (не `label`)** — `s32`/`s37`, оба
   `type: comparison`. Это СОВПАДАЕТ с тем, что читает `columns.columns_of`
   из ядра напрямую (`require_type="comparison"` по умолчанию), и
   отдельного переводчика (как `columns_from` у Лекции 9) здесь НЕ
   потребовалось — находка, а не предположение, проверена построчным
   чтением обоих файлов перед написанием этого модуля.
3. **`table:` (`headers:`/`rows:`) — поле ВООБЩЕ НЕ ЧИТАЕТСЯ ядром**, тот же
   класс расхождения, что у Лекции 9 — `table_from()` ниже, тонкий
   переводчик словаря `{headers, rows}` в список списков, которого ждёт
   `tables.draw_table`.
4. **`type: hook` (`s01`) и `type: udar` (`s43`) несут РАЗНОЕ содержание**,
   хотя оба используют поле `figure:`. `s01` несёт полноценное видимое тело
   (цитата Маска + строка «а мир тем временем») — то есть это обычный
   содержательный кадр с числом-акцентом, и он идёт через `content()` (тип
   добавлен в `CONTENT_TYPES`, фигура рисуется наравне с плашками/схемой).
   `s43`, наоборот, несёт короткий список-напоминание (5 буллитов) ПОД
   фигурой и плашку-вывод `itog:` ПОД списком — это треть размера обычного
   udar-кадра Лекции 7 (там фигура — единственное содержимое экрана), и
   собственный `udar()` ниже рисует все три слоя (фигура уменьшенным
   стилем → список → `itog`), а не копирует `lec-07.udar()` (та версия
   рисует ТОЛЬКО фигуру и намеренно ругается на непустое тело — здесь тело
   содержательное, и отказ был бы неверным).
5. **`type: keystone` (`s05`) несёт три плашки-опоры + именованный пробел,
   визуально отличный от Ocean rounded box** (бриф автора кадра: «белая
   заливка, серый контур, без золота» — тот же приём, которым Лекция 10
   держала свой «честный пробел»). Это единственный содержательный кадр
   деки, у которого первый абзац тела рисуется в ОТДЕЛЬНОЙ серой рамке, а
   не в общей golden-мотив коробке — `keystone_gap_box()` ниже, вызывается
   только для `sl.sid == "s05"`, остальные content-кадры эту ветку не
   видят.
6. **`type: qa` (`s44`) несёт три карточки-темы резерва**, не один большой
   центрированный вопрос, как у `lec-09.qa()` (там `blocks` не было
   вовсе). Заметки лектора самого файла это подтверждают («Три карточки
   держат только темы...») — собственный `qa()` ниже рисует заголовок +
   курсивную подпись + три плашки темами, используя `plates.draw_plates`
   тем же стилем, что и содержательные кадры.
7. **`s23`/`s29` не объявляют `type:` вовсе** — фронтматтер читается
   `slidefile.read_slide` с умолчанием `"norm"` (как и у любой другой
   лекции курса); деке это ничем не грозит, оба кадра — обычные
   hero-фото-кадры с подписью, `content()` обрабатывает их как любой
   `norm`-кадр с `media_hero: true`.

Запуск:
  python3 build_lec11.py                  — собрать PPTX (по умолчанию)
  python3 build_lec11.py --render         — ещё PDF и PNG (soffice+pdftoppm)
  python3 build_lec11.py --only s01,s45   — собрать ТОЛЬКО эти кадры — в
                                             ОТДЕЛЬНЫЙ файл
                                             (lec-11-partial.pptx), выпуск
                                             не трогается
  python3 build_lec11.py --selftest       — прогнать самопроверку ядра
                                             (deckkit.selftest/.contrast)
"""
import argparse
import re
import sys
from dataclasses import replace
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

HERE = Path(__file__).resolve().parent              # .../lec-11/rendered
LEC_ROOT = HERE.parent                               # .../lec-11
REPO_ROOT = HERE.parents[3]                           # корень репозитория
sys.path.insert(0, str(REPO_ROOT / "tools" / "presentation-build"))

from deckkit import (arhitektura, axis, columns, epohi, figure, floor,  # noqa: E402
                     ikonki, itog, ladder, markup, media, metrics,
                     piktogrammy, plates, polosy, prims, report, scheme,
                     slidefile, tables, timeline, titles, vyvody, wrap)
from deckkit import render as rnd                     # noqa: E402
from deckkit.theme import (DEEP, GOLD, LIGHT, MID, SURFACE, TEAL,  # noqa: E402
                           WHITE, SLIDE_H, SLIDE_W)

# issue #355 §9.1/§9.6/§9.7/§9.8 — апгрейд ядра деки (07-design-review-spec.md
# раздел 9, ветка issue-355-deckkit-core-upgrade, слитая в этот worktree):
# шесть новых форм разбора (timeline/polosy/epohi/piktogrammy/vyvody — свои
# поля фронтматтера; `axis` — через `scheme: kind: shkala`, уже встроено в
# `scheme.KINDS`, прямой импорт здесь только чтобы завести деке свой стиль
# тем же приёмом `_obyortki`, что `build_lec08_v5.py`/`build_lec09.py`) и
# иконки (`ikonki:`, каталог `rendered/assets/icons/`, раздел 7 спеки).
IKON_DIR = HERE / "assets" / "icons"

# ─── ПОЛ КЕГЛЯ ВИДИМОГО СЛОЯ: 15 пт — решение владельца (CLAUDE.md, этот
# бриф: «15pt floor на видимом слое»), тот же приём, что у Лекций 9/10:
# пакет читает `VIS_PT` в момент вызова (`floor.py`, docstring), подъём
# локален этой деке.
floor.VIS_PT = 15.0

SLIDES_DIR = LEC_ROOT / "slides"
OUT = HERE / "lec-11.pptx"
SNAPS = HERE / "snapshots"

# ════════════════════════════════════════════════════════════════════
# геометрия этой деки (копия числовой базы Лекции 9 — материал того же
# класса плотности: разборы случаев с 4 плашками + боковым/hero-фото)
# ════════════════════════════════════════════════════════════════════
MX = 0.55
FULL_W = SLIDE_W - 2 * MX                # 12,23"
TITLE_Y, TITLE_H = 0.40, 0.92
# `TITLE_H_NARROW` — высота-потолок для подбора кегля заголовка, когда
# ширина сужена hero-колонкой (`body_w_top` у фото-кадров s10/s23/s29/s45,
# ~2,9" при `media_hero_target: 0.62`). На такой ширине длинные заголовки
# («ENEOS Materials, площадка Йоккаичи — колонна, которую 840 часов не
# трогал человек», 84 знака) не влезают в одну-две строки на 0,92" ни на
# каком кегле ≥ рабочего предела 19 пт — первая сборка дала БЛОКИРУЮЩЕЕ
# `[кегль]` на четырёх кадрах. Заголовок не короче: три-четыре строки —
# высота растёт, `heading()` ниже возвращает НАСТОЯЩИЙ низ заголовка (как у
# `build_lec09.heading`), а не константу, так что тело просто начинается
# позже на тех же кадрах.
TITLE_H_NARROW = 1.95
BODY_TOP = 1.46
FOOT_BOT = 7.44
# 0,65"→0,95": несколько кадров (`s05`/`s06`/`s26`/`s39`/`s41` — keystone и
# коллажи-перечни, по 4-5 источников через «·») несут строку источника до
# 276 знаков, которая на 15 пт разворачивается в 2 строки (≈0,87" по мере,
# найдено первой сборкой — `[высота].../подвал`). Тот же приём подъёма
# потолка, что `build_lec09.FOOT_H_MAX` (там причина была подъём пола
# кегля; здесь — просто длина самого источника этой лекции).
FOOT_H_MAX = 0.95
FOOT_PT, FOOT_LS = 15.0, 1.12
FOOT_GAP = 0.12
MEDIA_W = 4.30
MEDIA_H_CAP = 3.40
MEDIA_H_CAP_OVERRIDE = {"s31": 5.2}
PHOTO_STRIP_H_OVERRIDE = {"s37": 1.1}
# `s37` делит кадр с `polosy:` (4 пары, легенда, ось, сетка — уже ≈3,6" на
# суженном стиле) — полный `photo_strip` в 1,85" не умещается рядом ни на
# каком бюджете кадра; 1,1" даёт полосе фото узкую, но непустую высоту.
COL_GAP = 0.34
# 0,14"→0,10": четвёртая сборка — несколько плотных case_study/schema_
# layered-кадров (`s22`/`s26`/`s30`) топили тело на 0,16-0,25" уже после
# всех прочих правок; просвет между примитивами — вкус (deckkit/README.md,
# «что всё ещё приближение» п.7), и 0,10" тот же нижний предел, что
# `metodika-podachi/kadr` допускает для «воздуха» внутри одного содержательного
# блока (не между разделами).
GAP = 0.10
HERO_TOP = 0.10
WRAP_GAP = 0.10
BODY_PT = 15.0
TICK_W, TICK_H = 1.05, 0.055

# Содержательные типы этой лекции (deck.yaml): divider/cover/qa/udar идут
# своими раскладками (см. ниже); остальные двенадцать — через `content()`.
CONTENT_TYPES = {"norm", "case_study", "case", "schema_matrix",
                 "schema_layered", "mentions", "regulatory_comparison",
                 "comparison", "summary", "keystone", "hook", "hero_closing"}

# Золото плашки — `1C7293` (LIGHT), не умолчательный GOLD: прожарка
# 2026-10-14, золото `F0AB00` на белом/поверхности 1,99:1/1,85:1 при пороге
# WCAG AA 3,0 (`plates.py`, `PlateStyle.value_key_color`). Палитра курса не
# меняется — золото остаётся обводкой/чертой-акцентом; меняется цвет
# КЛЮЧЕВОГО значения внутри плашки. Тот же приём, что Лекция 9/10.
#
# `max_per_row=2`: разборы этой лекции (`case_study`) несут 4 плашки с
# длинными value/note («75% цепочки · ≈12 dpm», «260 → 2425 → 9766 → 5031
# машин/нед.») — 4 в ряд на кадре с боковым фото душат каждую ширину.
PLATES = replace(plates.DEFAULT, value_key_color=LIGHT, max_per_row=2,
                 label_pt=15.0, note_pt=15.0, value_lo=15.0,
                 value_floor=15.0, pad=0.11)

# Один-единственный ключевой итог архитектурного разбора (`s24`: «840 ч
# автономии · −40% пара») дешевле строкой-буллитом, чем боксовой плашкой —
# тот же приём, что `BULLET_COLLAGE`, но на ОДНОМ элементе: высота плашки
# (поле + подпись + значение + оговорка) ~1,3" против ~0,5" у строки.
BULLET_SINGLE_KEY = {"s24"}

# `ai_by_word=False` — ни один `scheme:` этой лекции не несёт «шаг модели»
# по смыслу ряда (`s13` — хроника эпизода Boeing, шаги — даты, не этапы
# алгоритма); угадывать по слову «модель» было бы ложным золотом.
SCHEME = scheme.SchemeStyle(ai_by_word=False, step_rows=4,
                            step_hi=16.0, step_lo=15.0, lab_pt=15.0,
                            cap_pt=15.0)

columns.HEAD_PT = 15.0
columns.ITEM_HI, columns.ITEM_LO, columns.ITEM_FLOOR = 16.0, 15.0, 15.0

ARH = arhitektura.ArhStyle(role_pt=15.0, head_lo=15.0, line_lo=15.0,
                           line_hi=16.0, vyn_pt=15.0,
                           # `line_rows` 3→5: `s11`/`s24` несут строки
                           # разбора по ~80-140 знаков («политика обучена
                           # методом RL, обучения с подкреплением, заранее
                           # в симуляторе...»), которые не укладываются в
                           # 3 строки на полу 15 пт даже на полной ширине
                           # бокса (один ряд из 4 блоков). Сократить текст
                           # нельзя — контент финален. Поднятый потолок
                           # БЕЗОПАСЕН для блоков, которым и 3 строк
                           # хватало (`s30`): высота считается по
                           # `min(line_rows, фактические_строки)`, то есть
                           # растёт только там, где контенту ДЕЙСТВИТЕЛЬНО
                           # нужно больше строк — замерено здесь (4.24"
                           # вместо 5.71"/6.14" у альтернативы «2×2-грид»,
                           # которую пробовали и отвергли: один ряд из 4 с
                           # поднятым потолком строк дешевле по высоте, чем
                           # разнос на два ряда по два блока).
                           line_rows=5)

ARH_S11 = replace(ARH, role_h=0.56)
# `s11` — единственная архитектура деки, где ярлык роли длиннее одной
# строки («граница алгоритм · человек», 26 знаков) при ширине бокса в
# четверть кадра; `role_h` по умолчанию (0,28") — под ОДНУ строку (форма
# не делит полосу роли на абзацы, `arhitektura.py`). Высота бокса и его
# рисование читают `role_h` из ОДНОГО места (мера и рисование не
# расходятся), поэтому подъём до 0,56" даёт полосе ровно вторую строку без
# правки `arhitektura.py` — тот же приём, что подъём пола кегля.

ARH_S24 = replace(ARH, head_rows=4, line_rows=7)
# `s24` — САМЫЙ дорогой кадр деки по форме «архитектура». Измерено ТРИ
# варианта на реальном содержании (см. `iteration-log.md` § «Форма не
# встала» для полной таблицы):
#   1×4, head_rows=3/line_rows=7           — 5,78", 2 предупреждения о
#                                             нечитаемых строках
#   2×2-грид (широкие боксы)                — 6,14", читается целиком
#   1×4 + перенос самой длинной строки блока
#   2 в `vynoska` (см. `arh_vynoska_split`),
#   head_rows=4/line_rows=7                 — 5,89", читается целиком
# Третий вариант взят: он ДЕШЕВЛЕ грида (на 0,25") и ПОЛНОСТЬЮ читается
# (0 предупреждений `[архитектура]`), в отличие от первого. Ни один из
# трёх не укладывается в номинальный бюджет кадра (≈5,5" между `BODY_TOP`
# и подвалом вместе с плашкой-выводом и телом-разбором) — физический
# дефицит снят частично `BODY_TOP_TIGHT` (см. `heading()`), частично
# остаётся ЧЕСТНЫМ пробелом формы, см. `iteration-log.md`.

# Фигура кадра `s01` (`type: hook`) — ОБЫЧНЫЙ размер содержательного числа
# (не на весь экран, как у `udar`): кадр несёт заголовок + тело-цитату +
# фигуру рядом/под ней. `base_pt`/`note_pt`/`unit_pt` поднят до пола 15.
FIG_HOOK = replace(figure.DEFAULT, val_hi=64.0, val_lo=34.0,
                   unit_pt=16.0, base_pt=15.0, note_pt=15.0, min_h=1.55,
                   pad=0.06)
# `pad` 0,30→0,10: раздел 5 спеки добавил ось-шкалу под цитатой (`s01`) —
# бюджет кадра (заголовок+коробка-число+ось+цитата) не сходится на
# умолчательном поле коробки без того, чтобы срезать цитату или число
# (владелец запретил оба). Поле — раскладка, не содержимое «162».

# Фигура кадра `s43` (`type: udar`, собственная раскладка) — уменьшенная
# относительно `FIG_HOOK`: под ней ещё стоят список-напоминание и
# плашка-вывод `itog:`, бюджет высоты делится на три.
FIG_S43 = replace(figure.DEFAULT, val_hi=36.0, val_lo=28.0, pad=0.16,
                  unit_pt=16.0, base_pt=15.0, note_pt=15.0, min_h=0.95)
# `val_hi` 48→36, `pad` 0,30→0,16: `s43` делит кадр с заметным списком-
# напоминанием и плашкой-выводом — пятая сборка нашла дефицит 0,35" даже
# после общей экономии `GAP`; фигура здесь ВСПОМОГАТЕЛЬНАЯ (не на весь
# кадр, как у Лекции 7), её роль держит одно число, а не заполняет экран.

ITOG = replace(itog.DEFAULT, chip_pt=15.0, text_pt=16.0, text_ls=1.14)

tables.TBL_ROW_MIN = 0.30

# ─── формы раздела 9 апгрейда ядра (issue #355), пол 15 пт тем же приёмом,
# что `PLATES`/`SCHEME`/`ARH` выше — своя именная копия стиля модуля на
# ВСЕ поля, которые модуль реально проверяет `floor.pt(...)` при рисовании
# (не только помеченные в его исходнике «пол видимого слоя»), скопировано
# буквально у `build_lec08_v5.py`/`build_lec09.py`, тех же дек на этом ядре.
TIMELINE = replace(timeline.DEFAULT, unit_pt=15.0, cap_pt=15.0,
                   stage_pt=15.0, head_pt=15.0, txt_pt=15.0, lab_pt=15.0,
                   val_pt=15.0, srok_txt_pt=15.0, end_pt=15.0)
POLOSY = polosy.PolosyStyle(lab_pt=15.0, val_pt=15.0, mn_pt=15.0,
                            leg_pt=15.0, tick_pt=15.0, unit_pt=15.0,
                            cap_pt=15.0, row_gap=0.12, bar_h=0.22,
                            bar_gap=0.06, leg_gap=0.06)
# `row_gap`/`bar_h`/`bar_gap`/`leg_gap` сужены — единственный кадр-носитель
# `polosy:` в этой деке (`s37`) несёт форму НЕ одну на кадре: под ней ещё
# встаёт полоса из 3 фото (раздел 5 спеки) и тело с арифметикой месяца. На
# умолчательных числах форма одна просила 4,72" при бюджете кадра 5,28" —
# тот же приём, что сужение `lane_h`/`lane_gap` оси на `s01`.
EPOHI = epohi.EpohiStyle(label_pt=15.0, step_pt=15.0, vyvod_pt=15.0,
                         step_lo=15.0)
PIKTO = piktogrammy.PiktoStyle(leg_txt_pt=15.0)
VYVODY = vyvody.VyvodyStyle(text_pt=15.0, most_pt=15.0)

# `scheme: kind: shkala` → `axis.py`, уже встроено в `scheme.KINDS` —
# `axis.height`/`.check`/`.draw` зовутся БЕЗ декиного стиля и уходят на
# `axis.DEFAULT` (пол 12 пт). `_obyortki` подменяет эти три модульных
# алиаса декиным стилем, не трогая ни `scheme.py`, ни `axis.py` — тот же
# приём, что `build_lec08_v5._obyortki`/`build_lec09._obyortki`.
AXIS = replace(axis.DEFAULT, lab_pt=15.0, unit_pt=15.0, cap_pt=15.0,
              end_pt=15.0, lane_h=0.46, lane_gap=0.06, tick_h=0.12)
# `lane_h` 0,62→0,46: единственный кадр-носитель оси в этой деке — `s01`
# (hook), где ось стоит ДОПОЛНЕНИЕМ под уже готовой коробкой-числом (162) и
# цитатой, не единственным содержимым кадра, как у Лекции 7/9. На умолчании
# ось одна просила ≈2,6" — на кадре, где фигура + цитата уже стояли
# впритык к подвалу (авторский «низ пуст на ~30%» — slack, не пустой
# бюджет), это сминало цитату до 12 пт и топило её в подвал. Сужение
# дорожки подписи — та же мера, что подъём пола кегля: часть формы, не
# правка её контента.


def _obyortki(mod, st, h_fn, c_fn, d_fn):
    mod.height = lambda d, w: h_fn(d, w, st)
    mod.check = lambda sid, d, w: c_fn(sid, d, w, st)
    mod.draw = lambda s, sid, d, x, y, w, tag=None: d_fn(
        s, sid, d, x, y, w, st, tag=tag)


_obyortki(axis, AXIS, axis.axis_h, axis.check_axis, axis.draw_axis)

# `scheme: kind: lestnitsa` → `ladder.py` (П11, обзорные кадры раздела 4
# спеки) — та же подмена алиасов, пол 15 пт.
LADDER = replace(ladder.DEFAULT, step_hi=17.0, step_lo=15.0, axis_pt=15.0,
                 axis_h=0.30, cap_pt=15.0)
_obyortki(ladder, LADDER, ladder.ladder_h, ladder.check_ladder,
         ladder.draw_ladder)

# Кадры, на которых `ikonki:`/`scheme: kind: lestnitsa` держат кадр
# самостоятельно, без hero/боковой иллюстрации (раздел 4 спеки
# 07-design-review-spec.md: 4 новых обзорных кадра s08a/s16a/s21a/s27a) —
# собственная раскладка `stage_overview()` ниже, не `content()`.
STAGE_OVERVIEW_IDS = {"s08a", "s16a", "s21a", "s27a"}


def fit_table_height(tbl, hi, avail_h, w):
    """Кегль таблицы, подобранный по ВЫСОТЕ (`s03`/`s07`: 4-7 строк со
    шляпкой, ширина столбца укладывается раньше, чем высота). Тот же приём,
    что `build_lec09.fit_table_height`."""
    size = hi
    while size > tables.TBL_FLOOR:
        sz = tables.tbl_size(tbl, size, w)
        _w, heights, _rows = tables.table_geom(tbl, sz, w)
        if sum(heights) <= avail_h:
            return sz
        size -= 0.5
    return tables.TBL_FLOOR


def resolve_media(meta, sid):
    """`media.media_path`, но сначала переводит путь в АБСОЛЮТНЫЙ по трём
    конвенциям этой лекции (см. докстринг файла, пункт 1): путь от корня
    репозитория (`s02`/`s45`), путь от `rendered/` (большинство кадров),
    либо путь от `LEC_ROOT` на случай будущего кадра. Если ничего не
    нашлось — отдаёт исходную (относительную) строку: `media.media_path`
    сам скажет `[кадр]: файла нет`, предупреждение не теряется."""
    m = str(meta.get("media") or "").strip()
    if not m or m in ("none", "None") or Path(m).is_absolute():
        return media.media_path(meta, LEC_ROOT, "")
    for root in (REPO_ROOT, HERE, LEC_ROOT):
        p = root / m
        if p.exists():
            meta["media"] = str(p)
            break
    return media.media_path(meta, LEC_ROOT, "")


# ════════════════════════════════════════════════════════════════════
# общие части кадра
# ════════════════════════════════════════════════════════════════════


def gold_tick(s, sid, x, y):
    prims.rect(s, x, y, TICK_W, TICK_H, GOLD, count="акцент")
    report.GOLD_SEEN.add(sid)


# `s24` — единственный кадр деки, где архитектура (4 блока, читаемая только
# на `head_rows=4`/`line_rows=7`, см. `ARH_S24`) физически не помещается
# между обычным `BODY_TOP` и подвалом вместе с телом-разбором: замерено —
# архитектура одна стоит 5,89", а между `BODY_TOP=1,46` и подвалом (≈7,0)
# всего 5,5". Снятие floor'а заголовка возвращает телу ~0,35" (заголовок
# однострочный, реальная высота меньше отведённой константы) — попытка
# закрыть физический дефицит минимально инвазивным способом, не трогая
# геометрию остальных 44 кадров.
BODY_TOP_TIGHT = {"s24"}


def heading(s, sl, width=None, color=DEEP):
    if not sl.title:
        report.warn(f"[заголовок] {sl.sid}: поле `title` пусто")
        return BODY_TOP
    w = FULL_W if width is None else width
    # Узкая колонка (hero-фото рядом) получает запас по высоте под 3-4
    # строки вместо 1-2 — см. docstring `TITLE_H_NARROW`.
    th_box = TITLE_H if w >= FULL_W - 0.5 else TITLE_H_NARROW
    sz = metrics.fit_size(sl.title, w, th_box, hi=27.0, lo=19.0,
                          floor=15.0, bold=True, ls=1.08,
                          tag=f"{sl.sid}/заголовок")
    th = metrics.est_h(sl.title, sz, w, 1.08, True)
    prims.text_box(s, MX, TITLE_Y, w, th, sl.title, size=sz,
                   bold=True, color=color, ls=1.08, tag=f"{sl.sid}/заголовок")
    sl.tick_y = TITLE_Y + th + 0.07
    floor_y = 0.95 if sl.sid in BODY_TOP_TIGHT else BODY_TOP
    return max(floor_y, sl.tick_y + TICK_H + 0.12)


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
    runs = source_runs(sl)
    if not runs:
        return
    y, h, _bot = foot_geom(sl)
    prims.text_runs(s, MX, y, FULL_W, max(h, 0.3), runs, ls=FOOT_LS,
                    tag=f"{sl.sid}/подвал", quiet=True)


def check_prims(sl, kind, allow=()):
    for f, name in (("blocks", "плашки"), ("scheme", "схема"),
                    ("columns", "столбцы"), ("table", "таблица"),
                    ("matrix_empty", "матрица"), ("arhitektura", "архитектура"),
                    ("figure", "число"), ("itog", "итог")):
        if f in allow:
            continue
        if sl.meta.get(f):
            report.warn(
                f"[{name}] {sl.sid}: поле `{f}` объявлено на кадре типа "
                f"«{kind}» — оно рисуется только на содержательных кадрах")


def place_hero_centered(s, sl, img, body_bot_y, *, target=0.42, w_cap=9.0):
    """Hero-иллюстрация (§5.9, ≥40% площади) по вертикальной середине тела,
    шириной, выведенной из СОБСТВЕННОГО отношения сторон снимка. Тот же
    приём, что `build_lec09.place_hero_centered`."""
    ar = media.img_ar(img, sl.sid) or (16 / 9)
    w = min(w_cap, (target * SLIDE_W * SLIDE_H * ar) ** 0.5)
    box_h = w / ar + 2 * media.HERO_PAD
    y_top = max(HERO_TOP, HERO_TOP + (body_bot_y - HERO_TOP - box_h) / 2)
    x_box, bot = media.place_hero(s, sl.sid, sl.meta, img, SLIDE_W - MX,
                                  y_top, body_bot_y, w)
    return x_box, bot, y_top


def table_from(sl):
    """Поле `table` (`headers:`/`rows:`) → список списков. Этого поля не
    знает ни `slidefile`, ни любой другой модуль ядра — переводчик здесь,
    не в ядре (та же находка и то же решение, что `build_lec09.table_from`)."""
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


def body_runs(sl, sizes=None):
    """Тело кадра → список прогонов `text_runs` понимает. `sizes` —
    переопределение кеглей по виду абзаца (`head`/`cap`/`bullet`/`para`)."""
    sizes = sizes or {}
    runs, first = [], True
    for kind, t in slidefile.body_blocks(sl):
        sz = sizes.get(kind, 15.0)
        if not first:
            runs.append({"text": "", "size": sz, "newpara": True,
                         "space_before": 7})
        first = False
        for r in markup.inline_runs(t, sz, LIGHT if kind == "cap" else DEEP):
            if kind == "cap":
                r["italic"] = True
            if kind == "head":
                r["bold"] = True
            runs.append(r)
    return runs


# ════════════════════════════════════════════════════════════════════
# раскладки: обложка · дивайдер · Q&A · удар (s43) · содержательный кадр
# ════════════════════════════════════════════════════════════════════


def cover(p, sl, root):
    """`cover` — s02. Hero-снимок (цех Amberg) по центру тела, видимое
    тело обложки — `slidefile.body_blocks`, тот же приём, что
    `refdeck.cover`/`build_lec09.cover`."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "cover")
    bb = body_bot(sl)
    img = resolve_media(sl.meta, sl.sid)
    hero = img is not None
    ty, gy, tw = 1.70, 1.28, FULL_W
    if hero:
        x_box, _bot, y_top = place_hero_centered(s, sl, img, bb)
        tw = x_box - COL_GAP - MX
        ty = max(1.10, y_top + 0.30)
        gy = max(0.40, ty - 0.42)
    else:
        report.warn(f"[кадр] {sl.sid}: cover без снимка — §5.9 не может "
                    "быть выполнен")
    runs = []
    for i, (kind, t) in enumerate(slidefile.body_blocks(sl)):
        sz = {"head": 32.0, "cap": 15.0}.get(kind, 17.0)
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
    else:
        # У `s02` фронтматтер несёт `title`/`assertion`, но ЭТУ строку кадр
        # не рисует (см. docstring `build_lec09` про `title` vs `assertion`
        # на обложке) — если файл не дал видимого тела вовсе, обложка
        # осталась бы пустой белой страницей рядом с фото. Подстраховка:
        # заголовок как минимум стоит, если тела нет.
        prims.text_box(s, MX, ty, tw, 2.0, sl.title or "", size=30.0,
                       bold=True, color=DEEP, ls=1.12,
                       tag=f"{sl.sid}/обложка-заголовок")
    prims.rect(s, MX, gy, 1.60, 0.07, GOLD, count="акцент")
    report.GOLD_SEEN.add(sl.sid)
    footer(s, sl)
    return s


_NAMED_ITEM = re.compile(r"(?=\*\*[^*]+\*\*\s+—\s)")


def split_named_items(t):
    """Разрез абзаца «**ИМЯ** — текст **ИМЯ2** — текст2 …» на отдельные
    строки по границе каждого именованного пункта — ЧИСТО РАСКЛАДКА, слова
    не меняются и не добавляются, меняется только то, где `text_runs`
    ставит разрыв абзаца. Порт `build_lec09.split_named_items` — у ЭТОЙ
    лекции ВСЕ 5 дивайдеров несут перечень разборов раздела тем же приёмом
    («**Audi Neckarsulm** — … **Boeing 737 MAX 9** — …» четырьмя строками
    подряд БЕЗ пустой строки между ними, так читается с листа и так
    утверждено владельцем на Phase 5 — трогать файл этой задаче не
    разрешено). Без разреза здесь `slidefile.body_blocks` схлопывает
    перенос строки в пробел и отдаёт один длинный абзац, который на `s08`
    первая сборка показала буквально: «Audi Neckarsulm — контроль сварных
    точек кузова моделью Boeing 737 MAX 9 — разбор подмены…» — связный
    текст читается так, будто Boeing 737 MAX 9 — это модель контроля Audi,
    а не второй, отдельный разбор раздела."""
    parts = [p.strip() for p in _NAMED_ITEM.split(t) if p.strip()]
    return parts if len(parts) > 1 else [t]


def divider(p, sl, root):
    """`divider` — s08/s16/s21/s27/s38. Левая цветная полоса держит
    идентичность раздела. `s08` несёт боковую фотографию раздела (цех
    Audi) — та же боковая колонка, что у содержательного кадра; остальные
    четыре дивайдера — текстовые переходы без снимка (честно не поставлены
    во фронтматтере, см. `media_needed` каждого файла)."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.rect(s, 0, 0, 0.17, SLIDE_H, MID, count="полоса")
    check_prims(sl, "divider")
    bb = body_bot(sl)
    img = resolve_media(sl.meta, sl.sid)
    body_x = MX + 0.22
    body_w = FULL_W - 0.22
    img_box = None
    if img:
        mw, mh = media.media_box_size(media.img_ar(img, sl.sid), 4.60, 3.60)
        body_w = FULL_W - 0.22 - mw - COL_GAP
        img_box = (body_x + body_w + COL_GAP, 0.95, mw, mh)
    y = 0.90
    blocks_left = len(slidefile.body_blocks(sl))
    for kind, t in slidefile.body_blocks(sl):
        blocks_left -= 1
        if kind == "head":
            sz = metrics.fit_size(t, body_w, 1.05, hi=30.0, lo=20.0,
                                  floor=16.0, bold=True, ls=1.10,
                                  tag=f"{sl.sid}/дивайдер-имя")
            h = metrics.est_h(t, sz, body_w, 1.10, True)
            prims.text_box(s, body_x, y, body_w, h, t, size=sz, bold=True,
                           color=DEEP, ls=1.10, tag=f"{sl.sid}/дивайдер-имя")
            y += h + 0.08
            gold_tick(s, sl.sid, body_x, y)
            y += 0.20
        else:
            runs = []
            for i, part in enumerate(split_named_items(t)):
                piece = markup.inline_runs(part, 15.5, DEEP)
                if i:
                    piece[0]["newpara"] = True
                    piece[0]["space_before"] = 6
                runs.extend(piece)
            # issue #355 §9.1: тело дивайдера меряется и ужимается ДО
            # рисования (`fit_runs` до пола видимого слоя), а не рисуется
            # на фиксированном кегле с клипом по месту постфактум — живой
            # пример дефекта был здесь же, s21, длинный перечень раздела 3.
            # Резерв под ОСТАЛЬНЫЕ блоки ниже — 0,22" на блок, грубая, но
            # ненулевая оценка (голый `bb - y` отдавал ВЕСЬ остаток текущему
            # блоку и оставлял последующим пустое место, то есть ровно
            # тот клип, который эта правка снимает).
            reserve = 0.22 * blocks_left
            avail = max(0.3, bb - y - reserve)
            metrics.fit_runs(runs, body_w, avail, ls=1.24,
                             tag=f"{sl.sid}/дивайдер-тело", proj_base=15.5)
            floor.check_runs(runs, f"{sl.sid}/дивайдер-тело")
            h = min(avail, metrics.runs_h(runs, body_w, 1.24))
            prims.text_runs(s, body_x, y, body_w, h + 0.04, runs, ls=1.24,
                            tag=f"{sl.sid}/дивайдер-тело", quiet=True)
            y += h + 0.10
        if y > bb - 0.2:
            report.warn(f"[высота] {sl.sid}/дивайдер: текст дошёл до "
                        f"подвала — {y:.2f}\" при пределе {bb:.2f}\"")
            break
    if not sl.title and not slidefile.body_blocks(sl):
        report.warn(f"[заголовок] {sl.sid}: дивайдер без заголовка и без "
                    "тела — пустой кадр")
    if img_box:
        media.draw_media(s, sl.sid, img, *img_box)
    footer(s, sl)
    return s


def qa(p, sl, root):
    """`qa` — s44, собственная раскладка (не `refdeck.qa`/`build_lec09.qa`):
    этот кадр несёт три плашки-темы резерва, а не один центрированный
    вопрос (см. докстринг файла, пункт 6 — заметки самого кадра: «три
    карточки держат только темы»)."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "qa", allow=("blocks",))
    title = sl.title or "Вопросы"
    sz = metrics.fit_size(title, FULL_W, 1.2, hi=44.0, lo=30.0, floor=28.0,
                          bold=True, ls=1.05, tag=f"{sl.sid}/qa-заголовок")
    th = metrics.est_h(title, sz, FULL_W, 1.05, True)
    y = 1.30
    prims.text_box(s, MX, y, FULL_W, th, title, size=sz, bold=True,
                   color=DEEP, align=PP_ALIGN.CENTER, ls=1.05,
                   tag=f"{sl.sid}/qa-заголовок")
    y += th + 0.12
    caps = [t for k, t in slidefile.body_blocks(sl) if k == "cap"]
    if caps:
        ch = metrics.est_h(caps[0], 16.0, FULL_W, 1.18, italic=True)
        prims.text_box(s, MX, y, FULL_W, ch, caps[0], size=16.0, italic=True,
                       color=LIGHT, align=PP_ALIGN.CENTER, ls=1.18,
                       tag=f"{sl.sid}/qa-подпись")
        y += ch + 0.35
    else:
        y += 0.35
    prims.rect(s, SLIDE_W / 2 - 0.8, y, 1.6, 0.07, GOLD, count="акцент")
    report.GOLD_SEEN.add(sl.sid)
    y += 0.40
    pl = plates.plates_of(sl, PLATES)
    if pl:
        bb = body_bot(sl)
        pw = min(FULL_W, 9.60)
        px = MX + (FULL_W - pw) / 2
        plates.draw_plates(s, sl.sid, pl, px, y, pw, PLATES)
    footer(s, sl)
    return s


def udar(p, sl, root):
    """`udar` — s43, собственная раскладка (не `lec-07.udar()`): эта
    фигура делит кадр с видимым списком-напоминанием и плашкой-выводом
    `itog:`, а не стоит единственным содержимым экрана (см. докстринг
    файла, пункт 4). Заголовок · фигура (уменьшенный стиль `FIG_S43`) ·
    список-напоминание · `itog`-плашка · подвал."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "udar", allow=("figure", "itog", "piktogrammy"))
    y = heading(s, sl)
    bb = body_bot(sl)
    fig = figure.figure_of(sl, FIG_S43)
    pik = piktogrammy.pikto_of(sl, st=PIKTO)
    pik_h = piktogrammy.pikto_h(pik, FULL_W, PIKTO) if pik else 0.0
    it = itog.itog_of(sl, st=ITOG)
    it_h = itog.itog_h(it, FULL_W, ITOG) if it else 0.0
    list_runs = body_runs(sl, {"bullet": 15.0, "para": 15.0})
    list_h = metrics.runs_h(list_runs, FULL_W - 0.08, 1.22) if list_runs else 0.0
    if fig:
        figure.check_figure(sl.sid, fig, FULL_W, FIG_S43)
        fig_h = figure.figure_h(fig, FULL_W, FIG_S43)
        avail = bb - y
        reserve = (pik_h + (GAP if pik else 0) + list_h
                  + (GAP if list_runs else 0) + it_h + (GAP if it else 0))
        if fig_h > avail - reserve + 0.02:
            report.warn(
                f"[высота] {sl.sid}/удар: фигура+пиктограммы+список+итог "
                f"заняли бы {fig_h + reserve:.2f}\" при {avail:.2f}\" "
                "свободных — фигура сжата до пола, но может не влезть")
        figure.draw_figure(s, sl.sid, fig, MX, y, FULL_W, FIG_S43)
        y += fig_h + GAP
    else:
        report.warn(f"[число] {sl.sid}: кадр-удар без поля `figure` — "
                    "ударять нечем")
    if pik:
        piktogrammy.check_pikto(sl.sid, pik, FULL_W, PIKTO)
        piktogrammy.draw_pikto(s, sl.sid, pik, MX, y, FULL_W, PIKTO)
        y += pik_h + GAP
    if list_runs:
        metrics.fit_runs(list_runs, FULL_W - 0.08, bb - (it_h + GAP if it else 0) - y,
                         ls=1.22, tag=f"{sl.sid}/список", proj_base=BODY_PT)
        floor.check_runs(list_runs, f"{sl.sid}/список")
        lh = metrics.runs_h(list_runs, FULL_W - 0.08, 1.22)
        prims.text_runs(s, MX + 0.04, y, FULL_W - 0.08, lh, list_runs,
                        ls=1.22, tag=f"{sl.sid}/список")
        y += lh + GAP
    if it:
        itog.check_itog(sl.sid, it, FULL_W, ITOG)
        iy = max(y, bb - it_h)
        itog.draw_itog(s, sl.sid, it, MX, iy, FULL_W, ITOG,
                       tag=f"{sl.sid}/итог")
        report.GOLD_SEEN.add(sl.sid)
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


def keystone_gap_box(s, sid, text, x, y, w):
    """Полоса именованного пробела — визуально ОТЛИЧНАЯ от Ocean rounded
    box по явной просьбе автора кадра (`s05` `media_needed`): белая
    заливка, серый контур, БЕЗ золота. Тот же приём, которым Лекция 10
    держала свой «честный пробел» (см. CLAUDE.md, упоминания Лекции 10)."""
    sz = 15.0
    h = metrics.est_h(text, sz, w - 0.28, 1.22) + 0.20
    prims.rect(s, x, y, w, h, WHITE, stroke=MID, stroke_pt=1.25)
    prims.text_runs(s, x + 0.14, y + 0.10, w - 0.28, h - 0.20,
                    markup.inline_runs(text, sz, DEEP), ls=1.22,
                    tag=f"{sid}/пробел")
    return h


# Кадры-«коллажи» (5-6 плашек коротких чисел с длинными оговорками,
# обязательный разброс по §5.13 «упоминания без базы»): `s06`/`s19`/`s20`/
# `s39`/`s41`. Боксовая полоса плашек — ядро само об этом говорит мерой
# (`plates_h`), не вкусом — не укладывается даже на наименьшей высоте по
# `max_per_row` ни на одном из трёх вариантов (замерено до правки:
# `s06` 5,27"-6,27" при бюджете под плашки+тело ≈4,99"). Бюджет плашки
# тратят на подпись/значение/оговорку ТРЕМЯ типографскими ярусами и полем
# `pad` на каждый ряд — перечень из тех же слов одной строкой-буллитом
# (жирный ярлык — значение — оговорка) даёт то же утверждение БЕЗ этого
# оверхеда. Это раскладка, не контент: слова label/value/note переносятся
# буквально, просто без боксов.
BULLET_COLLAGE = set()
# Раздел 5 спеки (issue #353): все кадры анти-формы BULLET_COLLAGE
# переведены на `plates.COMPACT`/`best_plate_style`/новые формы ядра
# (`COMPACT_PLATES`, `ikonki:`, `itog:` и т. д.) по отдельности, ниже по
# файлам кадров. Множество оставлено пустым (не удалено) — единственное
# место, которое проверяется, если на какой-то кадр снова понадобится
# анти-форма вместо плашек.
# Раздел 5/9 спеки 07-design-review-spec.md (issue #353/#355): `plates.
# COMPACT` — пресет, который `BULLET_COLLAGE` пыталось заменить ДО того,
# как ядро научилось ужиматься (issue #355 §9.8, `note_truncate`/
# `label_value_oneline`). Кадры этого множества возвращены В ПЛАШКИ, но
# компактным пресетом (пол 15 пт тем же приёмом, что `PLATES`), а не
# текстовым перечнем: числа снова читаются блочками, а не абзацем.
PLATES_COMPACT = replace(plates.COMPACT, label_pt=15.0, value_hi=20.0,
                        value_lo=15.0, value_floor=15.0, note_pt=15.0)
COMPACT_PLATES = {"s06", "s19", "s33", "s35", "s40", "s17"}
PLATES_FORCE_SINGLE_COL = {"s33", "s35", "s40", "s17"}
# `s22`/`s26`/`s30` — не коллажи по смыслу (это §5.13 «цена ошибки →
# классика → модель → устройство» на `case_study`/`schema_layered`), но
# измерены (`plates.plates_h`) той же мерой: 4 плашки с оговорками до
# 209 знаков стоят 4,5-5,0" на ЛЮБОМ `max_per_row`, и тело-разбор («что
# переехало» / «честный пробел» — обязательная часть формы §5.13) не
# остаётся места. Строка-буллит даёт то же утверждение за ~3,1" — пятая
# сборка, находка по факту замера, не по плану.


def plates_as_list(sl, pl, w, sz=15.0):
    """`blocks:` → список прогонов `text_runs` одной строкой-буллитом на
    плашку: **ярлык** — значение — оговорка (курсивом). См. docstring
    `BULLET_COLLAGE`."""
    runs = []
    for i, p in enumerate(pl):
        if i:
            runs.append({"text": "", "size": sz, "newpara": True,
                         "space_before": 6})
        bullet = "• " if p["label"] or p["value"] else ""
        runs.append({"text": bullet + (p["label"] + " — " if p["label"]
                     else ""), "size": sz, "bold": True, "color": DEEP})
        if p["value"]:
            runs.append({"text": p["value"] + (". " if p["note"] else ""),
                         "size": sz, "bold": bool(p["key"]),
                         "color": LIGHT if p["key"] else DEEP})
        if p["note"]:
            runs.append({"text": p["note"], "size": sz, "italic": True,
                         "color": LIGHT})
    return runs


def arh_vynoska_split(arh, block_idx, min_chars=120):
    """Самая длинная строка разбора блока `block_idx` → `vynoska`, если
    блок несёт больше одной строки и кадр ещё не объявил свою выноску.

    Раскладочный перенос, не правка контента: слова не меняются, переходит
    только ТО, каким примитивом ядра эта строка нарисована — внутри узкого
    бокса (четверть ширины кадра, где строка в ~150 знаков не укладывается
    ни на каком разумном числе строк, см. `ARH_S24`) или отдельной полосой
    во всю ширину кадра под рядом боксов (`arhitektura.vyn_h`/`draw`,
    контракт `vynoska: {at, text}` уже встроен в ядро для ИМЕННО такого
    случая — см. `arhitektura.py`, докстринг модуля)."""
    if arh.get("vynoska"):
        return arh
    blocks = [dict(b) for b in arh["blocks"]]
    b = blocks[block_idx]
    lines = list(b.get("lines") or [])
    if len(lines) < 2:
        return arh
    longest_i = max(range(len(lines)), key=lambda i: len(lines[i]))
    if len(lines[longest_i]) < min_chars:
        return arh
    text = lines.pop(longest_i)
    b["lines"] = lines
    blocks[block_idx] = b
    return {"blocks": blocks, "vynoska": {"at": block_idx, "text": text}}


def best_plate_style(pl, w, base=PLATES):
    """Какой `max_per_row` даёт МЕНЬШУЮ суммарную высоту полосы для ЭТИХ
    плашек на ЭТОЙ ширине — мера, а не правило по памяти (ядро само это
    заповедует: «форма меряется до рисования», `README-formy.md` §
    «Общий договор формы»).

    Находка этой деки: четыре плашки `case_study` с длинными цепочками
    значений («вход ≈200 переменных → модель → инженер ОТК») выигрывают от
    `max_per_row=2` (приём Лекции 9) — но плашки-«коллажи» (`s06`/`s19`/
    `s20`/`s39`/`s41`, 4-6 штук с короткими числами и длинными оговорками)
    на ДВУХ в ряд уходят в 3 строки и топят тело кадра (замерено первой
    сборкой — семь `[высота]/тело: места не осталось`). Единого числа для
    всей деки, как у Лекции 9, здесь не подошло: пробуем 4·3·2 и берём
    наименьшую высоту для КАЖДОГО кадра отдельно."""
    if not pl:
        return base
    scored = [(plates.plates_h(pl, w, st), st)
              for st in (replace(base, max_per_row=n) for n in (4, 3, 2))]
    return min(scored, key=lambda t: t[0])[1]


def lecture_map(p, sl, root):
    """`map_cards` — s03 (раздел 5 спеки `07-design-review-spec.md`, П1:
    «карта лекции карточками с мини-фото, не таблицей», образец Л10 k-03).
    Сетка 3×2 карточек (не ряд из 6 — на ширине кадра курса ряд из 6 даёт
    ~1,85" на карточку, фото+номер+термин+«что держит» не читаются; та же
    раскладочная правка, что `ikonki.draw_grid`): номер + термин отрасли +
    строка «что держит» + мини-фото раздела. Поле `table:` снято — П1 прямо
    требует заменить таблицу карточками, а не держать обе формы разом."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "map_cards", allow=("map_cards",))
    y = heading(s, sl)
    bb = body_bot(sl)
    cards = sl.meta.get("map_cards") or []
    cols, gap = 3, 0.22
    cw = (FULL_W - (cols - 1) * gap) / cols
    img_h = 1.15
    txt_h = 1.55
    card_h = img_h + 0.08 + txt_h
    rows = -(-len(cards) // cols)
    grid_h = rows * card_h + (rows - 1) * gap
    avail = bb - y
    if grid_h > avail + 0.02:
        report.warn(f"[карта] {sl.sid}: сетка карточек просит "
                    f"{grid_h:.2f}\" при {avail:.2f}\" свободных")
    extra = avail - grid_h
    if extra > 0.3:
        y += extra / 2
    for i, c in enumerate(cards):
        col, row = i % cols, i // cols
        cx = MX + col * (cw + gap)
        cy = y + row * (card_h + gap)
        prims.ocean_box(s, cx, cy, cw, card_h)
        img = media.media_path(c, [REPO_ROOT, HERE, LEC_ROOT], f"{sl.sid}/карточка{i + 1}")
        if img:
            prims.add_image_cover(s, img, cx + 0.06, cy + 0.06, cw - 0.12,
                                  img_h, tag=f"{sl.sid}/карточка{i + 1}")
        else:
            prims.ocean_box(s, cx + 0.06, cy + 0.06, cw - 0.12, img_h,
                            fill=SURFACE)
        ty = cy + img_h + 0.14
        term = f"{c.get('n', '')}. {c.get('term', '')}".strip(". ")
        th = metrics.est_h(term, 14.0, cw - 0.16, 1.10, True)
        prims.text_box(s, cx + 0.08, ty, cw - 0.16, th, term, size=14.0,
                       bold=True, color=DEEP, ls=1.10,
                       tag=f"{sl.sid}/карточка{i + 1}-термин")
        dh = metrics.est_h(c.get("derzhit", ""), 12.0, cw - 0.16, 1.14,
                          italic=True)
        prims.text_box(s, cx + 0.08, ty + th + 0.05, cw - 0.16,
                       min(dh, card_h - (ty + th + 0.05 - cy) - 0.05),
                       c.get("derzhit", ""), size=12.0, italic=True,
                       color=LIGHT, ls=1.14, tag=f"{sl.sid}/карточка{i + 1}-держит")
    y += grid_h + GAP
    runs = body_runs(sl, {"head": 20.0, "cap": 15.0, "bullet": 15.0})
    if runs:
        avail2 = bb - y
        if avail2 > 0.35:
            metrics.fit_runs(runs, FULL_W - 0.08, avail2, ls=1.26,
                             tag=f"{sl.sid}/тело", proj_base=BODY_PT)
            floor.check_runs(runs, f"{sl.sid}/тело")
            h_text = min(avail2, metrics.runs_h(runs, FULL_W - 0.08, 1.26))
            prims.ocean_box(s, MX - 0.14, y - 0.10, FULL_W + 0.28,
                            h_text + 0.20)
            prims.text_runs(s, MX + 0.04, y, FULL_W - 0.08, h_text, runs,
                            ls=1.26, tag=f"{sl.sid}/тело")
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


def term_cards(p, sl, root):
    """`terms` — s04 (раздел 5 спеки, П·словарь): рамка с 7 абзацами →
    2 колонки × 3 термино-карточки с иконкой. Текст определений не
    меняется, только раскладка (та же оговорка, что у `lecture_map`/s03)."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "term_cards", allow=("terms",))
    y = heading(s, sl)
    bb = body_bot(sl)
    items = sl.meta.get("terms") or []
    cols, gap = 2, 0.28
    cw = (FULL_W - (cols - 1) * gap) / cols
    rows = -(-len(items) // cols)
    row_h = (bb - y - (rows - 1) * gap) / max(rows, 1)
    icon_size = 0.36
    for i, it in enumerate(items):
        col, row = i % cols, i // cols
        cx = MX + col * (cw + gap)
        cy = y + row * (row_h + gap)
        prims.tint_box(s, cx, cy, cw, row_h, tone="light")
        has_icon = ikonki.draw_icon(s, IKON_DIR, it.get("icon"), cx + 0.12,
                                    cy + 0.12, icon_size,
                                    tag=f"{sl.sid}/термин{i + 1}")
        tx = cx + (0.12 + icon_size + 0.12 if has_icon else 0.16)
        tw = max(0.3, cx + cw - 0.12 - tx)
        term = str(it.get("term") or "")
        runs = markup.inline_runs(term, 14.5, DEEP)
        for r in runs:
            r["bold"] = True
        defin = str(it.get("def") or "")
        runs.append({"text": "", "size": 12.5, "newpara": True,
                     "space_before": 3})
        runs.extend(markup.inline_runs(defin, 12.5, DEEP))
        rh = metrics.runs_h(runs, tw, 1.16)
        metrics.fit_runs(runs, tw, row_h - 0.24, ls=1.16,
                         tag=f"{sl.sid}/термин{i + 1}", proj_base=12.5)
        floor.check_runs(runs, f"{sl.sid}/термин{i + 1}")
        rh = min(row_h - 0.24, metrics.runs_h(runs, tw, 1.16))
        prims.text_runs(s, tx, cy + 0.12, tw, rh, runs, ls=1.16,
                        tag=f"{sl.sid}/термин{i + 1}")
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


def stage_overview(p, sl, root):
    """`stage_overview` — s08a/s16a/s21a/s27a (раздел 4 спеки
    `07-design-review-spec.md`, шаблон П4: обзор стадии ДО первого кейса
    раздела, канон `stroenie-i-povestvovanie.md` §3 пункт (в) — перечень
    способов получения данных стоит «на кадре», не только в заметках
    дивайдера). Заголовок · строка-определение · лестница режимов
    (`scheme: kind: lestnitsa`, когда объявлена) · иконко-карточки
    (`ikonki:`) · золотая полоса решения стадии (`itog:`). Собственная
    раскладка, а не `content()`: порядок «определение → лестница →
    карточки → решение» задаёт эта функция, а не фиксированный порядок
    форм `content()` (там тело прозы рисуется ПОСЛЕ количественных форм
    всегда — здесь строка-определение нужна ДО них)."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    check_prims(sl, "stage_overview", allow=("scheme", "ikonki", "itog"))
    y = heading(s, sl)
    bb = body_bot(sl)
    caps = [t for k, t in slidefile.body_blocks(sl) if k == "cap"]
    if caps:
        ch = metrics.est_h(caps[0], 16.0, FULL_W, 1.22, italic=True)
        prims.text_box(s, MX, y, FULL_W, ch, caps[0], size=16.0, italic=True,
                       color=LIGHT, ls=1.22, tag=f"{sl.sid}/определение")
        y += ch + GAP
    sch = scheme.scheme_of(sl, SCHEME)
    if sch:
        scheme.check_scheme(sl.sid, sch, FULL_W, SCHEME)
        y += scheme.draw_scheme(s, sl.sid, sch, MX, y, FULL_W, SCHEME) + GAP
    it = itog.itog_of(sl, st=ITOG)
    it_h = itog.itog_h(it, FULL_W, ITOG) if it else 0.0
    ik = ikonki.ikonki_of(sl)
    if ik:
        ik_h = ikonki.ikonki_h(ik, FULL_W)
        avail = bb - y - (it_h + GAP if it else 0)
        if ik_h > avail + 0.02:
            report.warn(
                f"[иконки] {sl.sid}: карточки просят {ik_h:.2f}\" при "
                f"{avail:.2f}\" свободных — наезд "
                f"{ik_h - avail:.2f}\"")
        # Кадр без `scheme` (s08a/s27a — чистая сетка карточек, без
        # лестницы) иначе оставляет пустой низ >30% между карточками и
        # золотой полосой (находка этой сборки, Пре-гейт п.3 — тот же
        # класс дефекта, который спека ставит в вину исходной деке).
        # Карточки центрируются в остатке высоты, а не прижимаются к верху.
        extra = avail - ik_h
        if extra > 0.5:
            y += extra / 2
        ikonki.draw_ikonki(s, IKON_DIR, ik, MX, y, FULL_W, tag=sl.sid)
        y += ik_h + GAP
    else:
        report.warn(f"[иконки] {sl.sid}: обзорный кадр стадии без `ikonki` "
                    "— карточки способов не нарисованы")
    if it:
        itog.check_itog(sl.sid, it, FULL_W, ITOG)
        iy = max(y, bb - it_h)
        itog.draw_itog(s, sl.sid, it, MX, iy, FULL_W, ITOG,
                       tag=f"{sl.sid}/итог")
        report.GOLD_SEEN.add(sl.sid)
    else:
        report.warn(f"[итог] {sl.sid}: обзорный кадр стадии без "
                    "`itog` — решение стадии не названо")
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


def content(p, sl, root):
    """Содержательный кадр: заголовок · плашки/число · схема · архитектура
    · столбцы · таблица · тело · подвал.

    ПЛАШКИ/СХЕМА/АРХИТЕКТУРА/СТОЛБЦЫ/ТАБЛИЦА рисуются ДО боковой/hero
    иллюстрации и НА ПОЛНУЮ ширину кадра — тот же приём, что
    `build_lec09.content` (находка той сессии: разборы с длинными value/
    note не укладываются в суженную боковым снимком колонку)."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    kind = str(sl.meta.get("type") or "norm")
    if kind in ("case_study", "case"):
        # Силуэт-метка роли разбора случая — минимальный маркер (тот же
        # приём, что у `divider()`/`build_lec09.content`): полоса TEAL,
        # нулевая по высоте и не отнимающая ширины у тела.
        prims.rect(s, 0, 0, 0.17, SLIDE_H, TEAL, count="полоса")
    is_content = kind in CONTENT_TYPES
    bb = body_bot(sl)
    # `itog:` на обычном содержательном кадре (не только `stage_overview`/
    # `udar`, которые уже умели его рисовать) — золотая полоса-вывод
    # прижата к НИЗУ тела, резервируется ПЕРВОЙ, до hero/боковой колонки,
    # тем же ходом, что `stage_overview()` резервирует свою.
    it = itog.itog_of(sl, st=ITOG) if is_content else None
    it_h = itog.itog_h(it, FULL_W, ITOG) if it else 0.0
    # `photos:` — полоса 2-3 фото в ряд с подписями (П6, раздел 5 спеки
    # 07-design-review-spec.md: s36/s37) — `media.photo_strip`. Резервируется
    # тем же ходом, что `itog`, стоит НАД ним: итог ближе к подвалу, полоса
    # фото выше (ни один кадр деки пока не несёт оба сразу, но порядок на
    # этот случай назван явно, а не угадан по месту).
    photos_raw = sl.meta.get("photos") if is_content else None
    photos = None
    if isinstance(photos_raw, list) and photos_raw:
        photos = [{"media": resolve_media({"media": p.get("media")}, sl.sid),
                  "caption": p.get("caption", "")} for p in photos_raw]
    PHOTO_STRIP_H = PHOTO_STRIP_H_OVERRIDE.get(sl.sid, 1.85)
    itog_y = bb - it_h
    photo_strip_y = itog_y - (PHOTO_STRIP_H if photos else 0.0) - (GAP if photos and it else 0.0)
    bb = photo_strip_y - (GAP if photos or it else 0.0)
    img = resolve_media(sl.meta, sl.sid)
    hero = img is not None and bool(sl.meta.get("media_hero"))
    col_bot, body_w_top = bb, FULL_W
    if hero:
        # `s22` (после перестановки раздела 3, issue #353 — бывш. `s23`) —
        # единственный `media_hero_target: 0.62` кадр деки, на котором
        # тело (3 абзаца «деньги не раскрыты» / «оператор и защита» /
        # «слепое пятно», ~170 знаков каждый) не укладывается в оставшуюся
        # колонку 2,89" даже на полу 15 пт (замерено: нужно ~2,5"+ строк
        # при реальной ширине, бюджет меньше). У `s09`/`s28` тот же
        # `media_hero_target: 0.62`, но тело короче — им хватает.
        # Понижение до 0,40 (умолчание формы) даёт телу 3,99" колонки —
        # раскладочное решение этой деки, не правка контента: фото
        # остаётся заметно крупнее порога §5.9 (40%), просто не на
        # авторский максимум.
        raw_target = 0.40 if sl.sid == "s22" else sl.meta.get("media_hero_target")
        kw = {"target": float(raw_target)} if raw_target else {}
        x_box, col_bot, _y_top = place_hero_centered(s, sl, img, bb, **kw)
        body_w_top = x_box - COL_GAP - MX
        y = heading(s, sl, width=body_w_top)
    else:
        y = heading(s, sl)

    if not is_content:
        check_prims(sl, kind)

    if is_content and sl.sid in COMPACT_PLATES:
        pl_c = plates.plates_of(sl, PLATES_COMPACT)
        if pl_c:
            # `s33`: колонка рядом с hero-фото широкого кадра (аспект
            # ≈1,52 — чтобы набрать обязательные §5.9 40% площади, фото
            # ушло в ширину и оставило узкую колонку ≈4,3"): 2 плашки в
            # ряд на такой ширине рвут слова даже компактным пресетом.
            # Один столбец шириной во всю узкую колонку чинит это —
            # мера, а не вкус (`best_plate_style` этот случай не видит:
            # он выбирает по высоте, не по ширине слова).
            pst_c = (replace(PLATES_COMPACT, max_per_row=1)
                    if sl.sid in PLATES_FORCE_SINGLE_COL else
                    best_plate_style(pl_c, body_w_top, base=PLATES_COMPACT))
            y += plates.draw_plates(s, sl.sid, pl_c, MX, y, body_w_top,
                                    pst_c) + GAP
        pl = []
    else:
        pl = plates.plates_of(sl, PLATES) if is_content else []
    if pl and (sl.sid in BULLET_COLLAGE or sl.sid in BULLET_SINGLE_KEY):
        runs = plates_as_list(sl, pl, body_w_top - 0.08)
        h = metrics.runs_h(runs, body_w_top - 0.08, 1.22)
        prims.text_runs(s, MX + 0.04, y, body_w_top - 0.08, h, runs,
                        ls=1.22, tag=f"{sl.sid}/плашки-списком")
        y += h + GAP
        pl = []           # уже нарисовано — дальше по кадру это не плашки
    elif pl:
        pst = best_plate_style(pl, body_w_top)
        y += plates.draw_plates(s, sl.sid, pl, MX, y, body_w_top, pst) + GAP

    fig = figure.figure_of(sl, FIG_HOOK) if is_content else None
    if fig:
        figure.check_figure(sl.sid, fig, body_w_top, FIG_HOOK)
        y += figure.draw_figure(s, sl.sid, fig, MX, y, body_w_top,
                                FIG_HOOK) + GAP

    sch = scheme.scheme_of(sl, SCHEME) if is_content else None
    if sch:
        scheme.check_scheme(sl.sid, sch, body_w_top, SCHEME)
        y += scheme.draw_scheme(s, sl.sid, sch, MX, y, body_w_top, SCHEME) + GAP

    arh_style = {"s11": ARH_S11, "s24": ARH_S24}.get(sl.sid, ARH)
    arh = arhitektura.arhitektura_of(sl, arh_style) if is_content else None
    if arh:
        arhitektura.check_arhitektura(sl.sid, arh, body_w_top, arh_style)
        y += arhitektura.draw_arhitektura(s, sl.sid, arh, MX, y,
                                          body_w_top, arh_style) + GAP

    # ── количественные формы раздела 9 апгрейда ядра (issue #355):
    # таймлайн · полосы · эпохи · пиктограммы · выводы — та же позиция в
    # конвейере кадра, что у `build_lec08_v5.content()` (сразу после
    # архитектуры, до столбцов/таблицы): это формы РАЗБОРА, гасятся
    # `is_content` тем же ходом, что `pl`/`fig` выше.
    tml = timeline.timeline_of(sl) if is_content else None
    if tml:
        timeline.check_timeline(sl.sid, tml, body_w_top, TIMELINE)
        y += timeline.draw_timeline(s, sl.sid, tml, MX, y, body_w_top,
                                    TIMELINE) + GAP

    pol = polosy.polosy_of(sl, POLOSY) if is_content else None
    if pol:
        polosy.check_polosy(sl.sid, pol, body_w_top, POLOSY)
        y += polosy.draw_polosy(s, sl.sid, pol, MX, y, body_w_top,
                                POLOSY) + GAP

    eph = epohi.epohi_of(sl, EPOHI) if is_content else None
    if eph:
        epohi.check_epohi(sl.sid, eph, body_w_top, EPOHI)
        y += epohi.draw_epohi(s, sl.sid, eph, MX, y, body_w_top, EPOHI) + GAP

    pik = piktogrammy.pikto_of(sl, st=PIKTO) if is_content else None
    if pik:
        piktogrammy.check_pikto(sl.sid, pik, body_w_top, PIKTO)
        y += piktogrammy.draw_pikto(s, sl.sid, pik, MX, y, body_w_top,
                                    PIKTO) + GAP

    vyv = vyvody.vyvody_of(sl, VYVODY) if is_content else None
    if vyv:
        vyvody.check_vyvody(sl.sid, vyv, body_w_top, VYVODY)
        y += vyvody.draw_vyvody(s, sl.sid, vyv, MX, y, body_w_top,
                                VYVODY) + GAP

    # `ikonki:` на обычном содержательном кадре (не только на обзорных
    # кадрах стадий — `stage_overview()` зовёт ту же пару сам): П7/stage_row
    # карточки раздела 5 спеки, например s20/s39/s40/s42.
    ik = ikonki.ikonki_of(sl) if is_content else None
    if ik:
        ik_h = ikonki.ikonki_h(ik, body_w_top)
        avail_ik = col_bot - y
        if ik_h > avail_ik + 0.02:
            report.warn(f"[иконки] {sl.sid}: карточки просят {ik_h:.2f}\" "
                        f"при {avail_ik:.2f}\" свободных")
        ikonki.draw_ikonki(s, IKON_DIR, ik, MX, y, body_w_top, tag=sl.sid)
        y += ik_h + GAP

    cols = columns.columns_of(sl) if is_content else None
    tbl = table_from(sl) if is_content else None

    # Кадр-ТОЛЬКО-таблица (`s03` карта лекции, `s07` контуры завода): ни
    # плашек, ни схемы, ни столбцов, но есть короткое тело-вступление
    # (`s03`: 5 строк-разделов; `s07`: 2-3 абзаца) — первая сборка топила
    # его в отрицательный остаток, потому что бюджет под таблицу считался
    # ПЕРЕД телом, не наоборот. Та же находка и то же решение, что
    # `build_lec09.content` (пункт «body_drawn»): вступление читается ДО
    # большой таблицы, бюджет под него — по ОСТАТКУ после минимальной
    # высоты таблицы на полу кегля, а не фиксом.
    body_drawn = False
    pure_table = bool(tbl) and not pl and not sch and not arh and not cols
    if pure_table and slidefile.body_blocks(sl):
        runs = body_runs(sl, {"head": 18.0, "cap": 15.0, "bullet": 15.0})
        if runs:
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
        cap = 2.20 if tbl else columns.MAX_H
        ch = max(columns.MIN_H, min(col_bot - y, cap))
        columns.draw_columns(s, sl.sid, cols, MX, y, body_w_top, ch, pary=True)
        y += ch + GAP
    if tbl:
        tag = f"{sl.sid}/таблица"
        true_avail = col_bot - y
        has_tail = bool(slidefile.body_blocks(sl))
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

    body_w, media_bot, draw_img = body_w_top, 0.0, None
    img2 = None
    if not hero and img and sl.meta.get("media_2"):
        img2 = resolve_media({"media": sl.meta.get("media_2")}, sl.sid)
    if not hero and img and img2:
        # Второе фото рядом с первым в той же боковой колонке — раздел 5
        # спеки (`s13`): «Событие» + «дверь в лаборатории NTSB» одной
        # парой, стопкой друг над другом (та же ширина колонки, что у
        # одиночного фото, высота колонки делится пополам).
        mw = sl.media_w or MEDIA_W
        half_h = min(MEDIA_H_CAP, col_bot - y) / 2 - COL_GAP / 2
        mw1, mh1 = media.media_box_size(media.img_ar(img, sl.sid), mw, half_h)
        mw2, mh2 = media.media_box_size(media.img_ar(img2, sl.sid), mw, half_h)
        mw_col = max(mw1, mw2)
        body_w = body_w_top - mw_col - COL_GAP
        draw_img = (MX + body_w + COL_GAP, y, mw1, mh1)
        draw_img2 = (MX + body_w + COL_GAP, y + mh1 + COL_GAP, mw2, mh2)
        media_bot = y + mh1 + COL_GAP + mh2
    elif not hero and img:
        # `s31` (раздел 5 спеки): фото было тёмным и мелким на умолчательном
        # потолке `MEDIA_H_CAP` 3,40" — слот поднят до ~5,2" точечно для
        # этого кадра, остальные некадрированные фото деки не трогает.
        h_cap = MEDIA_H_CAP_OVERRIDE.get(sl.sid, MEDIA_H_CAP)
        mw, mh = media.media_box_size(
            media.img_ar(img, sl.sid), sl.media_w or MEDIA_W,
            min(h_cap, col_bot - y))
        body_w = body_w_top - mw - COL_GAP
        draw_img = (MX + body_w + COL_GAP, y, mw, mh)
        media_bot = y + mh
        draw_img2 = None
    else:
        draw_img2 = None

    avail = col_bot - y
    blocks_present = bool(slidefile.body_blocks(sl)) and not body_drawn
    # `s24`: архитектура (4 блока с длинными строками разбора, читаемость
    # важнее нуля предупреждений — см. docstring `ARH_S24`) забирает
    # больше высоты, чем кадру физически досталось, и `avail` уходит в
    # минус. Молчаливый пропуск тела здесь был бы ХУЖЕ видимого наезда:
    # «что переехало»/«что не переехало» — обязательное содержание формы
    # §5.13, а не факультативный абзац. Рисуем на МИНИМАЛЬНО разумном
    # бюджете (0,90"), даже когда геометрия его не оставила, — предупреждение
    # `[высота]` при этом остаётся (решение владельца, не сборки), но текст
    # не исчезает с кадра молча.
    draw_budget = avail if avail > 0.35 else (0.90 if blocks_present else avail)
    if draw_budget > 0.35 and blocks_present:
        avail = draw_budget
        if sl.sid == "s05":
            # `keystone` — первый абзац («Четвёртая опора…») рисуется в
            # отдельной серой рамке (см. docstring `keystone_gap_box`);
            # «Вопрос лекции» — раздел 5 спеки 07-design-review-spec.md
            # (П9): собственная золотая tint-полоса (`prims.tint_box`),
            # визуально отделяющая ось лекции от любой другой рамки деки
            # — не Ocean rounded box, как раньше. «Сквозная линия» —
            # обычным телом в коробке мотива ниже, как и было.
            blocks = slidefile.body_blocks(sl)
            gap_text = blocks[0][1] if blocks else ""
            question = blocks[1][1] if len(blocks) > 1 else ""
            rest = blocks[2:]
            gh = keystone_gap_box(s, sl.sid, gap_text, MX, y, body_w)
            y += gh + GAP
            if question:
                q_runs = markup.inline_runs(question, 17.0, DEEP)
                for r in q_runs:
                    r["bold"] = True
                qh = metrics.runs_h(q_runs, body_w - 0.28, 1.22) + 0.20
                prims.tint_box(s, MX, y, body_w, qh, tone="gold")
                prims.text_runs(s, MX + 0.14, y + 0.10, body_w - 0.28,
                                qh - 0.20, q_runs, ls=1.22,
                                tag=f"{sl.sid}/вопрос")
                report.GOLD_SEEN.add(sl.sid)
                y += qh + GAP
            runs = []
            first = True
            for kind2, t in rest:
                sz = {"head": 20.0, "cap": 15.0, "bullet": 15.0}.get(kind2, 16.0)
                if not first:
                    runs.append({"text": "", "size": sz, "newpara": True,
                                 "space_before": 7})
                first = False
                for r in markup.inline_runs(t, sz, DEEP):
                    runs.append(r)
            if runs:
                metrics.fit_runs(runs, body_w - 0.08, col_bot - y, ls=1.26,
                                 tag=f"{sl.sid}/тело", proj_base=BODY_PT)
                floor.check_runs(runs, f"{sl.sid}/тело")
                h_text = min(col_bot - y, metrics.runs_h(runs, body_w - 0.08, 1.26))
                prims.ocean_box(s, MX - 0.14, y - 0.10, body_w + 0.28,
                                h_text + 0.20)
                prims.text_runs(s, MX + 0.04, y, body_w - 0.08, h_text,
                                runs, ls=1.26, tag=f"{sl.sid}/тело")
        else:
            runs = body_runs(sl, {"head": 20.0, "cap": 15.0, "bullet": 15.0})
            wrapped, y_bot = None, media_bot + WRAP_GAP
            if runs and not hero and img and y < media_bot:
                wrapped = wrap.fit_runs_wrap(
                    runs, body_w - 0.08, media_bot - y, FULL_W - 0.08,
                    col_bot - y_bot, body_w - 0.08, avail, ls=1.26,
                    tag=f"{sl.sid}/тело", proj_base=BODY_PT)
            pushed = None
            if runs and not wrapped and not hero and img and y < media_bot:
                pushed = wrap.fit_pushed(
                    runs, FULL_W - 0.08, col_bot - y_bot, body_w - 0.08,
                    avail, ls=1.26, tag=f"{sl.sid}/тело", proj_base=BODY_PT)
            if runs and (wrapped or pushed):
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
            elif runs:
                metrics.fit_runs(runs, body_w - 0.08, avail, ls=1.26,
                                 tag=f"{sl.sid}/тело", proj_base=BODY_PT)
                floor.check_runs(runs, f"{sl.sid}/тело")
                h_text = min(avail, metrics.runs_h(runs, body_w - 0.08, 1.26))
                prims.ocean_box(s, MX - 0.14, y - 0.10, body_w + 0.28,
                                h_text + 0.20)
                prims.text_runs(s, MX + 0.04, y, body_w - 0.08, h_text,
                                runs, ls=1.26, tag=f"{sl.sid}/тело")
    elif blocks_present:
        report.warn(f"[высота] {sl.sid}/тело: места под тело не осталось "
                    f"({avail:.2f}\") — примитивы съели кадр")
    if draw_img:
        media.draw_media(s, sl.sid, img, *draw_img)
    if draw_img2:
        media.draw_media(s, sl.sid, img2, *draw_img2)
    if photos:
        media.photo_strip(s, sl.sid, photos, MX, photo_strip_y, FULL_W,
                          PHOTO_STRIP_H, tag=f"{sl.sid}/фото-полоса")
    if it:
        itog.check_itog(sl.sid, it, FULL_W, ITOG)
        itog.draw_itog(s, sl.sid, it, MX, itog_y, FULL_W, ITOG,
                       tag=f"{sl.sid}/итог")
        report.GOLD_SEEN.add(sl.sid)
    gold_tick(s, sl.sid, MX, sl.tick_y or (TITLE_Y + 0.98))
    footer(s, sl)
    return s


BUILDERS = {"cover": cover, "divider": divider, "qa": qa, "udar": udar,
           "stage_overview": stage_overview, "map_cards": lecture_map,
           "term_cards": term_cards}


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
                    "ОТДЕЛЬНЫЙ файл lec-11-partial.pptx")
    ap.add_argument("--selftest", action="store_true",
                    help="прогнать самопроверку ядра (deckkit.selftest + "
                    "deckkit.contrast --selftest) и выйти")
    args = ap.parse_args()

    if args.selftest:
        import subprocess
        rc1 = subprocess.call([sys.executable, "-m", "deckkit.selftest"],
                              cwd=str(REPO_ROOT / "tools" / "presentation-build"))
        rc2 = subprocess.call(
            [sys.executable, "-m", "deckkit.contrast", "--selftest"],
            cwd=str(REPO_ROOT / "tools" / "presentation-build"))
        return rc1 or rc2

    out = (HERE / "lec-11-partial.pptx") if args.only else OUT

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
