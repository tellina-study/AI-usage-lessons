"""Лекция 4 v4 — Band 3 (s21–s30): анти-хайп, тестирование, ревью+безопасность."""
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
# s21 — anti-hype benchmarks (SWE-bench gap chart + 3 overclaims) [in-bucket]
# ============================================================
def s21(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A brand and a benchmark number != engineering discipline",
                size=25, w=12.0, h=0.82)

    # left: SWE-bench gap chart
    lx, lw = 0.55, 5.25
    ocean_box(s, lx, 1.52, lw, 4.02)
    add_image(s, CHARTS / "c21-swe-bench.png", lx + 0.12, 1.66, lw - 0.24, 2.30)
    text_box(s, x=lx + 0.24, y=4.02, w=lw - 0.48, h=1.44,
             text="Verified (~500 tasks, public code) — top ~88-89%. Pro "
                  "(private, contamination-resistant) — leader ~64%. Gap "
                  "~24 pp: trust in the number is inversely proportional to the "
                  "unfamiliarity and criticality of your task.",
             size=11, color=DEEP, line_spacing=1.16)

    # right: 3 overclaims + 5 questions
    rx, rw = 6.05, 6.75
    over = [
        ("Devin (Cognition): 13.86% [1]",
         "vs a 1.96% baseline — but only on 25% of the bench (79 of 570 tasks), "
         "acknowledged contamination, 45-min limit; independently ~15% (3 of 20)."),
        ("OpenAI: \"~80% Verified\" / \"70% more PRs\"",
         "OpenAI itself: ~59% of \"failures\" are test-design defects, not the "
         "model's; \"70% more PRs\" — with no denominator."),
        ("Cursor: Composer \"frontier, 4x faster\"",
         "its own blog admits: GPT-5 and Sonnet 4.5 \"both outperform\" → "
         "frontier-fast, not frontier-best."),
    ]
    oy = 1.52
    for i, (head, body) in enumerate(over):
        y = oy + i * 1.02
        ocean_box(s, rx, y, rw, 0.90)
        text_box(s, x=rx + 0.22, y=y + 0.08, w=rw - 0.44, h=0.32, text=head,
                 size=12, bold=True, color=MID)
        text_box(s, x=rx + 0.22, y=y + 0.40, w=rw - 0.44, h=0.48, text=body,
                 size=10.5, color=DEEP, line_spacing=1.08)
    # 5 questions strip
    filled_rect(s, rx, 4.60, rw, 0.94, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=4.68, w=rw - 0.44, h=0.34,
             text="Five questions for any vendor number:", size=11.5,
             bold=True, color=TEAL)
    text_box(s, x=rx + 0.22, y=5.02, w=rw - 0.44, h=0.48,
             text="1. Which slice? 2. Contamination? 3. Comparison baseline? "
                  "4. Fact or marketing? 5. What's in the fine print? [2]",
             size=11, color=DEEP, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Devin 13.86% — technically true on exactly a quarter of the tasks. A number "
        "can be true and misleading; a high figure doesn't answer the "
        "merge-gate question. A brand/benchmark doesn't replace discipline.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s22")
    notes_with_sources(s, "s22")
    return s


# ============================================================
# s22 — section divider Раздел 4 (Тестирование)
# ============================================================
def s22(p):
    return build_section_divider(
        p, here_idx=4,
        subtitle="Testing — TDD as a discipline",
        bridge="Implementation produces code — testing produces a verified "
               "claim about its correctness. TDD discipline leads here: the test "
               "is an executable specification, subject to neither the \"almost "
               "right\" nor the perception gap.",
        sid="s23",
        tag="Strong given the role · test-as-spec · 1 failure")


