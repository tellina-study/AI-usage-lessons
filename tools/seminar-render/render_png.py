#!/usr/bin/env python3
"""
Pillow-based PNG/PDF preview renderer for the case-centric seminar decks
(sem-03, sem-04) — a libreoffice-free visual-QA path.

Reproduces the *geometry* of tools/seminar-render/build_cases_deck.py 1:1
(same inch coordinates/sizes, same Ocean palette, same text wrapping by real
DejaVu metrics via ImageDraw.textbbox) onto a 1280x720 canvas
(13.333 x 7.5 in x 96 dpi).

Key QA feature: OVERFLOW HIGHLIGHT. For every text box, if the wrapped text's
total height exceeds the box height, the box is outlined in RED (2px) with a
small red "!" marker in the corner. The pptx auto-fit in build_cases_deck.py
should already have prevented this — this preview verifies it actually did.

Fonts: DejaVuSans / DejaVuSans-Bold / DejaVuSansMono (real metrics).
Pt -> px: px = pt * 96/72 = pt * 1.3333.

NOTE ON FIDELITY: build_cases_deck.py emits pptx text boxes with
tf.word_wrap=True and vertical_anchor; PowerPoint's own line-break algorithm
and per-glyph advances differ slightly from DejaVu. This preview uses DejaVu
metrics (documented divergence). It also does NOT reproduce pptx runtime
"shrink text on overflow" autofit (which build_cases_deck.py does NOT enable —
it uses manual size stepping in the spec helpers, which IS reproduced). So an
overflow flagged here corresponds to text that would clip / spill in the real
deck under DejaVu metrics; treat flags as leads to inspect, not proof.

Run: python3 tools/seminar-render/render_png.py
"""
import importlib.util
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ---- canvas / scale ----
DPI = 96
PX = lambda inch: inch * DPI            # inches -> px
PT = lambda pt: pt * 96.0 / 72.0        # pt -> px
CW, CHt = int(round(13.333 * DPI)), int(round(7.5 * DPI))   # 1280 x 720

# ---- Ocean palette (copied RGB from build_cases_deck.py) ----
DEEP   = (0x21, 0x29, 0x5C)
MID    = (0x06, 0x5A, 0x82)
LIGHT  = (0x1C, 0x72, 0x93)
TEAL   = (0x02, 0x80, 0x90)
SURF   = (0xF4, 0xF7, 0xFA)
WHITE  = (0xFF, 0xFF, 0xFF)
GOLD   = (0xF0, 0xAB, 0x00)
SLATE  = (0x33, 0x3B, 0x49)
GTINT  = (0xFE, 0xF5, 0xE0)
NEG_T  = (0xFB, 0xEA, 0xEA)
NEG_L  = (0xB0, 0x4A, 0x4A)
POS_T  = (0xE9, 0xF5, 0xF2)
GREY   = (0xE5, 0xEA, 0xF0)
CODEBG = (0x1B, 0x22, 0x3B)
CODEFG = (0xE3, 0xE9, 0xF2)
RED    = (0xE0, 0x00, 0x00)          # overflow highlight
ARROW_ACCENT = TEAL

# alignment / anchor enums (mirror pptx ones we use)
L, C, R = "left", "center", "right"
TOP, MIDDLE, BOTTOM = "top", "middle", "bottom"

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
_font_cache = {}
def font(size_px, bold=False, mono=False):
    size_px = max(1, int(round(size_px)))
    key = (size_px, bold, mono)
    if key not in _font_cache:
        if mono:
            fn = "DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
        else:
            fn = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
        _font_cache[key] = ImageFont.truetype(f"{FONT_DIR}/{fn}", size_px)
    return _font_cache[key]


