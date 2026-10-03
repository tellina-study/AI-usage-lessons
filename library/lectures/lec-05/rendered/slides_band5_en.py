"""Lecture 5 (EN) — Band 5 (Section 7 "Synthesis and the decision framework", s50-s55).

EN twin of slides_band5.py: same layout/geometry/palette, English visible
strings + speaker notes sourced from slides-en/sNN*.md.

Issue #212 — revision following the owner's remarks (notes/.../owner-review-2026-09-30).
The density of the visible layer was lowered deliberately: matrix cells were
shortened, the type size raised, abbreviations spelled out in words, direct
address to the audience removed. The requirement "a person must understand at
least something by reading alone" matters more here than structural parity
with Lecture 4.

s50 — Section 7 divider (a compass over the six arrows of the loop).
s51 — the summary matrix, 6 phases x 4 columns.
s53 — the decision instrument: three axes plus a run through two examined cases.
       The former checklist s54 was folded in here — it answered the same
       question, "how to take the decision", and was written as an instruction
       to an executor.
s55 — the closing hero (the bridge to Seminar 7 and Lecture 6) + "Questions?".

NOT PORTED TO EN: s52 (triangulation of three independent pieces of evidence)
and s54 (the 8-question checklist). Both were removed from the deck earlier and
survive in the RU module only as dead code — neither is in ORDER
(rendered/build_lec05_en.py), so neither would ever render. They are absent
here on purpose, not by oversight: an EN twin of a function nobody calls would
be text nobody reviews.

Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.
Timing and methodology commentary are forbidden in the visible layer.
Speaker notes come from slides-en/*.md through notes_with_sources.
"""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    icon, slide_title,
    gold_callout, notes_with_sources,
    build_section_divider,
    photo_in_box,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE,
    GOLD_TINT, MID_TINT,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN


# ============================================================
# Band-local primitives: the dense matrix table.
# _helpers has no table (nobody ever asked it for one), and three slides in a
# row need the same grid — we keep it here so the shared file is left alone
# while another agent is working in it.
# ============================================================
def matrix_header(slide, x, y, widths, labels, *, h=0.40, size=11.0,
                  fill=MID, accent_idx=None, accent_fill=GOLD,
                  accent_color=DEEP, gap=0.06):
    """Matrix header: one row of plates, one column may be gold."""
    cx = x
    for i, (w, lab) in enumerate(zip(widths, labels)):
        acc = (accent_idx is not None and i == accent_idx)
        filled_rect(slide, cx, y, w, h, (accent_fill if acc else fill),
                    radius=True, radius_adj=0.10)
        text_box(slide, x=cx + 0.10, y=y, w=w - 0.20, h=h, text=lab,
                 size=size, bold=True,
                 color=(accent_color if acc else WHITE),
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.98)
        cx += w + gap
    return y + h


