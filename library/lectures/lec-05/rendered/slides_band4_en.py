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


def s44(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Governance — the capstone that answers the hook paradox",
        bridge="Why assembly is nearly free, but value is not. Here we "
               "rise to the level of the organization and assemble the "
               "whole loop.",
        sid="s44", tag="2 failures · payoff",
        meme_name="s44-sad-pablo.jpg")


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
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The bottleneck shifted from technology to the organization's operating model",
                size=19, w=12.3, h=0.85)
    # 5 sources converge
    ocean_box(s, 0.55, 1.60, 6.35, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    srcs = ["Deloitte", "Sber", "Gartner", "McKinsey", "Forrester"]
    for i, sname in enumerate(srcs):
        y = 1.85 + i * 0.60
        chip(s, 0.85, y, 1.85, 0.44, sname, fill=LIGHT, color=WHITE, size=12)
        connector(s, 2.75, y + 0.22, 5.05, 2.95, color=SOFT_GREY, width=1.2)
    filled_rect(s, 4.15, 2.55, 2.5, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.10)
    text_box(s, x=4.20, y=2.62, w=2.4, h=0.65, text="operating model",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    text_box(s, x=0.80, y=4.85, w=5.9, h=0.3,
             text="Deloitte: 75% say the model must change · 42% low/zero ROI [1]",
             size=11, italic=True, color=SLATE)
    # right: maturity scale
    ocean_box(s, 7.15, 1.60, 5.65, 3.55, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.40, y=1.75, w=5.15, h=0.4, text="Maturity 0-5",
             size=14, bold=True, color=TEAL)
    for i in range(6):
        x = 7.45 + i * 0.85
        cur = (i == 3)
        col = GOLD if cur else SOFT_GREY
        filled_rect(s, x, 2.55, 0.70, 0.70, (GOLD_TINT if cur else SURFACE),
                    stroke=col, stroke_pt=(2.0 if cur else 1.0), radius=True,
                    radius_adj=0.12)
        text_box(s, x=x, y=2.70, w=0.70, h=0.4, text=str(i), size=15,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=7.45, y=3.35, w=2.4, h=0.5, text="Sber is here →",
             size=11.5, bold=True, color=DEEP)
    text_box(s, x=7.40, y=3.95, w=5.15, h=1.1,
             text="Operators → orchestrators. Sber rates itself at level "
                  "3 of 5 [2] — an anti-hype signal: even a large player "
                  "doesn't claim the top of the scale.",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.72,
        "Five independent sources converge on one point: the winner "
        "isn't whoever has the better model, but whoever rebuilt teams "
        "and governance around it.",
        size=12.5, bold=True)
    refs_of_slide(s, "s46")
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
