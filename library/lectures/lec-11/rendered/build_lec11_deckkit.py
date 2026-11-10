#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Дека Лекции 11 («AI в дискретном и процессном производстве», issue #338)
на общем ядре `deckkit` (issue #229) — Фаза 2 переделки
(`library/lectures/lec-11/rework/architecture.md` §3, объединённые бывшие
Фазы 2+5).

ЭТО НЕ ФИНАЛЬНЫЙ СБОРЩИК ЛЕКЦИИ. Выход лежит в `lec-11-deckkit.pptx`, а не
в `lec-11.pptx` — старые `build_lec11.py`/`build_lec11_part2.py` и их
доставленный `lec-11.pptx` этим файлом НЕ трогаются и не удаляются
(архитектура §3, Фаза 2: «не удалять старые build-скрипты, пока новый не
подтверждён»). Переименование/продвижение — решение оркестратора после
приёмки этого прохода.

ОХВАТ (архитектура §3, Фаза 2 ИСКЛЮЧАЕТ 7 «особых» слайдов, их здесь 12 —
см. разбор ниже): собираются ВСЕ 41 слайд одним файлом, но только **29**
получают целевую раскладку каталога форм (`tools/metodika-podachi/kadr/
02-KATALOG-FORM.md`). Оставшиеся **12** идут PASSTHROUGH — существующий
текст `.md` как есть, через ту же раскладку `content()`/`divider()`, без
`blocks:`/`columns:`/`scheme:`/`figure:` override, и отмечены ниже
комментарием `# TEMP passthrough`:

* 5 дивайдеров (`s06`/`s13`/`s23`/`s31`/`s36`) — блокирующий баг
  переполнения (`[высота] .../дивайдер: текст дошёл до подвала`) общий для
  всех пяти, фикс — отдельным проходом Фазы 3 (вне охвата этой сессии);
* `s05` (keystone) — редизайн формы (два столбца → два ряда) — Фаза 3;
* `s10`/`s15`/`s17`/`s24`/`s34`/`s37` — контент зависит от решений Фазы 3
  (тройка полных разборов + Boeing-жанр + сквозная линия), раскладка им
  назначается ТАМ ЖЕ, одним проходом с правкой контента.

ТРИ АДАПТЕРА СПАЙКА (Фаза 1, `rework/spike-deckkit/build_section1_spike.py`)
— перенесены БЕЗ ИЗМЕНЕНИЯ ЛОГИКИ на все 41 слайд:

1. Заголовок — первая `# …`-строка тела, поля `title` у фронтматтера этой
   лекции нет вовсе (`extract_title_if_missing`).
2. `media:` в `.md` нет ни на одном файле — уже существующие PNG/JPG
   старого сборщика подключаются словарём `sid → путь`
   (`MEDIA_OVERRIDE`/`apply_media_override`).
3. Файлы кадра НЕ обёрнуты в `## Видимый текст слайда`/`## Заметки
   лектора`, которые по умолчанию ждёт `slidefile.py` — раздел заметок
   называется по-английски `## Speaker notes`, видимый текст — всё тело ДО
   этой границы. Без правки `_SEC_VIS`/`_SEC_NOTES` кадры собрались бы с
   ПУСТЫМ видимым текстом молча (see spike docstring).

ФОРМА — ЧЕТВЁРТЫЙ СЛОЙ, КОТОРОГО НЕ БЫЛО В СПАЙКЕ. Спайк показал (§1a
архитектуры): механическая миграция — дешёвая, но без `blocks:`/`columns:`/
`scheme:`/`figure:` 33 уникальные формы `visual.pattern` схлопываются в
сплошной текст. `FORM_OVERRIDE`/`TABLE_BODY` ниже — это и есть восстановление
формы: поля фронтматтера, которых в `.md` нет, подставляются РАНТАЙМОМ в
`sl.meta`/`sl.body` (объект `Slide` в памяти одной сборки), файлы `slides/
*.md` не правятся НИ ОДНОЙ СТРОКОЙ. Числа и факты в каждой форме — те же,
что в исходном тексте слайда; это восстановление РАСКЛАДКИ, не содержания.

ДВЕ ТОЧЕЧНЫЕ ПРАВКИ СОДЕРЖАНИЯ — РОВНО ТЕ, ЧТО В БРИФЕ ЭТОЙ ЗАДАЧИ (не
переносятся рантайм-адаптером, а правят сам файл `.md`, см. git diff):

* `slides/s02-cover.md`: из `## Meta` убрано «75 минут + Q&A» — ENFORCED
  «No Timing in Slides» (CLAUDE.md), видимое тело обложки.
* `slides/s08-market-estimates-divergence.md`: заголовок `## Pedagogical
  point` переименован в `## Урок для инженера` — ENFORCED анти-англицизм +
  «No Methodology in Slides»; содержание строки не тронуто.

`slides/s03-lecture-map.md` проверен: минуты («12 минут» / «17 минут» / «6
минут», найденные архитектурой §2 блок N2) стоят в `## Speaker notes`, а не
в видимом теле — бриф просил убрать минуты «из видимого тела», и в видимом
теле их не было. Не правлен; находка названа в итоговом отчёте, не
исполнена молча мимо брифа.

РЕШЕНИЕ DELOITTE vs S&P GLOBAL (`s07`, архитектура §1a/§5 п.2). `deck.yaml`
заявляет «.md = источник правды»; `slides/s07-adoption-landscape.md` называет
третий источник оценки «Deloitte 2025: 42%…». Старый `build_lec11.py`
(литерал в Python, в обход `.md`) показывал «S&P Global Market
Intelligence» — это и есть расхождение, найденное спайком. Эта сборка читает
ТОЛЬКО `.md` (как и весь deckkit), то есть студент увидит «Deloitte» —
ЗАДУМАННОЕ поведение миграции на единственный источник правды, не решение
этой сессии по существу факта. Явно в отчёте сессии: это видимое изменение
против прежнего рендера.

Запуск:
  python3 build_lec11_deckkit.py              — только PPTX (все 41 кадра)
  python3 build_lec11_deckkit.py --render      — ещё PDF+PNG (soffice, таймаут)
  python3 build_lec11_deckkit.py --only s07,s09 — ТОЛЬКО эти кадры, отдельный
                                                   файл *-partial.pptx
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent              # .../lec-11/rendered
LEC_ROOT = HERE.parent                                # .../lec-11
REPO_ROOT = HERE.parents[3]                           # корень репозитория
sys.path.insert(0, str(REPO_ROOT / "tools" / "presentation-build"))

from deckkit import (axis, columns, figure, floor, markup, metrics,  # noqa: E402
                     plates, prims, refdeck, render as rnd, report,
                     scheme, slidefile, tracks)

SLIDES_DIR = LEC_ROOT / "slides"
OUT = HERE / "lec-11-deckkit.pptx"
PARTIAL = HERE / "lec-11-deckkit-partial.pptx"
SNAPS = HERE / "snapshots-deckkit"

# 12 слайдов, исключённых из восстановления формы этой фазой (см. docstring).
PASSTHROUGH_SIDS = {
    "s05", "s06", "s13", "s23", "s31", "s36",   # keystone + 5 дивайдеров
    "s10", "s15", "s17", "s24", "s34", "s37",   # content зависит от Фазы 3
}

# ─── адаптер №0 (спайк): формат файла кадра этой лекции — другой ───────
slidefile._SEC_VIS = r"\A(.*?)(?=\n##[ \t]*Speaker notes[ \t]*\r?\n|\Z)"
slidefile._SEC_NOTES = r"##[ \t]*Speaker notes[ \t]*\r?\n(.*?)(?=\n##\s|\Z)"

# ─── пол кегля видимого слоя: 15 пт, решение владельца 29.10.2026 ──────
# `floor.VIS_PT` (читается ДИНАМИЧЕСКИ `floor.pt()` при каждом вызове —
# поднятие здесь сразу работает на СТОРОЖ.
floor.VIS_PT = 15.0

# НО сторож — не то же самое, что ФАКТИЧЕСКИ выбранный кегль. `label_pt` /
# `note_pt` (плашки) и `lab_pt` / `cap_pt` (схема-ряды/ось/дорожки) — это
# ЛИТЕРАЛЬНЫЕ размеры, не через поиск; `step_lo`/`value_lo` — НИЖНЯЯ ГРАНИЦА
# поиска подбираемого кегля. Оба класса полей читаются как default-параметр
# `st=DEFAULT`, а default-параметр Python связывается с САМИМ ОБЪЕКТОМ при
# определении функции (один раз, при импорте модуля) — переприсвоение имени
# `plates.DEFAULT`/`axis.DEFAULT` в этом файле НЕ подействовало бы на уже
# определённые `draw_plates`/`draw_axis`/…, они продолжали бы смотреть на
# СТАРЫЙ объект. Поэтому поля поднимаются МУТАЦИЕЙ того же замороженного
# (`frozen=True`) синглтона через `object.__setattr__` — объект тот же,
# значит и `st=DEFAULT` внутри уже определённых функций видит новые поля.
#
# Для форм `kind: shkala`/`kind: dorozhki` (`axis.py`/`tracks.py`) это
# ЕДИНСТВЕННЫЙ рычаг извне: их публичные `parse/height/check/draw`
# (вызываемые диспетчером `scheme.KINDS`) НЕ принимают свой `st` параметром
# вовсе — пробросить декин стиль через аргумент вызова, как делает
# `build_lec09.py` для `plates.DEFAULT`-замен, здесь физически нельзя.
def _raise_floor(obj, **kw):
    for k, v in kw.items():
        object.__setattr__(obj, k, v)


_raise_floor(plates.DEFAULT, label_pt=15.0, note_pt=15.0, value_lo=15.0,
            value_floor=15.0,
            # Золотое значение `#F0AB00` на белой/поверхностной плашке —
            # 1,99:1 при пороге WCAG AA 3,0 (`plates.py` docstring,
            # прожарка 2026-10-14). Тот же фикс, что `build_lec09.py`/
            # `build_lec08_v5.py`: ключевой цвет — `LIGHT` (`#1C7293`,
            # 5,42:1), золото остаётся обводкой плашки и акцентной чертой.
            value_key_color=plates.LIGHT)
_raise_floor(scheme.DEFAULT, lab_pt=15.0, step_hi=17.0, step_lo=15.0,
            cap_pt=15.0)
_raise_floor(axis.DEFAULT, lab_pt=15.0, unit_pt=15.0, cap_pt=15.0,
            end_pt=15.0)
_raise_floor(tracks.DEFAULT, lab_pt=15.0, step_hi=17.0, step_lo=15.0,
            cap_pt=15.0, lab_w=1.90)
_raise_floor(figure.DEFAULT, base_pt=15.0, note_pt=15.0)
# `columns.py` держит свои числа ПРОСТЫМИ модульными именами (не
# dataclass-полями) — `HEAD_PT`/`ITEM_HI`/`ITEM_LO`/`ITEM_FLOOR` читаются
# внутри `draw_columns` как свободные переменные, то есть ищутся в
# пространстве имён модуля В МОМЕНТ ВЫЗОВА, а не связываются заранее —
# здесь достаточно простого переприсваивания имени.
columns.HEAD_PT = 15.0
columns.ITEM_HI, columns.ITEM_LO, columns.ITEM_FLOOR = 17.0, 15.0, 15.0

# ─── адаптер №1 (спайк): заголовок — первая H1-строка тела ─────────────
_TITLE_RE = re.compile(r"^#[ \t]+(.+?)[ \t]*\r?\n\s*\n", re.M)


def extract_title_if_missing(sl):
    if sl.title:
        return
    m = _TITLE_RE.match(sl.body)
    if not m:
        report.warn(f"[заголовок-деррив] {sl.sid}: нет поля `title` и тело "
                    "не начинается строкой «# …»")
        return
    sl.title = m.group(1).strip()
    sl.body = sl.body[m.end():]
    sl._cache.clear()


# ─── адаптер №2 (спайк, расширен на все найденные реальные ассеты) ─────
# `media:` нет ни в одном файле этой лекции. Словарь — ВСЕ уже существующие
# PNG/JPG старого сборщика под sid этой лекции (`rendered/assets/{charts,
# screenshots}/`), независимо от того, боевой слайд или passthrough:
# passthrough-слайды получают СВОИ старые фото как есть (та же картинка,
# что рисовал `build_lec11.py`), боевые — туда, где фото усиливает форму
# БЕЗ того, чтобы теснить её (см. отчёт сессии: `s07`/`s08` сознательно
# остались без фото — числовая форма (ось/плашки) уже несёт то, что несла
# бы картинка диаграммы, и боковой снимок сузил бы им тело).
MEDIA_OVERRIDE = {
    "s01": "rendered/assets/screenshots/s01-tesla-giga-press.png",
    "s10": "rendered/assets/screenshots/s10-siemens-hq.jpg",       # TEMP
    "s14": "rendered/assets/screenshots/s14-tsmc.jpg",
    "s15": "rendered/assets/screenshots/s15-alaska-737-max9.jpg",  # TEMP
    "s17": "rendered/assets/screenshots/s17-tata-port-talbot.jpg", # TEMP
    "s24": "rendered/assets/screenshots/s24-basf-ludwigshafen.jpg",# TEMP
    "s25": "rendered/assets/screenshots/s25-yokogawa.jpg",
    "s27": "rendered/assets/screenshots/s27-posco-tower.jpg",
    "s29": "rendered/assets/screenshots/s29-nornickel.jpg",
    "s39": "rendered/assets/screenshots/s39-bmw-welt.jpg",
}
HERO_SIDS = {"s01", "s39"}   # hero §5.9 — уже пройдено (архитектура §2 блок K),
                             # этот проход только ПОДКЛЮЧАЕТ существующий файл


def apply_media_override(sl):
    rel = MEDIA_OVERRIDE.get(sl.sid)
    if not rel:
        return
    if not (LEC_ROOT / rel).exists():
        report.warn(f"[медиа-деррив] {sl.sid}: ожидался файл {rel}, "
                    "которого нет на диске")
        return
    sl.meta["media"] = rel
    if sl.sid in HERO_SIDS:
        sl.meta["media_hero"] = True


# ─── форма каталога — 29 «боевых» слайдов (архитектура §3, Фаза 2) ──────
# Поля ТОЧНО по контракту ядра (`plates.py`/`columns.py`/`scheme.py`/
# `axis.py`/`tracks.py`/`figure.py`): никаких новых имён полей, никакой
# новой логики в деке — только данные, перенесённые из прозы `.md` в
# декларативную форму. Числа и факты — в точности те, что в файле; что где
# стояло абзацем, теперь стоит плашкой/осью/дорожкой/таблицей.
FORM_OVERRIDE = {
    # s03 — маршрут лекции: 5 разделов как состав счёта (плашки).
    "s03": {"blocks": [
        {"label": "Раздел 1 · Общее", "value": "6 слайдов",
         "note": "Adoption landscape · индустриальные модели · OT/IT · "
                 "hype-collapse трио"},
        {"label": "Раздел 2 · Дискретное", "value": "9 слайдов",
         "note": "CV-инспекция · разметка · PdM · коботы · Tesla 2018 · "
                 "границы CV-QC"},
        {"label": "Раздел 3 · Процессное", "value": "7 слайдов",
         "note": "Мягкие сенсоры · MPC/RL · PdM на границе · регуляторика"},
        {"label": "Раздел 4 · Рамка решения", "value": "6 слайдов",
         "note": "4 категории критериев · матрица альтернатив · "
                 "5-шаговая рамка"},
        {"label": "Раздел 5 · Замыкание", "value": "3 слайда",
         "note": "Recap + Q&A + bridge к Лекции 12", "key": True},
    ]},
    # s07 — headline 78%/5,5% как ось (сравнение одной базы) + три
    # альтернативных источника как плашки.
    "s07": {
        "scheme": {"kind": "shkala", "unit": "% компаний (McKinsey 2025)",
                   "base": "McKinsey State of AI 2025",
                   "marks": [
                       {"value": "78", "label": "Используют AI"},
                       {"value": "5,5", "label": "High performers, EBIT>5%",
                        "key": True},
                   ]},
        "blocks": [
            {"label": "MIT Sloan 2025", "value": "95%",
             "note": "пилотов не доходят до production · 14 мес · "
                     "+380% бюджета"},
            {"label": "RAND 2025", "value": "80,3%",
             "note": "проектов без business value · 547 из 684 млрд $"},
            {"label": "Deloitte 2025", "value": "42%",
             "note": "компаний закрыли ≥1 AI-инициативу · $7,2М sunk cost "
                     "per abandoned", "key": True},
        ],
    },
    # s08 — три рыночные оценки 2025 на одной оси ($, один сегмент).
    "s08": {"scheme": {"kind": "shkala",
                       "unit": "$ млрд, рынок «AI in manufacturing» 2025",
                       "base": "один и тот же сегмент, три методологии",
                       "marks": [
                           {"value": "7,6", "label": "Fortune Business "
                            "Insights"},
                           {"value": "8,57", "label": "Precedence "
                            "Research"},
                           {"value": "34,18", "label": "Markets and "
                            "Markets", "key": True},
                       ]}},
    # s09 — OT vs IT, классическое противопоставление.
    "s09": {"type": "comparison", "columns": {
        "left": {"head": "OT — Operational Technology", "items": [
            "PLC · SCADA · DCS · конвейеры · реакторы",
            "Цикл 1–10 мс, детерминированный",
            "Strong consistency — гарантированный budget",
            "Audit trail обязателен (FDA Part 11, GAMP, ATEX)",
            "SIL 2/3 — изменение требует валидации",
        ]},
        "right": {"head": "IT — Information Technology", "items": [
            "Облако · дата-центры · ML pipelines",
            "Цикл мс–секунды, eventually-consistent",
            "«Возможно, переспросим через секунду»",
            "Audit trail для security/compliance, не для control",
            "SaaS-обновления каждую неделю",
        ]},
    }},
    # s11 — Tesla Optimus: демо обещания vs production-реальность.
    "s11": {"type": "comparison", "columns": {
        "left": {"head": "Демо (2022–2024)", "items": [
            "Складывает футболки · переносит коробки · ходит по фабрике",
            "AI Day 2022/2024 · Cybercab event октябрь 2024",
            "Обещано: 10–20 тыс. Optimus к 2025, ~$30 тыс/юнит",
        ]},
        "right": {"head": "Production (2026)", "items": [
            "Не задействован в production-сборке ни на одном заводе",
            "Cybercab: напитки гостям — Wired подтвердил удалённое "
            "управление",
            "Reality check февраль 2026: deployment не подтверждён",
        ]},
    }},
    # s12 — трио провалов: три НЕЗАВИСИМЫЕ истории, внутри каждой —
    # сequence обещание→реальность→урок (дорожки + стрелки внутри дорожки).
    "s12": {"scheme": {"kind": "dorozhki", "steps_arrows": True, "rows": [
        {"label": "GE Predix (2011–2020)", "steps": [
            "$4+ млрд · «AOS for industrial»",
            "«Be everything to everyone» → развал 2018",
            "Урок: industrial AI ≠ general cloud AI",
        ]},
        {"label": "IBM Watson Health (2018–2022)", "steps": [
            "«–47% downtime» — маркетинг",
            "Drug Discovery закрыт 2019 → продан за ~$1 млрд",
            "Урок: демо ≠ production",
        ]},
        {"label": "Foxconn WI", "steps": [
            "$10 млрд, 8-е чудо",
            "10К → 1,5К → MS DC",
            "Маркетинг > физика",
        ]},
    ]}},
    # s14 — три рабочих кейса CV-инспекции как плашки.
    "s14": {"blocks": [
        {"label": "BMW GenAI4Q (Regensburg)", "value": "2025",
         "note": "Bespoke inspection catalogue · Factory of the Year 2024"},
        {"label": "TSMC wafer defect detection", "value": "95%",
         "note": "accuracy · +10–15% yield на 5/3 нм — сотни млн $",
         "key": True},
        {"label": "Boeing 737 fuselage", "value": "дек. 2025",
         "note": "CV критических зон · photo-driven part validation"},
    ]},
    # s16 — дёшево/дорого, классическое противопоставление.
    "s16": {"type": "comparison", "columns": {
        "left": {"head": "Дёшево", "items": [
            "Сырые данные — камеры: 10 ТБ/смену с конвейера",
            "Сенсоры IoT — гигабайты/день, копейки за ГБ",
            "Видеоархив SCADA — storage стоит, данные доступны",
        ]},
        "right": {"head": "Дорого", "items": [
            "Эталонная разметка — 500–2000 ₽/час эксперта",
            "Рентген шва: 5–15 мин на пример · десятки тыс. нужны",
            "Class imbalance 1% — на 1000 дефектов нужно ~100 000 "
            "примеров",
        ]},
    }},
    # s18 — Toyota GAIA: одно число (рост 8000→10000) + база.
    "s18": {"figure": {
        "value": "10 000",
        "unit": "AI-моделей Toyota GAIA, созданных сотрудниками цеха (2024)",
        "base": "было 8 000 в 2023 — рост ×1,25 за год",
        "note": "10 000 часов ручной работы сэкономлено в год · Jidoka "
                "2.0: augment, не replace",
    }},
    # s19 — Tesla 2018: цель против факта, одна единица (Model 3/неделю).
    "s19": {"scheme": {"kind": "shkala", "unit": "Model 3 / неделю",
                       "base": "Q1 2018, ориентир Wall Street",
                       "marks": [
                           {"value": "2020", "label": "Реально", "key": True},
                           {"value": "2500", "label": "Цель"},
                       ]}},
    # s20 — где CV ломается / альтернативы до ML.
    "s20": {"type": "comparison", "columns": {
        "left": {"head": "Где CV ломается", "items": [
            "Low-contrast defects — микротрещина при обычном свете "
            "невидима",
            "Сдвиг распределения при смене продукта (5+ моделей)",
            "Scarce defect labels — редкие типы, callback к s16",
        ]},
        "right": {"head": "Альтернативы до ML", "items": [
            "Структурированный/поляризованный свет · рентген · "
            "тепловидение",
            "Rules-based vision — 60–70% inspection workloads, дёшево",
            "Hybrid: физика → rules → ML только на остатке 10–20%",
        ]},
    }},
    # s21 — 4 вопроса к вендору как упорядоченный чек-лист.
    "s21": {"scheme": {"arrows": True, "rows": [
        {"label": "Вопросы к вендору", "steps": [
            "1 · Baseline — сколько часов/FTE было?",
            "2 · Окно — день? месяц? лучший run?",
            "3 · Вмешательства — что сделал AI?",
            "4 · OEE-канал — A/P/Q?",
        ]},
    ]}},
    # s25 — CIRL-архитектура: PID-baseline → RL-policy (шаг модели) →
    # эффект; настоящий порядок, стрелки.
    "s25": {"scheme": {"arrows": True, "caption": "Yokogawa-JSR FKDPP: "
                       "35 дней (840 ч) автономного RL · Japan PM Prize "
                       "2023", "rows": [
        {"label": "CIRL", "steps": [
            "PID — baseline, валидирован регулятором",
            {"text": "Deep RL — PID внутри loss function", "ai": True},
            "RL — ценность в нелинейных зонах",
        ]},
    ]}},
    # s26 — 4 независимых механизма дрейфа RL (дорожки, без стрелок между
    # дорожками — механизмы не следуют один из другого).
    "s26": {"scheme": {"kind": "dorozhki", "steps_arrows": True,
                       "caption": "Safe-fallback — MPC: реагирует на "
                       "текущие данные, не помнит обучения", "rows": [
        {"label": "Batch transitions", "steps": [
            "Переходный режим = OOD",
            "Скачки температуры",
        ]},
        {"label": "Смена feedstock", "steps": [
            "Policy stale на сырье",
            "Дрейф незаметен",
        ]},
        {"label": "Seasonal shifts", "steps": [
            "Один сезон в обучении",
            "Деградация без причины",
        ]},
        {"label": "Equipment wear", "steps": [
            "Износ катализатора",
            "Не учится online",
        ]},
    ]}},
    # s27 — детерминизм edge-вывода: одно число + база (PLC vs LLM).
    "s27": {"figure": {
        "value": "1–10 мс",
        "unit": "детерминированный PLC-цикл",
        "base": "против 100–500 мс недетерминированного LLM — разница "
                "50–100×",
        "note": "POSCO: 180 edge-узлов · +5% efficiency / −10% энергии / "
                "+3% yield · Holcim 100 заводов C3 AI",
    }},
    # s28 — три регуляторных блокера, независимые (дорожки), внутри каждой
    # — требование→следствие (стрелка внутри дорожки).
    "s28": {"scheme": {"kind": "dorozhki", "steps_arrows": True, "rows": [
        {"label": "FDA Part 11", "steps": [
            "Audit trail",
            "HITL",
        ]},
        {"label": "ATEX (Zone 0)", "steps": [
            "Hardware запрет",
            "AI — monitoring",
        ]},
        {"label": "Указ № 250 (КИИ)", "steps": [
            "КИИ, ФЗ-152",
            "Отеч. ПО 2027",
        ]},
    ]}},
    # s29 — три российских кейса как плашки.
    "s29": {"blocks": [
        {"label": "Норникель", "value": "industrial stage",
         "note": "flotation/grinding · ноя 2024 — альянс с Газпром нефть"},
        {"label": "СИБУР", "value": "Marketplace 2025→26",
         "note": "моделирование · импортозамещение КИИ к 2027"},
        {"label": "ММК · НЛМК · Северсталь", "value": "без метрик",
         "note": "общие декларации · Severstal: прибыль −55% (2024)",
         "key": True},
    ]},
    # s32 — 4 категории критериев, независимые (дорожки); внутри категории
    # критерии НЕ упорядочены (перечень, без steps_arrows).
    "s32": {"scheme": {"kind": "dorozhki",
                       "caption": "+ бонус-критерий: SIL 2/3 — чёрный "
                       "ящик ML не сертифицируется для контуров с риском "
                       "для жизни", "rows": [
        {"label": "A · Данные", "steps": [
            "MTBF >1 года",
            "Известная физика (CFD/FEA)",
            "Разметка дорогая (<1% дефектов)",
        ]},
        {"label": "B · Стоимость", "steps": [
            "Ложная тревога >10× цены пропуска",
            "Safety-critical контур",
        ]},
        {"label": "C · Регуляторика", "steps": [
            "Audit trail (FDA)",
            "ATEX Zone 0",
            "Указ 250 / КИИ",
        ]},
        {"label": "D · Человек", "steps": [
            "Недоверие оператора",
            "Пилот без критериев успеха",
        ]},
    ]}},
    # s34b — worked example (провал): 5 шагов рамки как плашки ✓/✗.
    "s34b": {"blocks": [
        {"label": "1 · Класс процесса", "value": "✓ дискретное",
         "note": "единичное изделие, штучный счёт"},
        {"label": "2 · Альтернативы", "value": "есть — RCM",
         "note": "виброанализ + масло + осмотр, 50 лет методика"},
        {"label": "3 · Данные", "value": "✗ провал",
         "note": "MTBF 8 лет → <100 отказов за 20 лет парка"},
        {"label": "4 · Регуляторика", "value": "✗ провал",
         "note": "SIL 2 + DO-178C — чёрный ящик не сертифицируется",
         "key": True},
        {"label": "5 · Человек", "value": "✗ нет окна",
         "note": "решение на земле, нет интерактивной эскалации"},
    ]},
    # s34c — worked example (успех): 5 шагов рамки как плашки ✓.
    "s34c": {"blocks": [
        {"label": "1 · Класс процесса", "value": "✓ дискретное",
         "note": "бутылки/банки штучно, линия 30 000/ч"},
        {"label": "2 · Альтернативы", "value": "✓ недостаточны",
         "note": "ручной отбор и периодический контроль — узкое место"},
        {"label": "3 · Данные", "value": "✓ достаточны",
         "note": "3 500 дефектных примеров/сутки · class-balance за "
                 "30 дней"},
        {"label": "4 · Регуляторика", "value": "✓ мягче",
         "note": "ISO 22000 · режим «характеристика», не финальное "
                 "решение", "key": True},
        {"label": "5 · Человек", "value": "✓ эскалация",
         "note": "8–12% потока на оператора, скорость линии позволяет"},
    ]},
    # s35 — 5-шаговая рамка: один длинный pipeline (>4) разбит на два
    # ОСМЫСЛЕННО названных ряда («оценка» / «исполнение»), не на дорожки —
    # это один линейный процесс, не параллельные линии.
    "s35": {"scheme": {"arrows": True, "rows": [
        {"label": "Оценка", "steps": [
            "Класс процесса?",
            "Альтернативы до ML?",
            "4 категории — Д/С/Р/Ч?",
        ]},
        {"label": "Исполнение", "steps": [
            "Пилот с критериями",
            "Эксплуатация + аудит",
        ]},
    ]}},
    # s38 — 5 вопросов к вендору как плашки (для кармана).
    "s38": {"blocks": [
        {"label": "1 · Baseline", "value": "до AI",
         "note": "на какой объём работы/времени сравниваем?"},
        {"label": "2 · Окно измерения", "value": "период",
         "note": "день? неделя? месяц? лучший или средний?"},
        {"label": "3 · Вмешательства", "value": "перечень",
         "note": "что автоматизировано полностью / частично / вручную?"},
        {"label": "4 · Канал OEE", "value": "A/P/Q",
         "note": "доступность / производительность / качество?"},
        {"label": "5 · Прошлые провалы", "value": "≥3 за 24 мес",
         "note": "нет ответа — либо не работал в индустрии, либо "
                 "скрывает", "key": True},
    ]},
}

# ─── таблицы — тело кадра ЗАМЕНЯЕТСЯ markdown-таблицей в памяти (та же
# техника, что `extract_title_if_missing`: правится ТОЛЬКО `Slide` этого
# прогона, файл `.md` не трогается). `body_ordered` разбирает "|"-строки
# нативно (`kind == "table"`), поэтому отдельного поля "table:" ядру не
# нужно — именно так уже устроен s33 (его markdown-таблица УЖЕ стоит в
# `.md` и не требует override вовсе, см. отчёт сессии).
TABLE_BODY = {
    "s04": (["Термин", "Определение"], [
        ["ISA-95", "Стандарт интеграции систем предприятия и "
         "производства. 5 уровней: L0 физический процесс ↔ L4 ERP."],
        ["MES", "Manufacturing Execution System — оперативное управление "
         "производством. Уровень L3: заказы, OEE-отчёты, traceability."],
        ["SCADA", "Supervisory Control And Data Acquisition — "
         "диспетчерский контроль и сбор данных. Уровень L2, мнемосхема."],
        ["PLC", "Programmable Logic Controller. Уровень L1, цикл "
         "1–10 мс, детерминированный. Сюда AI не входит как контроллер."],
        ["OEE", "Overall Equipment Effectiveness = доступность × "
         "производительность × качество. Без OEE-framing vendor-claim "
         "бессмыслен."],
        ["Мягкий сенсор", "Программная модель, оценивающая "
         "трудно-измеряемые параметры (вязкость, концентрация) по "
         "легко-измеряемым (температура, давление). Cornerstone "
         "процессного производства."],
    ]),
    "s22": (["Тип провала", "Кейс", "Урок"], [
        ["1 · Чрезмерная автоматизация",
         "Tesla 2018 — «excessive automation a mistake»",
         "Augment, не replace (Toyota Jidoka 2.0)"],
        ["2 · Сдвиг распределения",
         "CV модель A → плохо на модели B без дообучения",
         "План дообучения + drift-детектор + rules fallback"],
        ["3 · Scarce labels",
         "Rare defects 1:10000 · Boeing 737 door-plug",
         "Physical amplification + rules до ML · hybrid pipeline"],
        ["4 · Vendor self-claim",
         "Foxconn «80%» · Tata Steel «–20%» · BMW AIQX",
         "3 вопроса (baseline/окно/вмешательства) + OEE-вопрос"],
    ]),
    "s30": (["Тип провала", "Кейсы", "Урок"], [
        ["1 · RL distribution drift",
         "Batch transitions · feedstock · seasonal · wear",
         "RL дополняет MPC на scheduling, MPC — safe fallback"],
        ["2 · Regulatory blocker",
         "FDA Part 11 · ATEX Zone 0 · Указ 250",
         "Регуляторика already exists — HITL + audit trail обязательны"],
        ["3 · OT/IT раскол",
         "LLM 100–500 мс не влезает в PLC-цикл 1–10 мс",
         "Edge ML на копроцессоре, не LLM. Latency = determinism"],
        ["4 · Vendor PR без metrics",
         "ММК/НЛМК/Северсталь — общие декларации",
         "3 вопроса (baseline/окно/вмешательства); уклончивость — red "
         "flag"],
    ]),
}

# Типы кадров этой лекции, которых нет в словаре образца — добавляются,
# как и в спайке: без этого `refdeck.content()` рисует тело ОДНИМ потоком
# и ни одна форма (`blocks`/`scheme`/`columns`/`figure`) не рисуется вовсе.
refdeck.CONTENT_TYPES.update(
    {"assertion_visual", "hero_closing", "worked_example", "comparison"})


# ─── остаток тела после формы — НАЙДЕНО ТОЛЬКО ПОСЛЕ ПЕРВОЙ СБОРКИ ──────
# `apply_form_override` ДОБАВЛЯЕТ плашку/схему/столбцы/число, но НЕ трогает
# `sl.body` — исходная прозa `.md` оставалась внутри кадра целиком и
# рисовалась ВТОРЫМ слоем под формой: `slidefile.body_blocks`/`body_ordered`
# не умеют «это уже показано формой, это пропустить» — у них нет понятия
# формы вовсе. Первая сборка (см. отчёт сессии) дала на этом 75 блокирующих
# `[высота]` — тело требовало 2–5× больше места, чем осталось под ним.
# Нашлась и вторая причина того же класса: `refdeck.cover()` рисует КАЖДЫЙ
# `#`/`##`-блок тела как «head» (34 пт) — у `s01`/`s02` подзаголовки
# `## Visual`/`## Meta`/`## Цели лекции` уезжали в 34-пунктовые ложные
# заголовки, раздувая требуемую высоту без единого слова новой правки
# смысла.
#
# `BODY_OVERRIDE` — остаточное тело В ПАМЯТИ (та же техника, что
# `extract_title_if_missing`/`apply_table_body`): факты и числа — ТЕ ЖЕ,
# что в `.md`, но без повтора того, что уже стоит плашкой/осью/столбцом/
# дорожкой/числом на этом же кадре, и без вложенных `##`-подзаголовков
# (для `cover`/`hero_cover` — иначе каждый такой подзаголовок read как
# 34-пунктовый заголовок). Файл `.md` НЕ правится.
BODY_OVERRIDE = {
    "s01": ("# Tesla отступила дважды. Компании не учатся один раз.\n\n"
           "GE сожгла $4 млрд на Predix, 95% AI-пилотов не доходят до "
           "production (MIT Sloan 2025) — где AI работает, а где нет?\n\n"
           "*«Excessive automation at Tesla was a mistake. Humans are "
           "underrated» — Илон Маск, апрель 2018.*"),
    "s02": ("# AI в дискретном и процессном производстве\n\n"
           "Лекция 11 · Модуль 2 · Q&A. Курс «Применение AI в "
           "инженерии», 3 курс.\n\n"
           "Назвать два типа производства и для каждого 3–4 dominating "
           "инструмента 2026 года. Для конкретного кейса определить "
           "колонну (дискретное / процессное), AI-стек и структурный "
           "риск на стыке. Критически оценить vendor-claim «AI –70% "
           "downtime» — отличить демо от production-baseline, задать 3 "
           "уточняющих вопроса. Описать regulatory landscape (FDA Part "
           "11, ATEX, ISO 9001, Указ 250). Сформулировать 4 категории "
           "критериев «AI не нужен» и применить к учебному кейсу."),
    "s03": "",
    "s07": ("Большинство пилотов умирают между proof-of-concept и "
           "production — это и есть «застревание на пилотной стадии»."),
    "s08": ("**Урок для инженера.** Это не ошибка одного аналитика — "
           "определения сегмента и methodology расходятся. Читайте "
           "methodology, не верьте одной цифре. Gartner: весь "
           "GenAI-рынок — $644 млрд, но это все индустрии, не только "
           "производство."),
    "s09": ("AI приходит **из IT в OT** и упирается в этот раскол. LLM "
           "с задержкой 100–500 мс физически не вмещается в PLC-цикл "
           "1–10 мс."),
    "s11": ("**Демо ≠ production.** Production требует надёжности 99,9% "
           "в неконтролируемой среде × десятки тысяч часов × тысячи "
           "юнитов. Между демо и production — обычно 5–10 лет, и "
           "большинство демо не переходят."),
    "s12": "",
    "s14": ("Все три кейса требуют **эталонной разметки**: при defect "
           "rate 1–2% class imbalance заставляет учить модель на "
           "большом объёме нормальных примеров и скудных дефектах."),
    "s16": ("Это **первый критерий категории «данные»** в §4: нет "
           "эталонной разметки adequate volume → AI не работает, "
           "независимо от стека. Альтернативы: synthetic data, active "
           "learning, rules-based + ML hybrid."),
    "s18": ("**Anti-thesis к narrative «AI заменяет людей».** Toyota — "
           "крупнейший автопроизводитель мира — публично отрицает "
           "framing замены. Hyundai + Boston Dynamics: Spot для exterior "
           "QC, Atlas — первое коммерческое развёртывание гуманоида "
           "(HMGMA, Georgia)."),
    "s19": ("13 апреля 2018, твит Маска: «Excessive automation at Tesla "
           "was a mistake… Humans are underrated». Корневая причина "
           "(IMD): Tesla заменяла людей там, где variability — feature, "
           "не bug. **Automation paradox** (Bainbridge, 1983): чем "
           "больше автоматизация, тем критичнее остающиеся операторы. "
           "Альтернатива — Toyota Jidoka, работает с 1950-х на том же "
           "типе продукта."),
    "s20": ("**Hybrid:** физика амплифицирует сигнал → rules ловят "
           "60–70% → ML только на остатке 10–20%."),
    "s21": ("Young Liu (Foxconn, май 2025): «software теперь выполняет "
           "~80% работы по настройке». Vendor self-claim, не third-party "
           "metric — без baseline, окна измерения и перечня "
           "вмешательств."),
    "s25": ("RL добавляет ценность в нелинейных зонах, где PID плохо "
           "тюнится; ломается на batch transitions, смене feedstock, "
           "seasonal shift, equipment wear (далее). Альтернатива в "
           "большинстве кейсов — **MPC**: explicit, объяснимый, "
           "dominates process control; RL дополняет на high-level "
           "scheduling."),
    "s26": "",
    "s27": ("**Formula (read-out-loud): «Latency = determinism, не "
           "только speed».** F-35 ALIS callback (лекция 9): $44 000 / "
           "лётный час, заменён ODIN — defense PdM учит тому же, что "
           "промышленный."),
    "s28": ("**Урок.** Регуляторика уже существует. AI должен fit "
           "existing frameworks, не наоборот. Audit trail обязателен; "
           "HITL обязателен в safety-critical контурах."),
    "s29": ("**Урок для инженера (LO2).** Public-disclosure скудна — "
           "анти-pattern в reporting, не доказательство absence "
           "adoption. Различать PR statement и измеримый эффект — "
           "симметрично для РФ и западных вендоров."),
    "s32": ("**Три вопроса к вендору:** 1) базовая линия до AI, 2) окно "
           "измерения, 3) перечень вмешательств. +4-й — в какой "
           "компонент OEE добавляется эффект?"),
    "s33": ("| Инструмент | Когда применим | Плюсы | Минусы | Regulatory |\n"
           "|---|---|---|---|---|\n"
           "| **SPC** | Стабильные параметры | Дёшево, 100 лет в "
           "промышленности | Не ловит multi-variate | ✓ FDA/GAMP |\n"
           "| **DOE** | Малые партии | Causal inference | Не online | "
           "✓ |\n"
           "| **MPC** | Online control | Explicit, dominates | Нужна "
           "точная модель | ✓ |\n"
           "| **RCM** | MTBF > 1 года | Calibrated к физике | Не "
           "learning из отказов | ✓ |\n"
           "| **Physics-sim** | Известная физика | Обобщается на новое "
           "| Дорогая разработка | ✓ |\n"
           "| **Rules-vision** | Controlled env | Validated за неделю "
           "| Не держит variability | ✓ |\n\n"
           "**Hybrid:** PINN · CIRL · ML over SPC · PLC + edge ML "
           "coprocessor."),
    "s34b": ("Газотурбинный авиадвигатель, MTBF 8 лет. Производитель "
           "спрашивает: можно ли AI для прогностического обслуживания? "
           "Три из пяти шагов проваливают рамку."),
    "s34c": ("Пивоварня, 30 000 бутылок/час (~700 000/сутки), брак "
           "~0,5%. Ручной отбор и периодический контроль пропускают "
           "дефекты на скорости конвейера. Все пять шагов рамки "
           "проходят."),
    "s35": ("**Гибридные паттерны (закрытие):** PINN (физические "
           "ограничения в loss) · CIRL (PID в loss function RL) · ML "
           "поверх SPC · PLC + ML-копроцессор на крае."),
    "s38": ("**Типичные студенческие вопросы.** «SPC или ML?» — зависит "
           "от регуляторной среды и числа переменных; гибрид SPC+ML "
           "защищается перед регулятором. «RL или MPC?» — MPC доминирует "
           "в контуре, RL дополняет на планировании; безопасный откат к "
           "MPC обязателен."),
    # s39 — hero_closing: bridge-текст сжат до сути, полный список
    # отдельных инструментов (CV/soft sensors/PdM/foundation models) и
    # цитаты по BMW/Holcim/Foxconn оставлены — это НЕ дублирует форму
    # (у s39 формы нет, только hero media), просто короче прозы `.md`.
    "s39": ("**BMW:** 30+ заводов digital-twin-ready (2024–2025), NVIDIA "
           "GTC Paris 2025. **Holcim:** первый в мире digital-twin "
           "цементный завод (2024). **Foxconn-NVIDIA Omniverse:** digital "
           "twin для smart factories.\n\n"
           "Сегодня — отдельные инструменты: CV-инспекция, мягкие "
           "сенсоры, PdM, foundation models. **Лекция 12 — сшивка** в "
           "единый production-fabric через цифровые двойники; ГОСТ Р "
           "57700.37-2021 — regulatory ground в РФ."),
}


def apply_body_override(sl):
    if sl.sid not in BODY_OVERRIDE:
        return
    sl.body = BODY_OVERRIDE[sl.sid]
    sl._cache.clear()


def apply_form_override(sl):
    ov = FORM_OVERRIDE.get(sl.sid)
    if not ov:
        return
    for key in ("type", "blocks", "columns", "scheme", "figure"):
        if key in ov:
            sl.meta[key] = ov[key]


def apply_table_body(sl):
    spec = TABLE_BODY.get(sl.sid)
    if not spec:
        return
    headers, rows = spec
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    sl.body = "\n".join(lines)
    sl._cache.clear()


def content_adapter(p, sl, root, g):
    # ПОРЯДОК ОБЯЗАТЕЛЕН: заголовок достаётся из ОРИГИНАЛЬНОГО тела ДО
    # того, как `apply_body_override` его заменит остатком — иначе `sl.title`
    # останется пуст, и `heading()` не нарисует заголовок вовсе.
    extract_title_if_missing(sl)
    apply_body_override(sl)
    apply_table_body(sl)
    apply_form_override(sl)
    return refdeck.content(p, sl, root, g)


# `section_divider` (deck.yaml этой лекции) — то же, что `divider` у
# образца, но имя кадра этой лекции другое. `hero_cover`/`cover` → один и
# тот же builder; `hero_closing` НЕ сюда — это content() с hero (как
# у Лекции 9), дальше по умолчанию попадает в `content_adapter`.
BUILDERS = {
    "section_divider": refdeck.divider,
    "divider": refdeck.divider,
    "cover": refdeck.cover,
    "hero_cover": refdeck.cover,
}


def build(slides_dir, out, *, root, only=None):
    root = root or slides_dir
    p = prims.new_deck()
    n = 0
    for f in slidefile.slide_files(slides_dir, only):
        sl = slidefile.read_slide(f)
        if sl is None:
            continue
        apply_media_override(sl)
        kind = str(sl.meta.get("type") or "assertion_visual").strip()
        builder = BUILDERS.get(kind, content_adapter)
        # `cover`/`hero_cover` не проходят через `content_adapter` (нет
        # заголовка через `heading()`, нет `extract_title_if_missing`) —
        # остаток тела подставляется здесь же, напрямую, до вызова builder.
        if builder is not content_adapter:
            apply_body_override(sl)
        s = builder(p, sl, root, refdeck.G)
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
                    help="собрать ТОЛЬКО эти sid, в отдельный *-partial.pptx")
    args = ap.parse_args()

    report.reset()
    out = PARTIAL if args.only else OUT
    n = build(SLIDES_DIR, out, root=LEC_ROOT, only=args.only)
    blocking = report.report(n, out_name=out.name)

    shares, rows = rnd.verify_built(out, partial=bool(args.only))
    bad = [r for r in rows if r["ok"] is False]
    if bad:
        for r in bad:
            print(f"  стр {r['page']} {r['shape']}: «{r['text']}» — "
                  f"{r['ratio']:.2f}:1 (порог {r['thr']:.1f}:1)")

    if args.render:
        rc = rnd.render(out, SNAPS)
        if rc:
            return rc

    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
