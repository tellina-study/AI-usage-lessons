#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Свод по разделам 2-3: префиксы, схемы у case, заметки, язык §11.6, термины."""
import re, sys, glob, yaml, statistics
from pathlib import Path
D=Path(__file__).resolve().parent/'slides'
SEC={'2','3'}
rows=[]
for f in sorted(D.glob('s*.md')):
    t=f.read_text(encoding='utf-8')
    m=re.match(r'^---\n(.*?)\n---\n(.*)$',t,re.S)
    if not m: continue
    fm='\n'.join(l for l in m.group(1).split('\n') if not l.startswith('#'))
    meta=yaml.safe_load(fm) or {}
    sec=str(meta.get('section') or '')
    if sec.split('.')[0] not in SEC: continue
    body=m.group(2)
    vis=body.split('## Заметки лектора')[0]
    zam=body.split('## Заметки лектора')[1] if '## Заметки лектора' in body else ''
    rows.append(dict(f=f.name, sid=meta.get('id'), lid=str(meta.get('local_id')),
                     sec=sec, typ=meta.get('type'), title=meta.get('title'),
                     scheme=bool(meta.get('scheme')), media=bool(str(meta.get('media') or '').strip()),
                     zam=len(zam.split()), vis=vis, zamtext=zam, fmraw=m.group(1)))

print('═══ ПРЕФИКСЫ local_id ПО РАЗДЕЛАМ ═══')
from collections import defaultdict
pref=defaultdict(lambda: defaultdict(list))
for r in rows:
    p=r['lid'].split('-')[0]
    pref[r['sec']][p].append(r['sid'])
for sec in sorted(pref):
    for p,ids in sorted(pref[sec].items()):
        print(f"  {sec:45} {p:8} {len(ids):2}  {' '.join(map(str,ids))}")
    print(f"  → префиксов в разделе: {len(pref[sec])}  {'OK' if len(pref[sec])==1 else '*** СМЕСЬ ***'}")

print('\n═══ СХЕМА У КАДРОВ type: case (§11.3) ═══')
bad=[r for r in rows if r['typ']=='case' and not r['scheme']]
for r in rows:
    if r['typ']=='case':
        print(f"  {str(r['sid']):6} схема {'да ' if r['scheme'] else 'НЕТ'}  {r['title'][:62]}")
print(f"  → без схемы: {len(bad)} из {sum(1 for r in rows if r['typ']=='case')}")

print('\n═══ ЗАМЕТКИ (норма 500-800) ═══')
z=[r['zam'] for r in rows]
out=[r for r in rows if not (500<=r['zam']<=800)]
for r in sorted(rows,key=lambda r:-r['zam']):
    flag='' if 500<=r['zam']<=800 else ('  ← ВЫШЕ 800' if r['zam']>800 else '  ← НИЖЕ 500')
    print(f"  {str(r['sid']):6} {r['zam']:5}{flag}")
print(f"  → вне коридора {len(out)} из {len(rows)} · медиана {statistics.median(z):.0f} · максимум {max(z)}")

print('\n═══ ПРОИЗВОДСТВЕННЫЙ ЯЗЫК §11.6 + §6.3 (видимый слой И заметки) ═══')
PAT=[r'Имени\s+\S+\s+не\s+(получил|назвал|называет|печатает)', r'кадром\s+(следом|раньше|перед этим)',
     r'Раздел\s+(берёт|закрыл)', r'подмножеств\w*', r'\bразряд\w*', r'\bсвод\b', r'по этой паре',
     r'\(опционально\)', r'та же работ\w+', r'достроить', r'рычаг', r'несущ\w+\s+ось',
     r'вклад\s*№', r'по постановке', r'→\s*s\d+', r'\bсм\.\s*(слайд|разбор)', r'§\d']
hits=0
for r in rows:
    for lay,txt in (('видимое',r['vis']),('заметки',r['zamtext'])):
        for p in PAT:
            for mm in re.finditer(p,txt,re.I):
                s=max(0,mm.start()-45); print(f"  {str(r['sid']):6} {lay:8} …{txt[s:mm.end()+45].strip()}…"); hits+=1
print(f"  → совпадений: {hits}")

print('\n═══ ТЕРМИН «площадь под кривой» (§5.20/§11.7) ═══')
for r in rows:
    for lay,txt in (('видимое',r['vis']),('заметки',r['zamtext'])):
        if 'площад' in txt:
            expl = 'монетк' in txt or '0,5' in txt and '1,0' in txt
            for mm in re.finditer(r'площад\w+ под кривой',txt):
                s=max(0,mm.start()-60)
                print(f"  {str(r['sid']):6} {lay:8} объяснён:{'да ' if expl else 'НЕТ'} …{txt[s:mm.end()+70].strip()}…")
