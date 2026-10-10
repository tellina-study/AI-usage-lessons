#!/usr/bin/env python3
"""Сборка деки Семинара 6 из source-of-truth: ../deck.yaml + ../slides/nNN-*.md

Устройство — ПО ОБРАЗЦУ `sem-05/rendered/build_sem05.py`, не копия: Семинар 6
не тащит совместимость со старой 50-слайдной декой (`sNN`/`deck-s50.yaml`),
которая в build_sem05.py существовала только потому, что старая и новая дека
жили в репозитории одновременно. Здесь дека одна, нумерация одна (`nNN`), и
весь код про вторую нумерацию выброшен, а не перенесён.

Три правила библиотеки приёмов — те же самые (`tools/presentation-build/
seminar-deck-kit.md`, `proverki-i-pravila.md`), и держит их тот же код
`deck_kit.py`/`metrics.py`/`slide_parts.py`, взятый из Семинара 5 БЕЗ ИЗМЕНЕНИЙ
(см. `RENDERER-NOTES.md` § «Кит» этого занятия — там же обоснование решения
копировать, а не выносить в общее место):

* высота блока ИЗМЕРЯЕТСЯ тем же кодом, который рисует;
* вёрстка идёт ОТ КУРСОРА;
* воздух — параметр, не остаток.

Жанровые функции (`g_divider`, `g_cover`, `g_question`, …) и сборочные аудиты
(`audit_numbering`, `audit_figs`, `audit_question_answer`, …) перенесены из
`build_sem05.py` почти буквально — их логика не привязана к содержанию
Семинара 5, только к СЛОВАРЮ ПРИЁМОВ. Словарь ПРОВЕРЕН по уже написанным
слайдам (`slides/n*.md`, 28 из 63 на момент сборки этого файла), а не только
по плану `SVODKA-SLAIDOV.md` — и он почти буквально ТОТ ЖЕ, что в Семинаре 5
(`section_divider_macro`, `question_with_option_cards`, `answer_breakdown_
table`, `evidence_table_with_gap`, `base_and_edge`, `recap_table`, …), с двумя
новыми вариантами (`failure_vignette_table`, `mechanics_table`). `type`
слайда (из `SVODKA-SLAIDOV.md`) и `visual.pattern` — РАЗНЫЕ поля: см.
комментарий у `PATTERN_ROLE` ниже, где это важно для дальнейшей правки.
Переписаны под этот словарь: `PATTERN_ROLE`, `GENRE_FN`, `SECTIONS_BY_PREFIX`,
`TAGS`, `FIGS`, `BADGE_OVERRIDE`.

Границы разделов Семинара 6 (`SVODKA-SLAIDOV.md`):

    n01–n05   Мостик     (без ступени дорожной карты)
    n06–n28   MCP        (ступень 0, кейсы 1–2; кейс «подключён, а агент через него
                          не ходит» свёрнут до одного экрана n17, issue 225 §A2)
    n29–n60   Субагент   (ступень 1, кейсы 3–5)
    n61–n64   Сборка     (без ступени)

Схемы (`make_figures*.py`) этот файл не рисует и не трогает — рисовалки схем
Семинара 6 это ОТДЕЛЬНАЯ ФАЗА (см. SBORKA-OTCHET.md). `figure_for()` читает
только `visual.figure` из фронтматтера слайда; реестр `FIGS` пуст и остаётся
пустым, пока фаза схем не началась.
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

# Язык источника: каталог слайдов, манифест и имя выходного файла. Переключается
# флагом `--lang` (см. `set_lang` и `LANG_SIGNALS` ниже); по умолчанию русский.
SLIDES_DIR = {"ru": "slides", "en": "slides-en"}
DECK_FILE = {"ru": "deck.yaml", "en": "deck.en.yaml"}
OUT_NAME = {"ru": "sem-06.pptx", "en": "sem-06-en.pptx"}

TOP, BOTTOM = 0.34, 6.92        # рабочее поле по вертикали
LEFT, WIDTH = 0.55, 12.23       # и по горизонтали
GAP = 0.18                      # шаг между блоками

# ── Где мы: границы разделов и ступень дорожной карты ───────────────────────
#
# Запасной вариант, если по опорным приёмам границы не выводятся (например,
# на пробной сборке `--block n`, пока развилок в выборке меньше четырёх). Числа
# — ровно те, что в `SVODKA-SLAIDOV.md`: Мостик 1–5, MCP 6–28 (кейсы 1–2, после
# свёртки кейса «подключён, а агент через него не ходит»), Субагент 29–60
# (кейсы 3–5), Сборка 61–64. Нумерация сведена сквозной при сведении после
# проведения (2026-10-10): дырки на месте свёрнутого кейса больше нет, и
# идентификатор слайда снова равен его сквозному номеру.
# Имена блоков занятия ПЕЧАТАЮТСЯ НА ЭКРАНЕ: два из четырёх («MCP»,
# «Субагент») — это таблички дорожной карты внизу каждой макро-развилки
# (`deck_kit.roadmap` рисует их текстом, 12,5 pt). То есть строка ниже — не
# служебное имя, а видимый слой, и в английской деке она обязана быть
# английской, иначе дорожная карта на пяти развилках выйдет кириллицей.
#
# Найдено этой же сессией при разборе того, что вообще в деку попадает НЕ из
# слайдов: кроме этих имён и номерных значков (цифры) сборщик своего текста на
# слайд не выводит — все `text_box` в этом файле получают заголовок, смысловую
# строку или строку развилки из самого слайда, а `label=` таблиц в картинку не
# идёт, он только называет блок в предупреждениях.
#
# Английские имена — из замка (Часть D, строка блоков занятия): Мостик → Bridge,
# Субагент → Subagent, Сборка → Wrap-up (не *assembly*: это читалось бы как
# сборка деки; `со-сборка` остаётся *co-building*).
BLOCKS = {
    "ru": ("Мостик", "MCP", "Субагент", "Сборка"),
    "en": ("Bridge", "MCP", "Subagent", "Wrap-up"),
}


def blocks_names():
    return BLOCKS[LANG]


SECTIONS_BY_PREFIX = {
    "n": ([(1, 5, "Мостик", None), (6, 28, "MCP", 0), (29, 60, "Субагент", 1),
           (61, 64, "Сборка", None)],
          ["MCP", "Субагент"]),
}
SECTIONS, STAGES = SECTIONS_BY_PREFIX["n"]


def _sections_fallback(prefix):
    """Запасные границы с именами блоков текущего языка."""
    got = SECTIONS_BY_PREFIX.get(prefix)
    if not got:
        return None
    rows, _stages = got
    b = blocks_names()
    rows = [(lo, hi, b[i], st) for i, (lo, hi, _n, st) in enumerate(rows)]
    return rows, [b[1], b[2]]

# Ярлыки развилок (`visual.tag`) живут в самих слайдах (по тому же решению,
# что в Семинаре 5 — см. RENDERER-NOTES.md сем. 5 «Схема и ярлык объявляются
# САМИМ СЛАЙДОМ»). Реестр здесь — только запасной путь; ожидается, что он
# остаётся пустым.
TAGS = {}


def divider_index(sid):
    """Порядковый номер развилки в деке, считая с единицы; 0 — не развилка."""
    div = [s["id"] for s in _deck_slides(sid[0])
           if (s.get("visual") or {}).get("pattern") == "section_divider_macro"]
    return div.index(sid) + 1 if sid in div else 0


def badge_for(sid):
    if sid in BADGE_OVERRIDE:
        return BADGE_OVERRIDE[sid]
    n = divider_index(sid)
    return n or None


def tag_for(sid, visual_meta):
    """Ярлык развилки («5 подключений · 2 слоя провала»). С круга 2 замечаний
    владельца (issue 225, правило А6) его на развилках НЕТ: «комментарии "четыре
    хода сборки, два слоя провала" — это тоже лишнее, убери».

    Поэтому отсутствие ярлыка здесь больше не предупреждение, а норма — и
    наоборот: ярлык, случайно оставшийся в чьём-то фронтматтере, называется
    вслух, иначе снятое правило вернётся на экран незамеченным через одну
    невычищенную развилку."""
    tag = (visual_meta or {}).get("tag") or TAGS.get(sid)
    if tag:
        M._WARNINGS.append(
            f"ЯРЛЫК ВЕРНУЛСЯ [{sid}]: на развилке стоит `tag: {tag}` — круг 2 "
            f"замечаний владельца (правило А6) снял ярлыки со всех развилок; "
            f"уберите строку `tag:` из `visual:` фронтматтера")
    return tag


# Номер на значке развилки — номер КЕЙСА (сквозной, 1…6), не номер ступени.
# На этом занятии нет случая, когда он расходится с порядковым номером
# развилки в деке — реестр оставлен пустым и существует как тот же запасной
# путь, что в Семинаре 5 (там он понадобился на s07/s21/s33 старой деки).
BADGE_OVERRIDE = {}

# Реестр схем — пуст. Рисовалки схем Семинара 6 это отдельная фаза (см.
# SBORKA-OTCHET.md «Что осталось сделать»); до неё `visual.figure` слайдов
# тоже не заполнен, и обе проверки (`audit_figs`) должны молчать.
FIGS = {}


_NUM = re.compile(r"^[a-zA-Z]*(\d+)([a-zA-Z]*)$")


def num(sid):
    """Номер слайда из его идентификатора. Терпит буквенный хвост (`n18a`)."""
    m = _NUM.match(sid)
    if not m:
        M._WARNINGS.append(f"ИМЯ СЛАЙДА [{sid}]: из идентификатора не читается "
                           f"номер — слайд попадёт в конец и без раздела")
        return 10 ** 6
    return int(m.group(1))


# ── Границы разделов выводятся ИЗ САМОЙ ДЕКИ, а не задаются номерами ────────
#
# Тот же приём, что в Семинаре 5 (border by anchors, не by numbers) — потому
# что три параллельные сессии ещё пишут слайды, и номера могут сдвинуться.
# Опорные точки для Семинара 6:
#
#   1-й `section_divider` → начало блока MCP (кейс 1)
#   3-й С КОНЦА `section_divider` → начало блока Субагент (состав 2+3: кейс
#                            «подключён, а агент через него не ходит» свёрнут
#                            до одного экрана внутри кейса подключения, issue
#                            225, qa/RAZBOR-PROVEDENIYA.md §A2)
#   ПОСЛЕДНИЙ `recap_table` → начало блока Сборка
#
# Счёт С КОНЦА, а не с начала, выбран намеренно: у блока субагента три кейса и
# они замыкают деку, поэтому снятие или добавление кейса в блоке MCP границу не
# сдвигает. Порядковый номер с начала (прежний `div[3]`) после свёртки кейса
# MCP назвал бы началом субагента четвёртую развилку — то есть практику.
#
# Отличие от Семинара 5 в одном: там `recap_table` встречается в деке РОВНО
# ОДИН раз (в самом конце), и «первый» и «последний» совпадают. В Семинаре 6
# `recap_table` открывает дорожку оси ДВАЖДЫ — пустой на n03 (блок Мостик) и
# заполненной на n61 (блок Сборка), — поэтому границу даёт ПОСЛЕДНИЙ, а не
# первый; если взять первый, блок Сборка увёл бы на себя весь остаток деки от
# n03 и закрасил бы MCP и Субагент как «Сборка».
_DERIVED = {}


def _anchor_sections(slides):
    """Границы по опорным приёмам. `None`, если опор не хватает."""
    pat = [((s.get("visual") or {}).get("pattern", ""), num(s["id"])) for s in slides]
    div = [n for p_, n in pat if p_ == "section_divider_macro"]
    recaps = [n for p_, n in pat if p_ == "recap_table"]
    if len(div) < 4 or not recaps:
        return None
    if len(div) != 5:
        M._WARNINGS.append(
            f"СОСТАВ КЕЙСОВ: дивайдеров {len(div)}, а не 5 — граница блоков "
            f"выведена по допущению «блок Субагент открывает третья развилка с "
            f"конца» (кейсы 2+3). Если состав другой, поправить "
            f"SECTIONS_BY_PREFIX и это допущение")
    recap = max(recaps)
    last = max(n for _p, n in pat)
    bridge, mcp, sub, wrap = blocks_names()
    return [(1, div[0] - 1, bridge, None),
            (div[0], div[-3] - 1, mcp, 0),
            (div[-3], recap - 1, sub, 1),
            (recap, last, wrap, None)], [mcp, sub]


def _deck_slides(prefix):
    """Слайды деки. Семинар 6 — ОДНА дека (`deck.yaml`); если его слайды не
    той нумерации (пусто/старое содержимое) или блок ещё не вошёл в манифест,
    собираем прямо из файлов (`deck_from_files`) — тот же режим предпросмотра
    блока, что в Семинаре 5."""
    try:
        sl = yaml.safe_load(
            (ROOT / DECK_FILE[LANG]).read_text(encoding="utf-8"))["slides"]
        if sl and sl[0]["id"][0] == prefix:
            return sl
    except Exception:
        pass
    return deck_from_files(prefix)


def sections_for(sid):
    """Границы разделов и ступени дорожной карты.

    Кэш ключится ЯЗЫКОМ вместе с приставкой: имена блоков языковые (см.
    `BLOCKS`), и один общий ключ отдал бы английской сборке русские таблички,
    если в том же процессе до неё посчиталась русская."""
    pre = sid[0]
    key = (LANG, pre)
    if key not in _DERIVED:
        try:
            _DERIVED[key] = _anchor_sections(_deck_slides(pre))
        except Exception:
            _DERIVED[key] = None
    return _DERIVED[key] or _sections_fallback(pre) or (SECTIONS, STAGES)


def slide_number(sid):
    """Сквозной номер слайда (1…N) — ВЫВОДИТСЯ из порядка слайда в deck.yaml,
    а не из идентификатора. Та же причина, что в Семинаре 5 (круг 4, А6):
    буквенные хвосты и дырки в нумерации разводят номер с идентификатором."""
    ids = [s["id"] for s in _deck_slides(sid[0])]
    return ids.index(sid) + 1 if sid in ids else None


def where(sid):
    n = num(sid)
    for lo, hi, name, stage in sections_for(sid)[0]:
        if lo <= n <= hi:
            return name, stage
    return "", None


def slide_figure(sid):
    """Имя схемы, объявленное САМИМ СЛАЙДОМ (`visual.figure`), или None."""
    for s in _deck_slides(sid[0]):
        if s["id"] == sid:
            return (s.get("visual") or {}).get("figure")
    return None


def figure_for(sid):
    """Схема слайда: сперва то, что объявил сам слайд, потом реестр `FIGS`
    (который на Семинаре 6 пуст, пока не начата фаза схем)."""
    fn = slide_figure(sid) or FIGS.get(sid)
    if not fn:
        return None
    path = FIGDIR / fn
    return path if path.exists() else None


def draws_figure(pattern):
    """Спрашивает ли жанр этого приёма схему вообще."""
    return GENRE_FN.get(pattern, g_content) in (g_content, g_closing, g_cover)


# Что после вопроса — выбор, а что уже ответ (правило владельца: «на слайде
# всё одновременно»; если ответ приходит после паузы — он на СЛЕДУЮЩЕМ слайде).
ANSWER_KINDS = {"table", "code", "bullets"}
ANSWER_ROLES = {"formula", "fact", "caveat"}


def audit_question_answer(sid, pattern, blocks):
    """Вопрос к залу и ответ на него на ОДНОМ экране — проверка, не починка."""
    qi = None
    for i, (kind, b) in enumerate(blocks):
        if kind != "quote":
            continue
        if quote_role(b, pattern) == "question" or (
                pattern == "question_with_option_cards" and split_question(b)[2]):
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
    """Сквозной номер напечатан на КАЖДОМ слайде и ровно один раз, 1…N."""
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
    """Ссылка на соседний слайд из служебной части (`visual.primary/backup/tag`)
    ведёт на существующий слайд."""
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
    """Схемы против каталога и против деки — по ВСЕМ слайдам и ВСЕМУ реестру.

    На Семинаре 6 `FIGS` пуст по построению (фаза схем не начата) — эта
    проверка остаётся на будущее: как только `visual.figure` появится у
    первого слайда, она начнёт работать без единой правки."""
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
    """Разметка в тексте, который генераторы схем печатают на картинку.

    На Семинаре 6 пока нет ни одного `make_figures*.py` (фаза схем не
    начата) — глоб найдёт 0 файлов, и проверка честно промолчит. Она
    остаётся здесь готовой: как только рисовалки появятся, заработает без
    единой правки — то же рассуждение, что у `audit_figs`."""
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


# ── Замер = отрисовка ───────────────────────────────────────────────────────
_scratch = Presentation()
_scratch.slide_width, _scratch.slide_height = Inches(K.W_IN), Inches(K.H_IN)


def measure(fn, *a, **kw):
    """Высота блока, полученная ТЕМ ЖЕ кодом, который его рисует: блок
    рисуется на черновом слайде, высота запоминается, слайд остаётся в
    `_scratch` (который никогда не сохраняется — не удаляется, а просто
    выбрасывается вместе со всем модулем в конце процесса). Замер и отрисовка
    поэтому не могут разойтись.

    Перенесено из build_sem05.py — там ровно эта реализация (без попытки
    удалить XML черновой слайда: `sl._element.getparent()` для СЛАЙДА — это
    корень ОТДЕЛЬНОЙ part-XML, а не узел внутри дерева presentation.xml, и у
    него `getparent() is None` ВСЕГДА; попытка `.remove()` на нём обязана
    бросить `AttributeError` при первом же вызове. Черновик первой версии
    этого файла такую попытку делал — отличие от build_sem05.py появилось не
    при переносе кода, а при его пересказе по памяти, и было пойманo первым
    же прогоном смоук-теста, что и есть ровно то, для чего смоук-тест
    заведён)."""
    sl = _scratch.slides.add_slide(_scratch.slide_layouts[6])
    saved = list(M._WARNINGS)
    h = fn(sl, *a, **kw)
    M._WARNINGS[:] = saved      # предупреждения чернового прохода не печатаем
    return h


# ── Роль блока-цитаты/абзаца по умолчанию, когда текст сам её не диктует ───
#
# ВАЖНО: ключи здесь — это `visual.pattern` (приём вёрстки), а НЕ `type`
# слайда (жанр содержания из `SVODKA-SLAIDOV.md` § «Словарь типов»). Это два
# разных поля фронтматтера: `type: reflection_question` может стоять и у
# `visual.pattern: question_with_option_cards` (вопрос с карточками выбора,
# n11/n52), и у `visual.pattern: reflection_question` буквально (вопрос БЕЗ
# карточек, n04/n63) — see `SVODKA-SLAIDOV.md` n04 «(без карточек)».
#
# Таблица ниже сверена с ФАКТИЧЕСКИМ словарём `visual.pattern`, уже
# используемым в написанных слайдах (`slides/n*.md`, проверено 2026-10-04 —
# 18 уникальных значений на 28 слайдах из 63), а не с одним лишь планом:
# словарь приёмов Семинара 6 почти буквально воспроизводит словарь Семинара 5
# (`section_divider_macro`, `question_with_option_cards`, `answer_breakdown_
# table`, `evidence_table_with_gap`, `base_and_edge`, …), с двумя новыми
# вариантами, которых в Семинаре 5 не было: `failure_vignette_table` (табличный
# вариант провала) и `mechanics_table` (табличный вариант механики — Семинар 5
# не заводил роли ни для одного варианта `mechanics_*`, и здесь она тоже не
# заводится, см. комментарий ниже).
#
# Роль назначена по той же логике, что в Семинаре 5 (RENDERER-NOTES.md сем. 5,
# п. 3: «разбор и провал → формула, строка оси → факт»), и ровно на тех
# приёмах, где эта роль там же РЕАЛЬНО что-то решает (а не на всех 18 —
# `problem_scenario`, `cobuilding_config_reveal`, `code_artifact`,
# `file_tree_snapshot`, `mechanics_table`, `mechanics_with_figure` в Семинаре 5
# тоже не получили записи: там роль цитаты внутри них по умолчанию падает в
# «formula», и ни один живой слайд от этого не испортился).
PATTERN_ROLE = {
    "question_with_option_cards": "question",
    "reflection_question": "question",
    "answer_breakdown_table": "formula",
    "failure_vignette": "formula",
    "failure_vignette_table": "formula",
    "criteria_checklist_and_boundary": "formula",
    "evidence_table_with_gap": "formula",
    "lecture_map": "fact",
    "base_and_edge": "fact",
}

# Оговорка опознаётся двумя разными способами (см. RENDERER-NOTES.md сем. 5,
# п. 3): жанровым словом в начале блока ИЛИ признанием пробела где угодно.
# Сами шаблоны — в `LANG_SIGNALS` ниже, по одному набору на язык источника;
# модульные `ASK` / `CAVEAT_OPEN` / `CAVEAT` ставит `set_lang()`.


# ── Чем опознаётся РЕПЛИКА, а не формула ───────────────────────────────────
#
# Кавычка в начале блока-цитаты в этом конвейере — РАЗМЕТКА, а не типографика:
# по ней `quote_role()` ниже отличает тихую реплику докладчика (тиловая полоса)
# от формулы-итога (золотая планка). На этом стоят живые решения по деке:
# `backup` n03 описывает, как кавычки СНИМАЛИ, чтобы строка попала в золото, а
# n05 пришлось добавить в `GOLD_QUOTE_SIDS`, потому что снятия не хватило.
#
# Пока дека была одна, знак можно было вписать в код буквой. С английской декой
# нельзя: «ёлочек» в английском тексте нет (так во всех EN-деках семинаров 1–4,
# решение D5 EN-трека Семинара 4 — `"…"`), и тот же код, запущенный по
# `slides-en/`, опознал бы РОЛЬЮ ФОРМУЛЫ каждую из одиннадцати цитат деки и не
# оставил бы ни одной тихой реплики. Поймано сессиями перевода ДО рендера
# (`qa/perevod-n01-n32.md` §3.1), а не после него по картинке.
#
# Почему аргумент языка, а не второй сборщик. У Семинара 4 отдельный EN-драйвер
# (`sem-04/rendered/build_sem04_en.py`) заведён по ДРУГОЙ причине: там
# переведённых слайдов нет вовсе, английский собирается из русских слайдов плюс
# таблица строк, и драйверу приходится подменять текст на входе в вёрстку.
# Здесь переведены все 64 файла, и отличий у двух источников ровно два: каталог
# слайдов (его задаёт манифест, то есть уже существующий флаг `--deck`) и знак
# кавычки. Копия сборщика ради одного знака разошлась бы с русским при первой же
# правке русского — тот самый довод, которым свой выбор объясняет докстринг
# драйвера Семинара 4.
#
# Разметочная симметрия, на которой стоит решение, промерена: в `slides/` 11
# блоков-цитат открываются `«` и НИ ОДИН не открывается `"`; в `slides-en/` те же
# 11 слайдов открываются `"` и ни один — `«`. То есть соответствие один в один, и
# язык полностью определяет знак.
# Роль блока опознаётся НЕ ОДНИМ признаком, а тремя, и все три языковые.
# Задание в эту сессию называло один — кавычку; `--quote-roles` по готовой
# английской деке нашёл остальные два, и это ровно то, ради чего режим и
# заведён. Сверка ролей двух дек до починки: совпали 73 блока из 81, разошлись 8.
#
#   1. ЗНАК РЕПЛИКИ (6 из 8 несовпадений шли НЕ отсюда — см. п. 2 и 3). «Ёлочка»
#      в начале блока → тихая реплика докладчика, иначе формула-итог.
#   2. ВОПРОС К ЗАЛУ — по жанровому глаголу в повелительном наклонении
#      («выберите», «назовите»). Английский текст по русскому списку не
#      опознаётся вовсе, и шесть вопросов с карточками получали роль `fact`:
#      n11, n23, n33, n40, n52, n60.
#   3. ОГОВОРКА — по жанровому зачину («Честный пробел…»). Та же причина, два
#      места: n35 и n47 — честные пробелы кейсов — выходили формулой-итогом,
#      то есть признание «этого никто не измерял» печаталось золотой планкой
#      наравне с выводами, которые занятие как раз утверждает.
#
# Отсюда вывод, который стоит зафиксировать: вынести в язык надо было не знак, а
# ВСЕ признаки роли, и единственный надёжный способ это узнать — сверить роли
# двух дек поблочно, а не прочитать код. Английские шаблоны ниже проверены
# ровно так: каждый даёт столько же срабатываний, сколько русский, и на тех же
# слайдах (6 и 2), ни одного лишнего на остальных 73 блоках.
LANG_SIGNALS = {
    "ru": {
        "open": ("«",),
        "pairs": (("«", "»"), ("**", "**")),
        "ask": r"выберите|что бы вы|как бы вы|назовите|подумайте",
        "caveat_open": r"^\W*(оговорка|честный пробел|честно про|честно о\b)",
        "caveat": (r"не проверен|не провер[её]н|не измер|нет данных|не подтвер|"
                   r"не удалось|честного пробела|честный пробел|нечестн"),
    },
    "en": {
        "open": ('"', "\u201c"),
        "pairs": (('"', '"'), ("\u201c", "\u201d"), ("**", "**")),
        # «name» — слово частое, поэтому берётся не само, а повелительным
        # оборотом занятия («Name both numbers», «Name yours»): проверено на
        # всех 81 блоке, ложных срабатываний ноль.
        "ask": (r"\b(?:pick|choose)\b|\bname (?:yours|both|your|the piece|a |one )"
                r"|what would you|how would you|\bthink (?:about|through)\b"
                r"|say out loud"),
        "caveat_open": r"^\W*(an honest gap|a caveat|honestly about)",
        "caveat": (r"not been verified|not verified|unverified|not measured"
                   r"|no data|not confirmed|an honest gap|honest gap|dishonest"),
    },
}
LANG = "ru"
SPEECH_OPEN = ASK = CAVEAT_OPEN = CAVEAT = None


def set_lang(lang):
    """Переключить язык источника. Трогает ровно те признаки, по которым
    опознаётся РОЛЬ блока, и ничего кроме: композиция, сетка, цвета, кегли и
    жанры от языка не зависят. Если однажды начнут — видно это будет здесь, а
    не в тридцати местах."""
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
    """Блок начинается кавычкой языка источника, то есть это реплика."""
    return body.lstrip().startswith(SPEECH_OPEN)


def quote_role(lines, pattern):
    """Какую работу делает этот блок-цитата (см. RENDERER-NOTES.md сем. 5,
    п. 3 — работа блока видна из текста, форма не переиспользуется между
    разными работами)."""
    body = " ".join(K.plain(l) for l in lines).strip()
    if body.rstrip("»\"' ").endswith("?") or ASK.search(body):
        return "question"
    if CAVEAT_OPEN.match(K.plain(body).lstrip("*> ")) or CAVEAT.search(body):
        return "caveat"
    base = PATTERN_ROLE.get(pattern)
    if base == "question":          # вопрос уже нашёлся бы выше — значит это подводка
        return "speech" if opens_speech(body) else "fact"
    if opens_speech(body):
        return "speech"
    return base or "formula"


FORM = {"question": K.form_question, "formula": K.form_formula,
        "speech": K.form_speech, "caveat": K.form_caveat, "fact": K.form_fact}

ITALIC_LINE = re.compile(r"^\s*\*([^*].*?)\*\s*$")


def para_role(text, pattern):
    """Какую работу делает ГОЛЫЙ абзац и каким текстом он выйдет на слайд."""
    m = ITALIC_LINE.match(text)
    if m:
        return "speech", m.group(1).strip()
    return quote_role([text], pattern), text


# Заполняется из `LANG_SIGNALS` вызовом `set_lang("ru")` сразу под этой строкой;
# объявление нужно только затем, чтобы `global` в `set_lang` имел что связывать.
_WRAP_PAIRS = ()
set_lang("ru")


def split_question(lines):
    """Разделить блок на СЦЕНУ и сам ВОПРОС, по границе предложения.

    Если весь блок обёрнут ОДНОЙ парой маркеров целиком (`**жирный**` на
    несколько предложений или кавычки `«…»` вокруг целой реплики) — наивное
    разбиение по границе предложения резало текст ПОСЕРЕДИНЕ прогона:
    открывающий маркер оставался в одной половине без пары, закрывающий — в
    другой, и оба печатались на слайде буквально (`**И...` / `...**`,
    `«Работу...` без закрывающей » в одной рамке / висячая `»` без открывающей
    в другой — живые случаи n52/n42 и n04/n63).

    Починка: снять внешнюю пару ДО разбиения, разбить голый текст, и — если
    блок был обёрнут — вернуть обёртку каждой непустой половине ОТДЕЛЬНО, со
    своей собственной парой маркеров: каждая половина рисуется в своей рамке,
    и внутри своей рамки обязана быть полной репликой/жирным куском, а не
    половиной чужой пары."""
    flat = " ".join(lines).strip()
    op, cl = "", ""
    for o, c in _WRAP_PAIRS:
        if not (flat.startswith(o) and flat.endswith(c) and len(flat) > len(o) + len(c)):
            continue
        # Пара из ОДИНАКОВЫХ знаков (английские `"…"`, а также `**…**`) требует
        # оговорки, которой русским «…» не нужно: блок «"одна реплика" и
        # "вторая"» тоже начинается и кончается этим знаком, но одной обёрткой
        # НЕ является, и снятие «внешней пары» разрушило бы обе внутренние.
        # Признак настоящей обёртки — внутри знака больше нет.
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
    """Сказать вслух про блоки, которые этот жанр рисовать не будет."""
    for kind, _b in blocks:
        if kind not in handled:
            M._WARNINGS.append(f"БЛОК НЕ ПОКАЗАН [{sid} · {pattern}]: блок вида "
                               f"«{kind}» — {why}")


# ── Отрисовка одного блока ──────────────────────────────────────────────────

def block_drawer(kind, b, sid, pattern, *, role=None):
    """Блок → приём. Одна работа — одна форма."""
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
        # «выбери» (вопрос) и «запомни» (термины) — разные работы, разные формы
        if pattern == "question_with_option_cards":
            return lambda sl, y, mh: K.option_row(sl, LEFT, y, WIDTH, b,
                                                  max_h=min(mh or 1.7, 1.7),
                                                  label=f"{sid} варианты")
        return lambda sl, y, mh: K.term_pills(sl, LEFT, y, WIDTH, b, label=f"{sid} термины")
    if kind == "bullets":
        # `b` — либо список пунктов (старая форма), либо пара
        # «пункты + нумерован ли список в источнике» (разборщик даёт пару).
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
    """Универсальная укладка: сначала все блоки меряются, потом раскладываются
    (см. деталь алгоритма в build_sem05.py — здесь перенесена без изменений)."""
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
    """Дивайдер уровня раздела — градиент, золотая полоса, номерной значок,
    смысловая строка, ярлык, дорожная карта. Перенесено из build_sem05.py
    без изменений (приём не зависит от содержания Семинара 5)."""
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


def g_cover(sl, sid, title, blocks, pattern, assertion=""):
    """Обложка — градиент DEEP→MID→LIGHT, заголовок, иллюстрация, центральный
    вопрос в золотой коробке. Перенесено из build_sem05.py; номер занятия
    («06» в углу и надпись «СЕМИНАР 6» над заголовком) снят по решению
    владельца (issue 225, пересмотр правила): обложка была унаследованным
    исключением из правила «номера занятия нет на видимом слое» (Семинары
    2-5), исключение отменено. Заголовок поднят и отцентрован в освободившейся
    верхней полосе (anchor=MIDDLE вместо BOTTOM), чтобы пустота читалась как
    отступ, а не как дыра на месте снятой надписи; золотая полоса и hero-схема
    внизу (≥40% площади) не трогались."""
    K.gradient_rect(sl, 0, 0, K.W_IN, K.H_IN,
                    [(0, (0x21, 0x29, 0x5C)), (55000, (0x06, 0x5A, 0x82)),
                     (100000, (0x1C, 0x72, 0x93))])
    K.text_box(sl, 0.9, 0.3, 8.0, 1.42, title, size=33, bold=True, color=K.WHITE,
               anchor=MSO_ANCHOR.MIDDLE, spacing=1.08)
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
    K.slide_number_mark(sl, slide_number(sid), on_dark=True)


def g_question(sl, sid, title, blocks, pattern, assertion=""):
    """Вопрос — дословный вопрос в золотой коробке, ни одной подсказки.
    Перенесено из build_sem05.py без изменений."""
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


# Ось занятия возвращается дважды (n03, n61) — колонки задаются явно, чтобы
# обе отрисовки давали ту же ширину, а не пересчитанную по содержимому.
AXIS_COLS = (0.13, 0.27, 0.27, 0.33)


def g_axis_table(sl, sid, title, blocks, pattern, assertion=""):
    """Ось занятия и её возврат. Светлый фон, таблица-коробка; незаполненные
    ячейки — пунктирные слоты. Перенесено из build_sem05.py почти без
    изменений — одно исправление ниже.

    Вторая прожарка (issue 225, P1-3): `GOLD_QUOTE_SIDS` объявляет `n61`
    («recap_table») золотым («all»), но до этой правки объявление ничего не
    решало — эта функция рисовала блок-цитату через `block_drawer(...)` без
    `role`, той же веткой, что и `n03` (который в `GOLD_QUOTE_SIDS` НЕ стоит).
    Правило применялось только внутри `g_content` (жанр `code_artifact`/
    `answer_breakdown_table`/…), а `recap_table` идёт отдельным жанром через
    эту функцию — отсюда 0 золотых пикселей на `n61`, промеренных по PNG,
    при том что код уже называл его золотым. Чинится тем же правилом, что в
    `g_content` (строки `gold_rule`/`quote_total`/`quote_i` ниже — дословно
    та же логика, не новая)."""
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


# Круг после прожарок (issue 225, P1-3): n28 — ЕДИНСТВЕННЫЙ `criteria_
# checklist_and_boundary` (n20/n28 в блоке MCP, n37/n49/n59/n60 в блоке
# субагента), чей мостик-
# `>`-блок заканчивается знаком вопроса («...в каждой сессии её приходится
# объяснять заново?») — `quote_role()` ловит это первым правилом («тело
# кончается на ?» → роль `question`) и рисует его золотой кремовой рамкой
# «вопрос залу», хотя после n28 идёт не карточка-ответ, а дивайдер (n29):
# это авторский мостик в следующий блок, а не настоящее голосование. Та же
# коробка у n04/n11/n23/n33/n40/n52/n63 последовательно значит «сейчас
# зал отвечает» — n28 ломал этот язык. Проверено (см. комментарий ниже):
# у остальных пяти `criteria_checklist_and_boundary` мостик не кончается
# вопросом, форма `formula` подбирается автоматически и верно — форсируем
# роль только для n28, точечно.
CRITERIA_QUOTE_ROLE_FORCE = {"n28": "formula"}


def g_criteria(sl, sid, title, blocks, pattern, assertion=""):
    """Граница применимости — таблица на 2 колонки становится двумя плашками
    бок о бок. Перенесено из build_sem05.py без изменений."""
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


def g_closing(sl, sid, title, blocks, pattern, assertion=""):
    """Закрытие — вопрос открытия + сводка под ним. На Семинаре 6 этот жанр
    пока не назначен ни одному приёму словаря: n63 («тот же вопрос второй
    раз») рисуется `g_question` (приём `reflection_question`), а n64 («чем
    занятие кончается») — `g_content` (приём `answer_breakdown_table`).
    Отдельного закрывающего жанра деке не потребовалось. Функция держится
    про запас, как держалась в build_sem05.py — понадобится, если блок
    «Сборка» вырастет слайдом с тем же устройством, что у закрытия Семинара 5
    (вопрос открытия + схема сразу под ним)."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
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
                    sl, p, LEFT, y, WIDTH, mh if mh else 3.2, label=sid))
            continue
        d = block_drawer(kind, b, sid, pattern)
        if d:
            drawers.append(d)
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, slide_number(sid))


