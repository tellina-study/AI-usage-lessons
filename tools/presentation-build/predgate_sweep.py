#!/usr/bin/env python3
"""Pre-USER-GATE sweep по СОБРАННОМУ pptx — независимая проверка оркестратора.

Читает видимый слой и заметки прямо из .pptx (не из исходных .md), потому что
правило Pre-USER-GATE Walkthrough требует проверять то, что увидит студент,
а не то, что написал агент. Самоотчёт субагента «TOTAL=0» не принимается.

Запуск:  python3 tools/presentation-build/predgate_sweep.py <deck.pptx>

Выход: по группе на проверку, каждое совпадение — с номером кадра и контекстом.
Код возврата 1, если есть хоть одно совпадение в блокирующих группах.
"""
import re
import sys
from pathlib import Path

from pptx import Presentation

# ── 1. Строительные леса (Pre-USER-GATE §5, группа 1) ────────────────────────
SCAFFOLD = [
    (r"Лектору", "обращение к лектору"),
    (r"Преподавател", "обращение к преподавателю"),
    (r"Вы здесь", "маркер навигации"),
    (r"\[VERIFY-DAY-OF\]|\[VFY[^\]]*\]|\[FACT-CHECK\]", "рабочий маркер"),
    (r"\bLO[1-9][a-z]?\b", "код учебной цели"),
    (r"§\s?[0-9]", "ссылка на параграф"),
    (r"→\s?s[0-9]+|\(s[0-9]{2}\)", "ссылка на номер кадра"),
    (r"точк\w*\s+возврата", "точка возврата"),
    # «— в главе» снято: s07 этим ОБЪЯВЛЯЕТ, чего в деке нет (BRIEF-DEKA §9).
    (r"в материалах лекции", "отсылка к материалам"),
    (r"это payoff|возвращаемся\s+[0-9N]|не вводи\w*\s+нов", "сценарные ремарки"),
    (r"course-scaffold", "служебный маркер"),
    # дефект 1 из BRIEF-DEKA §13: внутреннее имя файла протекло в подвал
    (r"chapter[-\w]*\.md|PLAN-[0-9]|REESTR|DECK-KARTA|BRIEF-DEKA|research/R[0-9]",
     "внутреннее имя файла на кадре"),
]

# ── 2. Тайминг ЛЕКЦИИ (ENFORCED: заметки НЕ освобождены, только speech.md) ───
# Важно: длительности ВНУТРИ материала — не нарушение. «1–2 минуты записи для
# копии голоса», «обучение 41 мин 33 с», «укладка в длительность реплики» — это
# измерения предмета. Запрещён тайминг САМОГО занятия: сколько идёт раздел,
# сколько длится лекция, сколько отведено на вопросы.
TIMING = [
    (r"\([0-9]+[–\-]?[0-9]*\s*мин[^)]{0,10}\)", "минуты в скобках — разметка хода"),
    (r"[0-9]+\s*мин[а-я]*\s*[·|]", "минуты в служебной полосе"),
    (r"(раздел|блок|часть|лекци\w+|занятие)\w*\s*[—:-]?\s*[0-9]+\s*мин", "минуты раздела"),
    (r"[0-9]+\s*мин[а-я]*\s+на\s+(вопрос|обсужд|Q)", "минуты на вопросы"),
    (r"Время раздел|Тайминг раздел|Длительность раздел|Длительность лекц", "слово о тайминге"),
    (r"⏱|⏰", "значок часов"),
]

# ── 3. Методические комментарии ──────────────────────────────────────────────
METHOD = [
    (r"(методическ|педагогическ)\w*", "методический комментарий"),
    (r"На этом этапе студент|Здесь студент усваивает", "обращение про студента"),
    (r"Зачем это в Лекции|Этот раздел учит", "объяснение замысла"),
    (r"главный методический пункт|методическ\w+ (рамка|ценность|значимость)", "мета-рамка"),
]

# ── 4. Формат сопоставления (литературный запрет) ────────────────────────────
SOPOST = [
    (r"\bне\s+[^,.;:!?]{1,40},\s*а\s+", "«не X, а Y»"),
    (r"дело не в\s+[^,.;]{1,40},\s*(а\s+)?в\s+", "«дело не в X, а в Y»"),
    (r"с одной стороны", "«с одной стороны»"),
]

# ── 5. Научная запись и сдвоенные числа ──────────────────────────────────────
NUMBERS = [
    (r"[0-9]\s*[·x×]\s*10[\^⁰¹²³⁴⁵⁶⁷⁸⁹]", "научная запись"),
    (r"[0-9]+[eE][+-][0-9]+", "научная запись"),
]

GROUPS = [
    ("ЛЕСА", SCAFFOLD, True),
    ("ТАЙМИНГ", TIMING, True),
    ("МЕТОДОЛОГИЯ", METHOD, True),
    ("НАУЧНАЯ ЗАПИСЬ", NUMBERS, True),
    ("СОПОСТАВЛЕНИЕ", SOPOST, False),  # литературное, не блокирующее
]


