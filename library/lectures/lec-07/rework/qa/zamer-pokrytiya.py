# -*- coding: utf-8 -*-
import io, re, os, collections
src=io.open('deck/make_deck_yaml.py',encoding='utf-8').read()
body=re.search(r'CHAP = \{(.*?)\n\}',src,re.S).group(1)
E=re.findall(r"'(s\d+[a-z]*)'\s*:\s*'((?:[^'\\]|\\.)*)'",body)
addressed={p for _,v in E for p in re.findall(r'§\s*(\d+\.\d+)',v)}
# все параграфы главы с номером
have=collections.defaultdict(list)
for f in sorted(x for x in os.listdir('.') if re.match(r'chapter.*\.md$',x)):
    for l in io.open(f,encoding='utf-8'):
        m=re.match(r'^#{2,4}\s+§\s*(\d+)\.(\d+)\s',l)
        if m: have[int(m.group(1))].append(f'{m.group(1)}.{m.group(2)}')
print(f'{"раздел":>7} {"всего §":>8} {"адресовано":>11} {"не адресовано":>14}')
for r in sorted(have):
    ps=have[r]; a=[p for p in ps if p in addressed]; n=[p for p in ps if p not in addressed]
    mark=' <<<' if len(n)>len(a) else ''
    print(f'{r:>7} {len(ps):>8} {len(a):>11} {len(n):>14}{mark}')
    if n and len(n)>len(a): print(f'         не адресованы: {" ".join(n)}')