# Круг после прожарок (issue 225, P1-3): на n16 фигура (лестница приоритета)
# рисовалась ПЕРВЫМ блоком — глаз сперва читал цветной список, хотя
# заголовок слайда обещает «собранный файл» (код), а лестница — лишь
# компаньон к коду, вторая мысль. Код в блоках источника идёт следом за
# фигурой в `## Visual` слайда, но при фигуре-первой он всегда рисовался
# ПОСЛЕ неё. Для n16 — единственного `code_artifact` с фигурой — фигура
# переносится ПОСЛЕ блоков: код (то, что называет заголовок) читается
# первым, лестница (механика, подпирающая код) — вторым. Больше ни один
# `code_artifact`-слайд фигуры не объявляет (проверено), так что правка не
# трогает остальные жанры.
FIG_AFTER_BLOCKS = {"n16"}

# Круг после прожарок (issue 225, P1-4): «золото ≥1× на слайде» (CLAUDE.md)
# не выполнялось на четырёх repo-state/рекап слайдах — единственная цитата
# на них классифицируется как `quote_role` → «speech» (тихая реплика,
# тиловая полоса), потому что текст начинается с «« и подходящей роли
# «formula»/«fact» в `PATTERN_ROLE` для их приёмов (`code_artifact`,
# `recap_table`, `file_tree_snapshot`, `answer_breakdown_table`) не
# назначено. По содержанию эта цитата — не реплика лектора вразрез по
# ходу, а ЕДИНСТВЕННАЯ подпись-итог слайда (так и названо в их собственном
# `visual.primary`: «единственная подпись слайда») — ровно работа формулы
# (золотая планка), не речи. n64 несёт два `>`-блока; золотой становится
# только ПОСЛЕДНИЙ (короткая строка оси «Четыре строки из пяти…» — тот же
# рефрен, что у n61), первый (длинная рефлексия) остаётся тихой репликой.
#
# Вторая прожарка (issue 225, P1-3): та же дыра на `n05` («Два блока сегодня»,
# приём `lecture_map`) — там `PATTERN_ROLE["lecture_map"] = "fact"` даёт
# тиловую карточку для ЛЮБОЙ цитаты этого приёма независимо от «, поэтому
# простое снятие кавычек (которое чинит `recap_table`-слайды вроде n03, где
# роль по умолчанию не назначена вовсе) здесь не работает — нужен тот же
# точечный `role="formula"`, что у четвёрки выше. Цитата n05 — та же работа:
# единственная подпись-итог карты занятия, не реплика лектора.
GOLD_QUOTE_SIDS = {"n02": "all", "n05": "all", "n61": "all", "n62": "all", "n64": "last"}


