"""Сборочные аудиты: что проверяется на каждой сборке деки.

Правило канона (`tools/seminar-production/README.md` §7): свойство
проверяется ЗАМЕРОМ, а не взглядом, и замер печатается при сборке — иначе
его не запускают. Здесь живут проверки, которые имеют смысл только в момент
сборки (им нужен манифест и файлы слайдов рядом); сторожа по уже собранной
деке — отдельные скрипты (`audit_sluzhebnoe.py`, `audit_sopostavleniya.py`,
`check_text_overlap_pdf.py`, `check_tracks_pdf.py`).

Ни один аудит не падает и ничего не исправляет: он добавляет предупреждение
в `metrics._WARNINGS`, и `build.py` печатает их все одним списком. Сборка,
которая отказывается собираться из-за находки, перестаёт давать деку, по
которой находку видно.
"""

import re

import deck_config as D
import deck_kit as K
import genres
import metrics as M
from roles import quote_role, split_question

# Блок, который нельзя ставить под вопросом залу: он и есть ответ.
ANSWER_KINDS = {"table", "code", "bullets"}
ANSWER_ROLES = {"formula", "fact", "caveat"}


def audit_question_answer(sid, pattern, blocks):
    """Разбор идёт СЛЕДУЮЩИМ экраном, а не ниже и не мельче (правило А1).

    Дивайдеры исключены: у них другая грамматика — риторический вопрос в
    заголовке перехода не голосование, и разбор ему не положен. Без
    исключения аудит срабатывал на каждом дивайдере, чей заголовок
    случайно кончается на «?»."""
    if pattern in D.divider_patterns():
        return
    qi = None
    for i, (kind, b) in enumerate(blocks):
        if kind != "quote":
            continue
        if quote_role(b, pattern) == "question" or (
                pattern in D.vote_patterns() and split_question(b)[2]):
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


def audit_takty_keysa(slides, cfg):
    """Порядок тактов кейса: дивайдер → СЦЕНА → вопрос → разбор.

    Этот порядок записан в каноне (`tools/seminar-production/README.md` §3)
    с круга 4 Семинара 5 — и Семинар 7 от него отступил: четыре круга дека
    шла дивайдер → вопрос, без сцены. Владелец (2026-10-12): «почему ты в
    кейсах не используешь тот же формат, который был в предыдущих семинарах
    — слайд описание, слайд вопрос с вариантами (без протечек), разбор
    вариантов и дальше пошли детали».

    Цена отступления: зал спрашивают до того, как он что-то потерял. Правило
    было записано словами и не держалось; поэтому здесь оно проверяется
    машиной, а не памятью автора.

    Проверяется ровно три вещи, и ни одна не про содержание:
      1. за дивайдером кейса идёт сцена (`problem_scenario`);
      2. за сценой — вопрос;
      3. за вопросом — разбор (это уже проверяет `audit_question_answer`,
         здесь только порядок экранов, не их наполнение).
    """
    divs = set(cfg.get("divider_patterns") or ("case_divider_quote",))
    scenes = {"problem_scenario"}
    questions = set(cfg.get("question_patterns") or ()) or {
        "question_with_option_cards", "reflection_question", "guess_the_number"}
    seq = [(s["id"], (s.get("visual") or {}).get("pattern")) for s in slides]
    for i, (sid, pat) in enumerate(seq):
        if pat not in divs:
            continue
        after = seq[i + 1:i + 3]
        if not after or after[0][1] not in scenes:
            got = after[0][1] if after else "ничего"
            M._WARNINGS.append(
                f"НЕТ СЦЕНЫ [{sid}]: за дивайдером кейса идёт «{got}», а по "
                f"грамматике кейса (канон §3) обязана идти сцена — живая "
                f"постановка: кто, что делает, что ломается и чего это стоит. "
                f"Без неё зал спрашивают до того, как он что-то потерял")
            continue
        if len(after) > 1 and after[1][1] not in questions:
            M._WARNINGS.append(
                f"ПОСЛЕ СЦЕНЫ НЕ ВОПРОС [{after[0][0]}]: идёт "
                f"«{after[1][1]}» — порядок тактов канона §3: "
                f"дивайдер → сцена → вопрос → разбор")


def audit_numbering(slides):
    """Номер в углу обязан выводиться из ПОРЯДКА слайда в манифесте. Своё
    число во фронтматтере расходится с порядком молча — а именно по нему
    зал и ведущий ищут слайд вслух."""
    ids = [s["id"] for s in slides]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        M._WARNINGS.append(
            f"НОМЕР ДВАЖДЫ [{', '.join(dup)}]: идентификатор стоит в деке "
            f"больше одного раза — слайды получат один и тот же номер")
    off = []
    for pos, sid in enumerate(ids, 1):
        got = D.slide_number(sid)
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
    """Ссылка служебного поля на слайд, которого в деке нет. Такие остаются
    после каждой пересборки нумерации, и найти их глазами нельзя: полей
    порядка тысячи."""
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
    """Схема объявлена, а дойти до слайда не может. Три способа потерять её
    молча: файла нет, приём её не рисует, или она объявлена дважды."""
    by_id = {s["id"]: s for s in slides}
    figs = D.figs()
    for sid, slide in by_id.items():
        meta = slide.get("visual") or {}
        fn = meta.get("figure")
        if fn and sid in figs:
            M._WARNINGS.append(
                f"СХЕМА ДВАЖДЫ [{sid}]: объявлена и слайдом («{fn}»), и таблицей "
                f"FIGS («{figs[sid]}») — уберите запись из таблицы, слайд главнее")
        if not fn:
            continue
        if not (D.FIGDIR / fn).exists():
            M._WARNINGS.append(f"НЕТ СХЕМЫ [{sid}]: слайд объявляет «{fn}», файла нет "
                               f"— слайд соберётся без иллюстрации")
        if not genres.draws_figure(meta.get("pattern", "")):
            M._WARNINGS.append(
                f"СХЕМА НЕ ДОЙДЁТ [{sid}]: слайд объявляет «{fn}», но приём "
                f"«{meta.get('pattern','')}» схему не рисует — не сработает никогда")
    for sid, fn in sorted(figs.items()):
        if sid not in by_id:
            M._WARNINGS.append(f"МЁРТВАЯ ЗАПИСЬ FIGS [{sid}]: «{fn}» — такого "
                               f"слайда в деке нет")


def audit_figure_text():
    """Подписи ВНУТРИ схем — пиксели, и греп по собранной деке даёт по ним
    ноль независимо от того, что там написано (канон §7). Поэтому строки
    читаются из ИСХОДНИКОВ рисовалок (`make_figures*.py` этого занятия),
    разбором синтаксического дерева, а не грепом: докстринги рисовалки —
    не подписи на схеме, и смешивать их нельзя."""
    import ast
    c = K.Claims()
    for f in sorted(D.HERE.glob("make_figures*.py")):
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
