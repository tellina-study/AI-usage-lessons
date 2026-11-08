#!/usr/bin/env python3
"""Пофайловый замер формата сопоставления по трём слоям slide .md файлов.

Разметка (по заданию наряда):
  шапка   — первый блок между `---`...`---` в начале файла;
  тело    — всё после шапки до строки `## Speaker notes`;
  заметки — всё после строки `## Speaker notes`.

Использование:
  python3 measure_sopostavlenie.py <file1.md> [file2.md ...]
  python3 measure_sopostavlenie.py --self-test
"""
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "tools", "seminar-build"))
from sopostavlenie_figury import FIGURY  # noqa: E402


def split_layers(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            end = -1
    else:
        end = -1
    if end == -1:
        frontmatter = ""
        rest_lines = lines
    else:
        frontmatter = "\n".join(lines[: end + 1])
        rest_lines = lines[end + 1 :]
    rest = "\n".join(rest_lines)
    marker = "## Speaker notes"
    if marker in rest:
        idx = rest.index(marker)
        body = rest[:idx]
        notes = rest[idx + len(marker) :]
    else:
        body = rest
        notes = ""
    return frontmatter, body, notes


def count_layer(text):
    total = 0
    per_figure = {}
    for name, pattern in FIGURY:
        hits = pattern.findall(text)
        n = len(hits)
        if n:
            per_figure[name] = n
        total += n
    return total, per_figure


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        good = "не просто читает, а сверяет"
        bad = "сумма не прочитана"
        bad2 = "модель не видит текст заявки"
        g_total, _ = count_layer(good)
        b_total, _ = count_layer(bad)
        b2_total, _ = count_layer(bad2)
        print(f"проба 'не просто читает, а сверяет' -> {g_total} (ожидаем >=1)")
        print(f"проба 'сумма не прочитана' -> {b_total} (ожидаем 0)")
        print(f"проба 'модель не видит текст заявки' -> {b2_total} (ожидаем 0)")
        assert g_total >= 1
        assert b_total == 0
        assert b2_total == 0
        print("self-test OK")
        return

    grand = {"шапка": 0, "тело": 0, "заметки": 0}
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        frontmatter, body, notes = split_layers(text)
        fm_n, _ = count_layer(frontmatter)
        body_n, _ = count_layer(body)
        notes_n, _ = count_layer(notes)
        grand["шапка"] += fm_n
        grand["тело"] += body_n
        grand["заметки"] += notes_n
        print(f"{os.path.basename(path)}\tшапка={fm_n}\tтело={body_n}\tзаметки={notes_n}")
    print("---")
    print(f"ИТОГО\tшапка={grand['шапка']}\tтело={grand['тело']}\tзаметки={grand['заметки']}")


if __name__ == "__main__":
    main()
