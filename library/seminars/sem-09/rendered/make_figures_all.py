#!/usr/bin/env python3
"""Рисует ВСЕ программные схемы Семинара 9 одним прогоном и печатает замеры.

Шестнадцать файлов: лестница (1) + Кейс 1 (2: `postanovka()` сцены — новая,
issue #303 — и `k1-shema-samootchet` с `k1-shema-geyt`, сведённые в одну
двухпанельную `k1-shema-samootchet-i-geyt`, у Кейса 1 один такт слоя 1,
сопоставление обязано читаться с одного взгляда, `BRIEF-PROIZVODSTVO.md`
§5) + Кейс 2 (3: `postanovka()`, `sloy1()`, `kesh()`) + Кейс 3 (2:
`postanovka()`, `tsikl()`) + Кейс 4 (3: `postanovka()`, `klassy()`,
`voronka()` — кейс переопределён 2026-10-29, был один такт, стало три) +
Кейс 5 (2: `postanovka()`, `tri_ishoda()`) + Кейс 6 (3: `postanovka()`,
`chtenie_i_sverka()`, `vysota_simvola()`).

Пять схем сцены (`k1`/`k2`/`k3`/`k5`/`k6`-`shema-postanovka.png`) добавлены
issue #303 («в половине кейсов вместо схем в начале описание»): до этой
правки Кейсы 1, 2, 3, 5, 6 открывались тремя текстовыми кадрами подряд —
сцена, вопрос, разбор — и устройство зал видел только на кадре разбора.
Кейс 4 уже несёт схему постановки (переопределён этой же волной раньше) —
образец устройства и уровня для остальных пяти.

Ещё четыре схемы РАЗБОРА той же волны (issue #303, Часть Б) —
`k1-shema-spektr-deystviy.png` (n07a), `k2-shema-gde-v-promte.png` (n20a),
`k3-shema-kto-verdikt.png` (n31a), `k6-shema-tri-potoka.png` (на том же
кадре n67, не отдельным). Кейсы 4 и 5 своей НОВОЙ схемы разбора не
получили сознательно — решение задокументировано в `backup:` кадров n46 и
n58: обе таблицы уже показывают место способа в конвейере на соседнем
кадре (n44 и n56), вторая схема была бы cross-slide redundancy.

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
K1.postanovka()
K1.samootchet_i_geyt()
K1.razbor_spektr()
K2.postanovka()
K2.sloy1()
K2.kesh()
K2.razbor_gde_v_promte()
K3.postanovka()
K3.tsikl()
K3.razbor_kto_verdikt()
K4.postanovka()
K4.klassy()
K4.voronka()
K5.postanovka()
K5.tri_ishoda()
K6.postanovka()
K6.chtenie_i_sverka()
K6.vysota_simvola()
K6.razbor_tri_potoka()

bad = pt_report("программные схемы слоя 1 — Семинар 9")
off, lat, hits = audit_sources()
print(f"\nИТОГ: схем {20} · ниже порога кегля {len(bad)} · цвета мимо палитры "
      f"{len(off)} · латиница {len(lat)} · запрещённые обороты {len(hits)}")
