#!/usr/bin/env python3
"""Сшивает главу семинара в один читаемый файл.

ПРОИЗВОДНОЕ. Руками не правят — правят части, потом перезапускают:
    python3 tools/seminar-build/sobrat_glavu.py --seminar 12

Собирает в порядке: теория -> обзор замеров -> разделы по кейсам.
Фронтматтер частей снимается, его содержимое не теряется: имя файла и
заголовок остаются в оглавлении. Лимит 600 строк к этому файлу не
применяется — он производный, как deck.yaml и pptx.
"""
import re, sys, glob, os, argparse

p = argparse.ArgumentParser()
p.add_argument('--seminar', type=int, required=True)
a = p.parse_args()
BASE = f'library/seminars/sem-{a.seminar:02d}'

GROUPS = [
    ("Часть I. Теория: устройство, границы, цена",
     sorted(glob.glob(f'{BASE}/glava/10-teoriya-*.md'))),
    ("Часть II. Замеры: корпуса, протоколы, числа, что перевернулось",
     sorted(glob.glob(f'{BASE}/glava/20-zamery-*.md'))),
    ("Часть III. Разборы по кейсам",
     [f for f in sorted(glob.glob(f'{BASE}/rework/section-[A-Z]-*.md'))]),
]

def strip_fm(t):
    m = re.match(r'^---\n.*?\n---\n', t, re.S)
    return t[m.end():] if m else t

def demote(t, by=1):
    """Сдвигает уровни заголовков, чтобы части не спорили с оглавлением."""
    return re.sub(r'^(#{1,5}) ', lambda m: '#' * (len(m.group(1)) + by) + ' ', t, flags=re.M)

out, toc, words = [], [], 0
for title, files in GROUPS:
    if not files: continue
    toc.append(f'\n### {title}\n')
    for f in files:
        t = strip_fm(open(f).read()).strip()
        h = re.search(r'^#{1,2} (.+)$', t, re.M)
        name = h.group(1).strip() if h else os.path.basename(f)
        anchor = re.sub(r'[^\w\- ]', '', name.lower()).replace(' ', '-')
        toc.append(f'- [{name}](#{anchor}) · `{os.path.basename(f)}`')
        words += len(t.split())
        # Заголовок части печатает сборщик (строкой ниже). Собственный первый заголовок
        # части снимаем: все части лежат с заголовком первого уровня, demote делает из него
        # «##» — ровно тот уровень, который печатает сборщик, и заголовок выходил ДВАЖДЫ
        # подряд у каждой из частей. Ловилось глазами и ни одним сторожем (#351).
        body = re.sub(r'^#{1,2} .+\n+', '', t, count=1)
        out.append(f'\n\n---\n\n## {name}\n\n*Источник: `{f}`*\n\n' + demote(body, 1))

hdr = f"""# Семинар {a.seminar}. Глава занятия — полный текст

> **Это производный файл.** Он сшит программой `tools/seminar-build/sobrat_glavu.py`
> из частей, которые и есть источник правды. Править здесь нечего: правка потеряется
> при следующей сборке. Части лежат в `{BASE}/glava/` (теория и обзор замеров) и
> `{BASE}/rework/` (разборы по кейсам).
>
> Объём: **{words:,} слов** в {sum(len(f) for _, f in GROUPS)} частях.
> Лимит в 600 строк к производному файлу не применяется.

## Оглавление
""".replace(',', ' ')

open(f'{BASE}/GLAVA-POLNAYA.md', 'w').write(hdr + '\n'.join(toc) + ''.join(out) + '\n')
print(f'{BASE}/GLAVA-POLNAYA.md: {words} слов, {sum(len(f) for _,f in GROUPS)} частей')
