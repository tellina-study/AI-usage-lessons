#!/usr/bin/env python3
"""Сборка деки Семинара 7 из source-of-truth: ../deck.yaml + ../slides/nNN-*.md

Устройство — ПО ОБРАЗЦУ `sem-06/rendered/build_sem06.py` (которое само —
по образцу `sem-05`), не копия: Семинар 7 не тащит ничего из старой нумерации
и ничего EN (ещё нет английского трека на момент этой сборки). Три правила
библиотеки приёмов те же (`tools/presentation-build/seminar-deck-kit.md`,
`tools/seminar-production/README.md` §7-8), и держит их тот же код
`deck_kit.py`/`metrics.py`/`slide_parts.py`, взятый из Семинара 6 БЕЗ
ИЗМЕНЕНИЙ (три файла — чистая библиотека приёмов вёрстки, ни одной строки в
них не привязано к содержанию конкретного занятия).

Жанровые функции (`g_divider`, `g_cover`, `g_question`, `g_axis_table`,
`g_criteria`, `g_content`) и сборочные аудиты (`audit_numbering`, `audit_figs`,
`audit_question_answer`, …) перенесены из `build_sem06.py` почти буквально —
их логика не привязана к содержанию Семинара 6, только к СЛОВАРЮ ПРИЁМОВ.
`g_base_edge` (`base_and_edge`) перенесена тоже, хотя в деке Семинара 7 этот
приём не использован ни на одном слайде — на будущее, тем же рассуждением,
что у `audit_figs`/`audit_figure_text` в Семинаре 6 (код, готовый сработать,
как только приём понадобится, лучше, чем код, который надо будет писать с
нуля).

## Решения по НОВЫМ именам `visual.pattern` этой деки (задание Фазы 5, ENFORCED
## «решение по каждому новому имени — документировать»)

Список `visual.pattern`, использованных в 34 файлах `slides/n*.md`, шире
словаря Семинара 6 (18 имён) — в сем-07 их 23 уникальных. Из них 14 — ПРЯМО
совпадают с именами Семинара 6 (`hero_cover`, `recap_table`,
`section_divider_macro`, `question_with_option_cards`, `reflection_question`,
`criteria_checklist_and_boundary`, `answer_breakdown_table`,
`failure_vignette`, `failure_vignette_table`, `problem_scenario`,
`base_and_edge` — не используется, но имя то же) — переносятся без единой
правки. Оставшиеся 9 — НОВЫЕ. Решение по каждому:

* **`case_divider_quote`** (n04, n12, n16) — НОВАЯ ЖАНРОВАЯ ФУНКЦИЯ
  `g_case_divider` (см. ниже). По сути это младший брат `section_divider_macro`
  (тот же тёмный градиент, та же крупная реплика), но на уровень НИЖЕ: это
  дивайдер КЕЙСА внутри ступени, а не дивайдер ступени/блока — без золотого
  номерного значка и без дорожной карты БЛОКОВ занятия. Внизу вместо неё —
  дорожка ТРЁХ КЕЙСОВ текущей ступени (А·Б·В), реализована прямым повторным
  вызовом уже существующего `K.roadmap()` (ни одной новой примитивной функции
  в `deck_kit.py` не потребовалось — только новый жанровый сборщик уровня
  `build_sem07.py`, как и положено по контракту «кит не меняем»).
* **`section_divider_macro`** у n19/n25/n29 (ИСПРАВЛЕНО Фикс-кругом, см. ниже)
  — это были ТРИ дивайдера кейсов А/Б/В ступени 2, а не дивайдеры блоков.
  Автор раздела 2 использовал то же имя приёма, что в Семинаре 6 был
  зарезервирован под дивайдер БЛОКА, для всех трёх своих дивайдеров кейсов —
  асимметрия с разделом 1 (который для своих трёх дивайдеров кейсов взял
  `case_divider_quote`) объясняется тем, что два раздела писались
  параллельными сессиями (`rework/section-1-chaining.md` и
  `rework/section-2-routing.md`), не общим словарём с самого начала. Фаза 5
  изначально приняла имя буквально (смаппила на `g_divider`, как в
  Семинаре 6) и назвала результат вслух как находку — ступень 2 выглядела
  «тяжелее» ступени 1 на трёх переходах между кейсами (полный дивайдер
  раздела: прогресс-бар блоков, золотой номерной значок, дорожка ДВУХ
  ступеней — вместо лёгкого дивайдера кейса). **Фикс-круг (эта правка)**
  устранил асимметрию: поле `visual.pattern` в n19/n25/n29 изменено на
  `case_divider_quote` — они теперь идут через `g_case_divider`, ту же
  функцию, что и их зеркальные пары ступени 1 (n04/n12/n16). Текст полей
  `visual.primary`/`visual.backup` в этих трёх файлах менять не пришлось:
  автор раздела 2 уже ОПИСЫВАЛ рендер лёгкого дивайдера кейса («дорожка трёх
  кейсов ступени, кейс X подсвечен») — ошибка была только в имени паттерна,
  не в описании визуала. `CASE_IDX` уже содержал верные индексы для всех
  шести слайдов (n04/n12/n16/n19/n25/n29) — его трогать не потребовалось.
  Попутно этим же Фикс-кругом исправлена ловушка в самой `g_case_divider`:
  накопление «лишней» строки цитаты (`extra`) было устроено как перезапись
  переменной на каждой физической строке блока-цитаты, а не как накопление
  — многострочный (3 физические строки без пустой строки между ними) второй
  абзац цитаты n29 терялся бы на 2/3, если бы просто сменить имя паттерна
  без этой правки build-слоя (см. `g_case_divider` ниже — `extra_parts`
  вместо одиночной перезаписываемой `extra`).
* **`guess_the_number`** (n31) — синоним `reflection_question`/
  `question_with_option_cards` по РОЛИ (вопрос залу золотой коробкой), отличие
  только в том, что карточек-вариантов на слайде нет вовсе (зал называет
  число устно). Смапплено на СУЩЕСТВУЮЩУЮ функцию `g_question` — она уже умеет
  рисовать блок-цитату без карточек (у n31 в `## Visual` ровно один блок-
  цитата, кончающийся на «?», и `g_question` отрисует его целиком золотой
  коробкой через `split_question`/`form_question`, ничего кроме).
* **`scene_diagram_and_reveal`** (n03), **`scene_cards_and_question`** (n05),
  **`taxonomy_compare_table`** (n07), **`mechanism_pipeline`** (n08),
  **`code_block_with_callouts`** (n09), **`scene_mechanism`**/
  **`scene_mechanism_diagram`** (n13), **`verdict_numbers`**/
  **`verdict_numbers_table`** (n14), **`cost_reversibility_spectrum`** (n15),
  **`before_after_comparison`** (n17), **`synthesis_and_bridge`** (n18),
  **`case_bridge_statement`** (n24) — ни одна не меняет композицию слайда
  настолько, чтобы заслуживать отдельную жанровую функцию: у каждой на экране
  либо таблица (сравнение, механика, вердикт, спектр-как-таблица), либо код,
  либо цепочка блоков-цитат, которые уже умеет различать общий механизм ролей
  (`quote_role`/`para_role`, тот же, что в Семинаре 6). Все десять падают в
  `g_content` по умолчанию — РОВНО тем же рассуждением, каким в Семинаре 6 в
  него падали `problem_scenario`/`code_artifact`/`mechanics_table`/
  `evidence_table_with_gap`/… (см. докстринг `g_content` там). Два места
  всё же потребовали точечной правки САМОГО `g_content`/`block_drawer` (не
  новой функции):
    - **таблица-вариант без второй колонки** (`| Вариант | |`, n03 и n05) —
      новая ветка в `block_drawer`: двухколоночная таблица с пустым заголовком
      второй колонки и header[0] «вариант» рисуется КАРТОЧКАМИ-ВАРИАНТАМИ
      (`K.option_row`), а не таблицей с пустыми пунктирными слотами во всю
      высоту строки; если в одной из строк вторая колонка НЕ пуста (у n03 —
      «← верный ответ» на строке «нигде») — та карточка подсвечивается как
      выбранный/верный вариант (`highlight_idx`), это и есть reveal без
      отдельного цикла голосования, который `n03` само объявляет в
      `learning_goal`.
    - **`verdict_numbers_table`** (n14) — таблица цифр получает цветной акцент
      (`accent=K.GOLD_DARK`), той же техникой, что `evidence_table_with_gap` в
      Семинаре 6 получает `accent=K.MID`: один `if pattern == …` в
      `g_content`, не новая функция.
* **`failure_vignette_before_after`** (n10) — то же самое, что
  `failure_vignette` Семинара 6 (которое уже падает в `g_content`), только с
  более точным именем (у n10 действительно есть сравнение «что было бы
  правильно / что сломалось», а не только провал). Роль ведущей цитаты —
  `formula`, добавлена в `PATTERN_ROLE` рядом с `failure_vignette`, один в один.

Границы разделов Семинара 7 (`SVODKA-SLAIDOV.md`, дублируется статически
здесь — см. комментарий у `SECTIONS` ниже про то, почему без динамического
вывода по якорям):

    n01–n03   Мостик      (обложка + ось-пустая + открытие без ИИ)
    n04–n18   Ступень 1   (3 кейса: A механика / B Zillow / C Octomind)
    n19–n33   Ступень 2   (3 кейса: A механика / B Optum / C IRS)
    n34       Ось         (та же лестница, три нижние строки закрыты)

Схемы (`make_figures*.py`) эта сборка не рисует — фаза схем для Семинара 7 не
начата (ни один слайд не объявляет `visual.figure`), `FIGS` пуст.
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

SLIDES_DIR = {"ru": "slides"}
DECK_FILE = {"ru": "deck.yaml"}
OUT_NAME = {"ru": "sem-07.pptx"}

TOP, BOTTOM = 0.34, 6.92        # рабочее поле по вертикали
LEFT, WIDTH = 0.55, 12.23       # и по горизонтали
GAP = 0.18                      # шаг между блоками

# ── Где мы: границы разделов и ступень дорожной карты ───────────────────────
#
# В отличие от Семинара 6 (деку которого писали параллельные сессии, и номера
# слайдов могли сдвинуться в процессе), Семинар 7 на момент этой сборки —
# ЗАКОНЧЕННЫЙ, зафиксированный набор из 34 файлов (Фазы 1-4 пройдены и
# проверены оркестратором — см. задание Фазы 5). Динамический вывод границ по
# опорным приёмам (`_anchor_sections` в build_sem06.py), заведённый именно под
# риск параллельного дописывания, здесь — сложность без причины: границы
# заданы статически, той же парой чисел, что и в `ARCHITECTURE.md` §2/§6.
# Если Семинар 7 будет дописываться дальше (доп. кейсы, доп. ступени) — эту
# таблицу поправит тот, кто формирует НОВУЮ разметку, а не вывод по якорям.
BLOCKS = {"ru": ("Мостик", "Ступень 1", "Ступень 2", "Ось")}


def blocks_names():
    return BLOCKS[LANG]


SECTIONS_BY_PREFIX = {
    "n": ([(1, 3, "Мостик", None), (4, 18, "Ступень 1", 0), (19, 33, "Ступень 2", 1),
           (34, 34, "Ось", None)],
          ["Ступень 1", "Ступень 2"]),
}
SECTIONS, STAGES = SECTIONS_BY_PREFIX["n"]

# Дорожка кейсов на лёгком дивайдере (`case_divider_quote`, `g_case_divider`)
# и порядковый кейс для НЕ-лёгких дивайдеров той же работы, использующих
# `section_divider_macro` (см. докстринг модуля — решение по n19/n25/n29).
# Индекс 0/1/2 = кейс А/Б/В ТЕКУЩЕЙ ступени (сбрасывается на каждой ступени —
# это дорожка кейсов ступени, а не сквозной счётчик по всей деке).
CASE_IDX = {"n04": 0, "n12": 1, "n16": 2, "n19": 0, "n25": 1, "n29": 2}


def divider_index(sid):
    """Порядковый номер РАЗДЕЛЬНОГО дивайдера (`section_divider_macro`) в
    деке, считая с единицы; 0 — не такой дивайдер. Тот же счётчик, что в
    Семинаре 6 — считает только `section_divider_macro`, НЕ `case_divider_
    quote` (у лёгких дивайдеров кейса номерного значка нет вовсе, см.
    `g_case_divider`)."""
    div = [s["id"] for s in _deck_slides(sid[0])
           if (s.get("visual") or {}).get("pattern") == "section_divider_macro"]
    return div.index(sid) + 1 if sid in div else 0


def badge_for(sid):
    n = divider_index(sid)
    return n or None


def tag_for(sid, visual_meta):
    """Ярлык развилки — на этой деке НЕ используется ни на одном слайде
    (правило А6, то же решение, что в Семинаре 6: ярлык с минутами — лишнее).
    Если он всё же появится в чьём-то фронтматтере — предупреждение, не тихое
    игнорирование."""
    tag = (visual_meta or {}).get("tag")
    if tag:
        M._WARNINGS.append(
            f"ЯРЛЫК НА РАЗВИЛКЕ [{sid}]: `tag: {tag}` — на этой деке ярлыков на "
            f"развилках нет ни на одной (правило А6); уберите строку `tag:`")
    return tag


FIGS = {}

_NUM = re.compile(r"^[a-zA-Z]*(\d+)([a-zA-Z]*)$")


def num(sid):
    m = _NUM.match(sid)
    if not m:
        M._WARNINGS.append(f"ИМЯ СЛАЙДА [{sid}]: из идентификатора не читается "
                           f"номер — слайд попадёт в конец и без раздела")
        return 10 ** 6
    return int(m.group(1))


def _deck_slides(prefix):
    try:
        sl = yaml.safe_load(
            (ROOT / DECK_FILE[LANG]).read_text(encoding="utf-8"))["slides"]
        if sl and sl[0]["id"][0] == prefix:
            return sl
    except Exception:
        pass
    return deck_from_files(prefix)


def sections_for(sid):
    return SECTIONS_BY_PREFIX.get(sid[0], (SECTIONS, STAGES))


def slide_number(sid):
    ids = [s["id"] for s in _deck_slides(sid[0])]
    return ids.index(sid) + 1 if sid in ids else None


def where(sid):
    n = num(sid)
    for lo, hi, name, stage in sections_for(sid)[0]:
        if lo <= n <= hi:
            return name, stage
    return "", None


def slide_figure(sid):
    for s in _deck_slides(sid[0]):
        if s["id"] == sid:
            return (s.get("visual") or {}).get("figure")
    return None


def figure_for(sid):
    fn = slide_figure(sid) or FIGS.get(sid)
    if not fn:
        return None
    path = FIGDIR / fn
    return path if path.exists() else None


def draws_figure(pattern):
    return GENRE_FN.get(pattern, g_content) in (g_content, g_cover)


ANSWER_KINDS = {"table", "code", "bullets"}
ANSWER_ROLES = {"formula", "fact", "caveat"}


# Дивайдеры (оба уровня) — другая грамматика, не «вопрос залу → разбор
# рядом»: риторический вопрос/реплика в заголовке и формула-смысл под ней —
# это ПЕРЕХОД, а не голосование с ответом в одном кадре (см. n29:
# «Как число, в котором расы вообще нет, даёт результат, разный по расе?» —
# это название кейса, а следующий блок — почему это стоит спросить второй
# раз, не «правильный ответ»). Без исключения аудит давал ложное срабатывание
# на КАЖДОМ дивайдере, чей заголовок случайно кончается на «?».
DIVIDER_PATTERNS = {"section_divider_macro", "case_divider_quote"}


def audit_question_answer(sid, pattern, blocks):
    if pattern in DIVIDER_PATTERNS:
        return
    qi = None
    for i, (kind, b) in enumerate(blocks):
        if kind != "quote":
            continue
        if quote_role(b, pattern) == "question" or (
                pattern in ("question_with_option_cards", "guess_the_number")
                and split_question(b)[2]):
            qi = i
            break
    if qi is None:
        return
    for kind, b in blocks[qi + 1:]:
        role = quote_role(b, pattern) if kind == "quote" else None
        if kind in ANSWER_KINDS or role in ANSWER_ROLES:
            what = {"table": "таблица", "code": "технический блок",
                    "bullets": "список"}.get(kind, f"блок-{role}")
            M._WARNINGS.append(
                f"ОТВЕТ РЯДОМ С ВОПРОСОМ [{sid}]: под вопросом к залу стоит "
                f"{what} — зал прочтёт ответ раньше, чем откроет рот. "
                f"Ответ переносится на СЛЕДУЮЩИЙ слайд, а не ниже и не мельче")
            return


def audit_numbering(slides):
    ids = [s["id"] for s in slides]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        M._WARNINGS.append(
            f"НОМЕР ДВАЖДЫ [{', '.join(dup)}]: идентификатор стоит в деке "
            f"больше одного раза — слайды получат один и тот же номер")
    off = []
    for pos, sid in enumerate(ids, 1):
        got = slide_number(sid)
        if got is None:
            M._WARNINGS.append(
                f"НОМЕРА НЕТ [{sid}]: слайд есть в деке, а порядкового номера "
                f"у него не вышло — в углу будет пусто")
        elif got != pos:
            off.append(f"{sid}: напечатано {got}, порядок {pos}, сдвиг {got - pos:+d}")
    if off:
        M._WARNINGS.append(
            f"НОМЕР НЕ ПО ПОРЯДКУ ({len(off)} из {len(ids)}): " + "; ".join(off[:6])
            + ("…" if len(off) > 6 else "")
            + " — номер обязан выводиться из порядка слайда в deck.yaml")


def audit_crossrefs(slides):
    known = {s["id"] for s in slides}
    bad = []
    for s in slides:
        meta = s.get("visual") or {}
        text = " ".join(str(meta.get(k, "")) for k in ("primary", "backup", "tag"))
        for ref in sorted(set(re.findall(r"\bn[0-9]{2}[a-z]?\b", text))):
            if ref not in known:
                bad.append(f"{s['id']} → {ref}")
    if bad:
        M._WARNINGS.append(
            f"ССЫЛКА В НИКУДА ({len(bad)}): " + "; ".join(bad[:8])
            + ("…" if len(bad) > 8 else "")
            + " — служебное поле ссылается на слайд, которого в деке нет")


def audit_figs(slides):
    by_id = {s["id"]: s for s in slides}
    for sid, slide in by_id.items():
        meta = slide.get("visual") or {}
        fn = meta.get("figure")
        if fn and sid in FIGS:
            M._WARNINGS.append(
                f"СХЕМА ДВАЖДЫ [{sid}]: объявлена и слайдом («{fn}»), и таблицей "
                f"FIGS («{FIGS[sid]}») — уберите запись из таблицы, слайд главнее")
        if not fn:
            continue
        if not (FIGDIR / fn).exists():
            M._WARNINGS.append(f"НЕТ СХЕМЫ [{sid}]: слайд объявляет «{fn}», файла нет "
                               f"— слайд соберётся без иллюстрации")
        if not draws_figure(meta.get("pattern", "")):
            M._WARNINGS.append(
                f"СХЕМА НЕ ДОЙДЁТ [{sid}]: слайд объявляет «{fn}», но приём "
                f"«{meta.get('pattern','')}» схему не рисует — не сработает никогда")
    for sid, fn in sorted(FIGS.items()):
        if sid not in by_id:
            M._WARNINGS.append(f"МЁРТВАЯ ЗАПИСЬ FIGS [{sid}]: «{fn}» — такого "
                               f"слайда в деке нет")


def audit_figure_text():
    import ast
    c = K.Claims()
    for f in sorted(HERE.glob("make_figures*.py")):
        try:
            tree = ast.parse(f.read_text(encoding="utf-8"))
        except Exception as e:
            M._WARNINGS.append(f"ГЕНЕРАТОР СХЕМ [{f.name}]: не разбирается — {e}")
            continue
        docs = {d for n in ast.walk(tree)
                if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef,
                                  ast.AsyncFunctionDef))
                for d in [ast.get_docstring(n, clean=False)] if d}
        for n in ast.walk(tree):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) \
                    and n.value not in docs:
                c.label(n.value, f"{f.name}:{n.lineno}")
    M._WARNINGS.extend(c.report())


_scratch = Presentation()
_scratch.slide_width, _scratch.slide_height = Inches(K.W_IN), Inches(K.H_IN)


def measure(fn, *a, **kw):
    sl = _scratch.slides.add_slide(_scratch.slide_layouts[6])
    saved = list(M._WARNINGS)
    h = fn(sl, *a, **kw)
    M._WARNINGS[:] = saved
    return h


# ── Роль блока-цитаты/абзаца по умолчанию ───────────────────────────────────
#
# Ключи — `visual.pattern`, НЕ `type` (то же разделение полей, что в Семинаре
# 6 — см. докстринг модуля выше). Таблица сверена со СЛОВАРЁМ, фактически
# использованным в 34 написанных слайдах (23 уникальных имени pattern).
PATTERN_ROLE = {
    "question_with_option_cards": "question",
    "reflection_question": "question",
    "guess_the_number": "question",
    "answer_breakdown_table": "formula",
    "failure_vignette": "formula",
    "failure_vignette_table": "formula",
    "failure_vignette_before_after": "formula",
    "criteria_checklist_and_boundary": "formula",
    "base_and_edge": "fact",
    "recap_table": "fact",
}

LANG_SIGNALS = {
    "ru": {
        "open": ("«",),
        "pairs": (("«", "»"), ("**", "**")),
        "ask": r"выберите|что бы вы|как бы вы|назовите|подумайте|не выбирайте",
        "caveat_open": r"^\W*(оговорка|честный пробел|честно про|честно о\b)",
        "caveat": (r"не проверен|не провер[её]н|не измер|нет данных|не подтвер|"
                   r"не удалось|честного пробела|честный пробел|нечестн"),
    },
}
LANG = "ru"
SPEECH_OPEN = ASK = CAVEAT_OPEN = CAVEAT = None


def set_lang(lang):
    global LANG, SPEECH_OPEN, ASK, CAVEAT_OPEN, CAVEAT, _WRAP_PAIRS
    if lang not in LANG_SIGNALS:
        raise SystemExit(f"--lang принимает {'/'.join(LANG_SIGNALS)}, передано «{lang}»")
    cfg = LANG_SIGNALS[lang]
    LANG = lang
    SPEECH_OPEN = cfg["open"]
    _WRAP_PAIRS = cfg["pairs"]
    ASK = re.compile(cfg["ask"], re.I)
    CAVEAT_OPEN = re.compile(cfg["caveat_open"], re.I)
    CAVEAT = re.compile(cfg["caveat"], re.I)


def opens_speech(body):
    return body.lstrip().startswith(SPEECH_OPEN)


def quote_role(lines, pattern):
    body = " ".join(K.plain(l) for l in lines).strip()
    if body.rstrip("»\"' ").endswith("?") or ASK.search(body):
        return "question"
    if CAVEAT_OPEN.match(K.plain(body).lstrip("*> ")) or CAVEAT.search(body):
        return "caveat"
    base = PATTERN_ROLE.get(pattern)
    if base == "question":
        return "speech" if opens_speech(body) else "fact"
    if opens_speech(body):
        return "speech"
    return base or "formula"


FORM = {"question": K.form_question, "formula": K.form_formula,
        "speech": K.form_speech, "caveat": K.form_caveat, "fact": K.form_fact}

ITALIC_LINE = re.compile(r"^\s*\*([^*].*?)\*\s*$")


def para_role(text, pattern):
    m = ITALIC_LINE.match(text)
    if m:
        return "speech", m.group(1).strip()
    return quote_role([text], pattern), text


_WRAP_PAIRS = ()
set_lang("ru")


def split_question(lines):
    flat = " ".join(lines).strip()
    op, cl = "", ""
    for o, c in _WRAP_PAIRS:
        if not (flat.startswith(o) and flat.endswith(c) and len(flat) > len(o) + len(c)):
            continue
        if o == c and o in flat[len(o):len(flat) - len(c)]:
            continue
        op, cl = o, c
        break
    core = flat[len(op):len(flat) - len(cl)].strip() if op else flat

    bounds, pos = [], 0
    for m in re.finditer(r"[.!?…]+[»\"\')\s]*", core):
        bounds.append((pos, m.end()))
        pos = m.end()
    if pos < len(core):
        bounds.append((pos, len(core)))

    def rewrap(text):
        text = text.strip()
        return f"{op}{text}{cl}" if op and text else text

    for a, b in bounds:
        sent = core[a:b]
        if "?" in sent or ASK.search(sent):
            if a == 0:
                return [], [rewrap(core)], True
            return [rewrap(core[:a])], [rewrap(core[a:])], True
    return [], lines, False


def unseen(sid, pattern, blocks, handled, why):
    for kind, _b in blocks:
        if kind not in handled:
            M._WARNINGS.append(f"БЛОК НЕ ПОКАЗАН [{sid} · {pattern}]: блок вида "
                               f"«{kind}» — {why}")


# ── Одиночный курсив `*…*`, которого вёрстка не умеет ───────────────────────
#
# `metrics.fits()` уже ловит это и честно печатает предупреждение
# («РАЗМЕТКА … вёрстка не умеет — звёздочки выйдут на слайд как есть») — но
# только НАЗЫВАЕТ находку, не чинит её (см. комментарий в metrics.py: «молча
# срезать звёздочки нельзя — так прошлая версия теряла целевые ответы,
# помеченные жирным»; это предостережение про `**жирный**`, не про одиночный
# курсив). На этой деке одиночный курсив встретился в двух местах (n13, n18)
# — оба раза как разметка ВНУТРИ строки-диаграммы или цитаты с Anthropic, не
# как разметка текста, уже выделенного ЖИРНЫМ где-то рядом (`is_bold`
# работает на уровне целой строки, не части) — поэтому срезание звёздочек
# здесь безопасно: не задевает ни одну из `**bold**`/`` `mono` `` форм,
# которые несут смысл (целевой ответ, код).
#
# Решение — не трогать правила в `deck_kit.py`/`metrics.py` (эти два файла
# остаются байт-в-байт тем же китом, что в Семинаре 6 — см. докстринг
# модуля), а снять звёздочки ЗДЕСЬ, на входе в сборку, тем же регулярным
# выражением, что `metrics._ITALIC` использует для обнаружения (скопировано
# для согласованности находки и починки, не переопределено заново). Текст
# внутри круглых скобок остаётся на экране («независимого гейта нет»,
# «Building Effective Agents») — теряется только курсивное начертание,
# не содержание.
_LONE_ITALIC = re.compile(r"(?<![*\w])\*(?!\*)([^*\n]{2,}?)\*(?![*\w])")


def _degloss_italic(s):
    if not isinstance(s, str) or "*" not in s:
        return s
    return _LONE_ITALIC.sub(lambda m: m.group(1), s)


# ── Карточки-варианты, записанные НЕСКОЛЬКИМИ строками ──────────────────────
#
# `slide_parts.blocks()` опознаёт ряд карточек (`· ... · ...`) по строке
# исходника, у которой НА НЕЙ САМОЙ есть «·» и ≥4 бэктика (Семинар 6, та же
# проверка). На этой деке два слайда (n21, n27, оба — `question_with_option_
# cards`) записали те же четыре варианта В НЕСКОЛЬКО СТРОК ради читаемости
# исходника — находка Фазы 5, не предусмотренная словарём Семинара 6. У двух
# слайдов это ломается ДВУМЯ РАЗНЫМИ способами:
#
#   n21 — один вариант на строку (`` `вариант` · `` по одной паре бэктиков на
#   строку, 2 бэктика < порога 4): ни одна строка не зажигает триггер
#   `slide_parts` вовсе, все 4 строки просто копятся в буфер абзаца и
#   склеиваются ОДНИМ `para`-блоком на 4 сегмента.
#
#   n27 — по два варианта на строку (4 бэктика на строку, порог пройден):
#   `slide_parts.blocks()` зовёт `flush()` ПЕРЕД тем, как проверить «хватает
#   ли вариантов на единое голосование» (`len(items) >= 3`), и на 2 вариантах
#   строки это условие не проходит — но `flush()` уже случился. Для ДВУХ
#   таких строк подряд это рассекает один список на ДВА отдельных
#   `para`-блока по 2 сегмента в каждом, и порог «≥3» не набирается ни в
#   одном по отдельности.
#
# Починка — не правкой `slide_parts.py` (кит остаётся как есть), а повторным
# применением ТОГО ЖЕ признака (бэктики + «·») в build_sem07.py на ДВУХ
# уровнях: внутри одного `para`-блока (n21) и — если блок оказался «чистым
# фрагментом» карточек меньше порога — слиянием СОСЕДНИХ `para`-фрагментов
# подряд (n27), пока порог не наберётся или фрагменты не кончатся.
_CARD_SEG = re.compile(r"`([^`]+)`")


def _card_fragment(text):
    """Сегменты карточек в ОДНОМ `para`-блоке, если блок — ЧИСТЫЙ фрагмент
    списка (после вычитания `` `сегментов` `` остаются только «·» и
    пробелы), иначе `None`. Порог «минимум 3 варианта» здесь НЕ проверяется
    — он проверяется один раз, после слияния соседних фрагментов
    (`_merge_card_fragments`), иначе n27 (2+2) никогда бы не набрал его по
    отдельности. Без строгого условия «ничего кроме» обычный абзац со
    случайным кодовым словом в обратных кавычках (`call_classify`, `*.md`)
    прошёл бы тоже — там между сегментами всегда есть обычная проза."""
    if "`" not in text or "·" not in text:
        return None
    segs = _CARD_SEG.findall(text)
    rest = _CARD_SEG.sub("", text)
    if segs and re.fullmatch(r"[\s·]*", rest):
        return segs
    return None


def _merge_card_fragments(blocks):
    """Склеить подряд идущие `para`-фрагменты карточек (`_card_fragment`) в
    один блок `cards`, если суммарно они дают ≥3 варианта — порог, ниже
    которого это не голосование, а случайное совпадение разметки."""
    out, i = [], 0
    while i < len(blocks):
        kind, b = blocks[i]
        frag = _card_fragment(b) if kind == "para" else None
        if frag is not None:
            segs, j = list(frag), i + 1
            while j < len(blocks) and blocks[j][0] == "para":
                nxt = _card_fragment(blocks[j][1])
                if nxt is None:
                    break
                segs.extend(nxt)
                j += 1
            if len(segs) >= 3:
                out.append(("cards", segs))
                i = j
                continue
        out.append((kind, b))
        i += 1
    return out


def sanitize_blocks(blocks):
    """Снять одиночный курсив (`_degloss_italic`) из текста ВИДИМОГО СЛОЯ —
    `quote`/`para`/`bullets`/`table` — и распознать карточки-варианты,
    рассечённые построчным разбором на несколько `para` (`_merge_card_
    fragments`). `code`-блоки НЕ трогаются: внутри листинга `*` — часто
    настоящий знак (`*args`, глоб-шаблон), а не разметка курсива, и срезать
    его значило бы показать код, который автор не писал."""
    out = []
    for kind, b in blocks:
        if kind == "quote":
            out.append((kind, [_degloss_italic(l) for l in b]))
        elif kind == "para":
            out.append((kind, _degloss_italic(b)))
        elif kind == "bullets":
            items, numbered = (b, False) if isinstance(b, list) else b
            out.append((kind, ([_degloss_italic(i) for i in items], numbered)))
        elif kind == "table":
            headers, rows = b
            out.append((kind, ([_degloss_italic(h) for h in headers],
                               [[_degloss_italic(c) for c in r] for r in rows])))
        else:
            out.append((kind, b))
    return _merge_card_fragments(out)


# ── Отрисовка одного блока ──────────────────────────────────────────────────

def _is_variant_table(headers, rows):
    """Таблица-вариант без второй колонки (`| Вариант | |`) — НОВАЯ форма
    этой деки (n03, n05): автор написал список вариантов ответа markdown-
    таблицей из двух колонок, вторая пустая у всех строк кроме, может быть,
    одной (пометка верного ответа стрелкой/текстом). По сути это те же
    карточки-варианты, что `question_with_option_cards` рисует через
    `K.option_row` — только записанные в исходнике таблицей, не строкой
    `· ... · ...`. Разбирать её как таблицу значило бы рисовать пунктирные
    пустые слоты во всю высоту строки под каждой карточкой — технически
    верно, visуально шум. Здесь — распознавание формы, не новый приём."""
    if len(headers) != 2:
        return False
    return K.plain(headers[0]).strip().lower().startswith("вариант")


def block_drawer(kind, b, sid, pattern, *, role=None):
    if kind == "quote":
        r = role or quote_role(b, pattern)
        fn = FORM[r]
        return lambda sl, y, mh: fn(sl, LEFT, y, WIDTH, b, max_h=mh, label=f"{sid} {r}")
    if kind == "table":
        headers, rows = b
        if _is_variant_table(headers, rows):
            options = [r[0] for r in rows if r and r[0].strip()]
            hi = next((i for i, r in enumerate(rows)
                       if len(r) > 1 and r[1].strip()), None)
            return lambda sl, y, mh: K.option_row(
                sl, LEFT, y, WIDTH, options, highlight_idx=hi,
                max_h=min(mh or 1.8, 1.8), label=f"{sid} варианты")
        accent = K.GOLD_DARK if pattern == "verdict_numbers_table" else None
        return lambda sl, y, mh: K.table_card(sl, LEFT, y, WIDTH, headers, rows,
                                              max_h=mh, accent=accent,
                                              label=f"{sid} таблица")
    if kind == "code":
        lang, lines = b
        return lambda sl, y, mh: K.terminal_card(sl, LEFT, y, WIDTH, lines, max_h=mh,
                                                 markup=lang in ("markdown", "md"),
                                                 label=f"{sid} код")
    if kind == "cards":
        if pattern in ("question_with_option_cards", "guess_the_number"):
            return lambda sl, y, mh: K.option_row(sl, LEFT, y, WIDTH, b,
                                                  max_h=min(mh or 1.7, 1.7),
                                                  label=f"{sid} варианты")
        return lambda sl, y, mh: K.term_pills(sl, LEFT, y, WIDTH, b, label=f"{sid} термины")
    if kind == "bullets":
        items, numbered = (b, False) if isinstance(b, list) else b
        return lambda sl, y, mh: K.numbered_list(sl, LEFT, y, WIDTH, items, max_h=mh,
                                                 numbered=numbered,
                                                 label=f"{sid} список")
    if kind == "para":
        r, text = para_role(b, pattern)
        fn = FORM[role or r]
        return lambda sl, y, mh: fn(sl, LEFT, y, WIDTH, [text], max_h=mh,
                                    label=f"{sid} {role or r}")
    M._WARNINGS.append(f"БЛОК НЕ ПОКАЗАН [{sid} · {pattern}]: блок вида «{kind}» "
                       f"ни один приём не рисует — содержание пропало бы молча")
    return None


def compose(sl, sid, y0, drawers, *, bottom=BOTTOM, center=True):
    if not drawers:
        return
    avail = bottom - y0
    nat = [measure(d, y0, None) for d in drawers]
    total = sum(nat) + GAP * (len(nat) - 1)

    if total <= avail:
        slack = avail - total
        gap = GAP + min(slack / max(len(nat), 1), 0.55)
        used = sum(nat) + gap * (len(nat) - 1)
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

    end = y - GAP
    over = end - bottom
    if over > 0.02:
        if end > K.H_IN - 0.15:
            M._WARNINGS.append(
                f"ЗА КРАЕМ ПОЛОТНА [{sid}]: композиция кончается на {end:.2f}″ при "
                f"высоте полотна {K.H_IN:.2f}″ — нижний блок в PowerPoint не виден вовсе")
        else:
            M._WARNINGS.append(
                f"НЕ ПОМЕСТИЛОСЬ [{sid}]: композиция на {over:.2f}″ ниже рабочего поля — "
                f"блок заходит в поле подписи, номер слайда ляжет поверх него")


# ── Жанры слайдов ───────────────────────────────────────────────────────────

def g_divider(sl, sid, title, blocks, pattern, assertion="", meta=None):
    """Дивайдер уровня РАЗДЕЛА — градиент, золотая полоса, номерной значок,
    смысловая строка, дорожная карта ступеней. Перенесено из build_sem06.py
    без изменений. На этой деке сейчас НЕ используется ни одним слайдом —
    n19/n25/n29 Фикс-кругом переведены на `case_divider_quote`/
    `g_case_divider` (см. докстринг модуля); функция оставлена для будущего
    настоящего перехода МЕЖДУ ступенями, если он появится."""
    _, stage = where(sid)
    stages = sections_for(sid)[1]
    tag, badge = tag_for(sid, meta), badge_for(sid)
    K.divider_bg(sl)
    K.strip_pills(sl, LEFT, 0.5, 11.3, len(stages), stage if stage is not None else -1)

    meaning = []
    for kind, b in blocks:
        for ln in (b if kind == "quote" else ([b] if kind == "para" else [])):
            rest = K.plain(ln)
            if rest.lower().startswith(K.plain(title).lower()):
                rest = rest[len(K.plain(title)):].strip(" ·—–-.,;:!?")
            if rest and rest != tag:
                meaning.append(rest)
    if not meaning and assertion:
        meaning = [K.plain(assertion)]
    unseen(sid, pattern, blocks, {"quote", "para"},
           "на развилке рисуются только заголовок, смысловая строка и ярлык")

    tw = 10.0
    th = M.text_h(K.plain(title), 34, tw, spacing=1.05, bold=True)
    mh = (M.block_h(meaning, 17, 10.4, spacing=1.32, space_after=4)
          + M.line_h(17, 1.32)) if meaning else 0.0
    tag_h = 0.55 if tag else 0.0
    total = th + (mh + 0.34 if meaning else 0) + (tag_h + 0.30 if tag_h else 0)
    y = 1.25 + max((5.2 - total) / 2, 0.0)

    if badge:
        K.divider_badge(sl, badge, cy=y + th / 2)
    K.text_box(sl, 1.68, y, tw, th, title, size=34, bold=True, color=K.WHITE, spacing=1.05)
    y += th + 0.34
    if meaning:
        K.text_box(sl, LEFT + 0.35, y, 10.4, mh, meaning, size=17, italic=True,
                   color=K.ON_DARK, spacing=1.32, space_after=4)
        y += mh + 0.30
    if tag_h:
        K.tag_plate(sl, LEFT + 0.35, y, tag)
    if stage is not None:
        K.roadmap(sl, stages, stage)
    K.slide_number_mark(sl, slide_number(sid), on_dark=True)


def g_case_divider(sl, sid, title, blocks, pattern, assertion=""):
    """Дивайдер уровня КЕЙСА — жанровая функция этой деки (приём
    `case_divider_quote`; нет в словаре Семинара 6). На этой деке — ступень 1
    (n04/n12/n16, с самого начала) и ступень 2 (n19/n25/n29, с Фикс-круга —
    см. докстринг модуля: изначально эти три стояли на `section_divider_
    macro`/`g_divider`, асимметрия с зеркальными парами ступени 1).

    Легче `g_divider` на три вещи: без золотого номерного значка (кейс внутри
    ступени — не повод для сквозного счёта, который и так ведёт
    `K.roadmap`), без дорожной карты БЛОКОВ занятия (зал уже на дивайдере
    раздела видел, в какой ступени он находится; дивайдер кейса не повторяет
    это), без строки ярлыка. Вместо дорожной карты блоков — дорожка ТРЁХ
    КЕЙСОВ текущей ступени (А·Б·В), тот же примитив `K.roadmap`, вызванный
    со списком из трёх названий вместо списка ступеней — ни одной новой
    функции в `deck_kit.py` ради этого не потребовалось.

    Реплика кейса рисуется из `title` (H1 слайда), а не из блока-цитаты:
    на всех шести слайдах H1 и первая строка блока-цитаты совпадают
    дословно (или не несут отдельного смысла) — рисовать их оба значило бы
    напечатать одну и ту же фразу дважды на одном экране. Если в блоке-
    цитате есть ВТОРАЯ содержательная строка (n16 — курсивная приписка с
    источником цитаты; n29 — второй абзац цитаты про перенос механизма
    замены, физически разбитый в markdown на 3 строки без пустой строки
    между ними) — она идёт отдельной, мельче и приглушённее, под главной
    репликой. Накопление этой «лишней» строки (`extra_parts`) СКЛЕИВАЕТ все
    непустые, несовпадающие с заголовком физические строки блока-цитаты
    пробелом — не перезаписывает последней (перезапись на n29 роняла 2/3
    текста второго абзаца, см. докстринг модуля, Фикс-круг)."""
    K.divider_bg(sl)
    extra_parts = []
    title_key = K.plain(title).lower().strip(" «».")
    for kind, b in blocks:
        if kind != "quote":
            continue
        for ln in b:
            plain_ln = K.plain(ln).strip()
            if not plain_ln:
                continue
            if plain_ln.lower().strip(" «».") == title_key:
                continue
            extra_parts.append(plain_ln)
    extra = " ".join(extra_parts) if extra_parts else None
    if extra:
        m = ITALIC_LINE.match(extra)
        if m:
            extra = m.group(1).strip()

    tw = 10.6
    th = M.text_h(K.plain(title), 30, tw, spacing=1.18, bold=True)
    eh = (M.text_h(extra, 14, tw, spacing=1.3) + 0.22) if extra else 0.0
    total = th + eh
    y = 1.35 + max((4.5 - total) / 2, 0.0)

    K.text_box(sl, 1.35, y, tw, th, title, size=30, bold=True, color=K.WHITE,
               spacing=1.18)
    y += th + 0.2
    if extra:
        K.text_box(sl, 1.35, y, tw, eh, extra, size=14, italic=True,
                   color=K.ON_DARK_MUTE, spacing=1.3, rich=False)

    case_idx = CASE_IDX.get(sid)
    if case_idx is not None:
        K.roadmap(sl, ("Кейс А", "Кейс Б", "Кейс В"), case_idx)
    K.slide_number_mark(sl, slide_number(sid), on_dark=True)


def g_cover(sl, sid, title, blocks, pattern, assertion=""):
    """Обложка — градиент DEEP→MID→LIGHT, заголовок, золотая полоса, короткий
    подзаголовок о месте в дуге. Перенесено из build_sem06.py; на n01 ни
    номера семинара, ни hero-схемы нет вовсе (прямое требование задания
    слайда — обложка «чистая», без контента кейсов) — `figure_for` для n01
    не объявлен, hero-ветка кода просто не исполняется."""
    K.gradient_rect(sl, 0, 0, K.W_IN, K.H_IN,
                    [(0, (0x21, 0x29, 0x5C)), (55000, (0x06, 0x5A, 0x82)),
                     (100000, (0x1C, 0x72, 0x93))])
    K.text_box(sl, 0.9, 0.3, 11.5, 1.42, title, size=32, bold=True, color=K.WHITE,
               anchor=MSO_ANCHOR.MIDDLE, spacing=1.08, align=PP_ALIGN.CENTER)
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
           "на обложке рисуются иллюстрация (если есть) и подзаголовок")
    quotes = [b for k, b in blocks if k == "quote"]
    if quotes:
        lines = [l for q in quotes for l in q]
        question = [l for l in lines if K.plain(l).rstrip("»\"' ").endswith("?")]
        rest = [l for l in lines if l not in question]
        if rest:
            h = M.block_h([K.plain(l) for l in rest], 18, 11.5, space_after=4)
            ry = (y + bottom) / 2 - h / 2
            K.text_box(sl, 0.9, ry, 11.5, h, rest, size=18, color=K.ON_DARK,
                       align=PP_ALIGN.CENTER, space_after=4)
            y = ry + h + 0.26
        if question:
            K.form_question(sl, 0.9, y, 11.5, question, size=17,
                            max_h=max(bottom - y, 0.7),
                            label=f"{sid} центральный вопрос")
    K.slide_number_mark(sl, slide_number(sid), on_dark=True)


def g_question(sl, sid, title, blocks, pattern, assertion=""):
    """Вопрос — дословный вопрос в золотой коробке. Перенесено из
    build_sem06.py без изменений. Обслуживает `question_with_option_cards`
    (n21, n27 — вопрос + 4 карточки) и `guess_the_number` (n31 — тот же
    жанр, но без карточек: зал называет число устно, а не выбирает строку)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    bottom = BOTTOM

    drawers = []
    for kind, b in blocks:
        if kind == "quote":
            scene, question, found = split_question(b)
            if not found:
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
    K.slide_number_mark(sl, slide_number(sid))


