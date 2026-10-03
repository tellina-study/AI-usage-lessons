"""Lecture 5 (EN) — Band 6: eleven practice slides + s45a (issue #212).

EN twin of slides_band6.py: same layout, geometry, palette and motif; only
the visible strings and the speaker notes are English. Notes come from
slides-en/*.md through `notes_with_sources` (`_helpers_en.SLIDES_DIR` points
at slides-en/).

The owner rejected the deck because the AI practices lived only inside the
examples: "where are they in the slides, step by step?". This band answers
exactly that — one slide per practice, and all the cards share ONE form:

ONE EXCEPTION, named by the owner: s45a ("slide 46 — remake it from that
format into a normal presentation slide") is taken out of the card form and
built as an ordinary slide — the structure of cost and revenue in two cuts.
It lives here so that ORDER in build_lec05_en.py does not have to be
touched, but it calls none of the card primitives (head / Cursor /
what_is_it / mechanism / compare / edge). The other eleven hold the form
without exception:

    WHAT IT IS           — a human description of the method for a newcomer,
                           as the FIRST block;
    HOW IT WORKS         — numbered steps + a labelled diagram on the right;
    WITH AI AND WITHOUT  — two columns: what is classical here and what AI
                           added (rule R6);
    WHERE IT BREAKS      — the boundary of applicability, visually heavier
                           than the other three.

There are no "artefact", "criterion" or "building on what has been covered"
blocks and no questions to the room anywhere (rule R8). The mechanism runs
as prose on none of the cards: diagrams live inside HOW IT WORKS, and the
fourth block is exactly one and the same everywhere.

Band heights are computed from the content (steps_h / fit_h) rather than by
eye, with an SF margin against est_h under-counting — see
notes/mcp-limitations.md [#212-6].

Slides: s11a s11b (Section 1) · s17a (Section 2) · s24a s24b s24c
(Section 3) · s30a s31a (Section 4) · s38a s38b (Section 5) · s45b
(Section 6) + s45a (same section, outside the card form).

Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.
Timing and methodology commentary are forbidden in the visible layer.
"""
import math
import re

from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    circle, chip, connector, icon, slide_title, src, check_point,
    right_arrow, notes_with_sources, gold_callout,
    refs_of_slide,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT,
    FONT_BODY, FONT_MONO, SLIDES_DIR,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN


# ============================================================
# Practice-card geometry — one for all twelve slides
# ============================================================
X0 = 0.55            # left edge of the label column
LBL_W = 1.26         # width of the label column
GAPX = 0.16
CX = X0 + LBL_W + GAPX          # left edge of the content column
RIGHT = 12.80
CW = RIGHT - CX                 # ~10.83
PAD = 0.20
PAD_Y = 0.10
TOP = 0.84
RGAP = 0.07

# The bands of a practice card. Weight grows by purpose, not by order: the
# way in ("what it is") is more prominent than the mechanism but lighter
# than the boundary — the boundary stays the heaviest block, because it is
# what holds the link to the failure cases.
#
# NOTE: the key "what" was at one point defined HERE TWICE — two parallel
# sessions added it independently, Python silently took the second and the
# first was dead code. The variant kept is the dark label on a white fill:
# it reads as the way into the card, not as one more takeaway. Do not
# duplicate.
KIND = {
    # "what it is" — a human description of the practice for a newcomer,
    # as the FIRST block (R8).
    "what": dict(lab=DEEP,  labc=WHITE, fill=WHITE,     stroke=MID,   pt=1.8),
    "mech": dict(lab=MID,   labc=WHITE, fill=SURFACE,   stroke=LIGHT, pt=1.5),
    # "with AI and without" — the key practices compared (R6).
    "cmp":  dict(lab=LIGHT, labc=WHITE, fill=SURFACE,   stroke=LIGHT, pt=1.5),
    # the boundary — heavier than every other band, deliberately so.
    "edge": dict(lab=GOLD,  labc=DEEP,  fill=GOLD_TINT, stroke=GOLD,  pt=2.5),
}


# ============================================================
# Measurement: how much room the TEXT actually takes. The first calibration
# (122/114 characters per inch of width) systematically UNDER-counted the
# number of lines — see notes/mcp-limitations.md [#212-6]: the real density
# in LibreOffice on this host is closer to ~104 characters per inch, and on
# mechanism steps that made neighbouring lines run into each other while
# WARN stayed empty. The constant is brought to the fact; SF is left as a
# small residual margin.
# ============================================================
WARN = []
_TOP = [TOP]
_SID = [""]
_TAIL = [0.0]
_BAND = ["", 0.0]          # label of the current band and its bottom edge


def est_lines(text, size, w, *, bold=False):
    k = (98.0 if bold else 104.0) / max(size, 1.0)
    n = 0
    for para in text.split("\n"):
        plain = para.replace("**", "")
        n += max(1, math.ceil(len(plain) / max(1.0, w * k)))
    return n


def est_h(text, size, w, *, bold=False, ls=1.15, extra=0.05):
    return est_lines(text, size, w, bold=bold) * size * ls * 1.09 / 72.0 + extra


# Margin against the systematic under-count of est_h above 10.5 pt
# (notes/mcp-limitations.md [#212-6]): band and step heights are computed
# with it, while the _check guard is left on the bare estimate — otherwise
# it stays silent exactly where the text really does spill.
SF = 1.04


def fit_h(text, size, w, *, bold=False, ls=1.15, extra=0.05):
    return est_h(text, size, w, bold=bold, ls=ls, extra=extra) * SF


def _check(need, given, y, what):
    """Complain into the build console rather than silently clipping:
    overflow on these slides is the main risk, and it should be seen as a
    number, not by eye."""
    if need > given + 0.02:
        WARN.append(f"{_SID[0]} {_BAND[0]}: {what} does not fit — needs "
                    f"{need:.2f}\", given {given:.2f}\"")
    if y + need > _BAND[1] + 0.02 and _BAND[1] > 0:
        WARN.append(f"{_SID[0]} {_BAND[0]}: {what} runs past the band by "
                    f"{y + need - _BAND[1]:.2f}\"")


def free_slide(sid, label=""):
    """Address the guard for a slide of this band built WITHOUT card bands
    (there is exactly one such slide now — s45a).

    `_SID` / `_BAND` are module globals: they are set by `head()` and
    `row()`, i.e. by the card form. A slide that calls neither inherited the
    name and the bottom edge of the PREVIOUS card's band, and overflow in it
    was reported under someone else's address (the warning about the s45a
    legend arrived as "s38b WHERE IT BREAKS" — exactly what happened, issue
    #212). Here the name is set explicitly and the bottom edge is zeroed:
    there is no band, so there is nothing to check for running past it, and
    `_check` is left with the honest "text against the height of its own
    box" comparison only.
    """
    _SID[0] = sid
    _BAND[0] = label
    _BAND[1] = 0.0


