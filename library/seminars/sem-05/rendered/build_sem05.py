#!/usr/bin/env python3
"""Сборка деки Семинара 5 из source-of-truth: ../deck.yaml + ../slides/sNN-*.md

Устройство. Это СБОРЩИК ИЗ БИБЛИОТЕКИ ПРИЁМОВ (`deck_kit.py`), а не укладчик
блоков. Приём выбирается по полю `visual.pattern`, которое уже заполнено во
всех 56 слайдах и которое прежний рендерер не читал вовсе — он ветвился по
`type` и по наличию блоков, отчего 30 разных замыслов укладывались пятью
одинаковыми раскладками сверху вниз.

Середина между двумя крайностями: Семинар 4 верстал 57 функций под каждый
слайд (перенести нельзя — они привязаны к его содержанию), Семинар 5 верстал
всё одним стеком полноширинных коробок (видно, что получилось). Здесь —
универсальный сборщик плюс словарь именованных приёмов, где каждый слайд
называет свой приём сам.

Три правила, которые держит этот файл:

* Высота каждого блока ИЗМЕРЯЕТСЯ (`metrics.py`), а не оценивается по числу
  элементов, и замеряется тем же кодом, который потом рисует, — блок сначала
  рисуется на черновом слайде, который выбрасывается. Разойтись замер и
  отрисовка поэтому не могут.
* Вёрстка идёт ОТ КУРСОРА: каждый приём возвращает занятую высоту. Жёстких
  координат, в которые можно напечатать поверх уже нарисованного, здесь нет.
* Воздух — параметр, а не остаток: если содержимое не заполнило полотно,
  композиция центрируется, а не прижимается к верху.

Тексты слайдов и схемы `make_figures*.py` этот файл не трогает.
"""
import re
import sys
from pathlib import Path

import yaml
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

import deck_kit as K
import metrics as M
import slide_parts as SP

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
FIGDIR = HERE / "figures"

TOP, BOTTOM = 0.34, 6.92        # рабочее поле по вертикали
LEFT, WIDTH = 0.55, 12.23       # и по горизонтали
GAP = 0.18                      # шаг между блоками

# ── Где мы: короткое имя раздела для надзаголовка ────────────────────────────
#
# Границы заданы ОТДЕЛЬНО для каждой нумерации, а не одним списком по номеру.
# Старая дека (`sNN`) и новая (`nNN`) живут в репозитории одновременно, пока
# блоки пересобираются параллельными сессиями, и номера у них пересекаются:
# 22-й слайд старой деки — «Скилл», 22-й новой — всё ещё «Хук». Один список по
# номеру обслуживает ровно одну из двух и врёт про вторую — именно так на
# n22–n32 в надзаголовке стояло «СКИЛЛ» посреди блока хуков.
SECTIONS_BY_PREFIX = {
    "s": ([(1, 6, "Открытие", None), (7, 20, "Хук", 0), (21, 32, "Скилл", 1),
           (33, 45, "Доступ наружу", 2), (46, 50, "Сборка", None)],
          ["Хук", "Скилл", "Доступ наружу"]),
    # Новая дека, 63 слайда: шесть кейсов — три про хуки, три про скиллы.
    # Доступ наружу решением владельца уехал в Занятие 6 целиком.
    #
    # n33 — отдельной строкой, и это не описка: по номеру он попадает в
    # диапазон скиллов, а по смыслу закрывает блок хуков (граница кейса К3).
    # Границы разделов идут ПО СМЫСЛУ, а не по арифметике номеров; полосатый
    # диапазон выглядит странно ровно до тех пор, пока не посмотришь на слайд.
    "n": ([(1, 5, "Открытие", None), (6, 33, "Хук", 0), (34, 58, "Скилл", 1),
           (59, 63, "Сборка", None)],
          ["Хук", "Скилл"]),
}
SECTIONS, STAGES = SECTIONS_BY_PREFIX["s"]      # совместимость: прежние имена

# ── Что это за шаг: жанр слайда по его приёму ───────────────────────────────
# Это и есть потерянный приём Семинара 4 — одна строка, которая отвечает
# и на «вопрос это или утверждение», и на «мы ещё в том же кейсе».
GENRE = {
    "hero_cover": "", "lecture_map": "карта занятия",
    "keystone_scope_map": "ось занятия", "recap_table": "ось занятия",
    "closing_question_partial": "возврат к вопросу открытия",
    "question_repeat": "тот же вопрос, второй раз",
    "transfer_exercise": "перенос на свой репозиторий",
    "assertion_visual": "ограничение",
    "section_divider_macro": "",
    "problem_scenario": "завязка", "question_with_option_cards": "вопрос",
    "base_and_edge": "база",
    "evidence_table_with_gap": "свидетельства",
    "answer_breakdown_table": "разбор", "dual_mode_breakdown": "разбор",
    "cobuilding_config_reveal": "собираем вместе",
    "cobuilding_bad_example_reveal": "собираем вместе",
    "cobuilding_description_assembly": "собираем вместе",
    "code_artifact": "артефакт", "file_tree_snapshot": "артефакт",
    "failure_vignette": "провал",
    "criteria_checklist_and_boundary": "критерий и граница",
    "axis_placement": "строка оси", "token_cost_table": "цена",
}
MECHANICS_TAG = "механика"

TAGS = {"s07": "1 кейс · 2 слоя провала · 5 форм обхода",
        "s21": "1 кейс · 2 слоя провала · 6 причин молчания",
        "s33": "1 кейс · 3 слоя провала · 3 области видимости",
        # Новая дека: развилка каждого кейса. Ярлык называет, из чего кейс
        # состоит, — и ни в одном нет слова «хук»: развилка называет боль.
        "n06": "1 кейс · 5 решений сборки · 2 слоя провала",
        "n17": "1 инцидент · 5 клеток · 8 способов промолчать",
        "n25": "1 случай · 3 замера · 5 вариантов действия",
        "n34": "3 повода завести · 2 измерения · 1 наш файл",
        "n43": "3 части описания · 2 длины, которые путают",
        "n51": "13 скиллов · 1 с описанием · 5 средств ревизии"}
