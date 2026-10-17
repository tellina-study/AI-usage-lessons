#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пересчёт `timing_min` по весу кадра: слов по собранному PDF ÷ 122, до 0,05.

Зачем: прежняя разметка ставилась на глаз и давала 22–353 слова на минуту при
медиане 122 — по такой сумме нельзя назначить порядок резки, потому что она не
описывает, где вечер встанет. 122 — медиана деки, то есть темп, при котором
сумма минут не меняется от самого пересчёта, а перераспределяется.

    python3 pereschet_minut.py            # показать, ничего не писать
    python3 pereschet_minut.py --write    # записать в кадры
"""
import re
import sys
from pathlib import Path

import yaml

import build_lec07 as B
from deckkit import slidefile

TEMP = 122.0
HERE = Path(__file__).resolve().parent
ZAMER = HERE / "zamer-diyeta-r7-r10"


def slov():
    """{sid: слов по PDF} из сохранённых замеров render_sec.py."""
    out = {}
    for f in sorted(ZAMER.glob("zamer-sec*.txt")):
        for ln in f.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^\s*(\d+)\s+(s[0-9a-z]+)-", ln)
            if m:
                out[m.group(2)] = int(m.group(1))
    return out


def main():
    w = slov()
    rows, missing = [], []
    for f in slidefile.slide_files(B.SLIDES_DIR):
        m = re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        meta = yaml.safe_load(m.group(1)) or {}
        sid = f.name.split("-")[0]
        sec = str(meta.get("section") or "").split(".")[0]
        old = float(meta.get("timing_min") or 0)
        if sid not in w:
            missing.append(sid)
            continue
        new = round(round(w[sid] / TEMP / 0.05) * 0.05, 2)
        rows.append((sec, sid, w[sid], old, new, f))
    if missing:
        print("НЕТ ЗАМЕРА (кадр не пересчитан):", " ".join(missing))
    so, sn = sum(r[3] for r in rows), sum(r[4] for r in rows)
    print(f"кадров {len(rows)} · слов {sum(r[2] for r in rows)} · "
          f"минут {so:.2f} → {sn:.2f}")
    print("\nпо разделам:")
    for sec in sorted({r[0] for r in rows}, key=lambda x: int(x) if x.isdigit() else -1):
        g = [r for r in rows if r[0] == sec]
        print(f"  раздел {sec:>2}: кадров {len(g):3} · "
              f"{sum(r[3] for r in g):6.2f} → {sum(r[4] for r in g):6.2f}")
    print("\nсамые большие расхождения (|новое − старое|):")
    for r in sorted(rows, key=lambda r: -abs(r[4] - r[3]))[:8]:
        print(f"  {r[1]:7} {r[2]:4} слов · {r[3]:.2f} → {r[4]:.2f} "
              f"({r[4] - r[3]:+.2f})  {r[5].name}")
    print("\nтемп до пересчёта (слов на минуту), края:")
    sp = sorted((round(r[2] / r[3]) if r[3] else 0, r[1]) for r in rows)
    print("  медленнее всех:", " · ".join(f"{s} ({i})" for s, i in sp[:4]))
    print("  быстрее всех:  ", " · ".join(f"{s} ({i})" for s, i in sp[-4:]))
    if "--write" in sys.argv:
        for sec, sid, wd, old, new, f in rows:
            t = f.read_text(encoding="utf-8")
            t2 = re.sub(r"^timing_min: .*$", f"timing_min: {new:g}", t, count=1,
                        flags=re.M)
            if t2 != t:
                f.write_text(t2, encoding="utf-8")
        print(f"\nзаписано в {len(rows)} кадров")


if __name__ == "__main__":
    main()