class Cursor:
    """The bands of a card stack top to bottom by themselves: a slide
    specifies only the content height of a band, the vertical bookkeeping
    lives here."""

    def __init__(self, top=None):
        self.y = _TOP[0] if top is None else top

    def band(self, slide, kind, label, h):
        x, y, w, hh = row(slide, self.y, h, kind, label)
        self.y += h + RGAP
        return x, y, w, hh

    def text(self, slide, kind, label, text, *, size=10.5, bold=False,
             bold_color=MID, min_h=0.0, pad=0.10):
        ch = max(min_h, fit_h(text, size, CW - 2 * PAD, bold=bold) + pad)
        x, y, w, h = self.band(slide, kind, label, ch + 2 * PAD_Y)
        md_box(slide, x, y, w, h, text, size=size, base_bold=bold,
               color=DEEP, bold_color=(DEEP if bold else bold_color),
               line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
        return x, y, w, h

    def edge(self, slide, text, *, size=10.0, label="WHERE IT BREAKS",
             min_h=0.0):
        return self.text(slide, "edge", label, text, size=size, bold=True,
                         min_h=min_h)


def row(slide, y, h, kind, label):
    """One band of a card: the label on the left + the content container on
    the right. Returns (x, y, w, h) of the inner content area."""
    k = KIND[kind]
    ocean_box(slide, X0, y, LBL_W, h, fill=k["lab"], stroke=k["lab"],
              stroke_pt=1.0)
    text_box(slide, x=X0 + 0.05, y=y, w=LBL_W - 0.10, h=h, text=label,
             size=9.5, bold=True, color=k["labc"], align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
    ocean_box(slide, CX, y, CW, h, fill=k["fill"], stroke=k["stroke"],
              stroke_pt=k["pt"])
    _BAND[0] = label
    _BAND[1] = y + h - PAD_Y
    return CX + PAD, y + PAD_Y, CW - 2 * PAD, h - 2 * PAD_Y


# ============================================================
# Text primitives of a band
# ============================================================
def md_box(slide, x, y, w, h, text, *, size=10.5, color=DEEP, bold_color=MID,
           line_spacing=1.15, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
           font=FONT_BODY, space_before=None, base_bold=False):
    """Text with **bold** markup: one call instead of assembling runs by
    hand."""
    runs = []
    first_line = True
    for line in text.split("\n"):
        newp = not first_line
        first_line = False
        started = False
        for part in re.split(r'(\*\*.+?\*\*)', line):
            if not part:
                continue
            b = part.startswith("**") and part.endswith("**")
            txt = part[2:-2] if b else part
            cfg = {"text": txt, "size": size,
                   "bold": (True if b else base_bold),
                   "color": (bold_color if b else color)}
            if newp and not started:
                cfg["newpara"] = True
                if space_before is not None:
                    cfg["space_before"] = space_before
            started = True
            runs.append(cfg)
        if not started:
            cfg = {"text": " ", "size": size, "color": color}
            if newp:
                cfg["newpara"] = True
            runs.append(cfg)
    _check(est_h(text, size, w, bold=base_bold, ls=line_spacing), h, y,
           "text")
    return text_runs(slide, x, y, w, h, runs, align=align, anchor=anchor,
                     line_spacing=line_spacing, font=font)


STEP_IND = 0.34


def steps_h(items, w, size, *, gap=0.07):
    """How much room the numbered steps will take — computed before drawing,
    so that the band height comes from the content and not from the eye."""
    hs = [fit_h(t, size, w - STEP_IND) for t in items]
    return sum(hs) + gap * (len(hs) - 1)


def steps(slide, x, y, w, items, *, size=10.5, gap=0.07, num_fill=MID,
          bold_color=MID, start=1, line_spacing=1.15):
    """Numbered steps: a circle with the number + the text.
    items = [text, ...]."""
    yy = y
    n = start
    for txt in items:
        h = fit_h(txt, size, w - STEP_IND, ls=line_spacing)
        circle(slide, x, yy + 0.015, 0.235, num_fill)
        text_box(slide, x=x, y=yy + 0.015, w=0.235, h=0.235, text=str(n),
                 size=8.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        md_box(slide, x + 0.34, yy, w - 0.34, h, txt, size=size,
               bold_color=bold_color, line_spacing=line_spacing)
        yy += h + gap
        n += 1
    return yy


def mono_fit(lines, w, size, pitch, pad=0.13):
    """Type size and leading of a listing squeezed to the width of its box:
    a long path line must not run past the frame, nor the frame past the
    band."""
    longest = max(len(l) for l in lines)
    avail_pt = (w - 2 * pad - 0.08) * 72.0
    if longest * size * 0.615 > avail_pt:
        size = max(6.6, avail_pt / (longest * 0.615))
        pitch = min(pitch, size * 0.0198)
    return size, pitch


def mono_h(lines, w, *, size=8.5, pitch=0.168, pad=0.13):
    size, pitch = mono_fit(lines, w, size, pitch, pad)
    return len(lines) * pitch + 2 * pad


def mono_box(slide, x, y, w, lines, *, size=8.5, pitch=0.168, pad=0.13,
             fill=WHITE, stroke=SOFT_GREY, stroke_pt=1.1, color=DEEP,
             comment_color=SLATE, h=None):
    """A white box with a monospaced listing of an artefact. Comments after
    "#" are muted so that the path reads first."""
    size, pitch = mono_fit(lines, w, size, pitch, pad)
    hh = h if h is not None else len(lines) * pitch + 2 * pad
    _check(len(lines) * pitch + 2 * pad, hh, y, "listing")
    ocean_box(slide, x, y, w, hh, fill=fill, stroke=stroke,
              stroke_pt=stroke_pt, radius_pt=7.0)
    for j, line in enumerate(lines):
        yy = y + pad + j * pitch
        if "#" in line:
            head, tail = line.split("#", 1)
            runs = []
            if head:
                runs.append({"text": head, "size": size, "color": color,
                             "font": FONT_MONO})
            runs.append({"text": "#" + tail, "size": size,
                         "color": comment_color, "font": FONT_MONO})
            text_runs(slide, x + pad, yy, w - 2 * pad, pitch + 0.04, runs,
                      line_spacing=1.0, font=FONT_MONO)
        else:
            text_box(slide, x=x + pad, y=yy, w=w - 2 * pad, h=pitch + 0.04,
                     text=line, size=size, color=color, font=FONT_MONO,
                     line_spacing=1.0)
    return y + hh


def what_is_it(slide, C, text, *, size=10.2):
    """Rule R8, block 1: what this is at all, in plain words, for a
    newcomer. A separate function rather than just C.text(...), so that the
    band is exactly one across all the rebuilt practices and cannot be
    skipped by accident."""
    return C.text(slide, "what", "WHAT IT IS", text, size=size,
                  bold_color=DEEP)


def mechanism(slide, C, items, *, size=10.5, schema=None, schema_w=0.0,
              schema_h=0.0, gap=0.30, step_gap=0.07, label="HOW IT WORKS"):
    """Rule R8, block 2: how the practice works — as NUMBERED STEPS rather
    than prose, and with a labelled diagram on the right (rule R4). The band
    height comes from the content: from the total height of the steps and
    from the height of the diagram, whichever is greater — not assigned by
    eye, as it was on all twelve cards before the forms were brought
    together."""
    inner = CW - 2 * PAD
    sw = inner - (schema_w + gap) if schema else inner
    need = max(steps_h(items, sw, size, gap=step_gap), schema_h)
    x, y, w, h = C.band(slide, "mech", label, need + 2 * PAD_Y)
    steps(slide, x, y, sw, items, size=size, gap=step_gap)
    if schema:
        schema(slide, x + sw + gap, y, schema_w, h)
    return x, y, w, h


def compare(slide, C, left, right, *, label="WITH AI AND WITHOUT", size=9.5):
    """Rule R6: the key practices with AI and without — in TWO COLUMNS, not
    as a list of tools. left/right = (heading, text, colour)."""
    gap = 0.20
    colw = (CW - 2 * PAD - gap) / 2.0
    # 0.30 — the height of the column heading line, 0.06 — its offset from
    # the text, 0.06 — margin for est_h rounding: otherwise the band comes
    # out ~0.04" short.
    need = max(fit_h(left[1], size, colw - 0.22, ls=1.12),
               fit_h(right[1], size, colw - 0.22, ls=1.12)) + 0.42
    x, y, w, h = C.band(slide, "cmp", label, need + 2 * PAD_Y)
    for i, (hdr, body, col) in enumerate([left, right]):
        cx = x + i * (colw + gap)
        ocean_box(slide, cx, y, colw, h, fill=WHITE, stroke=col,
                  stroke_pt=1.4, radius_pt=7.0)
        text_box(slide, x=cx + 0.11, y=y + 0.05, w=colw - 0.22, h=0.24,
                 text=hdr, size=9.2, bold=True, color=col, line_spacing=1.0)
        md_box(slide, cx + 0.11, y + 0.30, colw - 0.22, h - 0.36, body,
               size=size, color=DEEP, bold_color=DEEP, line_spacing=1.12)
    return x, y, w, h


def head(p, title, *, sid="", size=19, y=0.13, h=None):
    """An assertion headline: the height is computed from the length, and
    the top of the card from that height, so that a two-line headline does
    not slide onto the first band."""
    _SID[0] = sid
    _TAIL[0] = 0.0
    s = blank(p)
    set_slide_bg(s, WHITE)
    if h is None:
        h = est_h(title, size, 11.80, bold=True, ls=1.10, extra=0.04)
    slide_title(s, title, size=size, y=y, h=h, w=12.25)
    _TOP[0] = y + h + 0.10
    return s


def tiny(slide, x, y, w, text, *, size=8.6, color=SLATE, align=PP_ALIGN.LEFT,
         h=0.22, bold=False, italic=True):
    text_box(slide, x=x, y=y, w=w, h=h, text=text, size=size, color=color,
             italic=italic, bold=bold, align=align, line_spacing=1.05)


# ============================================================
# PRACTICE CARDS — appended below by the porting of slides_band6.py
# ============================================================
# ============================================================
# s11a — rehearsing interview questions on AI personas
# ============================================================
def s11a(p):
    """The single card (issue #212, rule R8 + the forms brought together
    after the methodology review of 2026-09-30): WHAT IT IS -> HOW IT WORKS
    in steps -> WITH AI AND WITHOUT -> WHERE IT BREAKS. The "five
    interviewees" diagram moved inside the mechanism — none of the twelve
    cards carries a separate band for a diagram any more."""
    sid = "s11a"
    s = head(p, "Rehearsing interview questions on AI personas", sid=sid,
             size=21)
    C = Cursor()

    what_is_it(s, C,
               "Before going out to living people, the list of questions is "
               "run past several invented interviewees played by a model. "
               "The point is to catch bad questions before they spoil a real "
               "conversation. The run says nothing about the product. "
               "A rehearsal, not research.",
               size=11.5)

    def panel(sl, gx, gy, gw, gh):
        pw, pg = 0.48, 0.12
        tot = 5 * pw + 4 * pg
        sx = gx + (gw - tot) / 2.0
        for i in range(5):
            px = sx + i * (pw + pg)
            ocean_box(sl, px, gy + 0.10, pw, 0.34, fill=MID_TINT,
                      stroke=LIGHT, stroke_pt=1.0, radius_pt=6.0)
            icon(sl, "users", px + (pw - 0.20) / 2, gy + 0.17, 0.20, "mid")
            if i < 4:
                connector(sl, px + pw, gy + 0.27, px + pw + pg, gy + 0.27,
                          color=SLATE, width=1.0, dash="dash")
        icon(sl, "x", sx + tot / 2 - 0.09, gy + 0.18, 0.18, "gold")
        tiny(sl, gx, gy + 0.48, gw,
             "the invented interviewees do not hear each other",
             align=PP_ALIGN.CENTER, size=9.0, h=0.24)
        connector(sl, gx + gw / 2, gy + 0.78, gx + gw / 2, gy + 0.98,
                  color=MID, width=2.0, arrow_end=True)
        ocean_box(sl, gx + 0.05, gy + 1.02, gw - 0.10, 0.70, fill=GOLD_TINT,
                  stroke=GOLD, stroke_pt=1.5, radius_pt=8.0)
        text_box(sl, x=gx + 0.14, y=gy + 1.02, w=gw - 0.28, h=0.70,
                 text="the only thing that leaves is\na corrected list of "
                      "questions",
                 size=10.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)

    mechanism(s, C, [
        "Several different customer types are described — by how a person "
        "lives with the task: what they use now, what it costs them, what "
        "they once tried and dropped. **A character sketch is no use here.**",
        "Each type is kept apart, so that the answers do not run together "
        "into one common voice.",
        "The same list of questions is run past all of them.",
        "Two things are read, **and the answers are not among them:** a "
        "question everyone answered the same way tells nobody apart; a "
        "question answered in terms of an imagined future invites a polite "
        "invention. Both get rewritten.",
    ], size=10.0, schema=panel, schema_w=3.45, schema_h=1.76)

    compare(s, C,
            ("WITHOUT AI — how the rehearsal has always been run",
             "The list of questions is talked through with a colleague, or "
             "one live interview out of eight is spent on the rehearsal. It "
             "works, but it gives one point of view and costs a day.", MID),
            ("WITH AI — what changed",
             "The rehearsal takes minutes, and a dozen runs are affordable. "
             "**Only the rehearsal** gets cheaper: nothing replaces the "
             "interview with a living person.", TEAL))

    C.edge(s,
           "The interviewees' answers are not data about users: there is one "
           "model, and five interviewees give five views of that one model. "
           "There are no five people behind them. Checked against a real "
           "national survey, the model reproduces the average answers and "
           "halves the spread of opinion (**16 against 31**). If a "
           "conclusion about the product has been carried out of the run, "
           "the practice has been run wrong: its output is a corrected "
           "question.",
           size=11.0)

    src(s, X0, 7.04, 11.5,
        "Synthetic answers checked against a real national survey — Bisbee, "
        "Clinton, Dorff, Kenkel, Larson, Political Analysis, 2024")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s11b — searching accumulated support tickets for the pain
# ============================================================
def s11b(p):
    """The single card: WHAT IT IS -> HOW IT WORKS in steps -> WITH AI AND
    WITHOUT -> WHERE IT BREAKS. The three horizontal stage cards are folded
    into steps with a labelled diagram on the right; the funnel of the bias
    stayed with the boundary."""
    sid = "s11b"
    s = head(p, "Searching accumulated support tickets for the pain", sid=sid,
             size=21)
    C = Cursor()

    what_is_it(s, C,
               "A product with users already has an archive of complaints "
               "and questions. The practice turns it into a source of "
               "hypotheses: the tickets go into a searchable store, the "
               "ones close in meaning are grouped, and you see which themes "
               "repeat. What leaves is a named theme of pain.",
               size=11.5)

    def flow(sl, gx, gy, gw, gh):
        names = [("database", "store\nand tag", MID),
                 ("search-check", "search by word\nand by meaning", LIGHT),
                 ("group", "gather what is close\ninto groups", TEAL)]
        bh = 0.46
        for i, (ic, lab, col) in enumerate(names):
            by = gy + 0.06 + i * (bh + 0.18)
            ocean_box(sl, gx, by, gw, bh, fill=WHITE, stroke=col,
                      stroke_pt=1.6, radius_pt=7.0)
            icon(sl, ic, gx + 0.14, by + (bh - 0.24) / 2, 0.24, "mid")
            text_box(sl, x=gx + 0.48, y=by, w=gw - 0.60, h=bh, text=lab,
                     size=9.6, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=1.04)
            if i < 2:
                connector(sl, gx + gw / 2, by + bh, gx + gw / 2,
                          by + bh + 0.18, color=LIGHT, width=2.0,
                          arrow_end=True)
        tiny(sl, gx, gy + 0.06 + 3 * bh + 2 * 0.18 + 0.04, gw,
             "order matters: skip the tagging and the archive becomes a "
             "bag of text", size=8.8, align=PP_ALIGN.CENTER, h=0.30)

    mechanism(s, C, [
        "Every ticket goes into one common store, tagged with when it "
        "arrived, who it came from and which product it is about.",
        "The search runs **two ways at once**: on an exact match of words, "
        "and on meaning. An error code is found only by the first; a problem "
        "described in a person's own words only by the second.",
        "What is close is gathered into groups and retold in two passes: "
        "first each ticket on its own, then what the group has in common. "
        "Skip the first pass and 20–40% of the detail is lost.",
    ], size=10.0, schema=flow, schema_w=3.05, schema_h=2.16)

    compare(s, C,
            ("WITHOUT AI — tagging by theme, by hand",
             "Tickets are sorted into a list of themes thought up in "
             "advance. So the only themes found are the ones somebody has "
             "already guessed at.", MID),
            ("WITH AI — what changed",
             "What is close in meaning gathers itself, with no list of "
             "themes, and a group is retold in minutes. **The name of the "
             "theme is still checked by a person:** the machine groups, it "
             "takes no decisions.", TEAL))

    x, y, w, h = C.band(s, "edge", "WHERE IT BREAKS", 1.34)
    md_box(s, x, y, w - 2.55, h,
           "The archive is biased **by construction**: it holds only those "
           "who got as far as complaining. Volume does not cure it: **there "
           "is no ticket saying \"I need what you do not have at all\"**. "
           "The question \"why do people not get as far as signing up\" is "
           "not one it answers: that takes a conversation with those who "
           "left. And the search returns what is **close**, it does not "
           "weigh importance: ten thousand complaints about one typo are "
           "still one typo.",
           size=10.5, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    fx = x + w - 2.35
    ocean_box(s, fx, y + 0.02, 2.30, h - 0.04, fill=WHITE, stroke=GOLD,
              stroke_pt=1.2, radius_pt=7.0)
    icon(s, "funnel", fx + 0.12, y + 0.12, 0.26, "gold")
    text_box(s, x=fx + 0.46, y=y + 0.10, w=1.74, h=0.32,
             text="who got as far as complaining", size=9.5, bold=True,
             color=DEEP, line_spacing=1.05)
    filled_rect(s, fx + 0.16, y + 0.46, 1.98, 0.20, LIGHT, radius=True,
                radius_adj=0.35)
    tiny(s, fx + 0.16, y + 0.66, 1.98, "all users", size=8.5)
    filled_rect(s, fx + 0.16, y + 0.88, 0.40, 0.20, GOLD, radius=True,
                radius_adj=0.35)
    tiny(s, fx + 0.62, y + 0.88, 1.55, "the ticket archive", size=8.5,
         color=DEEP, bold=True, italic=False, h=0.22)

    src(s, X0, 7.04, 11.5,
        "Two-step synthesis — Teresa Torres, a coach of product teams and "
        "the author of \"Continuous Discovery Habits\", a book on continuous "
        "user research")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s17a — a design system as an automatic check
# ============================================================
def s17a(p):
    """The single card. The layers stayed, but they live inside HOW IT WORKS
    as a labelled diagram; the first block was moved into the common light
    "WHAT IT IS" band (it used to be drawn, wrongly, as the teal band of the
    removed "criterion" block — which made the section look like a school of
    its own)."""
    sid = "s17a"
    s = head(p, "A design system: shared interface rules that a machine can "
                "check on its own", sid=sid)
    C = Cursor()

    what_is_it(s, C,
               "A **design system** is the shared body of interface rules "
               "for a product and the ready-made components that go with "
               "it: the colour combinations allowed, the sizes of buttons "
               "and fields, how an element looks under the cursor. It used "
               "to be a document for people. What matters more now is the "
               "other part: some of the rules can be written so that a "
               "machine reads and checks them.",
               size=11.5)

    def layers(sl, gx, gy, gw, gh):
        rows = [("shield-check", "3", "A CHECK THAT\nSTOPS THE RELEASE",
                 TEAL, 1.00, 0.66,
                 "The rule is checked automatically on every generated "
                 "screen, and a breach is blocked with no discussion. "
                 "**Only this layer gives a guarantee.**"),
                ("component", "2", "OWN COMPONENTS\nINSTEAD OF STOCK ONES",
                 MID, 0.88, 0.56,
                 "The generator is given the team's own components. This "
                 "**lowers the chance of a breach and guarantees "
                 "nothing.**"),
                ("palette", "1", "RULES WRITTEN\nAS NUMBERS",
                 LIGHT, 0.76, 0.56,
                 "While a rule lives in a picture of a mockup, only a "
                 "person can check it, and only by eye.")]
        tiny(sl, gx, gy, gw,
             "from the bottom up: each layer is stronger than the one below "
             "it, and only the top one turns a wish into a guarantee",
             size=9.2, h=0.26)
        yy = gy + 0.30
        for ic, num, name, col, frac, bh, body in rows:
            bw = gw * frac
            ocean_box(sl, gx, yy, bw, bh, fill=WHITE, stroke=col,
                      stroke_pt=(2.2 if num == "3" else 1.2), radius_pt=8.0)
            filled_rect(sl, gx, yy, 2.42, bh, col, radius=True,
                        radius_adj=0.10)
            icon(sl, ic, gx + 0.14, yy + (bh - 0.26) / 2, 0.26, "white")
            text_box(sl, x=gx + 0.48, y=yy, w=1.88, h=bh,
                     text=f"{num}. {name}", size=9.2, bold=True, color=WHITE,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
            md_box(sl, gx + 2.56, yy + 0.04, bw - 2.68, bh - 0.08, body,
                   size=10.2, line_spacing=1.12, anchor=MSO_ANCHOR.MIDDLE)
            yy += bh + 0.06

    x, y, w, h = C.band(s, "mech", "HOW IT WORKS", 2.40)
    layers(s, x, y, w, h)

    compare(s, C,
            ("WITHOUT AI — a body of rules for people",
             "A designer checks it by eye: a set of rules keeps the product "
             "consistent.", MID),
            ("WITH AI — why the rules became machine-readable",
             "The generator turns out screens faster than a person can look "
             "at them. A machine check **grows with the generation**.",
             TEAL))

    # EDIT #212 (R3-2026-10-01): the last sentence continues the caveat from
    # the slide on the scope of design (s14a): a machine check covers the
    # screen.
    C.edge(s,
           "A machine checks only what can be expressed as a number. \"Is "
           "this clear to a living person\" stays with the person: a screen "
           "can pass every check and remain unclear. And separately: **a "
           "request to the generator is not a control mechanism** — a "
           "mechanism is a rule that can stop a release. This check looks "
           "at the screen: the system's behaviour over time cannot be "
           "expressed as a number and is not covered.",
           # EDIT #212 (forms brought together 2026-10-01): it was 11.0 —
           # five lines instead of four, the band reached 7.22" and ran into
           # both the sources line (7.04" on every other card of this band)
           # and the page-number corner (7.16"). The guard stayed silent: it
           # compares the text against the height of ITS OWN band, and the
           # band itself is sized by Cursor.text from that same est_h — there
           # is no overflow inside the band, the band ran past the foot of
           # the slide. 10.0 gives four lines with room to spare (s24a and
           # s45b carry the same size on longer text) and a bottom edge of
           # 6.95"; not one word of the text was cut.
           size=10.0)
    notes_with_sources(s, sid)
    return s


# ============================================================
# s24a — the autonomy scale
# ============================================================
def s24a(p):
    """The single card. The "SCALE" band is gone: the scale became a
    labelled diagram inside HOW IT WORKS, and the prose "how it works" was
    broken into steps — in Section 3 not one of the three practices had any.

    owner-review 2026-10-01: a speculative support bot was replaced by a
    measured case — RADAR at Meta (the level is set by a number, the raising
    of the threshold is documented, the consequences are measured against a
    named baseline). What was added to the boundary is what separates the
    practice from the anti-pattern of Lecture 4: the last word belongs to a
    deterministic check, and merging on the verdict of an AI reviewer is a
    different thing."""
    sid = "s24a"
    s = head(p, "The autonomy scale — the right to decide, given in parts",
             sid=sid, size=20)
    C = Cursor()

    what_is_it(s, C,
               "A feature is released by autonomy levels — from a hint, to a "
               "proposal that a person confirms, and on to a decision the "
               "system takes itself (the levels on the right). **A version "
               "here means the autonomy level the system has earned.**",
               size=10.8)

    def ladder(sl, gx, gy, gw, gh):
        rungs = [("it hints", "a person decides", LIGHT),
                 ("it proposes a solution", "a person confirms", MID),
                 ("it decides itself", "hands hard cases back to a person",
                  TEAL)]
        bh = 0.50
        for i, (lab, sub, col) in enumerate(rungs):
            by = gy + 0.04 + i * (bh + 0.18)
            filled_rect(sl, gx, by, gw, bh, col, radius=True, radius_adj=0.10)
            text_box(sl, x=gx + 0.10, y=by + 0.04, w=gw - 0.20, h=0.26,
                     text=lab, size=11.5, bold=True, color=WHITE,
                     align=PP_ALIGN.CENTER, line_spacing=1.02)
            text_box(sl, x=gx + 0.10, y=by + 0.30, w=gw - 0.20, h=0.22,
                     text=sub, size=8.8, color=WHITE, align=PP_ALIGN.CENTER,
                     line_spacing=1.02)
            if i < 2:
                connector(sl, gx + gw / 2, by + bh, gx + gw / 2,
                          by + bh + 0.18, color=GOLD, width=2.4,
                          arrow_end=True)
        tiny(sl, gx, gy + 0.04 + 3 * bh + 2 * 0.18 + 0.04, gw,
             "the autonomy scale: product versions have nothing to do with "
             "it", size=8.8, align=PP_ALIGN.CENTER, h=0.34)

    mechanism(s, C, [
        "Each level is **a separate release**: its own circle of users, its "
        "own set of observed signals, its own way to stop.",
        "The move up is opened by **evidence written down as a number before "
        "the run**: the system copes with the cases the new level entrusts "
        "to it. The calendar does not count as grounds.",
        "The evidence has to hold **across repeated attempts**. A single "
        "success does not give it.",
        "It is set out in advance **how to put the system back a level**: "
        "who decides, on what signal, and within what time.",
    ], size=10.0, schema=ladder, schema_w=3.30, schema_h=2.34)

    compare(s, C,
            ("WITHOUT AI — rights have long been handed out in parts",
             "To people and to automation alike: a newcomer is first allowed "
             "to watch, then to propose, then to decide alone. The level "
             "rests on time served without complaints.", MID),
            ("WITH AI — the level is confirmed by measurement",
             "A system gains no experience. Meta moved the risk threshold "
             "for merging without a person from the 25th percentile to the "
             "50th: **60.31%** are approved automatically. Rollbacks are "
             "**three times rarer**, production incidents **50 times "
             "rarer**, than on the ordinary path (535,000 changes).",
             TEAL), size=9.0)

    C.edge(s,
           "\"The operator has not corrected anything in ages\" is not "
           "evidence: **an absence of remarks is an absence of "
           "measurement.** Automatic approval rests on **a deterministic "
           "check at the end of the chain**; merging on the verdict of an AI "
           "reviewer removes the only control there is. And the irreversible "
           "and the expensive are never raised to the top level: a binding "
           "offer to a customer, the deletion of working data, a release to "
           "everyone at once — those sit behind a hard rule placed above the "
           "model.",
           size=10.0)

    src(s, X0, 7.04, 11.5,
        "Aishwarya Reganti (Amazon) and Kiriti Badam (OpenAI), 19 August "
        "2025 — a review of more than 50 deployments · Meta RADAR, arXiv "
        "2605.30208: 535,000 changes, the risk threshold moved from the 25th "
        "to the 50th percentile")
    notes_with_sources(s, sid)
    return s
# ============================================================
# s24b — mutation testing
# ============================================================
def s24b(p):
    """The practice was rebuilt from scratch per owner-review 2026-10-01
    (issue #212).

    It used to be "the golden set" — that almost word for word repeated the
    eval loop from Section 4 (s31a), and the owner removed the duplicate.
    Now it is mutation testing as applied to work with AI. Two supports, and
    the practice has to be a step forward against both rather than a
    retelling of them:
      * Lecture 4 §4.3 — the CODE was mutated, to check the tests (the share
        of mutants killed is more honest than coverage; Meta 32/5.3 %
        against 2.4/15 %);
      * the owner's article "AI delivery gap" (25 Sept 2026) — a check that
        has never had a defect planted in it on purpose is treated as
        broken.
    The step forward: the practice is pointed at the checks AROUND the AI —
    the golden set, the agent instructions file, a rule in the pipeline.
    That is what the diagram on the right carries.

    The 27 % figure (defects not linked to any mutant) is taken from the
    primary source, Just et al., FSE 2014 — 63 out of 357; the owner's
    article gives 17 %, and that divergence is raised in the report.
    """
    sid = "s24b"
    s = head(p, "A check that has never had a defect planted in it on "
                "purpose counts as broken", sid=sid, size=19)
    C = Cursor()

    what_is_it(s, C,
               "**Mutation testing** — a small error (a \"mutant\") is put "
               "into the code on purpose and you watch whether any check "
               "fails. The share of mutants killed tells you whether the "
               "checks catch anything; coverage answers another question — "
               "was the line touched by the run. With AI the same practice "
               "is pointed at everything that constrains it: **the golden "
               "set, the agent instructions file, a rule in the pipeline**.",
               size=10.8)

    def seeded(sl, gx, gy, gw, gh):
        """Three rows of "what we check → which defect we plant". That is
        the development of the practice: in Lecture 4 it was the code that
        was mutated, here it is the checks around the model, and the rows
        run from the familiar one to the new one."""
        text_box(sl, x=gx, y=gy, w=gw, h=0.40,
                 text="The same practice on three checks",
                 size=10.2, bold=True, color=DEEP, line_spacing=1.08)
        rows = [("Unit tests", "flip a condition", DEEP),
                ("The golden set", "swap the answer for\na nearly right one",
                 DEEP),
                ("The agent\ninstructions file",
                 "a task where breaking\nthe rule is shorter", TEAL)]
        ty = gy + 0.44
        for lab, val, vc in rows:
            fl = TEAL_TINT if vc == TEAL else MID_TINT
            st = TEAL if vc == TEAL else LIGHT
            ocean_box(sl, gx, ty, gw, 0.52, fill=fl, stroke=st,
                      stroke_pt=1.2, radius_pt=7.0)
            text_box(sl, x=gx + 0.12, y=ty, w=gw * 0.48, h=0.52, text=lab,
                     size=9.4, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=1.06)
            text_box(sl, x=gx + gw * 0.50, y=ty, w=gw * 0.48, h=0.52,
                     text=val, size=9.4, bold=True, color=vc,
                     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT,
                     line_spacing=1.06)
            ty += 0.56
        tiny(sl, gx, ty, gw,
             "silence in answer to a planted defect is what having no "
             "check means",
             size=9.0, h=0.22)

    mechanism(s, C, [
        "Name the check you rely on, and **the class of errors it is "
        "obliged to catch**.",
        "Put an error of that class in **on purpose** — one, small, in one "
        "place.",
        "Run the check. **Silence means there is no check**: it does not "
        "tell the sound from the spoilt.",
        "Record the share caught **as a number** and remeasure after every "
        "edit to the check: checks go stale quietly.",
    ], size=9.8, schema=seeded, schema_w=4.30, schema_h=2.30)

    compare(s, C,
            ("WITHOUT AI — the mutants come from a list of rules",
             "Flip a condition, shift a boundary, take out a call. The run "
             "is reproducible and there are tools for every language: PIT, "
             "mutmut, Cosmic Ray, Stryker.", MID),
            ("WITH AI — the model writes the mutants",
             "They sit closer to real errors: they find **76.5%** of real "
             "defects against **44.2%** for the list of rules (851 "
             "defects). The price — about a third of them do not compile.",
             TEAL), size=9.0)

    C.edge(s,
           "Some defects the practice cannot see by construction: of 357 "
           "real errors, **27% are not linked to any mutant** — wrong "
           "algorithms and code that should have been deleted. And the "
           "share killed spoils the same way coverage does: put a gate on "
           "it and easily killed mutants start breeding, while detection "
           "does not grow.",
           size=9.8)

    src(s, X0, 7.04, 11.5,
        "A continuation of Lecture 4 §4.3 · mutants from a model against a "
        "list of rules: 76.5% against 44.2% on 851 real defects "
        "(arXiv 2406.09843) · 27% of defects with no linked mutant — "
        "Just et al., FSE 2014")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s24c — staged rollout and the rollback path
# ============================================================
def s24c(p):
    """One card. The "DIAGRAM" band is gone — the rollout stages and the
    rollback path became a labelled diagram inside HOW IT WORKS, and the
    prose "HOW IT WORKS" was broken out into steps. The "WITH AI AND
    WITHOUT" block carries a load of its own here: the practice is a classic
    one, and the slide says so outright instead of passing over it."""
    sid = "s24c"
    s = head(p, "Staged rollout and the rollback path — how to set the cost "
                "of an error in advance", sid=sid, size=20)
    C = Cursor()

    what_is_it(s, C,
               "Something new is switched on gradually: first for a narrow "
               "circle, then wider. And the way to bring it all back is "
               "agreed in advance. **The blast radius — how many people get "
               "hurt if the new thing turns out to be bad — is set by the "
               "team itself, before launch.**",
               size=11.5)

    def stages(sl, gx, gy, gw, gh):
        names = ["narrow circle", "small share", "part of the audience",
                 "everyone"]
        fills = [SOFT_GREY, MID_TINT, TEAL_TINT, GOLD_TINT]
        strokes = [LIGHT, LIGHT, TEAL, GOLD]
        bh = 0.36
        bx = gx + 0.74
        bw = gw - 0.74
        for i, nm in enumerate(names):
            by = gy + 0.04 + i * (bh + 0.12)
            ocean_box(sl, bx, by, bw, bh, fill=fills[i], stroke=strokes[i],
                      stroke_pt=1.3, radius_pt=7.0)
            text_box(sl, x=bx + 0.06, y=by, w=bw - 0.12, h=bh, text=nm,
                     size=10.2, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
            if i < 3:
                connector(sl, bx + bw / 2, by + bh, bx + bw / 2,
                          by + bh + 0.12, color=MID, width=2.0,
                          arrow_end=True)
        top_y = gy + 0.04
        bot_y = gy + 0.04 + 3 * (bh + 0.12) + bh / 2
        connector(sl, gx + 0.54, bot_y, gx + 0.54, top_y + bh / 2,
                  color=GOLD, width=2.5, arrow_end=True)
        text_box(sl, x=gx - 0.28, y=gy + 0.72, w=0.76, h=0.30,
                 text="rollback\npath", size=9.2, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER, line_spacing=1.04)
        tiny(sl, gx, gy + 0.04 + 4 * bh + 3 * 0.12 + 0.04, gw,
             "audience share grows in stages; the rollback path is "
             "written before launch", size=8.8,
             align=PP_ALIGN.CENTER, h=0.30)

    mechanism(s, C, [
        "**Rollout stages** — which shares of the audience, and in what "
        "order.",
        "**Stop signal** — what is watched at each stage and what degree of "
        "worsening halts the move forward; with no signal named in advance, "
        "\"it got worse\" is argued about endlessly.",
        "**Rollback path** — who takes the decision to go back, how long "
        "that takes, and whether anyone has checked that going back works "
        "at all.",
    ], size=10.0, schema=stages, schema_w=3.30, schema_h=2.18)

    compare(s, C,
            ("WITHOUT AI — the practice is several decades old",
             "Staged rollout and rollback were invented long before AI and "
             "are built exactly the same way. **There is nothing to invent "
             "again**, you take what is already there.", MID),
            ("WITH AI — only the speed of the stages changes",
             "An ordinary feature shows up in errors and latency at once; "
             "worsening answers show only at volume: every stage needs "
             "**hours of watching, not minutes**.", TEAL))

    C.edge(s,
           "A rollout limits the radius, but **it does not replace the "
           "decision**. A long pilot on a tiny share that keeps failing has "
           "hit the approach's ceiling; \"a little more data\" will not "
           "cure it. The opposite error is as real: **maturity gives no "
           "right to skip the pilot** — it raises the cost of skipping. "
           "And a rollback path written down but never tested stays an "
           "intention.",
           size=11.0)

    notes_with_sources(s, sid)
    return s


# ============================================================
# s30a — pre-registration of an experiment
# ============================================================
def s30a(p):
    """One card. The "PRACTICES 2026" band with the experimentation
    platforms is gone: the platforms have nothing to do with AI and were
    taking up room. In its place — the common WITH AI AND WITHOUT block,
    which also closes the roast finding "zero mentions of AI in the visible
    layer of the longest practice in the deck": the chapter (§4.2) has
    exactly what AI changes in this practice — the unit of assignment, and a
    set of quantities in place of one."""
    sid = "s30a"
    s = head(p, "Pre-registration: the decision is written down before the "
                "result is seen", sid=sid, size=19)
    C = Cursor()

    what_is_it(s, C,
               "A short note made **before** the experiment is launched: "
               "what exactly we measure, what result counts as success, "
               "when we stop. The practice came from medicine — there the "
               "protocol is registered before patients are recruited, "
               "otherwise the journal will not take the paper.",
               size=11.5)

    def axis(sl, gx, gy, gw, gh):
        ax_y = gy + 0.52
        connector(sl, gx + 0.10, ax_y, gx + gw - 0.15, ax_y, color=SLATE,
                  width=1.6, arrow_end=True)
        circle(sl, gx + 0.30, ax_y - 0.10, 0.20, GOLD)
        text_box(sl, x=gx + 0.02, y=ax_y - 0.46, w=1.90, h=0.30,
                 text="note made", size=9.2, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.04)
        circle(sl, gx + gw - 0.85, ax_y - 0.10, 0.20, MID)
        text_box(sl, x=gx + gw - 1.75, y=ax_y - 0.46, w=1.80, h=0.30,
                 text="first result", size=9.2, bold=True, color=MID,
                 align=PP_ALIGN.CENTER, line_spacing=1.04)
        connector(sl, gx + 0.40, ax_y + 0.16, gx + gw - 0.85, ax_y + 0.16,
                  color=GOLD, width=1.6, dash="dash")
        tiny(sl, gx, ax_y + 0.26, gw,
             "the success criterion was written down earlier than the "
             "first result", size=9.0,
             align=PP_ALIGN.CENTER)
        md_box(sl, gx, ax_y + 0.58, gw, 0.86,
               "Three traps — stop on a lucky point, trawl through metrics, "
               "move the threshold — **every one of them needs the success "
               "criterion to be choosable after the result.**",
               size=9.8, line_spacing=1.12)

    mechanism(s, C, [
        "**Four things are written down before launch:** which quantity we "
        "take as the decision metric and which way it has to move; what we "
        "watch as a guardrail metric; what effect size counts as meaningful "
        "and how many observations it needs; under what condition we stop.",
        "**The note is put where time is recorded** — with a date and an "
        "author. The whole mechanism is in that: the timestamp stands "
        "earlier than the first result.",
        "**After launch the note is not rewritten** — the decision taken "
        "and its date are appended to it.",
    ], size=10.0, schema=axis, schema_w=3.90, schema_h=2.00)

    compare(s, C,
            ("WITHOUT AI — the practice comes from medicine",
             "One decision metric, the sample size, the stopping rule — "
             "written down in advance. That is how clinical protocols and "
             "ordinary product experiments work.", MID),
            ("WITH AI — what has to be written down on top",
             "**Randomise by user, not by request:** in a dialogue one "
             "person otherwise lands in both groups. And **several "
             "quantities at once**: a score for answer quality, the share "
             "of re-asks and edits, the cost of a contact.", TEAL))

    x, y, w, h = C.band(s, "edge", "WHERE IT BREAKS", 1.16)
    md_box(s, x, y, w - 3.20, h,
           "**Pre-registration does not make an experiment right — it makes "
           "wrongness visible.** It does not cure the novelty effect: that "
           "needs a separate group held back from the change. And it is "
           "powerless where there are physically not enough observations: "
           "the honest way out is to change the question or the method; the "
           "sample will not help here.",
           size=10.2, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    bx = x + w - 3.00
    ocean_box(s, bx, y, 3.00, h, fill=WHITE, stroke=GOLD, stroke_pt=1.2,
              radius_pt=7.0)
    tiny(s, bx, y + 0.02, 3.00, "over three months of waiting", size=8.6,
         align=PP_ALIGN.CENTER, color=DEEP, bold=True, italic=False, h=0.20)
    base = y + h - 0.20
    for i, (val, cap, col, hh) in enumerate(
            [(31200, "needed per group", MID, 0.30),
             (5000, "available per week", GOLD, 0.30 * 5000 / 31200)]):
        px = bx + 0.30 + i * 1.45
        filled_rect(s, px + 0.25, base - hh, 0.70, hh, col, radius=True,
                    radius_adj=0.08)
        text_box(s, x=px, y=base - hh - 0.18, w=1.20, h=0.16,
                 text=f"{val:,}", size=9.2, bold=True,
                 color=col, align=PP_ALIGN.CENTER, line_spacing=1.0)
        tiny(s, px, base + 0.01, 1.20, cap, size=8.2,
             align=PP_ALIGN.CENTER, color=DEEP, h=0.20)

    src(s, X0, 7.04, 11.5,
        "Random assignment by user against assignment by request · the "
        "31,200 per group calculation is illustrative")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s31a — the eval loop
# ============================================================
def s31a(p):
    """One card.

    owner-review 2026-10-01: the owner did not see what the slide was for,
    what the role of AI in it was, or why development frameworks were listed
    on it. Rebuilt on all three counts. WHAT FOR — the first sentence of the
    "WHAT IT IS" block: the quality of answers changes with no change to the
    code, and the code tests say nothing about it. THE ROLE OF AI — the
    "WITH AI" column, named as three different roles (the subject of
    evaluation, the measuring instrument, the supplier of cases), with the
    decision "what counts as a good answer" left to a human. THE TOOLS —
    step 4 of the mechanism, each with the verb it performs FOR THE
    EVALUATION; LangSmith and Arize Phoenix have been dropped.
    """
    sid = "s31a"
    s = head(p, "The eval loop: see that the answers have got worse before "
                "the user does", sid=sid, size=19)
    C = Cursor()

    what_is_it(s, C,
               "**An evaluation** (an \"eval\") — a set of tasks with the "
               "desired answer written in advance, on which a model or "
               "agent is run. **It is needed because answer quality changes "
               "with no code change:** you switch the model version, a rule "
               "or a source — behaviour moves, while the code tests stay "
               "green and say nothing.",
               size=10.6)

    def loop(sl, gx, gy, gw, gh):
        nw, nh = 1.72, 0.48
        dx2 = gw - nw
        nodes = [("the golden\nset", 0.00, 0.00, MID),
                 ("release", dx2, 0.00, LIGHT),
                 ("live traffic", dx2, 1.00, TEAL),
                 ("postmortem", 0.00, 1.00, SLATE)]
        for lab, dx, dy, col in nodes:
            ocean_box(sl, gx + dx, gy + dy, nw, nh, fill=WHITE, stroke=col,
                      stroke_pt=1.6, radius_pt=8.0)
            text_box(sl, x=gx + dx + 0.06, y=gy + dy, w=nw - 0.12, h=nh,
                     text=lab, size=9.4, bold=True, color=col,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=1.04)
        connector(sl, gx + nw, gy + nh / 2, gx + dx2, gy + nh / 2,
                  color=LIGHT, width=2.0, arrow_end=True)
        connector(sl, gx + dx2 + nw / 2, gy + nh, gx + dx2 + nw / 2,
                  gy + 1.00, color=LIGHT, width=2.0, arrow_end=True)
        connector(sl, gx + dx2, gy + 1.00 + nh / 2, gx + nw,
                  gy + 1.00 + nh / 2, color=SLATE, width=2.0, arrow_end=True)
        connector(sl, gx + nw / 2, gy + 1.00, gx + nw / 2, gy + nh,
                  color=GOLD, width=4.0, arrow_end=True, arrow_len="lg",
                  arrow_w="lg")
        tiny(sl, gx, gy + 1.56, gw,
             "the gold arrow is what makes the loop a loop: a postmortem "
             "adds a row to the golden set — without that step there is no "
             "loop, only a report",
             size=8.8, color=DEEP, h=0.46, align=PP_ALIGN.CENTER)

    mechanism(s, C, [
        "**Before release** — a run against the curated golden set: "
        "reproducible, catches what has broken before.",
        "**After release** — evaluation on live traffic: it opens up inputs "
        "the set never had, and behaviour over long chains.",
        "**Closing** — a postmortem of a production failure adds a row to "
        "the golden set, and it stays there for good.",
        "**What it is run with:** promptfoo drops the build by return code "
        "when the pass rate is below threshold; DeepEval — an ordinary test "
        "run with a minimum score per metric; Braintrust and Langfuse "
        "compare versions and block a merge on a drop.",
    ], size=9.4, schema=loop, schema_w=4.30, schema_h=2.04)

    compare(s, C,
            ("WITHOUT AI — a suite of code tests",
             "The answer is known character by character, the run is "
             "reproducible, the result is \"passed\" or \"failed\".", MID),
            ("WITH AI — three different roles for the AI itself",
             "**The subject of evaluation** — what gets checked. **The "
             "measuring instrument** — an LLM-as-judge scores by a written "
             "rule. **The supplier of cases** — labels live traffic and "
             "proposes additions. A human decides what a good answer is.",
             TEAL), size=9.0)

    C.edge(s,
           "**An LLM-as-judge agrees with a human 80–90% of the time where "
           "the preference is obvious, and falls to 60–65% as soon as the "
           "answers are close or are swapped round** — it is least reliable "
           "exactly where the cost of an error is highest. The corrections: "
           "shuffle the order of the answers, take a judge from a different "
           "family. An experiment on live users costs more and is not "
           "replaced by evals.",
           size=9.8)

    src(s, X0, 7.04, 11.5,
        "The three-layer framework — Hamel Husain, author of the piece "
        "\"Your AI Product Needs Evals\" · agreement of an LLM-as-judge "
        "with a human: 80–90% where the preference is explicit, 60–65% with "
        "ties and with the order swapped")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s38a — observability of AI answers
# ============================================================
def s38a(p):
    """AI in support: a suggester at the agent's elbow and a bot that
    answers on its own.

    OWNER-REVIEW 2026-10-01: "slide 38 is a completely unclear and unreadable
    example; let us do AI in support instead (assistants / bots and so on)
    and show where they are good and where they are not". The slide has been
    remade from end to end; the earlier observability of AI answers has been
    taken off — it is about controlling the model, whereas by that same
    review the section turns towards the USE OF AI IN SUPPORT.

    The card form is the same as on the other eleven practices of the deck.
    The numbers are given with a baseline: the suggester's effect both in
    percent and in resolutions per hour before the rollout (the rule
    "a baseline or a counterfactual for every measurable number").
    """
    sid = "s38a"
    s = head(p, "AI in support: a suggester at the agent's elbow and a bot "
                "that answers on its own", sid=sid)
    C = Cursor()

    what_is_it(s, C,
               "AI enters the work with tickets in two ways, and confusing "
               "them is expensive. A **suggester** offers the agent an "
               "answer; a human sends it, and the same human answers for "
               "what was said. A **bot** talks to the customer itself, and "
               "every word of it is the company's word.",
               size=11.2)

    def effect(sl, gx, gy, gw, gh):
        """Measuring the suggester's effect WITH A BASELINE: the "before the
        rollout" marker on the left, three bars of the gain on the right.
        The baseline is drawn rather than mentioned — otherwise there is
        nothing to measure "+15%" against."""
        text_box(sl, x=gx, y=gy, w=gw, h=0.24,
                 text="Suggester: measured on 5,172 support agents",
                 size=9.2, bold=True, color=DEEP, line_spacing=1.0)
        # the baseline marker
        ocean_box(sl, gx, gy + 0.28, gw, 0.34, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.2, radius_pt=6.0)
        text_runs(sl, gx + 0.12, gy + 0.28, gw - 0.24, 0.34, [
            {"text": "base before the rollout — ", "size": 8.8,
             "color": SLATE},
            {"text": "2.1 resolutions per hour", "size": 9.4, "bold": True,
             "color": DEEP},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        bars = [("all agents", "+15%", 0.50, MID),
                ("least experienced", "+30%", 1.00, GOLD),
                ("most experienced", "≈0", 0.06, SLATE)]
        by = gy + 0.74
        # the width of the bar plus the value label have to fit inside gw:
        # at barw_max = gw − 2.05 the label "+30%" ran past the right edge of
        # the box (caught by eye on a snapshot; the _check guard does not
        # measure diagrams).
        barw_max = gw - 2.35
        for lab, val, frac, col in bars:
            text_box(sl, x=gx, y=by, w=1.52, h=0.30, text=lab, size=8.6,
                     color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            w = max(0.10, barw_max * frac)
            filled_rect(sl, gx + 1.58, by + 0.05, w, 0.20, col, radius=True,
                        radius_adj=0.40)
            text_box(sl, x=gx + 1.58 + w + 0.07, y=by, w=0.70, h=0.30,
                     text=val, size=9.2, bold=True, color=col,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            by += 0.33
        tiny(sl, gx, by + 0.02, gw,
             "for the most experienced conversation quality is slightly "
             "lower: the suggestion offers them the average answer",
             size=8.2, h=0.32)
        ocean_box(sl, gx, by + 0.40, gw, 0.44, fill=GOLD_TINT, stroke=GOLD,
                  stroke_pt=1.4, radius_pt=6.0)
        text_box(sl, x=gx + 0.12, y=by + 0.40, w=gw - 0.24, h=0.44,
                 text="an agent with two months on the job and a suggester "
                      "works like an agent with six months without one",
                 size=8.8, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.04)

    mechanism(s, C, [
        "**Sort the ticket flow by the cost of an error.** Information that "
        "can be derived in full from your own knowledge base lives apart "
        "from a commitment the company pays for in money or answers for in "
        "law.",
        "**On the information flow, begin with a suggester.** It pays off "
        "where there is little experience, and it leaves the answer with a "
        "human.",
        "**Switch the bot on where the answer follows from a checkable "
        "source** — and show that source beside the answer.",
        "**Two safeguards are compulsory:** a guaranteed path to a live "
        "human, and a threshold at which the bot falls silent and calls an "
        "agent.",
    ], size=10.0, schema=effect, schema_w=4.30, schema_h=2.60)

    compare(s, C,
            ("WITHOUT AI — what support stands on and will go on standing on",
             "A knowledge base, answer templates, ticket routing, a mentor "
             "for the newcomer. Speed runs up against the agent's length of "
             "service: knowledge of rare cases takes months to build and "
             "leaves with whoever resigns.", MID),
            ("WITH AI — what it has added",
             "A real-time suggestion on top of the same knowledge base; a "
             "bot on the routine flow; a summary of a thread for whoever "
             "picks it up. **The knowledge base remains a precondition:** "
             "where it has a gap, AI fills it itself.", TEAL))

    C.edge(s,
           "A bot announces a rule that does not exist. **April 2025:** the "
           "Cursor support bot invented a “one login per user” limit; "
           "customers cancelled, the company apologised and refunded — no "
           "such policy existed.",
           size=9.8)

    src(s, X0, 7.04, 11.9,
        "The suggester measurement: Brynjolfsson, Li, Raymond, “Generative "
        "AI at Work”, Quarterly Journal of Economics, 2025 — 5,172 agents at "
        "a Fortune 500 company, staged rollout from November 2020 to May "
        "2021, base 2.1 resolutions per hour · The Cursor support bot: AI "
        "Incident Database, incident 1039 (April 2025)")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s38b — the failure drill
# ============================================================
def s38b(p):
    """The failure drill. OWNER-REVIEW 2026-10-01: the slide was accepted
    ("excellent"), the structure and the diagram of the four times are kept.
    Three pointed edits following the remark:

    1. The link between the fire alarm and an IT system is spelled out
       element by element right inside the "what it is" block — smoke,
       detector, siren, exit, evacuation time standard; before, the metaphor
       was named and then dropped.
    2. The role of AI is named INSIDE each step of the mechanism rather than
       pulled out into a separate aside.
    3. The subject of the drill is moved: we look at the use of AI inside
       the drill itself, while degradation of the AI component stays on s39,
       where it is taken apart.

    The contrastive "not X, but Y" format appeared eight times on this card
    — removed.
    """
    sid = "s38b"
    s = head(p, "The failure drill: is there anything here that would notice "
                "degradation", sid=sid)
    C = Cursor()

    what_is_it(s, C,
               "A fire drill tests the building and the people: the "
               "detector went off, the siren sounded, the exit was clear, "
               "everyone got out within the time standard. There is no "
               "fire; a plan plays its part. A support drill is built the "
               "same way: answer quality is spoiled deliberately and under "
               "control, to see whether detection fires.\n"
               "**Element of the drill → element of the system:** smoke → a "
               "substituted model prompt · detector → a threshold on a proxy "
               "metric · siren → paging the on-call engineer · exit → "
               "rolling the version back and a path to a human · evacuation "
               "time standard → four measured times.",
               size=10.0)

    def timeline(sl, gx, gy, gw, gh):
        """Four time marks, filled with the numbers of one drill that was
        actually run: empty fields read as "the slide was left
        unfinished"."""
        marks = [("noticed", "4"), ("a human arrived", "9"),
                 ("automation stopped it", "12"),
                 ("restored to how it was", "21")]
        bh = 0.32
        text_box(sl, x=gx + gw - 1.10, y=gy, w=1.10, h=0.20,
                 text="minutes from the start", size=7.8, italic=True,
                 color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.0)
        for i, (lab, val) in enumerate(marks):
            by = gy + 0.24 + i * (bh + 0.16)
            circle(sl, gx, by + 0.04, 0.26, MID)
            text_box(sl, x=gx, y=by + 0.04, w=0.26, h=0.26, text=str(i + 1),
                     size=8.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            text_box(sl, x=gx + 0.34, y=by, w=gw - 1.50, h=bh, text=lab,
                     size=9.0, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=1.04)
            ocean_box(sl, gx + gw - 1.10, by, 1.10, bh, fill=GOLD_TINT,
                      stroke=GOLD, stroke_pt=1.4, radius_pt=6.0)
            text_box(sl, x=gx + gw - 1.10, y=by, w=1.10, h=bh, text=val,
                     size=11, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            if i < 3:
                connector(sl, gx + 0.13, by + bh, gx + 0.13, by + bh + 0.16,
                          color=SLATE, width=1.6, arrow_end=True)
        tiny(sl, gx, gy + 0.24 + 4 * bh + 3 * 0.16 + 0.04, gw,
             "the numbers come from one drill that was run; at the next one "
             "they are filled in afresh", size=8.6, align=PP_ALIGN.CENTER,
             h=0.30)

    mechanism(s, C, [
        "One **class of failure** is chosen and a date is set. **AI:** "
        "proposes scenarios drawn from past postmortems; a human chooses.",
        "Quality is degraded **under control**: the model prompt is swapped "
        "for a weak one, guardrails are loosened. **AI:** generates a ticket "
        "flow to the scenario, so the on-call engineer sees the load.",
        "**Four times** are measured and written down as numbers — your own, "
        "from this drill.",
        "The postmortem. **AI:** assembles the timeline and hands over a "
        "draft; findings and procedure edits are signed off by a human.",
        "A drill that changed not a single procedure was too easy.",
    ], size=9.6, schema=timeline, schema_w=3.90, schema_h=2.34)

    compare(s, C,
            ("WITHOUT AI — the classic failure drill",
             "A service is killed, a resource taken away: you watch the "
             "system come back and the on-call engineer turn up. Scenario, "
             "timeline and postmortem are human work.", MID),
            ("WITH AI — what it is busy with inside the drill",
             "AI proposes scenarios from past postmortems, generates the "
             "ticket flow, assembles a timeline and hands over a draft. "
             "Tools 2026: incident.io, Rootly, PagerDuty.", TEAL))

    C.edge(s,
           "AI proposes variations on past failures: an unseen class it will "
           "not invent. A draft postmortem is plausible **even when the "
           "cause is wrong**. **A quarterly drill gives detection with a "
           "quarter-wide window.**",
           size=9.6)

    src(s, X0, 7.04, 11.9,
        "Assembling an incident timeline and a draft postmortem from the "
        "records — incident.io, Rootly, PagerDuty; the time saved on the "
        "postmortem is a vendor claim, with no independent measurement")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s45a — the structure of cost and revenue (TAKEN OUT OF THE CARD FORM,
# see #212)
# ============================================================
def s45a(p):
    """EDIT #212, owner remark 2: "slide 46: remake it out of this format
    into an ordinary presentation slide and show, from some research, the
    structure of costs and revenues broken down both by type (people,
    hardware, AI) and by feature/module, + ideally show how introducing one
    feature grows revenue and another grows cost and we take a decision, but
    with some caveat and an example of a loss-making feature you cannot give
    up".

    The slide is TAKEN OUT OF THE CARD FORM: it is the only one in this band
    assembled as an ordinary presentation slide, and so it calls neither
    head(), nor Cursor(), nor what_is_it / mechanism / compare / edge. The
    band has stopped being twelve cards of one form — eleven cards plus this
    slide. The previous content (the token arithmetic, routing a request to
    a cheap model, the 15x of a multi-agent scheme) stayed in §6.1a of the
    chapter; on the slides its only trace is the counter on the chart on
    s45.

    The left cut is measured (ICONIQ, around 305 executives, the second
    quarter of 2026). The right one is worked through on illustrative
    numbers, and the slide says so outright: there is no public study with a
    breakdown by feature, and illustrative numbers may not be passed off as
    a measurement. The fourth row of the table, in gold, is the one that
    cannot be closed; the caveat underneath explains it by the requirement
    of the EU AI Act."""
    sid = "s45a"
    free_slide(sid, "slide without bands")
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The structure of cost and revenue: by type it is "
                   "measured, by feature you do it yourself",
                size=19, w=12.25, h=0.62, y=0.13)

    # ── left: the breakdown by type, measured ──
    ocean_box(s, 0.55, 0.88, 5.15, 4.60, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_box(s, x=0.78, y=1.00, w=4.69, h=0.26,
             text="BY TYPE — WHAT HAS BEEN MEASURED", size=10.5, bold=True,
             color=MID, line_spacing=1.0)
    text_box(s, x=0.78, y=1.26, w=4.69, h=0.26,
             text="shares of product cost: before launch → at scale",
             size=9.6, italic=True, color=SLATE, line_spacing=1.0)

    SEG = [("people", MID, WHITE), ("model calls", GOLD, DEEP),
           ("hardware and cloud", TEAL, WHITE),
           ("data storage and processing", LIGHT, WHITE),
           ("everything else", SOFT_GREY, DEEP)]
    BW = 4.69

    def comp_bar(y, h, shares, num_size):
        """One stacked bar: the shares in colour, the number inside only
        where the segment is wider than 0.50", otherwise the label sits on
        top of its neighbour."""
        cx = 0.78
        for (_, fill, tc), sh in zip(SEG, shares):
            w = BW * sh / 100.0
            filled_rect(s, cx, y, w, h, fill)
            if w >= 0.50:
                text_box(s, x=cx, y=y, w=w, h=h, text=str(sh), size=num_size,
                         bold=True, color=tc, align=PP_ALIGN.CENTER,
                         anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            cx += w

    text_box(s, x=0.78, y=1.54, w=4.69, h=0.22,
             text="before the product launches", size=8.6, italic=True,
             color=SLATE, line_spacing=1.0)
    comp_bar(1.78, 0.36, [32, 20, 16, 6, 26], 9.0)
    text_box(s, x=0.78, y=2.18, w=4.69, h=0.24, text="at scale", size=8.8,
             bold=True, color=DEEP, line_spacing=1.0)
    comp_bar(2.44, 0.48, [26, 23, 17, 6, 28], 10.0)

    LEG = [("**people** — 32% → 26%", MID),
           ("**model calls** — 20% → 23%", GOLD),
           ("**hardware and cloud** — around 17%, unchanged", TEAL),
           ("**data storage and processing** — 6%", LIGHT),
           ("**everything else** — model training, compliance", SOFT_GREY)]
    _BAND[0] = "legend of the breakdown by type"
    for i, (txt, col) in enumerate(LEG):
        ly = 3.00 + i * 0.24
        filled_rect(s, 0.80, ly + 0.05, 0.15, 0.15, col, stroke=SLATE,
                    stroke_pt=0.6)
        md_box(s, 1.03, ly, 4.44, 0.24, txt, size=9.3, bold_color=DEEP,
               line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)

    src(s, 0.78, 4.24, 4.69,
        "ICONIQ Capital, State of AI 2026: around 305 executives of "
        "companies that build products with AI, a survey of the second "
        "quarter of 2026. The first four shares come from the report; the "
        "last one closes the sum to 100%",
        size=8.0, color=SLATE, h=0.40)
    md_box(s, 0.78, 4.70, 4.69, 0.72,
           "On the revenue side: model calls eat around **23% of revenue**. "
           "Gross margin on products with AI was **45%** in 2025, and "
           "**53%** is expected for 2026; on a classic software product it "
           "holds above 70%.",
           size=9.6, bold_color=DEEP, line_spacing=1.12)

    # ── right: the breakdown by feature and the mechanics of the decision ──
    ocean_box(s, 5.90, 0.88, 6.90, 4.60, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=6.13, y=1.00, w=6.44, h=0.26,
             text="BY FEATURE — AND HOW THE DECISION IS TAKEN", size=10.5,
             bold=True, color=TEAL, line_spacing=1.0)
    text_box(s, x=6.13, y=1.26, w=6.44, h=0.34,
             text="worked through on the illustrative numbers of one "
                  "catalogue: a breakdown like this is something few can "
                  "build",
             size=9.6, italic=True, color=SLATE, line_spacing=1.04)

    TW = [2.34, 1.40, 1.40, 1.18]

    def trow(y, h, cells, *, head=False, fill=SURFACE, stroke=LIGHT, pt=1.0,
             size=9.5):
        cx = 6.13
        for w, txt in zip(TW, cells):
            if head:
                filled_rect(s, cx, y, w, h, MID, radius=True, radius_adj=0.10)
                text_box(s, x=cx + 0.08, y=y, w=w - 0.16, h=h, text=txt,
                         size=10.0, bold=True, color=WHITE,
                         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                         line_spacing=1.0)
            else:
                filled_rect(s, cx, y, w, h, fill, stroke=stroke, stroke_pt=pt,
                            radius=True, radius_adj=0.08)
                md_box(s, cx + 0.10, y + 0.04, w - 0.20, h - 0.08, txt,
                       size=size, bold_color=DEEP, line_spacing=1.08,
                       anchor=MSO_ANCHOR.MIDDLE)
            cx += w + 0.04

    trow(1.64, 0.34, ["Feature", "Revenue", "Cost", "Decision"], head=True)
    TROWS = [
        (["**Suggestions in catalogue search**", "+8% to paid orders",
          "+₽0.9 per query", "we expand it"], SURFACE, LIGHT, 1.0),
        (["**An AI agent on the first line of support**", "0 directly",
          "−40% of the agent's time per ticket",
          "we keep it: it pays in savings"], SURFACE, TEAL, 1.0),
        (["**Review summaries on the product card**",
          "within the margin of error", "+₽1.4 per view", "we close it"],
         SURFACE, MID, 1.0),
        (["**A decision log and a way out to a human**", "0",
          "constant, grows with volume", "**cannot be closed**"],
         GOLD_TINT, GOLD, 1.8),
    ]
    for i, (cells, fill, stroke, pt) in enumerate(TROWS):
        trow(2.02 + i * 0.70, 0.66, cells, fill=fill, stroke=stroke, pt=pt)

    src(s, 6.13, 4.86, 6.44,
        "Every number in this breakdown stands against one baseline: the "
        "same catalogue without that feature, over the same month. A "
        "breakdown by feature is something few can build: 22% of finance "
        "leaders can connect AI spend to money, and 60% agree that they "
        "spend more on AI than they can justify — CloudZero, June 2026, 260 "
        "respondents, more than half of them chief financial officers",
        size=8.0, color=SLATE, h=0.52)

    gold_callout(
        s, 0.55, 5.60, 12.25, 1.14,
        "A caveat: a loss-making line cannot always be closed. A decision "
        "log and a way out to a human are required for a high-risk system "
        "by the EU AI Act: from 2 August 2026 events are recorded "
        "automatically, and the logs are kept for no less than six months. "
        "Revenue zero, cost constant, switching it off not allowed. The "
        "same class — a feature that loses money on its own line and holds "
        "revenue on somebody else's: the free tier, support, data export.",
        size=11.5, bold=True)
    refs_of_slide(s, sid)
    notes_with_sources(s, sid)
    return s


# ============================================================
# s45b — the financial criterion of a pilot
# ============================================================
def s45b(p):
    """One card. The mechanism is broken out into steps, and the filled-in
    sample entry stays as a labelled diagram on the right. The WITH AI AND
    WITHOUT block here, as on s24c, says it plainly: the apparatus is
    classical, AI changes only the rhythm."""
    sid = "s45b"
    s = head(p, "We write down the result at which the pilot gets closed — "
                "before we switch it on", sid=sid, size=18)
    C = Cursor()

    what_is_it(s, C,
               "One sentence with numbers in it, written down in advance, by "
               "which a few weeks later you can see whether to carry on or "
               "to close. The nearest familiar analogue is **the acceptance "
               "criterion in a statement of work**, translated out of "
               "functionality and into money. A number named after the "
               "result explains the result and tests nothing any more.",
               size=11.5)

    def sample(sl, gx, gy, gw, gh):
        ocean_box(sl, gx, gy + 0.04, gw, 1.34, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.2, radius_pt=8.0)
        text_runs(sl, gx + 0.14, gy + 0.10, gw - 0.28, 1.22, [
            {"text": "“Having the model handle tickets will bring the cost "
                     "of one ticket down ", "size": 10.0, "color": DEEP},
            {"text": "from ₽42 to ₽15", "size": 10.0, "bold": True,
             "color": MID},
            {"text": ", customer satisfaction will not drop ", "size": 10.0,
             "color": DEEP},
            {"text": "below 4.2 out of 5", "size": 10.0, "bold": True,
             "color": TEAL},
            {"text": ", and the share of tickets handed to a human will not "
                     "exceed ", "size": 10.0, "color": DEEP},
            {"text": "20%", "size": 10.0, "bold": True, "color": TEAL},
            {"text": ". We test on ", "size": 10.0, "color": DEEP},
            {"text": "5,000 tickets over 6 weeks", "size": 10.0,
             "bold": True, "color": LIGHT},
            {"text": ". Watched by ", "size": 10.0, "color": DEEP},
            {"text": "the head of support, once a week", "size": 10.0,
             "bold": True, "color": GOLD},
            {"text": ".”", "size": 10.0, "color": DEEP},
        ], line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
        tiny(sl, gx, gy + 1.42, gw,
             "a filled-in sample entry: one part in it for each step on the "
             "left", size=8.6, align=PP_ALIGN.CENTER, h=0.34)

    mechanism(s, C, [
        "**What we improve** — from what value to what value.",
        "**What must not get worse while we do it** — one or two guardrail "
        "quantities.",
        "**On what volume and over what period** we test.",
        "**Who looks, and how often.** The entry is made before switch-on, "
        "with a date and a name on it: otherwise there is nothing by which "
        "to check the order of events in time.",
    ], size=10.0, schema=sample, schema_w=5.10, schema_h=1.84)

    compare(s, C,
            ("WITHOUT AI — apparatus half a century old",
             "A business case with a payback threshold and a decision at a "
             "gate. **There is nothing to invent afresh**, you take what is "
             "already there.", MID),
            ("WITH AI — only the rhythm changes",
             "Cost moves daily, a quarterly rhythm cannot keep up, and that "
             "is why they look weekly. Meanwhile companies measure activity "
             "instead of money — hence the gap: almost everyone invests, "
             "**6%** see a measurable return.", TEAL))

    C.edge(s,
           "**The starting value is measured on your own process.** A "
           "vendor's promise will not do: somebody else's number describes "
           "somebody else's process. **If “we close it” is not among the "
           "outcomes, this is not a criterion:** a threshold you cannot fail "
           "to clear grants no permission. And **numbers that appeared after "
           "switch-on explain the result,** which is why the date and the "
           "name are checked before the numbers.",
           size=10.0)

    src(s, X0, 7.04, 11.5,
        "Companies measure activity instead of money in the profit and loss "
        "statement; a measurable return is seen by 6% — Boston Consulting "
        "Group, 2026")
    notes_with_sources(s, sid)
    return s


BUILDERS = [s11a, s11b, s17a, s24a, s24b, s24c, s30a, s31a, s38a, s38b,
            s45a, s45b]
