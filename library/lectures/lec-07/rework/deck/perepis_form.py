#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перепись ФОРМ по кадрам деки: какая форма у кадра сейчас, из чего она собрана.

Зачем отдельно от замеров слов: диета мерила, СКОЛЬКО текста на кадре; эта
перепись отвечает на другой вопрос — ЧЕМ он показан. Разнарядка форм
(`RAZNARYADKA-FORM.md`) опирается на её числа, а не на глаз.

Форма кадра читается из фронтматтера (`blocks` / `scheme` / `columns` / `media`)
и из тела (буллиты, таблицы, цитата). Самоотчёт кадра (`form:`) НЕ используется:
это поле про форму разбора в словаре курса, а не про визуальную форму.

    python3 perepis_form.py              # словарь форм + таблица по кадрам
    python3 perepis_form.py --seriya     # самые длинные серии одной формы подряд
"""
import argparse, re, sys
from collections import Counter, defaultdict
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"


def read(f):
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---(.*)", t, re.S)
    meta = yaml.safe_load(m.group(1)) or {}
    rest = m.group(2)
    body = re.split(r"## Заметки лектора", rest)[0]
    body = re.sub(r"^## Видимый текст слайда\s*", "", body.strip())
    return meta, body


def elements(meta, body):
    """Какие визуальные элементы реально стоят на кадре."""
    el = []
    nb = len(meta.get("blocks") or [])
    if nb:
        el.append("плашки×%d" % nb)
    sc = meta.get("scheme") or {}
    rows = sc.get("rows") or []
    if rows:
        steps = sum(len(r.get("steps") or []) for r in rows)
        el.append("схема %dр×%dш" % (len(rows), steps))
    if meta.get("columns"):
        el.append("столбцы")
    if (meta.get("media") or "").strip():
        el.append("снимок")
    if re.search(r"^\s*[-•]\s+\S", body, re.M):
        el.append("буллиты×%d" % len(re.findall(r"^\s*[-•]\s+\S", body, re.M)))
    if re.search(r"^\s*\|.+\|", body, re.M):
        el.append("таблица")
    if re.search(r"^\s*>", body, re.M) or "«" in body and body.count("«") >= 2:
        pass
    return el


def forma(meta, body):
    """Одно имя формы — то, чем кадр ЧИТАЕТСЯ в первую очередь."""
    nb = len(meta.get("blocks") or [])
    sc = (meta.get("scheme") or {}).get("rows") or []
    cols = bool(meta.get("columns"))
    med = bool((meta.get("media") or "").strip())
    bul = len(re.findall(r"^\s*[-•]\s+\S", body, re.M))
    tab = bool(re.search(r"^\s*\|.+\|", body, re.M))
    t = meta.get("type") or ""
    if tab:                      return "таблица"
    if med and nb == 0 and sc == [] and bul == 0: return "кадр-снимок"
    if nb and sc:                return "плашки + схема"
    if sc:                       return "схема рядами"
    if cols:                     return "два столбца"
    if nb == 1:                  return "одна плашка"
    if nb:                       return "полоса плашек"
    if bul:                      return "буллиты"
    if t == "divider":           return "дивайдер (текст)"
    return "только текст"


_NE_POSLED = ("откуда", "источник", "механизм", "способ", "перечень", "набор",
              "две дорожки", "устройство", "виды", "участник", "кто ")


def _podozr(cap):
    """Подпись намекает на перечень/набор/устройство, а не на порядок работы."""
    c = cap.lower()
    return any(k in c for k in _NE_POSLED)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seriya", action="store_true")
    ap.add_argument("--strelki", action="store_true",
                    help="схемы: утверждает ли стрелка последовательность, которой нет")
    a = ap.parse_args()

    files = sorted([f for f in SLIDES.glob("*.md") if f.name != "README.md"],
                   key=lambda f: (int(re.match(r"s(\d+)", f.name).group(1)),
                                  re.match(r"s\d+([a-z]*)", f.name).group(1)))
    rows = []
    for f in files:
        meta, body = read(f)
        sid = str(meta.get("id") or f.name.split("-")[0])
        sec = str(meta.get("section") or "—")
        rows.append(dict(id=sid, file=f.name, sec=sec.split(".")[0],
                         secname=sec, type=meta.get("type") or "",
                         forma=forma(meta, body), el=elements(meta, body),
                         media=bool((meta.get("media") or "").strip()),
                         scheme=(meta.get("scheme") or {}),
                         mneed=(meta.get("media_needed") or "").strip()))

    print("кадров: %d\n" % len(rows))
    print("=== СЛОВАРЬ ФОРМ ===")
    c = Counter(r["forma"] for r in rows)
    for k, v in c.most_common():
        print("  %-18s %3d   %4.1f%%" % (k, v, 100 * v / len(rows)))
    print("\n  всего разных форм: %d" % len(c))
    nm = sum(1 for r in rows if r["media"])
    print("  со снимком: %d · без единого снимка: %d" % (nm, len(rows) - nm))
    print("  таблиц: %d" % c.get("таблица", 0))

    print("\n=== ПРИОРИТЕТ: кадры, где форма мешает смыслу ===")
    tekst = [r for r in rows if r["forma"] in ("только текст", "дивайдер (текст)")]
    tri = [r for r in rows if r["forma"] == "полоса плашек"
           and len(r["el"]) == 1 and r["el"][0] == "плашки×3"]
    print("  только текст / дивайдер без элементов: %d" % len(tekst))
    print("   ", " ".join(r["id"] for r in tekst))
    print("  ровно три плашки и больше ничего: %d" % len(tri))
    print("   ", " ".join(r["id"] for r in tri))

    if a.seriya:
        print("\n=== СЕРИИ ОДНОЙ ФОРМЫ ПОДРЯД ===")
        best = []
        i = 0
        while i < len(rows):
            j = i
            while j + 1 < len(rows) and rows[j + 1]["forma"] == rows[i]["forma"]:
                j += 1
            if j - i + 1 >= 3:
                best.append((j - i + 1, rows[i]["forma"],
                             rows[i]["id"] + "…" + rows[j]["id"]))
            i = j + 1
        for n, f_, rng in sorted(best, reverse=True)[:12]:
            print("  %d подряд  %-18s %s" % (n, f_, rng))
        if not best:
            print("  серий из 3 и длиннее нет")

    if a.strelki:
        print("\n=== СХЕМЫ: СТРЕЛКА — ЭТО УТВЕРЖДЕНИЕ «СНАЧАЛА ОДНО, ПОТОМ ДРУГОЕ» ===")
        print("  `arrows` истинен по умолчанию: схема без явного `arrows: false`")
        print("  рисует конвейер. Перечень, набор источников, параллельные механизмы")
        print("  и две дорожки конвейером не являются — у них стрелка лжёт.\n")
        for r in rows:
            sc = r["scheme"]
            if not (sc.get("rows") or []):
                continue
            ar = sc.get("arrows", True)
            steps = sum(len(x.get("steps") or []) for x in sc.get("rows") or [])
            cap = (sc.get("caption") or "").strip()
            mark = "  " if not ar else ("←СВЕРИТЬ" if _podozr(cap) else "  ")
            print("  %-6s стрелки=%-5s шагов=%2d %s %s"
                  % (r["id"], ar, steps, mark, cap[:54] or "(без подписи)"))

    print("\n=== ПО РАЗДЕЛАМ ===")
    byn = defaultdict(list)
    for r in rows:
        byn[r["sec"]].append(r)
    for k in sorted(byn, key=lambda x: (not x.isdigit(), x)):
        rs = byn[k]
        cc = Counter(r["forma"] for r in rs)
        print("  раздел %-3s %2d кадров · снимков %d · форм %d · %s"
              % (k, len(rs), sum(1 for r in rs if r["media"]), len(cc),
                 ", ".join("%s×%d" % (a_, b_) for a_, b_ in cc.most_common())))
    return rows


if __name__ == "__main__":
    main()
