"""Где английская подпись вылезла за русскую — и не наехала ли она на соседку.

Порядок отрисовки у двух языков один (код один, меняется только строка), поэтому
подписи сравниваются ПОЗИЦИЯ В ПОЗИЦИЮ: i-я строка русского прогона против i-й
английской. Печатается то, что уехало вправо, и всякое налезание подписи на
подпись внутри одной схемы.

    python3 fig_width_check.py              # все четыре рисовалки
"""
import contextlib, io, runpy, sys
from pathlib import Path
from PIL import Image, ImageDraw
import fig_toolkit as FT

GENS = ("make_figures_mcp.py", "make_figures_subagent.py",
        "make_figures_mostik.py", "make_figures_posle_provedeniya.py")


def run(gen, lang):
    """Прогнать рисовалку, ничего не записав, и вернуть {схема: [подписи]}."""
    FT.LANG = "ru"; FT.TR = {}; FT.MISS.clear(); FT.WHOLE.clear()
    if lang == "en":
        FT.set_lang("en")
    figs, cur = [], []
    _t, _s = ImageDraw.ImageDraw.text, Image.Image.save

    def t(self, xy, text, *a, **k):
        s = FT.T(text, record=None)
        fo = k.get("font")
        if fo is not None and isinstance(s, str) and s.strip():
            cur.append((xy[0], xy[1], self.textlength(s, font=fo), fo.size, s))
        return _t(self, xy, text, *a, **k)

    def s(self, fp, *a, **k):
        if isinstance(fp, (str, Path)) and Path(fp).parent == FT.OUT:
            figs.append((Path(fp).name, list(cur))); cur.clear()
        return None                      # файлы не трогаем: это только замер

    ImageDraw.ImageDraw.text = t; Image.Image.save = s
    sys.argv = [gen]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(gen, run_name="__main__")
    finally:
        ImageDraw.ImageDraw.text = _t; Image.Image.save = _s
    return figs


def collisions(lst):
    """Пары подписей, чьи рамки пересеклись. Считается по ОБОИМ языкам: часть
    пар тесно стоит и по-русски (соседние строки в 18 px при кегле 20), и
    объявлять это английским дефектом нельзя — иначе две деки мерены разными
    линейками. В отчёт идёт только то, чего в русской схеме нет."""
    out = set()
    for i in range(len(lst)):
        x1, y1, w1, s1, t1 = lst[i]
        for j in range(i + 1, len(lst)):
            x2, y2, w2, s2, t2 = lst[j]
            if (x1 < x2 + w2 and x2 < x1 + w1
                    and y1 < y2 + s2 * 0.95 and y2 < y1 + s1 * 0.95):
                out.add((round(y1), round(y2), t1, t2))
    return out


wide, hits = [], []
for gen in GENS:
    ru, en = run(gen, "ru"), run(gen, "en")
    for (rn, rl), (en_n, el) in zip(ru, en):
        # Сопоставление ПО КООРДИНАТЕ, а не по номеру: перенос по словам даёт
        # разное число строк, и нумерация после первой же такой подписи врёт.
        by_xy = {(round(r[0]), round(r[1])): r for r in rl}
        pairs = matched = 0
        for e in el:
            r = by_xy.get((round(e[0]), round(e[1])))
            pairs += 1
            if r is None:
                continue
            matched += 1
            d = (e[0] + e[2]) - (r[0] + r[2])
            if d > 0.5:
                wide.append((d, en_n, e[4], r[4]))
        if matched < pairs:
            print(f"  · {en_n}: сопоставлено по координате {matched} из {pairs} "
                  f"подписей (остальные переехали из-за переноса)")
        ru_c = {(a_, b_) for a_, b_, _t1, _t2 in collisions(rl)}
        for y1, y2, t1, t2 in sorted(collisions(el)):
            if (y1, y2) not in ru_c:           # тесно и по-русски — не находка
                hits.append((en_n, t1, t2))

wide.sort(reverse=True)
print(f"подписей, уехавших вправо против русской: {len(wide)}; верхние 18 по величине")
for d, nm, e, r in wide[:18]:
    print(f"  +{d:6.0f} px  {nm:42} {e[:46]!r} ← {r[:28]!r}")
print(f"\nналезаний подписи на подпись, которых нет в русской схеме: {len(hits)}")
for nm, a, b in hits:
    print(f"  ✘ {nm}: {a[:44]!r} × {b[:44]!r}")