def g_content(sl, sid, title, blocks, pattern, assertion=""):
    """Содержательный слайд по умолчанию: заголовок-утверждение, схема (если
    объявлена), блоки в порядке источника. Это жанр для БОЛЬШИНСТВА приёмов
    словаря Семинара 6 (`visual.pattern`) — `problem_scenario`,
    `answer_breakdown_table`, `cobuilding_config_reveal`, `code_artifact`,
    `file_tree_snapshot`, `mechanics_table`, `mechanics_with_figure`,
    `failure_vignette`, `failure_vignette_table`, `evidence_table_with_gap`,
    `lecture_map` — ни один из них не отличается композицией настолько, чтобы
    заслужить отдельную функцию; различие между ними живёт в типе блоков
    (таблица / код / цитата) и в роли, которую даёт `PATTERN_ROLE`/текст."""
    K.set_bg(sl, K.WHITE)
    y0 = K.auto_header(sl, title)
    drawers = []
    fig = figure_for(sid)
    fig_after = bool(fig) and sid in FIG_AFTER_BLOCKS
    # Потолок высоты схемы. `K.FIG_NATURAL_H` (4,3″) стоит затем, чтобы схема не
    # съедала содержательный слайд, где кроме неё есть блоки текста. Если блоков
    # нет вовсе — одностраничник, где вся работа слайда ВНУТРИ схемы, — съедать
    # нечего, и потолок становится просто полосой пустоты под схемой: n09 и n31
    # упирались в него и оставляли ≈1,5″ неиспользованного полотна, а подписи на
    # них читались с экрана как 5–6 pt. Сведение круга 2 (issue 225, замечание
    # владельца по одностраничнику: «текст мелкий — укрупнить, место сверху и
    # снизу есть») отдаёт такой схеме всю доступную высоту.
    fig_ceiling = (BOTTOM - y0) if not blocks else K.FIG_NATURAL_H
    if fig and not fig_after:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, LEFT, y, WIDTH, mh if mh else fig_ceiling, label=sid))
    gold_rule = GOLD_QUOTE_SIDS.get(sid)
    quote_total = sum(1 for k, _ in blocks if k == "quote") if gold_rule == "last" else 0
    quote_i = -1
    for kind, b in blocks:
        if kind == "table" and pattern == "evidence_table_with_gap":
            # таблица свидетельств — свой акцент: взвешивает, не выбирает
            drawers.append(lambda sl, y, mh, h_=b[0], r_=b[1]: K.table_card(
                sl, LEFT, y, WIDTH, h_, r_, max_h=mh, accent=K.MID, highlight={},
                label=f"{sid} свидетельства"))
            continue
        role = None
        if kind == "quote" and gold_rule:
            quote_i += 1
            if gold_rule == "all" or (gold_rule == "last" and quote_i == quote_total - 1):
                role = "formula"
        d = block_drawer(kind, b, sid, pattern, role=role)
        if d:
            drawers.append(d)
    if fig_after:
        drawers.append(lambda sl, y, mh, p=fig: K.figure(
            sl, p, LEFT, y, WIDTH, mh if mh else K.FIG_NATURAL_H, label=sid))
    compose(sl, sid, y0, drawers)
    K.slide_number_mark(sl, slide_number(sid))