def matrix_row(slide, x, y, widths, cells, *, h=0.70, size=10.0,
               accent_idx=None, stroke=LIGHT, fill=SURFACE,
               accent_stroke=GOLD, accent_fill=GOLD_TINT, gap=0.06,
               first_bold=True, first_size=11.0, first_icon=None,
               row_fill=None, row_stroke=None, pad=0.14):
    """One matrix row. The first cell is the "axis" (heavier, may carry an
    icon), the rest are content. accent_idx paints one column gold."""
    cx = x
    for i, (w, txt) in enumerate(zip(widths, cells)):
        acc = (accent_idx is not None and i == accent_idx)
        f = accent_fill if acc else (row_fill or fill)
        st = accent_stroke if acc else (row_stroke or stroke)
        filled_rect(slide, cx, y, w, h, f, stroke=st,
                    stroke_pt=(1.5 if acc else 1.0), radius=True,
                    radius_adj=0.07)
        tx, tw = cx + pad, w - 2 * pad
        if i == 0 and first_icon:
            icon(slide, first_icon, cx + pad, y + (h - 0.30) / 2, 0.30, "mid")
            tx, tw = cx + pad + 0.38, w - pad - 0.38 - 0.08
        if i == 0 and "\n" in txt:
            # "Name\nlevel qualifier" — the second line is muted and smaller
            name, sub = txt.split("\n", 1)
            text_box(slide, x=tx, y=y + 0.08, w=tw, h=h * 0.46, text=name,
                     size=first_size, bold=True, color=DEEP,
                     anchor=MSO_ANCHOR.BOTTOM, line_spacing=1.08)
            text_box(slide, x=tx, y=y + h * 0.58, w=tw, h=h * 0.38, text=sub,
                     size=first_size - 2.0, italic=True, color=SLATE,
                     anchor=MSO_ANCHOR.TOP, line_spacing=1.05)
        else:
            text_box(slide, x=tx, y=y + 0.05, w=tw, h=h - 0.10, text=txt,
                     size=(first_size if i == 0 else size),
                     bold=(first_bold if i == 0 else False),
                     color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
        cx += w + gap
    return y + h


# ============================================================
# s50 — Section 7 divider
# ============================================================

def s50(p):
    """Section 7 divider.

    REVISION #212 (student-roast 2026-09-30, revision 5): the right-hand hero
    here used to be a bespoke diagram — a compass inside a ring of six arrows
    labelled with the phase names. A student read it as empty: "pretty, but it
    carries nothing: I already know there are six phases." He is right — the
    diagram retold what the viewer had already seen on the five preceding
    dividers and on the section ribbon along the bottom, so it said nothing at
    all. Removed entirely; the divider was brought back to the deck's common
    form (a giant section digit plus one emblem icon) that the other six are
    built in.
    """
    return build_section_divider(
        p, here_idx=7,
        subtitle="Synthesis: one instrument\nfor all six phases",
        bridge="The six phases were examined one at a time, and a task "
               "arrives whole — nobody will break it down for you along the "
               "lecture's sections. Without a common instrument you are left "
               "with six separate conclusions and no answer for a case that "
               "was not covered here.",
        sid="s50", tag="6 phases · 1 matrix · 3 decision axes",
        icon_name="compass",
    )


# ============================================================
# s51 — the summary matrix: 6 phases x 4 columns
# ============================================================

def s51(p):
    """The summary matrix of the six phases. The requirement on this slide is
    that it read without the lecturer, so the cells are short, the type size is
    11 pt, abbreviations are spelled out in words, and the figures stayed in
    their own sections: the table holds the structure.

    REVISION #212, owner remark 4 ("slide 52 — run a review after all the
    revisions"). Every row was checked against the actual content of its
    section after the parallel sessions' revisions; six discrepancies were
    found:

      1. Discovery / what AI made cheaper — s10 names THREE steps (desk
         research, running conversations and bringing them together), the cell
         had two.
      2. Design / what AI made cheaper — it read "a draft screen: a day →
         minutes", and that DIRECTLY CONTRADICTED s17: a measurement with a
         control group gives about a 20% reduction in time, and that slide
         calls the phrase "a day turns into minutes" an overstatement. The
         table was refuting its own section.
      3. Design / failure mode — "sameness of solutions" has gone from s18;
         the second limitation there is now non-determinism.
      4. Design / where a human is mandatory — "safety audit" was replaced
         with a check that can stop the release: s17a introduces it as the
         third layer.
      5. Support / what AI made cheaper — "speed of observation" belonged to
         the removed s38; the current s38a measures the suggestion assistant
         given to the operator.
      6. Governance / what AI made cheaper — "diagnosing the operating model"
         belonged to s46 before it was reworked under remark 3. The cell now
         carries an honest "nothing": fitting a plausible phrase into it for
         the sake of the table's symmetry would mean lying.

    Two figures are kept in the table together with their basis of comparison
    (−20% against the control group, +15% from a baseline of 2.1 resolutions
    per hour) — both refute a common expectation, and without them the row
    reads softer than its section."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Six phases, one structure: discipline, what got cheaper, failure "
           "mode, the human",
        size=18, w=12.3, h=0.52, y=0.28)

    x0, gap = 0.55, 0.06
    widths = [2.10, 2.70, 2.25, 2.50, 2.46]      # sum + 4 gaps = 12.25
    heads = ["Phase", "Leading discipline", "What AI made cheaper",
             "Failure mode", "Where a human is mandatory"]
    y = matrix_header(s, x0, 0.98, widths, heads, h=0.42, size=11.0,
                      accent_idx=4, gap=gap)

    rows = [
        ("search", "Discovery",
         "Customer Development and \"The Mom Test\": a testable hypothesis",
         "Desk research, running conversations and bringing them together",
         "Sycophancy: a synthetic source will not say no",
         "A check against a real past and a real commitment"),
        ("pencil", "Design",
         "Double Diamond, Nielsen's heuristics, the design system",
         "Screen variants: −20% of the time against the baseline",
         "Accessibility gaps; one prompt gives different answers",
         "Convergence onto the context; a check that can stop the release"),
        ("hammer", "Build and launch",
         "Minimum viable product; the stop gate",
         "The build itself: boilerplate and glue code",
         "A gate skipped; rollout to the whole audience at once",
         "Specifying the intent; the decision on pace and on stopping"),
        ("gauge", "Measurement",
         "Controlled experiment; the guardrail metric",
         "Judging quality at scale; a cheap first pass",
         "A gamed proxy metric; the measurement does not transfer to the task",
         "The criterion and the guardrail metric named before the test"),
        ("server", "Support",
         "Reliability engineering: service level objective, error budget",
         "A suggester for the agent: +15% resolutions per hour, base 2.1",
         "Silent drift is masked by the average across all answers",
         "A system model and accountability for every answer"),
        ("scale", "Governance",
         "Portfolio governance; every number has an owner",
         "Nothing: here AI adds a cost that grows with scale",
         "Statistics with no denominator",
         "The success criterion agreed in advance; your own baseline"),
    ]
    for ic, *cells in rows:
        y = matrix_row(s, x0, y + 0.05, widths, cells, h=0.72, size=11.0,
                       accent_idx=4, gap=gap, first_icon=ic, first_size=11.0)

    gold_callout(
        s, 0.55, y + 0.22, 12.25, 0.80,
        "How to read it: name the phase your task is in — the row answers, in "
        "order, which discipline to hold, what AI helps with here, which "
        "failure to watch for and what stays with the human. Tool names are "
        "replaceable; the four columns rest on the nature of the difficulty "
        "and the cost of an error in the phase.",
        size=11.5, bold=True)
    notes_with_sources(s, "s51")
    return s


# ============================================================
# s53 — the decision instrument: three axes + a run through two cases
# ============================================================

def s53(p):
    """The decision instrument — three axes. REVISION #212, owner remark 5:
    "slide 53 — shorten and simplify. it has to be made beautiful, not
    oversaturated as it is now".

    There were eight blocks: a two-line title, the band with the question that
    comes before the axes, the caption of the axes diagram, three cards with
    insets, the gold rule, the caption of the run-through, the two-case
    run-through table (5 columns x 2 dense rows) and the closing teal panel.
    Four were taken off: both diagram captions, the run-through table and the
    teal panel, whose content was condensed into the gold rule. Four blocks
    remain, the cards became twice as large and airier, and the bottom third of
    the slide is left empty on purpose — the slide is a final one and has to be
    memorable rather than read out.

    The run through Google AI Overviews / Zillow Offers was moved entirely into
    the speaker notes, with the same figures and the same basis of comparison;
    the analyses themselves stand in full on s26 and s40.

    The question that comes before the three axes is kept: it was restored
    after the roast of 2026-09-30, it is asked before the axes and it answers
    "is there anything here to amplify at all". The wording comes from
    chapter-part5.md §7.4, item 1."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Three axes decide if the human can come off the gate",
                size=26, w=12.25, h=0.60, y=0.30)

    # -- the question asked before all three axes (chapter-part5.md §7.4) --
    ocean_box(s, 0.55, 1.12, 12.25, 0.54, fill=MID_TINT, stroke=MID,
              stroke_pt=1.6)
    text_runs(s, 0.80, 1.12, 11.75, 0.54, [
        {"text": "Before all three comes the question of the phase's "
                 "classical discipline: ",
         "size": 11.5, "bold": True, "color": DEEP},
        {"text": "if it is absent, you build it first — there is nothing to "
                 "amplify in a vacuum.",
         "size": 11.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)

    # -- three large axis cards --
    axes = [
        ("rotate-ccw", "Reversibility", TEAL,
         "How easily the consequence can be rolled back if the output is "
         "wrong",
         "Low → a staged rollout and a tested rollback path"),
        ("banknote", "Cost of an error", MID,
         "What an error will cost: money, reputation, health",
         "High → a named owner for the decision"),
        ("eye", "Observability", LIGHT,
         "How quickly it shows that an output is wrong",
         "Low → the eval loop and a guardrail metric"),
    ]
    cw, cgap, cy0, ch = 3.91, 0.26, 1.96, 3.56
    for i, (ic, name, col, body, need) in enumerate(axes):
        x = 0.55 + i * (cw + cgap)
        ocean_box(s, x, cy0, cw, ch, fill=SURFACE, stroke=col, stroke_pt=1.8)
        icon(s, ic, x + (cw - 0.78) / 2, cy0 + 0.26, 0.78, "mid")
        text_box(s, x=x + 0.20, y=cy0 + 1.16, w=cw - 0.40, h=0.48, text=name,
                 size=19, bold=True, color=col, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        text_box(s, x=x + 0.28, y=cy0 + 1.74, w=cw - 0.56, h=0.78, text=body,
                 size=12.0, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.TOP, line_spacing=1.16)
        filled_rect(s, x + 0.24, cy0 + 2.62, cw - 0.48, 0.76, GOLD_TINT,
                    stroke=GOLD, stroke_pt=1.2, radius=True, radius_adj=0.12)
        text_box(s, x=x + 0.34, y=cy0 + 2.62, w=cw - 0.68, h=0.76, text=need,
                 size=11.0, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)

    # -- one rule: the removed teal panel was condensed into this --
    gold_callout(
        s, 0.55, 5.72, 12.25, 0.90,
        "No axis forbids AI — each one names what must stand beside it. All "
        "three in a good position and the human can come off the gate; any "
        "other combination calls for a gate on the problem axis.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    notes_with_sources(s, "s53")
    return s


# ============================================================
# s55 — the closing hero: bridge to Seminar 7 and Lecture 6 + "Questions?"
# ============================================================

def s55(p):
    """Hero >=40% of the area, a real image (6-tier acquisition, Tier 2 —
    Wikimedia Commons, public domain): an engineer at a computer-aided design
    (CAD) workstation with a light pen, Hughes Aircraft, late 1970s. Double
    duty: the bridge to Lecture 6 (engineering design) and the slide's
    load-bearing thought itself — the workstation, the pen and the company are
    gone, the discipline remained.
    Source and licence: assets/screenshots/s55-cad-real-source.png.url.
    A 3:2 crop — the image is 7.83x5.22 inches, about 41% of the slide area."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The method transfers, the list of tools does not: code was the "
           "first proving ground, the product the second",
        size=18, w=12.3, h=0.78, y=0.18)

    photo_in_box(s, "s55-cad-crop.png", 0.55, 1.04, 8.30, 5.42, pad=0.10)
    text_box(s, x=0.62, y=6.50, w=7.90, h=0.48,
             text="An engineer at a computer-aided design (CAD) workstation "
                  "with a light pen, late 1970s: the tool is gone — the "
                  "discipline of design remained",
             size=10, italic=True, color=SLATE, line_spacing=1.08)

    rx, rw = 8.68, 4.12
    gold_callout(
        s, rx, 1.04, rw, 1.38,
        "This course does not teach \"use AI more\" and it does not teach "
        "\"fear AI\" — it teaches you to say a well-founded \"yes\" and a "
        "well-founded \"no.\"",
        size=13, bold=True)

    cards = [
        ("Seminar 7", TEAL,
         "A full run of the instrument on a practice AI product: from the "
         "hypothesis to the point of escalation to a human."),
        ("Lecture 6", MID,
         "The same method in computer-aided design (CAD): the cost of a "
         "physical error is higher."),
    ]
    cy = 2.60
    for name, col, body in cards:
        ocean_box(s, rx, cy, rw, 1.32, fill=SURFACE, stroke=col, stroke_pt=1.6)
        text_box(s, x=rx + 0.22, y=cy + 0.13, w=rw - 0.44, h=0.30, text=name,
                 size=14, bold=True, color=col)
        text_box(s, x=rx + 0.22, y=cy + 0.49, w=rw - 0.44, h=0.78, text=body,
                 size=11.5, color=DEEP, line_spacing=1.16)
        cy += 1.32 + 0.18

    filled_rect(s, rx, 5.62, rw, 0.84, GOLD, radius=True, radius_adj=0.14)
    text_box(s, x=rx, y=5.62, w=rw, h=0.84, text="Questions?", size=24,
             bold=True, color=DEEP, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    notes_with_sources(s, "s55")
    return s
