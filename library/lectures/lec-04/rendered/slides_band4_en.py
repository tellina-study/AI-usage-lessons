"""Lecture 4 v4 — Band 4 (s31–s40): Replit, delivery/ops/docs, synthesis, closing.

EN twin of slides_band4.py. Block-5 EN-parity rebuild (issue #172 / #162
round 6) covers s32..s40: the §6 divider, the delivery/ops/docs cluster
(incl. NEW s33b, s35b) and the whole synthesis/closing tail (incl. NEW s37b).
"""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s31 — Replit culmination [in-bucket]
# ============================================================
def s31(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The agent's speed is the speed of the catastrophe; accountability is not delegated",
                size=21, w=12.3, h=0.82)

    # left: Replit chronicle
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.66,
             text="July 2025, a vibe-coding experiment (Replit; Fortune, "
                  "2025-07-23). The human set an explicit code freeze: \"NO MORE "
                  "CHANGES\". Despite the ban, the agent:",
             size=11.5, bold=True, color=MID, line_spacing=1.1)
    chron = [
        "deleted the live (production) DB (1200+ executives, 1190+ companies)",
        "fabricated reports masking the problem",
        "lied to a direct question",
        "rated its own behavior 95 out of 100",
        "claimed rollback was impossible — yet the mechanism worked, the data was restored",
    ]
    cy = 2.30
    for i, txt in enumerate(chron):
        y = cy + i * 0.44
        circle(s, lx + 0.30, y + 0.06, 0.16, GOLD)
        text_box(s, x=lx + 0.60, y=y - 0.02, w=lw - 0.86, h=0.42, text=txt,
                 size=10.5, color=DEEP, line_spacing=1.05)
    filled_rect(s, lx + 0.24, 4.60, lw - 0.48, 0.78, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.44, y=4.68, w=lw - 0.86, h=0.64,
             text="Echoes of the same class (The Register): Amazon Kiro (Dec 2025) — "
                  "hours of downtime · PocketOS / Cursor (Apr 2026) — wiped the DB "
                  "in 9 seconds.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.1)

    # right: 3 collapsing pillars
    rx, rw = 6.85, 5.95
    pillars = [
        ("Prompt != control",
         "\"NO MORE CHANGES\" is, to an agent, not an environment barrier but text "
         "competing for attention. There is no architectural boundary between a \"rule\" "
         "and a \"wish\"."),
        ("Self-assessment != verification",
         "\"95/100\" is anti-correlated with reality (highest at the worst outcome)."),
        ("The agent's report != proof",
         "the source of truth in a postmortem is independent telemetry, not the agent's narrative."),
    ]
    py = 1.52
    hs = [1.30, 0.92, 0.92]
    yy = py
    for i, (head, body) in enumerate(pillars):
        ocean_box(s, rx, yy, rw, hs[i] - 0.06)
        text_box(s, x=rx + 0.24, y=yy + 0.10, w=rw - 0.48, h=0.34, text=head,
                 size=12.5, bold=True, color=MID)
        text_box(s, x=rx + 0.24, y=yy + 0.44, w=rw - 0.48, h=hs[i] - 0.54,
                 text=body, size=11, color=DEEP, line_spacing=1.14)
        yy += hs[i]
    filled_rect(s, rx, yy + 0.02, rw, 0.66, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=yy + 0.08, w=rw - 0.48, h=0.56,
             text="\"95/100\" at the worst outcome · \"9 seconds\"", size=13,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)

    gold_callout(
        s, 0.55, 5.70, 12.25, 0.60,
        "Level-D safety does not live in the prompt — it lives outside the agent: "
        "dev/prod isolation, a hard human gate on destructive actions, least-privilege, "
        "a tested rollback. The root error is autonomy inadequate to the cost of "
        "error [1]. Accountability is not delegated.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s32")
    notes_with_sources(s, "s32")
    return s


# ============================================================
# s32 — section divider, Section 6 (Delivery · Ops · Docs)
# ============================================================
def s32(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Delivery · Operations · Documentation",
        bridge="Three closing phases of the cycle. Delivery and operations are thin: "
               "their input is the state of the real world (the pipeline, prod, "
               "telemetry), which is not in the text. Documentation is the map's "
               "only bright spot, but it too has a price.",
        sid="s33",
        tag="Two thin phases + a bright spot · 3 failures")


# ============================================================
# s33 — delivery, DORA-first (entry slide of §6) [in-bucket]
# ============================================================
def s33(p):
    """Round-6 block-4 restructure, mirrored into EN. This is the FIRST content
    slide of §6, so it carries ONE thesis — the order of investment: maturity
    first, AI second — as a two-step figure, with the DORA pair as its evidence.
    The three co-equal asides of the previous version (risk-calibrated gate ·
    consumes-not-owns · ops is the weakest phase) are demoted to a single muted
    subordinate paragraph, and the seven capabilities are named as a count with
    four examples instead of enumerated in full."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Delivery — DORA-first: a mature pipeline first, then scale AI",
                size=21, w=12.3, h=0.82)

    lx, lw = 0.55, 6.05
    top = 1.44
    ocean_box(s, lx, top, lw, 4.18)
    filled_rect(s, lx + 0.24, top + 0.12, lw - 0.48, 0.70, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=lx + 0.42, y=top + 0.16, w=lw - 0.84, h=0.62,
             text="\"AI amplifies what is already there\" — so there is only one "
                  "order, and it runs against intuition:",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    steps = [
        ("1", "First — mature delivery that works WITHOUT AI: automated tests "
              "as a gate · version control with cheap rollback · fast feedback · "
              "small batches. These are four of the seven delivery capabilities "
              "DORA identifies.", 0.90),
        ("2", "Only then — scale AI on top of it.", 0.50),
    ]
    sy = top + 0.94
    for num, txt, hh in steps:
        filled_rect(s, lx + 0.24, sy, lw - 0.48, hh, TEAL_TINT, stroke=TEAL,
                    stroke_pt=1.3, radius=True, radius_adj=0.07)
        chip(s, lx + 0.40, sy + 0.10, 0.28, 0.26, num, fill=TEAL, color=WHITE,
             size=10)
        text_box(s, x=lx + 0.78, y=sy + 0.08, w=lw - 1.06, h=hh - 0.14,
                 text=txt, size=10, color=DEEP, line_spacing=1.14)
        sy += hh + 0.10
    text_box(s, x=lx + 0.24, y=top + 2.56, w=lw - 0.48, h=0.44,
             text="The reverse does not work: AI does not fix an immature "
                  "pipeline — it speeds it up.",
             size=11.5, bold=True, color=MID, line_spacing=1.12)
    text_box(s, x=lx + 0.24, y=top + 3.10, w=lw - 0.48, h=1.06,
             text="Inside the practice: the prod gate is calibrated by risk — a "
                  "human approves the irreversible; something small and "
                  "reversible that has passed its gates may be confirmed by AI. "
                  "AI consumes the pipeline but does not own it: the agent calls "
                  "gh / aws / gcloud as a privilege-limited user. Operations is "
                  "the weakest of the three phases: no runtime context.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.14)

    # right: the evidence — DORA's two halves of one and the same adoption
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, top, rw, 4.18)
    add_image(s, CHARTS / "c33-dora.png", rx + 0.14, top + 0.12, rw - 0.28, 2.44)
    filled_rect(s, rx + 0.20, top + 2.68, rw - 0.40, 0.90, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.5, radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.40, y=top + 2.73, w=rw - 0.80, h=0.82,
             text="One and the same AI adoption yields both halves: +7.5% to "
                  "documentation quality and -7.2% to delivery stability "
                  "(DORA 2024 [1]); the link with stability is negative for the "
                  "second year running (DORA 2025 [2]).",
             size=10.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)
    text_box(s, x=rx + 0.24, y=top + 3.70, w=rw - 0.48, h=0.50,
             text="Which half outweighs the other is decided by the maturity of "
                  "the pipeline, not by the choice of model.",
             size=11, color=DEEP, line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The failure of this phase is scaling AI onto an immature pipeline: both "
        "speed and instability grow. Hype: \"an AI-CD/ops product as a "
        "replacement for the human\".",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
    return s


# ============================================================
# s33b (NEW in EN, #162 round 3 + round 6) — BT Group / Azure Triangle
# copilot wins vs IaC insecurity: the multiplier works both ways inside
# one and the same phase
# ============================================================
def s33b(p):
    """Round-6 block-4 fix, mirrored into EN: the previous version put two facts
    side by side under a shared banner and never stated the MECHANISM. Both
    columns now answer the same two questions — "what exactly does AI multiply"
    and "where is the gate" — so the reader sees that the multiplier is
    identical (volume × speed) and only the maturity of the gate differs."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The multiplier is volume: a mature gate multiplies what is verified, "
           "a missing gate multiplies what is unsafe",
        size=18.5, w=12.3, h=0.86)

    lx, lw = 0.55, 6.05
    rx, rw = 6.85, 5.95
    top = 1.44

    # left: where the copilot works — and WHY the volume is safe there
    ocean_box(s, lx, top, lw, 4.18, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.6)
    icon(s, "gauge", lx + 0.22, top + 0.14, 0.44, "gold")
    text_box(s, x=lx + 0.80, y=top + 0.16, w=lw - 1.02, h=0.34,
             text="Where the AI copilot works", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 0.58, w=lw - 0.48, h=0.28,
             text="BT Group [1]", size=11.5, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.86, w=lw - 0.48, h=0.36,
             text="MTTR ~2h → 85s (~97% reduction)", size=15, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 1.26, w=lw - 0.48, h=0.42,
             text="MTTR (mean time to repair) — the average time to restore "
                  "service after an incident",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    text_box(s, x=lx + 0.24, y=top + 1.72, w=lw - 0.48, h=0.28,
             text="Microsoft Azure \"Triangle\" [2]", size=11.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=top + 1.98, w=lw - 0.48, h=0.36,
             text="time-to-engage -91%, triage 97%", size=15, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.34, w=lw - 0.48, h=0.26,
             text="time-to-engage — the time until the on-call engineer is engaged",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    filled_rect(s, lx + 0.24, top + 2.64, lw - 0.48, 0.56, WHITE, stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, lx + 0.40, top + 2.67, lw - 0.80, 0.50, [
        {"text": "What AI multiplies: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "alert correlation and steps from a runbook written in advance.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, lx + 0.24, top + 3.26, lw - 0.48, 0.88, WHITE, stroke=GOLD,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, lx + 0.40, top + 3.30, lw - 0.80, 0.82, [
        {"text": "Where the gate is: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "the runbook (a ready-made remediation script) defines the "
                 "permitted actions, telemetry shows the result of every step. "
                 "What is multiplied is work already verified — on top of an "
                 "ALREADY mature operations practice (SRE).",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    # right: same multiplier, opposite side — and WHY the volume is unsafe here
    ocean_box(s, rx, top, rw, 4.18, fill=SOFT_GREY, stroke=LIGHT, stroke_pt=1.0)
    icon(s, "shield-alert", rx + 0.22, top + 0.14, 0.44, "mid")
    text_box(s, x=rx + 0.80, y=top + 0.16, w=rw - 1.02, h=0.34,
             text="The same multiplier, the other side", size=13, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=top + 0.58, w=rw - 0.48, h=0.44,
             text="AI-generated IaC (infrastructure-as-code) [3]",
             size=11.5, bold=True, color=MID, line_spacing=1.10)
    text_box(s, x=rx + 0.24, y=top + 1.04, w=rw - 0.48, h=0.36,
             text="~55% secure by default", size=15, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=top + 1.44, w=rw - 0.48, h=0.60,
             text="the share of tasks where the generated Terraform / Kubernetes "
                  "code is secure out of the box, with no human edits; over "
                  "2 years the figure has barely moved. Syntactic correctness "
                  ">95%.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.10)
    # The «8.4%» must not read as a second measurement of the same 55% —
    # chapter-part5.md §6.2 calls it "a separate 2026 benchmark".
    text_box(s, x=rx + 0.24, y=top + 2.04, w=rw - 0.48, h=0.52,
             text="A separate 2026 benchmark, a different measurement: 8.4% "
                  "on security-checked tasks",
             size=11.5, bold=True, color=DEEP, line_spacing=1.10)
    filled_rect(s, rx + 0.24, top + 2.64, rw - 0.48, 0.56, WHITE, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.40, top + 2.67, rw - 0.80, 0.50, [
        {"text": "What AI multiplies: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "the generation of configurations — many times more artifacts, "
                 "and faster.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, rx + 0.24, top + 3.26, rw - 0.48, 0.88, WHITE, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.40, top + 3.30, rw - 0.80, 0.82, [
        {"text": "There is no gate: ", "size": 9.5, "bold": True, "color": DEEP},
        {"text": "the pipeline checks syntax, not security. More configurations "
                 "→ less attention on each → the unsafe one reaches production.",
         "size": 9.5, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The problem is not that \"there are more rollouts\" but WHAT exactly is "
        "being multiplied: BT multiplies a verified step, IaC generation "
        "multiplies an unverified artifact. The multiplier is the same; only the "
        "maturity of the gate differs.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s33b")
    notes_with_sources(s, "s33b")
    return s


# ============================================================
# s34 — docs bright spot [in-bucket]
# ============================================================
def s34(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Documentation — AI's only clean plus, but it too has a paired cost",
                size=21, w=12.3, h=0.82)

    # left: bright spot (gold accent)
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.8)
    icon(s, "lightbulb", lx + 0.24, 1.66, 0.5, "gold")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Bright spot", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=2.20, w=lw - 0.48, h=1.24,
             text="The only phase with a clean positive systemic effect from "
                  "AI. Why: accidental complexity dominates; the cost of error "
                  "is asymmetrically low; human control is built in — the docs get read.",
             size=11.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, lx + 0.24, 3.48, lw - 0.48, 1.06, WHITE, stroke=GOLD,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.58, w=lw - 0.9, h=0.90,
             text="DORA 2024 [1]: +7.5% to documentation quality. Baseline: cited "
                  "only paired with -7.2% delivery stability (the AI effect almost "
                  "always has a paired cost); stability is negative for a second year.",
             size=11, bold=True, color=DEEP, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    # right: 2 failures
    rx, rw = 6.85, 5.95
    fails = [
        ("bomb", "Cognitive debt (Radar, Hold)",
         "documentation generation outpaces understanding: lots of text, less "
         "understanding. The named remedy is architectural fitness functions "
         "(Ford/Parsons): they keep the \"why\" in a verifiable form."),
        ("triangle-alert", "Onboarding docs hallucinate the setup / deployment",
         "Böckeler [2]: \"AI cannot magically replace a well-documented and "
         "automated setup.\""),
    ]
    heights = [1.84, 1.30]
    yy = 1.52
    for i, (ic, head, body) in enumerate(fails):
        h = heights[i]
        ocean_box(s, rx, yy, rw, h)
        icon(s, ic, rx + 0.24, yy + 0.20, 0.5, "mid")
        text_box(s, x=rx + 0.88, y=yy + 0.20, w=rw - 1.10, h=0.56, text=head,
                 size=12.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=rx + 0.24, y=yy + 0.78, w=rw - 0.48, h=h - 0.86,
                 text=body, size=10.5, color=DEEP, line_spacing=1.12)
        yy += h + 0.10
    filled_rect(s, rx, 4.86, rw, 0.68, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=4.92, w=rw - 0.48, h=0.58,
             text="Secondary: Confluence AI · AWS Q /doc · JetBrains "
                  "KDoc/Javadoc.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Practice: docs-as-context — code stays the source of truth, "
        "documentation is context; generation pace <= comprehension pace. "
        "Documentation-as-context — yes; documentation-as-truth — no.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s35")
    notes_with_sources(s, "s35")
    return s


# ============================================================
# s35b (NEW in EN, #162 r2) — documentation tooling in practice:
# Confluence AI / AWS Q /doc / the code-first skill alternative
# ============================================================
def s35b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The documentation toolchain: the input is code, the output is a "
           "retelling of what was already said",
        size=20, w=12.3, h=0.78)

    colw = 6.05
    gap = 0.15
    lx = 0.55
    rx = lx + colw + gap
    top = 1.42
    boxh = 4.06

    # --- LEFT: SaaS vendor layer ---
    ocean_box(s, lx, top, colw, boxh, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "bot", lx + 0.22, top + 0.16, 0.44, "mid")
    text_box(s, x=lx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="The SaaS vendor layer", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.66, w=colw - 0.48, h=0.30,
             text="Confluence AI (Atlassian Intelligence)", size=11.5,
             bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 0.98, w=colw - 0.48, h=1.10,
             text="Summarizing a long thread into a digest; generating and "
                  "transforming a draft from a prompt; Q&A search over the "
                  "knowledge base (a RAG-like pattern over the corporate base).",
             size=11, color=DEEP, line_spacing=1.20)
    filled_rect(s, lx + 0.24, top + 2.10, colw - 0.48, 0.02, SOFT_GREY)
    text_box(s, x=lx + 0.24, y=top + 2.26, w=colw - 0.48, h=0.30,
             text="AWS Q Developer /doc", size=11.5, bold=True, color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.58, w=colw - 0.48, h=1.42,
             text="The agent analyzes the codebase rather than retelling the "
                  "prompt. It builds infrastructure diagrams from IaC files "
                  "(Terraform/CDK) — a direct link to the already-introduced "
                  "principle of architecture-as-code. A closed loop: the code "
                  "changed → a diff in the documentation is proposed.",
             size=11, color=DEEP, line_spacing=1.20)

    # --- RIGHT: code-first alternative ---
    ocean_box(s, rx, top, colw, boxh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "file-code", rx + 0.22, top + 0.16, 0.44, "teal")
    text_box(s, x=rx + 0.80, y=top + 0.18, w=colw - 1.0, h=0.36,
             text="The code-first alternative", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.24, y=top + 0.66, w=colw - 0.48, h=1.36,
             text="Instead of a separate SaaS — the coding agent itself, through "
                  "an installed skill (\"Code Documentation Skill\", \"README "
                  "Generator\"): it analyzes the project structure, the "
                  "dependencies and the code patterns, and generates README / "
                  "ADR / inline comments.",
             size=11, color=DEEP, line_spacing=1.20)
    filled_rect(s, rx + 0.24, top + 2.10, colw - 0.48, 1.62, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.06)
    icon(s, "graduation-cap", rx + 0.42, top + 2.24, 0.38, "teal")
    text_box(s, x=rx + 0.90, y=top + 2.26, w=colw - 1.28, h=0.30,
             text="An honest caveat", size=11, bold=True, color=TEAL)
    text_box(s, x=rx + 0.42, y=top + 2.62, w=colw - 0.84, h=1.00,
             text="a community pattern, not a single official skill from the "
                  "Anthropic repository. Onboarding documentation is a good "
                  "skill candidate by the heuristics already introduced: a "
                  "repeated instruction + it needs progressive disclosure.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.16)

    gold_callout(
        s, 0.55, top + boxh + 0.14, 12.25, 0.60,
        "The vendor-specific layer illustrates the mechanics of the current "
        "2026 stack, not a recommendation of one vendor: the same pattern is "
        "available through a skill on top of the agent you already use, "
        "without SaaS.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s35b")
    notes_with_sources(s, "s35b")
    return s


# ============================================================
# s35 — section divider, Section 7 (Synthesis)
# ============================================================
def s35(p):
    return build_section_divider(
        p, here_idx=7,
        subtitle="Synthesis — discipline by phase",
        bridge="We have gone through every phase; now let's fold them into a working "
               "toolkit: a matrix \"phase × leading practice × where the human is "
               "mandatory\", triangulation of independent measurements, a compact "
               "risk triad, and a checklist \"when AI yes, when no\".",
        sid="s36",
        tag="Decision toolkit · practice × human")


# ============================================================
# s36 — synthesis matrix (8 phases × 4 cols; the vendor column was
# removed entirely in round 3 so the table cannot read as a tool ranking)
# ============================================================
def s36(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The lecture's matrix: the practice leads — no vendor column",
                size=21, w=12.2, h=0.66)

    headers = ["Phase", "Leading practice", "Failure mode",
               "Where the human is required"]
    # column widths (sum ~12.25) — rebalanced after the vendor column was removed
    cws = [1.95, 3.85, 3.40, 3.05]
    x0 = 0.55
    rows = [
        ("file-code", "Requirements", "spec-driven: spec before code",
         "prompt-and-pray; \"spec = truth\"", "deciding what to build"),
        ("gavel", "Architecture", "ADR + fitness + arch-as-code",
         "poisoned context without management", "choosing the forks under trade-off"),
        ("code", "Implementation", "explore→plan→code→commit + harness",
         "the 70% problem; \"almost right\"", "reviewing the diff + merge"),
        ("flask-conical", "Testing", "TDD: test-as-spec + determ. gate",
         "\"all green\" lies; coverage != defects", "what the test asserts"),
        ("shield-check", "Review + Sec.", "fresh-context; least-priv+SAST",
         "complacency; false confidence", "a second pass + threat modeling"),
        ("git-merge", "Delivery", "headless + risk-calibr. gate (DORA-first)",
         "AI consumes, does not own", "prod gate (hard on the irreversible)"),
        ("wrench", "Operations", "telemetry + on-call",
         "no system context", "owning the system model"),
        ("lightbulb", "Documentation", "docs-as-context (code = truth)",
         "cognitive debt; hallucinations", "pace <= comprehension pace"),
    ]
    top = 1.18
    hh = 0.42
    # header
    cx = x0
    for j, htxt in enumerate(headers):
        col = GOLD if j == 3 else MID
        txtcol = DEEP if j == 3 else WHITE
        filled_rect(s, cx, top, cws[j], hh, col, radius=True, radius_adj=0.10)
        text_box(s, x=cx + 0.06, y=top + 0.03, w=cws[j] - 0.12, h=hh - 0.06,
                 text=htxt, size=11, bold=True, color=txtcol,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.95)
        cx += cws[j]
    # rows
    rh = 0.52
    ry = top + hh + 0.06
    for r, row in enumerate(rows):
        ic = row[0]
        cells = row[1:]
        cx = x0
        fill = SURFACE if r % 2 == 0 else WHITE
        for j in range(4):
            cell_fill = GOLD_TINT if j == 3 else fill
            filled_rect(s, cx, ry, cws[j], rh, cell_fill, stroke=SOFT_GREY,
                        stroke_pt=0.8, radius=True, radius_adj=0.04)
            if j == 0:
                icon(s, ic, cx + 0.08, ry + rh / 2 - 0.16, 0.32,
                     "mid")
                text_box(s, x=cx + 0.46, y=ry + 0.04, w=cws[j] - 0.50,
                         h=rh - 0.08, text=cells[j], size=10, bold=True,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            else:
                text_box(s, x=cx + 0.10, y=ry + 0.04, w=cws[j] - 0.20,
                         h=rh - 0.08, text=cells[j], size=10.3,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
            cx += cws[j]
        ry += rh + 0.04

    gold_callout(
        s, 0.55, 6.20, 12.25, 0.55,
        "The vendor names from sections 1-6 are replaceable; the practice, the "
        "failure mode and the human's point here are durable — they rest on the "
        "character of the phase's complexity [2]. Every cell is derived from a "
        "section covered, not assigned. [1]",
        size=11.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s37", y=7.08)
    notes_with_sources(s, "s37")
    return s


# ============================================================
# s37 — triangulation (3 methods converge) [in-bucket]
# ============================================================
def s37(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Three independent methods converge: an individual AI gain != systemic quality",
        size=20, w=12.4, h=0.82)

    methods = [
        ("radar", "DORA (n ~ 5000, systemic) [1]",
         "~90% of reports: throughput positive, but AI's link to stability is "
         "negative for a second year running. Lens: \"AI amplifies what is already there\"."),
        ("git-compare", "GitClear — two measurements [2]",
         "211M lines (2020-24): refactoring ~25%→<10%, duplicates 8.3%→12.3%. "
         "623M changes (2023-26): refactoring 21%→3.8% (-70%), duplicates +81%, "
         "churn +15%. (Both are correlation, not an RCT.)"),
        ("gauge", "METR (n = 16, experts, familiar code) [3]",
         "tasks with AI took +19% time, yet believed in a speed-up (~-20%) = the "
         "perception gap. (On unfamiliar code the effect differs.)"),
    ]
    cw, gap = 3.97, 0.17
    x0 = 0.55
    my = 1.52
    body_sizes = [10.5, 9.0, 10.5]
    for i, (ic, head, body) in enumerate(methods):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, my, cw, 2.60)
        icon(s, ic, x + 0.24, my + 0.22, 0.56, "teal" if i == 1 else "mid")
        text_box(s, x=x + 0.24, y=my + 0.86, w=cw - 0.48, h=0.46, text=head,
                 size=11.5, bold=True, color=MID, line_spacing=1.0)
        text_box(s, x=x + 0.24, y=my + 1.32, w=cw - 0.48, h=1.20, text=body,
                 size=body_sizes[i], color=DEEP, line_spacing=1.12)
        # arrow down toward centre
        right_arrow(s, x + cw / 2 - 0.14, my + 2.62, 0.28, 0.22, fill=GOLD)

    # convergence strip
    filled_rect(s, 0.55, 4.42, 12.25, 0.94, GOLD_TINT, stroke=GOLD, stroke_pt=1.7,
                radius=True, radius_adj=0.05)
    text_box(s, x=0.80, y=4.50, w=11.75, h=0.80,
             text="The strength is in the convergence of independent methods: DORA, "
                  "GitClear and METR have different blind spots, so the chance all "
                  "three erred the same way is low. The shared conclusion is more "
                  "reliable than any single number.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.56, 12.25, 0.56,
        "One conclusion: the method matters more than the tool. Practice — a CI gate on "
        "duplication and churn; measure the systemic effect, not the perception.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s38")
    notes_with_sources(s, "s38")
    return s


# ============================================================
# s37b (NEW in EN, #162 round 3 + round 6) — Uber: adoption without a
# criterion + the "same product, two registers" bridge (AWS Kiro)
# ============================================================
def s37b(p):
    """Round-6 block-5 fix, mirrored into EN. Diagnosis on the RU deck: the
    slide's own conclusion — that a 2.6× rise in adoption produced NO traceable
    effect for the product — lived only inside the COO quote, so the visible
    layer read as four impressive scale numbers plus a spending line. The fix
    promotes "Effect: not traceable" into its own gold block as the card's main
    conclusion and restructures the left card as Scale → Effect → Response.
    In EN the quote is natively English, but the framing block still has to be
    explicit — the quote alone is not the conclusion."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Scale of adoption is not yet an effect: what decides is neither the "
           "brand nor the reach, but the discipline applied",
        size=19, w=12.4, h=0.82)

    lx, lw = 0.55, 6.05
    rx, rw = 6.85, 5.95
    top = 1.44

    # left: Uber — scale without a criterion → no measurable effect
    ocean_box(s, lx, top, lw, 4.10)
    icon(s, "scale", lx + 0.22, top + 0.14, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=top + 0.18, w=lw - 1.70, h=0.36,
             text="Uber, 2026 [1]", size=13, bold=True, color=MID)
    add_image(s, ASSETS / "logos" / "uber-logo.png", lx + lw - 0.86,
              top + 0.10, 0.60, 0.60)
    text_box(s, x=lx + lw - 1.00, y=top + 0.72, w=0.90, h=0.18,
             text="Uber · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=top + 0.70, w=lw - 1.30, h=0.28,
             text="Scale of adoption", size=11, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=top + 1.00, w=lw - 0.48, h=0.72,
             text="agentic practices 32% → 84% in one month (a 2.6× rise) · "
                  "95% of engineers monthly · 70% of committed code — from AI · "
                  "$500–2000 per engineer per month",
             size=10.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, lx + 0.24, top + 1.80, lw - 0.48, 1.46, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.8, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.42, y=top + 1.88, w=lw - 0.84, h=0.32,
             text="Effect: not traceable", size=13, bold=True, color=DEEP)
    text_box(s, x=lx + 0.42, y=top + 2.22, w=lw - 0.84, h=0.72,
             text="\"It's hard to draw a connection between the company's rising "
                  "use of Claude Code and innovations meant to serve "
                  "consumers… That link is not there yet\"",
             size=9.5, italic=True, color=DEEP, line_spacing=1.12)
    text_box(s, x=lx + 0.42, y=top + 2.94, w=lw - 0.84, h=0.24,
             text="— Andrew Macdonald, President and COO of Uber",
             size=8.5, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=top + 3.38, w=lw - 0.48, h=0.62,
             text="Response: a $1500 per-employee monthly cap — after the fact, "
                  "once the annual budget had burned through in 4 months.",
             size=11, bold=True, color=DEEP, line_spacing=1.16)

    # right: same product, two registers
    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "split", rx + 0.22, top + 0.14, 0.46, "teal")
    text_box(s, x=rx + 0.82, y=top + 0.18, w=rw - 2.35, h=0.60,
             text="AWS Kiro — the same product, two registers [2]", size=11.5,
             bold=True, color=TEAL, line_spacing=1.05)
    add_image(s, ASSETS / "logos" / "aws-logo.png", rx + rw - 1.10,
              top + 0.14, 0.68, 0.41)
    text_box(s, x=rx + rw - 1.20, y=top + 0.58, w=0.88, h=0.18,
             text="AWS · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=rx + 0.24, y=top + 0.66, w=rw - 0.48, h=0.30,
             text="Success:", size=11.5, bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 0.98, w=rw - 0.48, h=0.78,
             text="life sciences — a spec-first discipline, verifiability gates "
                  "set in advance → production in 3 weeks (the same case we "
                  "already saw earlier in the lecture).",
             size=10, color=DEEP, line_spacing=1.14)
    text_box(s, x=rx + 0.24, y=top + 1.80, w=rw - 0.48, h=0.30,
             text="Failure:", size=11.5, bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=top + 2.12, w=rw - 0.48, h=0.94,
             text="the Kiro incident, December 2025 — the agent autonomously "
                  "tore down and rebuilt the environment without approval → "
                  "hours of downtime.",
             size=10.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, rx + 0.24, top + 3.14, rw - 0.48, 0.80, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.40, y=top + 3.20, w=rw - 0.80, h=0.68,
             text="The difference is not the brand (the product is one and the "
                  "same) but the discipline applied or skipped: here the outcome "
                  "is measurable in both directions — unlike the scale without a "
                  "criterion on the left.",
             size=10, italic=True, color=SLATE, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.66, 12.25, 0.78,
        "A rise in adoption is not in itself a result: 2.6× in one month with no "
        "criterion set in advance produced a rise in spending and an unconfirmed "
        "effect. The decision about the scale of AI is a measurable engineering "
        "decision with a criterion set in advance, not cultural inertia.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s37b")
    notes_with_sources(s, "s37b")
    return s


# ============================================================
# s38 — risk triad (3 axes, where the autonomy ceiling is highest)
# [in-bucket]
# ============================================================
def s38(p):
    """Round-6 block-5 reframe, mirrored into EN: the triad used to be titled and
    framed as a binary gate ("when AI yes / no"). The yes/no question no longer
    stands — AI is applied either way; what has to be computed is the AUTONOMY
    CEILING, its price and its measures. The mechanics of the triad (three axes,
    multiplication, the low×low×high zone, "which axis to fix") are untouched —
    they ARE the apparatus for computing the level; the title and framing are
    rewritten (chapter-part5 §7.3). The probability axis is self-contained: it
    names unfamiliarity of the task and the codebase directly, with no reference
    to the anti-hype benchmark slide that round 6 deleted."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The question is not \"AI or not\" but which level of autonomy: "
                   "probability × impact × detectability",
                size=20, w=12.3, h=0.82)

    teal_callout(
        s, 0.55, 1.26, 12.25, 0.50,
        "AI is applied in one mode or another almost always — the triad answers "
        "not \"yes / no\" but which autonomy ceiling is admissible and what pays "
        "for it.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)

    # left: three axes with scale markers inside
    lx, lw = 0.55, 6.50
    axes = [
        ("Probability of error", "low → high",
         "grows with unfamiliarity of the task and codebase"),
        ("Impact of error", "low → high",
         "irreversibility, safety, money, data"),
        ("Detectability", "low → high",
         "is there a test oracle, SAST or review that catches it"),
    ]
    ay = 1.94
    ah = 1.06
    for i, (name, scale, desc) in enumerate(axes):
        y = ay + i * (ah + 0.08)
        ocean_box(s, lx, y, lw, ah)
        text_box(s, x=lx + 0.24, y=y + 0.10, w=lw - 0.48, h=0.30,
                 text=f"{i+1}. {name}", size=13, bold=True, color=MID)
        # scale bar with arrow (markers below the bar, arrow at end of bar)
        bar_y = y + 0.46
        bar_w = lw - 1.10
        filled_rect(s, lx + 0.24, bar_y, bar_w, 0.14, SOFT_GREY,
                    radius=True, radius_adj=0.5)
        right_arrow(s, lx + 0.24 + bar_w + 0.04, bar_y - 0.05, 0.44, 0.24,
                    fill=TEAL)
        text_box(s, x=lx + 0.24, y=bar_y + 0.18, w=2.35, h=0.24, text=scale,
                 size=10, italic=True, color=TEAL)
        text_box(s, x=lx + 2.60, y=bar_y + 0.14, w=lw - 2.85, h=0.42,
                 text=desc, size=9.5, color=SLATE, line_spacing=1.02)

    # right: where the ceiling is highest + what each axis costs
    rx, rw = 7.35, 5.45
    filled_rect(s, rx, 1.94, rw, 1.70, GOLD_TINT, stroke=GOLD, stroke_pt=1.9,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=2.04, w=rw - 0.48, h=0.34,
             text="Where the autonomy ceiling is highest", size=13, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=2.42, w=rw - 0.48, h=1.16,
             text="Full vibe-coding — only with the combination low × low × "
                  "high: low probability of error, low impact, high "
                  "detectability. Any other combination is not a ban on AI but a "
                  "lower ceiling and mandatory measures. The axes multiply, they "
                  "do not add.",
             size=10.5, bold=True, color=DEEP, line_spacing=1.14)
    ocean_box(s, rx, 3.72, rw, 1.58)
    text_box(s, x=rx + 0.24, y=3.82, w=rw - 0.48, h=0.34,
             text="What a higher level is paid for with:", size=12,
             bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=4.22, w=rw - 0.48, h=0.98,
             text="• impact ↑ → a hard human gate\n"
                  "• detectability ↓ → a machine oracle\n"
                  "• probability ↑ → line-by-line senior review",
             size=11, color=DEEP, line_spacing=1.28)

    gold_callout(
        s, 0.55, 5.44, 12.25, 1.00,
        "Böckeler [1]: \"using generative AI is a continuous risk assessment\": "
        "the decision is not made once and not about the tool as a whole, but on "
        "every task. The failure is vibe-coding \"by feel\": not one of the three "
        "axes is computed. Every case in the lecture converges on it: Replit "
        "(impact ↑), curl-slop (detectability ↓), vulnerable code "
        "(probability ↑).",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s39")
    notes_with_sources(s, "s39")
    return s


# ============================================================
# s39 — checklist + Anthropic -17% [in-bucket]
# ============================================================
def s39(p):
    """Round-6 block-5 reframe, matched pair with s38, mirrored into EN: the
    eight questions stay the same (they ARE the working criterion) but stop
    reading as a binary barrier "let AI in or not" — each item is phrased as a
    setting of the mode and the level of autonomy. Frame source: chapter-part5
    §7.4 — "the checklist distributes the burden of proof, it is not 'always
    choose less AI'; for a suitable task it deliberately leads to high
    autonomy"."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Eight questions — not \"AI or not\", but how, where and with "
                   "what control to apply it",
                size=22, w=12.2, h=0.82)

    # left: 8-point checklist
    lx, lw = 0.55, 7.05
    ocean_box(s, lx, 1.52, lw, 4.40)
    checks = [
        ("Which lifecycle phase is this? It sets the failure mode", False),
        ("What is decided deterministically here? Ordinary code writes that "
         "part; AI is for analysis and checking", False),
        ("Essential or accidental complexity? Essential — the human decides, "
         "AI stays at the periphery", False),
        ("Is the consequence reversible? Irreversible → lower the autonomy "
         "ceiling, a hard gate — the VETO axis", True),
        ("Is there a machine oracle (test, SAST, run)? No → the oracle first, "
         "autonomy after", False),
        ("Are secrets / untrusted content involved? Yes → least privilege and "
         "isolation", False),
        ("Who reviews and who merges? Merging and accountability — always the "
         "human", False),
        ("Is the goal an artifact or a skill? A skill → do not delegate the "
         "generation", False),
    ]
    ci_y = 1.68
    for i, (txt, veto) in enumerate(checks):
        y = ci_y + i * 0.52
        if veto:
            filled_rect(s, lx + 0.20, y, lw - 0.40, 0.48, GOLD_TINT,
                        stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.08)
        icon(s, "check-check", lx + 0.28, y + 0.07, 0.32,
             "gold" if veto else "mid")
        text_box(s, x=lx + 0.70, y=y + 0.02, w=lw - 0.92, h=0.44,
                 text=f"{i+1}. {txt}", size=10.5, bold=veto,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # right: Anthropic -17% chart + explanation
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.52, rw, 4.40)
    add_image(s, CHARTS / "c39-anthropic-quiz.png", rx + 0.14, 1.64,
              rw - 0.28, 2.02)
    text_box(s, x=rx + 0.24, y=3.74, w=rw - 0.48, h=1.52,
             text="Anthropic, Shen & Tamkin 2026 (RCT, n=52, learning an "
                  "unfamiliar library) [1]: the AI group scored 50% on the quiz "
                  "against 67% without AI (~-17 pp). Those who delegated the "
                  "generation dropped; those who asked about concepts (\"how it "
                  "works, why\") show no degradation. The speed-up is "
                  "statistically insignificant.",
             size=10.5, color=DEEP, line_spacing=1.18)
    text_box(s, x=rx + 0.24, y=5.30, w=rw - 0.48, h=0.52,
             text="When the goal is a skill, you do the writing; AI explains and "
                  "checks.",
             size=11, bold=True, color=MID, line_spacing=1.10)

    gold_callout(
        s, 0.55, 6.00, 12.25, 0.86,
        "The checklist does not decide \"apply AI or not\" — it issues a mode: "
        "for a suitable task it leads to high autonomy; for an unsuitable one it "
        "lowers the ceiling and names the mandatory measures. This is a "
        "distribution of the burden of proof, not \"always less AI\". "
        "Irreversibility and impact are the veto axis.",
        size=11.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s40", y=7.14)
    notes_with_sources(s, "s40")
    return s


# ============================================================
# s40 — hero closing + bridge + Q&A
# ============================================================
def s40(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    # HERO right half — engineering/review environment photo
    hx, hy, hw, hh = 7.05, 0.0, 6.283, 7.5
    add_image(s, SCR / "s40-closing.jpg", hx, hy, hw, hh, preserve_aspect=False)

    # left: carrying thought + bridges
    slide_title(s, "AI changes the cost of writing code — not the cost of understanding and responsibility",
                size=22, w=6.35, h=1.1, x=0.45, y=0.42)

    gold_callout(
        s, 0.45, 1.72, 6.30, 1.20,
        "AI changes the cost of writing code, but not the cost of understanding what to build and who "
        "is responsible for it. It touches each phase differently — and reliability comes "
        "not from the tool but from discipline by phase.",
        size=12.5, bold=True)

    # Round-6 (Block 5): the teal "Seminar 4 — apply the checklist…" strip that
    # used to sit at y=5.58 is REMOVED — it is a cross-artifact course-scaffold
    # pointer, not student-facing material (owner note p57; the same class as
    # the "mastery — Seminar 4" line deliberately kept off s39). The four
    # method-transfer steps now breathe into the freed vertical band and
    # "Questions?" moves up to close the slide.
    ocean_box(s, 0.45, 3.06, 6.30, 3.02)
    text_box(s, x=0.68, y=3.20, w=5.85, h=0.36,
             text="The method carries over to every industry (not a list of tools):",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    steps = [
        "decompose the activity into phases",
        "ask: accidental or essential complexity",
        "demand a baseline for every number and the systemic effect",
        "separate the durable pattern from vendor hype with five questions",
    ]
    for i, st in enumerate(steps):
        y = 3.74 + i * 0.56
        circle(s, 0.70, y + 0.04, 0.32, TEAL)
        text_box(s, x=0.70, y=y + 0.04, w=0.32, h=0.32, text=str(i + 1),
                 size=12.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.16, y=y, w=5.45, h=0.42, text=st, size=11, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    text_box(s, x=0.45, y=6.36, w=6.30, h=0.7, text="Questions?", size=32,
             bold=True, color=DEEP)
    notes_with_sources(s, "s41")
    return s