class Slide:
    """Pillow canvas mirroring the pptx slide API used by the k_* helpers.
    Coordinates passed to methods are in INCHES (same as build_cases_deck.py)."""
    def __init__(self):
        self.img = Image.new("RGB", (CW, CHt), WHITE)
        self.d = ImageDraw.Draw(self.img)
        self.overflows = []   # list of (label, x_in, y_in, w_in, h_in)

    # ---- primitives ----
    def rect(self, x, y, w, h, fill=None, stroke=None, spt=1.4, radius=True, adj=0.08):
        x0, y0 = PX(x), PX(y)
        x1, y1 = PX(x + w), PX(y + h)
        sw = max(1, int(round(PT(spt))))
        if radius:
            # pptx ROUNDED_RECTANGLE adj is fraction of the shorter side
            rad = adj * min(w, h) * DPI
            rad = max(0, min(rad, (x1 - x0) / 2, (y1 - y0) / 2))
            self.d.rounded_rectangle([x0, y0, x1, y1], radius=rad,
                                     fill=fill, outline=stroke, width=sw if stroke else 1)
        else:
            self.d.rectangle([x0, y0, x1, y1],
                             fill=fill, outline=stroke, width=sw if stroke else 1)

    def right_arrow(self, x, y, w, h, fill=TEAL):
        # simple triangle-headed bar; geometry approximates MSO RIGHT_ARROW
        x0, y0 = PX(x), PX(y)
        x1, y1 = PX(x + w), PX(y + h)
        midy = (y0 + y1) / 2
        headw = min((x1 - x0) * 0.5, (y1 - y0) * 2.2)
        bar_x1 = x1 - headw
        # shaft
        shaft_h = (y1 - y0) * 0.55
        self.d.rectangle([x0, midy - shaft_h / 2, bar_x1, midy + shaft_h / 2], fill=fill)
        # head
        self.d.polygon([(bar_x1, y0 - (y1 - y0) * 0.4), (x1, midy),
                        (bar_x1, y1 + (y1 - y0) * 0.4)], fill=fill)

    # ---- text wrapping by real DejaVu metrics ----
    def _wrap(self, text, fnt, max_w_px):
        """Word-wrap a single paragraph string to max_w_px (mirrors pptx word_wrap)."""
        words = text.split()
        if not words:
            return [""]
        lines, cur = [], words[0]
        for wd in words[1:]:
            trial = cur + " " + wd
            if self.d.textlength(trial, font=fnt) <= max_w_px:
                cur = trial
            else:
                lines.append(cur)
                cur = wd
                # hard-break a single over-long token
                while self.d.textlength(cur, font=fnt) > max_w_px and len(cur) > 1:
                    # find max prefix that fits
                    lo, hi = 1, len(cur)
                    while lo < hi:
                        mid = (lo + hi + 1) // 2
                        if self.d.textlength(cur[:mid], font=fnt) <= max_w_px:
                            lo = mid
                        else:
                            hi = mid - 1
                    lines.append(cur[:lo])
                    cur = cur[lo:]
        lines.append(cur)
        return lines

    def _line_h(self, fnt, ls):
        asc, desc = fnt.getmetrics()
        return (asc + desc) * ls

    def measure_h(self, w, runs, size=17, bold=False, ls=1.12, mono=False,
                  bullet=False, space_after=4):
        """Return wrapped text height in px for a box of width w (inches),
        mirroring text() metrics exactly. Used by auto-fit helpers to pick a
        font size / grow a box before drawing."""
        if isinstance(runs, str):
            runs = [runs]
        max_w = PX(w)
        total_h = 0.0
        n_para = 0
        for item in runs:
            if isinstance(item, tuple):
                st, sz, col, bd = item
            else:
                st, sz, col, bd = item, size, None, bold
            fnt = font(PT(sz), bold=bd, mono=mono)
            txt_str = ("— " + st) if bullet else st
            for ln in self._wrap(txt_str, fnt, max_w):
                total_h += self._line_h(fnt, ls)
            n_para += 1
        if n_para > 1:
            total_h += PT(space_after) * (n_para - 1)
        return total_h

    def text(self, x, y, w, h, runs, size=17, color=SLATE, bold=False,
             align=L, anchor=TOP, ls=1.12, mono=False, bullet=False,
             space_after=4, label=""):
        """Render a text box the way txt()/_txt_tight() do in build_cases_deck.py.
        `runs` is a str, list[str], or list of (text,size,color,bold) tuples.
        Returns True if content height <= box height (fits), False if overflow."""
        if isinstance(runs, str):
            runs = [runs]
        max_w = PX(w)
        # build wrapped paragraphs, remembering per-line font
        para_lines = []   # list of (line_str, fnt, color)
        para_gaps = []    # gap (px) after each paragraph
        for item in runs:
            if isinstance(item, tuple):
                s, sz, col, bd = item
            else:
                s, sz, col, bd = item, size, color, bold
            fnt = font(PT(sz), bold=bd, mono=mono)
            txt_str = ("— " + s) if bullet else s
            wrapped = self._wrap(txt_str, fnt, max_w)
            for i, ln in enumerate(wrapped):
                para_lines.append((ln, fnt, col, ls))
            para_gaps.append(PT(space_after))
        # total height
        total_h = 0.0
        for (ln, fnt, col, lsp) in para_lines:
            total_h += self._line_h(fnt, lsp)
        total_h += sum(para_gaps[:-1]) if len(para_gaps) > 1 else 0.0
        # last paragraph's trailing space_after not counted (pptx space_after
        # affects between-paragraph; keep parity approximate)

        box_h = PX(h)
        # vertical start
        if anchor == MIDDLE:
            start_y = PX(y) + max(0, (box_h - total_h) / 2)
        elif anchor == BOTTOM:
            start_y = PX(y) + max(0, box_h - total_h)
        else:
            start_y = PX(y)

        # draw
        cy = start_y
        gap_idx = 0
        # rebuild with per-paragraph gap application
        # regroup: we appended lines then gaps per paragraph; easier: redo loop
        cy = start_y
        for item in runs:
            if isinstance(item, tuple):
                s, sz, col, bd = item
            else:
                s, sz, col, bd = item, size, color, bold
            fnt = font(PT(sz), bold=bd, mono=mono)
            txt_str = ("— " + s) if bullet else s
            wrapped = self._wrap(txt_str, fnt, max_w)
            lh = self._line_h(fnt, ls)
            for ln in wrapped:
                if align == C:
                    lw = self.d.textlength(ln, font=fnt)
                    lx = PX(x) + (max_w - lw) / 2
                elif align == R:
                    lw = self.d.textlength(ln, font=fnt)
                    lx = PX(x) + (max_w - lw)
                else:
                    lx = PX(x)
                self.d.text((lx, cy), ln, font=fnt, fill=col)
                cy += lh
            cy += PT(space_after)

        fits = total_h <= box_h + 0.5   # small tolerance
        if not fits:
            self.overflows.append((label or "(text)", x, y, w, h))
        return fits


