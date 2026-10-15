#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Свёртка ПАРЫ кадров в один: механически, одним правилом на все шесть пар.

ЗАЧЕМ ПРОГОН, А НЕ ШЕСТЬ ПРАВОК РУКАМИ. Пар шесть, у каждой свой состав
фронтматтера (плашки, схема, столбцы, формы, шаги разбора), и правка руками
теряет поле молча -- ровно так в Лекции 5 манифест разошёлся с кадрами на 153
поля, ничего при этом не сломав. Здесь состав СВОДИТСЯ по одному правилу, и
что именно съехало, видно в выдаче.

ЧТО ДЕЛАЕТ:
  * цель -- файл ПЕРВОГО кадра пары: его `id` остаётся, поэтому сквозная
    нумерация не едет и ссылки манифестов разрешаются (snyat-номер не
    переиспользуется -- правило `_snyato/README.md`);
  * `blocks` / `scheme` / `columns` / `form` / `method_steps` / `source`
    сливаются (второй приписывается к первому, дубли по тексту снимаются);
  * видимый текст второго кадра приписывается к первому ПОД ЯВНЫМ МАРКЕРОМ
    `<!-- СЛИТО ИЗ sNN -->`, заметки -- так же;
  * второй файл уходит в `_snyato/` -- он СЛИТ, а не выброшен, и запись в
    README это говорит.

ЧЕГО ЭТОТ ПРОГОН НЕ ДЕЛАЕТ, сказано вслух:
  * НЕ сокращает текст. Собранный кадр почти наверняка тяжелее предела и
    требует сжатия до формы §5.13 -- это работа содержательной сессии, и
    маркер `<!-- СЛИТО -->` оставлен ровно для того, чтобы она видела, что
    откуда пришло;
  * НЕ судит, сложилась пара или нет (наряд §3.6). Вес после склейки печатает,
    решение -- человека;
  * НЕ правит `pol_slov`: объявленный пол обязан называть, ЧЕМ заняты слова,
    а это суждение. Прогон старый пол СНИМАЕТ и говорит об этом, чтобы
    не осталось числа, которое врёт.

    python3 slit_pary.py s18 s19
    python3 slit_pary.py --selftest
