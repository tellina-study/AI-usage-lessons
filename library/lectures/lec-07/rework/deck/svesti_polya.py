#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Довод свёртки: поля, которые склейка пары НЕ сводит сама.

`slit_pary.py` сводит состав (плашки, схему, столбцы, формы, шаги, источник).
Остаются поля, где сведение -- СУЖДЕНИЕ, а не склейка, и их перечисляют здесь
поимённо, чтобы ни одно не уехало молча:

  timing_min  -- СУММА двух кадров. Молчаливая потеря минут второго кадра
                 ломает минутный счёт деки: шесть пар -- это 4,6 минуты.
  in_bucket   -- ИЛИ: собранный кадр несёт strict-in, если его несла хоть
                 одна половина (доля провалов/границ считается по кадрам).
  vfy         -- ИЛИ: число под пересверку в день лекции осталось на кадре.
  type        -- РАЗБОР СИЛЬНЕЕ: `case` побеждает `comparison`, потому что
                 собранный кадр несёт состав разбора (§5.13), а не
                 противопоставление в два столбца.
  vizforma    -- от того, у кого она была: ось/ряды рисует схему, и без
                 метки схема второго кадра не отрисуется.
  media       -- от того, у кого снимок был: пустое поле не затирает живой.
"""
import glob
import os
import re
import sys

PARY = [('s18', 0.95, 0.6), ('s22a', 0.5, 0.6), ('s31', 0.9, 0.75),
        ('s41', 1.1, 0.6), ('s47', 1.15, 1.05), ('s49b', 1.15, 1.0)]
PRAVKI = {
    's18':  {'in_bucket': 'true'},
    's22a': {'media': '"rework/deck/assets/s23-laborant-za-pultom-reshaet-o-godnosti.jpg"'},
    's41':  {'type': 'case'},
    's47':  {'in_bucket': 'true'},
    's49b': {'type': 'case', 'vizforma': '"ось"'},
}


def put(sid):
    return [f for f in glob.glob('slides/s*.md')
            if os.path.basename(f).startswith(sid + '-')][0]


def main():
    for sid, ta, tb in PARY:
        p = put(sid)
        t = open(p, encoding='utf-8').read()
        summa = round(ta + tb, 2)
        t2, n = re.subn(r'^timing_min:.*$',
                        'timing_min: %s   # свёртка пары (#229): %s + %s' % (summa, ta, tb),
                        t, count=1, flags=re.M)
        assert n == 1, 'timing_min не найден у %s' % sid
        print('%-6s timing_min %s + %s -> %s' % (sid, ta, tb, summa))
        for k, v in PRAVKI.get(sid, {}).items():
            if re.search(r'^%s:' % k, t2, re.M):
                t2, n = re.subn(r'^%s:.*$' % k, '%s: %s' % (k, v), t2,
                                count=1, flags=re.M)
            else:   # поля не было -- поставить перед timing_min
                t2 = t2.replace('timing_min:', '%s: %s\ntiming_min:' % (k, v), 1)
                n = 1
            assert n == 1, '%s у %s не поставлено' % (k, sid)
            print('       %-10s -> %s' % (k, v[:60]))
        open(p, 'w', encoding='utf-8').write(t2)


if __name__ == '__main__':
    main()
