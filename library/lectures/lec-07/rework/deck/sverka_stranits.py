#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сверка СТРАНИЦЫ с КАДРОМ по заголовку: стоит ли страница на своём кадре.

Зачем отдельно от замера. Прогоны по собранному PDF сопоставляют страницу с
кадром ПОРЯДКОМ и отказывают только на расхождении ЧИСЛА («страниц 101,
кадров 99 — сопоставить нечем»). Но совпадение числа не означает совпадения
порядка: PDF, склеенный из секционных кусков, даёт ровно то же число при
сдвиге на один кадр, и тогда замер идёт по чужим страницам, а все до одного
числа выглядят правдоподобно.

Поймала это не проверка, а человек: сессия разделов 7–10 собрала 101 страницу
из четырёх секционных PDF и ПЕРЕД замером сверила постранично, что каждая
страница стоит на своём кадре. Эта работа держалась на её внимательности —
здесь она становится прогоном.

ЧТО СЧИТАЕТСЯ ЗАГОЛОВКОМ СТРАНИЦЫ. У обложки и дивайдера поле `title` на
экран не выводится вовсе: их строители рисуют только тело, а заголовок стоит
первой строкой тела (то же правило, которым считается их вес). У остальных
сверяется поле `title`. Сравнение по доле слов заголовка, найденных на
странице: перенос, мягкий дефис и разрядка ломают посимвольное равенство, но
не словарь.

    python3 sverka_stranits.py
    python3 sverka_stranits.py --pdf sklejka.pdf
    python3 sverka_stranits.py --samoproverka
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import yaml                                                  # noqa: E402
import build_lec07 as B                                      # noqa: E402
from deckkit import slidefile                                # noqa: E402

PORRG = 0.60      # доля слов заголовка, которую надо найти на странице


def slova(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(s or ""))
    s = re.sub(r"[*_`#«»„“”\"]", " ", s)
    s = s.replace("­", "").replace("‑", "-")
    return [w for w in re.findall(r"[^\W\d_]+", s.lower()) if len(w) > 2]


def zagolovok(f):
    """Что у этого кадра стоит заголовком НА ЭКРАНЕ."""
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    fm = yaml.safe_load(m.group(1)) or {}
    if str(fm.get("type")) in B.BUILDERS:
        telo = m.group(2).split("## Видимый текст слайда", 1)[-1]
        for ln in telo.splitlines():
            if ln.strip().startswith("#"):
                return str(fm.get("id")), ln.strip("# ").strip()
        return str(fm.get("id")), ""
    return str(fm.get("id")), str(fm.get("title") or "")


def dolya(zag, tekst_stranitsy):
    """Доля слов заголовка, найденных на странице."""
    nuzhno = slova(zag)
    if not nuzhno:
        return None
    est = set(slova(tekst_stranitsy))
    return sum(1 for w in nuzhno if w in est) / len(nuzhno)


def prichina(tekst, fayly, i, porog, okno=2):
    """Почему заголовок не совпал — СДВИГ или УСТАРЕВШИЙ PDF.

    Признак дешёвый и назван сессией разделов 7–10 по своему случаю: при
    сдвиге порядка заголовок страницы совпадёт с СОСЕДНИМ кадром (±1…2),
    при устаревшем PDF — ни с одним. У неё на странице 1 стояла прежняя
    обложка: страница была на своём месте, а содержание старое, и она
    минуту искала сдвиг там, где его не было.

    Для замера разницы нет — мерить нельзя в обоих случаях, и отказ
    правильный. Для чтения разница большая: это две разные починки.
    Поэтому прогон называет причину, а не только симптом."""
    for d in list(range(1, okno + 1)) + [-x for x in range(1, okno + 1)]:
        j = i + d
        if 0 <= j < len(fayly):
            sid, zag = zagolovok(fayly[j])
            dl = dolya(zag, tekst)
            if dl is not None and dl >= porog:
                return ("сдвиг", sid, d)
    return ("устарел", None, 0)