# ============================================================================
# Helpers reproduced 1:1 from build_cases_deck.py (geometry preserved)
# ============================================================================
FONT_DEF = 17

def box(s, x, y, w, h, fill=SURF, stroke=LIGHT, spt=1.4, radius=True, adj=0.08):
    s.rect(x, y, w, h, fill=fill, stroke=stroke, spt=spt, radius=radius, adj=adj)

def txt(s, x, y, w, h, runs, size=17, color=SLATE, bold=False,
        align=L, anchor=TOP, ls=1.12, mono=False, bullet=False, label=""):
    return s.text(x, y, w, h, runs, size=size, color=color, bold=bold,
                  align=align, anchor=anchor, ls=ls, mono=mono, bullet=bullet,
                  space_after=4, label=label)

def _txt_tight(s, x, y, w, h, runs, size=17, color=SLATE, bold=False,
               align=L, anchor=TOP, ls=1.12, mono=False, bullet=False,
               space_after=4, label=""):
    return s.text(x, y, w, h, runs, size=size, color=color, bold=bold,
                  align=align, anchor=anchor, ls=ls, mono=mono, bullet=bullet,
                  space_after=space_after, label=label)

def chip(s, x, y, label, fill=MID, color=WHITE, size=12.5):
    w = 0.28 + 0.115 * len(label)
    box(s, x, y, w, 0.42, fill=fill, stroke=None, adj=0.5)
    # chip text is centered middle, no wrap (word_wrap=False)
    fnt = font(PT(size), bold=True)
    lw = s.d.textlength(label, font=fnt)
    asc, desc = fnt.getmetrics()
    lx = PX(x) + (PX(w) - lw) / 2
    ly = PX(y) + (PX(0.42) - (asc + desc)) / 2
    s.d.text((lx, ly), label, font=fnt, fill=color)
    return w

def titlebar(s, kicker, title):
    box(s, 0, 0, 13.333, 1.2, fill=DEEP, stroke=None, radius=False)
    txt(s, 0.6, 0.14, 12.1, 0.4, kicker, size=13, color=GOLD, bold=True, label="titlebar.kicker")
    txt(s, 0.6, 0.48, 12.1, 0.66, title, size=22, color=WHITE, bold=True, ls=1.05, label="titlebar.title")

def callout(s, x, y, w, h, text, size=15, fill=GTINT, stroke=GOLD, color=DEEP,
            label="callout", floor=11.0, max_h=None):
    """Auto-fit callout: text is measured against (h - vertical padding); if it
    overflows, step the font down by ~1pt to `floor`, then grow the box height
    downward (bounded by `max_h`) until it fits. Returns the actual box height
    (inches) so callers can shift following elements. Geometry 1:1 with the
    pptx callout()."""
    pad_x, pad_y = 0.25, 0.1
    tw = w - 2 * pad_x
    sz = size
    cur_h = h
    while True:
        need_px = s.measure_h(tw, text, size=sz, bold=True, ls=1.2)
        avail_px = PX(cur_h - 2 * pad_y)
        if need_px <= avail_px + 0.5:
            break
        if sz > floor + 0.01:
            sz = max(floor, sz - 1.0)
            continue
        # font at floor and still overflowing → grow height if allowed
        grow_to = need_px / PX(1.0) + 2 * pad_y
        if max_h is not None:
            grow_to = min(grow_to, max_h)
        if grow_to <= cur_h + 0.01:
            break   # can't grow any more; will flag overflow honestly
        cur_h = grow_to
    box(s, x, y, w, cur_h, fill=fill, stroke=stroke, spt=1.2)
    txt(s, x + pad_x, y + pad_y, tw, cur_h - 2 * pad_y, text, size=sz, color=color,
        bold=True, anchor=MIDDLE, ls=1.2, label=label)
    return cur_h

def codeblock(s, x, y, w, h, lines, label="codeblock"):
    box(s, x, y, w, h, fill=CODEBG, stroke=None, adj=0.04)
    # each line is its own paragraph, mono 12.5, ls 1.05, no space_after
    runs = [(ln, 12.5, CODEFG, False) for ln in lines]
    s.text(x + 0.2, y + 0.12, w - 0.4, h - 0.24, runs, ls=1.05, mono=True,
           space_after=0, label=label)