# Номер на значке развилки — номер КЕЙСА, а не ступени. Кейсов шесть, и счёт
# СКВОЗНОЙ через всю деку: три про хуки (1–3), три про скиллы (4–6). Номер
# ступени на значке не нужен — ступень и так видна полосой сверху и дорожкой
# внизу, а зал считает кейсы: «это четвёртый из шести», а не «второй из двух».
BADGE = {"s07": 3, "s21": 4, "s33": 5,
         "n06": 1, "n17": 2, "n25": 3, "n34": 4, "n43": 5, "n51": 6}

FIGS={
    "n01": "ramka-n01-hero.png",
    "n05": "ramka-n05-karta.png",
    "n62": "ramka-n62-chto-razlozheno.png",
    "n63": "ramka-n63-korziny.png",
    "s01": "hero-barier.png",
    "s05": "pravilo-poryadka.png",
    "s06": "karta-stupeney.png",
    "s08": "khuk-scene.png",
    "s12": "khuk-cobuild.png",
    "s14": "bypass.png",
    "s15": "khuk-blindspot.png",
    "s16": "khuk-tochka-i-vhod.png",
    "s17": "contract.png",
    "s18": "khuk-debug.png",
    "s22": "skill-sluchay.png",
    "s28": "skill-uroven-odin.png",
    "s29": "skill-otladka.png",
    "s30": "skill-vred.png",
    "s34": "mcp-stsena.png",
    "s36": "mcp-lestnitsa.png",
    "s37": "mcp-poryadok-proverok.png",
    "s38": "mcp-vycherkivanie.png",
    "s39": "mcp-podklyuchenie.png",
    "s40": "mcp-anatomiya.png",
    "s41": "mcp-ot-fayla.png",
    "s42": "mcp-poryadok-otladki.png",
    "s43": "mcp-trio.png",
    "s44": "mcp-podmena.png",
    "s47": "mcp-chto-gruzitsya.png",
    "s49": "itog-chto-razlozheno.png",
    "s50": "itog-tri-korziny.png",
    # Блок «Хуки» новой деки, n06–n32 — девять схем
    "n07": "khuki-n07-stsena.png",
    "n12": "khuki-n12-ustroystvo.png",
    "n13": "khuki-n13-sborka.png",
    "n15": "khuki-n15-proval.png",
    "n18": "khuki-n18-stsena.png",
    "n22": "khuki-n22-kletki.png",
    "n26": "khuki-n26-stsena.png",
    "n29": "khuki-n29-umnozhenie.png",
    "n32": "khuki-n32-sloi.png",
    # Блок «Скиллы», n34–n58 — четыре схемы
    "n40": "skilly-dvoynaya-oplata.png",
    "n41": "skilly-otbor.png",
    "n52": "skilly-nalog.png",
    "n57": "skilly-relevantnyy-vred.png",
}


def num(sid):
    return int(sid[1:])


# ── Границы разделов выводятся ИЗ САМОЙ ДЕКИ, а не задаются номерами ────────
#
# Номера в `SECTIONS_BY_PREFIX` — запасной вариант и документация замысла. Сами
# же границы считаются по опорным точкам, которые дека объявляет о себе: пять
# приёмов встречаются в ней ровно по одному разу, а `section_divider_macro` —
# ровно шесть раз, по числу кейсов.
#
#   `lecture_map`           → последний слайд Открытия
#   1-й `section_divider_macro` → начало блока хуков
#   4-й `section_divider_macro` → начало блока скиллов (кейсы 1–3 хуки, 4–6 скиллы)
#   `recap_table`           → начало Сборки
#
# Почему не номерами. Номера переписывались уже трижды: 33–45 «Доступ наружу»
# → n06–n32 хуки → n06–n33 после переезда границы К3 → и снова после вставки
# нового кейса у скиллов, когда рамка уехала с n59 на n60. Каждый раз между
# вставкой слайда и правкой этой таблицы надзаголовок на хвосте деки ВРАЛ, и
# заметить это можно было только глазами. Правило, записанное числом, ломается
# на первой же вставке; правило, выведенное из структуры, переживает её.
_DERIVED = {}


def _anchor_sections(slides):
    """Границы по опорным приёмам. `None`, если опор не хватает."""
    pat = [((s.get("visual") or {}).get("pattern", ""), num(s["id"])) for s in slides]
    div = [n for p_, n in pat if p_ == "section_divider_macro"]
    recap = next((n for p_, n in pat if p_ == "recap_table"), None)
    if len(div) < 4 or recap is None:
        return None
    last = max(n for _p, n in pat)
    return [(1, div[0] - 1, "Открытие", None),
            (div[0], div[3] - 1, "Хук", 0),
            (div[3], recap - 1, "Скилл", 1),
            (recap, last, "Сборка", None)], ["Хук", "Скилл"]


def _deck_slides(prefix):
    if prefix == "n":
        return deck_from_files("n")
    try:
        return yaml.safe_load((ROOT / "deck.yaml").read_text(encoding="utf-8"))["slides"]
    except Exception:
        return []


def sections_for(sid):
    """Границы разделов и ступени дорожной карты для нумерации этого слайда."""
    pre = sid[0]
    if pre not in _DERIVED:
        try:
            _DERIVED[pre] = _anchor_sections(_deck_slides(pre))
        except Exception:
            _DERIVED[pre] = None
    return _DERIVED[pre] or SECTIONS_BY_PREFIX.get(pre, (SECTIONS, STAGES))


def where(sid):
    n = num(sid)
    for lo, hi, name, stage in sections_for(sid)[0]:
        if lo <= n <= hi:
            return name, stage
    return "", None