def proverit(pdf, fayly=None, porog=PORRG):
    """(находки, прочитано) — страницы, чей заголовок не совпал с кадром."""
    import fitz
    fayly = fayly or list(slidefile.slide_files(B.SLIDES_DIR))
    d = fitz.open(str(pdf))
    prochitano = {"страниц": d.page_count, "кадров": len(fayly)}
    if d.page_count != len(fayly):
        return [{"pusto": True, "prichina":
                 f"страниц {d.page_count}, кадров {len(fayly)}"}], prochitano
    nakhodki = []
    for i, f in enumerate(fayly):
        sid, zag = zagolovok(f)
        dl = dolya(zag, d[i].get_text())
        if dl is None or dl >= porog:
            continue
        vid, sosed, sm = prichina(d[i].get_text(), fayly, i, porog)
        nakhodki.append({"stranitsa": i + 1, "kadr": sid, "dolya": dl,
                         "zagolovok": zag[:70], "vid": vid,
                         "sosed": sosed, "smeshchenie": sm})
    return nakhodki, prochitano


def samoproverka():
    """Сторож обязан срабатывать на сдвиге — иначе он печатает только ноль."""
    pdf = HERE / "lec-07-karkas.pdf"
    if not pdf.exists():
        print("ОТКАЗ: нет PDF для самопроверки")
        return 2
    fayly = list(slidefile.slide_files(B.SLIDES_DIR))
    proby = []
    n0, pr = proverit(pdf, fayly)
    proby.append(("на своём порядке молчит", not n0))
    sdvig = fayly[1:] + fayly[:1]
    n1, _ = proverit(pdf, sdvig)
    proby.append(("на сдвиге в один кадр срабатывает", len(n1) > len(fayly) // 2))
    proby.append(("сдвиг назван сдвигом, а не устареванием",
                  sum(1 for n in n1 if n["vid"] == "сдвиг") > len(n1) * 0.8))
    # Устаревшее содержание: страница на месте, заголовок ничей. Берём кадр,
    # заголовка которого в деке нет ни на одной странице.
    import tempfile
    with tempfile.TemporaryDirectory() as dd:
        chuzhoy = Path(dd) / "s01-chuzhoy.md"
        chuzhoy.write_text("---\nid: s01\ntype: norm\n"
                           "title: \"Небывалый заголовок про квазимонохромный "
                           "ферромагнетик\"\n---\n\n"
                           "## Видимый текст слайда\n\nТекст.\n", encoding="utf-8")
        n3, _ = proverit(pdf, [chuzhoy] + fayly[1:])
        svoi = [n for n in n3 if n["stranitsa"] == 1]
        proby.append(("устаревшее содержание названо устареванием",
                      bool(svoi) and svoi[0]["vid"] == "устарел"))
    n2, _ = proverit(pdf, fayly[:-1])
    proby.append(("на нехватке кадра отказывает", bool(n2) and n2[0].get("pusto")))
    ploho = 0
    for imya, ok in proby:
        print(f"  {'✓' if ok else '✗ ПРОВАЛ'}  {imya}")
        ploho += not ok
    if not n0:
        print(f"  (на порядке деки: страниц {pr['страниц']}, расхождений 0; "
              f"на сдвиге: {len(n1)})")
    return 1 if ploho else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default="lec-07-karkas.pdf")
    ap.add_argument("--porog", type=float, default=PORRG)
    ap.add_argument("--samoproverka", action="store_true")
    a = ap.parse_args()
    if a.samoproverka:
        return samoproverka()
    pdf = HERE / a.pdf if not Path(a.pdf).is_absolute() else Path(a.pdf)
    if not pdf.exists():
        print(f"ОТКАЗ: PDF {a.pdf} не найден")
        return 2
    nakhodki, pr = proverit(pdf, porog=a.porog)
    print(f"прочитано: страниц {pr['страниц']} · кадров {pr['кадров']} "
          f"· порог доли слов заголовка {a.porog}")
    if nakhodki and nakhodki[0].get("pusto"):
        print(f"ОТКАЗ: {nakhodki[0]['prichina']} — сверять нечем")
        return 2
    if not nakhodki:
        print("каждая страница стоит на своём кадре — расхождений 0")
        return 0
    print(f"\nЗАМЕЧАНИЕ: страниц не на своём кадре — {len(nakhodki)}. "
          "Замер по такому PDF идёт по чужим страницам:")
    for n in nakhodki:
        print(f"  стр. {n['stranitsa']:3} ждали кадр {n['kadr']:6} "
              f"«{n['zagolovok']}» — нашлось {n['dolya'] * 100:.0f}% слов")
    return 1


if __name__ == "__main__":
    sys.exit(main())
