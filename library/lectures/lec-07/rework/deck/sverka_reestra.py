#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""РЕЕСТР РАЗБОРОВ НА ДИВАЙДЕРЕ = ЗАГОЛОВКИ КАДРОВ. Сверка, не ревью по памяти.

ЗАЧЕМ. `storozha-i-priyomka.md` §14 требует «автоматический diff `title:`
кадров `case` против текста дивайдера при каждой пересборке, 0 расхождений,
не ревью по памяти», а `trebovaniya-k-soderzhaniyu-forma.md` §5.16 —
«дивайдер называет разборы раздела по порядку, ДОСЛОВНО теми же
заголовками, что стоят на их кадрах». Цена пропуска измерена чтением
Лекции 6: лектор семь раз за вечер узнавал слайд на экране, потому что
дивайдер говорил, о чём раздел, и не говорил, какие в нём разборы. В
разделе 1 Лекции 7 дивайдер цитировал «Пример 2: глазное дно снимают на
приёме, а не у офтальмолога» при фактическом заголовке «Пример 2: целевой
скрининг осложнения у диабетиков, не у офтальмолога» — две разные строки,
и расхождение прожило четыре круга правок.

ЧТО СВЕРЯЕТСЯ. Головной кадр каждого разбора — ПЕРВЫЙ по порядку показа
кадр с этим номером, какой бы формой заголовок ни был набран: и «Пример 1:
…», и «Пример 1, без модели: …» одинаково годятся в головные, потому что
разбор на несколько кадров может начинаться с любой своей части (раздел 1
начинает Примера 1 с классических режимов — «Пример 1, без модели:
шведская программа зовёт по возрасту», и это он и есть). Его заголовок
обязан встретиться в видимом теле дивайдера ДОСЛОВНО. Остальные кадры того
же номера на дивайдере не называются.

ЧТО ПРОВЕРЯЕТСЯ ОТДЕЛЬНО. Нумерация: номера разборов раздела обязаны идти
подряд с единицы, без дыр и повторов, — счётчик в прозе ни один генератор
не пересобирает (`seminar-production/README.md` §8.10).

    python3 sverka_reestra.py            # все разделы
    python3 sverka_reestra.py 1          # один раздел
    python3 sverka_reestra.py --selftest
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"

GOLOVNOY = re.compile(r"^Пример\s+(\d+)\s*:")
PRODOLZHENIE = re.compile(r"^Пример\s+(\d+)\s*,")


def kadry(katalog=None):
    out = []
    for f in sorted((katalog or SLIDES).glob("s*.md")):
        s = f.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", s, re.S)
        if not m:
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except Exception:
            continue
        telo = s[m.end():].partition("## Заметки лектора")[0]
        out.append((meta, telo, f.name))
    return out


def sverit(nomera_razdelov=None, katalog=None, tiho=False):
    vse = kadry(katalog)
    razdely = defaultdict(lambda: {"divider": None, "golovnye": [], "vse_nomera": []})
    for meta, telo, imya in vse:
        sec = str(meta.get("section") or "")
        nomer = sec.split(".")[0].strip()
        if nomera_razdelov and nomer not in nomera_razdelov:
            continue
        r = razdely[sec]
        if str(meta.get("type")) == "divider":
            r["divider"] = (meta, telo, imya)
        zag = str(meta.get("title") or "")
        mm = GOLOVNOY.match(zag) or PRODOLZHENIE.match(zag)
        if mm:
            r["vse_nomera"].append(int(mm.group(1)))
            # Головной — ПЕРВЫЙ кадр этого номера по порядку показа; файлы
            # уже отсортированы, значит первый встреченный и есть он.
            if int(mm.group(1)) not in {n for n, _, _ in r["golovnye"]}:
                r["golovnye"].append((int(mm.group(1)), zag, imya))

    besh = 0
    for sec in sorted(razdely):
        r = razdely[sec]
        if not r["golovnye"]:
            continue
        if not tiho:
            print(f"\n{sec}")
        div = r["divider"]
        if div is None:
            print("  [!] дивайдера нет — сверять не с чем")
            besh += 1
            continue
        tekst = " ".join(div[1].split())
        for nomer, zag, imya in sorted(r["golovnye"]):
            est = " ".join(zag.split()) in tekst
            if not tiho:
                print(f"  {'ok ' if est else 'НЕТ'} «{zag}»  ({imya})")
            if not est:
                besh += 1

        nomera = sorted(set(r["vse_nomera"]))
        zhdyom = list(range(1, len(nomera) + 1))
        if nomera != zhdyom:
            print(f"  [!] нумерация разборов {nomera}, ожидалась {zhdyom}")
            besh += 1
        golovnyh = sorted(n for n, _, _ in r["golovnye"])
        if golovnyh != sorted(set(golovnyh)):
            print(f"  [!] два головных кадра под одним номером: {golovnyh}")
            besh += 1

    if not tiho:
        print(f"\nрасхождений {besh}")
        if besh == 0:
            print("ДИВАЙДЕР И ЗАГОЛОВКИ СОВПАДАЮТ ДОСЛОВНО — сверено строками, "
                  "не прочитано глазами.")
    return besh


def selftest():
    """Сверка обязана поймать расхождение, которое мы сами подложили."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        k = Path(d)
        (k / "s01-divider.md").write_text(
            '---\nid: s01\nsection: "9. Проба"\ntype: divider\n'
            'title: "9. Проба"\n---\n\n## Видимый текст слайда\n\n'
            "По порядку: **Пример 1: верный заголовок** · "
            "**Пример 2: НЕ ТОТ заголовок**\n\n## Заметки лектора\n\nх\n",
            encoding="utf-8")
        (k / "s02-a.md").write_text(
            '---\nid: s02\nsection: "9. Проба"\ntype: case\n'
            'title: "Пример 1: верный заголовок"\n---\n\n'
            "## Видимый текст слайда\n\nх\n\n## Заметки лектора\n\nх\n",
            encoding="utf-8")
        (k / "s03-b.md").write_text(
            '---\nid: s03\nsection: "9. Проба"\ntype: case\n'
            'title: "Пример 2: другой заголовок"\n---\n\n'
            "## Видимый текст слайда\n\nх\n\n## Заметки лектора\n\nх\n",
            encoding="utf-8")
        besh = sverit(katalog=k, tiho=True)
    ok = besh == 1
    print(f"selftest: подложено одно расхождение, сверка нашла {besh}")
    print("selftest ПРОШЁЛ — нулю этой сверки можно верить" if ok
          else "selftest ПРОВАЛЕН — нулю этой сверки верить НЕЛЬЗЯ")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("razdely", nargs="*")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return 1 if sverit(set(a.razdely) or None) else 0


if __name__ == "__main__":
    sys.exit(main())