def label_for(sid, pattern):
    """Надзаголовок «где мы · что это за шаг»."""
    name, _ = where(sid)
    genre = GENRE.get(pattern, MECHANICS_TAG if pattern.startswith("mechanics") else "")
    return f"{name} · {genre}" if genre else name


def figure_for(sid):
    """Автоподбор схемы по имени файла — `figures/<id>.png` или `<id>-*.png`.
    Поведение сохранено ровно как было: 23 схемы сделаны отдельно и хорошо."""
    cand = []
    if not cand and sid in FIGS and (FIGDIR / FIGS[sid]).exists():
        cand = [FIGDIR / FIGS[sid]]
    return cand[0] if cand else None


# ── Замер = отрисовка ───────────────────────────────────────────────────────
_scratch = Presentation()
_scratch.slide_width, _scratch.slide_height = Inches(K.W_IN), Inches(K.H_IN)


def measure(fn, *a, **kw):
    """Высота блока, полученная ТЕМ ЖЕ кодом, который его рисует: блок
    рисуется на черновом слайде, высота запоминается, слайд выбрасывается.
    Замер и отрисовка поэтому не могут разойтись — а именно это расхождение
    (`0.40 × число строк` против реальной высоты) и роняло прежнюю вёрстку."""
    sl = _scratch.slides.add_slide(_scratch.slide_layouts[6])
    saved = list(M._WARNINGS)
    h = fn(sl, *a, **kw)
    M._WARNINGS[:] = saved      # предупреждения чернового прохода не печатаем
    return h


# ── Роль блока: какую работу он делает на слайде ────────────────────────────

# Приём слайда (`visual.pattern`) объявляет работу; текст её только уточняет.
# Это надёжнее, чем угадывать по одним лишь кавычкам: вопрос залу далеко не
# всегда кончается знаком вопроса — из 56 слайдов таких оказалось два, а
# остальные вопросы сформулированы повелительно («Выберите, куда её вынести»).
PATTERN_ROLE = {
    "question_with_option_cards": "question",
    "question_repeat": "question",
    "closing_question_partial": "question",
    "transfer_exercise": "question",
    "evidence_table_with_gap": "caveat",
    "answer_breakdown_table": "formula",
    "failure_case_story": "fact",
    "problem_scenario_ledger": "fact",
    "dual_mode_breakdown": "formula",
    "failure_vignette": "formula",
    "criteria_checklist_and_boundary": "formula",
    "axis_placement": "fact",
    "assertion_visual": "fact",
    # Карта занятия НЕ формула. Золотая планка слева означает «это надо
    # запомнить» — на слайде-карте запоминать нечего, он отвечает на «где мы и
    # куда идём». Без этой строки карта проваливалась в `formula` по умолчанию
    # и получала набор форм, неотличимый от слайда-правила (`dual_mode_
    # breakdown`), хотя работы у них разные: одна даёт правило, вторая
    # ориентирует. Это и показал аудит совпадением наборов.
    "lecture_map": "fact",
    "token_cost_table": "fact",
    "base_and_edge": "fact",
}

ASK = re.compile(r"выберите|что бы вы|как бы вы|назовите|подумайте", re.I)
CAVEAT = re.compile(r"честн|не наш|не проверен|не измер|нет данных|не найден|"
                 r"оговорк|не подтвер|пробел|не удалось|не ставит", re.I)


def quote_role(lines, pattern):
    """Какую работу делает этот блок-цитата.

    Прежняя вёрстка красила золотом ЛЮБУЮ цитату — и золотая коробка встала на
    33 слайдах из 56, в основном под утверждениями. Сигнал, который у Семинара
    4 означал «вопрос или формула», обнулился частотой. Здесь у каждой работы
    своя форма, и золотая заливка с рамкой остаётся ровно за вопросом."""
    body = " ".join(K.plain(l) for l in lines).strip()
    if body.rstrip("»\"' ").endswith("?") or ASK.search(body):
        return "question"
    if CAVEAT.search(body):
        return "caveat"
    base = PATTERN_ROLE.get(pattern)
    if base == "question":          # вопрос уже нашёлся бы выше — значит это подводка
        return "speech" if body.lstrip().startswith("«") else "fact"
    if body.lstrip().startswith("«"):
        return "speech"
    return base or "formula"


FORM = {"question": K.form_question, "formula": K.form_formula,
        "speech": K.form_speech, "caveat": K.form_caveat, "fact": K.form_fact}

# Абзац целиком в звёздочках — тихая ремарка. Форма та же, что у реплики
# докладчика: приглушённый курсив с тиловой линией слева.
ITALIC_LINE = re.compile(r"^\s*\*([^*].*?)\*\s*$")
# Курсив ВНУТРИ строки вёрстка не умеет — о нём говорит `metrics.fits()`,
# потому что её зовут все формы и каждая ячейка таблицы, а не только эта ветка.


def para_role(text, pattern):
    """Какую работу делает ГОЛЫЙ абзац и каким текстом он выйдет на слайд.

    Голый абзац в `## Visual` — это тот же материал, что и абзац в плашке
    `>`; отличается он только тем, как автор его набрал. Прежде вёрстка
    считала его «спецификацией для дизайнера» и не выводила вовсе. По факту
    во всех 50 слайдах прежней деки нет НИ ОДНОГО такого абзаца — то есть
    правило описывало намерение, а не наблюдение, и первый же раздел новой
    деки потерял на нём 18 абзацев на 8 слайдах, ничего не сказав."""
    m = ITALIC_LINE.match(text)
    if m:
        return "speech", m.group(1).strip()
    return quote_role([text], pattern), text


