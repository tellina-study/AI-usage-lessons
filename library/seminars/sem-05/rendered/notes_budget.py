#!/usr/bin/env python3
"""Замер заметки по контракту круга 4: речь 120–180 слов, справка 180–270.

Зачем отдельный файл. `AUTHOR-BRIEF.md` §3 п. 9 после круга 4 мерит заметку ДВУМЯ
числами, а не одним, и в хронометраж слайда входит ТОЛЬКО речевая часть. Ни одна
проверка в `rendered/` этого не считает: `metrics.py` мерит текст на слайде,
`audit_grammar.py` — формы. Отчёт «заметка выросла» без разделения частей
неотличим от отчёта «заметка стала длиннее нормы».

Граница частей берётся из самой деки, а не назначается заново: справка в этой
деке начинается с оборота «Если спросят…» (так её написала сессия механики на
`n08`/`n12`). Первый абзац, начинающийся с этого оборота, и есть шов.

    python3 notes_budget.py ../slides/n4*.md ../slides/n5*.md
    python3 notes_budget.py --self-test

`--self-test` гоняет проверку на нарочно сломанном входе: заметка без справки,
заметка с пустой речью, заметка, где справка на месте, но речь вдвое длиннее
нормы. Проверка, которая на них молчит, — мёртвая.
"""
import re
import sys
from pathlib import Path

SPEECH_MIN, SPEECH_MAX = 120, 180
WPM = 130               # темп, которым меряет AUTHOR-BRIEF §3 п. 9
QUESTION_MIN, QUESTION_MAX = 60, 100   # на слайде вопроса говорит зал
                        # (AUTHOR-BRIEF §3 п. 9, исключение названо явно)
REF_MIN, REF_MAX = 180, 270
SEAM = re.compile(r"^\**Если спросят", re.I)


def is_question(md: str) -> bool:
    return bool(re.search(r"(?m)^type:\s*reflection_question\s*$", md))


def slot_min(md: str):
    """`duration_min` из фронтматтера — слот слайда в минутах."""
    m = re.search(r"(?m)^duration_min:\s*([0-9.]+)\s*$", md)
    return float(m.group(1)) if m else None


def notes_of(md: str) -> str:
    m = re.search(r"(?ms)^##\s+Speaker notes\s*$(.*)", md)
    return m.group(1).strip() if m else ""


def split_parts(notes: str):
    """(речь, справка) — шов на первом абзаце, начинающемся с «Если спросят»."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", notes) if p.strip()]
    for i, p in enumerate(paras):
        if SEAM.match(p.lstrip("*_ ")):
            return paras[:i], paras[i:]
    return paras, []


def words(paras) -> int:
    txt = " ".join(paras)
    txt = re.sub(r"[*_`>]", " ", txt)
    return len(re.findall(r"[^\W\d_]+(?:-[^\W\d_]+)*", txt, re.UNICODE))


def check(path: Path):
    title = path.stem
    md = path.read_text(encoding="utf-8")
    sp, rf = split_parts(notes_of(md))
    ws, wr = words(sp), words(rf)
    slot = slot_min(md)
    bad = []
    # Слот — потолок жёстче словесного: на дивайдере в 0,50 мин 120 слов
    # физически не произносятся. Поэтому верх коридора берётся как минимум
    # из нормы и того, что помещается в слот на темпе 130 слов/мин.
    lo = QUESTION_MIN if is_question(md) else SPEECH_MIN
    hi = QUESTION_MAX if is_question(md) else SPEECH_MAX
    cap = hi if slot is None else min(hi, int(slot * WPM))
    if slot is not None and ws > slot * WPM:
        bad.append(f"речь {ws} сл. = {ws / WPM:.2f} мин при слоте {slot:.2f}")
    if not rf:
        bad.append("справки нет вовсе")
    if ws > cap and not (slot is not None and ws > slot * WPM):
        bad.append(f"речь {ws} вне {lo}–{cap}")
    # Когда связывает слот (cap < lo), нижняя граница — доля слота, а не сам
    # cap: требовать попадания В САМЫЙ потолок значит ловить расхождение в одно
    # слово. Смысл нижней границы — «слот занят речью, а не молчанием».
    floor = lo if cap >= lo else int(cap * 0.85)
    if ws < floor:
        bad.append(f"речь {ws} ниже {floor}")
    if rf and not (REF_MIN <= wr <= REF_MAX):
        bad.append(f"справка {wr} вне {REF_MIN}–{REF_MAX}")
    return title, ws, wr, bad


SELF_TEST = {
    "сломан: справки нет": "## Speaker notes\n\n" + ("слово " * 150),
    "сломан: речь пустая": "## Speaker notes\n\nЕсли спросят, что это — " + ("слово " * 200),
    "сломан: речь вдвое длиннее": ("## Speaker notes\n\n" + "слово " * 360
                                   + "\n\nЕсли спросят, что это — " + "слово " * 200),
    "годный": ("## Speaker notes\n\n" + "слово " * 150
               + "\n\nЕсли спросят, что это — " + "слово " * 200),
}


def self_test():
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as d:
        for name, md in SELF_TEST.items():
            p = Path(d) / (re.sub(r"\W+", "-", name) + ".md")
            p.write_text(md, encoding="utf-8")
            _, ws, wr, bad = check(p)
            caught = bool(bad)
            want = not name.startswith("годный")
            mark = "✓" if caught == want else "✗ ПРОВЕРКА МЁРТВАЯ"
            if caught != want:
                ok = False
            print(f"{mark} {name:30} речь={ws:4} справка={wr:4}  → {'; '.join(bad) or 'чисто'}")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--self-test":
        return self_test()
    worst = 0
    for a in args:
        title, ws, wr, bad = check(Path(a))
        mark = "⚠" if bad else "·"
        if bad:
            worst = 1
        print(f"{mark} {title[:44]:44} слот={slot_min(Path(a).read_text(encoding='utf-8')) or 0:.2f} "
              f"речь={ws:4} ({ws / WPM:.2f} мин) справка={wr:4}  {'; '.join(bad)}")
    return worst


if __name__ == "__main__":
    sys.exit(main())