TRACK_LABELS = ("база", "кромка")


def g_base_edge(sl, sid, title, blocks, pattern, assertion=""):
    """Такт Б — база и кромка на одном экране. Перенесено из build_sem05.py
    без изменений (приём документирован в RENDERER-NOTES.md сем. 5, раздел
    «Такт Б — приём base_and_edge» — та же разметка `.md`, та же норма текста)."""
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


# ── Словарь приёмов Семинара 6 ───────────────────────────────────────────────
#
# Ключи — `visual.pattern` (НЕ `type`, см. комментарий у `PATTERN_ROLE` выше).
# Семь явных входов — жанры, у которых композиция отличается от стандартного
# содержательного слайда; таблица сверена с фактическим словарём написанных
# слайдов (18 уникальных значений `visual.pattern`, см. там же). Всё
# остальное (`problem_scenario`, `answer_breakdown_table`,
# `cobuilding_config_reveal`, `code_artifact`, `file_tree_snapshot`,
# `mechanics_table`, `mechanics_with_figure`, `failure_vignette`,
# `failure_vignette_table`, `evidence_table_with_gap`, `lecture_map`) падает в
# `g_content` по умолчанию — ровно как в build_sem05.py падали туда все
# приёмы без собственной записи в GENRE_FN.
GENRE_FN = {
    "hero_cover": g_cover,
    "section_divider_macro": g_divider,
    "question_with_option_cards": g_question,
    "reflection_question": g_question,
    "recap_table": g_axis_table,
    "criteria_checklist_and_boundary": g_criteria,
    "base_and_edge": g_base_edge,
}