def split_question(lines):
    """Разделить блок на СЦЕНУ и сам ВОПРОС.

    Вопрос к залу в исходнике почти всегда дописан в конец того же абзаца, что
    и сцена: «Правило записано… Коммит всё равно случился. Выберите, как
    сделать нарушение невозможным». Целиком в золотой коробке это четыре
    строки, из которых вопрос — последняя: коробка перестаёт читаться как
    вопрос и становится просто самым большим текстом на слайде.

    Режем по границе предложения, по ПЕРВОМУ предложению-вопросу: всё до него
    — сцена, всё от него и дальше — вопрос (за вопросом часто идёт уточнение
    вроде «назовите недостающие части», и оно принадлежит вопросу, а не сцене).
    Текст не меняется ни на знак — меняется только то, какой формой набрана
    каждая его часть.

    Возвращает `(сцена, вопрос, нашёлся ли вопрос)`. Третье значение
    обязательно: «вопрос занял весь блок» и «вопроса в блоке нет вовсе» прежде
    возвращались одинаково — пустой сценой и блоком целиком во второй позиции.
    Из-за этого ЛЮБАЯ цитата на слайде-вопросе уезжала в золотую коробку,
    включая подводку без единого вопросительного знака, и на слайде оказывалось
    ДВЕ золотые коробки: одна под цитатой из файла, вторая под настоящим
    вопросом. Золотая заливка с рамкой существует ровно в одном месте — на
    вопросе, — и две такие коробки на одном слайде обнуляют сигнал ровно так
    же, как его обнуляла одна кремовая плашка на 31 слайде из 56.
    """
    flat = " ".join(lines)
    # предложение = до точки/воскл./вопр./многоточия, вместе с закрывающими кавычками
    bounds, pos = [], 0
    for m in re.finditer(r"[.!?…]+[»\"\')\s]*", flat):
        bounds.append((pos, m.end()))
        pos = m.end()
    if pos < len(flat):
        bounds.append((pos, len(flat)))
    for a, b in bounds:
        sent = flat[a:b]
        if "?" in sent or ASK.search(sent):
            if a == 0:
                return [], [flat.strip()], True     # вопрос занимает весь блок
            return [flat[:a].strip()], [flat[a:].strip()], True
    return [], lines, False                         # вопроса в блоке нет


def unseen(sid, pattern, blocks, handled, why):
    """Сказать вслух про блоки, которые этот жанр рисовать не будет.

    Нужна там, где жанр строит композицию сам и до `block_drawer` блоки не
    доводит. Правило на всю вёрстку одно: **блок либо нарисован, либо назван в
    предупреждении**. Молча исчезнуть он не может нигде — потерянный блок
    ничем не отличается от ненаписанного, и заметить его можно только сверкой
    текста собранного файла с исходником, чего никто не делает.
    """
    for kind, _b in blocks:
        if kind not in handled:
            M._WARNINGS.append(f"БЛОК НЕ ПОКАЗАН [{sid} · {pattern}]: блок вида "
                               f"«{kind}» — {why}")


# ── Отрисовка одного блока ──────────────────────────────────────────────────

def block_drawer(kind, b, sid, pattern, *, role=None):
    """Блок → приём. Одна работа — одна форма, форма под другую работу не
    переиспользуется. Возвращает функцию (sl, y, max_h) -> занятая высота."""
    if kind == "quote":
        r = role or quote_role(b, pattern)
        fn = FORM[r]
        return lambda sl, y, mh: fn(sl, LEFT, y, WIDTH, b, max_h=mh, label=f"{sid} {r}")
    if kind == "table":
        headers, rows = b
        return lambda sl, y, mh: K.table_card(sl, LEFT, y, WIDTH, headers, rows,
                                              max_h=mh, label=f"{sid} таблица")
    if kind == "code":
        lang, lines = b
        return lambda sl, y, mh: K.terminal_card(sl, LEFT, y, WIDTH, lines, max_h=mh,
                                                 markup=lang in ("markdown", "md"),
                                                 label=f"{sid} код")
    if kind == "cards":
        # «выбери» и «запомни» — разные работы, значит разные формы
        if pattern == "question_with_option_cards":
            return lambda sl, y, mh: K.option_row(sl, LEFT, y, WIDTH, b,
                                                  max_h=min(mh or 1.7, 1.7),
                                                  label=f"{sid} варианты")
        return lambda sl, y, mh: K.term_pills(sl, LEFT, y, WIDTH, b, label=f"{sid} термины")
    if kind == "bullets":
        return lambda sl, y, mh: K.numbered_list(sl, LEFT, y, WIDTH, b, max_h=mh,
                                                 label=f"{sid} список")
    if kind == "para":
        r, text = para_role(b, pattern)
        fn = FORM[role or r]
        return lambda sl, y, mh: fn(sl, LEFT, y, WIDTH, [text], max_h=mh,
                                    label=f"{sid} {role or r}")
    # Сюда попадает только вид блока, которого вёрстка не знает. Молчать
    # нельзя: потерянный блок ничем не отличается от ненаписанного.
    M._WARNINGS.append(f"БЛОК НЕ ПОКАЗАН [{sid} · {pattern}]: блок вида «{kind}» "
                       f"ни один приём не рисует — содержание пропало бы молча")
    return None