AXIS_COLS = (0.13, 0.27, 0.27, 0.33)

# «Внизу — одна подпись-формула во всю ширину, без кавычек-реплики (золотая
# роль по умолчанию для recap_table)» — n02 и n34 ОБА явно просят золото для
# своей единственной закрывающей цитаты поверх дефолтной роли `fact`
# (`PATTERN_ROLE["recap_table"] = "fact"`). Тот же механизм и тот же повод,
# что в Семинаре 6 (`GOLD_QUOTE_SIDS = {"n02": "all", "n61": "all", …}` там).
GOLD_QUOTE_SIDS = {"n02": "all", "n34": "all"}


def g_axis_table(sl, sid, title, blocks, pattern, assertion=""):
    """Ось занятия и её возврат (n02 — мостик, пустая; n34 — закрытие, три
    нижние строки закрыты). Перенесено из build_sem06.py без изменений."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    gold_rule = GOLD_QUOTE_SIDS.get(sid)
    quote_total = sum(1 for k, _ in blocks if k == "quote") if gold_rule == "last" else 0
    quote_i = -1
    for kind, b in blocks:
        if kind == "table" and len(b[0]) == len(AXIS_COLS):
            inner = WIDTH - 0.4
            cols = [c * inner for c in AXIS_COLS]
            drawers.append(lambda sl, y, mh, h_=b[0], r_=b[1], c=cols: K.table_card(
                sl, LEFT, y, WIDTH, h_, r_, col_w=c, max_h=mh, label=f"{sid} ось"))
            continue
        role = None
        if kind == "quote" and gold_rule:
            quote_i += 1
            if gold_rule == "all" or (gold_rule == "last" and quote_i == quote_total - 1):
                role = "formula"
        d = block_drawer(kind, b, sid, pattern, role=role)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, slide_number(sid))


# «Нижняя строка выделена как мостик к следующему вопросу» (n11 learning_goal)
# — закрывающая цитата n11 кончается на «?» и по умолчанию получила бы роль
# `question` (зал голосует), но после n11 нет reveal-слайда: n12 — дивайдер
# следующего кейса, не разбор. Та же находка и тот же точечный override, что
# в Семинаре 6 держал `CRITERIA_QUOTE_ROLE_FORCE = {"n28": "formula"}`.
CRITERIA_QUOTE_ROLE_FORCE = {"n11": "formula"}


def g_criteria(sl, sid, title, blocks, pattern, assertion=""):
    """Граница применимости — таблица на 2 колонки становится двумя плашками
    бок о бок. Перенесено из build_sem06.py без изменений. На этой деке —
    n11 (конец ступени 1) и n33 (конец ступени 2)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    tables = [b for k, b in blocks if k == "table"]
    others = [(k, b) for k, b in blocks if k != "table"]

    drawers = []
    for kind, b in others:
        if kind == "quote":
            drawers.append(block_drawer(kind, b, sid, pattern,
                                        role=CRITERIA_QUOTE_ROLE_FORCE.get(sid)))

    if len(tables) == 1 and len(tables[0][0]) == 2:
        headers, rows = tables[0]
        left = [r[0] for r in rows if len(r) > 0 and r[0].strip() and r[0].strip() != "—"]
        right = [r[1] for r in rows if len(r) > 1 and r[1].strip() and r[1].strip() != "—"]
        gap, cw = 0.3, (WIDTH - 0.3) / 2

        def pair(sl, y, mh, h_=headers, l_=left, r_=right, cw=cw, gap=gap):
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
        accents = [None, K.GOLD_DARK, K.MID]
        for i, (headers, rows) in enumerate(tables):
            drawers.append(lambda sl, y, mh, h_=headers, r_=rows, a=accents[min(i, 2)]:
                           K.table_card(sl, LEFT, y, WIDTH, h_, r_, max_h=mh, accent=a,
                                        label=f"{sid} критерии"))

    for kind, b in others:
        if kind in ("bullets", "code", "cards", "para"):
            drawers.append(block_drawer(kind, b, sid, pattern))
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, slide_number(sid))