def excard(s, x, y, w, h, kind, title, body):
    tint, line, mark, mcol = (NEG_T, NEG_L, "X", NEG_L) if kind == "neg" else (POS_T, TEAL, "V", TEAL)
    box(s, x, y, w, h, fill=tint, stroke=line, spt=1.4, adj=0.06)
    box(s, x + 0.2, y + 0.2, 0.42, 0.42, fill=mcol, stroke=None, adj=0.5)
    fnt = font(PT(16), bold=True)
    mw = s.d.textlength(mark, font=fnt); asc, desc = fnt.getmetrics()
    s.d.text((PX(x + 0.2) + (PX(0.42) - mw) / 2, PX(y + 0.2) + (PX(0.42) - (asc + desc)) / 2),
             mark, font=fnt, fill=WHITE)
    txt(s, x + 0.78, y + 0.18, w - 1.0, 0.45, title, size=14.5, color=DEEP,
        bold=True, anchor=MIDDLE, label="excard.title")
    body_w = w - 0.48; body_h = h - 0.85
    cap = max(1.0, (body_w * 13.0) * (body_h / 0.24))
    b_sz = 13.5
    if len(str(body)) > cap:
        b_sz = 12.5
    if len(str(body)) > cap * 1.3:
        b_sz = 11.5
    txt(s, x + 0.24, y + 0.72, body_w, body_h, body, size=b_sz, color=SLATE, ls=1.12,
        label="excard.body")

def pipeline(s, x, y, w, nodes, accent=MID, node_h=None, label_size=None):
    n = len(nodes); gap = 0.42
    nw = (w - gap * (n - 1)) / n
    if node_h is None:
        node_h = 1.0 if n <= 4 else 1.28
    if label_size is None:
        base = 13 if n <= 4 else 11
        cap = max(1.0, (nw - 0.16) * (13.0 / base) * 3.4)
        longest = max(len(str(lb)) for lb in nodes)
        if longest > cap * 2:
            label_size = base - 1.5
        else:
            label_size = base
    cx = x
    for i, label in enumerate(nodes):
        box(s, cx, y, nw, node_h, fill=SURF, stroke=accent, spt=1.4)
        txt(s, cx + 0.07, y + 0.08, nw - 0.14, node_h - 0.16, label, size=label_size,
            color=DEEP, bold=True, align=C, anchor=MIDDLE, ls=1.04,
            label=f"pipeline.node{i}")
        if i < n - 1:
            s.right_arrow(cx + nw + 0.04, y + node_h / 2 - 0.09, gap - 0.08, 0.18)
        cx += nw + gap


# ============================================================================
# slide kinds — geometry 1:1 with build_cases_deck.py
# ============================================================================
def k_cover(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=DEEP, stroke=None, radius=False)
    box(s, 0, 3.0, 13.333, 0.06, fill=GOLD, stroke=None, radius=False)
    txt(s, 1.0, 1.5, 11.3, 0.6, sp["kicker"], size=19, color=GOLD, bold=True, label="cover.kicker")
    txt(s, 1.0, 2.15, 11.3, 1.6, sp["title"], size=38, color=WHITE, bold=True, ls=1.05, label="cover.title")
    txt(s, 1.0, 4.3, 11.3, 1.5, sp["sub"], size=19, color=SURF, ls=1.2, label="cover.sub")

def k_map(s, sp):
    titlebar(s, "Карта занятия", sp["title"])
    y = 1.55
    for name, desc in sp["blocks"]:
        box(s, 0.6, y, 12.13, 1.15, fill=SURF, stroke=LIGHT)
        box(s, 0.6, y, 0.12, 1.15, fill=TEAL, stroke=None, radius=False)
        txt(s, 0.95, y + 0.13, 11.6, 0.45, name, size=18, color=DEEP, bold=True, label="map.name")
        txt(s, 0.95, y + 0.6, 11.6, 0.5, desc, size=14, color=SLATE, label="map.desc")
        y += 1.32
    txt(s, 0.6, y + 0.02, 12.1, 0.5,
        "Каждый кейс: контекст → решение и схема → усложнение из практики → разбор с примером",
        size=13.5, color=MID, bold=True, label="map.footer")

def k_divider(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=MID, stroke=None, radius=False)
    txt(s, -0.1, -0.5, 6, 3.4, sp["number"], size=250, color=(0x2E, 0x6A, 0x8F),
        bold=True, anchor=BOTTOM, label="divider.number")
    box(s, 0.62, 1.72, 0.2, 0.2, fill=GOLD, stroke=None, adj=0.5)
    txt(s, 0.6, 2.9, 12, 0.5, sp["block"], size=17, color=GTINT, bold=True, label="divider.block")
    txt(s, 0.6, 3.4, 12, 1.4, sp["title"], size=36, color=WHITE, bold=True, ls=1.05, label="divider.title")
    chip(s, 0.64, 4.9, sp["tag"], fill=DEEP)

def _fit_font(s, w, text, sizes, box_h, ls, bold=True):
    """Largest size from `sizes` whose REAL wrapped height ≤ box_h (inches)."""
    for sz in sizes:
        if s.measure_h(w, text, size=sz, bold=bold, ls=ls) / PX(1.0) <= box_h + 0.01:
            return sz
    return sizes[-1]