def shape_texts(shape):
    """Весь текст фигуры, включая таблицы и группы."""
    out = []
    if shape.shape_type == 6:  # GROUP
        for sub in shape.shapes:
            out.extend(shape_texts(sub))
        return out
    if getattr(shape, "has_text_frame", False):
        for para in shape.text_frame.paragraphs:
            t = "".join(r.text for r in para.runs)
            if t.strip():
                out.append(t)
    if getattr(shape, "has_table", False):
        for row in shape.table.rows:
            for cell in row.cells:
                t = cell.text
                if t.strip():
                    out.append(t)
    return out


def collect(pptx_path):
    prs = Presentation(pptx_path)
    frames = []
    for i, slide in enumerate(prs.slides, start=1):
        visible = []
        for sh in slide.shapes:
            visible.extend(shape_texts(sh))
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text
        frames.append((i, "\n".join(visible), notes))
    return frames


def main():
    if len(sys.argv) < 2:
        sys.exit("укажи путь к .pptx")
    path = Path(sys.argv[1])
    frames = collect(path)
    print(f"Кадров в файле: {len(frames)}\n")

    blocking_total = 0
    for gname, patterns, blocking in GROUPS:
        hits = []
        for num, visible, notes in frames:
            for where, text in (("кадр", visible), ("заметки", notes)):
                for pat, label in patterns:
                    for m in re.finditer(pat, text, re.IGNORECASE):
                        a = max(0, m.start() - 45)
                        b = min(len(text), m.end() + 45)
                        ctx = text[a:b].replace("\n", " ")
                        hits.append((num, where, label, ctx))
        mark = "БЛОКИРУЕТ" if blocking else "литературное"
        print(f"── {gname} ({mark}): {len(hits)}")
        for num, where, label, ctx in hits[:60]:
            print(f"   s{num:02d} [{where}] {label}: …{ctx}…")
        if len(hits) > 60:
            print(f"   … ещё {len(hits) - 60}")
        print()
        if blocking:
            blocking_total += len(hits)

    # ── 6. Заметки: 500–800 слов на кадр (лекция) ────────────────────────────
    print("── ОБЪЁМ ЗАМЕТОК")
    short, empty = [], []
    for num, _, notes in frames:
        w = len(notes.split())
        if w == 0:
            empty.append(num)
        elif w < 150:
            short.append((num, w))
    print(f"   кадров без заметок: {len(empty)} {empty if empty else ''}")
    print(f"   заметки короче 150 слов: {len(short)}")
    for num, w in short[:40]:
        print(f"   s{num:02d}: {w} слов")
    print()

    # ── 7. База у измеримых утверждений — выборка для глаз ───────────────────
    print("── ИЗМЕРИМЫЕ УТВЕРЖДЕНИЯ НА КАДРАХ (проверить базу глазами)")
    unit = re.compile(r"[0-9][0-9  ,.]*\s*(%|\$|₽|раз|кратно|процент\w*|млн|млрд|тыс)")
    cnt = 0
    for num, visible, _ in frames:
        for m in unit.finditer(visible):
            a = max(0, m.start() - 60)
            b = min(len(visible), m.end() + 60)
            print(f"   s{num:02d}: …{visible[a:b]}…".replace("\n", " "))
            cnt += 1
            if cnt > 50:
                break
        if cnt > 50:
            break
    print()

    # ── 8. Ссылки обязаны быть ссылками ──────────────────────────────────────
    # Правило формы подачи: источник на кадре и каждый URL в заметках — живая
    # гиперссылка (run.hyperlink.address). Проверяется по r:id в XML, потому
    # что покрашенный синим текст выглядит на снимке точно так же.
    print("── ГИПЕРССЫЛКИ")
    import zipfile
    with zipfile.ZipFile(path) as z:
        slide_xml = [n for n in z.namelist()
                     if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        with_link = 0
        for n in slide_xml:
            if b"r:id" in z.read(n) and b"hlinkClick" in z.read(n):
                with_link += 1
    # Сравнивать надо с числом кадров, ГДЕ АДРЕС ВООБЩЕ ЕСТЬ: источник,
    # названный именем издания без адреса, правилом разрешён, и считать его
    # нарушением значило бы требовать выдумать 88 ссылок.
    src_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    declared = None
    if src_dir and src_dir.is_dir():
        declared = sum(1 for f in src_dir.glob("s*.md")
                       if re.search(r"^source:.*https?://", f.read_text(), re.M))
    if declared is None:
        print(f"   кадров с живой гиперссылкой: {with_link} из {len(slide_xml)}")
        print("   (передай вторым доводом каталог slides/, чтобы сверить с объявленными)")
    else:
        mark = "сходится" if with_link == declared else "← РАСХОЖДЕНИЕ"
        print(f"   адрес объявлен на {declared} кадрах, живая ссылка на {with_link} — {mark}")
    # текст, похожий на адрес, но без ссылки рядом — ловим глазами по выдаче
    plain = []
    for num, visible, notes in frames:
        for m in re.finditer(r"https?://\S+|\b[a-z0-9-]+\.(ru|com|org|net|io)\b", visible):
            plain.append((num, m.group(0)))
    print(f"   адресов в видимом теле кадра (должны быть в подвале): {len(plain)}")
    for num, a in plain[:20]:
        print(f"   s{num:02d}: {a}")
    print()

    print(f"ИТОГО блокирующих совпадений: {blocking_total}")
    return 1 if blocking_total else 0


if __name__ == "__main__":
    sys.exit(main())