def compose(sl, sid, y0, drawers, *, bottom=BOTTOM, center=True):
    """Универсальная укладка: сначала все блоки меряются, потом раскладываются.

    Если содержимого меньше, чем полотна, лишнее место становится ВОЗДУХОМ —
    композиция центрируется в оставшемся поле и получает увеличенные интервалы.
    Прежнее правило «блоки сверху, остаток вниз» давало больше 1,4″ пустоты
    внизу на 27 слайдах из 56 и 3,4–3,7″ на четырёх.

    Если содержимого больше — бюджет режется пропорционально, и каждый приём
    сам ужимает кегль; что не влезло, попадает в список предупреждений, а не
    выезжает за край молча.
    """
    if not drawers:
        return
    avail = bottom - y0
    nat = [measure(d, y0, None) for d in drawers]
    total = sum(nat) + GAP * (len(nat) - 1)

    if total <= avail:
        # Лишнее место сначала уходит в интервалы между блоками, остаток — в
        # паузу под заголовком: Семинар 4 держал её осознанно и вешал
        # композицию в нижних ¾ полотна. Правило «блоки сверху, остаток вниз»
        # давало больше 1,4″ пустого низа на 27 слайдах из 56.
        slack = avail - total
        gap = GAP + min(slack / max(len(nat), 1), 0.55)
        used = sum(nat) + gap * (len(nat) - 1)
        # `center` — доля, а не флаг: True = 0.8 (композиция висит в нижних ¾,
        # приём Семинара 4), False = 0.0 (блоки сверху), число = как задано.
        # Такту Б нужна ровно 1.0: на нём мало текста по построению, и при 0.8
        # под дорожками остаётся полоса пустоты вдвое шире, чем над ними.
        kc = 0.8 if center is True else (0.0 if center is False else float(center))
        y = y0 + (avail - used) / 2 * kc
        for d, h in zip(drawers, nat):
            d(sl, y, None)
            y += h + gap
        return

    budget = avail - GAP * (len(drawers) - 1)
    k = budget / sum(nat)
    y = y0
    for d, h in zip(drawers, nat):
        drawn = d(sl, y, max(h * k, 0.5))
        y += drawn + GAP

    # Урезание бюджета — просьба, а не гарантия: у каждой формы есть пол по
    # кеглю, а таблица, которая не влезла даже после сжатия, честно возвращает
    # СВОЮ высоту, а не отведённую. Значит курсор может уехать ниже рабочего
    # поля, и последний блок окажется поверх номера слайда или вовсе за краем
    # полотна — то есть исчезнет, не сказав ни слова. Здесь он говорит.
    end = y - GAP
    over = end - bottom
    if over > 0.02:
        # Две разные беды, и путать их нельзя. Ниже рабочего поля, но на
        # полотне — блок видно, просто номер слайда ложится поверх него. Ниже
        # ПОЛОТНА — блока в PowerPoint не видно вовсе, а файл при этом
        # собирается без единой жалобы: ровно тот молчаливый пропуск, который
        # ищется сверкой текста, а не глазами.
        if end > K.H_IN - 0.15:
            M._WARNINGS.append(
                f"ЗА КРАЕМ ПОЛОТНА [{sid}]: композиция кончается на {end:.2f}″ при "
                f"высоте полотна {K.H_IN:.2f}″ — нижний блок в PowerPoint не виден вовсе")
        else:
            M._WARNINGS.append(
                f"НЕ ПОМЕСТИЛОСЬ [{sid}]: композиция на {over:.2f}″ ниже рабочего поля — "
                f"блок заходит в поле подписи, номер слайда ляжет поверх него")


# ── Жанры слайдов ───────────────────────────────────────────────────────────

def g_divider(sl, sid, title, blocks, pattern, assertion=""):
    """Дивайдер уровня раздела: градиент DEEP→MID→LIGHT, широкая золотая
    полоса прогресса, номерной значок, смысловая строка, ярлык — и дорожная
    карта внизу.

    Ярлык рисуется ОТ КУРСОРА. Прежняя вёрстка печатала его жёстко в
    `Inches(3.0)` — ровно туда, где уже стоял абзац, — и два текстовых блока
    ложились друг на друга буква в букву на s07 и s21; на s33 он прошивал
    рамку коробки-цитаты. Три разделителя, три разные поломки, одна причина.

    Смысловая строка берётся из `## Assertion` самого слайда, если в `##
    Visual` её нет: у s07 в Visual лежал только собственный заголовок,
    напечатанный второй раз, и раздел на 16 слайдов открывался пустым полем.
    Ничего не дописывается — используется текст, который у слайда уже есть."""
    _, stage = where(sid)
    stages = sections_for(sid)[1]
    K.divider_bg(sl)
    K.strip_pills(sl, LEFT, 0.5, 11.3, len(stages), stage if stage is not None else -1)

    meaning = []
    for kind, b in blocks:
        for ln in (b if kind == "quote" else ([b] if kind == "para" else [])):
            rest = K.plain(ln)
            if rest.lower().startswith(K.plain(title).lower()):
                # После снятия заголовка-приставки впереди остаётся знак,
                # которым он кончался в предложении: «Тела скилла в контексте
                # нет. До срабатывания…» → «. До срабатывания…». Точку надо
                # снимать вместе с приставкой — это её хвост, а не начало
                # оставшейся фразы.
                rest = rest[len(K.plain(title)):].strip(" ·—–-.,;:!?")
            if rest and rest != TAGS.get(sid, ""):
                meaning.append(rest)
    if not meaning and assertion:
        meaning = [K.plain(assertion)]
    # Дивайдер — единственный жанр, который НЕ проводит блоки через
    # `block_drawer`: у него своя композиция из заголовка, смысловой строки и
    # ярлыка. Значит и сказать о непоказанном блоке он обязан сам.
    unseen(sid, pattern, blocks, {"quote", "para"},
           "на развилке рисуются только заголовок, смысловая строка и ярлык")

    # композиция считается целиком, потом центрируется между полосой и картой
    tw = 10.0
    th = M.text_h(K.plain(title), 34, tw, spacing=1.05, bold=True)
    # резерв на одну строку больше измеренного: перенос в настоящем Arial
    # может разойтись с замером по DejaVu, и лучше оставить воздух, чем
    # подпустить смысловую строку вплотную к ярлыку
    mh = (M.block_h(meaning, 17, 10.4, spacing=1.32, space_after=4)
          + M.line_h(17, 1.32)) if meaning else 0.0
    tag_h = 0.55 if sid in TAGS else 0.0
    total = th + (mh + 0.34 if meaning else 0) + (tag_h + 0.30 if tag_h else 0)
    y = 1.25 + max((5.2 - total) / 2, 0.0)

    if sid in BADGE:
        K.divider_badge(sl, BADGE[sid], cy=y + th / 2)
    K.text_box(sl, 1.68, y, tw, th, title, size=34, bold=True, color=K.WHITE, spacing=1.05)
    y += th + 0.34
    if meaning:
        K.text_box(sl, LEFT + 0.35, y, 10.4, mh, meaning, size=17, italic=True,
                   color=K.ON_DARK, spacing=1.32, space_after=4)
        y += mh + 0.30
    if tag_h:
        K.tag_plate(sl, LEFT + 0.35, y, TAGS[sid])
    if stage is not None:
        K.roadmap(sl, stages, stage)
    K.slide_id_mark(sl, sid, on_dark=True)


