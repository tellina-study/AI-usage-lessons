"""Lecture 5 (EN) — Band 4 (Section 6 Governance/finale s44-s49 + ELI5 s44b).

EN twin of slides_band4.py: same layout/geometry/palette, English visible
strings + speaker notes sourced from slides-en/sNN*.md.
Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.
s49 = hero payoff (>=40% area, a closed loop with a human at the center).
"""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, icon, slide_title,
    gold_callout, teal_callout, notes_with_sources, refs_of_slide,
    build_section_divider,
    eli5_overview, meme_in_box, photo_in_box, add_image,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, CHARTS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
import re


def md_text(slide, x, y, w, h, text, *, size=11.0, color=DEEP,
            bold_color=MID, line_spacing=1.15, anchor=MSO_ANCHOR.TOP):
    """Text with **bold** markup in a single call. Local copy of the device
    from slides_band4.py (RU twin), which in turn copies it from band6: the
    shared _helpers_en is being edited by other agents, and dragging one more
    primitive in there for the sake of two slides buys nothing."""
    runs = []
    first = True
    for line in text.split("\n"):
        newp = not first
        first = False
        started = False
        for part in re.split(r'(\*\*.+?\*\*)', line):
            if not part:
                continue
            b = part.startswith("**") and part.endswith("**")
            cfg = {"text": (part[2:-2] if b else part), "size": size,
                   "bold": b, "color": (bold_color if b else color)}
            if newp and not started:
                cfg["newpara"] = True
            started = True
            runs.append(cfg)
        if not started:
            cfg = {"text": " ", "size": size, "color": color}
            if newp:
                cfg["newpara"] = True
            runs.append(cfg)
    return text_runs(slide, x, y, w, h, runs, line_spacing=line_spacing,
                     anchor=anchor)


def block_label(slide, x, y, w, text, *, color=MID, size=10.0):
    """Caption of a block inside an Ocean box: says WHAT the block is —
    rule R4 of owner-review-2026-09-30 (every part of a slide is captioned)."""
    text_box(slide, x=x, y=y, w=w, h=0.26, text=text, size=size, bold=True,
             color=color, line_spacing=1.0)


def s44(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Governance — the capstone that answers the hook paradox",
        bridge="Why assembly is nearly free, but value is not. Here we "
               "rise to the level of the organization and assemble the "
               "whole loop.",
        sid="s44", tag="2 failures · payoff",
        meme_name="s44-sad-pablo.jpg")


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
def s44b(p):
    return eli5_overview(
        p, "s44b", title="Governance in plain terms", icon_name="scale",
        cards=[
            ("What it is",
             "An organization-level phase: not \"how to build one "
             "product,\" but \"what to fund at all\" — and stop what "
             "doesn't pay off."),
            ("Why",
             "Resources are limited. The same \"continue / kill\" gate "
             "as for a single feature is raised to the level of capital "
             "across many initiatives."),
            ("Mental model",
             "A portfolio funnel: many ideas in, few funded ones out. An "
             "AI product adds a new variable — the cost of every request "
             "against its value."),
        ])


