#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Слов в заметках лектора по кадрам — норма владельца 500–800."""
import re, sys
import pravka_diyeta as P

for sid in sys.argv[1:]:
    f = P.find(sid)
    n = f.read_text(encoding='utf-8').split('## Заметки лектора')
    if len(n) < 2:
        print(f"{sid:7} заметок нет"); continue
    txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', n[1])
    w = len(txt.split())
    flag = '' if 500 <= w <= 800 else '  ← вне нормы 500–800'
    print(f"{sid:7} {w:4}{flag}")