def g_cover(sl, sid, title, blocks, pattern, assertion=""):
    """Обложка: тёмный фон, крупный заголовок, иллюстрация во всю ширину,
    центральный вопрос занятия — в золотой коробке поверх неё."""
    K.set_bg(sl, K.DEEP)
    K.text_box(sl, 0.9, 0.42, 11.5, 1.5, title, size=33, bold=True, color=K.WHITE,
               anchor=MSO_ANCHOR.BOTTOM, spacing=1.08)
    K.rect(sl, 0, 2.02, K.W_IN, 0.07, K.GOLD)
    y, bottom = 2.34, BOTTOM

    hero = figure_for(sid)
    if hero:
        from PIL import Image
        iw, ih = Image.open(hero).size
        fh = K.W_IN * ih / iw
        sl.shapes.add_picture(str(hero), Inches(0), Inches(K.H_IN - fh), width=Inches(K.W_IN))
        bottom = K.H_IN - fh - 0.2

    unseen(sid, pattern, blocks, {"quote"},
           "на обложке рисуются иллюстрация и центральный вопрос")
    quotes = [b for k, b in blocks if k == "quote"]
    if quotes:
        lines = [l for q in quotes for l in q]
        question = [l for l in lines if K.plain(l).rstrip("»\"' ").endswith("?")]
        rest = [l for l in lines if l not in question]
        if rest:
            h = M.block_h([K.plain(l) for l in rest], 15, 11.5, space_after=4)
            K.rect(sl, 0.9, y + 0.04, 0.035, h - 0.08, K.TEAL)
            K.text_box(sl, 1.2, y, 11.2, h, rest, size=15, color=K.ON_DARK, space_after=4)
            y += h + 0.26
        if question:
            K.form_question(sl, 0.9, y, 11.5, question, size=17,
                            max_h=max(bottom - y, 0.7),
                            label=f"{sid} центральный вопрос")
    K.slide_id_mark(sl, sid, on_dark=True)


def g_question(sl, sid, title, blocks, pattern, assertion=""):
    """Вопрос — отдельный жанр из трёх сигналов сразу: надзаголовок «· ВОПРОС»,
    дословный вопрос в золотой коробке, серая подпись «разбор — на следующем
    слайде». Ни одной цифры, ни одного подсвеченного варианта: голосование
    идёт вслепую.

    Прежде вопрос отличался от утверждения только содержимым золотой коробки —
    а та же коробка стояла на 33 слайдах из 56 под утверждениями, и жанр
    «вопрос» перестал читаться вовсе."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title)
    bottom = BOTTOM - 0.46

    drawers = []
    for kind, b in blocks:
        if kind == "quote":
            scene, question, found = split_question(b)
            if not found:
                # Вопроса в блоке нет — значит это подводка, и форму ей даёт
                # обычная грамматика, а не жанр слайда.
                d = block_drawer(kind, b, sid, pattern)
                if d:
                    drawers.append(d)
                continue
            if scene:
                drawers.append(lambda sl, y, mh, s_=scene: K.form_speech(
                    sl, LEFT, y, WIDTH, s_, max_h=mh, label=f"{sid} сцена"))
            if question:
                drawers.append(lambda sl, y, mh, q=question: K.form_question(
                    sl, LEFT, y, WIDTH, q, max_h=mh, label=f"{sid} вопрос"))
        elif kind == "cards":
            drawers.append(lambda sl, y, mh, c=b: K.option_row(
                sl, LEFT, y, WIDTH, c, highlight_idx=None, max_h=min(mh or 1.8, 1.8),
                label=f"{sid} варианты"))
        else:
            d = block_drawer(kind, b, sid, pattern)
            if d:
                drawers.append(d)
    compose(sl, sid, y0, drawers, bottom=bottom)
    K.footer_note(sl, "разбор — на следующем слайде", y=bottom + 0.12, align=PP_ALIGN.CENTER)
    K.slide_id_mark(sl, sid)


# Таблица оси возвращается пять раз за занятие. Колонки ей задаются явно:
# иначе ширины пересчитываются по содержимому каждого возврата, и «та же
# таблица, которую занятие открывало пустой» выглядит каждый раз другой.
AXIS_COLS = (0.13, 0.27, 0.27, 0.33)


def g_axis_table(sl, sid, title, blocks, pattern, assertion=""):
    """Ось занятия и её возвраты. Светлый фон, таблица-коробка; незаполненные
    ячейки — пунктирные слоты, а не пустые клетки сетки.

    Прежде эта таблица была настоящей таблицей PPTX с зеброй и синей шапкой,
    положенной прямо на тёмно-синее поле, — и читалась как вставленный из
    другого документа скриншот; пустые ячейки читались как недоделанный слайд."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title)
    drawers = []
    for kind, b in blocks:
        if kind == "table" and len(b[0]) == len(AXIS_COLS):
            inner = WIDTH - 0.4
            cols = [c * inner for c in AXIS_COLS]
            drawers.append(lambda sl, y, mh, h_=b[0], r_=b[1], c=cols: K.table_card(
                sl, LEFT, y, WIDTH, h_, r_, col_w=c, max_h=mh, label=f"{sid} ось"))
            continue
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_id_mark(sl, sid)


