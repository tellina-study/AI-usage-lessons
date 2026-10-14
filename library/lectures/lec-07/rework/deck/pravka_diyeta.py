#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Правка кадра круга диеты: меняет поля фронтматтера и/или видимый текст,
заметки лектора не трогает. Вызывается из скриптов правки, не руками.

Зачем отдельно от `pravka.py`: тот правит текст построчно; здесь нужна
замена ЦЕЛОЙ секции «Видимый текст слайда» и полей фронтматтера, которые
живут в счёте страницы наравне с телом (заголовок, подвал, плашки, схема).
"""
import re
import sys
from pathlib import Path

SL = Path(__file__).resolve().parent / "slides"


def find(sid):
    hits = [f for f in SL.glob("*.md") if re.match(rf"^{sid}[-.]", f.name)]
    if len(hits) != 1:
        sys.exit(f"{sid}: найдено файлов {len(hits)}")
    return hits[0]


def split(txt):
    m = re.match(r"^---\n(.*?\n)---\n(.*?)(## Заметки лектора\n.*)$", txt, re.S)
    if not m:
        sys.exit("файл не разбирается на фронтматтер / тело / заметки")
    return m.group(1), m.group(2), m.group(3)


def setfield(fm, key, val):
    """Заменить скалярное поле фронтматтера (одна строка)."""
    pat = re.compile(rf"^{key}: .*$", re.M)
    if not pat.search(fm):
        sys.exit(f"поля {key} в кадре нет")
    return pat.sub(lambda _: f"{key}: {val}", fm, count=1)


def setblock(fm, key, val):
    """Заменить блочное поле (`blocks:`/`scheme:`/`columns:`) целиком.
    `val=None` — выкинуть поле. Конец блока — следующая строка с нулевым
    отступом."""
    lines = fm.split("\n")
    out, i, seen = [], 0, False
    while i < len(lines):
        ln = lines[i]
        if re.match(rf"^{key}:", ln):
            seen = True
            i += 1
            while i < len(lines) and (lines[i].startswith((" ", "-")) or not lines[i].strip()):
                i += 1
            if val is not None:
                out.append(val.rstrip("\n"))
            continue
        out.append(ln)
        i += 1
    if not seen and val is not None:
        sys.exit(f"блочного поля {key} в кадре нет — вставлять надо руками")
    return "\n".join(out)


def apply(sid, body=None, fields=(), blocks=None, notes_add=None, drop=()):
    f = find(sid)
    fm, old_body, notes = split(f.read_text(encoding="utf-8"))
    for k, v in fields:
        fm = setfield(fm, k, v)
    for k in drop:
        fm = setblock(fm, k, None)
    for k, v in (blocks or {}).items():
        fm = setblock(fm, k, v)
    if body is not None:
        old_body = "## Видимый текст слайда\n" + body.strip("\n") + "\n\n"
    if notes_add:
        notes = notes.rstrip("\n") + "\n\n" + notes_add.strip("\n") + "\n"
    f.write_text(f"---\n{fm}---\n{old_body}{notes}", encoding="utf-8")
    print(f"{sid}: правлено ({f.name})")
