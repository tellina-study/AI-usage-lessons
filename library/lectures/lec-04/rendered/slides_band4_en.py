"""Лекция 4 v4 — Band 4 (s31–s40): Replit, доставка/ops/docs, обобщение, closing."""
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
# s32 — section divider Раздел 6 (Доставка · Ops · Docs)
# ============================================================
def s32(p):
    return build_section_divider(
        p, here_idx=6,
        subtitle="Delivery · Operations · Documentation",
        bridge="Three closing phases of the cycle. Delivery and operations are thin: their "
               "input is the state of the real world (the pipeline, prod, telemetry), "
               "which is not in the text. Documentation is the map's only bright "
               "spot, but it too has a cost.",
        sid="s33",
        tag="Two thin phases + a bright spot · 3 failures")


# ============================================================
# s33 — CI/CD DORA-first + both halves [in-bucket]
# ============================================================
def s33(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Delivery — DORA-first: a mature pipeline first, then scale AI",
                size=21, w=12.3, h=0.82)

    # left: DORA-first practice
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.62, w=lw - 0.48, h=1.08,
             text="What leads is not the tool but the order: first the seven mature "
                  "DORA delivery capabilities — platform engineering · "
                  "automated tests · version control · fast feedback · "
                  "loosely-coupled architecture · documentation · small batches — "
                  "then scale AI. \"AI amplifies what is already there.\"",
             size=11, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, 2.80, lw - 0.48, 0.56, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.07)
    text_box(s, x=lx + 0.46, y=2.87, w=lw - 0.9, h=0.44,
             text="Inside — a hard human prod gate (a release is irreversible).",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.24, y=3.46, w=lw - 0.48, h=0.74,
             text="AI consumes pipelines but does not own them — there is no "
                  "\"AI-CD product\"; the agent calls gh / aws / gcloud as a "
                  "privilege-limited user.",
             size=11, color=DEEP, line_spacing=1.12)
    filled_rect(s, lx + 0.24, 4.30, lw - 0.48, 1.08, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.05)
    icon(s, "wrench", lx + 0.42, 4.42, 0.44, "light")
    text_box(s, x=lx + 1.00, y=4.36, w=lw - 1.3, h=0.98,
             text="Operations is the cycle's weakest phase: there is no system or "
                  "runtime context; the agent's report of state != source of truth "
                  "(an echo of Replit).",
             size=11, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # right: DORA both halves chart + failure
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    add_image(s, CHARTS / "c33-dora.png", rx + 0.14, 1.66, rw - 0.28, 2.40)
    filled_rect(s, rx + 0.20, 4.14, rw - 0.40, 1.20, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.5, radius=True, radius_adj=0.05)
    text_runs(s, rx + 0.40, 4.22, rw - 0.8, 1.06, [
        {"text": "+ throughput and +7.5% documentation — but -7.2% delivery "
                 "stability", "size": 11, "bold": True, "color": DEEP,
         "line_spacing": 1.12},
        {"text": " (DORA 2024) [1]", "size": 9.5, "italic": True, "color": LIGHT},
        {"text": "; a negative link for the second year running (DORA 2025) [2]. Failure: "
                 "scaling AI onto an immature pipeline → the DORA multiplier turns "
                 "the wrong way.", "size": 11, "bold": True, "color": DEEP,
         "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The AI multiplier works both ways. Durable pattern: DORA-first + "
        "a human prod gate. Hype: \"an AI-CD/ops product as a replacement for the human.\"",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s34")
    notes_with_sources(s, "s34")
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
        "documentation is context; generation pace <= understanding pace. "
        "Documentation-as-context — yes; documentation-as-truth — no.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s35")
    notes_with_sources(s, "s35")
    return s


# ============================================================
# s35 — section divider Раздел 7 (Обобщение)
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
# s36 — synthesis matrix (8 phases × 5 cols)
# ============================================================
def s36(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The lecture's matrix: practice leads, the vendor is a swappable column",
                size=22, w=12.2, h=0.66)

    headers = ["Phase", "Leading practice", "Failure mode",
               "Where the human is mandatory", "Vendor (secondary)"]
    # column widths (sum ~12.25)
    cws = [1.55, 3.15, 2.75, 2.65, 2.15]
    x0 = 0.55
    rows = [
        ("file-code", "Requirements", "spec-driven: spec before code",
         "prompt-and-pray; \"spec=truth\"", "deciding what to build",
         "Kiro, Spec-Kit, plan mode"),
        ("gavel", "Architecture", "ADR + fitness + arch-as-code",
         "poisoned context without management", "choosing forks for the tradeoff",
         "no product; Structurizr"),
        ("code", "Implementation", "explore->plan->code->commit + harness",
         "70% problem; \"almost right\"", "review diff + merge",
         "Cursor, Junie, Copilot"),
        ("flask-conical", "Testing", "TDD: test-as-spec + determ. gate",
         "\"all green\" lies; coverage!=defects", "what the test asserts",
         "AWS Q /test, Qodo"),
        ("shield-check", "Review + Sec.", "fresh-context; least-priv+SAST",
         "complacency; false confidence", "second pass + threats",
         "Copilot review; Big Sleep"),
        ("git-merge", "Delivery", "headless + prod gate (DORA-first)",
         "AI consumes, does not own", "production gate", "Actions; gh / CLI"),
        ("wrench", "Operations", "telemetry + on-call",
         "no system context", "owning the system model",
         "AWS Q CloudWatch"),
        ("lightbulb", "Documentation", "docs-as-context (code=truth)",
         "cognitive debt; hallucinations", "pace <= understanding pace",
         "Confluence AI, Q /doc"),
    ]
    top = 1.18
    hh = 0.42
    # header
    cx = x0
    for j, htxt in enumerate(headers):
        col = GOLD if j == 3 else (SOFT_GREY if j == 4 else MID)
        txtcol = DEEP if j in (3, 4) else WHITE
        filled_rect(s, cx, top, cws[j], hh, col, radius=True, radius_adj=0.10)
        text_box(s, x=cx + 0.06, y=top + 0.03, w=cws[j] - 0.12, h=hh - 0.06,
                 text=htxt, size=10.5, bold=True, color=txtcol,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=0.95)
        cx += cws[j]
    # rows
    rh = 0.485
    ry = top + hh + 0.05
    for r, row in enumerate(rows):
        ic = row[0]
        cells = row[1:]
        cx = x0
        fill = SURFACE if r % 2 == 0 else WHITE
        for j in range(5):
            cell_fill = fill
            if j == 3:
                cell_fill = GOLD_TINT
            elif j == 4:
                cell_fill = SOFT_GREY
            filled_rect(s, cx, ry, cws[j], rh, cell_fill, stroke=SOFT_GREY,
                        stroke_pt=0.8, radius=True, radius_adj=0.04)
            if j == 0:
                icon(s, ic, cx + 0.08, ry + rh / 2 - 0.16, 0.32,
                     "mid")
                text_box(s, x=cx + 0.46, y=ry + 0.04, w=cws[j] - 0.50,
                         h=rh - 0.08, text=cells[j], size=10, bold=True,
                         color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            else:
                col = SLATE if j == 4 else DEEP
                sz = 9 if j == 4 else 9.3
                text_box(s, x=cx + 0.08, y=ry + 0.03, w=cws[j] - 0.16,
                         h=rh - 0.06, text=cells[j], size=sz,
                         color=col, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.96)
            cx += cws[j]
        ry += rh + 0.03

    gold_callout(
        s, 0.55, 6.06, 12.25, 0.55,
        "Only the illustration column will be replaced. The leading practice, failure mode and "
        "human checkpoint are durable — they rest on the nature of the phase's complexity [2]. Every "
        "cell is derived from a section we covered, not assigned. [1]",
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
         "negative for a second year running. Lens: \"AI amplifies what is already there.\""),
        ("git-compare", "GitClear (211M lines) [2]",
         "refactoring ~25% -> <10%; duplicates 8.3% -> 12.3%; churn rose. Three "
         "markers of tech-debt accumulation. (Correlation, not an RCT.)"),
        ("gauge", "METR (n = 16, experts, familiar code) [3]",
         "tasks with AI took +19% time, yet believed in a speed-up (~-20%) = the perception "
         "gap. (On unfamiliar code the effect differs.)"),
    ]
    cw, gap = 3.97, 0.17
    x0 = 0.55
    my = 1.52
    for i, (ic, head, body) in enumerate(methods):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, my, cw, 2.60)
        icon(s, ic, x + 0.24, my + 0.22, 0.56, "teal" if i == 1 else "mid")
        text_box(s, x=x + 0.24, y=my + 0.86, w=cw - 0.48, h=0.56, text=head,
                 size=12, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=x + 0.24, y=my + 1.44, w=cw - 0.48, h=1.06, text=body,
                 size=10.5, color=DEEP, line_spacing=1.14)
        # arrow down toward centre
        right_arrow(s, x + cw / 2 - 0.14, my + 2.62, 0.28, 0.22, fill=GOLD)

    # convergence strip
    filled_rect(s, 0.55, 4.42, 12.25, 0.94, GOLD_TINT, stroke=GOLD, stroke_pt=1.7,
                radius=True, radius_adj=0.05)
    text_box(s, x=0.80, y=4.50, w=11.75, h=0.80,
             text="The strength is in the convergence of independent methods: DORA, GitClear and "
                  "METR have different blind spots, so the chance all three "
                  "erred the same way is low. The shared conclusion is more reliable than any "
                  "single number.",
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
# s38 — risk-triad (3 axes, allowed zone) [in-bucket]
# ============================================================
def s38(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "risk triad: \"when AI yes / no\" = probability × impact × detectability",
                size=21, w=12.3, h=0.82)

    # left: three axes with scale markers inside
    lx, lw = 0.55, 6.50
    axes = [
        ("Probability of error", "low → high",
         "rises with the task's unfamiliarity (the SWE-bench Pro axis)"),
        ("Impact of error", "low → high",
         "irreversibility, safety, money, data"),
        ("Detectability", "low → high",
         "is there a test oracle, SAST, review that will catch the error"),
    ]
    ay = 1.48
    ah = 1.08
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
        text_box(s, x=lx + 0.24, y=bar_y + 0.18, w=2.6, h=0.24, text=scale,
                 size=10, italic=True, color=TEAL)
        text_box(s, x=lx + 2.95, y=bar_y + 0.16, w=lw - 3.25, h=0.42,
                 text=desc, size=9.5, color=SLATE, line_spacing=1.02)

    # right: allowed zone + which axis to fix
    rx, rw = 7.35, 5.45
    filled_rect(s, rx, 1.48, rw, 1.62, GOLD_TINT, stroke=GOLD, stroke_pt=1.9,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=1.58, w=rw - 0.48, h=0.34,
             text="Zone of acceptable vibe-coding", size=13, bold=True, color=DEEP)
    text_box(s, x=rx + 0.24, y=1.96, w=rw - 0.48, h=1.06,
             text="ONLY low × low × high (low probability × low "
                  "impact × high detectability). Any other combination → "
                  "discipline. The axes multiply, they do not add.",
             size=11, bold=True, color=DEEP, line_spacing=1.16)
    ocean_box(s, rx, 3.24, rw, 1.66)
    text_box(s, x=rx + 0.24, y=3.34, w=rw - 0.48, h=0.34,
             text="The triad tells you what to fix:", size=12, bold=True,
             color=MID)
    fixes = [
        "impact ↑ → a hard human gate, lower the autonomy ceiling",
        "detectability ↓ → add a machine oracle",
        "probability ↑ → senior review",
    ]
    for i, fx in enumerate(fixes):
        text_box(s, x=rx + 0.24, y=3.74 + i * 0.38, w=rw - 0.48, h=0.34,
                 text=f"• {fx}", size=11, color=DEEP, line_spacing=1.02)

    gold_callout(
        s, 0.55, 5.06, 12.25, 0.90,
        "Böckeler [1]: \"using generative AI is a continuous risk assessment\". "
        "The failure is vibe-coding \"by feel\": ignoring all three axes. Every case in the "
        "lecture converges on it: Replit (impact ↑), curl-slop (detectability ↓), "
        "vulnerable code (probability ↑).",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s39")
    notes_with_sources(s, "s39")
    return s


# ============================================================
# s39 — checklist + Anthropic -17% [in-bucket]
# ============================================================
def s39(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A checklist \"when AI yes / when no\" + what it means for you personally",
                size=22, w=12.2, h=0.82)

    # left: 8-point checklist
    lx, lw = 0.55, 7.05
    ocean_box(s, lx, 1.52, lw, 4.60)
    checks = [
        ("Which lifecycle phase is this?", False),
        ("Can it be solved without AI (deterministically)? Yes → don't add AI", False),
        ("Essential or accidental complexity? Essential → the human", False),
        ("Is the consequence reversible? Irreversible → a hard human gate — VETO axis", True),
        ("Is there a machine oracle (test, SAST, run)? No → don't trust it", False),
        ("Are secrets / untrusted content involved? Yes → least-priv + isolation", False),
        ("Who reviews and merges? Merge and accountability — always the human", False),
        ("Is the goal an artifact or a skill? A skill → don't delegate the generation", False),
    ]
    ci_y = 1.72
    for i, (txt, veto) in enumerate(checks):
        y = ci_y + i * 0.535
        if veto:
            filled_rect(s, lx + 0.20, y, lw - 0.40, 0.48, GOLD_TINT,
                        stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.08)
        icon(s, "check-check", lx + 0.28, y + 0.06, 0.34,
             "gold" if veto else "mid")
        text_box(s, x=lx + 0.72, y=y + 0.03, w=lw - 0.94, h=0.44,
                 text=f"{i+1}. {txt}", size=11, bold=veto,
                 color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # right: Anthropic -17% chart + explanation
    rx, rw = 7.85, 4.95
    ocean_box(s, rx, 1.52, rw, 4.60)
    add_image(s, CHARTS / "c39-anthropic-quiz.png", rx + 0.14, 1.66,
              rw - 0.28, 2.10)
    text_box(s, x=rx + 0.24, y=3.82, w=rw - 0.48, h=2.24,
             text="Anthropic, Shen & Tamkin 2026 (RCT, n=52, learning an unfamiliar "
                  "library) [1]: the AI group scored 50% on the quiz vs 67% without AI "
                  "(~-17 pp). Those who delegated generation dropped; those who asked about "
                  "concepts (\"how it works, why\") show no degradation. The speed-up is "
                  "statistically insignificant.",
             size=11, color=DEEP, line_spacing=1.20)

    gold_callout(
        s, 0.55, 6.20, 12.25, 0.55,
        "The checklist distributes the burden of proof, it is not \"always less AI\": "
        "for a suitable task it leads to high autonomy. Irreversibility and "
        "impact are the veto axis. When learning, you should do the writing; AI's role is to explain and check.",
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

    ocean_box(s, 0.45, 3.06, 6.30, 2.36)
    text_box(s, x=0.68, y=3.16, w=5.85, h=0.36,
             text="The method carries over to every industry (not a list of tools):",
             size=12, bold=True, color=MID, line_spacing=1.0)
    steps = [
        "decompose the activity into phases",
        "ask: accidental or essential complexity",
        "demand a baseline for every number and the systemic effect",
        "separate the durable pattern from vendor hype with five questions",
    ]
    for i, st in enumerate(steps):
        y = 3.56 + i * 0.44
        circle(s, 0.70, y + 0.02, 0.30, TEAL)
        text_box(s, x=0.70, y=y + 0.02, w=0.30, h=0.30, text=str(i + 1),
                 size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=1.14, y=y, w=5.45, h=0.40, text=st, size=10.5, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)

    # bridge to seminar + Q&A
    filled_rect(s, 0.45, 5.58, 6.30, 0.62, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.08)
    text_box(s, x=0.68, y=5.66, w=5.85, h=0.48,
             text="Seminar 4 — apply the checklist to real cases with your own hands.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=0.45, y=6.36, w=6.30, h=0.7, text="Questions?", size=30,
             bold=True, color=DEEP)
    notes_with_sources(s, "s41")
    return s