# ============================================================
# s23 — TDD discipline (red-green-refactor cycle + role split + nuance)
# ============================================================
def s23(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "TDD-as-approach: the human decides what to check; the run is deterministic",
        size=22, w=12.2, h=0.82)

    # left: red-green-refactor cycle
    lx, lw = 0.55, 5.35
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.34,
             text="The red-green-refactor cycle (Kent Beck, TDD) [1] — the human owns "
                  "the test spec", size=12.5, bold=True, color=MID,
             line_spacing=1.0)
    cyc = [
        ("red", "a failing test expresses a requirement", GOLD, True),
        ("green", "the code that makes it pass", MID, False),
        ("refactor", "improve while keeping it green", TEAL, False),
    ]
    cy0 = 2.06
    for i, (name, desc, col, start) in enumerate(cyc):
        y = cy0 + i * 0.66
        filled_rect(s, lx + 0.30, y, lw - 0.60, 0.54,
                    (GOLD_TINT if start else SURFACE),
                    stroke=col, stroke_pt=(1.8 if start else 1.2),
                    radius=True, radius_adj=0.10)
        if start:
            circle(s, lx + 0.42, y + 0.15, 0.24, GOLD)
        text_box(s, x=lx + (0.78 if start else 0.50), y=y + 0.04, w=1.6, h=0.46,
                 text=name, size=12.5, bold=True, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE, font="DejaVu Sans Mono")
        text_box(s, x=lx + 2.15, y=y + 0.04, w=lw - 2.5, h=0.46, text=desc,
                 size=10.5, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30, y=4.04, w=lw - 0.60, h=0.16, text="↑ repeats",
             size=10.5, italic=True, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    # role split
    filled_rect(s, lx + 0.30, 4.30, lw - 0.60, 1.06, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_runs(s, lx + 0.50, 4.40, lw - 1.0, 0.9, [
        {"text": "AI writes tests fast", "size": 11.5, "bold": True,
         "color": TEAL},
        {"text": " — volume (accidental). ", "size": 11.5, "color": DEEP},
        {"text": "The human decides WHAT the test must assert", "size": 11.5,
         "bold": True, "color": DEEP},
        {"text": " — essential.", "size": 11.5, "color": DEEP},
    ])

    # right: no-outsource + nuance + tools
    rx, rw = 6.10, 6.70
    ocean_box(s, rx, 1.52, rw, 1.28)
    text_box(s, x=rx + 0.24, y=1.62, w=rw - 0.48, h=0.34,
             text="Verification is not outsourced to the model", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx + 0.24, y=1.96, w=rw - 0.48, h=0.80,
             text="Willison / Fowler: \"if you haven't seen it work, it's not a "
                  "working system.\" Tests are run by a deterministic executor "
                  "(script / CI), not by the model's word. Incident → permanent regression test.",
             size=11, color=DEEP, line_spacing=1.14)
    # nuance (honest)
    filled_rect(s, rx, 2.92, rw, 1.28, GOLD_TINT, stroke=GOLD, stroke_pt=1.6,
                radius=True, radius_adj=0.05)
    text_box(s, x=rx + 0.24, y=3.02, w=rw - 0.48, h=0.34,
             text="An important nuance — structure != ritual", size=12.5, bold=True,
             color=DEEP)
    text_box(s, x=rx + 0.24, y=3.36, w=rw - 0.48, h=0.80,
             text="The value of TDD is the structure (spec-test + gate), not the ritual "
                  "of forcing the order on the agent. Böckeler [2]: TDD-first in the agent loop — "
                  "no gain + ~3x tokens (\"I stopped telling "
                  "agents to write tests first\").",
             size=11, color=DEEP, line_spacing=1.12)
    # Fowler tests-as-guardrails caption
    filled_rect(s, rx, 4.32, rw, 0.52, TEAL_TINT, stroke=TEAL, stroke_pt=1.2,
                radius=True, radius_adj=0.07)
    text_runs(s, rx + 0.22, 4.39, rw - 0.44, 0.40, [
        {"text": "Tests-as-guardrails (Fowler) [3]: ", "size": 10.5, "bold": True,
         "color": TEAL},
        {"text": "a test forces the interface without coupling to the implementation — "
                 "which is why the TDD structure is valuable.", "size": 10.5, "color": DEEP},
    ], anchor=MSO_ANCHOR.MIDDLE)
    # tools row
    filled_rect(s, rx, 4.96, rw, 0.52, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=5.03, w=rw - 0.48, h=0.40,
             text="Executors (secondary): AWS Q /test · Qodo · JetBrains Junie · "
                  "Anthropic (failing test → fix + Stop-hook as a gate).",
             size=10, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Durable pattern: test-as-executable-specification + a deterministic "
        "run gate. Hype: \"AI covered the code with tests on its own.\"",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s24")
    notes_with_sources(s, "s24")
    return s


# ============================================================
# s24 — all-green lies + coverage vs mutation (Meta chart) [in-bucket]
# ============================================================
def s24(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Green tests and high coverage can lie — the gate must be honest",
                size=22, w=12.2, h=0.82)

    # left: all-green lies
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "message-square-warning", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="\"all green\" lies (Fowler) [1]", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=2.18, w=lw - 0.48, h=1.00,
             text="\"An LLM will happily say 'all tests green' even when there are "
                  "failures.\" The mechanism is the same — the model generates a plausible "
                  "report with the same token-by-token sampling.",
             size=11.5, color=DEEP, line_spacing=1.16)
    filled_rect(s, lx + 0.24, 3.24, lw - 0.48, 0.88, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.34, w=lw - 0.9, h=0.70,
             text="The AI's report of a run != proof of a run. The gate is a "
                  "deterministic run by a script/CI with a real return "
                  "code, not the model's words.",
             size=11.5, bold=True, color=DEEP, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.24, y=4.24, w=lw - 0.48, h=1.20,
             text="Coverage is deceptive: a line \"touched\" != checked. More honest — "
                  "mutation testing: inject artificial \"mutant\" defects "
                  "and measure the share killed. The danger — Goodhart's law: AI "
                  "optimizes the target metric; a coverage gate → tests \"for "
                  "coverage,\" not for defects.",
             size=11, color=DEEP, line_spacing=1.14)

    # right: Meta chart + numbers
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    add_image(s, CHARTS / "c24-meta-mutation.png", rx + 0.14, 1.66,
              rw - 0.28, 2.55)
    text_box(s, x=rx + 0.24, y=4.28, w=rw - 0.48, h=1.16,
             text="Meta [2]: LLM generation covers more classes (32% vs "
                  "5.3% for a narrow targeted method), but kills fewer mutants "
                  "(2.4% vs 15%). More tests and coverage != better "
                  "defect detection.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The alternative: a deterministic run as the gate + a quality gate on "
        "mutation score, not coverage. Incident → permanent regression test.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s25")
    notes_with_sources(s, "s25")
    return s


# ============================================================
# s25 — section divider Раздел 5 (Ревью + Безопасность)
# ============================================================
def s25(p):
    return build_section_divider(
        p, here_idx=5,
        subtitle="Review + Security — the discipline of skepticism",
        bridge="Review and security are the second, critical look at AI's "
               "output, and both come down to automation bias. "
               "The counterintuitive thesis of this phase: AI code needs more review, not "
               "less — the source of its defects is different.",
        sid="s26",
        tag="Strong in capability · power != security · 4 failures")


# ============================================================
# s26 — review practice (2 human practices + tradeoff + tools)
# ============================================================
def s26(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Review practice — two human practices, not a choice of AI reviewer",
                size=22, w=12.2, h=0.82)

    # left: two human practices
    lx, lw = 0.55, 6.60
    pracs = [
        ("eye-off", "1. Adversarial review with fresh context [1]",
         "The code is reviewed by someone OTHER than the author; the reviewer starts with clean context: "
         "sees only the diff and the acceptance criteria. Reduces the \"I wrote it, "
         "so it's right\" bias (writer-reviewer, two passes)."),
        ("user-check", "2. Retained human accountability",
         "AI review is an assist and a first pass, but the decision and accountability rest with the "
         "human. Osmani [2]: \"if you can't explain it, don't commit.\""),
    ]
    py = 1.52
    for i, (ic, head, body) in enumerate(pracs):
        y = py + i * 1.62
        ocean_box(s, lx, y, lw, 1.50)
        icon(s, ic, lx + 0.24, y + 0.24, 0.54, "mid")
        text_box(s, x=lx + 0.90, y=y + 0.20, w=lw - 1.14, h=0.60, text=head,
                 size=12.5, bold=True, color=MID, line_spacing=1.05)
        text_box(s, x=lx + 0.24, y=y + 0.80, w=lw - 0.48, h=0.62, text=body,
                 size=11, color=DEEP, line_spacing=1.14)

    # right: tradeoff
    rx, rw = 7.35, 5.45
    ocean_box(s, rx, 1.52, rw, 3.12)
    icon(s, "scale", rx + 0.24, 1.66, 0.5, "teal")
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="A fundamental tradeoff", size=13, bold=True, color=TEAL)
    text_box(s, x=rx + 0.24, y=2.18, w=rw - 0.48, h=1.34,
             text="Detection completeness ↔ noise: stricter — more bugs caught, "
                  "but more false alarms; softer — less noise, but misses. "
                  "Anthropic [3]: told to look for holes, the reviewer will find them even in "
                  "healthy code (over-eagerness → over-engineering); scope it to "
                  "correctness.",
             size=10.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, rx + 0.24, 3.54, rw - 0.48, 0.98, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.46, y=3.64, w=rw - 0.9, h=0.80,
             text="No tradeoff point makes AI review an autonomous gate.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)
    # tools row (spanning)
    filled_rect(s, 0.55, 4.80, 12.25, 0.56, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    text_box(s, x=0.80, y=4.88, w=11.75, h=0.42,
             text="First pass over the diff (secondary): GitHub Copilot code review · "
                  "Cursor Bugbot · Qodo Merge · Atlassian Rovo Dev (against criteria "
                  "in Jira) · Anthropic adversarial reviewer.",
             size=10.5, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.52, 12.25, 0.62,
        "Durable pattern: AI review as an assist / first pass. Hype: AI review "
        "as a gate (\"AI reviewed it — safe to merge\"). The decision and accountability rest with the human.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s27")
    notes_with_sources(s, "s27")
    return s


# ============================================================
# s27 — review failure: complacency + curl-slop asymmetry [in-bucket]
# ============================================================
def s27(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Review failure: complacency and the \"fake in seconds, triage in hours\" asymmetry",
                size=21, w=12.3, h=0.82)

    # left: complacency
    lx, lw = 0.55, 5.35
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "eye-off", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Complacency (Radar, Hold ring) [1]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=2.20, w=lw - 0.48, h=0.92,
             text="Uncritical acceptance of AI code, a drop in critical thinking. "
                  "CodeCrash (arXiv:2504.14119) [3]: misleading "
                  "comments crash the model's reasoning (~-23% on "
                  "CRUXEVAL / LIVECODEBENCH).",
             size=11, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, 3.16, lw - 0.48, 1.00, TEAL_TINT, stroke=TEAL,
                stroke_pt=1.4, radius=True, radius_adj=0.06)
    text_box(s, x=lx + 0.46, y=3.26, w=lw - 0.9, h=0.82,
             text="AI review ~19% F1 (SWR-Bench) — and even that is only stated against a "
                  "human-review baseline (low + a high rate of false "
                  "positives).",
             size=11.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.14)
    text_box(s, x=lx + 0.24, y=4.28, w=lw - 0.48, h=1.14,
             text="Stenberg: AI analyzers \"in the right hands\" find real "
                  "bugs — the process architecture is to blame, not AI.",
             size=11, italic=True, color=SLATE, line_spacing=1.14)

    # right: curl-slop asymmetry
    rx, rw = 6.10, 6.70
    ocean_box(s, rx, 1.52, rw, 4.02)
    icon(s, "package-x", rx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="curl-slop as a DDoS on maintainers [2]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx + 0.24, y=2.20, w=rw - 0.48, h=0.58,
             text="A flood of LLM-generated \"vulnerability reports\" in the "
                  "curl bug bounty.",
             size=11.5, color=DEEP, line_spacing=1.14)
    # asymmetry main visual
    filled_rect(s, rx + 0.24, 2.82, rw - 0.48, 1.06, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.8, radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.46, 2.94, rw - 0.9, 0.9, [
        {"text": "Cost asymmetry: ", "size": 13, "bold": True,
         "color": DEEP},
        {"text": "generating a plausible fake takes seconds; refuting it takes "
                 "hours of a maintainer's time.",
         "size": 12.5, "bold": True, "color": DEEP, "line_spacing": 1.14},
    ])
    text_box(s, x=rx + 0.24, y=4.00, w=rw - 0.48, h=1.44,
             text="Numbers: share of valid reports >15% → <5% (~1 in 20-30); volume "
                  "grew several-fold; the program was suspended and moved back to "
                  "HackerOne in March 2026.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI didn't \"make spam nastier\" — it removed the throttle, and the economics of the "
        "process shifted. The alternative: a machine-verifiable barrier at the entrance "
        "(a reproducible PoC), not a manual review of every text.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s28")
    notes_with_sources(s, "s28")
    return s


# ============================================================
# s28 — security practice: Lethal Trifecta + 4 controls
# ============================================================
def s28(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Security — break the lethal trifecta architecturally",
                size=24, w=12.0, h=0.82)

    # left: Lethal Trifecta — 3 conditions
    lx, lw = 0.55, 5.85
    ocean_box(s, lx, 1.52, lw, 4.02)
    text_box(s, x=lx + 0.24, y=1.64, w=lw - 0.48, h=0.60,
             text="The lethal trifecta (Willison, June 2025 [1]; "
                  "Fowler [2]) — only the intersection of all three is dangerous:",
             size=12.5, bold=True, color=MID, line_spacing=1.08)
    tri = [
        ("link", "untrusted content", "issues, emails, web pages"),
        ("key", "secrets / private data", "keys, database"),
        ("arrow-right-left", "outbound transfer (egress)", "can send data out"),
    ]
    ty = 2.42
    for i, (ic, head, sub) in enumerate(tri):
        y = ty + i * 0.90
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.76, SOFT_GREY, stroke=LIGHT,
                    stroke_pt=1.2, radius=True, radius_adj=0.07)
        icon(s, ic, lx + 0.42, y + 0.14, 0.48, "mid")
        text_box(s, x=lx + 1.04, y=y + 0.08, w=lw - 1.3, h=0.36,
                 text=f"{i+1}. {head}", size=12.5, bold=True, color=DEEP)
        text_box(s, x=lx + 1.04, y=y + 0.44, w=lw - 1.3, h=0.28, text=sub,
                 size=10.5, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=5.14, w=lw - 0.48, h=0.34,
             text="Untrusted content via prompt injection → grab a secret → "
                  "send it out.",
             size=10.5, italic=True, color=MID, line_spacing=1.0)

    # right: 4 controls + terms + tools + caveat
    rx, rw = 6.65, 6.15
    ocean_box(s, rx, 1.52, rw, 1.66)
    text_box(s, x=rx + 0.24, y=1.62, w=rw - 0.48, h=0.34,
             text="Four human-owned controls that break the trifecta",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    ctrls = ["least-privilege", "sandbox", "egress-allowlist", "SAST gate"]
    ccx = rx + 0.26
    ccy = 2.02
    for i, c in enumerate(ctrls):
        col = i % 2
        row = i // 2
        chip(s, rx + 0.26 + col * 2.95, 2.02 + row * 0.54, 2.80, 0.46, c,
             fill=TEAL, color=WHITE, size=11)
    text_box(s, x=rx + 0.24, y=3.14, w=rw - 0.48, h=0.34,
             text="Terms: SAST (static) / secret-scanning / SCA (dependencies) "
                  "/ supply-chain.",
             size=10.5, italic=True, color=SLATE)
    # tools
    filled_rect(s, rx, 3.54, rw, 1.06, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=3.62, w=rw - 0.44, h=0.90,
             text="Secondary: GitHub (CodeQL + Copilot Autofix + secret-scanning "
                  "+ Dependabot) · Google (Big Sleep — live exploitation of SQLite; "
                  "OSS-Fuzz + LLM — a ~20-year-old OpenSSL bug) [3] · AWS Q security · "
                  "Anthropic /security-review.",
             size=10, italic=True, color=SLATE, line_spacing=1.1)
    # caveat
    filled_rect(s, rx, 4.72, rw, 0.82, TEAL_TINT, stroke=TEAL, stroke_pt=1.3,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.22, y=4.80, w=rw - 0.44, h=0.68,
             text="\"The first AI to stop a zero-day\" = one curated case; \"AI "
                  "finds 50%\" = metrics on their own code, not universal.",
             size=10.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Durable pattern: a mandatory automated security scan as a gate "
        "+ an architectural break of the trifecta. SAST is necessary but NOT sufficient; "
        "threat modeling is the human's.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s29")
    notes_with_sources(s, "s29")
    return s


# ============================================================
# s29 — vulnerable code + false confidence [in-bucket]
# ============================================================
def s29(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "The danger isn't the vulnerability itself, but the confidence that the code is secure",
                size=23, w=12.2, h=0.82)

    # centre-top: double risk thesis
    ocean_box(s, 0.55, 1.46, 12.25, 1.66)
    text_runs(s, 0.85, 1.57, 11.65, 1.48, [
        {"text": "The most systemic risk is not \"AI sometimes writes vulnerable code,\" but "
                 "\"vulnerable code + a developer's heightened confidence that it's "
                 "secure\"", "size": 14, "bold": True, "color": DEEP},
        {"text": " = automation bias in its most dangerous form.",
         "size": 14, "color": DEEP},
        {"text": "Why systemic: autocomplete relies on the statistically "
                 "frequent, and vulnerable patterns (SQL concatenation, missing "
                 "validation, hardcoded secrets) are pervasive in open code. "
                 "The model reproduces the frequent, not the secure.",
         "size": 11.5, "color": SLATE, "newpara": True, "space_before": 6,
         "line_spacing": 1.14},
    ])

    # two studies
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.26, lw, 2.14)
    icon(s, "flask-conical", lx + 0.24, 3.40, 0.5, "teal")
    text_box(s, x=lx + 0.88, y=3.40, w=lw - 1.10, h=0.34,
             text="Stanford (randomized) [1]", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.88, y=3.72, w=lw - 1.10, h=0.24,
             text="Perry et al. · arXiv:2211.03622 · CCS 2023",
             size=9, italic=True, color=LIGHT)
    text_box(s, x=lx + 0.24, y=4.06, w=lw - 0.48, h=1.28,
             text="Developers with an AI assistant introduced vulnerabilities MORE often — and were "
                  "MORE confident their code was secure. False confidence "
                  "measured directly.",
             size=12, color=DEEP, line_spacing=1.16)

    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 3.26, rw, 2.14)
    icon(s, "bug", rx + 0.24, 3.40, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=3.40, w=rw - 1.10, h=0.34,
             text="NYU \"Asleep at the Keyboard?\" [2]", size=13, bold=True, color=MID)
    text_box(s, x=rx + 0.88, y=3.72, w=rw - 1.10, h=0.24,
             text="arXiv:2108.09293 · IEEE S&P 2022",
             size=9, italic=True, color=LIGHT)
    text_box(s, x=rx + 0.24, y=4.06, w=rw - 0.48, h=0.40,
             text="~40% of Copilot programs contained vulnerabilities.",
             size=13, bold=True, color=DEEP, line_spacing=1.1)
    text_box(s, x=rx + 0.24, y=4.50, w=rw - 0.48, h=0.86,
             text="Baseline: of 1689 programs across 89 scenarios around the MITRE Top-25 CWE "
                  "— the share among deliberately security-sensitive tasks, NOT \"40% "
                  "of all code.\"",
             size=11, italic=True, color=SLATE, line_spacing=1.14)

    gold_callout(
        s, 0.55, 5.52, 12.25, 0.62,
        "The alternative: SAST + DAST + a mandatory security gate plus "
        "threat modeling (essential complexity, not delegated). The danger isn't "
        "the error, but the false confidence next to it.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s30")
    notes_with_sources(s, "s30")
    return s


