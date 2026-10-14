#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Быстрая ОЦЕНКА числа слов на странице PDF по файлу кадра — без сборки.

Зачем: сборка раздела идёт минутами, а правка кадра требует десятка проб.
Счёт PDF — это `len(page.get_text().split())`, то есть по пробелам, и в него
входят заголовок, тело, плашки, схема, столбцы и подвал. Разделители «·» и
глифы буллитов — тоже слова этого счёта.

Оценка КАЛИБРУЕТСЯ по 20 известным числам раздела 3 (замер до правок), и
прогон печатает свою ошибку — пользоваться можно только пока она мала.

    python3 ocenka.py 3            # оценка по разделу
    python3 ocenka.py s41 s42      # по кадрам
"""
import re
import sys
import glob
import statistics

import yaml
HERE = __import__("pathlib").Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))
from deckkit import markup  # noqa: E402

BASE = {  # замер собранного PDF до правок — render_sec.py 3, 2026-10-14
    "s35": 69, "s35a": 199, "s36": 198, "s37": 152, "s38": 196, "s41": 191,
    "s42": 150, "s43": 181, "s44": 168, "s44a": 147, "s45": 192, "s46": 120,
    "s47": 211, "s48": 204, "s49": 225, "s49a": 185, "s49b": 189,
    "s49c": 167, "s49d": 194, "s50": 217,
}


def toks(s):
    """Слова так, как их считает fitz: по пробелам, разметка снята."""
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(s or ""))
    s = re.sub(r"https?://\S+", " ", s)          # голый адрес из подвала убран
    s = re.sub(r"[*_`#]", " ", s)
    return len(s.split())


def count(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", t, re.S)
    meta = yaml.safe_load(m.group(1)) or {}
    n = 0
    n += toks(meta.get("title"))
    body = ""
    if "## Видимый текст слайда" in t:
        body = t.split("## Видимый текст слайда", 1)[1].split("## Заметки лектора")[0]
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        n += toks(ln)
        if ln.startswith(("- ", "* ")):
            n += 1                                # глиф буллита — слово счёта
    for b in (meta.get("blocks") or []):
        n += toks(b.get("label")) + toks(b.get("value")) + toks(b.get("note"))
    sch = meta.get("scheme") or {}
    if isinstance(sch, dict) and sch.get("rows"):
        n += toks(sch.get("caption"))
        for r in sch["rows"]:
            n += toks(r.get("label"))
            for st in (r.get("steps") or []):
                n += toks(st)
            if r.get("arrows", True) is not False:
                n += max(0, len(r.get("steps") or []) - 1)   # стрелки
    cols = meta.get("columns") or {}
    if isinstance(cols, dict):
        for side in ("left", "right"):
            c = cols.get(side) or {}
            n += toks(c.get("head"))
            for i in (c.get("items") or []):
                n += toks(i) + 1
    src = str(meta.get("source") or "").strip()
    if src and src != "—":
        n += sum(toks(v) for v, _u in markup.source_parts(src))
    cap = str(meta.get("media_caption") or "").strip()
    if cap and meta.get("media_hero"):
        n += toks(cap)
    return str(meta.get("id")), n


def files_for(args):
    out = []
    for f in sorted(glob.glob("slides/s*.md")):
        t = open(f, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---", t, re.S)
        meta = yaml.safe_load(m.group(1)) or {}
        sec = str(meta.get("section") or "").split(".")[0].strip()
        sid = str(meta.get("id"))
        if sec in args or sid in args:
            out.append(f)
    return out


def main():
    args = set(sys.argv[1:]) or {"3"}
    rows, errs = [], []
    for f in files_for(args):
        sid, n = count(f)
        b = BASE.get(sid)
        rows.append((sid, n, b, f))
        if b:
            errs.append(n - b)
    rows.sort(key=lambda r: (len(r[0]), r[0]))
    for sid, n, b, f in rows:
        d = f"  (было {b}, Δ{n - b:+d})" if b else ""
        flag = ""
        if n > 140:
            flag = "  ← ТЯЖЕЛЕЕ 140"
        elif n > 75:
            flag = "  ← тяжелее 75"
        print(f"{n:4d}  {sid:5}{flag}{d}")
    v = [r[1] for r in rows]
    print(f"\nкадров {len(v)} · медиана {statistics.median(v):g} · "
          f"максимум {max(v)} · тяжелее 140 — {sum(1 for x in v if x > 140)} · "
          f"тяжелее 75 — {sum(1 for x in v if x > 75)}")
    if errs:
        print(f"ошибка оценки против замера PDF: медиана |Δ| "
              f"{statistics.median([abs(e) for e in errs]):.0f} · "
              f"среднее Δ {statistics.mean(errs):+.1f} · "
              f"разброс {min(errs):+d}…{max(errs):+d} · n={len(errs)}")


if __name__ == "__main__":
    sys.exit(main())
