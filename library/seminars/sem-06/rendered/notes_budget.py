#!/usr/bin/env python3
"""Замер заметки по контракту круга 4: речь 120–180 слов, справка 180–270.

Зачем отдельный файл. `AUTHOR-BRIEF.md` §3 п. 9 после круга 4 мерит заметку ДВУМЯ
числами, а не одним, и в хронометраж слайда входит ТОЛЬКО речевая часть. Ни одна
проверка в `rendered/` этого не считает: `metrics.py` мерит текст на слайде,
`audit_grammar.py` — формы. Отчёт «заметка выросла» без разделения частей
неотличим от отчёта «заметка стала длиннее нормы».

Граница частей берётся из самой деки, а не назначается заново — и ШВОВ В ЭТОЙ
ДЕКЕ ДВА, а не один. Большинство слайдов (58 из 68) открывают справку оборотом
«Если спросят…» — так её написала сессия механики на `n08`/`n13`. Остальные
десять — слайды рамки и закрытия — отбивают справку явной чертой `---` и
заголовком `**Справка.**`, а оборот «Если спросят» стоит в них НЕ первым
абзацем справки, а где-то в середине.

Пока проверка знала только второй шов, на этих десяти она резала заметку не по
той границе: заголовок справки и все абзацы `*Про …*` до первого «Если спросят»
попадали в РЕЧЬ. Отсюда брались приговоры вида «речь 223 слова = 1,72 мин при
слоте 0,75» на `n01`, где произносимая часть — 72 слова и написана короткой
намеренно (сам слайд это и говорит: «речевая часть короче ста двадцати слов
намеренно»). На `n04`, `n67` и `n10` та же слепота давала ещё и «справки нет
вовсе» при полной справке на экране. Десять слайдов из десяти меняют приговор,
когда шов опознан верно, — то есть проверка измеряла не то, что обещала.

Поэтому швы ищутся ПО ОЧЕРЕДИ: сначала явный (`---` / `**Справка.**`), и только
если его нет — оборотный. Порядок важен: на слайде с обоими маркерами явный
стоит раньше, и взять оборотный значило бы снова отдать половину справки речи.

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
# Явный шов: горизонтальная черта или заголовок справки отдельным абзацем.
# Он сильнее оборотного и проверяется первым — см. преамбулу.
SEAM_EXPLICIT = re.compile(r"^(?:---+|\**Справка\.?\**)\s*$")


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
    """(речь, справка). Шов ищется в двух видах, явный раньше оборотного.

    Справка начинается С САМОГО ШВА, а не после него: `**Справка.**` — её
    заголовок и считается её словами. Голая черта `---` разметкой не является
    и в счёт не идёт, иначе каждая такая заметка получала бы лишнее слово.
    """
    paras = [p.strip() for p in re.split(r"\n\s*\n", notes) if p.strip()]
    for i, p in enumerate(paras):
        if SEAM_EXPLICIT.match(p.splitlines()[0].strip()):
            tail = paras[i + 1:] if p.strip().strip("-") == "" else paras[i:]
            return paras[:i], tail
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


# Пробы покрывают ОБА шва. Пока их было четыре и все на обороте «Если спросят»,
# проверка молчала про десять слайдов, которые отбивают справку чертой: на них
# она резала заметку не по той границе и приговаривала к переполнению речь,
# написанную ровно по норме. Проба на явный шов (ниже, «справка за чертой»)
# красная на прежнем коде: он уводил заголовок справки и первый абзац `*Про …*`
# в речь, и 150-словная речь приходила 196-словной.
_SPRAVKA_TAIL = ("\n\n---\n\n**Справка.**\n\n*Про запас.* " + "слово " * 40
                 + "\n\nЕсли спросят, что это — " + "слово " * 150)

SELF_TEST = {
    "сломан: справки нет": "## Speaker notes\n\n" + ("слово " * 150),
    "сломан: речь пустая": "## Speaker notes\n\nЕсли спросят, что это — " + ("слово " * 200),
    "сломан: речь вдвое длиннее": ("## Speaker notes\n\n" + "слово " * 360
                                   + "\n\nЕсли спросят, что это — " + "слово " * 200),
    "годный": ("## Speaker notes\n\n" + "слово " * 150
               + "\n\nЕсли спросят, что это — " + "слово " * 200),
    # ── явный шов ───────────────────────────────────────────────────────────
    "годный: справка за чертой": "## Speaker notes\n\n" + "слово " * 150 + _SPRAVKA_TAIL,
    "сломан: за чертой речь длинна": ("## Speaker notes\n\n" + "слово " * 360
                                      + _SPRAVKA_TAIL),
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
