#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пол слов на кадре — по СОБРАННОМУ PDF, с объявленными полами и причинами.

Чего не делал ни один прогон до этого. `render_sec.py` печатает слова по
страницам и медиану, но ни с каким полом их не сравнивает. `ocenka.py`
сравнивает — по файлу кадра, то есть оценкой, а числа отчёта оценкой быть
не могут. Между ними пролегал ровно тот зазор, в котором и живёт вопрос
приёмки: «взят ли предел на каждом кадре».

ПОЧЕМУ ПОЛ ОТВЕЧАЕТ ПЕРЕД PDF, А НЕ ПЕРЕД ОЦЕНКОЙ. Иначе объявленный пол
начинает покрывать не кадр, а чужую погрешность: кадр `s12` весит 117 слов
по PDF и 122 по оценке, и пол ему пришлось бы объявить 125 — то есть
двадцать слов запаса там, где кадру нужно ноль. Пол — это РАЗРЕШЕНИЕ, и
лишнее разрешение кадр со временем зарастает.

ЧТО ПЕЧАТАЕТСЯ И ПОЧЕМУ ИМЕННО ТАК. Объявленный пол выводится ВМЕСТЕ С
ПРИЧИНОЙ. Решение О10 принимает человек, а прогон его исполняет; без
причины строка «кадр выше 75» читается как дефект там, где это записанное
решение, и приёмка начинает блокировать по решениям. Причина живёт в
комментарии YAML той же строки, поэтому читается сырая строка файла:
разбор YAML комментарии снимает.

    python3 pol_slov_po_pdf.py
    python3 pol_slov_po_pdf.py --pdf lec-07-karkas.pdf
"""
import argparse
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import ocenka                                                # noqa: E402

POL_PROCHIH = 75          # медиана деки; норма круга #229, замер 26 дек
PREDEL = 140              # 95-й процентиль эталонных страниц


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="lec-07-karkas.pdf")
    a = ap.parse_args()
    pdf = HERE / a.pdf
    if not pdf.exists():
        print(f"ОТКАЗ: PDF {a.pdf} не найден — пол слов по файлам кадров "
              "не мерится, числа отчёта берутся только с собранного")
        return 2
    fayly = ocenka.files_for(set())
    stranitsy = ocenka.pdf_pages(str(pdf))
    print(f"прочитано: кадров {len(fayly)} · страниц PDF {len(stranitsy)} "
          f"({pdf.name})")
    if len(stranitsy) != len(fayly):
        print(f"ОТКАЗ: страниц {len(stranitsy)}, кадров {len(fayly)} — "
              "сопоставить страницу с кадром нечем, сдвиг на один кадр "
              "дал бы замер по чужим страницам")
        return 2

    rows = [ocenka.ves(f) for f in fayly]
    objavleno, vyshe_pola, vyshe_predela, bez_prichiny = [], [], [], []
    for r, ves in zip(rows, stranitsy):
        pol, declared = ocenka.pol(r)
        if declared:
            objavleno.append((r["id"], pol, ves, r["prichina"]))
            if not r["prichina"]:
                bez_prichiny.append(r["id"])
        if ves > pol:
            vyshe_pola.append((r["id"], ves, pol, declared, r["izmerennyh"]))
        if ves > PREDEL:
            vyshe_predela.append((r["id"], ves))

    med = statistics.median(stranitsy)
    print(f"\nмедиана {med:g} · максимум {max(stranitsy)} · "
          f"не тяжелее {POL_PROCHIH} — "
          f"{100 * sum(1 for x in stranitsy if x <= POL_PROCHIH) / len(stranitsy):.0f}%")

    print(f"\nПОЛ ОБЪЯВЛЕН у {len(objavleno)} кадров "
          f"(решение О10: принимает человек, прогон исполняет):")
    for sid, pol, ves, why in sorted(objavleno, key=lambda x: -x[2]):
        zapas = pol - ves
        print(f"  {sid:6} пол {pol:3} · вес {ves:3} · запас {zapas:+3} — "
              f"{why or 'ПРИЧИНА НЕ НАЗВАНА'}")

    zamechaniy = 0
    if bez_prichiny:
        zamechaniy += len(bez_prichiny)
        print(f"\nЗАМЕЧАНИЕ: пол объявлен без причины — {bez_prichiny}. "
              "Пол без причины неотличим от запаса, взятого на всякий случай")
    ne_objavlen = [x for x in vyshe_pola if not x[3]]
    if ne_objavlen:
        zamechaniy += len(ne_objavlen)
        print(f"\nЗАМЕЧАНИЕ: выше предела {POL_PROCHIH}, пол не объявлен — "
              f"{len(ne_objavlen)} кадров:")
        for sid, ves, pol, _d, nz in ne_objavlen:
            hint = f" · измеренных блоков {nz}" if nz >= 2 else ""
            print(f"  {sid:6} {ves:3} при пределе {pol}{hint}")
    pereves = [x for x in vyshe_pola if x[3]]
    if pereves:
        zamechaniy += len(pereves)
        print("\nЗАМЕЧАНИЕ: тяжелее СВОЕГО ОБЪЯВЛЕННОГО пола — решение есть, "
              "а кадр его перевесил:")
        for sid, ves, pol, _d, _nz in pereves:
            print(f"  {sid:6} {ves} при объявленном {pol}")
    if vyshe_predela:
        zamechaniy += len(vyshe_predela)
        print(f"\nЗАМЕЧАНИЕ: тяжелее предела деки {PREDEL} — {vyshe_predela}")
    if med > POL_PROCHIH:
        zamechaniy += 1
        print(f"\nЗАМЕЧАНИЕ: медиана {med:g} выше нормы {POL_PROCHIH}")

    print(f"\nзамечаний: {zamechaniy}")
    return 1 if zamechaniy else 0


if __name__ == "__main__":
    sys.exit(main())