def s45(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The same go/kill gate — but now it allocates capital across many initiatives",
                size=19, w=12.3, h=0.85)
    # portfolio funnel
    ocean_box(s, 0.55, 1.60, 6.05, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=5.5, h=0.4, text="Portfolio funnel",
             size=13.5, bold=True, color=MID)
    widths = [5.35, 4.0, 2.6, 2.3]
    labels = ["many initiatives", "gate 1", "gate 2", "funded"]
    sizes = [11.5, 11.5, 11.5, 10.5]
    cols = [LIGHT, MID, TEAL, GOLD]
    for i, (w, lb, col, sz) in enumerate(zip(widths, labels, cols, sizes)):
        y = 2.25 + i * 0.68
        x = 0.80 + (5.5 - w) / 2
        filled_rect(s, x, y, w, 0.52, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x, y=y, w=w, h=0.52, text=lb, size=sz, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # right: unit economics
    ocean_box(s, 6.85, 1.60, 5.95, 1.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.10, y=1.75, w=5.45, h=0.4, text="Unit economics of an AI product",
             size=14, bold=True, color=TEAL)
    text_box(s, x=7.10, y=2.25, w=5.45, h=1.1,
             text="A new variable — cost per request against value per "
                  "request. Every call to the model costs real money.",
             size=12.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, 6.85, 3.65, 5.95, 1.50, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.07)
    text_box(s, x=7.10, y=3.78, w=5.45, h=1.25,
             text="Financial KPI at pilot entry: \"cut ticket cost from "
                  "X to Y while CSAT >= Z; N tickets, M weeks, owner — "
                  "Smith.\"",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.72,
        "Portfolio governance = Stage-Gate, raised to the level of "
        "capital: the same \"a funnel, not a tunnel\" discipline, but "
        "across products, not within one.",
        size=12.5, bold=True)
    notes_with_sources(s, "s45")
    return s


def s46(p):
    """EN PARITY, issue #212 — REWRITTEN WHOLE, not re-translated.

    The EN twin still carried the pre-Stage-6 slide ("The bottleneck shifted
    from technology to the organization's operating model": five converging
    sources Deloitte/Sber/Gartner/McKinsey/Forrester + a 0-5 maturity scale),
    which the RU rebuild deleted on the owner's remark 3 — "slide 48 is an
    abrupt, illogical transition. better to give the assessment of a feature
    in the abstract, AI inside or not". The slide now gives the apparatus for
    assessing ANY feature, indifferent to whether AI sits inside it, and a
    separate band states which two of the four points AI changes and which
    two stay word for word the same.

    The statistics of the former slide stay in the chapter §6.2; Deloitte and
    Boston Consulting Group are voiced on s45. The s46 entry in SLIDE_REFS is
    removed in step with the RU side: there are no external numbers on the
    slide any more, and the reference list under it would print sources the
    slide does not cite."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "How any feature is assessed — AI inside or not",
                size=19, w=12.25, h=0.62, y=0.13)

    cards = [
        ("1", "What behaviour it changes",
         "Which user action becomes more frequent, faster or cheaper. "
         "Unnamed action — nothing to assess.", MID, "target"),
        ("2", "Against what baseline",
         "The same product without the feature, same period. With no "
         "baseline, any gain gets credited to it.", TEAL, "ruler"),
        ("3", "What it costs",
         "Build once, run every month. The second is counted together "
         "with usage volume.", LIGHT, "banknote"),
        ("4", "At what result it gets shut down",
         "Number and date written down before launch: named after, it "
         "only explains the result.", GOLD, "timer"),
    ]
    for i, (num, name, body, col, ic) in enumerate(cards):
        x = 0.55 + (i % 2) * 6.20
        y = 0.92 + (i // 2) * 1.63
        ocean_box(s, x, y, 6.05, 1.48, fill=SURFACE, stroke=col, stroke_pt=1.5)
        circle(s, x + 0.20, y + 0.16, 0.36, col)
        text_box(s, x=x + 0.20, y=y + 0.16, w=0.36, h=0.36, text=num, size=14,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        text_box(s, x=x + 0.66, y=y + 0.14, w=4.70, h=0.40, text=name,
                 size=12.5, bold=True,
                 color=(DEEP if col is GOLD else col),
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.04)
        icon(s, ic, x + 5.52, y + 0.18, 0.32, "light")
        md_text(s, x + 0.22, y + 0.60, 5.61, 0.78, body, size=10.5,
                line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, 0.55, 4.18, 12.25, 1.22, fill=SURFACE, stroke=GOLD,
              stroke_pt=2.0)
    block_label(s, 0.78, 4.28, 11.75,
                "WHAT CHANGES WHEN THERE IS AI INSIDE", color=DEEP,
                size=10.5)
    md_text(s, 0.78, 4.58, 11.75, 0.76,
            "Two of the four change. **The third:** running stops being a "
            "one-off — it gains a meter that ticks with volume. **The "
            "first:** the model's answer varies run to run, so \"it works\" "
            "is confirmed on a sample, and one lucky example does not "
            "count. **The second and fourth** stay word for word the same.",
            size=11.5, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.52, 12.25, 1.00,
        "The second question — the baseline — breaks more often than the "
        "other three. The two cases ahead are exactly about that: a loud "
        "failure number that turns out to have no denominator, and a "
        "claimed autonomy fourteen times off the company's own target.",
        size=13, bold=True)
    notes_with_sources(s, "s46")
    return s


def s47(p):
    """GATE-B fix mirrored from RU: the funnel chart is the unambiguous
    visual dominant (wide top band, ~46% of slide area)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "60% explored → 20% piloted → 5% succeeded: 25% among those who got there, not \"95% failure\" [1]",
                size=17, w=12.3, h=0.72, y=0.28)
    # TOP: the funnel chart is now the dominant visual — full-width, tall
    ocean_box(s, 0.55, 1.20, 12.25, 3.15, fill=SURFACE, stroke=GOLD,
              stroke_pt=2.0)
    add_image(s, CHARTS / "c-mit-funnel.png", 1.35, 1.40, 10.65, 2.75,
              preserve_aspect=True)
    # debunk statement directly under the funnel — the payoff stated in words
    gold_callout(
        s, 0.55, 4.50, 12.25, 0.72,
        "\"95% failure\" is a headline that doesn't survive calibration: "
        "success among those who reached a pilot is 25%, not 5% [2, 3].",
        size=14, bold=True, align=PP_ALIGN.CENTER)
    # BOTTOM ROW: MIT source photo (small) + 4-question checklist + BCG note
    photo_in_box(s, "s47-mit-real-source.png", 0.55, 5.35, 2.55, 1.55, pad=0.12)
    ocean_box(s, 3.25, 5.35, 5.35, 1.55, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=3.48, y=5.45, w=4.9, h=0.32,
             text="4 questions for any loud AI-failure number",
             size=11.5, bold=True, color=MID, line_spacing=1.0)
    qs = ["1. What is the denominator?", "2. What counts as \"failure\"?",
          "3. What's the author's conflict of interest? [3]",
          "4. Does it trace to a primary source?"]
    for i, qq in enumerate(qs):
        text_box(s, x=3.48, y=5.82 + i * 0.27, w=4.9, h=0.26, text=qq,
                 size=10, color=DEEP, line_spacing=1.0)
    filled_rect(s, 8.75, 5.35, 4.05, 1.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.08)
    text_box(s, x=8.95, y=5.45, w=3.65, h=1.35,
             text="BCG: 60% of companies track zero financial KPIs tied "
                  "to AI value [5] — this is why failure numbers inflate "
                  "so easily.",
             size=10.5, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    refs_of_slide(s, "s47")
    notes_with_sources(s, "s47")
    return s


def s48(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The \"autonomous\" store: 700 of 1,000 transactions needed manual review against a target of 50",
                size=16, w=12.3, h=0.85)
    # top: Just Walk Out
    photo_in_box(s, "s48-amazon-real-source.png", 0.55, 1.50, 3.35, 1.85)
    ocean_box(s, 4.10, 1.50, 3.55, 1.85, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(s, CHARTS / "c-jwo.png", 4.30, 1.65, 3.15, 1.55,
              preserve_aspect=True)
    ocean_box(s, 7.85, 1.50, 4.95, 1.85, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    text_box(s, x=8.10, y=1.62, w=4.45, h=1.65,
             text="Just Walk Out (Amazon), since 2018: 700/1,000 "
                  "transactions — manual review (14x above the 50/1,000 "
                  "target) [1]. 6 years of \"autonomous AI\" marketing "
                  "with no disclosure of the labor scale (hidden human "
                  "cost) [2].",
             size=11, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    # bottom: 6-phase summary matrix
    phases = [("Discovery", "synthesis, desk", "interviews"),
              ("Design", "generation", "safety reqs"),
              ("Build/Launch", "code ~= free", "review, kill gate"),
              ("Measure", "evals", "randomization"),
              ("Support", "tracing", "escalation"),
              ("Governance", "operating model", "cost/request")]
    cw = 12.25 / 6
    y0 = 3.65
    # header
    filled_rect(s, 0.55, y0, 12.25, 0.42, MID, radius=True, radius_adj=0.05)
    text_box(s, x=0.55, y=y0, w=12.25, h=0.42, text="Phase x what AI changes x what stays from the classic",
             size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    for i, (ph, ai, cl) in enumerate(phases):
        x = 0.55 + i * cw
        ocean_box(s, x + 0.02, y0 + 0.48, cw - 0.04, 1.35, fill=SURFACE,
                  stroke=LIGHT, stroke_pt=1.0)
        text_box(s, x=x + 0.08, y=y0 + 0.56, w=cw - 0.16, h=0.4, text=ph,
                 size=10.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.95)
        text_box(s, x=x + 0.08, y=y0 + 1.00, w=cw - 0.16, h=0.34, text=ai,
                 size=9, color=TEAL, align=PP_ALIGN.CENTER, line_spacing=0.95)
        text_box(s, x=x + 0.08, y=y0 + 1.42, w=cw - 0.16, h=0.34, text=cl,
                 size=9, color=SLATE, align=PP_ALIGN.CENTER, line_spacing=0.95)
    refs_of_slide(s, "s48")
    notes_with_sources(s, "s48")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: a duplicate of s47/s51/s55 (issue #212).
def s49(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Assembly is free — the scarcity now is judgment, not execution",
                size=20, w=12.3, h=0.62, y=0.22)
    # closing hero photo (>=40% area) — real photo via 6-tier acquisition,
    # NASA Mission Control (Apollo 16), public domain, Wikimedia Commons
    photo_in_box(s, "s49-missioncontrol-crop.png", 0.55, 0.92, 12.25, 3.55,
                 pad=0.09)
    text_box(s, x=0.70, y=4.50, w=9.0, h=0.28,
             text="NASA Mission Control, Apollo 16 — humans make the "
                  "call while automation runs",
             size=10.5, italic=True, color=SLATE)
    gold_callout(
        s, 0.55, 4.82, 12.25, 0.62,
        "When execution is nearly free, the scarce resource is "
        "judgment: telling signal from noise and keeping intent and "
        "accountability with the human.",
        size=12.5, bold=True)
    # compact 8-question checklist below the keystone statement (2 rows x 4)
    checks = [
        "1. Is the classic in place?", "2. Is trust worth the cost?",
        "3. Eval + reference dataset?", "4. A guardrail metric?",
        "5. Staged rollout + rollback?", "6. Human escalation guaranteed?",
        "7. Who is accountable?", "8. Is the data safe?",
    ]
    chip(s, 0.55, 5.56, 5.4, 0.32, "Checklist \"before you go AI-first\"",
         fill=GOLD, color=DEEP, size=10.5)
    cw2, gap2 = 2.98, 0.12
    x0, y0 = 0.55, 5.98
    for i, c in enumerate(checks):
        col_i = i % 4
        row_i = i // 4
        x = x0 + col_i * (cw2 + gap2)
        y = y0 + row_i * 0.55
        icon(s, "circle-check", x, y, 0.24, "teal")
        text_box(s, x=x + 0.30, y=y - 0.03, w=cw2 - 0.30, h=0.50, text=c,
                 size=9.2, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.95)
    notes_with_sources(s, "s49")
    return s
