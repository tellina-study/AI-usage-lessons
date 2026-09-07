"""Lecture 5 (EN) — Band 2 (Section 2 Design s14-s20 + Section 3 Build/Launch
s21-s27, plus ELI5 overviews s14b, s21b).

EN twin of slides_band2.py: same layout/geometry/palette, English visible
strings + speaker notes sourced from slides-en/sNN*.md.
Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.
NO timing / NO methodology / NO photo-attribution on visible layer.
Memes: real imgflip templates via assets/memes-en; real photos via
assets/screenshots (language-agnostic). Sources -> speaker notes only.
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


# ============================================================
# Section 2. Design / prototype
# ============================================================
def s14(p):
    return build_section_divider(
        p, here_idx=2,
        subtitle="Design — a hypothesis becomes an artifact",
        bridge="How a hypothesis from research turns into a concrete "
               "artifact you can show a person. This is also where safety "
               "gets built in — in the design brief, not patched on after "
               "something has already gone wrong.",
        sid="s14", tag="2 base cases · 2 failures",
        meme_name="s14-drake.jpg")


def s14b(p):
    return eli5_overview(
        p, "s14b", title="Design in plain terms", icon_name="pencil",
        cards=[
            ("What it is",
             "A hypothesis becomes a cheap draft: a screen sketch, a "
             "clickable prototype — something you can show a person."),
            ("Why",
             "You won't mind throwing away a draft. Discovering \"it "
             "doesn't work\" on paper is cheap; discovering the same thing "
             "after launch is very expensive."),
            ("Mental model",
             "Two diamonds: first find the right problem, then the right "
             "solution. A common mistake is jumping straight to the "
             "solution."),
        ])


def s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Two diamonds: first the right problem, then the right solution",
                size=22, w=12.2, h=0.85)

    def diamond(cx, top_lbl, bot_lbl, col, domain_lbl):
        y0, dw, dh = 2.05, 2.7, 2.0
        sh = s.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(cx - dw / 2),
                                Inches(y0), Inches(dw), Inches(dh))
        sh.fill.solid(); sh.fill.fore_color.rgb = SURFACE
        sh.line.color.rgb = col; sh.line.width = Pt(1.8)
        from _helpers_en import disable_shadow
        disable_shadow(sh)
        text_box(s, x=cx - dw / 2 - 0.5, y=y0 + dh / 2 - 0.35, w=dw + 1.0,
                 h=0.7, text=domain_lbl, size=13.5, bold=True, color=col,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=cx - dw / 2 - 0.35, y=y0 - 0.62, w=dw + 0.7, h=0.55,
                 text=top_lbl, size=12.5, bold=True, color=col,
                 align=PP_ALIGN.CENTER, line_spacing=1.05)
        text_box(s, x=cx - dw / 2 - 0.35, y=y0 + dh + 0.08, w=dw + 0.7,
                 h=0.55, text=bot_lbl, size=12.5, bold=True, color=DEEP,
                 align=PP_ALIGN.CENTER, line_spacing=1.05)
    diamond(3.35, "Widen the problem", "Narrow: one problem", MID,
            "The right\nproblem")
    diamond(7.65, "Widen the solution", "Narrow: one solution", TEAL,
            "The right\nsolution")
    right_arrow(s, 5.05, 2.90, 0.55, 0.28, fill=LIGHT)
    text_box(s, x=9.35, y=2.85, w=3.4, h=1.3,
             text="Double Diamond [1]\n(Design Council UK)\n\nDesign "
                  "Thinking — its 5-step version of the same framework",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    gold_callout(
        s, 0.55, 4.60, 12.25, 1.35,
        "A common mistake: converging on a solution without checking the "
        "problem itself — skipping the first diamond. A cheap prototype "
        "exists precisely to surface this before money is spent on "
        "development.",
        size=14, bold=True)
    refs_of_slide(s, "s15")
    notes_with_sources(s, "s15")
    return s


def s16(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Nielsen's heuristics are a linter for UX, not a substitute for testing",
                size=22, w=12.2, h=0.85)
    heur = [
        "Visibility of system status",
        "Match with the user's language",
        "User control and freedom (undo)",
        "Consistency",
        "Error prevention",
    ]
    ocean_box(s, 0.55, 1.55, 6.75, 5.35)
    icon(s, "circle-check", 0.80, 1.75, 0.55, "mid")
    text_box(s, x=1.55, y=1.80, w=5.6, h=0.4, text="Top 5 of 10 heuristics [1]",
             size=15, bold=True, color=MID)
    for i, h in enumerate(heur):
        y = 2.45 + i * 0.50
        chip(s, 0.80, y, 0.42, 0.34, str(i + 1), fill=GOLD, color=DEEP, size=12)
        text_box(s, x=1.40, y=y - 0.02, w=5.6, h=0.4, text=h, size=13,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 0.55, 5.20, 6.75, 1.55, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.6)
    icon(s, "shield-check", 0.80, 5.42, 0.55, "teal")
    text_box(s, x=1.55, y=5.44, w=5.6, h=0.4, text="Design system = guardrail",
             size=14, bold=True, color=TEAL)
    text_box(s, x=0.80, y=6.05, w=6.25, h=0.6,
             text="Keeps generative freedom inside an already-validated "
                  "brand.",
             size=12.5, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 7.55, 1.55, 5.25, 1.05,
        "Metaphor: heuristics are like a linter for the interface. They "
        "catch typical problems before money is spent on research — but "
        "don't replace testing with a real user [2].",
        size=12.5, bold=True)
    mx, my, mw, mh = 7.90, 2.80, 4.55, 3.60
    meme_in_box(s, "s16-bernie.jpg", mx, my, mw, mh, pad=0.12)
    text_box(s, x=7.55, y=my + mh + 0.12, w=5.25, h=0.65,
             text="\"I'm once again asking\": heuristics catch typical "
                  "problems, but don't replace testing with a real user.",
             size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    refs_of_slide(s, "s16")
    notes_with_sources(s, "s16")
    return s


def s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "AI for divergence, humans for convergence",
                size=24, w=12.2, h=0.85)
    # funnel: 2-4 AI directions -> 1 human-refined
    ocean_box(s, 0.55, 1.60, 6.55, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=6.0, h=0.4, text="Direction generation",
             size=13.5, bold=True, color=MID)
    for i in range(4):
        x = 0.85 + i * 1.55
        filled_rect(s, x, 2.25, 1.30, 0.95, WHITE, stroke=LIGHT, stroke_pt=1.2,
                    radius=True, radius_adj=0.10)
        icon(s, "monitor-smartphone", x + 0.42, 2.42, 0.45, "light")
        text_box(s, x=x, y=3.02, w=1.30, h=0.25, text=f"option {i+1}",
                 size=9.5, color=SLATE, align=PP_ALIGN.CENTER)
    right_arrow(s, 3.05, 3.55, 1.0, 0.30, fill=GOLD)
    filled_rect(s, 2.55, 3.95, 2.0, 0.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.12)
    text_box(s, x=2.55, y=4.02, w=2.0, h=0.4, text="1 refined",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # right: tools
    ocean_box(s, 7.35, 1.60, 5.45, 3.05, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=7.60, y=1.72, w=5.0, h=0.4, text="2025-26 tools",
             size=13.5, bold=True, color=TEAL)
    text_box(s, x=7.60, y=2.20, w=5.0, h=0.5,
             text="v0 (Vercel) · Figma Make [1] · Google Stitch [2] · bolt.new",
             size=12.5, color=DEEP, line_spacing=1.15)
    text_box(s, x=7.60, y=2.95, w=5.0, h=1.5,
             text="• 2-4 directions in minutes (used to be a day of manual "
                  "wireframing)\n• Figma Make pulls in the team's own "
                  "components — less rework",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 4.85, 12.25, 1.05,
        "Convergence needs judgment about specific context that isn't in "
        "the training data: AI widens the space of options, choosing and "
        "testing with a real user stays with the human.",
        size=13, bold=True)
    refs_of_slide(s, "s17")
    notes_with_sources(s, "s17")
    return s


def s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "29% WCAG conformance across 21,880 evaluations — the platform matters more than the prompt [1]",
                size=21, w=12.3, h=0.85)
    # left: real WCAG donut chart
    ocean_box(s, 0.55, 1.55, 4.85, 3.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-wcag-29.png", 0.85, 1.75, 4.25, 3.15,
              preserve_aspect=True)
    # right: pigeon meme + facts
    meme_in_box(s, "s18-pigeon.jpg", 5.65, 1.55, 3.55, 3.55, pad=0.12)
    ocean_box(s, 9.45, 1.55, 3.35, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=9.68, y=1.70, w=2.9, h=1.4,
             text="21,880 WCAG evaluations of AI-generated interfaces:\n\n"
                  "• contrast 26.8%\n• use of color 19.2%",
             size=11.5, color=DEEP, line_spacing=1.2)
    text_box(s, x=9.68, y=3.35, w=2.9, h=1.6,
             text="\"Make it accessible\" in the prompt does not guarantee "
                  "the result — platform defaults decide, not the "
                  "request text.",
             size=11.5, italic=True, color=SLATE, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.30, 12.25, 0.80,
        "Design for NON-DETERMINISTIC output: same input → different "
        "output → breaks the consistency heuristic; you need human "
        "checkpoints.",
        size=13, bold=True)
    refs_of_slide(s, "s18")
    notes_with_sources(s, "s18")
    return s


def s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Safeguards appeared almost two years after launch — only after the tragedy",
                size=21, w=12.3, h=0.85)
    ocean_box(s, 0.55, 1.55, 3.75, 4.30, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    icon(s, "shield-alert", 1.55, 2.05, 1.75, "light")
    text_box(s, x=0.85, y=4.05, w=3.15, h=1.5,
             text="Protection for vulnerable users was added as a "
                  "retrofit — after the tragedy, not in the original "
                  "design brief.",
             size=13, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.2)
    # right: real logo + timeline + facts
    photo_in_box(s, "s19-characterai-real-source.png", 4.55, 1.55, 3.15, 1.45,
                 pad=0.20)
    ocean_box(s, 7.90, 1.55, 4.90, 1.45, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=8.15, y=1.62, w=4.4, h=0.34, text="Character.AI",
             size=14, bold=True, color=MID)
    text_box(s, x=8.15, y=2.02, w=4.4, h=0.9,
             text="A 14-year-old user died after months of conversation "
                  "with an AI character (02.2024) [1].",
             size=12, color=DEEP, line_spacing=1.15)
    # timeline strip
    stages = ["Launch", "Tragedy\n02.2024", "Lawsuit\n10.2024", "Safeguards\n11.2025"]
    xs = [4.85, 6.85, 8.85, 10.85]
    for i, (st, x) in enumerate(zip(stages, xs)):
        col = GOLD if i == 3 else LIGHT
        circle(s, x, 3.55, 0.30, col, stroke=WHITE, stroke_pt=1.5)
        st_lbl = f"{st} [2]" if i == 3 else st
        text_box(s, x=x - 0.55, y=3.95, w=1.40, h=0.5, text=st_lbl, size=10,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER, line_spacing=0.9)
        if i < 3:
            connector(s, x + 0.30, 3.70, xs[i + 1], 3.70, color=SOFT_GREY,
                      width=2.0)
    gold_callout(
        s, 4.55, 4.75, 8.25, 1.10,
        "Root cause — not a runtime bug, but a missing requirement in the "
        "design brief: the MVP optimized for engagement without asking "
        "\"who could be harmed.\" Criterion: safeguards for vulnerable "
        "users belong in the MVP, not as a patch after a tragedy.",
        size=12.5, bold=True)
    refs_of_slide(s, "s19")
    notes_with_sources(s, "s19")
    return s


def s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Found by accident: the same application with a different birth date — an instant invite",
                size=19, w=12.3, h=0.85)
    # left: hard-coded filter concept
    ocean_box(s, 0.55, 1.60, 6.05, 3.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "cog", 1.05, 1.95, 0.9, "mid")
    text_box(s, x=2.20, y=2.05, w=4.1, h=0.75,
             text="A filter with a hardcoded \"birth date\" rule",
             size=13, bold=True, color=DEEP, line_spacing=1.1)
    filled_rect(s, 0.90, 3.05, 5.35, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.08)
    text_box(s, x=1.15, y=3.15, w=4.9, h=0.62,
             text="Women 55+ / men 60+ → auto-rejection",
             size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.90, y=4.00, w=5.4, h=0.8,
             text="Found by accident: resubmitting the same application "
                  "with a different birth date → an instant invite.",
             size=12, italic=True, color=SLATE, line_spacing=1.15)
    # right: EEOC
    ocean_box(s, 6.85, 1.60, 5.95, 1.55, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.8)
    icon(s, "scale", 7.10, 1.85, 0.6, "gold")
    text_box(s, x=7.85, y=1.85, w=4.7, h=0.55, text="$365,000 [1]",
             size=24, bold=True, color=DEEP)
    text_box(s, x=7.10, y=2.55, w=5.5, h=0.5,
             text="EEOC, Aug 9, 2023 — the first-ever AI discrimination "
                  "settlement",
             size=11.5, italic=True, color=SLATE, line_spacing=1.1)
    gold_callout(
        s, 6.85, 3.35, 5.95, 1.60,
        "Contrast with Character.AI: there, design did NOT build in a "
        "safeguard; here, design DID build in a specific harmful rule. "
        "Criterion: automating a decision about people → audit for "
        "discriminatory features BEFORE release.",
        size=12.5, bold=True)
    refs_of_slide(s, "s20")
    notes_with_sources(s, "s20")
    return s


# ============================================================
# Section 3. Build / Launch
# ============================================================
def s21(p):
    return build_section_divider(
        p, here_idx=3,
        subtitle="Build & Launch — the collapsed arrow",
        bridge="This is exactly where AI changes the most — the cost of "
               "writing the code itself. But the section doesn't start "
               "from that fact — it starts from the classical discipline "
               "of release: how to ship safely and when to stop.",
        sid="s21", tag="2 base cases · 2 failures",
        meme_name="s21-anakin-padme.jpg")


def s21b(p):
    return eli5_overview(
        p, "s21b", title="Build and launch in plain terms", icon_name="sliders-horizontal",
        cards=[
            ("What it is",
             "The artifact becomes a working product for users. AI made "
             "writing the code itself nearly free."),
            ("Why release mechanics matter",
             "Since building is cheap, the cost of a mistake is no "
             "longer \"writing it\" but \"shipping the wrong thing to "
             "everyone at once.\" You need to turn things on gradually "
             "and roll back fast."),
            ("Mental model",
             "Launch is a valve, not a switch: 1% → 10% → 100%, watch "
             "the reaction. And keep a \"kill\" decision ready, not just "
             "\"keep polishing forever.\""),
        ])


def s22(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Same mechanics — but here the decision is to kill the product, not flip a flag",
                size=20, w=12.3, h=0.85)
    # flow of primitives
    prim = ["Feature flag", "Canary", "Staged rollout", "Rollback"]
    gloss = ["a switch", "canary", "gradual", "revert"]
    cw, gap = 2.72, 0.28
    x0, y0 = 0.55, 1.70
    for i, (pr, gl) in enumerate(zip(prim, gloss)):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
        text_box(s, x=x + 0.10, y=y0 + 0.20, w=cw - 0.20, h=0.4, text=pr,
                 size=13.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.68, w=cw - 0.20, h=0.34, text=gl,
                 size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        if i < 3:
            right_arrow(s, x + cw + 0.02, y0 + 0.44, gap - 0.04, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=2.98, w=12.25, h=0.35,
             text="You know these primitives from engineering rollout (CI/CD)",
             size=12.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # new content card
    ocean_box(s, 1.55, 3.65, 10.25, 1.30, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    icon(s, "scale", 1.80, 3.95, 0.55, "gold")
    text_box(s, x=2.55, y=3.78, w=9.0, h=1.05,
             text="NEW here — whose decision they serve and by what "
                  "criteria: MVP (Ries) [1] = learning, not shipping. "
                  "Stage-Gate go/kill (Cooper) [2] — \"a funnel, not a "
                  "tunnel\": failure thresholds are written down as "
                  "numbers in advance.",
             size=12.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.25, 12.25, 0.85,
        "The common thread: launch speed is bought with a limited blast "
        "radius — how many users are affected if the new thing turns out "
        "bad.",
        size=13, bold=True)
    refs_of_slide(s, "s22")
    notes_with_sources(s, "s22")
    return s


def s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "+200% code per engineer — but only 16% of PRs got substantive review [1]",
                size=20, w=12.3, h=0.85)
    # left: real contrast chart
    ocean_box(s, 0.55, 1.55, 6.15, 3.55, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-review-bottleneck.png", 0.80, 1.80, 5.65, 3.05,
              preserve_aspect=True)
    # right: facts
    ocean_box(s, 6.95, 1.55, 5.85, 3.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=7.20, y=1.72, w=5.4, h=0.4, text="Anthropic's own measurement",
             size=14, bold=True, color=MID)
    text_box(s, x=7.20, y=2.25, w=5.4, h=2.6,
             text="• Implementation: weeks/months → minutes of agentic "
                  "execution\n\n"
                  "• Code volume per engineer: +200% year over year\n\n"
                  "• Substantive human review before merge: only ~16% "
                  "of PRs",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.30, 12.25, 0.80,
        "The scarce resource shifted to the two human ends: precision of "
        "intent going in and quality of judgment coming out — the "
        "bottleneck is now review, not writing.",
        size=13, bold=True)
    refs_of_slide(s, "s23")
    notes_with_sources(s, "s23")
    return s


def s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Launch isn't \"flip it on\" — it's a staged transfer of control",
                size=22, w=12.3, h=0.85)
    # ladder of 3 steps
    steps = [
        ("v1", "High control / low agency", "routes"),
        ("v2", "Proposes solutions for human approval", "human in the loop"),
        ("v3", "Automatic, with fallback to a human", "earned by track record"),
    ]
    for i, (v, head, sub) in enumerate(steps):
        y = 4.25 - i * 0.95
        w = 5.5 + i * 0.9
        col = [LIGHT, MID, GOLD][i]
        filled_rect(s, 0.70, y, w, 0.80, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.08)
        chip(s, 0.90, y + 0.22, 0.75, 0.36, v, fill=col, color=WHITE, size=13)
        text_box(s, x=1.80, y=y + 0.10, w=w - 1.2, h=0.4, text=head, size=12.5,
                 bold=True, color=DEEP)
        text_box(s, x=1.80, y=y + 0.46, w=w - 1.2, h=0.3, text=sub, size=10.5,
                 italic=True, color=SLATE)
    ocean_box(s, 7.75, 1.55, 5.05, 3.50, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=8.00, y=1.70, w=4.6, h=0.9, text="CC/CD vs the familiar CI/CD [1]",
             size=14, bold=True, color=TEAL, line_spacing=1.1)
    text_box(s, x=8.00, y=2.55, w=4.6, h=2.3,
             text="CC/CD — Continuous Calibration/Development. A release "
                  "is versioned by level of agency, not by feature set. "
                  "The agency ladder: Copilot, Cursor.",
             size=12.5, color=DEEP, line_spacing=1.2)
    gold_callout(
        s, 0.70, 5.05, 12.10, 0.95,
        "\"If you haven't tested it under high control, you're not ready "
        "to give it high agency\": an agent earns autonomy through a "
        "track record, not by default from the start.",
        size=13, bold=True)
    refs_of_slide(s, "s24")
    notes_with_sources(s, "s24")
    return s


def s25(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Double the generation speed and you double the review queue — not the throughput",
                size=19, w=12.3, h=0.85)
    # tilted scales metaphor
    ocean_box(s, 0.55, 1.60, 6.55, 3.40, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "scale", 3.15, 1.85, 1.1, "mid")
    filled_rect(s, 0.95, 3.25, 2.65, 0.80, GOLD_TINT, stroke=GOLD, stroke_pt=1.4,
                radius=True, radius_adj=0.10)
    text_box(s, x=1.05, y=3.35, w=2.45, h=0.6, text="generation\ncheap and fast",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 4.05, 3.25, 2.65, 0.80, SOFT_GREY, stroke=LIGHT, stroke_pt=1.4,
                radius=True, radius_adj=0.10)
    text_box(s, x=4.15, y=3.35, w=2.45, h=0.6, text="verification\nhasn't sped up",
             size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             line_spacing=1.0, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.95, y=4.20, w=5.7, h=0.7,
             text="Generating plausible code — seconds; checking it — "
                  "hasn't gotten faster.",
             size=12, italic=True, color=SLATE, line_spacing=1.12)
    # right: 70% problem
    ocean_box(s, 7.35, 1.60, 5.45, 3.40, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.60, y=1.75, w=5.0, h=0.4, text="The 70% problem [1]",
             size=14, bold=True, color=TEAL)
    text_box(s, x=7.60, y=2.30, w=5.0, h=2.4,
             text="A senior developer rethinks AI output and spends time "
                  "reworking it.\n\nA junior ships a \"house of cards "
                  "made of code\" that looks plausible but collapses "
                  "under load.",
             size=12.5, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.15, 12.25, 0.85,
        "Shipping without an eval gate or a rollback plan isn't speed — "
        "it's a deferred cost: review doesn't scale alongside generation.",
        size=13, bold=True)
    refs_of_slide(s, "s25")
    notes_with_sources(s, "s25")
    return s


def s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "0% → 100% in one step — skipping canary rollout entirely",
                size=21, w=12.3, h=0.85)
    # left: balloon meme
    meme_in_box(s, "s26-balloon.jpg", 0.55, 1.55, 3.55, 4.30, pad=0.14)
    # right: real logo + staged vs direct
    photo_in_box(s, "s26-google-real-source.png", 4.35, 1.55, 3.05, 1.35,
                 pad=0.24)
    ocean_box(s, 7.65, 1.55, 5.15, 1.35, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=7.90, y=1.62, w=4.65, h=0.34, text="Google AI Overviews, May 2024",
             size=13, bold=True, color=MID)
    text_box(s, x=7.90, y=2.00, w=4.65, h=0.85,
             text="Rolled out to 100% of US search in one step [1]. No "
                  "eval gate. Users couldn't turn it off.",
             size=11.5, color=DEEP, line_spacing=1.15)
    # staged bar
    stages = ["1%", "10%", "25%", "50%", "100%"]
    for i, st in enumerate(stages):
        x = 4.45 + i * 1.65
        col = SOFT_GREY if i < 4 else GOLD_TINT
        filled_rect(s, x, 3.30, 1.45, 0.60, col, stroke=LIGHT, stroke_pt=1.2,
                    radius=True, radius_adj=0.14)
        text_box(s, x=x, y=3.38, w=1.45, h=0.44, text=st, size=13, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
        if i < 4:
            right_arrow(s, x + 1.47, 3.48, 0.16, 0.24, fill=LIGHT)
    text_box(s, x=4.45, y=4.00, w=8.35, h=0.4,
             text="the correct canary rollout (skipped)",
             size=11.5, italic=True, color=SLATE)
    gold_callout(
        s, 4.35, 4.65, 8.45, 1.20,
        "At 1% of traffic the pattern (\"eat rocks\" — a satirical Onion "
        "article; \"glue on pizza\" — a Reddit joke) would have surfaced "
        "within days in internal monitoring [2]. Instead — public "
        "ridicule in front of 100% of the audience at once.",
        size=12.5, bold=True)
    refs_of_slide(s, "s26")
    notes_with_sources(s, "s26")
    return s


def s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "2.5-3 years on 0.7% of the chain — and stopping was the right call [1]",
                size=20, w=12.3, h=0.85)
    # left: real logo + tiny segment
    photo_in_box(s, "s27-mcdonalds-real-source.png", 0.55, 1.60, 3.05, 1.55,
                 pad=0.22)
    ocean_box(s, 0.55, 3.30, 3.05, 2.10, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=0.80, y=3.45, w=2.55, h=0.9, text="0.7%",
             size=40, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    text_box(s, x=0.70, y=4.45, w=2.75, h=0.85,
             text="~100 of ≈13,786 US restaurants",
             size=11.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.1)
    # right: facts
    ocean_box(s, 3.85, 1.60, 8.95, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=4.15, y=1.75, w=8.4, h=0.4, text="McDonald's x IBM — voice order-taking",
             size=14, bold=True, color=MID)
    text_box(s, x=4.15, y=2.30, w=8.4, h=2.2,
             text="• 2.5-3 years piloted on 0.7% of the chain [2]\n\n"
                  "• Viral failures: bacon in ice cream, 9 iced teas "
                  "instead of one\n\n"
                  "• Killed June 2024 — the goal (voice automation) "
                  "stayed, the vendor's approach was killed",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 3.85, 4.80, 8.95, 1.05,
        "Mirror of the previous case: there they skipped the pilot "
        "entirely and shipped to everyone; here the pilot ran long — and "
        "its signal was used correctly, in a disciplined decision to "
        "kill, not scale, the failure.",
        size=12.5, bold=True)
    refs_of_slide(s, "s27")
    notes_with_sources(s, "s27")
    return s
