#!/usr/bin/env python3
"""Рисует ВСЕ программные схемы Семинара 9 одним прогоном и печатает замеры.

Одиннадцать файлов: лестница (1) + Кейс 1 (1, `k1-shema-samootchet` и
`k1-shema-geyt` сведены в одну двухпанельную `k1-shema-samootchet-i-geyt` — у
Кейса 1 один такт слоя 1, сопоставление обязано читаться с одного взгляда,
`BRIEF-PROIZVODSTVO.md` §5) + Кейс 2 (2: `sloy1()` и `kesh()`) + Кейс 3 (1) +
Кейс 4 (3: `postanovka()`, `klassy()`, `voronka()` — кейс переопределён
2026-10-29, был один такт, стало три) + Кейс 5 (1) + Кейс 6 (2:
`chtenie_i_sverka()` и `vysota_simvola()`).

**Список вызовов ниже обязан быть ТОЧНОЙ КОПИЕЙ того, что вызывает
`if __name__ == "__main__":` каждого отдельного `make_figures_kN.py`** — не
пересказом по памяти. Разрыв между ними уже стоил полной пересборки: до
2026-10-29 здесь стояло `K4.potoki()` (такой функции в модуле нет вовсе —
полная пересборка падала), и молча отсутствовали `K2.sloy1()` (даёт
`k2-shema-promt-i-kesh.png`, фигура `n22-k2-reshenie-sloy1.md`) и
`K6.chtenie_i_sverka()` (даёт `k6-shema-chtenie-i-sverka.png`, фигура
`n68-k6-reshenie-sloy1.md`) — оба файла существовали на диске только потому,
что кто-то когда-то запустил свой `make_figures_kN.py` отдельно; путь
«пересобрать производное целиком» их бы не создал и не обновил. Сторожа на
этот разрыв нет: `pt_report`/`audit_sources` меряют то, что дошло до холста
В ЭТОМ прогоне, и молчат про функцию, которую прогон не позвал.

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
K2.sloy1()
K2.kesh()
K3.tsikl()
K4.postanovka()
K4.klassy()
K4.voronka()
K5.tri_ishoda()
K6.chtenie_i_sverka()
K6.vysota_simvola()

bad = pt_report("программные схемы слоя 1 — Семинар 9")
off, lat, hits = audit_sources()
print(f"\nИТОГ: схем {11} · ниже порога кегля {len(bad)} · цвета мимо палитры "
      f"{len(off)} · латиница {len(lat)} · запрещённые обороты {len(hits)}")
