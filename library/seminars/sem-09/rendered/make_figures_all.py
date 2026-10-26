#!/usr/bin/env python3
"""Рисует ВСЕ программные схемы Семинара 9 одним прогоном и печатает замеры.

Семь файлов, не восемь: схемы `k1-shema-samootchet` и `k1-shema-geyt` сведены
в одну двухпанельную `k1-shema-samootchet-i-geyt` — у Кейса 1 один такт слоя 1,
и сопоставление обязано читаться с одного взгляда (`BRIEF-PROIZVODSTVO.md` §5).

Зачем один вход на все: замер кегля и аудит подписей считаются по ТОМУ, что
реально дошло до холста, и считать их имеет смысл сразу по всем схемам — пол
кегля один на деку, словарь запретов один, палитра одна. Поштучный прогон
каждой рисовалки тоже работает, но даёт замер только по своим схемам.

    python3 make_figures_all.py
"""
import make_figures_lestnitsa as L
import make_figures_k1 as K1
import make_figures_k2 as K2
import make_figures_k3 as K3
import make_figures_k4 as K4
import make_figures_k5 as K5
import make_figures_k6 as K6
from make_figures_common import pt_report, audit_sources

L.lestnitsa()
K1.samootchet_i_geyt()
K2.kesh()
K3.tsikl()
K4.potoki()
K5.tri_ishoda()
K6.vysota_simvola()

bad = pt_report("программные схемы слоя 1 — Семинар 9")
off, lat, hits = audit_sources()
print(f"\nИТОГ: схем {7} · ниже порога кегля {len(bad)} · цвета мимо палитры "
      f"{len(off)} · латиница {len(lat)} · запрещённые обороты {len(hits)}")
