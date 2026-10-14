# -*- coding: utf-8 -*-
"""Проверка адресов chapter_ref деки против нынешней главы: файл существует и параграф в нём.

Повод: два разреза части 4 по пределу 600 строк перенесли § 8.11–8.16 в chapter-part4da.md и
§ 9.9–9.12 в chapter-part4f.md. Адрес, указывающий на прежний файл, разрешается молча — файл
существует, просто параграфа в нём больше нет. Только чтение: ни деку, ни CHAP не правим.
"""
import io, os, re, sys

CH_DIR = '.'
src = io.open('deck/make_deck_yaml.py', encoding='utf-8').read()
body = re.search(r'CHAP = \{(.*?)\n\}', src, re.S).group(1)
entries = re.findall(r"'(s\d+[a-z]*)'\s*:\s*'((?:[^'\\]|\\.)*)'", body)
print(f'прочитано записей CHAP: {len(entries)}')

# где какой параграф лежит сейчас
para_of = {}
files = sorted(f for f in os.listdir(CH_DIR) if re.match(r'chapter.*\.md$', f))
named = {}
for f in files:
    for line in io.open(os.path.join(CH_DIR, f), encoding='utf-8'):
        m = re.match(r'^#{2,4}\s+§?\s*(\d+\.\d+(?:\.\d+)?)\s', line)
        if m:
            para_of.setdefault(m.group(1), []).append(f)
        h = re.match(r'^#{2,4}\s+(.*)$', line)
        if h:
            named.setdefault(f, []).append(h.group(1).strip())
print(f'прочитано файлов главы: {len(files)}; параграфов с номером: {len(para_of)}')

PARA = re.compile(r'§\s*(\d+\.\d+(?:\.\d+)?)')
FILE = re.compile(r'(chapter[\w-]*\.md)')
bad_file, bad_para, ok = [], [], 0
for sid, val in entries:
    # разбиваем на участки «файл … параграфы», файл действует до следующего упоминания файла
    parts = []
    pos = 0
    for m in FILE.finditer(val):
        if parts: parts[-1] = (parts[-1][0], val[parts[-1][1]:m.start()])
        parts.append((m.group(1), m.end()))
    if parts: parts[-1] = (parts[-1][0], val[parts[-1][1]:])
    if not parts:
        bad_file.append((sid, val, 'файл в адресе не назван вовсе')); continue
    for fname, tail in parts:
        if fname not in files:
            bad_file.append((sid, val, f'файла нет: {fname}')); continue
        for p in PARA.findall(tail):
            where = para_of.get(p)
            if not where:
                bad_para.append((sid, fname, p, 'параграфа нет ни в одном файле'))
            elif fname not in where:
                bad_para.append((sid, fname, p, 'параграф лежит в ' + ', '.join(where)))
            else:
                ok += 1

print(f'\nадресов «файл+параграф» сошлось: {ok}')
print(f'ОШИБОК ФАЙЛА: {len(bad_file)}')
for s_, v, why in bad_file: print(f'   {s_}: {why}  ← {v[:90]}')
print(f'ОШИБОК ПАРАГРАФА: {len(bad_para)}')
for s_, f_, p, why in bad_para: print(f'   {s_}: адрес говорит «{f_} §{p}», а {why}')
# контроль: проверка обязана уметь находить
assert '8.12' in para_of and para_of['8.12'] == ['chapter-part4da.md'], para_of.get('8.12')
assert '9.10' in para_of and para_of['9.10'] == ['chapter-part4f.md'], para_of.get('9.10')
print('\nконтроль: § 8.12 найден в chapter-part4da.md, § 9.10 — в chapter-part4f.md, то есть проверка видит переезд')
