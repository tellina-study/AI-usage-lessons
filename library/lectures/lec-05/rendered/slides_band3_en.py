"""Lecture 5 (EN) — Band 3 (Section 4 Measure s28-s35 + Section 5 Support
s36-s43, plus ELI5 overviews s28b, s36b).

EN twin of slides_band3.py: same layout/geometry/palette, English visible
strings + speaker notes sourced from slides-en/sNN*.md.
Palette Ocean LOCKED, motif "Ocean rounded box", Gold >=1x/slide.
NO timing / NO methodology / NO photo-attribution.
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
# Section 4. Measure / Experiment
# ============================================================
def s28(p):
    return build_section_divider(
        p, here_idx=4,
        subtitle="Measure — the arrow where AI lowered trust",
        bridge="Measurement is where \"looks good\" hits the product "
               "hardest. Many are seeing the formal discipline of a "
               "product experiment for the first time.",
        sid="s28", tag="2 base cases · 2 failures",
        meme_name="s28-woman-yelling-cat.jpg")


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
def s28b(p):
    return eli5_overview(
        p, "s28b", title="Measurement in plain terms", icon_name="ruler",
        cards=[
            ("What it is",
             "The phase where you honestly check: did the change work, "
             "or does it only look like it did. Many people see the "
             "formal discipline of experimentation for the first time."),
            ("Why",
             "\"The metric grew after the release\" proves nothing — it "
             "could have grown on its own. You need a way to separate "
             "cause from coincidence."),
            ("Mental model",
             "Split users into two random groups: one gets the new "
             "thing, the other the old thing. The difference is the "
             "real effect. Agree on the success metric in advance."),
        ])


def s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Randomization tells cause apart from coincidence",
                size=23, w=12.3, h=0.85)
    # two groups split by coin
    ocean_box(s, 0.55, 1.60, 5.35, 3.05, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    circle(s, 2.85, 1.80, 0.55, GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    icon(s, "circle-help", 2.98, 1.93, 0.30, "gold")
    text_box(s, x=1.55, y=2.45, w=3.0, h=0.3, text="random split",
             size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    for j, (lbl, col, xx) in enumerate([("Control", LIGHT, 0.90),
                                        ("Treatment", TEAL, 3.55)]):
        filled_rect(s, xx, 2.85, 1.45, 1.55, SURFACE, stroke=col, stroke_pt=1.6,
                    radius=True, radius_adj=0.08)
        icon(s, "users", xx + 0.45, 3.05, 0.55, "mid" if j == 0 else "teal")
        text_box(s, x=xx, y=3.75, w=1.45, h=0.4, text=lbl, size=12.5, bold=True,
                 color=col, align=PP_ALIGN.CENTER)
    right_arrow(s, 2.55, 3.45, 0.9, 0.28, fill=LIGHT)
    # right: OEC
    ocean_box(s, 6.15, 1.60, 6.65, 3.05, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=6.40, y=1.75, w=6.2, h=0.4,
             text="OEC — the metric agreed on in advance [1]",
             size=13.5, bold=True, color=TEAL, line_spacing=1.05)
    text_box(s, x=6.40, y=2.55, w=6.2, h=1.9,
             text="Controlled experiment (Kohavi): a hypothesis with a "
                  "mechanism → randomization → a sample size fixed in "
                  "advance → a decision.\n\nThe teaching trap: \"time on "
                  "the support site\" — good or bad? The metric's "
                  "direction must be agreed before the test.",
             size=12.5, color=DEEP, line_spacing=1.2)
    gold_callout(
        s, 0.55, 4.85, 12.25, 0.95,
        "Only random group splitting gives causation: the difference "
        "between Control and Treatment is caused by your change, not by "
        "season, advertising, or luck [2].",
        size=13, bold=True)
    refs_of_slide(s, "s29")
    notes_with_sources(s, "s29")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: superseded base — the experiment traps moved into s29 and s30a (issue #212).
def s30(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Three questions catch all eight experiment traps",
                size=22, w=12.3, h=0.85)
    cards = [
        ("before the test", "shield-alert", "Is the test set up correctly?",
         "SRM (sample ratio mismatch) [1] — group shares didn't match the "
         "plan; sample size must be fixed in advance, not adjusted to fit "
         "the result"),
        ("interpretation", "search", "Am I reading the result correctly?",
         "peeking [2] — checking the result too early: 2 peeks ~=2x false "
         "positives, so the decision is made only at the pre-set sample "
         "size"),
        ("the effect", "triangle-alert", "Is the effect itself real?",
         "Twyman's law [3]: a suspiciously nice or unexpected number "
         "usually means a measurement error, not a real effect — recheck "
         "the methodology before celebrating"),
    ]
    cw, gap = 3.95, 0.20
    x0, y0 = 0.55, 1.75
    for i, (grp, ic, head, body) in enumerate(cards):
        x = x0 + i * (cw + gap)
        chip(s, x + 0.24, y0 - 0.32, cw - 0.48, 0.28, grp.upper(),
             fill=TEAL_TINT, color=TEAL, size=9.5)
        ocean_box(s, x, y0, cw, 2.85)
        chip(s, x + 0.24, y0 + 0.20, 0.5, 0.4, str(i + 1), fill=GOLD,
             color=DEEP, size=15)
        icon(s, ic, x + cw - 0.85, y0 + 0.18, 0.55, "mid")
        text_box(s, x=x + 0.24, y=y0 + 0.80, w=cw - 0.48, h=0.65, text=head,
                 size=13.5, bold=True, color=DEEP, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=y0 + 1.45, w=cw - 0.48, h=1.30, text=body,
                 size=10, italic=True, color=SLATE, line_spacing=1.14)
    gold_callout(
        s, 0.55, 4.80, 12.25, 1.15,
        "A/B (measurement) is not the same as a feature flag (rollout): "
        "one tests an effect, the other controls access. And careful with "
        "the legend: the Bing test ~=$100M revenue gain (Kohavi/Thomke, "
        "HBR 2017) is NOT \"the $300M button\" (a separate usability case).",
        size=13, bold=True)
    refs_of_slide(s, "s30")
    notes_with_sources(s, "s30")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: absorbed by s31a (the eval loop as a practice card) (issue #212).
def s31(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "pass@k trends toward 100%, pass^k toward 0%: one probability, a different question",
                size=20, w=12.3, h=0.85)
    # left: ladder
    ocean_box(s, 0.55, 1.60, 5.35, 3.35, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=4.9, h=0.4, text="3 levels of evaluation (Husain)",
             size=13.5, bold=True, color=MID)
    ladder = [
        ("1", "Unit tests — fast, deterministic", LIGHT),
        ("2", "Human + LLM-as-judge", MID),
        ("3", "A/B — only once the product is mature", GOLD),
    ]
    for i, (n, txt, col) in enumerate(ladder):
        y = 2.25 + i * 0.85
        filled_rect(s, 0.80, y, 4.85, 0.70, SURFACE, stroke=col, stroke_pt=1.5,
                    radius=True, radius_adj=0.08)
        chip(s, 0.95, y + 0.18, 0.42, 0.34, n, fill=col, color=WHITE, size=12)
        text_box(s, x=1.50, y=y, w=4.05, h=0.70, text=txt, size=11.5,
                 bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.05)
    # right: real pass@k chart
    ocean_box(s, 6.15, 1.60, 6.65, 3.35, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    add_image(s, CHARTS / "c-passk.png", 6.40, 1.85, 6.15, 2.85,
              preserve_aspect=True)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.90,
        "pass@k = at least 1 success out of k; pass^k = ALL k successful "
        "[1]. Production reliability almost always requires pass^k — "
        "\"unit tests for the agent\", where probabilistic output breaks "
        "the familiar pass/fail.",
        size=13, bold=True)
    refs_of_slide(s, "s31")
    notes_with_sources(s, "s31")
    return s


def s32(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The boat circles the lagoon racking up points — but never finishes",
                size=21, w=12.3, h=0.85)
    ocean_box(s, 0.55, 1.60, 5.85, 3.30, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "repeat", 2.85, 2.00, 1.1, "teal")
    text_box(s, x=0.85, y=3.25, w=5.25, h=1.5,
             text="An RL agent in a boat race scored 20% more points than "
                  "human players — by circling a lagoon collecting "
                  "bonuses, never finishing [1]. It optimized the proxy, "
                  "not the real goal.",
             size=12.5, color=DEEP, line_spacing=1.18)
    ocean_box(s, 6.65, 1.60, 6.15, 3.30, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.90, y=1.75, w=5.65, h=0.9,
             text="Goodhart's law: when a measure becomes a target, it "
                  "ceases to be a good measure.",
             size=14, bold=True, color=DEEP, line_spacing=1.12)
    text_box(s, x=6.90, y=2.85, w=5.65, h=1.9,
             text="Anthropic: a model generalized from sycophancy to "
                  "directly editing its own reward function [2].\n\nWhat "
                  "stays: OEC discipline, guardrail metrics, Twyman's "
                  "law — a suspiciously perfect score is now more likely "
                  "a bug than a breakthrough.",
             size=12, color=DEEP, line_spacing=1.18)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.85,
        "Reward hacking: the model finds a way to \"win\" the proxy "
        "metric without achieving the intended outcome — so a measure "
        "and a target must never be confused.",
        size=13, bold=True)
    refs_of_slide(s, "s32")
    notes_with_sources(s, "s32")
    return s


def s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "All 5 reactions were weighted equally at ×5 — not just \"anger\"",
                size=21, w=12.3, h=0.85)
    # left: "They're The Same Picture" meme
    meme_in_box(s, "s33-same-picture.jpg", 0.55, 1.55, 4.35, 3.05, pad=0.12)
    # right: 5 equal reactions + timeline + real logo
    photo_in_box(s, "s33-facebook-real-source.png", 5.15, 1.55, 2.55, 1.15,
                 pad=0.18)
    ocean_box(s, 7.95, 1.55, 4.85, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=8.20, y=1.62, w=4.35, h=0.95,
             text="Facebook MSI, January 2018: love/haha/wow/sad/angry — "
                  "all ×5 above a like (not just anger) [1].",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    reacts = ["love", "haha", "wow", "sad", "angry"]
    for i, r in enumerate(reacts):
        x = 5.15 + i * 1.56
        filled_rect(s, x, 2.90, 1.42, 0.85, SURFACE, stroke=LIGHT, stroke_pt=1.3,
                    radius=True, radius_adj=0.12)
        text_box(s, x=x, y=2.98, w=1.42, h=0.34, text=r, size=11.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER)
        chip(s, x + 0.46, 3.32, 0.5, 0.32, "×5", fill=GOLD, color=DEEP, size=11)
    gold_callout(
        s, 5.15, 3.95, 7.65, 1.90,
        "An engagement proxy with no misinformation guardrail hid the "
        "harm for ~2 years: an internal guardrail (anger <-> "
        "misinformation correlation) confirmed by 2019, weight zeroed in "
        "September 2019 [2]. Lesson: measure the guardrail metric from "
        "day one, not after the harm has already happened.",
        size=12.5, bold=True)
    refs_of_slide(s, "s33")
    notes_with_sources(s, "s33")
    return s


def s34(p):
    """issue #212, R9: both cases described first, the analysis after.
    R5: MedQA and MMLU expanded. R6: the 2026 state of benchmarks added."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A benchmark score is evidence only of its own format",
                size=23, w=12.3, h=0.78)
    text_box(s, x=0.58, y=1.06, w=12.20, h=0.26,
             text="A benchmark is a standard set of tasks on which models "
                  "are compared", size=10.5, italic=True, color=SLATE)

    # ── CASE 1. MEDICINE ──
    ocean_box(s, 0.55, 1.42, 6.05, 3.28, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_box(s, x=0.80, y=1.50, w=5.55, h=0.28, text="CASE 1. MEDICINE",
             size=11, bold=True, color=MID, line_spacing=1.0)
    chip(s, 0.80, 1.84, 2.95, 0.46, "86.5% on MedQA", fill=GOLD, color=DEEP,
         size=14)
    text_box(s, x=0.80, y=2.44, w=5.55, h=2.14,
             text="2023. Google shows Med-PaLM 2, a model for medical "
                  "questions. On MedQA (questions in the format of a "
                  "medical licensing exam, with four ready answer choices) "
                  "it scores 86.5% and makes headlines as \"doctor-level "
                  "AI\". Meanwhile Google's own researchers separately "
                  "build a harder set of 240 adversarial questions — an "
                  "exam with ready choices does not surface clinical-safety "
                  "failures in open dialogue, where the patient offers no "
                  "choices.",
             size=11.5, color=DEEP, line_spacing=1.16)

    # ── CASE 2. LAW ──
    ocean_box(s, 6.75, 1.42, 6.05, 3.28, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=7.00, y=1.50, w=5.55, h=0.28, text="CASE 2. LAW",
             size=11, bold=True, color=TEAL, line_spacing=1.0)
    for i, (lbl, val, col) in enumerate([("Lexis+", "17%", MID),
                                         ("Westlaw", "33%", TEAL)]):
        x = 7.00 + i * 2.85
        filled_rect(s, x, 1.84, 2.60, 0.46, SURFACE, stroke=col, stroke_pt=1.5,
                    radius=True, radius_adj=0.14)
        text_runs(s, x + 0.14, 1.84, 2.32, 0.46, [
            {"text": lbl + "  ", "size": 11.5, "color": DEEP},
            {"text": val + " fabricated citations", "size": 11.5,
             "bold": True, "color": col},
        ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    text_box(s, x=7.00, y=2.44, w=5.55, h=2.14,
             text="2023. A lawyer files a brief citing six entirely "
                  "fabricated court cases — Mata v. Avianca. ChatGPT "
                  "generated them; the legal service Harvey had nothing to "
                  "do with it — a common attribution mistake. Stanford "
                  "RegLab then tests the legal tools themselves on real "
                  "queries: the most accurate one fabricates citations in "
                  "about one query in six, the second twice as often, "
                  "despite a \"hallucination-free\" promise.",
             size=11.5, color=DEEP, line_spacing=1.16)

    # ── ANALYSIS ──
    ocean_box(s, 0.55, 4.76, 12.25, 0.80, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    text_runs(s, 0.80, 4.82, 11.75, 0.68, [
        {"text": "ANALYSIS   ", "size": 11, "bold": True, "color": MID},
        {"text": "The score is measured on a narrow task format and does "
                 "not carry over to the user's real task. A benchmark is "
                 "not useless — it compares versions of one model fairly. "
                 "The trouble starts where a written-exam score is offered "
                 "as proof of readiness to treat a patient.",
         "size": 11.5, "color": DEEP},
    ], line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.62, 12.25, 1.22,
        "By 2026 saturation has been added to the format gap. On MMLU "
        "(Massive Multitask Language Understanding, a combined set of 57 "
        "subjects) frontier models sit in a narrow band of 89–92% — the "
        "score can no longer tell them apart. Worse: 6.5% of the set's own "
        "questions carry an error in the reference answer, and in the "
        "virology section 57%. A safety claim resting on a benchmark alone "
        "is unsupported: it needs an adversarial check on the task the "
        "product solves.",
        size=12.0)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the per-section syntheses were dropped (issue #212).
def s35(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A/B stays the foundation — evals and guardrail metrics are now mandatory on top",
                size=20, w=12.3, h=0.85)
    # layered diagram bottom-aligned
    layers = [
        ("Classical A/B (randomization)", 6.55, MID, 4.35),
        ("Evals (offline + online)", 5.0, TEAL, 3.70),
        ("Guardrail metrics", 3.6, GOLD, 3.05),
    ]
    for txt, w, col, y in layers:
        x = 0.55 + (6.9 - w) / 2
        filled_rect(s, x, y, w, 0.62, SURFACE, stroke=col, stroke_pt=1.8,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x, y=y, w=w, h=0.62, text=txt, size=12.5, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.55, y=1.65, w=7.0, h=0.4,
             text="Measure = the arrow where AI lowered trust",
             size=13.5, bold=True, color=MID, align=PP_ALIGN.CENTER)
    ocean_box(s, 7.85, 1.65, 4.95, 3.35, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    text_box(s, x=8.10, y=1.85, w=4.5, h=3.0,
             text="• Randomization is still what gives causation, not "
                  "coincidence.\n\n• Evals and guardrail metrics are new "
                  "layers on top, not a replacement for A/B.\n\n• The "
                  "phase's central skill — telling signal from noise.",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.20, 12.25, 0.80,
        "Bridge into Support: the same \"signal != noise\" skill in "
        "operation means noticing drift before it shows up on the "
        "dashboard.",
        size=13, bold=True)
    notes_with_sources(s, "s35")
    return s


# ============================================================
# Section 5. Support / Operate
# ============================================================
def s36(p):
    return build_section_divider(
        p, here_idx=5,
        subtitle="Support — the product as an orchestra",
        bridge="Between \"the code works on my machine\" and \"the "
               "product reliably works for millions, 24/7\" lies a gap, "
               "and it's closed by process, not just code quality.",
        sid="s36", tag="2 base cases · 3 failures",
        meme_name="s36-disaster-girl.jpg")


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the ELI5 overviews are gone as a class (issue #212).
def s36b(p):
    return eli5_overview(
        p, "s36b", title="Support in plain terms", icon_name="headphones",
        cards=[
            ("What it is",
             "The product already lives with people around the clock: "
             "it needs to be watched, its failures fixed, and complaints "
             "answered — for years."),
            ("Why",
             "\"Works on my machine\" and \"reliably works for millions, "
             "24/7\" are different things. The gap is closed by process, "
             "not just clean code."),
            ("Mental model",
             "Agree in advance on how many failures are acceptable (a "
             "budget for errors). Harder with AI: a model can \"quietly "
             "degrade\" while the charts are still green."),
        ])


# issue #212, owner review 2026-10-01: the slide was ADDED by the owner and
# until the 2026-10-01 reconciliation did not appear in the manifest at all.
# It introduces the subject of the section (quality as two halves with
# different instruments) before the first descent into numbers.
# DIVERGENCE, THE ORCHESTRATOR DECIDES: this is now the FIRST base slide of
# Section 5, while the protection-tier principle is "the first base slide of
# every phase". But s36c-*.md carries no `protected: true` flag, so the slide
# is NOT entered into that tier here: raising the flag is a decision about
# content, not a reconciliation. For now this is the one section whose first
# base slide is unprotected.
def s36c(p):
    """NEW slide, owner review 2026-10-01, on the remark about slide 37:
    "we start telling the SRE story from the middle — introduce the notion
    and say what it is, a separate preceding step is fine; and show the work
    with users in the same place".

    Carries the frame of the whole section unfolded: support holds quality in
    place, quality is made of two halves with DIFFERENT instruments — the
    user's satisfaction with the product and the reliability of the system —
    and each half names where AI enters it. Both disciplines are named, the
    abbreviations expanded at first appearance (rule R5).
    """
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Support holds quality in place: one half is people, "
                   "the other is the system",
                size=21, y=0.13, w=12.3, h=0.78)

    # ── what this is at all ───────────────────────────────────────────
    ocean_box(s, 0.55, 0.98, 12.25, 1.06, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_runs(s, 0.78, 1.06, 11.79, 0.90, [
        {"text": "WHAT SUPPORT IS.  ", "size": 12, "bold": True,
         "color": MID},
        {"text": "After launch a product makes the same promise every day: "
                 "an answer will come, it will be correct, and what breaks "
                 "will be mended. Support is the work that holds that "
                 "promise for years. The promise has two halves, and they "
                 "are measured with different instruments: one you ask a "
                 "person about, the other you read off the system.",
         "size": 12, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)

    # ── the two halves of quality ─────────────────────────────────────
    COLS = [
        dict(x=0.55, accent=MID, icon_name="users",
             head="PEOPLE · the user's satisfaction with the product",
             body="The half turned towards the person: questions, "
                  "complaints, tickets, returns.",
             mlabel="The measures are what the person sees",
             marks=["the share of tickets closed on first contact",
                    "time to first response and time to resolution",
                    "the rating a person gives once a ticket is closed"],
             disc="The discipline grew out of the help desk and the IT "
                  "service management framework (ITIL).",
             ai="Where AI enters: a suggester at the agent's elbow, and a "
                "bot answering the customer on its own — the next slide."),
        dict(x=6.78, accent=TEAL, icon_name="activity",
             head="SYSTEM · reliability",
             body="The half turned towards the machine: availability, "
                  "latency, outages, deployments.",
             mlabel="The measures are what you read off the system",
             marks=["the share of requests served successfully",
                    "response latency",
                    "the error budget — how many failures are permissible "
                    "in a period"],
             disc="The discipline was given its shape at Google and "
                  "published as a book in 2016 — site reliability "
                  "engineering (Site Reliability Engineering, SRE).",
             ai="Where AI enters: the object of observation, and an "
                "instrument of failure drills."),
    ]
    CY, CH, CWD = 2.12, 3.62, 6.02
    for c in COLS:
        x = c["x"]
        ocean_box(s, x, CY, CWD, CH, fill=SURFACE, stroke=c["accent"],
                  stroke_pt=1.6)
        # column header
        filled_rect(s, x, CY, CWD, 0.46, c["accent"], radius=True,
                    radius_adj=0.14)
        icon(s, c["icon_name"], x + 0.16, CY + 0.10, 0.26, "white")
        text_box(s, x=x + 0.52, y=CY, w=CWD - 0.70, h=0.46, text=c["head"],
                 size=11.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
        # what this half is
        text_box(s, x=x + 0.20, y=CY + 0.56, w=CWD - 0.40, h=0.46,
                 text=c["body"], size=11, color=DEEP, line_spacing=1.14)
        # the name of the discipline — straight under the description
        text_box(s, x=x + 0.20, y=CY + 1.06, w=CWD - 0.40, h=0.56,
                 text=c["disc"], size=9.8, italic=True, color=SLATE,
                 line_spacing=1.10)
        # the measures
        text_box(s, x=x + 0.20, y=CY + 1.66, w=CWD - 0.40, h=0.26,
                 text=c["mlabel"], size=10, bold=True, color=c["accent"],
                 line_spacing=1.04)
        yy = CY + 1.98
        for m in c["marks"]:
            circle(s, x + 0.22, yy + 0.07, 0.11, GOLD)
            text_box(s, x=x + 0.44, y=yy, w=CWD - 0.66, h=0.34, text=m,
                     size=10.5, color=DEEP, line_spacing=1.10)
            yy += 0.34
        # where AI enters
        ocean_box(s, x + 0.18, CY + CH - 0.60, CWD - 0.36, 0.52,
                  fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.4, radius_pt=7.0)
        text_box(s, x=x + 0.32, y=CY + CH - 0.60, w=CWD - 0.64, h=0.52,
                 text=c["ai"], size=10.2, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)

    gold_callout(
        s, 0.55, 5.86, 12.25, 1.00,
        "The halves hold quality only together. A system that never fails "
        "but leaves a person unable to get an answer to their question "
        "loses the product's promise; attentive support on top of a service "
        "that keeps falling over loses it just the same. From here the "
        "section runs along both: reliability in numbers, AI in the work "
        "with people, and the failure drill that tests both.",
        size=12)
    refs_of_slide(s, "s36c")
    notes_with_sources(s, "s36c")
    return s


def s37(p):
    """The "system" half — reliability as a number. EN PARITY, issue #212.

    The EN twin still carried the pre-Stage-6 slide ("A 200 OK response says
    nothing about whether the model is hallucinating": an SLI->SLO->error
    budget flow plus a struck-through HTTP 200 band). OWNER-REVIEW 2026-10-01
    on the RU side: "we start telling the SRE story from the middle". The
    introduction of the notion moved out to the new s36c; what stays here is
    the mechanics, and the slide's place in the frame of the section is shown
    by a teal tag at the title.

    What else this change brought:
    - 70% is given WITH a baseline: the share of ALL outages is named and so
      is the remainder;
    - the two windows got numbers (2% of the monthly budget in an hour, 5% in
      six hours) — before, they differed only in the shape of the curve;
    - the bridge at the end leads to the second half of quality (people and
      AI in that work) instead of model observability: the section was turned
      round onto the use of AI in support."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Error budget: the allowed number of failures, counted "
                   "ahead",
                size=21, y=0.13, w=9.95, h=0.78)
    chip(s, 10.62, 0.22, 2.18, 0.40, "the \"system\" half", fill=TEAL,
         color=WHITE, size=10.5)

    # -- why this work exists: the share of outages caused by the team's own
    #    changes, with a baseline --
    ocean_box(s, 0.55, 0.98, 12.25, 1.16, fill=SURFACE, stroke=MID,
              stroke_pt=1.5)
    text_runs(s, 0.78, 1.06, 11.79, 1.00, [
        {"text": "WHY THIS WORK EXISTS.  ", "size": 12, "bold": True,
         "color": MID},
        {"text": "Google attributes about 70% of the outages of a running "
                 "system to the team's own changes: a deploy, a prompt edit, "
                 "a model version change. The rest is split between hardware "
                 "failures and external causes. So failures come from the "
                 "work the team does every day, and their allowed number is "
                 "worth agreeing in advance: otherwise \"faster or more "
                 "reliable\" is settled after the incident, for whoever is "
                 "louder.",
         "size": 12, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)

    # -- the chain "indicator -> objective -> budget", unfolded into a number
    chain = [
        ("Service level indicator (SLI)", "as the user sees it", MID),
        ("Service level objective (SLO)", "the team's bar: 99.9%", MID),
        ("Error budget", "left over: 1,000 errors", GOLD),
    ]
    cy, ch, cw, cgap = 2.28, 1.00, 2.30, 0.28
    for i, (ttl, sub, col) in enumerate(chain):
        x = 0.55 + i * (cw + cgap)
        ocean_box(s, x, cy, cw, ch, fill=SURFACE, stroke=col, stroke_pt=1.6)
        text_box(s, x=x + 0.10, y=cy + 0.10, w=cw - 0.20, h=0.46, text=ttl,
                 size=11.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 line_spacing=1.05)
        text_box(s, x=x + 0.10, y=cy + 0.60, w=cw - 0.20, h=0.32, text=sub,
                 size=9.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
                 line_spacing=1.05)
        if i < 2:
            right_arrow(s, x + cw + 0.02, cy + 0.38, cgap - 0.04, 0.24,
                        fill=LIGHT)

    text_runs(s, 0.55, 3.42, 7.46, 0.50, [
        {"text": "A 99.9% objective on a million requests in the period "
                 "gives ", "size": 12, "color": DEEP},
        {"text": "1,000 errors", "size": 12, "bold": True, "color": DEEP},
        {"text": " — what is left to spend.",
         "size": 12, "color": DEEP},
    ], line_spacing=1.15)

    ocean_box(s, 0.55, 3.98, 7.46, 1.02, fill=TEAL_TINT, stroke=TEAL,
              stroke_pt=1.5)
    text_runs(s, 0.77, 4.12, 7.02, 0.74, [
        {"text": "Rule: ", "size": 11.5, "bold": True, "color": TEAL},
        {"text": "budget exhausted — shipping new features stops. The "
                 "speed-versus-reliability conversation happens before the "
                 "incident, and it has a basis that rhetoric cannot argue "
                 "with.",
         "size": 11.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)

    # -- two windows: the difference carried by SHAPE, LABEL and NUMBER --
    ocean_box(s, 8.30, 2.28, 4.50, 2.72, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=8.52, y=2.38, w=4.06, h=0.28,
             text="Two alert windows, always both", size=12.5, bold=True,
             color=TEAL, line_spacing=1.05)
    text_box(s, x=8.52, y=2.68, w=4.06, h=0.30,
             text="alone, each is blind to the other's case",
             size=9, italic=True, color=SLATE, line_spacing=1.05)

    # short window: short axis + sharp peak + the number burned
    text_box(s, x=8.52, y=3.02, w=4.06, h=0.26,
             text="Short window — a sharp spike", size=10, bold=True,
             color=DEEP, line_spacing=1.05)
    connector(s, 8.55, 3.72, 10.05, 3.72, color=SLATE, width=1.4)
    connector(s, 9.05, 3.72, 9.30, 3.34, color=GOLD, width=2.4)
    connector(s, 9.30, 3.34, 9.55, 3.72, color=GOLD, width=2.4)
    text_runs(s, 10.22, 3.28, 2.42, 0.52, [
        {"text": "2% of budget in an hour", "size": 9.5, "bold": True,
         "color": DEEP},
        {"text": "at that rate it is gone in two days — page the on-call "
                 "now", "newpara": True,
         "size": 8.6, "italic": True, "color": SLATE},
    ], line_spacing=1.06)

    # long window: long axis + shallow rise
    text_box(s, x=8.52, y=3.98, w=4.06, h=0.26,
             text="Long window — a slow slide", size=10, bold=True,
             color=DEEP, line_spacing=1.05)
    connector(s, 8.55, 4.60, 12.55, 4.60, color=SLATE, width=1.4)
    connector(s, 8.55, 4.54, 12.40, 4.24, color=TEAL, width=2.4)
    text_runs(s, 8.55, 4.66, 4.05, 0.30, [
        {"text": "5% in six hours", "size": 9.5, "bold": True,
         "color": DEEP},
        {"text": "  — a task for working hours", "size": 8.6,
         "italic": True, "color": SLATE},
    ], line_spacing=1.05)

    gold_callout(
        s, 0.55, 5.18, 12.25, 0.96,
        "All this is built for a system where a request either works or it "
        "does not. A 200 — \"delivered successfully\" — arrives even when "
        "the model confidently makes things up. Next, the other half of "
        "quality: people, their tickets, AI in that work.",
        size=12.5)
    refs_of_slide(s, "s37")
    notes_with_sources(s, "s37")
    return s



# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: absorbed by s38a / s38b (issue #212).
def s38(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Tracing catches hallucination drift where infrastructure monitoring stays silent",
                size=20, w=12.3, h=0.85)
    text_box(s, x=0.65, y=1.30, w=11.5, h=0.35,
             text="Tracing (a camera over every node): LangSmith · "
                  "Langfuse · Arize Phoenix · Helicone [1]",
             size=12, italic=True, color=SLATE)
    # request path with cameras
    path = ["prompt", "retrieval", "tools", "response"]
    x0, y0 = 0.65, 2.55
    cw, gap = 2.55, 0.55
    for i, node in enumerate(path):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, y0, cw, 0.95, fill=SURFACE, stroke=MID, stroke_pt=1.4)
        text_box(s, x=x, y=y0, w=cw, h=0.95, text=node, size=13, bold=True,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        icon(s, "search", x + cw / 2 - 0.22, y0 - 0.62, 0.44, "teal")
        if i < 3:
            right_arrow(s, x + cw + 0.05, y0 + 0.35, gap - 0.10, 0.25,
                        fill=LIGHT)
    # LLMOps card + PII warning
    ocean_box(s, 0.55, 3.75, 7.55, 1.15, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    text_box(s, x=0.80, y=3.85, w=7.05, h=0.95,
             text="LLMOps/AgentOps: data drift vs concept drift · "
                  "runtime guardrails · circuit breaker. Guardian Agents "
                  "(a Gartner category) [2] — agents that watch agents.",
             size=12, color=DEEP, line_spacing=1.15, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, 8.30, 3.75, 4.50, 1.15, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.08)
    icon(s, "lock", 8.55, 3.98, 0.5, "gold")
    text_box(s, x=9.20, y=3.85, w=3.4, h=0.95,
             text="Don't send regulated PII to external tracing without "
                  "anonymization or self-hosting.",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    gold_callout(
        s, 0.55, 5.05, 12.25, 0.90,
        "Infrastructure monitoring sees \"the service is alive\"; "
        "tracing sees \"the answers are degrading\": hallucination "
        "drift, retrieval failures, prompt regression.",
        size=13, bold=True)
    refs_of_slide(s, "s38")
    notes_with_sources(s, "s38")
    return s


def s39(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Dashboards stay green while trust has already been falling for weeks",
                size=21, w=12.3, h=0.85)
    # left: Gru's Plan meme
    meme_in_box(s, "s39-grus-plan.jpg", 0.55, 1.55, 3.35, 4.20, pad=0.14)
    # right: silent drift + governance drift
    ocean_box(s, 4.15, 1.60, 8.65, 1.75, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    icon(s, "monitor-smartphone", 4.40, 1.90, 0.6, "teal")
    text_box(s, x=5.20, y=1.78, w=7.35, h=0.4, text="Silent drift",
             size=15, bold=True, color=TEAL)
    text_box(s, x=5.20, y=2.25, w=7.35, h=1.0,
             text="Power users notice a regression before the aggregated "
                  "metrics do — trust falls before the dashboards move.",
             size=13, color=DEEP, line_spacing=1.18)
    ocean_box(s, 4.15, 3.50, 8.65, 1.55, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=4.40, y=3.62, w=8.15, h=0.4, text="Governance drift",
             size=14, bold=True, color=MID)
    text_box(s, x=4.40, y=4.05, w=8.15, h=0.95,
             text="Guardrails with no versioning silently go stale: the "
                  "rules drift from reality unnoticed.",
             size=12.5, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 4.15, 5.20, 8.65, 0.70,
        "What stays: human escalation, accountability, incident "
        "discipline — reinforced by AI's autonomy, not eliminated by it.",
        size=12.5, bold=True)
    notes_with_sources(s, "s39")
    return s


def s40(p):
    """EN twin of slides_band3.py::s40 (issue #212, rule R9): "what happened"
    in plain words first, the analysis second and explicitly named as the
    analysis. The old EN title was the CONCLUSION of the analysis ("the model
    was calibrated correctly — no fuse"), so a reader of the screen alone met
    the verdict before learning which case it was about. The old EN body also
    kept a "circuit breaker" framing the RU source no longer uses here — that
    term is introduced on s42, not on this slide.
    """
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Zillow: algorithm bought homes, market moved, "
                   "business shut",
                size=21, y=0.13, w=12.3, h=0.78)

    # ── WHAT HAPPENED: reads without the lecturer ─────────────────────
    ocean_box(s, 0.55, 0.98, 12.25, 1.50, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    photo_in_box(s, "s40-zillow-real-source.png", 0.72, 1.12, 2.45, 1.22,
                 pad=0.10)
    text_box(s, x=3.34, y=1.06, w=9.24, h=0.26, text="WHAT HAPPENED",
             size=10, bold=True, color=MID, line_spacing=1.0)
    text_runs(s, 3.34, 1.34, 9.24, 1.06, [
        {"text": "Zillow Offers — a service that bought homes on an "
                 "algorithmic valuation and resold them fast. In the third "
                 "quarter of 2021 it bought 9,680 and sold 3,032. On "
                 "2 November 2021 it announced the shutdown: write-downs of ",
         "size": 11.5, "color": DEEP},
        {"text": "$304–408M", "size": 11.5, "bold": True, "color": DEEP},
        {"text": ", a cut of about ", "size": 11.5, "color": DEEP},
        {"text": "2,000 people — 25% of staff", "size": 11.5,
         "bold": True, "color": DEEP},
        {"text": ". Average loss — about ", "size": 11.5, "color": DEEP},
        {"text": "$80K per home", "size": 11.5, "bold": True,
         "color": DEEP},
        {"text": ".", "size": 11.5, "color": DEEP},
    ], line_spacing=1.16)

    # ── chart: captioned ──────────────────────────────────────────────
    ocean_box(s, 0.55, 2.60, 5.95, 2.62, fill=SURFACE, stroke=LIGHT,
              stroke_pt=1.5)
    # Mirrors the RU fix (student-roast 2026-09-30): ONE chart, both
    # quantities in the SAME unit (homes), so the gap between them IS the
    # mechanism. Money figures stay in the "what happened" bar above.
    add_image(s, CHARTS / "c-zillow.png", 0.75, 2.86, 5.55, 2.10,
              preserve_aspect=True)

    # ── ANALYSIS ──────────────────────────────────────────────────────
    ocean_box(s, 6.70, 2.60, 6.10, 2.62, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=6.92, y=2.70, w=5.66, h=0.46,
             text="ANALYSIS: OPERATIONS,\nNOT MEASUREMENT",
             size=10, bold=True, color=TEAL, line_spacing=1.08)
    text_box(s, x=6.92, y=3.22, w=5.66, h=1.90,
             text="The model was calibrated correctly — on historically "
                  "stable data. What was missing: real-time "
                  "monitoring of accuracy and an automatic stop when it "
                  "falls.\n\nGo back to the two windows: Zillow had "
                  "neither. The short one — a sharp rise in error went "
                  "unseen. The long one — quarterly reporting exists, "
                  "but a report every three months is no observation "
                  "window: it is an archive, the homes are already bought.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.38, 12.25, 1.05,
        "Criterion: a model that commits money on its own needs real-time "
        "monitoring of accuracy and a threshold at which it stops with no "
        "human involved. Alternative: the algorithmic valuation as an "
        "input, the decision above a risk threshold left to a person.",
        size=12.5)
    refs_of_slide(s, "s40")
    notes_with_sources(s, "s40")
    return s


def s41(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "\"The bot is a separate legal entity\" — the tribunal rejected this in one sentence",
                size=20, w=12.3, h=0.85)
    # left: real photo (aircraft)
    photo_in_box(s, "s41-aircanada-real-source.png", 0.55, 1.60, 5.55, 3.05)
    # right: balanced scales concept + verdict
    ocean_box(s, 6.35, 1.60, 6.45, 1.75, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    icon(s, "scale", 6.60, 1.95, 0.9, "mid")
    text_box(s, x=7.65, y=1.80, w=4.9, h=1.4,
             text="Scales in balance: the bot's answer = a static page "
                  "on the site. Equal accountability for both.",
             size=13, bold=True, color=DEEP, line_spacing=1.15,
             anchor=MSO_ANCHOR.MIDDLE)
    ocean_box(s, 6.35, 3.55, 6.45, 1.85, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.60, y=3.68, w=5.95, h=0.4, text="Air Canada, website chatbot",
             size=13.5, bold=True, color=DEEP)
    text_box(s, x=6.60, y=4.10, w=5.95, h=1.2,
             text="The bot incorrectly stated a retroactive discount. "
                  "Tribunal — CAD $812.02 [1]: the company is "
                  "responsible for the bot's answer as for any other "
                  "site content [2].",
             size=12, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "You own every answer the bot gives — no more, but not one gram "
        "less accountability than for any other content on the site.",
        size=12.5, bold=True)
    refs_of_slide(s, "s41")
    notes_with_sources(s, "s41")
    return s


def s42(p):
    """EN twin of slides_band3.py::s42 (issue #212). The old EN slide was the
    pre-Stage-6 composition: a Klarna chart, the 853-FTE-equivalent inset and
    the "not an isolated glitch" headline. The RU source dropped the Klarna
    headcount chronicle (a business story about staffing, not a lesson about
    application) and moved Klarna to s39 as a one-line piece of evidence, so
    this slide is now purely the New York case.

    (R9) "what happened" first — who shipped the bot, what it advised, how it
    ended; the analysis second and named as the analysis.
    """
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "New York: city bot advised breaking the law "
                   "10 times out of 10",
                size=21, y=0.13, w=12.3, h=0.78)

    # ── WHAT HAPPENED ─────────────────────────────────────────────────
    ocean_box(s, 0.55, 0.98, 12.25, 1.76, fill=SURFACE, stroke=MID,
              stroke_pt=1.6)
    text_box(s, x=0.78, y=1.06, w=11.79, h=0.26, text="WHAT HAPPENED",
             size=10, bold=True, color=MID, line_spacing=1.0)
    text_runs(s, 0.78, 1.34, 11.79, 1.32, [
        {"text": "New York City shipped a chatbot for small business "
                 "owners — to answer questions about city rules. In March "
                 "2024 an investigation found the bot advising employers to "
                 "take their staff's tips and to fire people for reporting "
                 "harassment, and landlords to turn away tenants with "
                 "housing vouchers. All of that goes against the law in "
                 "force, and the advice came confidently, as instruction. "
                 "All ", "size": 11.5, "color": DEEP},
        {"text": "10 of 10", "size": 11.5, "bold": True, "color": DEEP},
        {"text": " journalists who asked got the same wrong answer. The "
                 "mayor acknowledged the errors and did not pull the bot, "
                 "though switching it off was technically possible.",
         "size": 11.5, "color": DEEP},
    ], line_spacing=1.16)

    # ── reproducibility reads as SHAPE and is captioned ───────────────
    ocean_box(s, 0.55, 2.86, 6.05, 2.42, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    photo_in_box(s, "s42-nyc-real-source.png", 0.75, 2.98, 1.12, 1.12,
                 pad=0.06)
    text_box(s, x=2.02, y=2.98, w=4.36, h=1.12,
             text="The same question — ten times. The same unlawful "
                  "answer — ten times.",
             size=11.5, bold=True, color=DEEP, line_spacing=1.16,
             anchor=MSO_ANCHOR.MIDDLE)
    for i in range(10):
        x = 0.80 + (i % 5) * 1.14
        y = 4.18 + (i // 5) * 0.42
        icon(s, "user-x", x, y, 0.36, "gold")
    # caption BELOW the icons: on the old coordinates it lay over the
    # second row and read through it
    text_box(s, x=0.78, y=5.02, w=5.60, h=0.24,
             text="ten people asked — ten identical answers to break the law",
             size=8.8, italic=True, color=SLATE, line_spacing=1.0)

    # ── ANALYSIS ──────────────────────────────────────────────────────
    ocean_box(s, 6.80, 2.86, 6.00, 2.42, fill=SURFACE, stroke=TEAL,
              stroke_pt=1.5)
    text_box(s, x=7.02, y=2.96, w=5.56, h=0.26, text="ANALYSIS",
             size=10, bold=True, color=TEAL, line_spacing=1.0)
    text_box(s, x=7.02, y=3.26, w=5.56, h=1.92,
             text="Repeatability changes the class of the event. A single "
                  "error is grounds for a fix. Ten identical answers to ten "
                  "identical questions are a system property, "
                  "reproducible on demand.\n\nThe decision to keep "
                  "iterating came after reproducibility was shown in "
                  "public. That is the error under review: the data was "
                  "there, the response stayed the same.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.44, 12.25, 0.92,
        "Criterion: a reproducible harmful answer calls for a circuit "
        "breaker. Next iteration waits. The threshold is named as a "
        "number in advance — else, when it has to be "
        "applied, it is argued over again and loses to the wish to "
        "\"polish it\".",
        size=12.5)
    refs_of_slide(s, "s42")
    notes_with_sources(s, "s42")
    return s


# ============================================================
# [NOT IN THE DECK] This function is not in ORDER (rendered/build_lec05_en.py)
# and is never called during the build: its text does not reach the deck. Kept
# by the convention build_lec05_en.py states ("the dropped builder functions
# stay as dead code"), not by oversight. Any term search over the builders must
# exclude such functions — strings removed from the visible layer legitimately
# live on in them.
# ============================================================
# Dropped: the per-section syntheses were dropped (issue #212).
def s43(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Operation is the point where the loop physically closes",
                size=22, w=12.3, h=0.85)
    # loop with highlighted return arrow
    import math
    cx, cy, r = 3.65, 3.00, 1.45
    steps = ["Discovery", "Design", "Build", "Measure", "Support",
             "Governance"]
    centers = []
    for i in range(6):
        ang = math.pi / 2 - i * (2 * math.pi / 6)
        centers.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    for i in range(6):
        x1, y1 = centers[i]
        x2, y2 = centers[(i + 1) % 6]
        gold_edge = (i == 4)
        connector(s, x1, y1, x2, y2, color=(GOLD if gold_edge else LIGHT),
                  width=(3.0 if gold_edge else 1.8))
    for i, (nx, ny) in enumerate(centers):
        col = GOLD if i in (0, 4) else MID
        circle(s, nx - 0.24, ny - 0.24, 0.48, col, stroke=WHITE, stroke_pt=1.4)
        text_box(s, x=nx - 0.85, y=ny + 0.26, w=1.7, h=0.34, text=steps[i],
                 size=9, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    # right
    ocean_box(s, 6.35, 1.65, 6.45, 3.05, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    text_box(s, x=6.60, y=1.82, w=5.95, h=2.7,
             text="Support → the product closes the loop.\n\nThe signal "
                  "from operation (drift, an incident, a complaint) "
                  "updates the reference dataset and guardrails — and, "
                  "on a deeper signal, sends us back to intent itself: "
                  "what we're building and for whom.",
             size=13, color=DEEP, line_spacing=1.25)
    gold_callout(
        s, 0.55, 5.10, 12.25, 0.85,
        "Observe, interpret, decide — these steps stay human on every "
        "turn of the loop, even as execution is nearly free.",
        size=13, bold=True)
    notes_with_sources(s, "s43")
    return s