# ============================================================
# s30 — supply-chain: slopsquatting + CamoLeak [in-bucket]
# ============================================================
def s30(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Supply-chain — a separate class: a reproducible hallucination and a leak channel",
        size=21, w=12.3, h=0.82)

    # left: slopsquatting chain
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    icon(s, "package-x", lx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=1.70, w=lw - 1.10, h=0.40,
             text="Slopsquatting (a supply-chain attack)", size=12.5, bold=True,
             color=MID)
    chain = [
        "the LLM reproducibly hallucinates a package name",
        "an attacker registers it IN ADVANCE with malware",
        "a developer / a C-D agent runs install <made-up>",
    ]
    ch_y = 2.20
    for i, txt in enumerate(chain):
        y = ch_y + i * 0.66
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.52, SURFACE, stroke=LIGHT,
                    stroke_pt=1.1, radius=True, radius_adj=0.08)
        text_box(s, x=lx + 0.46, y=y + 0.05, w=lw - 0.9, h=0.44, text=txt,
                 size=11, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
        if i < 2:
            text_box(s, x=lx + 0.24, y=y + 0.50, w=lw - 0.48, h=0.16, text="↓",
                     size=11, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    filled_rect(s, lx + 0.24, 4.24, lw - 0.48, 1.14, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.05)
    text_runs(s, lx + 0.46, 4.32, lw - 0.9, 1.00, [
        {"text": "The axis of the threat is reproducibility: of 576,000 samples ~20% "
                 "recommended non-existent packages; 43% of hallucinated "
                 "names recurred across all 10 queries",
         "size": 11, "bold": True, "color": DEEP, "line_spacing": 1.12},
        {"text": " (Spracklen et al., USENIX Security 2025) [1]", "size": 9,
         "italic": True, "color": LIGHT},
        {"text": ". The term was coined by Seth Larson (PSF, April 2025).", "size": 11,
         "bold": True, "color": DEEP, "line_spacing": 1.12},
    ], anchor=MSO_ANCHOR.MIDDLE)

    # right: CamoLeak
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.52, rw, 4.02)
    icon(s, "shield-alert", rx + 0.24, 1.66, 0.5, "mid")
    text_box(s, x=rx + 0.88, y=1.70, w=rw - 1.10, h=0.40,
             text="CamoLeak (prompt injection in a dev agent · Legit Security) [2]",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    text_box(s, x=rx + 0.24, y=2.20, w=rw - 0.48, h=1.24,
             text="Instructions hidden in invisible markdown PR comments "
                  "made GitHub Copilot Chat search for secrets (AWS keys) and "
                  "exfiltrate them through the GitHub image proxy.",
             size=11.5, color=DEEP, line_spacing=1.18)
    filled_rect(s, rx + 0.24, 3.42, rw - 0.48, 0.62, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.46, y=3.50, w=rw - 0.9, h=0.48,
             text="CVE-2025-59145, CVSS 9.6 (critical).", size=13, bold=True,
             color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=rx + 0.24, y=4.16, w=rw - 0.48, h=1.24,
             text="A dev agent with access to untrusted content + secrets = "
                  "a ready-made exfiltration channel (a structural property, not a bug). The "
                  "same lethal trifecta — inside a developer's tool.",
             size=11, color=DEEP, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Not cured by a \"better model\" — only by architecture: a lockfile with "
        "hash pinning, a registry allowlist, package verification before install, SCA; "
        "least-privilege + isolation + human-in-the-loop on writes + egress control.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s31")
    notes_with_sources(s, "s31")
    return s
