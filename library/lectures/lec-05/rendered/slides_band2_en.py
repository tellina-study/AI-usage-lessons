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
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, CHARTS,
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


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
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


def s14a(p):
    """ISSUE #212 (owner remark R3-2026-10-01): "in the design section we
    need a slide and the caveats that this is not only about interface
    design". The slide opens the section right after the divider and before
    the base slide: the scope of the word, six surfaces of contact, three
    decisions about the system's behaviour over time. The gold panel works as
    the run-up to the section's failure — the product's name sets the picture
    of the system in a person's head before the first screen does. The caveat
    is continued on s15, s17, s17a and s18, so that it does not stand
    alone."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Design here is the whole of a person's work with the "
                   "system: surfaces and touchpoints, behaviour, the answer "
                   "when unsure",
                size=22, y=0.13, w=12.25, h=0.86)

    # -- the scope of the word --
    filled_rect(s, 0.55, 1.05, 12.25, 1.04, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.6, radius=True, radius_adj=0.08)
    icon(s, "compass", 0.78, 1.38, 0.40, "teal")
    text_runs(s, 1.36, 1.09, 11.30, 0.96, [
        {"text": "THE SCOPE OF THE WORD   ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "The screen is one of the surfaces on which a person meets "
                 "the system. Design in this phase settles the whole make-up "
                 "of that meeting: where the system comes across a person, "
                 "how it behaves over time, and what it does in the minute "
                 "when it is unsure of its own answer. In a product built on "
                 "a language model, there is usually more work on the other "
                 "surfaces than there is on the screen.",
         "size": 11, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14)

    # -- six surfaces and touchpoints --
    text_box(s, x=0.55, y=2.18, w=12.25, h=0.26,
             text="Surfaces and touchpoints", size=12, bold=True,
             color=MID, line_spacing=1.0)
    tiles = [
        ("monitor-smartphone", "Screen",
         "what a person sees, and in what order", MID),
        ("headphones", "Voice",
         "the same decision with no picture: order, length, the right to "
         "interrupt", MID),
        ("siren", "Notification",
         "the system opens the conversation itself: when, and on what "
         "occasion", TEAL),
        ("file-text", "Email, report",
         "the answer read when the system is nowhere at hand", MID),
        ("shield-off", "Refusal",
         "what the system says when it will not do the thing", TEAL),
        ("clock", "Silence",
         "processing is running, there is no answer yet: what a person sees "
         "for that minute",
         TEAL),
    ]
    tw = (12.25 - 2 * 0.16) / 3.0
    for i, (icn, name, body, col) in enumerate(tiles):
        tx = 0.55 + (i % 3) * (tw + 0.16)
        ty = 2.48 + (i // 3) * (0.82 + 0.10)
        ocean_box(s, tx, ty, tw, 0.82, fill=SURFACE, stroke=col,
                  stroke_pt=1.4)
        icon(s, icn, tx + 0.16, ty + 0.11, 0.28,
             "teal" if col is TEAL else "mid")
        text_box(s, x=tx + 0.54, y=ty + 0.09, w=tw - 0.70, h=0.28,
                 text=name, size=11, bold=True, color=col, line_spacing=1.0)
        text_box(s, x=tx + 0.18, y=ty + 0.42, w=tw - 0.36, h=0.36,
                 text=body, size=9.5, color=DEEP, line_spacing=1.12)

    # -- the system's behaviour over time --
    text_box(s, x=0.55, y=4.52, w=12.25, h=0.26,
             text="The system's behaviour over time", size=12, bold=True,
             color=MID, line_spacing=1.0)
    behav = [("circle-check", "Sure",
              "it answers and shows what the answer is built on", MID),
             ("circle-help", "Unsure",
              "it says so in the first person and offers a move forward",
              TEAL),
             ("undo-2", "Wrong",
              "the person sees what happened, and has a rollback path",
              TEAL)]
    for i, (icn, name, body, col) in enumerate(behav):
        bx = 0.55 + i * (tw + 0.16)
        ocean_box(s, bx, 4.82, tw, 0.84, fill=WHITE, stroke=col,
                  stroke_pt=1.6)
        icon(s, icn, bx + 0.16, 4.92, 0.28,
             "teal" if col is TEAL else "mid")
        text_box(s, x=bx + 0.54, y=4.90, w=tw - 0.70, h=0.28, text=name,
                 size=11, bold=True, color=col, line_spacing=1.0)
        text_box(s, x=bx + 0.18, y=5.22, w=tw - 0.36, h=0.36, text=body,
                 size=9.5, color=DEEP, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.80, 12.25, 0.92,
        "Decisions in this layer are taken once, and they outlive any "
        "layout: the product's name, the promise at the entrance, the right "
        "to stop. The name sets the picture of the system in a person's head "
        "before they see the first screen — and correcting that picture "
        "costs a recall of the entire fleet.",
        size=12.5, bold=True)
    notes_with_sources(s, "s14a")
    return s


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


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: superseded base — heuristics / the design system moved into s15 and s17a (issue #212).
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
    """EN twin of the rewritten RU s17. Owner remark R6 (#212): the tool
    list and the time-saving estimate are brought to 2026, and instead of a
    list of capabilities the slide shows a "with AI and without"
    comparison — a randomised trial with a control group, not a vendor
    promise. The title is a way in for a newcomer, not a formula for people
    who already know it (R8-6)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Interface generators: machine gives options, "
                   "human picks and refines",
                size=22, y=0.13, w=12.25, h=0.80)

    # ── left: what the machine actually does ──
    # FIX #212 (student-roast 2026-09-30, fix 5): four IDENTICAL monitor
    # icons used to stand here, captioned "sketch 1–4" — the student called
    # them meaningless, and was right: the slide's claim is that the machine
    # produces UNLIKE variants of one screen, and four copies of one picture
    # said the opposite. They are now four different layout schemes.
    ocean_box(s, 0.55, 1.02, 6.25, 2.60, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_box(s, x=0.78, y=1.06, w=5.80, h=0.50,
             text="What the machine does itself: four different layouts "
                  "of one screen in minutes",
             size=12.5, bold=True, color=MID, line_spacing=1.04)

    def wire(x, y, w, h, kind):
        """A miniature screen-layout scheme — different for each variant."""
        filled_rect(s, x, y, w, h, WHITE, stroke=LIGHT, stroke_pt=1.2,
                    radius=True, radius_adj=0.10)
        px, py = x + 0.11, y + 0.11
        iw, ih = w - 0.22, h - 0.22
        bar = 0.075
        if kind == "hero":          # header + a large block + two captions
            filled_rect(s, px, py, iw, bar, MID, radius=True, radius_adj=0.30)
            filled_rect(s, px, py + bar + 0.05, iw, ih - bar * 2 - 0.14,
                        SOFT_GREY)
            filled_rect(s, px, py + ih - bar, iw * 0.55, bar, SOFT_GREY,
                        radius=True, radius_adj=0.30)
        elif kind == "list":        # header + a list of rows
            filled_rect(s, px, py, iw, bar, MID, radius=True, radius_adj=0.30)
            for k in range(3):
                filled_rect(s, px, py + bar + 0.06 + k * 0.115,
                            iw * (1.0 - 0.14 * k), bar, SOFT_GREY,
                            radius=True, radius_adj=0.30)
        elif kind == "sidebar":     # a side panel + content
            filled_rect(s, px, py, iw * 0.30, ih, MID)
            filled_rect(s, px + iw * 0.36, py, iw * 0.64, ih * 0.44,
                        SOFT_GREY)
            filled_rect(s, px + iw * 0.36, py + ih * 0.52, iw * 0.64,
                        ih * 0.48, SOFT_GREY)
        else:                       # 2x2 tiles
            for r in range(2):
                for c in range(2):
                    filled_rect(s, px + c * (iw * 0.54), py + r * (ih * 0.54),
                                iw * 0.46, ih * 0.46,
                                (MID if (r + c) == 0 else SOFT_GREY))

    kinds = ["hero", "list", "sidebar", "tiles"]
    for i, kind in enumerate(kinds):
        x = 0.78 + i * 1.45
        wire(x, 1.60, 1.36, 0.84, kind)
        text_box(s, x=x, y=2.46, w=1.36, h=0.24,
                 text=f"option {i + 1}", size=9.5, color=SLATE,
                 align=PP_ALIGN.CENTER)
    filled_rect(s, 0.78, 2.76, 5.78, 0.80, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.5, radius=True, radius_adj=0.10)
    text_box(s, x=0.96, y=2.78, w=5.42, h=0.76,
             text="Then the human: picks one direction, discards the rest "
                  "and fixes what the model got wrong — spacing, order of "
                  "importance, edge cases.",
             size=11, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.16)

    # ── right: the 2026 tools ──
    ocean_box(s, 7.05, 1.02, 5.75, 2.60, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=7.28, y=1.10, w=5.30, h=0.28,
             text="The tools of 2026 [1]", size=12.5, bold=True, color=TEAL)
    tools = [
        ("Figma Make", " — builds screens inside the design editor from the "
                       "team's own components, not generic templates."),
        ("Google Stitch", " — text and sketches into a screen; free, and "
                          "since March 2026 it imports Figma files and "
                          "emits code [2]."),
        ("v0", " — a description straight into interface code."),
        ("Lovable, bolt.new", " — a description straight into a whole "
                             "working app."),
        ("Magic Patterns", " — fast sweep over variants of one screen."),
    ]
    runs = []
    for k, (name, tail) in enumerate(tools):
        runs.append({"text": name, "size": 10.5, "bold": True, "color": DEEP,
                     "newpara": k > 0, "space_before": 3})
        runs.append({"text": tail, "size": 10.5, "color": DEEP})
    text_runs(s, 7.28, 1.44, 5.30, 2.06, runs, line_spacing=1.14)

    # ── bottom: "with AI and without" by an actual measurement (R6) ──
    ocean_box(s, 0.55, 3.70, 12.25, 2.18, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.5)
    text_box(s, x=0.80, y=3.78, w=11.75, h=0.28,
             text="With a generator and without: measured, not promised [3]",
             size=12.5, bold=True, color=DEEP)
    text_runs(s, 0.80, 4.12, 5.55, 0.90, [
        {"text": "How it was measured. ", "size": 11, "bold": True,
         "color": MID},
        {"text": "A hundred participants — fifty designers and fifty "
                 "product managers — randomly split into two groups: one "
                 "got a generator, the other did not. Three identical "
                 "interface-editing tasks, September 2026.",
         "size": 11, "color": DEEP},
    ], line_spacing=1.16)
    text_runs(s, 6.98, 4.12, 5.57, 0.90, [
        {"text": "What came out. ", "size": 11, "bold": True, "color": TEAL},
        {"text": "Overall time fell by about 20%. For product managers the "
                 "gain is 35%. For professional designers — only on the "
                 "hardest of the three tasks (26%), and their overall "
                 "effect is borderline (17%).",
         "size": 11, "color": DEEP},
    ], line_spacing=1.16)
    text_box(s, x=0.80, y=5.08, w=11.75, h=0.70,
             text="The measurement does not bear out the promise that "
                  "\"a day of manual wireframing turns into minutes\": the "
                  "gain is real, but it runs in tens of percent and depends "
                  "on who works and how hard the task is. Figma ran the "
                  "trial on its own tool — keep that in mind.",
             size=11, italic=True, color=SLATE, line_spacing=1.16)

    # FIX #212 (R3-2026-10-01): the second sentence continues the caveat
    # from the design-scope slide (s14a): the generator covers the screen.
    gold_callout(
        s, 0.55, 5.94, 12.25, 0.94,
        "The machine widens the set of options. Narrowing to one is a "
        "decision about your users and your constraints, which the "
        "training data does not hold. The generator covers the screen; "
        "surfaces and touchpoints, system behaviour and the answer under "
        "uncertainty stay human.",
        size=12.5, bold=True)
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
    """ISSUE #212 (owner remark R2-2026-10-01): Character.AI used to stand
    here — a case whose root lies in an absent safety requirement, and in the
    section on interaction design it was standing in the wrong place. In its
    place goes a case where interaction design itself is what failed: the
    system's behaviour, its warnings, and the picture of the system in a
    person's head. The choice rests on the wording in the manufacturer's own
    defect report and on the fact that the remedy lay entirely in this layer
    — the prominence of the warnings and the strictness of the attention
    checks, with no changes to the driving model. The abbreviation NHTSA is
    expanded at its first appearance (R5)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "All 2,031,220 cars with the driver-assistance feature "
                   "recalled: the prominence of the controls was found "
                   "insufficient",
                size=21, y=0.13, w=12.30, h=0.80)

    # -- 1. WHAT THE CASE IS — description before analysis (R9) --
    ocean_box(s, 0.55, 0.97, 12.25, 1.90, fill=SURFACE, stroke=MID,
              stroke_pt=1.4)
    photo_in_box(s, "s19-tesla-real-source.png", 0.70, 1.34, 2.02, 0.84,
                 pad=0.10)
    text_box(s, x=0.70, y=2.24, w=2.02, h=0.44,
             text="driver-assistance\nfeatures", size=9.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)
    text_box(s, x=2.94, y=1.03, w=9.64, h=0.26,
             text="What the case is", size=12, bold=True, color=MID)
    text_runs(s, 2.94, 1.31, 9.64, 1.50, [
        {"text": "Autopilot ", "size": 10.5, "bold": True, "color": DEEP},
        {"text": "is the set of driver-assistance features in Tesla cars: "
                 "it holds the lane, the speed and the following distance "
                 "while the person watches the road and keeps their hands "
                 "on the wheel.", "size": 10.5,
         "color": DEEP},
        {"text": "On 13 August 2021 the National Highway Traffic Safety "
                 "Administration (NHTSA) opened an investigation: cars with "
                 "Autopilot engaged were running into emergency vehicles "
                 "stopped on the road. On 12 December 2023 Tesla recalled "
                 "all 2,031,220 cars carrying the feature — the entire fleet "
                 "built since 2012. In the defect report the company wrote, "
                 "in its own words, that the prominence and scope of the "
                 "system's controls may be insufficient to prevent driver "
                 "misuse.",
         "size": 10.5, "color": DEEP, "newpara": True, "space_before": 4},
    ], line_spacing=1.14)

    # -- 2. HOW IT RAN IN TIME --
    ocean_box(s, 0.55, 2.93, 12.25, 0.72, fill=WHITE, stroke=LIGHT,
              stroke_pt=1.4)
    stages = [("Investigation\n08.2021", False),
              ("Recall of 2,031,220 cars\n12.12.2023", True),
              ("Over-the-air update\n12.2023", False),
              ("Recall query\n25.04.2024", False),
              ("≥20 crashes\nafter the update", False)]
    xs = [1.55, 4.05, 6.60, 9.15, 11.65]
    for i, ((lbl, hot), x) in enumerate(zip(stages, xs)):
        col = GOLD if hot else LIGHT
        circle(s, x - 0.11, 3.05, 0.22, col, stroke=WHITE, stroke_pt=1.5)
        text_box(s, x=x - 1.15, y=3.32, w=2.30, h=0.28, text=lbl, size=8.5,
                 bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=0.95)
        if i < len(xs) - 1:
            connector(s, x + 0.11, 3.16, xs[i + 1] - 0.11, 3.16,
                      color=SOFT_GREY, width=2.0)

    # -- 3. WHAT BROKE / WHY THIS IS THE DESIGN PHASE --
    cw_ = 6.05
    for x_, head_, col, icn, runs in [
        (0.55, "What broke", MID, "eye-off", [
            {"text": "Over the course of the investigation, from August "
                     "2021 to December 2023, at least 13 fatal crashes "
                     "accumulated in which foreseeable misuse played its "
                     "part.", "size": 10, "color": DEEP},
            {"text": "The driver's picture of the system diverged from what "
                     "the system was doing. The name of this error is ",
             "size": 10, "color": DEEP, "newpara": True, "space_before": 4},
            {"text": "mode confusion", "size": 10, "bold": True,
             "color": MID},
            {"text": ".", "size": 10, "color": DEEP},
        ]),
        (6.75, "Why this is a design-phase decision", TEAL, "layers", [
            {"text": "The recall touched not one line of the driving model. "
                     "What was fixed was how the system presents itself: the "
                     "prominence of the warnings, the frequency of the "
                     "attention checks, the threshold past which the feature "
                     "switches off.", "size": 10,
             "color": DEEP},
            {"text": "The name \"Autopilot\" is a decision from the same "
                     "layer: it sets the picture before the first warning "
                     "does.", "size": 10,
             "color": DEEP, "newpara": True, "space_before": 4},
        ]),
    ]:
        ocean_box(s, x_, 3.71, cw_, 1.58, fill=SURFACE, stroke=col,
                  stroke_pt=1.5)
        icon(s, icn, x_ + 0.22, 3.82, 0.32, "teal" if col is TEAL else "mid")
        text_box(s, x=x_ + 0.64, y=3.82, w=cw_ - 0.88, h=0.30, text=head_,
                 size=11.5, bold=True, color=col, line_spacing=1.0)
        text_runs(s, x_ + 0.22, 4.16, cw_ - 0.44, 1.04, runs,
                  line_spacing=1.12)

    # -- 4. ANALYSIS --
    gold_callout(
        s, 0.55, 5.35, 12.25, 0.82,
        "The root is a decision about how the system presents itself to a "
        "person: what it reports, how insistently, and when it refuses to "
        "go on. Two years and four months passed between the opening of "
        "the investigation and the recall, and all that time the fleet drove "
        "with the picture it was given. Testing the model does not catch "
        "this: it behaved exactly as advertised.",
        size=12, bold=True)

    # -- 5. THE CRITERION THAT CARRIES FORWARD --
    teal_callout(
        s, 0.55, 6.23, 12.25, 0.76,
        "The agency opened its query into the remedy on 25 April 2024: in "
        "the first four months after the update, at least 20 crashes "
        "accumulated with the system suspected of involvement, and some of "
        "the measures are switched on by the driver's own consent and "
        "switched off the same way. The criterion that carries forward: a "
        "measure a person can switch off stays a request — what turns it "
        "into a mechanism is the ability to stop the action.",
        size=10.5, bold=False)
    refs_of_slide(s, "s19")
    notes_with_sources(s, "s19")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: superseded failure — iTutorGroup now runs as a neighbouring class on s18 (issue #212).
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


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
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
    """EN PARITY, issue #212 — re-synchronised with the RU slide as rebuilt in
    Stage 6. The EN twin still carried "+200% code per engineer — but only 16%
    of PRs got substantive review": a two-bar chart plus a three-bullet
    Anthropic list. Three things the RU side had already fixed:

    R6 — the figures are the 2026 data (Faros AI, LinearB) and the slide is a
    comparison of the key practices without AI and with it, not a list of
    facts.

    Fact-check 2026-09-30 — the Anthropic figures belong to the post Code
    Review for Claude Code (9 March 2026), not to the Agentic Coding Trends
    Report; the 16% is unfolded into "16% before -> 54% after", because alone
    it asserted the opposite of what the source says; the Faros metric is
    "time in review", not "time waiting for review" (waiting is +157%).

    owner-review 2026-10-01, cross-check with Lecture 4 — the title called
    review the ONLY bottleneck where L4 §1.3 named precision of intent at the
    input first (hence "adds to"); the test row was silent about L4 §4.1/§4.3
    (executable specification + deterministic run gate, mutation score more
    honest than coverage); there was no warning from L4 §3.7/§5.2 that
    handing the merge to an agent removes the only control."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Code got cheap to write, not to check: review adds to "
                   "the bottleneck at the input",
                size=22, y=0.13, h=0.82, w=12.3)

    # -- left: the measured shift --
    ocean_box(s, 0.55, 1.02, 4.60, 4.72, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.78, y=1.12, w=4.15, h=0.30, text="MEASURED SHIFT",
             size=11.5, bold=True, color=MID)
    stats = [
        ("+200%", "code per engineer in a year — Anthropic's own "
                  "measurement", GOLD),
        ("16% \u2192 54%", "share of changes with substantive review before "
                           "merge: before \u2014 after, once the first pass "
                           "went to automation; nearly half still merges "
                           "without one [1]", DEEP),
        ("+441%", "median time a change spends in review — telemetry from "
                  "22,000 developers, Faros AI", DEEP),
        ("2.5\u00d7 / 5\u00d7", "AI changes are larger and wait longer for a "
                                "reviewer — 8.1M pull requests, LinearB",
         DEEP),
    ]
    yy = 1.48
    for num, txt, col in stats:
        text_box(s, x=0.78, y=yy, w=4.15, h=0.42, text=num, size=21,
                 bold=True, color=col, line_spacing=1.0)
        text_box(s, x=0.78, y=yy + 0.44, w=4.15, h=0.60, text=txt,
                 size=10.0, color=SLATE, line_spacing=1.14)
        yy += 1.06

    # -- right: the key practices without AI and with it --
    ocean_box(s, 5.35, 1.02, 7.45, 4.72, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.6)
    text_box(s, x=5.58, y=1.12, w=7.00, h=0.30,
             text="PRACTICES: WHAT WAS AND WHAT WAS ADDED",
             size=11.5, bold=True, color=TEAL)
    hx1, hw1 = 5.58, 2.32
    hx2, hw2 = 8.24, 4.34
    text_box(s, x=hx1, y=1.46, w=hw1, h=0.26, text="did and still do, no AI",
             size=9.5, bold=True, italic=True, color=SLATE)
    text_box(s, x=hx2, y=1.46, w=hw2, h=0.26,
             text="added when an agent writes the code",
             size=9.5, bold=True, italic=True, color=TEAL)
    rows = [
        ("Review of changes before merge",
         "it became the bottleneck itself; handing the merge to an agent "
         "removes the only control"),
        ("Feature flag",
         "switches the autonomy level: how much the system decides itself"),
        ("Staged rollout by share of users",
         "rolled out on two axes at once: share of audience and autonomy "
         "level"),
        ("Test as executable specification and a run gate",
         "a mutation-score gate was added: it checks the test can catch a "
         "defect at all"),
        ("Circuit breaker",
         "always needed: a failure spreads faster than anyone notices it"),
        ("A human-owned specification",
         "the one input an agent cannot invent for itself"),
    ]
    ry = 1.78
    for i, (a, b) in enumerate(rows):
        if i % 2 == 0:
            filled_rect(s, 5.50, ry, 7.15, 0.62, MID_TINT)
        text_box(s, x=hx1, y=ry + 0.02, w=hw1, h=0.58, text=a, size=9.8,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
        right_arrow(s, hx1 + hw1 + 0.06, ry + 0.24, 0.14, 0.14, fill=MID)
        text_box(s, x=hx2, y=ry + 0.02, w=hw2, h=0.58, text=b, size=9.8,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
        ry += 0.64

    gold_callout(
        s, 0.55, 5.86, 12.25, 0.78,
        "Scarcity sits at the edges: precision of the task in, speed of "
        "judgment out.",
        size=13.5, bold=True)
    refs_of_slide(s, "s23")
    notes_with_sources(s, "s23")
    return s



# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: absorbed by s24a (the autonomy ladder as a practice card) (issue #212).
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
    """EN twin of slides_band2.py::s27 (issue #212). The builder and the
    source had diverged on the RU side (~37% overlap) and were reconciled;
    the EN twin is brought to the same composition. R9: a short "what
    happened" block before the analysis. The slide stays the payoff of the
    section's base material, not a standalone failure.
    """
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "McDonald's and IBM, 2021–2024: killing a pilot on 0.7% "
                   "of the chain was right",
                size=21, y=0.13, h=0.82, w=12.3)

    # ── what happened ──
    ocean_box(s, 0.55, 1.02, 8.30, 2.46, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.80, y=1.10, w=7.80, h=0.28, text="WHAT HAPPENED",
             size=11.5, bold=True, color=MID)
    text_box(s, x=0.80, y=1.42, w=7.80, h=1.96,
             text="From late 2021 McDonald's and IBM tested voice "
                  "order-taking at the drive-thru window: the customer "
                  "speaks the order straight to the system, past the "
                  "employee. It ran at about 100 restaurants out of nearly "
                  "13,800 in the US — 0.7% of the chain — for two and a "
                  "half years. All that time clips of failures kept "
                  "surfacing: bacon in ice cream, nine iced teas instead of "
                  "one, orders mixed between adjacent lanes. In June 2024 "
                  "the partnership ended. What was killed was the approach; "
                  "the goal stayed — voice automation is still planned.",
             size=11.5, color=DEEP, line_spacing=1.18)

    # ── right: the pilot's scale and length ──
    photo_in_box(s, "s27-mcdonalds-real-source.png", 9.05, 1.02, 3.75, 1.18,
                 pad=0.16)
    ocean_box(s, 9.05, 2.30, 3.75, 1.18, fill=SURFACE, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=9.15, y=2.36, w=3.55, h=0.58, text="0.7%", size=34,
             bold=True, color=GOLD, align=PP_ALIGN.CENTER, line_spacing=1.0)
    text_box(s, x=9.15, y=2.96, w=3.55, h=0.46,
             text="≈100 of ≈13,800 US restaurants · 2.5-year pilot",
             size=10.0, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.10)

    # ── analysis ──
    ocean_box(s, 0.55, 3.58, 12.25, 1.74, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=0.80, y=3.64, w=11.8, h=0.26, text="ANALYSIS", size=11.5,
             bold=True, color=TEAL)
    text_box(s, x=0.80, y=3.94, w=11.8, h=1.30,
             text="• The denominator is mandatory: \"100 restaurants\" "
                  "without \"of 13,800\" reads as a large rollout; with it, "
                  "as a narrow strip deliberately kept narrow\n"
                  "• The ceiling here is plain: speech recognition in noise, "
                  "across accents, with other voices around. More time does "
                  "not move such a ceiling\n"
                  "• A specific technical path was killed; the task stayed. "
                  "Different decisions, and mixing them is costly\n"
                  "• Mirror of the previous case: there the pilot was "
                  "skipped, here it was run honestly and its signal was read",
             size=11.0, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.42, 12.25, 0.94,
        "The signal was read right: a long pilot on a small share still "
        "failing in public means the approach has a ceiling; a data "
        "shortage is not the cause. That is the continue-or-kill gate "
        "working.",
        size=13, bold=True)
    refs_of_slide(s, "s27")
    notes_with_sources(s, "s27")
    return s
