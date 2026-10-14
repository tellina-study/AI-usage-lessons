#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Предсказание веса кадра по его файлу — ДО сборки.

Не замена `render_sec.py`: тот мерит собранный PDF и он единственный, на чей
счёт можно ссылаться. Этот прогон складывает заголовок + плашки + схему +
тело + подвал по файлу кадра и на разделе 2 сошёлся с PDF в пределах 2 слов
на кадр. Нужен затем, чтобы не гонять рендер на каждую правку абзаца.

    python3 predict.py s28 s30 s31
    python3 predict.py --sec 2
"""
import re, sys, pathlib, yaml, statistics

S = pathlib.Path(__file__).resolve().parent / "slides"

def words(x):
    return len(str(x or "").split())

def weigh(f):
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    fm = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    vis = re.search(r"## Видимый текст слайда\n(.*?)(?=\n## |\Z)", body, re.S)
    nts = re.search(r"## Заметки лектора\n(.*?)(?=\n## |\Z)", body, re.S)
    bl = fm.get("blocks") or []
    bw = sum(words(b.get("label")) + words(b.get("value")) + words(b.get("note")) for b in bl)
    sc = fm.get("scheme") or {}
    sw = words(sc.get("caption")) + sum(
        words(r.get("label")) + sum(words(s) for s in (r.get("steps") or []))
        for r in (sc.get("rows") or []))
    src = str(fm.get("source") or "")
    fw = 0 if src.strip() in ("", "—") else words(re.sub(r"https?://\S+", " ссылка ", src))
    # тело дивайдера несёт заголовок первой строкой — он же поле title, не двоится
    vw = words(vis.group(1) if vis else "")
    tw = 0 if fm.get("type") == "divider" else words(fm.get("title"))
    return dict(id=fm.get("id"), type=fm.get("type"), title=tw, blocks=bw, nbl=len(bl),
                scheme=sw, body=vw, foot=fw, notes=words(nts.group(1) if nts else ""),
                timing=float(fm.get("timing_min") or 0),
                total=tw + bw + sw + vw + fw)

def main():
    a = sys.argv[1:]
    if a[:1] == ["--sec"]:
        want = a[1]
        fs = [f for f in sorted(S.glob("s*.md"))
              if (yaml.safe_load(re.match(r"^---\n(.*?)\n---", f.read_text(encoding='utf-8'), re.S).group(1)) or {})
              .get("section", "").startswith(want + ".")]
    else:
        fs = [next(S.glob(f"{i}-*.md")) for i in a]
    rows = [weigh(f) for f in fs]
    print(f"{'кадр':6s} {'тип':8s} {'ВЕС':>4s} | {'загл':>4s} {'плашк':>6s} {'схема':>5s} {'тело':>4s} {'подв':>4s} | {'заметки':>7s} {'мин':>5s}")
    for r in rows:
        flag = "  ← >140" if r["total"] > 140 else ("  ← >75" if r["total"] > 75 else "")
        nf = "" if 500 <= r["notes"] <= 800 else f"  заметки вне 500-800"
        print(f"{r['id']:6s} {str(r['type']):8s} {r['total']:4d} | {r['title']:4d} "
              f"{r['blocks']:4d}({r['nbl']}) {r['scheme']:5d} {r['body']:4d} {r['foot']:4d} "
              f"| {r['notes']:7d} {r['timing']:5.2f}{flag}{nf}")
    v = [r["total"] for r in rows]
    print(f"\nкадров {len(v)} · медиана {statistics.median(v):g} · максимум {max(v)} · "
          f">140 — {sum(1 for x in v if x > 140)} · >75 — {sum(1 for x in v if x > 75)}")
    print(f"минут {sum(r['timing'] for r in rows):.2f} · "
          f"заметки {min(r['notes'] for r in rows)}–{max(r['notes'] for r in rows)}")

if __name__ == "__main__":
    sys.exit(main())