def k_context(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    lead_sz = _fit_font(s, 12.1, sp["lead"], [16, 15, 14, 13], 0.82, 1.2, bold=False)
    lead_h = min(0.9, max(0.7, s.measure_h(12.1, sp["lead"], size=lead_sz, ls=1.2) / PX(1.0)))
    txt(s, 0.6, 1.35, 12.1, lead_h, sp["lead"], size=lead_sz, color=SLATE, ls=1.2, label="context.lead")
    items = sp["inputs"]; cols = 3
    cw = (12.13 - 0.3 * (cols - 1)) / cols
    x0, y0, ch = 0.6, max(2.25, 1.35 + lead_h + 0.08), 1.5
    lab_chars = (cw - 0.36) * 11
    max_lab = max(len(str(lab)) for lab, _ in items)
    lab_two_lines = max_lab > lab_chars
    lab_sz = 12.5 if max_lab <= lab_chars * 1.6 else 11.5
    lab_h = 0.62 if lab_two_lines else 0.36
    val_top = 0.14 + lab_h + 0.04
    for i, (lab, tx) in enumerate(items):
        r, c = divmod(i, cols)
        x = x0 + c * (cw + 0.3); y = y0 + r * (ch + 0.22)
        box(s, x, y, cw, ch, fill=SURF, stroke=LIGHT)
        txt(s, x + 0.18, y + 0.12, cw - 0.36, lab_h, lab, size=lab_sz, color=TEAL, bold=True, ls=1.05,
            label=f"context.label{i}")
        txt(s, x + 0.18, y + val_top, cw - 0.36, ch - val_top - 0.1, tx,
            size=13, color=SLATE, ls=1.1, label=f"context.value{i}")
    qy = y0 + ((len(items) + cols - 1) // cols) * (ch + 0.22) + 0.08
    if qy > 6.2: qy = 6.2
    callout(s, 0.6, qy, 12.13, 0.72, sp["question"], size=17, fill=DEEP, stroke=None, color=WHITE,
            label="context.question", floor=13.0, max_h=7.32 - qy)

def k_scheme(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    lead = sp.get("lead", "")
    lead_sz = _fit_font(s, 12.1, lead, [15, 14, 13], 0.62, 1.15, bold=False) if lead else 15
    txt(s, 0.6, 1.35, 12.1, 0.75, lead, size=lead_sz, color=SLATE, ls=1.15, label="scheme.lead")
    pipeline(s, 0.6, 2.25, 12.13, sp["nodes"], accent=sp.get("accent", MID))
    if sp.get("bullets"):
        txt(s, 0.9, 3.75, 11.6, 2.0, [(b, 15, SLATE, False) for b in sp["bullets"]],
            bullet=True, ls=1.15, label="scheme.bullets")
    if sp.get("caption"):
        callout(s, 0.6, 6.35, 12.13, 0.7, sp["caption"], size=14, label="scheme.caption",
                floor=11.0, max_h=7.32 - 6.35)

_CONCEPT_LOW = 7.32   # note must not cross this bottom line

def _concept_note_fit(s, note):
    """Pick font size + height for the bottom note by REAL metrics so it fits
    above _CONCEPT_LOW. Returns (size, note_top, note_h) in inches."""
    if not note:
        return (13.5, _CONCEPT_LOW, 0.0)
    for sz in (13.5, 12.5, 11.5, 11.0):
        h_in = s.measure_h(12.1, note, size=sz, bold=True, ls=1.15) / PX(1.0)
        if h_in <= 1.05 or sz == 11.0:
            return (sz, _CONCEPT_LOW - h_in, h_in)
    return (11.0, _CONCEPT_LOW - 1.05, 1.05)

def k_concept(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    def_h = callout(s, 0.6, 1.35, 12.13, 0.95, sp["definition"], size=15,
                    fill=GTINT, stroke=GOLD, color=DEEP, label="concept.definition",
                    max_h=1.30)
    lab_y = 1.35 + def_h + 0.12
    txt(s, 0.6, lab_y, 5.0, 0.4, "Как работает", size=14, color=MID, bold=True, label="concept.howlabel")
    steps_y = lab_y + 0.40
    note = sp.get("note")
    note_sz, note_top, note_h = _concept_note_fit(s, note)
    steps = sp["steps"]
    total_chars = sum(len(str(x)) for x in steps)
    if len(steps) >= 5 or total_chars > 320:
        step_sz, step_ls = 13.0, 1.12
    elif len(steps) >= 4 or total_chars > 240:
        step_sz, step_ls = 13.8, 1.15
    else:
        step_sz, step_ls = 14.5, 1.18
    step_bottom = (note_top - 0.12) if note else _CONCEPT_LOW
    step_area_h = max(1.2, step_bottom - steps_y)
    txt(s, 0.6, steps_y, 6.0, step_area_h, [(x, step_sz, SLATE, False) for x in steps],
        bullet=True, ls=step_ls, label="concept.steps")
    if sp.get("scheme"):
        cont_y = steps_y - 0.20
        cont_h = max(2.4, step_bottom - cont_y)
        box(s, 6.9, cont_y, 5.83, cont_h, fill=SURF, stroke=LIGHT)
        m = len(sp["scheme"]); pad = 0.16
        avail = cont_h - 2 * pad
        step_v = avail / m
        node_h = min(0.62, step_v - 0.14)
        yy = cont_y + pad
        for j, node in enumerate(sp["scheme"]):
            box(s, 7.15, yy, 5.33, node_h, fill=WHITE, stroke=MID, spt=1.2)
            txt(s, 7.25, yy + 0.03, 5.13, node_h - 0.06, node, size=13, color=DEEP,
                bold=True, anchor=MIDDLE, label=f"concept.scheme{j}")
            yy += step_v
    if note:
        txt(s, 0.6, note_top, 12.1, note_h + 0.05, note, size=note_sz, color=MID,
            bold=True, ls=1.15, label="concept.note")

def k_complication(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    box(s, 0.6, 1.45, 12.13, 2.4, fill=SURF, stroke=LIGHT)
    box(s, 0.6, 1.45, 0.12, 2.4, fill=GOLD, stroke=None, radius=False)
    txt(s, 1.0, 1.7, 11.4, 2.0, sp["body"], size=17, color=SLATE, ls=1.25, label="complication.body")
    eff_h = callout(s, 0.6, 4.15, 12.13, 1.0, sp["effect"], size=16, label="complication.effect",
                    floor=12.0, max_h=1.55)
    if sp.get("ask"):
        ask_y = max(5.4, 4.15 + eff_h + 0.12)
        txt(s, 0.6, ask_y, 12.1, 7.28 - ask_y, sp["ask"], size=15, color=MID, bold=True, ls=1.2,
            label="complication.ask")

def k_resolution(s, sp):
    titlebar(s, sp["kicker"], "Разбор · как реализовать")
    sol_h = callout(s, 0.6, 1.33, 12.13, 0.9, sp["solution"], size=15, fill=DEEP,
                    stroke=None, color=WHITE, label="resolution.solution", floor=11.0, max_h=1.35)
    lab_y = 1.33 + sol_h + 0.13
    txt(s, 0.6, lab_y, 11.6, 0.34, "Как реализовать", size=14, color=MID, bold=True, label="resolution.howlabel")
    steps = sp.get("howto", sp.get("lesson", []))
    ex = sp["example"]
    ex_y = 4.98
    steps_y = lab_y + 0.36
    steps_area = max(1.0, ex_y - 0.1 - steps_y)
    st_sz = 14
    for cand in (14, 13, 12):
        runs = [(x, cand, SLATE, False) for x in steps]
        if s.measure_h(11.7, runs, ls=1.14, bullet=True) / PX(1.0) <= steps_area + 0.01:
            st_sz = cand; break
    else:
        st_sz = 12
    txt(s, 0.9, steps_y, 11.7, steps_area, [(x, st_sz, SLATE, False) for x in steps],
        bullet=True, ls=1.14, label="resolution.howto")
    excard(s, 0.6, ex_y, 12.13, 1.72, ex["kind"], ex["title"], ex["text"])

def k_variants(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    lead_sz = _fit_font(s, 12.1, sp["lead"], [15, 14, 13], 0.58, 1.15, bold=False)
    txt(s, 0.6, 1.35, 12.1, 0.7, sp["lead"], size=lead_sz, color=SLATE, ls=1.15, label="variants.lead")
    cols = sp["cols"]; n = len(cols)
    cw = (12.13 - 0.3 * (n - 1)) / n; x0, y0, ch = 0.6, 2.05, 3.7
    sample_top = y0 + 0.72
    max_chars = max(len(c["sample"]) for c in cols)
    chars_per_col = (cw - 0.36) * 13
    for i, c in enumerate(cols):
        x = x0 + i * (cw + 0.3)
        box(s, x, y0, cw, ch, fill=SURF, stroke=LIGHT)
        box(s, x, y0, cw, 0.6, fill=MID, stroke=None, radius=True, adj=0.08)
        txt(s, x + 0.1, y0 + 0.06, cw - 0.2, 0.48, c["head"], size=14.5, color=WHITE,
            bold=True, align=C, anchor=MIDDLE, label=f"variants.head{i}")
        est_lines = max(2, int(max_chars / chars_per_col) + 1)
        s_sz = 12.5 if est_lines <= 4 else (11.5 if est_lines <= 5 else 11.0)
        s_h = min(2.2, 0.30 * est_lines + 0.30)
        txt(s, x + 0.18, sample_top, cw - 0.36, s_h, c["sample"], size=s_sz,
            color=SLATE, ls=1.1, label=f"variants.sample{i}")
        use_top = sample_top + s_h + 0.12
        use_area = (y0 + ch) - use_top - 0.12
        use_sz = 12.5 if est_lines <= 4 else 11.5
        for cand in (use_sz, 11.0, 10.5, 10.0):
            runs = [(u, cand, SLATE, False) for u in c["use"]]
            if s.measure_h(cw - 0.36, runs, ls=1.1, bullet=True) / PX(1.0) <= use_area + 0.01:
                use_sz = cand; break
        else:
            use_sz = 10.0
        txt(s, x + 0.18, use_top, cw - 0.36, use_area,
            [(u, use_sz, SLATE, False) for u in c["use"]], bullet=True, ls=1.1,
            label=f"variants.use{i}")
    callout(s, 0.6, 6.0, 12.13, 0.95, sp["note"], size=15, label="variants.note",
            floor=11.0, max_h=7.32 - 6.0)

def k_structured(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.6, 1.3, 6.0, 0.4, "Задаём схему ответа", size=14, color=MID, bold=True, label="structured.schemalabel")
    codeblock(s, 0.6, 1.7, 6.0, 3.0, sp["schema_code"], label="structured.schema")
    txt(s, 6.85, 1.3, 5.9, 0.4, "Что получаем", size=14, color=MID, bold=True, label="structured.getlabel")
    box(s, 6.85, 1.7, 5.88, 1.55, fill=POS_T, stroke=TEAL)
    txt(s, 7.05, 1.85, 5.5, 1.3, sp["sample"], size=13, color=SLATE, ls=1.15, mono=True, label="structured.sample")
    excard(s, 6.85, 3.4, 5.88, 1.3, "neg", "Где упираемся", sp["limitation"])
    callout(s, 0.6, 4.95, 12.13, 1.2, sp["takeaway"], size=15, label="structured.takeaway",
            floor=11.0, max_h=7.32 - 4.95)

def _bars(s, x, y, w, h, heights, labels, cut=None, cut_kind=None, accent=MID):
    n = len(heights); gap = 0.09
    bw = (w - gap * (n - 1)) / n
    base = y + h - 0.34
    maxh = h - 0.52
    cx = x
    for i, hv in enumerate(heights):
        bh = max(0.06, hv * maxh)
        kept = (cut is None) or (i < cut)
        fill = accent if kept else GREY
        box(s, cx, base - bh, bw, bh, fill=fill, stroke=None, radius=False)
        txt(s, cx - 0.05, base + 0.02, bw + 0.1, 0.28, labels[i], size=9.5,
            color=SLATE if kept else (0xA0, 0xA8, 0xB4), bold=kept, align=C,
            label=f"bars.label{i}")
        cx += bw + gap
    if cut_kind:
        txt(s, x, y - 0.02, w, 0.3, cut_kind, size=11, color=accent, bold=True, align=C,
            label="bars.cutkind")

_PAL = {"deep": DEEP, "mid": MID, "light": LIGHT, "teal": TEAL, "gold": GOLD}

def k_distribution(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.6, 1.32, 12.1, 0.6, sp["lead"], size=15, color=SLATE, ls=1.15, label="distribution.lead")
    panels = sp["panels"]; n = len(panels)
    pw = (12.13 - 0.3 * (n - 1)) / n; x0, y0, ph = 0.6, 2.15, 3.55
    for i, pn in enumerate(panels):
        x = x0 + i * (pw + 0.3)
        accent = _PAL.get(pn.get("accent", "teal"), TEAL)
        head_fill = _PAL.get(pn.get("head_fill", "mid"), MID)
        box(s, x, y0, pw, ph, fill=SURF, stroke=LIGHT)
        box(s, x, y0, pw, 0.55, fill=head_fill, stroke=None, radius=True, adj=0.08)
        txt(s, x + 0.08, y0 + 0.04, pw - 0.16, 0.46, pn["head"], size=13.5, color=WHITE,
            bold=True, align=C, anchor=MIDDLE, label=f"distribution.head{i}")
        _bars(s, x + 0.22, y0 + 0.75, pw - 0.44, 2.05, pn["heights"], pn["labels"],
              cut=pn.get("cut"), cut_kind=pn.get("cut_kind"), accent=accent)
        txt(s, x + 0.18, y0 + 2.92, pw - 0.36, 0.55, pn["note"], size=11.5, color=SLATE,
            ls=1.1, align=C, label=f"distribution.note{i}")
    callout(s, 0.6, 5.95, 12.13, 0.95, sp["takeaway"], size=15, label="distribution.takeaway",
            floor=11.0, max_h=7.32 - 5.95)

def k_breakdown(s, sp):
    titlebar(s, sp["kicker"], sp.get("title", "Разбор · компоненты и комментарии"))
    colw = 5.96
    bx_y, bx_h = 1.4, 5.5
    txt(s, 0.6, 1.02, colw, 0.34, "Ключевые компоненты", size=14, color=MID, bold=True, label="breakdown.complabel")
    txt(s, 6.77, 1.02, colw, 0.34, "Ключевые комментарии по теме", size=14, color=MID, bold=True, label="breakdown.commlabel")
    box(s, 0.6, bx_y, colw, bx_h, fill=SURF, stroke=LIGHT)
    box(s, 6.77, bx_y, colw, bx_h, fill=GTINT, stroke=GOLD)
    comps = sp["components"]
    n = len(comps)
    if n <= 4:
        name_sz, role_sz, ls, sa = 12.5, 12.0, 1.14, 4
    elif n == 5:
        name_sz, role_sz, ls, sa = 12.0, 11.0, 1.08, 2
    else:
        name_sz, role_sz, ls, sa = 11.5, 10.5, 1.02, 1
    lines = []
    for c in comps:
        if isinstance(c, tuple):
            name, role = c
            lines.append((name, name_sz, DEEP, True))
            lines.append((role, role_sz, SLATE, False))
        else:
            lines.append((c, name_sz, SLATE, False))
    _txt_tight(s, 0.8, bx_y + 0.14, colw - 0.4, bx_h - 0.28, lines, ls=ls, space_after=sa,
               label="breakdown.components")
    csz = 12.5 if len(sp["comments"]) <= 3 else 11.5
    _txt_tight(s, 6.97, bx_y + 0.14, colw - 0.4, bx_h - 0.28,
               [(x, csz, DEEP, False) for x in sp["comments"]], ls=1.16,
               space_after=4, bullet=True, label="breakdown.comments")

def k_finale(s, sp):
    titlebar(s, sp["kicker"], sp["title"])
    txt(s, 0.9, 1.55, 11.6, 3.4, [(p, 16, SLATE, False) for p in sp["points"]],
        bullet=True, ls=1.22, label="finale.points")
    callout(s, 0.6, 5.35, 12.13, 1.1, sp["takeaway"], size=16, label="finale.takeaway",
            floor=11.0, max_h=7.32 - 5.35)

def k_closing(s, sp):
    box(s, 0, 0, 13.333, 7.5, fill=DEEP, stroke=None, radius=False)
    txt(s, 0.7, 0.85, 12, 0.9, "Что унести", size=30, color=GOLD, bold=True, label="closing.title")
    txt(s, 0.9, 2.0, 11.6, 3.2, [(t, 18, SURF, False) for t in sp["takeaways"]],
        bullet=True, ls=1.2, label="closing.takeaways")
    txt(s, 0.9, 5.7, 11.6, 0.9, sp["bridge"], size=16, color=GOLD, bold=True, ls=1.15, label="closing.bridge")

KIND = {"cover": k_cover, "map": k_map, "divider": k_divider, "context": k_context,
        "scheme": k_scheme, "concept": k_concept, "complication": k_complication,
        "resolution": k_resolution, "variants": k_variants, "structured": k_structured,
        "distribution": k_distribution, "breakdown": k_breakdown,
        "finale": k_finale, "closing": k_closing}


def draw_overflow_marks(s):
    """After all content, outline overflowed boxes in RED (2px) + corner '!'."""
    fnt = font(PT(13), bold=True)
    for (label, x, y, w, h) in s.overflows:
        x0, y0 = PX(x), PX(y)
        x1, y1 = PX(x + w), PX(y + h)
        s.d.rectangle([x0, y0, x1, y1], outline=RED, width=2)
        # marker in top-right corner
        mr = 11
        mx1, my0 = x1 - 2, y0 + 2
        s.d.ellipse([mx1 - mr, my0, mx1, my0 + mr], fill=RED)
        # "!" glyph centered in the dot
        gw = s.d.textlength("!", font=fnt)
        asc, desc = fnt.getmetrics()
        s.d.text((mx1 - mr / 2 - gw / 2, my0 + (mr - (asc + desc)) / 2 - 1),
                 "!", font=fnt, fill=WHITE)


def render_seminar(sem):
    dir_ = sem["dir"]
    root = Path("library/seminars") / dir_
    out = root / "rendered"
    png_dir = out / "png"
    png_dir.mkdir(parents=True, exist_ok=True)
    imgs = []
    overflow_report = []
    for i, sp in enumerate(sem["slides"], 1):
        sid = f"s{i:02d}"
        s = Slide()
        KIND[sp["kind"]](s, sp)
        draw_overflow_marks(s)
        p = png_dir / f"{sid}.png"
        s.img.save(str(p))
        imgs.append(s.img.convert("RGB"))
        if s.overflows:
            for (label, *_rest) in s.overflows:
                overflow_report.append((sid, sp["kind"], label))
    # combined PDF
    pdf_path = out / f"{dir_}-preview.pdf"
    if imgs:
        imgs[0].save(str(pdf_path), save_all=True, append_images=imgs[1:])
    return len(imgs), overflow_report, png_dir, pdf_path


if __name__ == "__main__":
    here = Path(__file__).parent
    results = {}
    for spec_file in ["spec_sem03.py", "spec_sem04.py"]:
        p = here / spec_file
        st = importlib.util.spec_from_file_location(spec_file[:-3], p)
        m = importlib.util.module_from_spec(st); st.loader.exec_module(m)
        n, overflows, png_dir, pdf_path = render_seminar(m.SEMINAR)
        results[m.SEMINAR["dir"]] = (n, overflows, png_dir, pdf_path)
        print(f"\n=== {m.SEMINAR['dir']}: {n} PNG -> {png_dir}")
        print(f"    PDF -> {pdf_path}")
        # divider.number is a decorative oversized glyph designed to bleed
        # off-canvas (pptx uses y=-0.5, 250pt) — not a real content overflow.
        real = [(sid, k, lb) for (sid, k, lb) in overflows if lb != "divider.number"]
        deco = [(sid, k, lb) for (sid, k, lb) in overflows if lb == "divider.number"]
        if real:
            print(f"    OVERFLOW — real content ({len(real)} boxes):")
            for sid, kind, label in real:
                print(f"      {sid} [{kind}] box={label}")
        else:
            print("    OVERFLOW — real content: none")
        if deco:
            print(f"    (decorative divider bleed, expected, not a defect: "
                  f"{', '.join(sid for sid, _, _ in deco)})")