def g_content(sl, sid, title, blocks, pattern, assertion=""):
    """Содержательный слайд по умолчанию: заголовок-утверждение, схема (если
    объявлена), блоки в порядке источника. Это жанр для БОЛЬШИНСТВА приёмов
    словаря Семинара 7 — см. докстринг модуля, раздел «решения по новым
    именам»: 19 из 23 уникальных `visual.pattern` этой деки падают сюда."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    fig = figure_for(sid)
    fig_ceiling = (BOTTOM - y0) if not blocks else K.FIG_NATURAL_H
    if fig:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, LEFT, y, WIDTH, mh if mh else fig_ceiling, label=sid))
    gold_rule = GOLD_QUOTE_SIDS.get(sid)
    quote_total = sum(1 for k, _ in blocks if k == "quote") if gold_rule == "last" else 0
    quote_i = -1
    for kind, b in blocks:
        role = None
        if kind == "quote" and gold_rule:
            quote_i += 1
            if gold_rule == "all" or (gold_rule == "last" and quote_i == quote_total - 1):
                role = "formula"
        d = block_drawer(kind, b, sid, pattern, role=role)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, slide_number(sid))


TRACK_LABELS = ("база", "кромка")


def g_base_edge(sl, sid, title, blocks, pattern, assertion=""):
    """Такт Б — база и кромка на одном экране. Перенесено из build_sem06.py
    без изменений. На этой деке приём `base_and_edge` НЕ использован ни на
    одном из 34 слайдов — функция держится про запас (то же рассуждение, что
    у `audit_figs`/`audit_figure_text` в Семинаре 6: готовый код лучше, чем
    код, который пришлось бы писать с нуля при первой реальной нужде)."""
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
        M._WARNINGS.append(f"ПРИЁМ [{sid} base_and_edge]: в «## Visual» нет таблицы "
                           f"из двух колонок — слайд собран обычной раскладкой")
        return g_content(sl, sid, title, blocks, pattern, assertion)

    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    bottom = BOTTOM

    drawers = [lambda sl, y, mh: K.base_edge_tracks(
        sl, LEFT, y, WIDTH, left, right, left_label=labels[0], right_label=labels[1],
        terms=terms, max_h=mh, label=f"{sid} дорожки")]
    for kind, b in rest:
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers, bottom=bottom, center=1.0)
    K.slide_number_mark(sl, slide_number(sid))


# ── Словарь приёмов Семинара 7 ───────────────────────────────────────────────
#
# Ключи — `visual.pattern`. Семь явных входов — жанры с нестандартной
# композицией; всё остальное падает в `g_content`. Решение по каждому новому
# имени — в докстринге модуля (начало файла).
GENRE_FN = {
    "hero_cover": g_cover,
    "section_divider_macro": g_divider,
    "case_divider_quote": g_case_divider,
    "question_with_option_cards": g_question,
    "reflection_question": g_question,
    "guess_the_number": g_question,
    "recap_table": g_axis_table,
    "criteria_checklist_and_boundary": g_criteria,
    "base_and_edge": g_base_edge,
}


# ── Сборка ──────────────────────────────────────────────────────────────────

def refresh_manifest():
    """Пересобрать манифест из его слайдов перед сборкой — манифест
    производное, правят слайд, а не `deck.yaml` (правило §8.5)."""
    import difflib
    name = DECK_FILE[LANG]
    try:
        import make_deck_yaml as G
        doc, slides = G.build("n", LANG)
        text = G.header_comment(slides, doc["deck"], LANG) + G.yaml.safe_dump(
            doc, allow_unicode=True, sort_keys=False, width=100,
            default_flow_style=False)
    except Exception as e:
        M._WARNINGS.append(f"МАНИФЕСТ: пересобрать не удалось — {e}. "
                           f"Собираю по тому, что лежит в {name}")
        return
    path = ROOT / name
    was = path.read_text(encoding="utf-8") if path.exists() else ""
    if was == text:
        return
    path.write_text(text, encoding="utf-8")
    changed = [l for l in difflib.unified_diff(was.splitlines(), text.splitlines(), n=0)
               if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    head = "; ".join(l.strip() for l in changed[:4])
    M._WARNINGS.append(
        f"МАНИФЕСТ ПЕРЕСОБРАН: {name} был старше слайдов, строк разошлось "
        f"{len(changed)} — {head}{'…' if len(changed) > 4 else ''}")


def deck_from_files(prefix):
    out = []
    sub = SLIDES_DIR[LANG]
    for f in sorted((ROOT / sub).glob(f"{prefix}*.md")):
        md = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
        fm = (yaml.safe_load(m.group(1)) if m else {}) or {}
        out.append({"id": fm.get("id") or f.name.split("-")[0],
                    "file": f"{sub}/{f.name}",
                    "visual": fm.get("visual") or {}})
    return sorted(out, key=lambda s: s["id"])


USAGE = """build_sem07.py — сборка деки Семинара 7.

  --block nNN   ПРЕДПРОСМОТР одного слайда или группы: строит из файлов на
                диске в отдельный `sem-07-nNN.pptx`. Не трогает deck.yaml и
                rendered/sem-07.pptx.
  --all         ПОЛНАЯ пересборка: пересобирает `deck.yaml` из слайдов и
                перезаписывает `rendered/sem-07.pptx`.
  --deck F      собрать по другому манифесту (в `sem-07-F.pptx`).
  nNN nMM …     собрать полотно только этих слайдов, остальные страницы
                оставить пустыми (отладка вёрстки).