# ── Сборка ──────────────────────────────────────────────────────────────────

def refresh_manifest():
    """Пересобрать манифест ТЕКУЩЕГО языка из его слайдов перед сборкой — и
    СКАЗАТЬ, если он разошёлся (тот же контракт, что в build_sem05.py —
    манифест производное, правят слайд, а не этот файл).

    Язык здесь несущий: при `--lang en` пересобирается `deck.en.yaml` из
    `slides-en/`, а русский `deck.yaml` не читается и не пишется вовсе. Иначе
    английская сборка освежала бы ЧУЖОЙ манифест и собиралась бы по своему,
    несвежему."""
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
    """Список слайдов блока, собранный ИЗ САМИХ ФАЙЛОВ, минуя `deck.yaml`.

    Пока блоки деки пишутся параллельными сессиями, `deck.yaml` может ещё не
    знать части из них — это режим ПРЕДПРОСМОТРА БЛОКА (`--block n`), не
    вторая дека: порядок — по `id`."""
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


USAGE = """build_sem06.py — сборка деки Семинара 6.

  --block nNN   ПРЕДПРОСМОТР одного слайда или группы: строит из файлов на
                диске в отдельный `sem-06-nNN.pptx`. Безопасно при
                параллельной работе: `deck.yaml` и `rendered/sem-06.pptx`
                не трогает.
  --all         ПОЛНАЯ пересборка: пересобирает `deck.yaml` из слайдов и
                перезаписывает `rendered/sem-06.pptx`. Общие файлы, то есть
                ход сведения, а не проверка своей зоны.
  --deck F      собрать по другому манифесту (в `sem-06-F.pptx`).
  nNN nMM …     собрать полотно только этих слайдов, остальные страницы
                оставить пустыми (отладка вёрстки).
  --lang en     собирать АНГЛИЙСКУЮ деку: слайды `slides-en/`, манифест
                `deck.en.yaml`, выход `sem-06-en.pptx`, и — главное — реплика
                опознаётся по `"`, а не по «ёлочке» (см. `LANG_SIGNALS`).
                Русскую деку и русский манифест при этом не трогает ничем.
  --quote-roles НИЧЕГО НЕ СОБИРАЕТ И НЕ ПИШЕТ: печатает, какую роль получит
                каждый блок-цитата деки. С `--lang en` — то же по английской.
                Нужно, чтобы сверить роли двух дек ДО рендера: роли обязаны
                совпасть слайд в слайд, иначе язык меняет не текст, а вёрстку.

Полная пересборка требует ЯВНОГО `--all` и без него не запускается. Так
решено после круга 2 замечаний владельца (issue 225): четыре сессии круга
независимо запустили полную пересборку, набрав `--help` или перепутав флаг,
и перезаписали общую деку — расплата за то, что «ничего не передано» значило
«сделай самое разрушительное».
"""