"""
import glob
import os
import re
import shutil
import subprocess
import sys

SPISKI = ('method_steps', 'form')
BLOKI = ('blocks', 'scheme', 'columns')


def put(sid):
    h = [f for f in glob.glob('slides/s*.md')
         if re.match(r'^%s-' % re.escape(sid), os.path.basename(f))]
    if len(h) != 1:
        sys.exit('кадр %s: найдено %d файлов' % (sid, len(h)))
    return h[0]


def razrez(t):
    """Файл кадра -> (фронтматтер, видимый текст, заметки)."""
    ch = t.split('---\n')
    fm = ch[1]
    ost = '---\n'.join(ch[2:])
    vid, zam = ost, ''
    if '## Заметки лектора' in ost:
        vid, zam = ost.split('## Заметки лектора', 1)
    vid = vid.replace('## Видимый текст слайда', '', 1)
    return fm, vid.strip(), zam.strip()


def pole(fm, k):
    """Значение поля ВМЕСТЕ с его вложенными строками (yaml-блок)."""
    m = re.search(r'^%s:(.*)$' % k, fm, re.M)
    if not m:
        return None, None
    start = m.start()
    lines = fm[start:].splitlines()
    out = [lines[0]]
    for ln in lines[1:]:
        if ln.startswith((' ', '\t')) or ln.strip().startswith('-'):
            out.append(ln)
        else:
            break
    return '\n'.join(out), start


def selftest():
    sb = []
    obr = ('---\nid: s18\nblocks:\n  - {label: "А", value: "1"}\n'
           'form: ["форма 5"]\n---\n\n## Видимый текст слайда\n\nтело\n\n'
           '## Заметки лектора\n\nзаметка\n')
    fm, vid, zam = razrez(obr)
    if 'id: s18' not in fm:
        sb.append('разрез потерял фронтматтер')
    if vid != 'тело':
        sb.append('разрез дал тело %r вместо %r' % (vid, 'тело'))
    if zam != 'заметка':
        sb.append('разрез дал заметки %r' % zam)
    v, _ = pole(fm, 'blocks')
    if v is None or 'label: "А"' not in v:
        sb.append('pole() не забрал вложенные строки blocks: %r' % v)
    v, _ = pole(fm, 'form')
    if v != 'form: ["форма 5"]':
        sb.append('pole() испортил однострочное поле: %r' % v)
    if pole(fm, 'scheme')[0] is not None:
        sb.append('pole() нашёл отсутствующее поле')
    if sb:
        print('САМОПРОВЕРКА НЕ ПРОШЛА:')
        [print('  ' + s) for s in sb]
        return 1
    print('самопроверка: разрез и чтение yaml-блока ведут себя как заложено')
    print('ЧЕГО НЕ ДОКАЗЫВАЕТ: что склейка даёт ЧИТАЕМЫЙ кадр. Это глазами.')
    return 0


def main():
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    a, b = sys.argv[1], sys.argv[2]
    pa, pb = put(a), put(b)
    ta = open(pa, encoding='utf-8').read()
    tb = open(pb, encoding='utf-8').read()
    fa, va, za = razrez(ta)
    fb, vb, zb = razrez(tb)
    print('СЛИВАЮ %s <- %s' % (os.path.basename(pa), os.path.basename(pb)))

    # 1. блочные поля: приписать второй к первому
    for k in BLOKI:
        vbk, _ = pole(fb, k)
        if not vbk:
            continue
        telo_b = '\n'.join(vbk.splitlines()[1:])
        vak, st = pole(fa, k)
        if vak and vak.splitlines()[0].strip() not in ('%s:' % k, '%s: []' % k) \
                and len(vak.splitlines()) == 1:
            print('  ! %s у %s однострочное (%s) -- второй дописан ниже, '
                  'свести руками' % (k, a, vak.strip()))
        if vak:
            if telo_b.strip():
                fa = fa[:st] + vak + '\n' + telo_b + fa[st + len(vak):]
                print('  %s: дописаны строки из %s' % (k, b))
        else:
            fa = fa.replace('timing_min:', vbk + '\ntiming_min:', 1)
            print('  %s: перенесено целиком из %s' % (k, b))

    # 2. списковые поля: объединить без дублей
    for k in SPISKI:
        va_, st = pole(fa, k)
        vb_, _ = pole(fb, k)
        if not (va_ and vb_):
            continue
        ea = re.findall(r'"([^"]+)"', va_)
        eb = re.findall(r'"([^"]+)"', vb_)
        vse = ea + [e for e in eb if e not in ea]
        nov = '%s: [%s]' % (k, ', '.join('"%s"' % e for e in vse))
        fa = fa[:st] + nov + fa[st + len(va_):]
        if len(vse) > len(ea):
            print('  %s: + %s' % (k, ', '.join(e for e in eb if e not in ea)))

    # 3. источник
    sa = re.search(r'^source:\s*"?(.*?)"?$', fa, re.M)
    sbb = re.search(r'^source:\s*"?(.*?)"?$', fb, re.M)
    if sa and sbb and sbb.group(1) not in ('', '—') \
            and sbb.group(1) not in sa.group(1):
        novy = (sa.group(1) + ' · ' + sbb.group(1)) if sa.group(1) != '—' \
            else sbb.group(1)
        fa = fa[:sa.start()] + 'source: "%s"' % novy + fa[sa.end():]
        print('  source: дописан источник %s' % b)

    # 4. снять объявленный пол -- он называл состав ДО склейки
    m = re.search(r'^pol_slov:.*$', fa, re.M)
    if m:
        fa = fa[:m.start()] + ('# pol_slov СНЯТ свёрткой (#229): прежнее число '
                               'называло состав ДО склейки с %s и после неё '
                               'врёт. Объявить заново обязана содержательная '
                               'сессия -- с причиной, называющей, ЧЕМ заняты '
                               'слова собранного кадра.' % b) + fa[m.end():]
        print('  pol_slov: снят (называл состав до склейки)')

    # 5. тело и заметки
    nov = ('---\n' + fa + '---\n\n## Видимый текст слайда\n\n' + va
           + '\n\n<!-- СЛИТО ИЗ %s (#229, свёртка пары): ниже видимый текст '
             'второго кадра пары, НЕ СЖАТЫЙ. Свести в одну форму §5.13 и '
             'снять этот маркер обязана содержательная сессия. -->\n\n' % b
           + vb + '\n\n## Заметки лектора\n\n' + za
           + '\n\n<!-- ЗАМЕТКИ, СЛИТЫЕ ИЗ %s -->\n\n' % b + zb + '\n')
    open(pa, 'w', encoding='utf-8').write(nov)
    subprocess.run(['git', 'mv', pb, 'slides/_snyato/' + os.path.basename(pb)],
                   check=True)
    print('  %s -> _snyato/ (СЛИТ, не выброшен)' % os.path.basename(pb))


if __name__ == '__main__':
    main()