def g_criteria(sl, sid, title, blocks, pattern, assertion=""):
    """«Ещё рано» и «не нужно вообще» — два РАЗНЫХ вопроса, и выглядеть они
    обязаны по-разному. Две таблицы подряд становятся двумя плашками-критериями
    бок о бок; одна таблица — плашкой на две колонки.

    Прежде здесь стояли две одинаковые сетки друг над другом, отличавшиеся
    только заголовком первой колонки, — самый буквальный «сплошные таблицы
    странные» в деке."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title)
    tables = [b for k, b in blocks if k == "table"]
    others = [(k, b) for k, b in blocks if k != "table"]

    drawers = []
    for kind, b in others:
        if kind == "quote":
            drawers.append(block_drawer(kind, b, sid, pattern))

    if len(tables) == 1 and len(tables[0][0]) == 2:
        # одна таблица «рано | не нужно» — две плашки бок о бок
        headers, rows = tables[0]
        left = [r[0] for r in rows if len(r) > 0 and r[0].strip() and r[0].strip() != "—"]
        right = [r[1] for r in rows if len(r) > 1 and r[1].strip() and r[1].strip() != "—"]
        gap, cw = 0.3, (WIDTH - 0.3) / 2

        def pair(sl, y, mh, h_=headers, l_=left, r_=right, cw=cw, gap=gap):
            # плашки выравниваются по высоте: две колонки одного сравнения с
            # разными низами читаются как недовёрстанные
            tall = max(measure(lambda s2, yy, m2, it=it, t=t, a=a: K.criterion_plate(
                           s2, LEFT, yy, cw, t, it, max_h=m2, accent=a), y, mh)
                       for t, it, a in ((h_[0], l_, K.SLATE), (h_[1], r_, K.GOLD_DARK)))
            K.criterion_plate(sl, LEFT, y, cw, h_[0], l_, max_h=mh, min_h=tall,
                              accent=K.SLATE, label=f"{sid} рано")
            K.criterion_plate(sl, LEFT + cw + gap, y, cw, h_[1], r_, max_h=mh, min_h=tall,
                              accent=K.GOLD_DARK, label=f"{sid} не нужно")
            return tall
        drawers.append(pair)
    else:
        # «ещё рано» — вопрос про МОМЕНТ (тиловая, нейтральная);
        # «не нужно вообще» — вопрос про ЗАДАЧУ (золотая, это граница)
        accents = [None, K.GOLD_DARK, K.MID]
        for i, (headers, rows) in enumerate(tables):
            drawers.append(lambda sl, y, mh, h_=headers, r_=rows, a=accents[min(i, 2)]:
                           K.table_card(sl, LEFT, y, WIDTH, h_, r_, max_h=mh, accent=a,
                                        label=f"{sid} критерии"))

    for kind, b in others:
        if kind in ("bullets", "code", "cards", "para"):
            drawers.append(block_drawer(kind, b, sid, pattern))
    compose(sl, sid, y0, drawers)
    K.slide_id_mark(sl, sid)


def g_closing(sl, sid, title, blocks, pattern, assertion=""):
    """Закрытие — возврат к вопросу открытия и перенос на свой репозиторий.
    Золотая коробка с вопросом получает вес, остальное — спокойная сводка под
    ней. Схема, если она у слайда есть, встаёт СРАЗУ ПОД вопросом: здесь вопрос
    задаёт рамку, а схема показывает, во что раскладывается ответ, — поэтому
    порядок обратный тому, что на содержательном слайде (`g_content`)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title)
    drawers = []
    first = True
    for kind, b in blocks:
        if kind == "quote" and first:
            first = False
            drawers.append(lambda sl, y, mh, q=b: K.form_question(
                sl, LEFT, y, WIDTH, q, size=15.5, max_h=mh,
                label=f"{sid} вопрос открытия"))
            fig = figure_for(sid)
            if fig:
                drawers.append(lambda sl, y, mh, p=fig: K.figure(
                    sl, p, LEFT, y, WIDTH, mh if mh else 3.2))
            continue
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_id_mark(sl, sid)


