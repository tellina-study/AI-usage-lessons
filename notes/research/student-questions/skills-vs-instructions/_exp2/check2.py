#!/usr/bin/env python3
"""Механическая проверка соблюдения правил R1-R6 дизайн-гайда DG-v1
(issue tellina-study/AI-usage-lessons#217, второй раунд — skills vs instructions).

Проверяет файлы в notes/research/student-questions/skills-vs-instructions/_exp2/out/<ПЛЕЧО>/*.md
(кроме index.md). Запуск из корня репозитория:

    python3 notes/research/student-questions/skills-vs-instructions/_exp2/check2.py
"""
import os
import glob
import re

BASE = "notes/research/student-questions/skills-vs-instructions/_exp2"
OUT = os.path.join(BASE, "out")
ARMS = ["S1", "S2", "P1", "P2", "P3", "N", "F"]

DG_HEADER = "**Design-guide:** DG-v1"
STATES_HEADING = "## Состояния"
STATES_ORDER = ["покой", "наведение", "нажатие", "недоступно"]
SIZES = ["34", "26", "19", "15"]
CONTRAST = "4.8:1"
END_MARKER = "<!-- DG-v1 -->"

TOKENS = ["P-INK", "P-SEA", "P-GOLD"]
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")

# "Канарейки" — правила, формулировку/значения которых нельзя угадать не читая
# документ. R3 (порядок состояний) сюда намеренно не входит — порядок частично
# угадываем по логике UI без чтения гайда.
CANARY_KEYS = ["R1", "R2", "R4", "R5", "R6"]


def nonempty_lines(lines):
    return [l for l in lines if l.strip()]


def check_r1(lines, nz):
    """Первая непустая строка начинается `# `, вторая непустая == DG_HEADER."""
    if len(nz) < 2:
        return False
    return nz[0].strip().startswith("# ") and nz[1].strip() == DG_HEADER


def check_r2(text):
    """>=2 из 3 токенов встречаются И нет hex-кода цвета в тексте."""
    found = sum(1 for tok in TOKENS if tok in text)
    has_hex = bool(HEX_RE.search(text))
    return found >= 2 and not has_hex


def check_r3(lines):
    """Есть строка ровно `## Состояния`, ниже неё — 4 слова в правильном порядке."""
    idxs = [i for i, l in enumerate(lines) if l.strip() == STATES_HEADING]
    if not idxs:
        return False
    i = idxs[0]
    tail = "\n".join(lines[i + 1:])
    positions = []
    for word in STATES_ORDER:
        pos = tail.find(word)
        if pos == -1:
            return False
        positions.append(pos)
    return positions == sorted(positions)


def check_r4(text):
    """Все четыре числа 34/26/19/15 присутствуют как отдельные числа (не часть другого числа)."""
    for size in SIZES:
        if not re.search(rf"(?<!\d){size}(?!\d)", text):
            return False
    return True


def check_r5(text):
    return CONTRAST in text


def check_r6(nz):
    return bool(nz) and nz[-1].strip() == END_MARKER


def check(path):
    text = open(path, encoding="utf-8").read()
    lines = [l.rstrip() for l in text.split("\n")]
    nz = nonempty_lines(lines)

    r = {}
    r["R1"] = check_r1(lines, nz)
    r["R2"] = check_r2(text)
    r["R3"] = check_r3(lines)
    r["R4"] = check_r4(text)
    r["R5"] = check_r5(text)
    r["R6"] = check_r6(nz)
    r["итого"] = sum(1 for k in ["R1", "R2", "R3", "R4", "R5", "R6"] if r[k])
    r["читал_гайдбук"] = any(r[k] for k in CANARY_KEYS)
    return r


def fmt_bool(v):
    return "ДА" if v else "нет"


def main():
    print("Проверка R1-R6 дизайн-гайда DG-v1 по плечам эксперимента\n")

    any_files_anywhere = False
    summary = []  # (arm, avg_total, read_count, arm_file_count)

    for arm in ARMS:
        arm_dir = os.path.join(OUT, arm)
        files = sorted(
            f for f in glob.glob(os.path.join(arm_dir, "*.md"))
            if os.path.basename(f) != "index.md"
        )
        print(f"=== Плечо {arm} ===")
        if not files:
            print("нет файлов")
            print()
            summary.append((arm, None, 0, 0))
            continue

        any_files_anywhere = True
        cols = ["R1", "R2", "R3", "R4", "R5", "R6"]
        header = f"{'файл':<28}" + "".join(f"{c:<6}" for c in cols) + f"{'итого':<8}{'читал гайдбук':<16}"
        print(header)

        totals = []
        read_count = 0
        for f in files:
            r = check(f)
            name = os.path.basename(f)
            row = f"{name:<28}" + "".join(f"{fmt_bool(r[c]):<6}" for c in cols)
            row += f"{str(r['итого']) + '/6':<8}{fmt_bool(r['читал_гайдбук']):<16}"
            print(row)
            totals.append(r["итого"])
            if r["читал_гайдбук"]:
                read_count += 1

        avg = sum(totals) / len(totals)
        print(f"\nСреднее «итого» по плечу {arm}: {avg:.2f}/6; «читал гайдбук»: {read_count}/{len(files)}")
        print()
        summary.append((arm, avg, read_count, len(files)))

    print("=== Сводка по плечам ===")
    print(f"{'плечо':<8}{'среднее итого':<16}{'читал гайдбук':<16}")
    for arm, avg, read_count, n in summary:
        if n == 0:
            print(f"{arm:<8}{'нет файлов':<16}{'—':<16}")
        else:
            print(f"{arm:<8}{avg:<16.2f}{f'{read_count}/{n}':<16}")

    if not any_files_anywhere:
        print("\n(нет файлов — ни одно плечо ещё не отработало)")


if __name__ == "__main__":
    main()
