"""Lecture 5 (EN) — Band 1 (Section 0 s01-s06 + Section 1 Discovery s07-s13a).

EN twin of slides_band1.py: same layout/geometry/palette, English visible
strings + speaker notes sourced from slides-en/sNN*.md. Each sNN(p) builds
one slide. Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.

NO timing / NO methodology / NO superlatives / NO photo-attribution labels
on the visible layer (owner ENFORCED rules) — source lives only in
notes_with_sources() -> speaker notes, never on the slide body.
"""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes,
    notes_with_sources, refs_of_slide, roadmap_bar, build_section_divider,
    eli5_overview, meme_in_box, photo_in_box,
    NAV, DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s01 - hook paradox (hero >=40% area, icon-metaphor)
# ============================================================
def s01(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Assembly is nearly free. So why does almost no one capture the value?",
        size=21, w=12.2, h=0.80, y=0.30)

    lx, lw = 0.55, 4.35
    fact_h = 1.62
    ocean_box(s, lx, 1.30, lw, fact_h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    icon(s, "clock", lx + 0.24, 1.30 + 0.20, 0.80, "mid")
    text_box(s, x=lx + 1.18, y=1.30 + 0.16, w=lw - 1.40, h=0.75,
             text="Weeks of work → hours [1]", size=14, bold=True, color=MID,
             line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.30 + fact_h - 0.42, w=lw - 1.40, h=0.34,
             text="Anthropic internal experience", size=10.5, italic=True,
             color=SLATE)
    ocean_box(s, lx, 1.30 + fact_h + 0.16, lw, fact_h, fill=SURFACE,
              stroke=LIGHT, stroke_pt=1.5)
    icon(s, "funnel", lx + 0.24, 1.30 + fact_h + 0.16 + 0.20, 0.80, "teal")
    text_box(s, x=lx + 1.18, y=1.30 + fact_h + 0.16 + 0.16, w=lw - 1.40, h=0.75,
             text="~95% of pilots — zero return [2]", size=14, bold=True,
             color=TEAL, line_spacing=1.02, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 1.18, y=1.30 + 2 * fact_h + 0.16 - 0.42, w=lw - 1.40,
             h=0.34, text="MIT, summer 2025", size=10.5, italic=True, color=SLATE)
    gold_callout(
        s, lx, 1.30 + 2 * fact_h + 0.16 + 0.18, lw, 2.14,
        "Both facts are true at the same time: assembly became nearly free, "
        "but turning assembly into value did not. Hold the question — "
        "we'll come back to it at the end of the lecture.",
        size=13, bold=True)
    # right: real meme (Spider-Man Pointing at Spider-Man) — two
    # simultaneously-true facts pointing at each other, the unambiguous hero
    # (>=40% slide area)
    from _helpers_en import meme_in_box
    meme_in_box(s, "s01-spiderman-pointing.jpg", 5.15, 1.30, 7.65, 5.30,
                pad=0.18)
    refs_of_slide(s, "s01")
    notes_with_sources(s, "s01")
    return s


# ============================================================
# s02 - cover + roadmap (hero >=40% area: circular loop icon)
# ============================================================
def s02(p):
    s = blank(p)
    set_slide_bg(s, SURFACE)
    # decorative circular loop of 6 nodes, upper-left (hero, evergreen)
    cx, cy, r = 3.15, 2.85, 1.55
    import math
    nodes = ["Discovery", "Design", "Build\n& Launch", "Measure",
             "Support", "Governance"]
    centers = []
    for i, label in enumerate(nodes):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        nx = cx + r * math.cos(ang)
        ny = cy - r * math.sin(ang)
        centers.append((nx, ny))
    # connecting arcs first (behind nodes) so the ring reads as ONE loop
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        connector(s, x1, y1, x2, y2, color=LIGHT, width=2.0)
    for i, (label, (nx, ny)) in enumerate(zip(nodes, centers)):
        circle(s, nx - 0.30, ny - 0.30, 0.60, MID if i else GOLD,
               stroke=WHITE, stroke_pt=1.5)
        text_box(s, x=nx - 0.85, y=ny + 0.32, w=1.70, h=0.42, text=label,
                 size=9, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.9)
    icon(s, "lightbulb", cx - 0.32, cy - 0.32, 0.64, "gold")

    # real meme (One Does Not Simply) — cover meme, bottom-left, framed
    from _helpers_en import meme_in_box
    meme_in_box(s, "s02-one-does-not-simply.jpg", 0.75, 4.85, 5.0, 1.55,
                pad=0.10)

    # title block, right
    text_box(s, x=6.55, y=1.55, w=6.35, h=0.5, text="LECTURE 5",
             size=20, bold=True, color=TEAL)
    text_box(s, x=6.55, y=2.10, w=6.40, h=2.0,
             text="AI Product: the full lifecycle — from intent to operation",
             size=30, bold=True, color=DEEP, line_spacing=1.05)
    text_box(s, x=6.58, y=4.35, w=6.30, h=0.6,
             text="Course \"Deliberate Use of AI\" · 3rd-year engineering students",
             size=14, italic=True, color=LIGHT)
    gold_callout(
        s, 6.55, 5.05, 6.35, 0.78,
        "Six sections — six arrows of one loop: code (Lecture 4) is one "
        "cheap step inside it.",
        size=13, bold=True)
    roadmap_bar(s, 0, y=6.55)
    notes_with_sources(s, "s02")
    return s


# ============================================================
# s03 - lecture map as loop (schema_cycle)
# ============================================================
def s03(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The lecture is a loop, not a list of six topics",
                size=25, w=12.0, h=0.85)

    import math
    cx, cy, r = 4.15, 4.05, 2.05
    steps = [
        ("search", "1. Discovery", "where the hypothesis comes from"),
        ("pencil", "2. Design", "hypothesis → artifact"),
        ("hammer", "3. Build & Launch", "artifact → product"),
        ("ruler", "4. Measure", "did it work"),
        ("headphones", "5. Support", "lives 24/7"),
        ("scale", "6. Governance", "where to invest"),
    ]
    centers = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        centers.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        pad = 0.62
        sx1, sy1 = x1 + ux * pad, y1 + uy * pad
        sx2, sy2 = x2 - ux * pad, y2 - uy * pad
        is_return = (i == 5)  # Governance(5) -> Discovery(0)
        connector(s, sx1, sy1, sx2, sy2,
                  color=(GOLD if is_return else LIGHT),
                  width=(2.6 if is_return else 2.0),
                  arrow_end=True)
    for i, (ic, name, desc) in enumerate(steps):
        nx, ny = centers[i]
        ocean_box(s, nx - 0.70, ny - 0.48, 1.40, 0.96, fill=SURFACE,
                  stroke=MID, stroke_pt=1.3)
        icon(s, ic, nx - 0.24, ny - 0.42, 0.48, "mid")
        text_box(s, x=nx - 0.68, y=ny + 0.06, w=1.36, h=0.40, text=name,
                 size=7.8, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.88)
    text_box(s, x=cx - 0.85, y=cy - 0.30, w=1.7, h=0.6, text="Intent",
             size=12, bold=True, color=GOLD, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)

    # right column: numbered list + return arrow note
    rx, rw = 7.15, 5.65
    for i, (ic, name, desc) in enumerate(steps):
        y = 1.55 + i * 0.62
        text_box(s, x=rx, y=y, w=rw, h=0.56,
                 text=f"{name} — {desc}", size=13, bold=True, color=DEEP,
                 line_spacing=1.0)
    gold_callout(
        s, 7.15, 5.55, 5.65, 1.00,
        "The return arrow: governance feeds discovery again — a closed "
        "loop, not a one-time linear process.",
        size=12.5, bold=True)
    notes_with_sources(s, "s03")
    return s


# ============================================================
# s04 - REBUILT (issue #212): "why a product needs the loop, and what
# happens without one". The previous slide (the bridge from Lecture 4 plus
# the central question) was rejected by the owner: "the value is not clear,
# beyond saying that we are using what was in Lecture 4". The content is
# taken from chapter.md §0.3a — a section that was not on the slides at all.
# The bridge from Lecture 4 is compressed into a single subordinate line
# under the title; the central question moved to s06.
# ============================================================
def s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Why a product needs the loop: without one, the error is "
                   "found too late",
                size=22, w=12.25, h=0.66, y=0.24)
    # EDIT #212 (student-roast 2026-09-30, edit 4 — overload): the bridge
    # from Lecture 4 ("the code loop sits inside the build phase") is off the
    # visible layer and has moved into the notes. It was a subordinate line,
    # yet it occupied the first position after the title — students read it
    # before they read the five questions.

    # ── left column: five questions ↔ phases (ties to the lecture map, s03) ──
    lx, lw = 0.55, 6.10
    text_box(s, x=lx, y=1.02, w=lw, h=0.34,
             text="Five questions a product answers by observation rather "
                  "than by opinion",
             size=11.5, bold=True, color=TEAL, line_spacing=1.02)
    questions = [
        ("Does anyone need this at all", "phase 1 · discovery"),
        ("Can a person actually use it, and will someone nobody thought "
         "about be harmed", "phase 2 · design"),
        ("Can we build it and release it safely",
         "phase 3 · build and launch"),
        ("Will it be chosen firmly enough that people pay for it",
         "phases 4 and 6 · measurement, governance"),
        ("Do those answers still hold a quarter later", "phase 5 · support"),
    ]
    for i, (q, phase) in enumerate(questions):
        y = 1.46 + i * 0.64
        ocean_box(s, lx, y, lw, 0.60, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        circle(s, lx + 0.16, y + 0.15, 0.30, MID)
        text_box(s, x=lx + 0.16, y=y + 0.17, w=0.30, h=0.28, text=str(i + 1),
                 size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        text_box(s, x=lx + 0.58, y=y + 0.02, w=lw - 0.76, h=0.38, text=q,
                 size=11, bold=True, color=DEEP, line_spacing=0.96,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=lx + 0.58, y=y + 0.38, w=lw - 0.76, h=0.20, text=phase,
                 size=9.5, italic=True, color=TEAL)
    # A name on a slide has to carry a role (student-roast 2026-09-30, edit
    # 1): "Marty Cagan" means nothing to a third-year student, so the
    # argument "the product risks after Cagan" read as a pointer to a
    # stranger.
    text_box(s, x=lx + 0.04, y=4.74, w=lw - 0.08, h=0.84,
             text="The first four are the product risks named by Marty "
                  "Cagan (product leader, founder of the Silicon Valley "
                  "Product Group, author of \"Inspired\"); the fifth only "
                  "opens up after launch. Each has a phase of its own: the "
                  "loop is the minimum set of places where these questions "
                  "get answered.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.08)

    # ── right column: the mechanism of having no loop ──
    # EDIT #212 (student-roast, edit 4): there used to be three text frames
    # in a row plus a large gold panel — the right column as a whole could
    # not be read in the time available. Two frames now: "the cost of late
    # discovery" is folded into a single line inside the first one (Boehm's
    # figure kept together with his role), and the repeat of the 60/20/5
    # funnel is out of the gold panel — that figure was already on s01 and
    # gets a slide of its own in Section 6.
    rx, rw = 6.95, 5.85

    def framed(y, h, head, body, *, stroke=MID, body_size=11, head_color=TEAL):
        ocean_box(s, rx, y, rw, h, fill=SURFACE, stroke=stroke, stroke_pt=1.4)
        text_box(s, x=rx + 0.22, y=y + 0.10, w=rw - 0.44, h=0.28, text=head,
                 size=12.5, bold=True, color=head_color)
        # anchor TOP, not MIDDLE: with MIDDLE, text that does not fit the
        # frame rides UP and covers the frame's own heading — which is
        # exactly what happened on the first iteration of this edit.
        text_box(s, x=rx + 0.22, y=y + 0.44, w=rw - 0.44, h=h - 0.56,
                 text=body, size=body_size, color=DEEP, line_spacing=1.14)

    framed(1.02, 2.58, "When there is no loop",
           "The questions do not disappear — optimistic assumptions take "
           "their place.\n"
           "The error does not disappear either; only the moment of finding "
           "it moves — to after the build has been paid for and the release "
           "has happened, where rolling back costs more than the error "
           "itself.\n"
           "From requirements to release, the cost of a fix spreads out up "
           "to a hundredfold on large projects and fourfold on small ones "
           "(Barry Boehm, a researcher in the economics of software "
           "development, 1981).")
    framed(3.70, 2.10, "From inside the team it does not look like failure",
           "Built it, nobody uses it · got to a pilot and stalled · it works "
           "and it is not chosen · rolled it out, and a quarter later people "
           "stopped opening it.\n"
           "In all four cases the build itself went through successfully — "
           "which is why from inside the team it reads as success; an error "
           "sitting inside an unchecked hypothesis is not visible to anyone.",
           stroke=TEAL)

    gold_callout(
        s, 0.55, 5.94, 12.25, 0.88,
        "The expense of building worked as an involuntary barrier: while "
        "making the thing cost weeks, that cost alone forced teams to think "
        "in advance. AI is exactly what zeroed it out — and teams that never "
        "had an explicit loop now have nothing left holding them back from "
        "skipping these questions.",
        size=12.5, bold=True)
    notes_with_sources(s, "s04")
    return s


# ============================================================
# s05 - KEYSTONE: loop, 3 independent sources (PDCA/OODA/BML)
# ============================================================
# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: removed by the owner — a repeat of the loop already introduced; its argument was condensed into one line on s06 (issue #212).
def s05(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Three people from different fields drew the same blueprint",
                size=23, w=12.2, h=0.85)

    domains = [
        ("bar-chart-3", "Deming · statistical quality", "PDCA",
         "plan → do → check → act"),
        ("plane", "Boyd · air combat", "OODA",
         "observe → orient → decide → act"),
        ("rocket", "Ries · startups", "BML",
         "build → measure → learn"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, who, tag, seq) in enumerate(domains):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 2.05)
        icon(s, ic, x + 0.24, y0 + 0.20, 0.56, "mid")
        text_box(s, x=x + 0.94, y=y0 + 0.22, w=cw - 1.15, h=0.55, text=who,
                 size=11.5, bold=True, color=MID, line_spacing=1.0)
        chip(s, x + 0.24, y0 + 0.86, 1.15, 0.36, tag, fill=GOLD, color=DEEP,
             size=13)
        text_box(s, x=x + 0.24, y=y0 + 1.32, w=cw - 0.48, h=0.66, text=seq,
                 size=10.5, color=DEEP, line_spacing=1.08)

    # central shared loop symbol below
    cx = 6.67
    circle(s, cx - 0.55, 3.95, 1.10, GOLD_TINT, stroke=GOLD, stroke_pt=2.2)
    icon(s, "repeat", cx - 0.35, 4.15, 0.70, "gold")
    for i in range(3):
        x = x0 + i * (cw + gap) + cw / 2
        connector(s, x, y0 + 2.05, cx, 3.95, color=LIGHT, width=1.4,
                  dash="dash")

    gold_callout(
        s, 0.55, 5.35, 12.25, 0.85,
        "Without coordinating — the same blueprint: the feedback loop as a "
        "structural property of any system that learns under uncertainty.",
        size=13.5, bold=True)
    notes_with_sources(s, "s05")
    return s


# ============================================================
# s06 - KEYSTONE-2: cost/trust asymmetry (axis slide)
# ============================================================
def s06(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "AI changes the cost and trust of every arrow of the loop — but not equally",
                size=21, w=12.3, h=0.85)

    rows = [
        ("hammer", "Build", "cost nearly collapsed to zero", GOLD, "gold"),
        ("ruler", "Measure / Learn", "cost about the same, trust fell",
         LIGHT, "light"),
        ("search", "Observe / Orient", "faster, but more exposed to attack",
         TEAL, "teal"),
    ]
    y0 = 1.55
    for i, (ic, name, desc, col, av) in enumerate(rows):
        y = y0 + i * 1.05
        ocean_box(s, 0.55, y, 12.25, 0.90, fill=SURFACE, stroke=col,
                  stroke_pt=1.6)
        icon(s, ic, 0.80, y + 0.20, 0.5, av)
        text_box(s, x=1.50, y=y + 0.14, w=3.5, h=0.6, text=name, size=15,
                 bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=5.15, y=y + 0.14, w=7.4, h=0.6, text=desc, size=14,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 4.85, 12.25, 0.95,
        "A meta-pattern repeating in each of the 6 sections: every arrow "
        "has a classical discipline — AI doesn't cancel it, it changes its "
        "cost and the degree of verification it requires.",
        size=13.5, bold=True)

    filled_rect(s, 0.55, 5.95, 12.25, 0.75, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.08)
    text_box(s, x=0.85, y=6.08, w=11.65, h=0.55,
             text="Think about it: on which arrow of your latest task did "
                  "speed outrun your actual trust in the result?",
             size=12.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    notes_with_sources(s, "s06")
    return s


# ============================================================
# s07 - section divider S1 Discovery
# ============================================================
def s07(p):
    return build_section_divider(
        p, here_idx=1,
        subtitle="Discovery — intent and hypothesis",
        bridge="Where does a hypothesis about what to build even come from. "
               "Most people have the informal experience of \"ask your "
               "friends\" — and almost no one has met the formal "
               "discipline that explains why that experience "
               "systematically lies.",
        sid="s07", tag="2 base cases · 3 failures",
        meme_name="s07-distracted-boyfriend.jpg")


# ============================================================
# s07b - ELI5 overview "Discovery in plain terms"
# ============================================================
# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
def s07b(p):
    return eli5_overview(
        p, "s07b", title="Discovery in plain terms", icon_name="search",
        cards=[
            ("What it is",
             "The phase where you look not for a solution but for a "
             "problem: who has the pain, how bad it is, and whether the "
             "person is willing to pay for a fix in time, reputation, or "
             "money."),
            ("Why it matters",
             "You can build anything; only what solves a real pain for a "
             "real person has value. \"I'd use something like that\" is "
             "not a fact."),
            ("Mental model",
             "There are no facts inside the building — facts are outside. "
             "Write down a hypothesis, go out to people, check it. AI "
             "speeds up the gathering, but doesn't replace the "
             "conversation with a real person."),
        ])


# ============================================================
# s08 - BASE: Customer Development (4-step flow)
# ============================================================
def s08(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "\"There are no facts inside the building\" — 4 steps, each ending in a decision",
                size=22, w=12.2, h=0.85)

    steps = [
        ("Discovery", "discovery"), ("Validation", "validation"),
        ("Demand creation", "creation"), ("Scale", "building"),
    ]
    cw, gap = 2.72, 0.28
    x0 = 0.55
    y0 = 1.85
    for i, (name, gloss) in enumerate(steps):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
        text_box(s, x=x + 0.10, y=y0 + 0.12, w=cw - 0.20, h=0.28,
                 text=f"{i+1}", size=14, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.06, y=y0 + 0.42, w=cw - 0.12, h=0.34, text=name,
                 size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.74, w=cw - 0.20, h=0.26, text=gloss,
                 size=9.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        icon(s, "diamond", x + cw / 2 - 0.16, y0 + 1.02, 0.32, "gold")
        if i < 3:
            right_arrow(s, x + cw + 0.02, y0 + 0.55, gap - 0.04, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=y0 + 1.45, w=12.25, h=0.35,
             text="Steve Blank — the Customer Development methodology [1]",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    # falsifiable-hypothesis card
    ocean_box(s, 1.55, 3.90, 10.25, 1.35, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    icon(s, "route", 1.80, 4.10, 0.5, "gold")
    text_runs(s, 2.45, 4.08, 9.10, 1.05, [
        {"text": "Falsifiable hypothesis", "size": 14, "bold": True,
         "color": DEEP},
        {"text": "we believe X → we'll test it via Y → by date Z we'll have a yes/no answer",
         "size": 13, "color": DEEP, "newpara": True, "space_before": 6},
    ])

    gold_callout(
        s, 0.55, 5.55, 12.25, 0.85,
        "BML is the engine; Customer Development is the map of the terrain "
        "the engine drives on. First understand what you're testing and "
        "with whom — only then how fast to spin the loop.",
        size=13, bold=True)
    refs_of_slide(s, "s08")
    notes_with_sources(s, "s08")
    return s


# ============================================================
# s09 - BASE-2: The Mom Test (3 rules + contrast)
# ============================================================
# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: superseded base — the Mom Test is folded into s08 (issue #212).
def s09(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Even your mother will lie to you — if the question is built wrong [1]",
                size=23, w=12.2, h=0.85)

    rules = [
        ("message-square-x", "About their life, not your idea",
         "don't pitch the idea and don't ask for a verdict"),
        ("history", "About the past, not the future",
         "hypothetical questions invite dishonest optimism"),
        ("handshake", "A commitment, not a compliment",
         "legitimate signals: time, reputation, money"),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, head, body) in enumerate(rules):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.85)
        icon(s, ic, x + 0.24, y0 + 0.18, 0.5, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.78, w=cw - 0.48, h=0.50, text=head,
                 size=13, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.30, w=cw - 0.48, h=0.50, text=body,
                 size=10.5, italic=True, color=SLATE, line_spacing=1.05)

    # contrast: bad vs good question
    by = 3.70
    filled_rect(s, 0.55, by, 5.95, 1.35, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.07)
    text_box(s, x=0.80, y=by + 0.15, w=5.45, h=0.35, text="Bad",
             size=12.5, bold=True, color=SLATE)
    text_box(s, x=0.80, y=by + 0.52, w=5.45, h=0.75,
             text="\"Would you pay $20 a month for this?\"", size=13.5, italic=True,
             color=SLATE, line_spacing=1.1)
    filled_rect(s, 6.75, by, 6.05, 1.35, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=7.00, y=by + 0.15, w=5.55, h=0.35, text="Good",
             size=12.5, bold=True, color=TEAL)
    text_box(s, x=7.00, y=by + 0.52, w=5.55, h=0.75,
             text="\"How much do you pay today for the closest thing to this?\"",
             size=13.5, bold=True, color=DEEP, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.35, 12.25, 0.85,
        "Qualitative answers \"why\" on a small sample and generates "
        "hypotheses; quantitative answers \"how much\" at scale and tests "
        "a hypothesis that already exists — not a hierarchy, a division "
        "of labor.",
        size=12.5, bold=True)
    refs_of_slide(s, "s09")
    notes_with_sources(s, "s09")
    return s


# ============================================================
# s10 - AI: discovery tools 2025-26
# ============================================================
def s10(p):
    """EN twin of the rewritten RU s10 (FIX #212, owner remarks R6/R7):
    the stale time-saving estimates and tool list are replaced by 2026
    practice and shown as a "without AI / with AI" comparison per step of
    the phase. AI personas no longer appear out of nowhere: they have a
    named place on the scale of who is on the other end of the
    conversation. The golden set is gone from here — it gets its own slide
    in Section 3 (s24b); here it was an opaque forward reference."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "What AI changed in research by 2026 — "
                   "and what it did not",
                size=22, w=12.25, h=0.58, y=0.13)

    # ── Step-by-step comparison table ─────────────────────────────────
    col_x = [0.55, 3.30, 8.00]
    col_w = [2.60, 4.55, 4.80]
    for x, w, t in zip(col_x, col_w,
                       ["STEP OF THE PHASE", "WITHOUT AI", "WITH AI — 2026"]):
        filled_rect(s, x, 0.82, w, 0.32, MID, radius=True, radius_adj=0.12)
        text_box(s, x=x + 0.08, y=0.82, w=w - 0.16, h=0.32, text=t,
                 size=9.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)

    rows = [
        ("file-search", "Desk research",
         "what is already known about the market and the pain",
         "An analyst reads reports, papers and forums — days of work",
         "Deep research mode plans the search itself, reads hundreds of "
         "sources and returns a report with links in 2–30 minutes. Every "
         "major assistant has it, free tiers included, with a cap"),
        ("headphones", "The conversation", "",
         "The researcher runs each interview in person; eight of them take "
         "weeks of calendar",
         "The model asks, a live human answers — many times more "
         "conversations in the same span"),
        ("layout-list", "Interview synthesis", "",
         "Transcription by hand, themes picked out by eye",
         "Transcription is now a free add-on to any call; tools "
         "continuously re-cluster themes across the whole accumulated "
         "corpus, not one call"),
    ]
    ry = 1.22
    for ic, name, gloss, was, now in rows:
        rh = 0.78
        ocean_box(s, col_x[0], ry, col_w[0], rh, fill=SURFACE, stroke=LIGHT,
                  stroke_pt=1.3)
        icon(s, ic, col_x[0] + 0.16, ry + 0.10, 0.32, "mid")
        text_box(s, x=col_x[0] + 0.54, y=ry + 0.08, w=col_w[0] - 0.66,
                 h=0.34, text=name, size=11, bold=True, color=MID,
                 line_spacing=1.04)
        if gloss:
            text_box(s, x=col_x[0] + 0.14, y=ry + 0.42, w=col_w[0] - 0.28,
                     h=0.32, text=gloss, size=8.5, italic=True, color=SLATE,
                     line_spacing=1.04)
        ocean_box(s, col_x[1], ry, col_w[1], rh, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.2)
        text_box(s, x=col_x[1] + 0.16, y=ry, w=col_w[1] - 0.32, h=rh,
                 text=was, size=10, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.14)
        ocean_box(s, col_x[2], ry, col_w[2], rh, fill=TEAL_TINT, stroke=TEAL,
                  stroke_pt=1.4)
        text_box(s, x=col_x[2] + 0.16, y=ry, w=col_w[2] - 0.32, h=rh,
                 text=now, size=10, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.14)
        ry += rh + 0.08

    # ── The scale: who is on the other end of the conversation ────────
    text_box(s, x=0.55, y=3.80, w=12.25, h=0.30,
             text="Who is on the other end of the conversation", size=12.5,
             bold=True, color=MID)
    lad = [
        ("human ↔ human", "the classic interview", MID, SURFACE),
        ("human ↔ model", "the machine asks, a live human answers",
         TEAL, TEAL_TINT),
        ("model ↔ model",
         "an AI persona: a machine answers too — no live human in the "
         "chain at all", GOLD, GOLD_TINT),
    ]
    lw_ = 3.97
    for i, (t1, t2, col, fill) in enumerate(lad):
        x = 0.55 + i * (lw_ + 0.17)
        ocean_box(s, x, 4.14, lw_, 0.86, fill=fill, stroke=col, stroke_pt=1.7)
        text_box(s, x=x + 0.12, y=4.20, w=lw_ - 0.24, h=0.28, text=t1,
                 size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=1.02)
        text_box(s, x=x + 0.12, y=4.50, w=lw_ - 0.24, h=0.46, text=t2,
                 size=9.5, color=SLATE, align=PP_ALIGN.CENTER,
                 line_spacing=1.08)
    text_runs(s, 0.55, 5.08, 12.25, 0.30, [
        {"text": "Survey of 150 researchers, May 2026:   ", "size": 10.5,
         "italic": True, "color": SLATE},
        {"text": "81%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " regularly use AI in their work   ·   ", "size": 10.5,
         "color": DEEP},
        {"text": "8%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " — as the answering participant   ·   ", "size": 10.5,
         "color": DEEP},
        {"text": "28%", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " reject it outright", "size": 10.5, "color": DEEP},
    ], align=PP_ALIGN.CENTER, line_spacing=1.05)

    # ── What did not change: the boundary of desk research ────────────
    # FIX #212 (student-roast 2026-09-30, fix 4): the callout carried six
    # numbers and a whole chain of reasoning — the student took away only
    # "links are sometimes made up" and never followed the arithmetic. One
    # chain is left (53,090 → 3–13% → 78%) and one case; the share of links
    # that do not open and the caveat about independence moved to the notes.
    gold_callout(
        s, 0.55, 5.62, 12.25, 1.06,
        "A link in a report is not evidence until someone opens it. "
        "Measured on 53,090 links from the reports of ten models: 3–13% "
        "are fabricated — those sources never existed. At the lowest "
        "rate, 3%, a report with 50 links holds at least one fabricated "
        "link with probability 78%. Deloitte handed exactly such a report "
        "to the Australian government for A$440,000.",
        size=12.5, bold=True)
    refs_of_slide(s, "s10")
    notes_with_sources(s, "s10")
    return s


# ============================================================
# s11 - AI LIMITS: synthetic sycophancy, live-interview criteria
# ============================================================
def s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A synthetic interviewee structurally cannot produce disagreement",
                size=22, w=12.2, h=0.85)

    lx, lw = 0.55, 4.30
    ocean_box(s, lx, 1.55, lw, 3.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    icon(s, "smile", lx + lw / 2 - 0.55, 1.90, 1.10, "light")
    text_box(s, x=lx + 0.25, y=3.15, w=lw - 0.50, h=1.55,
             text="Mirror of agreement: a synthetic interviewee structurally "
                  "cannot reflect disagreement — it has no real past that "
                  "could contradict the way the question is phrased.",
             size=12.5, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=1.18)

    rx, rw = 5.15, 7.65
    crit = [
        "The cost of a \"continue/stop\" mistake is high",
        "You need a real past, not a plausible one",
        "You need validation by commitment, not by opinion",
    ]
    text_box(s, x=rx, y=1.55, w=rw, h=0.40,
             text="When a live interview is strictly better than AI synthesis",
             size=14, bold=True, color=MID)
    for i, c in enumerate(crit):
        y = 2.10 + i * 0.85
        ocean_box(s, rx, y, rw, 0.70, fill=SURFACE, stroke=MID, stroke_pt=1.3)
        text_box(s, x=rx + 0.65, y=y, w=rw - 0.85, h=0.70, text=f"{i+1}. {c}",
                 size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "shield-alert", rx + 0.14, y + 0.15, 0.42, "mid")

    gold_callout(
        s, 0.55, 5.10, 12.25, 0.95,
        "AI summaries lose 20-40% of interview detail (Torres) [1] when "
        "the \"individually first\" step is skipped — a failure traceable "
        "to a specific step, not a vague \"AI is sometimes wrong.\"",
        size=13, bold=True)
    refs_of_slide(s, "s11")
    notes_with_sources(s, "s11")
    return s


# ============================================================
# s12 - FAILURE on-point #1: synthetic users (NN/g)
# ============================================================
def s12(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The same task: real people — 3 of 7, the synthetic panel — 7 of 7 [1]",
        size=20, w=12.2, h=0.85)

    # LEFT: real meme (Trade Offer) — the false 7/7 "offer" vs the 3/7 that
    # actually decides
    from _helpers_en import meme_in_box
    meme_in_box(s, "s12-trade-offer.jpg", 0.55, 1.55, 4.55, 3.15, pad=0.14)

    # RIGHT: split comparison 3/7 vs 7/7
    rx, rw = 5.35, 7.45
    ocean_box(s, rx, 1.55, rw, 1.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=rx + 0.24, y=1.63, w=3.0, h=0.36,
             text="Real people", size=12.5, bold=True, color=MID)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        ok = i < 3
        icon(s, "check-check" if ok else "x", cxx, 2.02, 0.36,
             "mid" if ok else "light")
    text_box(s, x=rx + 3.35, y=1.75, w=rw - 3.6, h=0.7,
             text="3 of 7 — \"far-fetched and useless\"", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)

    ocean_box(s, rx, 2.75, rw, 1.05, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.8)
    text_box(s, x=rx + 0.24, y=2.83, w=3.0, h=0.36,
             text="Synth panel", size=12.5, bold=True, color=DEEP)
    for i in range(7):
        cxx = rx + 0.28 + i * 0.42
        icon(s, "check-check", cxx, 3.22, 0.36, "gold")
    text_box(s, x=rx + 3.35, y=2.95, w=rw - 3.6, h=0.7,
             text="7 of 7 — \"a game changer\"", size=12, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, x=rx, y=3.95, w=rw, h=0.55,
             text="The same feature — opposite verdicts",
             size=12.5, italic=True, color=SLATE)

    gold_callout(
        s, 0.55, 4.90, 12.25, 1.05,
        "Criterion: synthetic output is disqualified for a \"continue/"
        "stop\" decision by construction, not from bad luck on a run. "
        "Alternative: a pre-research role + real testing with 5-8 "
        "participants.",
        size=13, bold=True)
    refs_of_slide(s, "s12")
    notes_with_sources(s, "s12")
    return s


# ============================================================
# s13a - FAILURE on-point #2: Humane AI Pin (a failure of user research)
# ============================================================

def s13a(p):
    """EDIT #212 (owner remark R1-2026-10-01): IBM Watson for Oncology used
    to stand here — a case whose root cause lies in the training data rather
    than in user research, which means that in the user-research phase it was
    standing in the wrong place. In its place goes a case where that very
    phase is what failed: the product was built on an assumption about a
    person that was never checked with that person, and the question
    "compared with what" was closed by the market 10.5 months into sales.
    Watson stays in the chapter (§1.9, Case A): the failure class "the
    plausible taken for the real" has already been shown in Section 1 on s10
    and s12. The Google Glass counterfactual supplies the alternative the
    course rule requires — the same class of device, after the user was
    changed, delivered a measured gain."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "10,000 devices sold out of the 100,000 planned: the "
                   "comparison with the phone in the buyer's pocket was "
                   "made after the build",
                size=20, w=12.25, h=0.86, y=0.13)

    # ── WHAT HAPPENED — the account before the analysis ───────────────
    filled_rect(s, 0.55, 1.10, 12.25, 1.36, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.07)
    icon(s, "file-text", 0.78, 1.60, 0.42, "teal")
    text_runs(s, 1.38, 1.14, 11.28, 1.28, [
        {"text": "WHAT HAPPENED   ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "Humane is a company founded in 2018 by people who came "
                 "out of Apple. Its only product, the AI Pin, is a wearable "
                 "device with no screen: a small box worn on your clothes "
                 "with a camera, a microphone and a laser projection onto "
                 "your palm, answering out loud through a language model. "
                 "The idea: a person stops looking at their phone. The "
                 "device was shown on 9 November 2023 and sales opened in "
                 "April 2024 — $699 plus $24 a month. On 18 February 2025 "
                 "HP bought the assets for $116 million, and on 28 February "
                 "the cloud service was shut down: the devices in buyers' "
                 "hands stopped answering.",
         "size": 11, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)

    cw_ = 6.05
    left, right = 0.55, 6.75

    # ── What the numbers showed: every line with a base of its own ────
    ocean_box(s, left, 2.56, cw_, 2.30, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    icon(s, "trending-down", left + 0.24, 2.70, 0.46, "mid")
    text_box(s, x=left + 0.84, y=2.74, w=cw_ - 1.08, h=0.34,
             text="What the numbers showed", size=13, bold=True, color=MID)
    by = 3.20
    for b in ["About 10,000 devices sold — a tenth of the company's own "
              "target of 100,000 by the end of the year",
              "Revenue of about $9 million against about $230 million "
              "raised — roughly 4%",
              "Between May and August 2024, more returns than purchases: by "
              "August, closer to 7,000 were still in people's hands",
              "The price was cut from $699 to $499 on 23 October 2024 — six "
              "months after sales opened"]:
        text_box(s, x=left + 0.26, y=by, w=cw_ - 0.52, h=0.36,
                 text="• " + b, size=10, color=DEEP, line_spacing=1.12)
        by += 0.38

    # ── What was not found out before the build ───────────────────────
    ocean_box(s, right, 2.56, cw_, 2.30, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.6)
    icon(s, "search-x", right + 0.24, 2.70, 0.46, "teal")
    text_box(s, x=right + 0.84, y=2.74, w=cw_ - 1.08, h=0.34,
             text="What was not found out before the build", size=13,
             bold=True, color=TEAL)
    text_runs(s, right + 0.26, 3.18, cw_ - 0.52, 1.62, [
        {"text": "The discovery phase's question fits in one phrase: ",
         "size": 10.5, "color": DEEP},
        {"text": "compared with what", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": ". Every buyer already had a phone in their pocket that "
                 "does the same things, and everything else on top. "
                 "Reviewers converged on the same point: the device does "
                 "less than a phone and does it more slowly.",
         "size": 10.5, "color": DEEP},
        {"text": "An answer like that costs eight conversations with living "
                 "people before the build. Here it arrived from the market "
                 "— by way of $230 million and 10.5 months of sales.",
         "size": 10.5, "color": DEEP, "newpara": True, "space_before": 4},
    ], line_spacing=1.14)

    gold_callout(
        s, 0.55, 4.96, 12.25, 0.84,
        "The answer about the user arrives either way; the discovery phase "
        "only chooses when, and at what price. The criterion that carries "
        "forward: a hypothesis about the user is closed by comparing it "
        "with whatever that person gets by with today.",
        size=12.5, bold=True)

    teal_callout(
        s, 0.55, 5.88, 12.25, 1.06,
        "The device does work, and the miss lies in the answer to who needs "
        "it and what for. Google Glass travelled the same road in the "
        "opposite direction: the $1,500 glasses were pulled from general "
        "sale in January 2015 and then handed to people whose hands are "
        "busy with work. At AGCO, a maker of agricultural machinery, "
        "machine assembly time fell by 25% and inspection time by 30%; at "
        "the logistics company DHL, warehouse output rose by 15% — all "
        "against the same work done without the glasses. Same device. "
        "Different user.",
        size=10.5, bold=False)
    refs_of_slide(s, "s13a")
    notes_with_sources(s, "s13a")
    return s


# ============================================================
# s13 - FAILURE on-point #2: Deloitte fabricated research
# ============================================================
# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: superseded failure — the Deloitte fabricated-research case left Section 1 (issue #212).
def s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A $440,000 government report — with fabricated quotes inside",
                size=20, w=12.2, h=0.85)

    lx, lw = 0.55, 6.55
    ocean_box(s, lx, 1.55, lw, 3.30)
    icon(s, "file-x", lx + 0.24, 1.75, 0.6, "mid")
    text_box(s, x=lx + 1.00, y=1.78, w=lw - 1.2, h=0.55,
             text="Deloitte Australia, 2025", size=15, bold=True, color=MID)
    facts = [
        "References to nonexistent papers + a fabricated court quote [1]",
        "Produced via Azure OpenAI with no human verification of citations",
    ]
    for i, f in enumerate(facts):
        y = 2.55 + i * 0.85
        text_box(s, x=lx + 0.28, y=y, w=lw - 0.56, h=0.75, text=f"• {f}",
                 size=12.5, color=DEEP, line_spacing=1.15)

    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 1.55, rw, 1.55, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.8)
    icon(s, "banknote", rx + 0.24, 1.78, 0.55, "gold")
    text_box(s, x=rx + 0.95, y=1.80, w=rw - 1.15, h=0.55,
             text="A$440,000", size=26, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=2.55, w=rw - 0.48, h=0.45,
             text="~US$290,000 report", size=12, italic=True, color=SLATE)
    filled_rect(s, rx, 3.30, rw, 1.55, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.07)
    text_box(s, x=rx + 0.24, y=3.45, w=rw - 0.48, h=1.25,
             text="Base rate: ~712 court cases worldwide involving AI-"
                  "hallucinated citations, ~90% of them in 2025 [2]",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.10, 12.25, 0.95,
        "Lesson: model output during the discovery phase is an unverified "
        "draft, not a source of facts. Criterion: a final document for an "
        "external client requires verifying 100% of citations, not a "
        "sample.",
        size=12.5, bold=True)
    refs_of_slide(s, "s13")
    notes_with_sources(s, "s13")
    return s