def print_quote_roles(only):
    """Какую роль получит каждый блок-цитата — БЕЗ сборки и без записи файлов.

    Зачем отдельный режим, а не «собери и посмотри глазами»: роль видна на
    картинке цветом полосы, то есть проверяется рендером, PDF и просмотром
    64 снимков. Между языками сверять надо не картинку, а решение, и решение
    печатается здесь одной строкой на блок. Несколько реплик на деке вообще
    не на всех слайдах — глазами их пересчитывать дороже, чем прочесть список.

    Контракт для EN-деки: набор ролей обязан СОВПАСТЬ с русским слайд в слайд.
    Расхождение значит, что язык поменял не текст, а вёрстку, — и это дефект
    независимо от того, какая из двух раскрасок красивее."""
    deck_path = ROOT / DECK_FILE[LANG]
    if deck_path.exists():
        slides = yaml.safe_load(deck_path.read_text(encoding="utf-8"))["slides"]
    else:
        slides = deck_from_files("n")
    tally, total = {}, 0
    for sv in slides:
        sid = sv["id"]
        if only and sid not in set(only):
            continue
        pattern = (sv.get("visual") or {}).get("pattern", "")
        _t, _a, visual, _n = SP.sections((ROOT / sv["file"]).read_text(encoding="utf-8"))
        for kind, b in SP.blocks(visual):
            if kind != "quote":
                continue
            role = quote_role(b, pattern)
            if GOLD_QUOTE_SIDS.get(sid) == "all":
                role += " (+gold по GOLD_QUOTE_SIDS)"
            head = K.plain(" ".join(b))[:58]
            tally[role.split(" ")[0]] = tally.get(role.split(" ")[0], 0) + 1
            total += 1
            print(f"{sid}  {pattern:28} {role:30} {head}…")
    print(f"\nязык: {LANG}   знак реплики: {' / '.join(SPEECH_OPEN)}   "
          f"блоков-цитат: {total}")
    for r, v in sorted(tally.items()):
        print(f"  {r:10} {v:3}")
    return 0


