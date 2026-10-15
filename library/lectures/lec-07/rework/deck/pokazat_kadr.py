#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Печать кадра БЕЗ заметок: фронтматтер + раздел «Видимый текст слайда».

Служебный прогон сессии структурного разреза (#229): заметки у кадров этой деки
500-800 слов, и читать их целиком при структурной работе незачем -- а контекст
они съедают. Печатает ровно то, что видит зал, плюс фронтматтер.

    python3 pokazat_kadr.py s30 s30a        # по id
    python3 pokazat_kadr.py --zametki s30   # вместе с заметками
"""
import sys, glob, re, os

zam = '--zametki' in sys.argv
ids = [a for a in sys.argv[1:] if not a.startswith('--')]
for sid in ids:
    hits = [f for f in glob.glob('slides/*.md')
            if re.match(r'^%s[-.]' % re.escape(sid), os.path.basename(f))]
    if not hits:
        print('НЕ НАЙДЕН: %s' % sid); continue
    t = open(hits[0], encoding='utf-8').read()
    if not zam:
        t = t.split('## Заметки лектора')[0]
    print('#' * 20, os.path.basename(hits[0]))
    print(t.rstrip())
    print()
