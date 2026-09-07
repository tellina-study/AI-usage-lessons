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
# s04 - bridge from Lec-4 + central question (nested loops)
# ============================================================
def s04(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Lecture 4's code loop is one step inside the product loop",
                size=23, w=12.0, h=0.85)

    # outer big loop box
    ocean_box(s, 0.55, 1.50, 12.25, 2.85, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.80, y=1.62, w=6.0, h=0.35, text="Product loop (Lecture 5)",
             size=13, bold=True, color=MID)
    import math
    mcx, mcy, mr = 2.55, 2.85, 0.72
    mnodes = ["search", "pencil", "hammer", "ruler", "headphones", "scale"]
    mcenters = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        mcenters.append((mcx + mr * math.cos(ang), mcy - mr * math.sin(ang)))
    for i in range(6):
        x1, y1 = mcenters[i]
        x2, y2 = mcenters[(i + 1) % 6]
        connector(s, x1, y1, x2, y2,
                  color=(GOLD if i == 5 else LIGHT),
                  width=(2.0 if i == 5 else 1.4), arrow_end=True)
    for i, ic in enumerate(mnodes):
        nx, ny = mcenters[i]
        circle(s, nx - 0.22, ny - 0.22, 0.44, WHITE, stroke=MID, stroke_pt=1.2)
        icon(s, ic, nx - 0.14, ny - 0.14, 0.28, "mid")
    chip(s, 4.55, 2.62, 1.05, 0.42, "6 phases", fill=GOLD, color=DEEP, size=12)
    icon(s, "layers", 0.85, 3.75, 0.5, "teal")
    text_box(s, x=1.50, y=3.75, w=6.05, h=0.55,
             text="discovery → design → build/launch → measure → "
                  "operate → govern → discovery again",
             size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    # inner small loop box nested inside "build" area
    ocean_box(s, 7.9, 2.05, 4.65, 2.00, fill=WHITE, stroke=GOLD,
              stroke_pt=1.8)
    text_box(s, x=8.10, y=2.20, w=4.30, h=0.32,
             text="Code loop (Lecture 4)", size=11.5, bold=True, color=DEEP)
    text_box(s, x=8.10, y=2.62, w=4.30, h=1.20,
             text="spec → ADR → plan → PR → incident",
             size=12, italic=True, color=SLATE, line_spacing=1.2,
             anchor=MSO_ANCHOR.TOP)
    icon(s, "git-branch", 8.10, 3.30, 0.5, "teal")

    ocean_box(s, 0.55, 4.35, 12.25, 1.65)
    text_box(s, x=0.85, y=4.48, w=11.65, h=1.4,
             text="Now that AI made assembly nearly free — what became the "
                  "product's real bottleneck, and on every phase of the "
                  "loop: which classical discipline stays, what does AI "
                  "speed up, and where does AI-first break?",
             size=17, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.18)

    gold_callout(
        s, 0.55, 6.15, 12.25, 0.60,
        "Lecture 4's unit of work is the pull request. The unit of work "
        "here is a hypothesis, an experiment, a release decision.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    notes_with_sources(s, "s04")
    return s


# ============================================================
# s05 - KEYSTONE: loop, 3 independent sources (PDCA/OODA/BML)
# ============================================================
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
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Hours → minutes: but links exist so they can be checked",
                size=22, w=12.2, h=0.85)

    blocks = [
        ("file-search", "Desk research",
         "Perplexity Deep Research: 2 hours → ~30 minutes [1]"),
        ("layout-list", "Interview synthesis",
         "Dovetail — pain-point clustering at scale [2]"),
        ("database", "Reference dataset",
         "a curated collection of \"query → correct answer\""),
    ]
    cw, gap = 3.95, 0.20
    x0 = 0.55
    y0 = 1.55
    for i, (ic, head, body) in enumerate(blocks):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 2.05)
        icon(s, ic, x + 0.24, y0 + 0.20, 0.56, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.88, w=cw - 0.48, h=0.50, text=head,
                 size=12, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.44, w=cw - 0.48, h=0.55, text=body,
                 size=11, color=DEEP, line_spacing=1.10)
        if i == 0:
            chip(s, x + cw - 1.55, y0 + 0.20, 1.30, 0.36, "verify the source",
                 fill=GOLD, color=DEEP, size=9)

    gold_callout(
        s, 0.55, 3.90, 12.25, 0.72,
        "97% of researchers use AI — only ~8% trust AI personas as data [3]",
        size=14.5, bold=True, align=PP_ALIGN.CENTER)

    filled_rect(s, 0.55, 4.85, 12.25, 1.35, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=0.85, y=4.98, w=11.65, h=1.10,
             text="Mandatory practice: verify important data directly "
                  "against the source before using it in a decision. "
                  "Synthetic users are only a pre-research step (piloting "
                  "a guide, a draft of personas, generating hypotheses), "
                  "never evidence for a go/no-go decision.",
             size=12.5, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
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
# s13a - FAILURE on-point #3: IBM Watson for Oncology
# ============================================================
def s13a(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "$62 million — and not a single patient treated",
                size=23, w=12.2, h=0.85)

    # scale visual
    lx = 0.55
    ocean_box(s, lx, 1.55, 5.55, 2.55, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    icon(s, "scale", lx + 2.35, 1.70, 0.9, "mid")
    text_box(s, x=lx + 0.25, y=2.70, w=2.4, h=0.75,
             text="$62M", size=22, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 2.9, y=2.70, w=2.4, h=0.75,
             text="0 patients", size=22, bold=True, color=TEAL,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.25, y=3.55, w=5.05, h=0.45,
             text="MD Anderson: partnership closed (2016) [1]", size=11.5,
             italic=True, color=SLATE, align=PP_ALIGN.CENTER)

    rx, rw = 6.35, 6.45
    text_box(s, x=rx, y=1.55, w=rw, h=0.35,
             text="IBM Watson for Oncology, since 2012", size=14, bold=True,
             color=MID)
    bullets = [
        "Internal documents: recommendations were \"unsafe and incorrect\" [1]",
        "Trained on hypothetical cases from a handful of MSK oncologists — "
        "not on real outcomes [2]",
    ]
    for i, b in enumerate(bullets):
        y = 2.05 + i * 0.95
        icon(s, "user-x" if i else "users", rx, y, 0.42, "light")
        text_box(s, x=rx + 0.55, y=y - 0.05, w=rw - 0.55, h=0.85, text=b,
                 size=12.5, color=DEEP, line_spacing=1.12)

    gold_callout(
        s, 0.55, 4.35, 12.25, 1.15,
        "Criterion: a high-stakes domain + only synthetic/hypothetical "
        "data behind the recommendation = the product isn't ready, no "
        "matter how impressive the demo. Alternative: a system built on "
        "evidence-based clinical guidelines with transparent source "
        "traceability.",
        size=13, bold=True)
    refs_of_slide(s, "s13a")
    notes_with_sources(s, "s13a")
    return s


# ============================================================
# s13 - FAILURE on-point #2: Deloitte fabricated research
# ============================================================
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
