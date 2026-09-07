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
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Passing a format-A benchmark != safe in a format-B production setting",
                size=21, w=12.3, h=0.85)
    # two mini-cases
    ocean_box(s, 0.55, 1.60, 6.05, 2.85, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    text_box(s, x=0.80, y=1.72, w=5.5, h=0.4, text="Medicine", size=14,
             bold=True, color=MID)
    chip(s, 0.80, 2.20, 2.4, 0.5, "86.5% MedQA [1]", fill=GOLD, color=DEEP,
         size=15)
    text_box(s, x=0.80, y=2.90, w=5.5, h=1.4,
             text="Med-PaLM 2 does well on a Q&A benchmark — but clinical "
                  "safety requires a SEPARATE adversarial safety set.",
             size=12.5, color=DEEP, line_spacing=1.2)
    ocean_box(s, 6.75, 1.60, 6.05, 2.85, fill=SURFACE, stroke=TEAL, stroke_pt=1.5)
    text_box(s, x=7.00, y=1.72, w=5.5, h=0.4, text="Law", size=14,
             bold=True, color=TEAL)
    text_box(s, x=7.00, y=2.20, w=5.5, h=0.9,
             text="Stanford RegLab: Lexis+ 17% hallucinations, Westlaw "
                  "33% — on real legal queries [3].",
             size=12.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, 7.00, 3.20, 5.55, 0.95, GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
                radius=True, radius_adj=0.07)
    text_box(s, x=7.25, y=3.30, w=5.1, h=0.75,
             text="Mata v. Avianca (fake citations) = ChatGPT, NOT Harvey "
                  "[2] — a common attribution mistake.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    gold_callout(
        s, 0.55, 4.65, 12.25, 1.20,
        "A benchmark is evidence of performance only on that specific "
        "benchmark's task format. Alternative: adversarial evals on real "
        "edge cases of the exact domain the product will run in.",
        size=13, bold=True)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
    return s


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


def s37(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A 200 OK response says nothing about whether the model is hallucinating",
                size=20, w=12.3, h=0.85)
    # flow SLI->SLO->error budget
    flow = [("SLI", "a metric"), ("SLO", "target 99.9%"),
            ("Error budget", "\"1 - SLO\"")]
    x0, y0 = 0.55, 1.75
    cw, gap = 3.1, 0.35
    for i, (t, sub) in enumerate(flow):
        x = x0 + i * (cw + gap)
        col = GOLD if i == 2 else MID
        ocean_box(s, x, y0, cw, 1.15, fill=SURFACE, stroke=col, stroke_pt=1.5)
        text_box(s, x=x + 0.10, y=y0 + 0.18, w=cw - 0.2, h=0.4, text=t,
                 size=14, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.10, y=y0 + 0.66, w=cw - 0.2, h=0.34, text=sub,
                 size=11, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
        if i < 2:
            right_arrow(s, x + cw + 0.03, y0 + 0.44, gap - 0.06, 0.26,
                        fill=LIGHT)
    text_box(s, x=0.55, y=3.05, w=11.0, h=0.5,
             text="Error budget = \"1 - SLO\". Example: 99.9% → 1,000 "
                  "errors per 1M requests over 4 weeks. Changes cause "
                  "~=70% of all outages [1].",
             size=12.5, color=DEEP, line_spacing=1.15)
    # struck-through 200
    filled_rect(s, 0.55, 3.75, 12.25, 1.10, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "x", 0.85, 4.00, 0.55, "light")
    text_box(s, x=1.60, y=3.90, w=10.9, h=0.85,
             text="An SLI of \"share of 200 responses\" = all fine? No: "
                  "200 arrives even when the model is confidently "
                  "hallucinating. Infrastructure metrics don't see "
                  "answer quality.",
             size=13, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.05, 12.25, 0.90,
        "On-call, blameless incident reviews, runbooks — you may already "
        "know these. What's new here: a non-deterministic model now sits "
        "in production (next slide).",
        size=13, bold=True)
    refs_of_slide(s, "s37")
    notes_with_sources(s, "s37")
    return s


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
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The model was calibrated correctly — there was no real-time fuse for drift",
                size=18, w=12.3, h=0.85)
    # left: real chart + logo
    photo_in_box(s, "s40-zillow-real-source.png", 0.55, 1.60, 3.05, 1.30,
                 pad=0.22)
    ocean_box(s, 0.55, 3.10, 3.05, 2.30, fill=SURFACE, stroke=MID, stroke_pt=1.4)
    icon(s, "triangle-alert", 1.55, 3.30, 0.9, "mid")
    text_box(s, x=0.70, y=4.30, w=2.75, h=1.0,
             text="The market shifted — concept drift with no circuit "
                  "breaker",
             size=12, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.15)
    # right: chart
    ocean_box(s, 3.85, 1.60, 8.95, 3.80, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    add_image(s, CHARTS / "c-zillow.png", 4.15, 1.85, 8.35, 2.55,
              preserve_aspect=True)
    text_box(s, x=4.15, y=4.45, w=8.35, h=0.85,
             text="Zillow Offers, November 2021: 9,680 homes bought, "
                  "3,032 sold · ~2,000 laid off (~25% of staff) [1] · "
                  "~=$80K loss per property [2].",
             size=12, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "Criterion: a model executing trades with real money requires "
        "real-time monitoring of prediction accuracy with an automatic "
        "circuit breaker that shuts it off on drift.",
        size=12, bold=True)
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
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "10 of 10 journalists got the same unlawful advice — not an isolated glitch",
                size=18, w=12.3, h=0.85)
    # left: Klarna chart + logo
    photo_in_box(s, "s42-klarna-real-source.png", 0.55, 1.60, 2.55, 1.15,
                 pad=0.16)
    ocean_box(s, 0.55, 2.90, 5.75, 2.50, fill=SURFACE, stroke=MID, stroke_pt=1.5)
    add_image(s, CHARTS / "c-klarna.png", 0.80, 3.10, 5.25, 2.05,
              preserve_aspect=True)
    text_box(s, x=3.25, y=1.72, w=3.05, h=1.0,
             text="Klarna: the \"AI-only\" policy was walked back "
                  "(05.2025) [1] — but automation grew to an 853-FTE "
                  "equivalent [2] (augmenting people, not replacing "
                  "them).",
             size=11.5, color=DEEP, line_spacing=1.15)
    # right: NYC 10/10
    ocean_box(s, 6.55, 1.60, 6.25, 3.05, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.6)
    text_box(s, x=6.80, y=1.72, w=5.75, h=0.4, text="NYC MyCity — government bot",
             size=14, bold=True, color=DEEP)
    for i in range(10):
        col_i = i % 5
        row_i = i // 5
        x = 6.85 + col_i * 1.12
        y = 2.25 + row_i * 0.70
        icon(s, "user-x", x, y, 0.48, "gold")
    text_box(s, x=6.80, y=3.70, w=5.75, h=0.85,
             text="10 of 10 journalists — the same unlawful advice [3]. "
                  "The mayor did not pull the bot.",
             size=12.5, bold=True, color=DEEP, line_spacing=1.15)
    gold_callout(
        s, 0.55, 5.55, 12.25, 0.62,
        "The lesson isn't \"AI doesn't work\" — it's \"a throughput "
        "metric with no guaranteed human escalation is the wrong "
        "design.\"",
        size=12.5, bold=True)
    refs_of_slide(s, "s42")
    notes_with_sources(s, "s42")
    return s


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