def g_content(sl, sid, title, blocks, pattern, assertion=""):
    """Содержательный слайд: надзаголовок, заголовок-утверждение с кеглем по
    длине, схема (если есть) и блоки в порядке источника — каждый своим
    приёмом, все по измеренной высоте."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title)
    drawers = []
    fig = figure_for(sid)
    if fig:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, LEFT, y, WIDTH, mh if mh else 4.3))
    for kind, b in blocks:
        if kind == "table" and pattern == "evidence_table_with_gap":
            # таблица свидетельств — свой акцент: «разбор» подсвечивает целевую
            # строку золотом, «свидетельства» ничего не выбирают, они взвешивают
            drawers.append(lambda sl, y, mh, h_=b[0], r_=b[1]: K.table_card(
                sl, LEFT, y, WIDTH, h_, r_, max_h=mh, accent=K.MID, highlight={},
                label=f"{sid} свидетельства"))
            continue
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_id_mark(sl, sid)


# Ярлыки дорожек по умолчанию. Заголовок слайда фиксирован приёмом («Что это
# за штука и зачем она»), ярлыки — нет: их берёт шапка таблицы из исходника,
# если автор её заполнил. Рекомендованная шапка — ровно `| База | Кромка |`,
# чтобы все шесть Тактов Б выглядели одним и тем же слайдом.
TRACK_LABELS = ("база", "кромка")


def g_base_edge(sl, sid, title, blocks, pattern, assertion=""):
    """Такт Б — база и кромка на одном экране, 45 секунд, ничего не решается.

    Два сигнала жанра, направленные в сторону, обратную слайду-вопроса:
    надзаголовок «· БАЗА» СЕРЫМ (самый тихий ярлык в деке — на этом слайде
    нечего решать, и это сказано цветом) и две равные дорожки вместо коробок.
    Сильный опознаёт слайд по шапке и знает, что следующие три четверти минуты
    можно слушать вполуха; слабый получает термины напечатанными.

    Третьим сигналом была серая подпись внизу «здесь ничего не решается» —
    снята по решению владельца: надзаголовка и формы хватает.

    Источник дорожек — ТАБЛИЦА ИЗ ДВУХ КОЛОНОК в `## Visual` (первая колонка —
    база, вторая — кромка). Это не прихоть разметки: разбор `.md` живёт в
    `slide_parts.py`, который этой сессии трогать нельзя, а таблицу он уже
    умеет — значит приём обязан встать на то, что парсер отдаёт сегодня, без
    новой разметки и без правки чужого файла.
    """
    left, right, labels, terms, rest = [], [], TRACK_LABELS, [], []
    for kind, b in blocks:
        if kind == "table" and not left and not right:
            headers, rows = b
            if headers and len(headers) >= 2 and any(K.plain(h).strip() for h in headers):
                labels = (K.plain(headers[0]).strip() or TRACK_LABELS[0],
                          K.plain(headers[1]).strip() or TRACK_LABELS[1])
            for r in rows:
                if len(r) > 0 and r[0].strip():
                    left.append(r[0].strip())
                if len(r) > 1 and r[1].strip():
                    right.append(r[1].strip())
            continue
        if kind == "cards" and not terms:
            terms = b
            continue
        rest.append((kind, b))

    if not (left and right):
        # Двух дорожек нет — это не Такт Б. Лучше показать слайд обычной
        # раскладкой, чем нарисовать половину приёма и молчать об этом.
        M._WARNINGS.append(f"ПРИЁМ [{sid} base_and_edge]: в «## Visual» нет таблицы "
                           f"из двух колонок — слайд собран обычной раскладкой")
        return g_content(sl, sid, title, blocks, pattern, assertion)

    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, label_for(sid, pattern), title, tag_color=K.SLATE)
    bottom = BOTTOM - 0.46

    drawers = [lambda sl, y, mh: K.base_edge_tracks(
        sl, LEFT, y, WIDTH, left, right, left_label=labels[0], right_label=labels[1],
        terms=terms, max_h=mh, label=f"{sid} дорожки")]
    for kind, b in rest:
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    # Серой подписи «здесь ничего не решается» здесь больше нет: снята по
    # решению владельца. Жанр опознаётся надзаголовком «· БАЗА» и самой формой
    # из двух дорожек — третий сигнал оказался лишним.
    compose(sl, sid, y0, drawers, bottom=bottom, center=1.0)
    K.slide_id_mark(sl, sid)


GENRE_FN = {
    "section_divider_macro": g_divider,
    "base_and_edge": g_base_edge,
    "hero_cover": g_cover,
    "question_with_option_cards": g_question,
    "question_repeat": g_question,
    "transfer_exercise": g_closing,
    "keystone_scope_map": g_axis_table,
    "recap_table": g_axis_table,
    "criteria_checklist_and_boundary": g_criteria,
    "closing_question_partial": g_closing,
}


# ── Сборка ──────────────────────────────────────────────────────────────────

def deck_from_files(prefix):
    """Список слайдов блока, собранный ИЗ САМИХ ФАЙЛОВ, минуя `deck.yaml`.

    Пока блоки новой деки пишутся параллельными сессиями, `deck.yaml` ещё
    перечисляет старые 50 слайдов — и блок, которого в нём нет, собрать было
    нечем вовсе. Поэтому смотреть на свою работу сессия блока не могла и
    сверяла текст собранного файла с исходником вместо того, чтобы открыть
    картинку. Здесь `id` и `visual.pattern` читаются из фронтматтера слайда —
    тех же полей, что потом окажутся в `deck.yaml`.

    Это режим ПРЕДПРОСМОТРА БЛОКА, а не вторая дека: порядок — по `id`,
    `deck.yaml` остаётся единственным источником правды для настоящей сборки.
    """
    out = []
    for f in sorted((ROOT / "slides").glob(f"{prefix}*.md")):
        md = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
        fm = (yaml.safe_load(m.group(1)) if m else {}) or {}
        out.append({"id": fm.get("id") or f.name.split("-")[0],
                    "file": f"slides/{f.name}",
                    "visual": fm.get("visual") or {}})
    return sorted(out, key=lambda s: s["id"])


def main():
    argv = list(sys.argv[1:])
    block = None
    if "--block" in argv:
        i = argv.index("--block")
        block = argv[i + 1] if i + 1 < len(argv) else "n"
        del argv[i:i + 2]

    if block:
        slides = deck_from_files(block)
        out_name = f"sem-05-{block}.pptx"
        if not slides:
            print(f"слайдов по образцу «{block}*.md» не найдено")
            return
    else:
        slides = yaml.safe_load((ROOT / "deck.yaml").read_text(encoding="utf-8"))["slides"]
        out_name = "sem-05.pptx"
    deck = {"slides": slides}
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(K.W_IN), Inches(K.H_IN)
    blank = prs.slide_layouts[6]
    M.reset()

    only = set(argv)
    built = 0
    for s in deck["slides"]:
        sid = s["id"]
        pattern = (s.get("visual") or {}).get("pattern", "")
        md = (ROOT / s["file"]).read_text(encoding="utf-8")
        title, _assertion, visual, notes = SP.sections(md)
        sl = prs.slides.add_slide(blank)
        if not only or sid in only:
            GENRE_FN.get(pattern, g_content)(sl, sid, title or sid, SP.blocks(visual),
                                             pattern, _assertion)
        if notes:
            sl.notes_slide.notes_text_frame.text = notes
        built += 1

    out = HERE / out_name
    prs.save(out)
    warns = M.report()
    for w in warns:
        print("•", w)
    print(f"\nслайдов: {built}   предупреждений: {len(warns)}   "
          f"файл: {out.name} ({out.stat().st_size // 1024} КБ)")


if __name__ == "__main__":
    main()
