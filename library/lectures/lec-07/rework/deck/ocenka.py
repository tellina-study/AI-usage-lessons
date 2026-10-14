#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вес кадра по его файлу — ДО сборки. Один инструмент вместо двух.

**НА ЭТОТ ПРОГОН В ОТЧЁТАХ СОСЫЛАТЬСЯ НЕЛЬЗЯ.** Числа отчёта даёт только
`render_sec.py`: он мерит собранный PDF, то есть страницу, которую видит зал.
Здесь — оценка по файлу кадра, нужная затем, чтобы не гонять сборку (минуты)
на каждую правку абзаца (секунды). Расхождение прогон печатает сам.

Сведён из двух прогонов круга R3 (#229), калиброванных каждый на своём разделе
и потому расходившихся на чужом: `ocenka.py` (раздел 3) и `predict.py`
(раздел 2). Взято из обоих:
* поэлементная раскладка, проверка полосы заметок и сумма минут — от `predict.py`;
* видимый подвал через `markup.source_parts` (голый адрес из строки убирается,
  ссылкой становится название работы), глифы буллитов, стрелки схемы, столбцы
  и снятие разметки таблиц — от `ocenka.py`;
* правило дивайдера (тело повторяет `title`, и в PDF он один) — от `predict.py`.

Калибровка живёт НЕ в коде, а в `ocenka-kalibrovka.json` рядом, и
пересчитывается по готовому PDF — иначе прогон устаревает на следующем круге:

    python3 ocenka.py 3                      # оценка по разделу
    python3 ocenka.py s41 s44 s49b           # по кадрам
    python3 ocenka.py --kalibrovka sec-1-2-3.pdf 1 2 3   # пересчёт по PDF
    python3 ocenka.py --kalibrovka deka.pdf              # … по всей деке
"""
import argparse
import json
import re
import statistics
import sys
from datetime import date
from pathlib import Path

import numpy as np
import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

import build_lec07 as B                                      # noqa: E402
from deckkit import markup, slidefile                        # noqa: E402

KAL = HERE / "ocenka-kalibrovka.json"
# Пол: веса глифов, которые в файле кадра не написаны, а в PDF слова занимают.
# Это ПЕРВОЕ приближение; `--kalibrovka` их перезаписывает по настоящему PDF.
DEFAULT = {"glif_bullita": 1.0, "strelka": 1.0, "glif_stolbtsa": 1.0,
           "a": 1.0, "b": 0.0, "istochnik": "пол, без калибровки"}


def kal():
    if KAL.exists():
        return {**DEFAULT, **json.loads(KAL.read_text(encoding="utf-8"))}
    return dict(DEFAULT)


def sl(x):
    """Слова так, как считает fitz: по пробелам, разметка снята."""
    x = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(x or ""))
    x = re.sub(r"[*_`#]", " ", x)
    return len(x.split())


def body_parts(body):
    """Тело кадра → (слов, буллитов). Таблица отдаёт содержимое клеток:
    в PDF рисуется таблица, а не её разметка — `|` и ряд `|---|` словами не
    становятся. На этом прежняя версия завышала свод `s49d` на 21 слово."""
    w = n_bul = 0
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if re.fullmatch(r"\|[\s:|-]+\|", ln):      # ряд-разделитель таблицы
            continue
        if ln.startswith("|"):
            w += sl(ln.strip("|").replace("|", " "))
            continue
        w += sl(ln)
        if ln.startswith(("- ", "* ")):
            n_bul += 1
    return w, n_bul


def n_izm(bl, body):
    """Сколько на кадре ИЗМЕРЕННЫХ блоков — плашек с числом и базой при нём
    либо строк таблицы с числом. Это ПОКАЗАНИЕ, а не порог: решение О10
    (кадр, несущий измеренные блоки с разрядом и выборкой, живёт по полу 140)
    принимает человек и записывает в кадр полем `pol_slov`. Прогон сам порог
    не ослабляет — иначе он прятал бы настоящие нарушения, а сторож, который
    молча поднимает планку, хуже отсутствующего. Этот счёт печатается затем,
    чтобы основание для такого решения было видно рядом с весом."""
    n = sum(1 for b in bl if isinstance(b, dict)
            and re.search(r"\d", str(b.get("value") or ""))
            and str(b.get("note") or "").strip())
    n += sum(1 for ln in body.splitlines()
             if ln.strip().startswith("|") and re.search(r"\d", ln)
             and not re.fullmatch(r"\|[\s:|-]+\|", ln.strip()))
    return n


def ves(f, k=None):
    k = k or kal()
    t = Path(f).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    fm = yaml.safe_load(m.group(1)) or {}
    rest = m.group(2)
    vis = re.search(r"## Видимый текст слайда\n(.*?)(?=\n## |\Z)", rest, re.S)
    nts = re.search(r"## Заметки лектора\n(.*?)(?=\n## |\Z)", rest, re.S)

    # дивайдер печатает заголовок телом — в PDF он один, не два
    w_title = 0 if fm.get("type") == "divider" else sl(fm.get("title"))
    w_body, n_bul = body_parts(vis.group(1) if vis else "")

    bl = fm.get("blocks") or []
    w_bl = sum(sl(b.get("label")) + sl(b.get("value")) + sl(b.get("note"))
               for b in bl if isinstance(b, dict))

    sc = fm.get("scheme") or {}
    w_sc = n_arr = 0
    if isinstance(sc, dict) and sc.get("rows"):
        w_sc = sl(sc.get("caption"))
        for r in sc["rows"]:
            steps = r.get("steps") or []
            w_sc += sl(r.get("label")) + sum(sl(s) for s in steps)
            if r.get("arrows", True) is not False:
                n_arr += max(0, len(steps) - 1)

    co = fm.get("columns") or {}
    w_co = n_ci = 0
    if isinstance(co, dict):
        for side in ("left", "right"):
            c = co.get(side) or {}
            w_co += sl(c.get("head"))
            for it in (c.get("items") or []):
                w_co += sl(it)
                n_ci += 1

    src = str(fm.get("source") or "").strip()
    cap = str(fm.get("media_caption") or "").strip()
    if cap and fm.get("media_hero"):
        src = f"{src} · {cap}" if src and src != "—" else cap
    w_ft = (sum(sl(v) for v, _u in markup.source_parts(src))
            if src and src != "—" else 0)

    base = w_title + w_body + w_bl + w_sc + w_co + w_ft
    glifs = (n_bul * k["glif_bullita"] + n_arr * k["strelka"]
             + n_ci * k["glif_stolbtsa"])
    return dict(
        id=str(fm.get("id")), tip=str(fm.get("type") or ""),
        sec=str(fm.get("section") or "").split(".")[0].strip(),
        title=w_title, blocks=w_bl, nbl=len(bl), scheme=w_sc, cols=w_co,
        body=w_body, foot=w_ft, glifs=glifs,
        n_bul=n_bul, n_arr=n_arr, n_ci=n_ci, base=base,
        ves=int(round(k["a"] * (base + glifs) + k["b"])),
        notes=sl(nts.group(1) if nts else ""),
        timing=float(fm.get("timing_min") or 0),
        razbor=any(str(s).startswith(("①", "②"))
                   for s in (fm.get("method_steps") or [])),
        izmerennyh=n_izm(bl, vis.group(1) if vis else ""),
        pol_slov=int(fm.get("pol_slov") or 0))


def pol(r):
    """Предел слов для кадра: объявленный полем `pol_slov` (решение О10,
    записанное в кадр), иначе 140 разбору по ①/② и 75 всем прочим."""
    if r["pol_slov"]:
        return r["pol_slov"], True
    return (140 if r["razbor"] else 75), False


def files_for(args):
    """Кадры по номерам разделов и/или по идентификаторам, в порядке деки."""
    out = []
    for f in slidefile.slide_files(B.SLIDES_DIR):
        t = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---", t, re.S)
        fm = yaml.safe_load(m.group(1)) if m else {}
        fm = fm or {}
        sec = str(fm.get("section") or "").split(".")[0].strip()
        if not args or sec in args or str(fm.get("id")) in args:
            out.append(f)
    return out


def pdf_pages(pdf):
    import fitz
    d = fitz.open(pdf)
    return [len(p.get_text().split()) for p in d]


def kalibrovka(pdf, secs):
    """Пересчёт весов глифов и аффинной поправки по СОБРАННОМУ PDF.

    Страница к кадру сопоставляется порядком деки — тем же, которым собирает
    `render_sec.py`. Расхождение числа страниц и кадров — отказ, а не подгонка:
    сдвиг на один кадр откалибровал бы прогон на чужих страницах."""
    fs = files_for(set(secs))
    rows = [ves(f, DEFAULT) for f in fs]
    real = pdf_pages(pdf)
    if len(real) != len(rows):
        print(f"ОТКАЗ: в PDF страниц {len(real)}, кадров по разделам "
              f"{secs or 'вся дека'} — {len(rows)}. Сопоставить нечем.")
        return 1
    # невязка = настоящее − структурный счёт; объясняем её глифами и сдвигом
    A = np.array([[r["n_bul"], r["n_arr"], r["n_ci"], 1.0] for r in rows])
    y = np.array([t - r["base"] for t, r in zip(real, rows)], dtype=float)
    w, *_ = np.linalg.lstsq(A, y, rcond=None)
    k = {"glif_bullita": round(float(w[0]), 3),
         "strelka": round(float(w[1]), 3),
         "glif_stolbtsa": round(float(w[2]), 3),
         "a": 1.0, "b": round(float(w[3]), 3),
         "istochnik": f"{Path(pdf).name}, разделы {','.join(secs) or 'вся дека'}, "
                      f"{len(real)} страниц, {date.today().isoformat()}"}
    err = [ves(f, k)["ves"] - t for f, t in zip(fs, real)]
    k["oshibka"] = {"median_abs": round(float(np.median(np.abs(err))), 2),
                    "mean": round(float(np.mean(err)), 2),
                    "max_abs": int(np.max(np.abs(err)))}
    by = {}
    for r, e in zip(rows, err):
        by.setdefault(r["sec"], []).append(e)
    k["oshibka_po_razdelam"] = {
        s: {"n": len(v), "median_abs": round(float(np.median(np.abs(v))), 2),
            "mean": round(float(np.mean(v)), 2)} for s, v in sorted(by.items())}
    KAL.write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    print(f"калибровка записана в {KAL.name}")
    print(f"  глиф буллита {k['glif_bullita']} · стрелка {k['strelka']} · "
          f"глиф столбца {k['glif_stolbtsa']} · сдвиг {k['b']}")
    print(f"  ошибка на наборе: медиана |Δ| {k['oshibka']['median_abs']} · "
          f"среднее Δ {k['oshibka']['mean']:+} · макс |Δ| {k['oshibka']['max_abs']}")
    print("  по разделам:")
    for s, v in k["oshibka_po_razdelam"].items():
        print(f"    раздел {s or '—':3} n={v['n']:3} медиана |Δ| "
              f"{v['median_abs']:5} · среднее Δ {v['mean']:+}")
    return 0


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("tseli", nargs="*", help="номера разделов и/или id кадров")
    ap.add_argument("--kalibrovka", metavar="PDF",
                    help="пересчитать веса по собранному PDF")
    a = ap.parse_args()
    if a.kalibrovka:
        return kalibrovka(a.kalibrovka, a.tseli)

    k = kal()
    rows = [ves(f, k) for f in files_for(set(a.tseli))]
    if not rows:
        print("кадров не найдено")
        return 1
    print(f"{'кадр':6} {'тип':10} {'ВЕС':>4} | {'загл':>4} {'плашки':>7} "
          f"{'схема':>5} {'стлб':>4} {'тело':>4} {'подв':>4} | "
          f"{'изм':>3} {'заметки':>7} {'мин':>4}")
    for r in rows:
        pred, declared = pol(r)
        flag = f"  ← тяжелее {pred}" if r["ves"] > pred else ""
        if declared:
            flag += f"  [пол {pred} объявлен, измеренных блоков {r['izmerennyh']}]"
        nf = "" if 500 <= r["notes"] <= 800 else "  заметки вне 500–800"
        print(f"{r['id']:6} {r['tip']:10} {r['ves']:4} | {r['title']:4} "
              f"{r['blocks']:4}({r['nbl']}) {r['scheme']:5} {r['cols']:4} "
              f"{r['body']:4} {r['foot']:4} | {r['izmerennyh']:3} "
              f"{r['notes']:7} "
              f"{r['timing']:4.2f}{flag}{nf}")
    v = [r["ves"] for r in rows]
    rz = [r["ves"] for r in rows if pol(r)[0] == 140]
    pr = [r["ves"] for r in rows if pol(r)[0] != 140]
    vne = [(r["id"], r["ves"], pol(r)[0], r["izmerennyh"])
           for r in rows if r["ves"] > pol(r)[0]]
    print(f"\nкадров {len(v)} · медиана {statistics.median(v):g} · "
          f"максимум {max(v)} · тяжелее 140 — {sum(1 for x in v if x > 140)}")
    if rz:
        print(f"  по полу 140 ({len(rz)}: разборы + кадры с измеренными "
              f"блоками, О10): в полосе 105–140 — "
              f"{sum(1 for x in rz if 105 <= x <= 140)}, тяжелее 140 — "
              f"{sum(1 for x in rz if x > 140)}")
    if pr:
        print(f"  по полу 75 ({len(pr)}): тяжелее 75 — "
              f"{sum(1 for x in pr if x > 75)}")
    if vne:
        print("  ВНЕ ПРЕДЕЛА:")
        for i, v, pr_, nz in vne:
            hint = (f" — измеренных блоков {nz}; если это решение О10, "
                    f"объяви `pol_slov: 140` в кадре") if nz >= 2 and pr_ == 75 else ""
            print(f"    {i}: {v} при пределе {pr_}{hint}")
    print(f"минут {sum(r['timing'] for r in rows):.2f} · заметки "
          f"{min(r['notes'] for r in rows)}–{max(r['notes'] for r in rows)}")
    o = k.get("oshibka")
    print(f"\nкалибровка: {k['istochnik']}")
    if o:
        print(f"ошибка ЭТОГО прогона против собранного PDF: медиана |Δ| "
              f"{o['median_abs']} · среднее Δ {o['mean']:+} · макс |Δ| "
              f"{o['max_abs']}. Числа отчёта берут из `render_sec.py`.")
    else:
        print("ошибка не замерена: калибровки нет. Прогон на полу весов, "
              "числам верить нельзя — сделай `--kalibrovka <pdf>`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