def main():
    argv = list(sys.argv[1:])
    if {"--help", "-h", "help"} & set(argv):
        print(USAGE)
        return
    unknown = [a for a in argv if a.startswith("-")
               and a not in ("--block", "--deck", "--all", "--lang", "--quote-roles")]
    if unknown:
        print(f"неизвестный флаг: {' '.join(unknown)}\n")
        print(USAGE)
        raise SystemExit(2)
    if "--lang" in argv:
        i = argv.index("--lang")
        set_lang(argv[i + 1] if i + 1 < len(argv) else "")
        del argv[i:i + 2]
    if "--quote-roles" in argv:
        argv.remove("--quote-roles")
        return print_quote_roles(argv)
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
        out_name = f"sem-06-{block}.pptx" if LANG == "ru" else f"sem-06-en-{block}.pptx"
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
            # Самая первая сборка этого занятия: манифеста ещё не существует
            # вовсе (не «устарел», а именно отсутствует — в Семинаре 5 этот
            # путь никогда не исполнялся, там deck.yaml существовал с первого
            # дня). `refresh_manifest()` ниже создаст его из слайдов; здесь
            # достаточно пустого списка, чтобы не упасть раньше срока.
            slides = []
        else:
            raise SystemExit(f"файла «{deck_file}» нет — и это не deck.yaml, "
                             f"чтобы пересобрать его автоматически")
        out_name = OUT_NAME[LANG] if deck_file == DECK_FILE[LANG] else \
            f"sem-06-{Path(deck_file).stem}.pptx"
    deck = {"slides": slides}
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(K.W_IN), Inches(K.H_IN)
    blank = prs.slide_layouts[6]
    M.reset()
    if not block and deck_file == DECK_FILE[LANG]:
        refresh_manifest()
        slides = yaml.safe_load((ROOT / deck_file).read_text(encoding="utf-8"))["slides"]
        # `deck["slides"]` был снят СО СТАРОГО чтения (строка выше, до
        # пересборки манифеста) — на бутстрапе этого занятия старое чтение
        # пустое (deck.yaml ещё не существовал), и цикл сборки ниже без этой
        # строки прошёл бы по ПУСТОМУ списку, молча сохранив пустую
        # презентацию, пока аудиты (которые читают `slides` напрямую, не
        # `deck["slides"]`) честно отчитались бы по полному манифесту. Тот же
        # код в build_sem05.py несёт тот же дефект — там он ЛАТЕНТНЫЙ
        # (deck.yaml там никогда не отсутствовал целиком, второе чтение
        # всегда давало тот же список, что первое), здесь — живой, поймано
        # первым прогоном полной сборки на этом занятии.
        deck["slides"] = slides

    only = set(argv)
    built = 0
    for s in deck["slides"]:
        sid = s["id"]
        pattern = (s.get("visual") or {}).get("pattern", "")
        md = (ROOT / s["file"]).read_text(encoding="utf-8")
        title, _assertion, visual, notes = SP.sections(md)
        sl = prs.slides.add_slide(blank)
        if not only or sid in only:
            fn = GENRE_FN.get(pattern, g_content)
            kw = {"meta": s.get("visual")} if fn is g_divider else {}
            fn(sl, sid, title or sid, SP.blocks(visual), pattern, _assertion, **kw)
        audit_question_answer(sid, pattern, SP.blocks(visual))
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