Полная пересборка требует ЯВНОГО `--all` (правило §8.9/README circle-2:
ничего не передано — не значит «сделай самое разрушительное»).
"""


def main():
    argv = list(sys.argv[1:])
    if {"--help", "-h", "help"} & set(argv):
        print(USAGE)
        return
    unknown = [a for a in argv if a.startswith("-")
               and a not in ("--block", "--deck", "--all")]
    if unknown:
        print(f"неизвестный флаг: {' '.join(unknown)}\n")
        print(USAGE)
        raise SystemExit(2)
    full = "--all" in argv
    if full:
        argv.remove("--all")
    block = None
    if "--block" in argv:
        i = argv.index("--block")
        block = argv[i + 1] if i + 1 < len(argv) else "n"
        del argv[i:i + 2]

    deck_file = DECK_FILE[LANG]
    if "--deck" in argv:
        i = argv.index("--deck")
        deck_file = argv[i + 1]
        del argv[i:i + 2]

    if block:
        slides = deck_from_files(block)
        out_name = f"sem-07-{block}.pptx"
        if not slides:
            print(f"слайдов по образцу «{block}*.md» не найдено")
            return
    elif not full and deck_file == DECK_FILE[LANG]:
        print("полная пересборка деки не запрошена.\n")
        print(USAGE)
        raise SystemExit(2)
    else:
        deck_path = ROOT / deck_file
        if deck_path.exists():
            slides = yaml.safe_load(deck_path.read_text(encoding="utf-8"))["slides"]
        elif deck_file == DECK_FILE[LANG]:
            slides = []
        else:
            raise SystemExit(f"файла «{deck_file}» нет — и это не deck.yaml, "
                             f"чтобы пересобрать его автоматически")
        out_name = OUT_NAME[LANG] if deck_file == DECK_FILE[LANG] else \
            f"sem-07-{Path(deck_file).stem}.pptx"
    deck = {"slides": slides}
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(K.W_IN), Inches(K.H_IN)
    blank = prs.slide_layouts[6]
    M.reset()
    if not block and deck_file == DECK_FILE[LANG]:
        refresh_manifest()
        slides = yaml.safe_load((ROOT / deck_file).read_text(encoding="utf-8"))["slides"]
        deck["slides"] = slides

    only = set(argv)
    built = 0
    for s in deck["slides"]:
        sid = s["id"]
        pattern = (s.get("visual") or {}).get("pattern", "")
        md = (ROOT / s["file"]).read_text(encoding="utf-8")
        title, _assertion, visual, notes = SP.sections(md)
        sl = prs.slides.add_slide(blank)
        blocks = sanitize_blocks(SP.blocks(visual))
        if not only or sid in only:
            fn = GENRE_FN.get(pattern, g_content)
            kw = {"meta": s.get("visual")} if fn is g_divider else {}
            fn(sl, sid, title or sid, blocks, pattern, _assertion, **kw)
        audit_question_answer(sid, pattern, blocks)
        if notes:
            K.write_notes(sl, notes)
        built += 1

    audit_numbering(deck["slides"])
    audit_crossrefs(deck["slides"])
    audit_figs(slides)
    audit_figure_text()
    out = HERE / out_name
    prs.save(out)
    warns = M.report()
    for w in warns:
        print("•", w)
    print(f"\nслайдов: {built}   предупреждений: {len(warns)}   "
          f"файл: {out.name} ({out.stat().st_size // 1024} КБ)")


if __name__ == "__main__":
    main()
