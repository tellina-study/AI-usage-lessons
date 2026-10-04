"""Общий тулкит для программных схем Семинара 6 (PIL).

Перенесён по образцу `sem-05/rendered/make_figures_ramka.py` /
`make_figures_mcp.py` — тот же набор примитивов (коробка, пунктирная коробка,
стрелка, центрированная подпись, перенос по словам, измерение влезания), но
переписан заново для sem-06 (копия, не импорт — `sem-05/**` не трогается).
Палитра Ocean — те же HEX, что в `deck_kit.py`.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FMB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); WARM = (0xFF, 0xF7, 0xE2); PALE = (0xE6, 0xEE, 0xF4)
GHOST = (0x4A, 0x57, 0x74); DIMTX = (0x8B, 0x9A, 0xAD); GOLDTX = (0xC8, 0x8E, 0x08)
DARKCARD = (0x18, 0x20, 0x3A); GOLDINK = (0x5A, 0x44, 0x08)
GREY_FILL = (0xC9, 0xD1, 0xDB); GREY_TX = (0x55, 0x60, 0x70)
SOFT_GREY = (0xE5, 0xEA, 0xF0)

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)
WARN = []


def f(sz, b=False, m=False):
    return ImageFont.truetype((FMB if b else FM) if m else (FB if b else F), sz)


def fit(d, txt, fo, limit, where):
    if d.textlength(txt, font=fo) > limit:
        WARN.append(f"{where}: шире отведённого — {txt[:56]!r}")


def wrap(d, txt, fo, limit):
    """Перенос по словам: длинная строка на схеме не обрезается и не
    выезжает — она становится двумя. Ширину меряем тем шрифтом, которым
    будем рисовать."""
    out, cur = [], ""
    for wd in txt.split():
        probe = (cur + " " + wd).strip()
        if cur and d.textlength(probe, font=fo) > limit:
            out.append(cur); cur = wd
        else:
            cur = probe
    if cur:
        out.append(cur)
    return out


def lines_at(d, x, y, lines, fo, col, lh, center=None):
    for i, ln in enumerate(lines):
        xx = x if center is None else center - d.textlength(ln, font=fo) / 2
        d.text((xx, y + i * lh), ln, font=fo, fill=col)


def clabel(d, cx, y, txt, sz, col=INK, b=False, m=False, where="?", limit=None):
    """Подпись по центру. `limit` — ширина, в которую она обязана уложиться."""
    fo = f(sz, b, m)
    if limit:
        fit(d, txt, fo, limit, where)
    d.text((cx - d.textlength(txt, font=fo) / 2, y), txt, font=fo, fill=col)


def box(d, x, y, w, h, lines, fc, tc=W, sz=32, b=True, m=False, r=12, pad=18,
        outline=None, where="?"):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    if isinstance(lines, str):
        lines = lines.split("\n")
    lh = sz + 8
    cy = y + (h - (len(lines) * lh - 8)) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        d.text((x + (w - d.textlength(ln, font=fo)) / 2, cy + i * lh), ln,
               font=fo, fill=tc)


def dashbox(d, x, y, w, h, col, dash=18, gap=12, width=3, r=10, bg=W):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, outline=col, width=width)
    for sx in range(int(x) + r, int(x + w) - r, dash + gap):
        d.rectangle([sx + dash, y - 1, sx + dash + gap, y + width], fill=bg)
        d.rectangle([sx + dash, y + h - width - 1, sx + dash + gap, y + h + 1], fill=bg)
    for sy in range(int(y) + r, int(y + h) - r, dash + gap):
        d.rectangle([x - 1, sy + dash, x + width, sy + dash + gap], fill=bg)
        d.rectangle([x + w - width - 1, sy + dash, x + w + 1, sy + dash + gap], fill=bg)


def arrow(d, x1, y1, x2, y2, col=MID, wd=5, head=16, dash=False):
    if dash:
        seg, gap = 14, 10
        total = math.hypot(x2 - x1, y2 - y1)
        n = max(int(total // (seg + gap)), 1)
        ux, uy = (x2 - x1) / total, (y2 - y1) / total
        p = 0.0
        while p < total - seg:
            sx, sy = x1 + ux * p, y1 + uy * p
            ex, ey = x1 + ux * min(p + seg, total), y1 + uy * min(p + seg, total)
            d.line([sx, sy, ex, ey], fill=col, width=wd)
            p += seg + gap
    else:
        d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42)),
               (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))],
              fill=col)


def xmark(d, cx, cy, s, col=RED, wd=5):
    d.line([cx - s, cy - s, cx + s, cy + s], fill=col, width=wd)
    d.line([cx - s, cy + s, cx + s, cy - s], fill=col, width=wd)


def check_outline(d, cx, cy, s, col):
    """Незалитая галочка — вопрос задан, не отвечен."""
    d.line([cx - s, cy, cx - s * 0.25, cy + s * 0.7], fill=col, width=max(4, s // 5))
    d.line([cx - s * 0.25, cy + s * 0.7, cx + s, cy - s * 0.6], fill=col, width=max(4, s // 5))


def lock(d, cx, cy, s, col):
    d.rounded_rectangle([cx - s, cy, cx + s, cy + s * 1.35], radius=s // 3, fill=col)
    d.arc([cx - s * 0.62, cy - s * 0.95, cx + s * 0.62, cy + s * 0.35], 180, 360,
          fill=col, width=max(4, s // 4))


def head(d, txt, sz=34, col=DEEP, x=40, y=18):
    d.text((x, y), txt, font=f(sz, True), fill=col)


def save(im, name):
    im.save(OUT / name)
    print("  ", name, im.size)


def cover_backdrop(w, h, top_frac, bottom_frac):
    """Подложка обложки — продолжение градиента самого слайда (DEEP→MID→LIGHT,
    45°), не своя заливка. Перенесено из sem-05 `make_figures_ramka.py`
    буквально (формула и назначение те же: холст — нижняя полоса слайда)."""
    stops = ((0.0, DEEP), (0.55, MID), (1.0, LIGHT))

    def at(t):
        t = min(max(t, 0.0), 1.0)
        for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
            if t <= p1:
                k = (t - p0) / (p1 - p0)
                return tuple(round(a + (b - a) * k) for a, b in zip(c0, c1))
        return stops[-1][1]

    im = Image.new("RGB", (w, h))
    dd = ImageDraw.Draw(im)
    span = bottom_frac - top_frac
    step = 4
    for px in range(0, w, step):
        for py in range(0, h, step):
            t = (px / w + top_frac + span * py / h) / 2
            dd.rectangle([px, py, px + step - 1, py + step - 1], fill=at(t))
    return im


def report():
    print("схемы sem-06:")
    if WARN:
        print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
        for w_ in dict.fromkeys(WARN):
            print("  ", w_)
    else:
        print("\nпредупреждений нет: весь текст укладывается в отведённые блоки")
