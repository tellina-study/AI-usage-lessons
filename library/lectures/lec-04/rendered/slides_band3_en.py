"""Лекция 4 v4 — Band 3 (s21–s30): анти-хайп, тестирование, ревью+безопасность."""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS, WEB,
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
# s25b — BDD + trunk-based, explicit «+ / −» columns [#162 r2, rebuilt r6 b3]
# ============================================================
def s25b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "BDD and trunk-based on the AI loop: what they give, what they "
           "cost",
        size=20, w=12.3, h=0.82)

    colw = 6.05
    gap = 0.15
    lx = 0.55
    rx = lx + colw + gap
    top = 1.24
    boxh = 4.38

    def example(x, text):
        """One concrete micro-example per column — for first-time readers."""
        filled_rect(s, x + 0.20, top + 1.26, colw - 0.40, 0.32, SOFT_GREY,
                    stroke=SLATE, stroke_pt=0.75, radius=True, radius_adj=0.16)
        text_box(s, x=x + 0.34, y=top + 1.29, w=colw - 0.68, h=0.28, text=text,
                 size=9.5, italic=True, color=SLATE, line_spacing=1.04,
                 anchor=MSO_ANCHOR.MIDDLE)

    def plus_minus(x, pros, cons, y_plus, y_minus, h_plus, h_minus):
        """Explicit «+ what it gives» / «− what it costs» blocks in one column."""
        for (yy, hh, sign, label, items, tint, stroke_col, label_col) in (
            (y_plus, h_plus, "+", "WHAT IT GIVES", pros, TEAL_TINT, TEAL, TEAL),
            (y_minus, h_minus, "−", "WHAT IT COSTS", cons, GOLD_TINT, GOLD, DEEP),
        ):
            filled_rect(s, x + 0.20, yy, colw - 0.40, hh, tint,
                        stroke=stroke_col, stroke_pt=1.4, radius=True,
                        radius_adj=0.06)
            text_runs(s, x + 0.36, yy + 0.06, colw - 0.72, 0.26, [
                {"text": f"{sign}  ", "size": 14, "bold": True,
                 "color": stroke_col},
                {"text": label, "size": 11, "bold": True, "color": label_col},
            ], line_spacing=1.0)
            runs = []
            for j, it in enumerate(items):
                runs.append({"text": ("• " + it), "size": 10.5, "color": DEEP,
                             "newpara": bool(j), "space_before": 4})
            text_runs(s, x + 0.36, yy + 0.34, colw - 0.72, hh - 0.40, runs,
                      line_spacing=1.10)

    # --- LEFT: BDD ---
    ocean_box(s, lx, top, colw, boxh, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "check-check", lx + 0.22, top + 0.14, 0.42, "mid")
    text_box(s, x=lx + 0.78, y=top + 0.16, w=colw - 1.0, h=0.34,
             text="BDD — a test in business language",
             size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.22, y=top + 0.52, w=colw - 0.44, h=0.72,
             text="BDD (Behavior-Driven Development) — a Given-When-Then "
                  "scenario a non-technical stakeholder can read and edit. The "
                  "cycle: discuss examples → write them down as scenarios → "
                  "run them as tests.",
             size=10, color=DEEP, line_spacing=1.10)
    example(lx, "Given the slot is free · When \"Book\" is pressed · Then the "
                "slot is taken")
    plus_minus(
        lx,
        ["A gap in the acceptance criteria shows up before the code: the "
         "scenario is read by the people who set the task.",
         "The agent generates scenarios from acceptance criteria — including "
         "edge cases and security checks; the human reviews them."],
        ["An extra layer: ~27% of open-source projects that have a test "
         "framework at all (68% of those are Ruby).",
         "Without a guideline the agent's scenarios degrade: vague Then steps, "
         "coupling to the UI.",
         "With no non-technical stakeholder around it is redundant."],
        top + 1.66, top + 2.94, 1.22, 1.44)

    # --- RIGHT: trunk-based ---
    ocean_box(s, rx, top, colw, boxh, fill=SURFACE, stroke=LIGHT, stroke_pt=1.6)
    icon(s, "git-merge", rx + 0.22, top + 0.14, 0.42, "teal")
    text_box(s, x=rx + 0.78, y=top + 0.16, w=colw - 1.0, h=0.34,
             text="Trunk-based — a short-lived branch", size=13, bold=True,
             color=TEAL)
    text_box(s, x=rx + 0.22, y=top + 0.52, w=colw - 0.44, h=0.72,
             text="Trunk-based development — a branch lives less than a day "
                  "(DORA) and merges into the trunk. Git fixes textual "
                  "conflicts, but not the semantic assumptions of the agent's "
                  "branch.",
             size=10, color=DEEP, line_spacing=1.10)
    example(rx, "claude/fix-auth: opened in the morning, merged by lunch "
                "behind a flag")
    plus_minus(
        rx,
        ["The agent's branch has no time to drift from the trunk in meaning — "
         "and semantic drift is what git does not fix.",
         "Small frequent changes: review keeps up with the pace of agent "
         "commits, and the agent's branch prefix means something."],
        ["Feature flags are mandatory: without them, merging unfinished work "
         "shows it to the user right away.",
         "You need a safety net — real test coverage and a green deterministic "
         "run; without it, frequent merges are more dangerous than a long "
         "branch."],
        top + 1.66, top + 2.94, 1.22, 1.44)

    gold_callout(
        s, 0.55, top + boxh + 0.12, 12.25, 0.58,
        "Both extend practices already named rather than adding a new axis: "
        "BDD earns its place where a non-technical stakeholder exists; "
        "trunk-based, where automated checks and feature flags already do.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s25b")
    notes_with_sources(s, "s25b")
    return s


# ============================================================
# s25c — the agent's local test toolkit: five blind channels [#162 r2/r6 b3]
# ============================================================
def s25c(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The agent's local toolkit: closing its five blind channels",
        size=20, w=12.3, h=0.78)

    # Five cards, 3 + 2 layout; the sixth cell carries the teal takeaway so the
    # bottom row is not half-empty (visual mass balance).
    cards = [
        ("database", "Data", "Testcontainers", MID,
         "Spins up a real Postgres / Kafka / Redis in Docker on a temporary "
         "port — on the agent's own machine.",
         "The agent checks a query against an imagined schema: the test is "
         "either never written, or green on a stub and red in prod."),
        ("route", "Network", "MSW", MID,
         "Intercepts HTTP inside the process: one handler for both unit and "
         "end-to-end tests. Outside JS — WireMock (open source).",
         "The agent either hits the real API — flaky, paid, rate-limited — or "
         "does not test networking code at all."),
        ("monitor", "User interface", "Playwright", TEAL,
         "Gives the agent a browser: not a picture, but the page's element "
         "(accessibility) tree — it clicks, fills forms, emits a test.",
         "The agent never sees the real interface: front-end debugging runs "
         "blind and is essentially pointless."),
        ("terminal", "Your own checks", "a skill wrapper", MID,
         "Packs the repository's existing \"linter → type check → tests\" loop "
         "into a single call.",
         "The agent guesses the project's commands every time — and silently "
         "skips the check it never knew about."),
        ("lock", "Air-gapped setup", "pytest-generator", TEAL,
         "A fine-tuned 8-billion-parameter model (~5 GB, a CPU build exists) "
         "writes test skeletons on the machine.",
         "Any AI test generation = sending source code to an external service: "
         "in an air-gapped setup that is a ban."),
    ]

    x0 = 0.55
    total = 12.25
    gap = 0.16
    cw = (total - gap * 2) / 3           # 3.977
    row_y = [1.20, 3.68]
    ch = 2.42

    for i, (ic, cat, tool, col, does, without) in enumerate(cards):
        r, c = divmod(i, 3)
        x = x0 + c * (cw + gap)
        y = row_y[r]
        # header plate
        filled_rect(s, x, y, cw, 0.58, col, radius=True, radius_adj=0.12)
        icon(s, ic, x + 0.13, y + 0.09, 0.40, "white")
        text_box(s, x=x + 0.60, y=y + 0.04, w=cw - 0.72, h=0.22, text=cat,
                 size=10, bold=True, color=WHITE)
        text_box(s, x=x + 0.60, y=y + 0.25, w=cw - 0.72, h=0.28, text=tool,
                 size=12.5, bold=True, color=WHITE, line_spacing=0.96)
        # «what it does»
        filled_rect(s, x, y + 0.62, cw, 0.84, SURFACE, stroke=SOFT_GREY,
                    stroke_pt=1.0, radius=True, radius_adj=0.08)
        text_box(s, x=x + 0.14, y=y + 0.66, w=cw - 0.28, h=0.18,
                 text="WHAT IT DOES", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.14, y=y + 0.85, w=cw - 0.28, h=0.58, text=does,
                 size=10, color=DEEP, line_spacing=1.06)
        # «what is impossible without it»
        filled_rect(s, x, y + 1.50, cw, 0.92, GOLD_TINT, stroke=GOLD,
                    stroke_pt=1.4, radius=True, radius_adj=0.07)
        text_box(s, x=x + 0.14, y=y + 1.54, w=cw - 0.28, h=0.18,
                 text="IMPOSSIBLE / VERY HARD WITHOUT IT", size=9,
                 bold=True, color=DEEP)
        text_box(s, x=x + 0.14, y=y + 1.73, w=cw - 0.28, h=0.64, text=without,
                 size=10, color=DEEP, line_spacing=1.06)

    # sixth cell — takeaway (balances the 3+2 grid instead of empty space)
    tx = x0 + 2 * (cw + gap)
    ty = row_y[1]
    filled_rect(s, tx, ty, cw, ch, TEAL_TINT, stroke=TEAL, stroke_pt=1.6,
                radius=True, radius_adj=0.07)
    text_box(s, x=tx + 0.18, y=ty + 0.14, w=cw - 0.36, h=0.30,
             text="How to choose", size=12.5, bold=True, color=TEAL)
    text_box(s, x=tx + 0.18, y=ty + 0.50, w=cw - 0.36, h=1.80,
             text="Each tool closes exactly one channel the agent is blind in: "
                  "data, network, user interface, your own checks, an "
                  "air-gapped setup.\n\nLocal, deterministic and already "
                  "working — take it and wrap it; the only thing worth writing "
                  "yourself is a wrapper around your own check loop.",
             size=10, color=DEEP, line_spacing=1.10)

    # honest-limits strip (muted, one line)
    cy = row_y[1] + ch + 0.08
    filled_rect(s, x0, cy, total, 0.48, SOFT_GREY, stroke=SLATE, stroke_pt=0.75,
                radius=True, radius_adj=0.11)
    text_box(s, x=x0 + 0.18, y=cy + 0.04, w=total - 0.36, h=0.40,
             text="Honest limits: without a real sample API response an MSW "
                  "mock is the agent's guess, not a contract · WireMock's AI "
                  "features live in the paid WireMock Cloud, not in the local "
                  "open-source core · pytest-generator — ~77% accuracy claimed "
                  "by the vendor, not independently verified, adoption low.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.08,
             anchor=MSO_ANCHOR.MIDDLE)
    refs_of_slide(s, "s25c")
    notes_with_sources(s, "s25c")
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
# s27 — review failure: complacency + curl-slop asymmetry + load shift
# [in-bucket; round-6 block-4 rebuild: 2 cases -> 3, 2-col -> 3-col]
# ============================================================
def s27(p):
    """Round-6 block-4: 2 cases -> 3. Owner ask — add a third case showing that
    the aggregate «productivity went up» hides a REDISTRIBUTION: juniors gain,
    seniors absorb the new review load. Layout rebuilt 2-col -> 3-col so all
    three cases read as parallel instances of one mechanism (AI removed the
    volume limiter; the cost of checking did not fall with it)."""
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Review failure: complacency, the \"fake in seconds, triage in "
                   "hours\" asymmetry, and a load shift onto seniors",
                size=20, w=12.3, h=0.86)

    cw = 3.93
    c1, c2, c3 = 0.55, 4.70, 8.85
    top, bh = 1.44, 4.16
    pad = 0.24

    # ---------- column 1: complacency ----------
    ocean_box(s, c1, top, cw, bh)
    icon(s, "eye-off", c1 + pad, top + 0.12, 0.42, "mid")
    text_box(s, x=c1 + 0.74, y=top + 0.12, w=cw - 0.98, h=0.34,
             text="1. Complacency toward AI code [1]", size=12, bold=True,
             color=MID)
    text_box(s, x=c1 + 0.74, y=top + 0.46, w=cw - 0.98, h=0.28,
             text="Thoughtworks Radar — the Hold ring", size=9, italic=True,
             color=SLATE)
    text_box(s, x=c1 + pad, y=top + 0.88, w=cw - 2 * pad, h=0.70,
             text="Uncritical acceptance of AI code, a drop in critical "
                  "thinking. CodeCrash [3]: misleading comments crash the "
                  "model\u2019s reasoning (~\u221223%).",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c1 + pad, top + 1.62, cw - 2 * pad, 0.66, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.07)
    text_box(s, x=c1 + 0.38, y=top + 1.66, w=cw - 0.76, h=0.58,
             text="AI review ~19% F1 (SWR-Bench) — against human review as "
                  "the baseline.",
             size=9.5, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c1 + pad, y=top + 2.40, w=cw - 2 * pad, h=0.30,
             text="Rubber-Stamp Collapse, 470 PRs [4]", size=10.5, bold=True,
             color=MID)
    text_box(s, x=c1 + pad, y=top + 2.72, w=cw - 2 * pad, h=0.72,
             text="+170% findings, +40% of them critical, \u00d72.74 "
                  "vulnerabilities; across 22,000 developers — +242.7% "
                  "incidents per PR.",
             size=9.5, color=DEEP, line_spacing=1.12)
    text_box(s, x=c1 + pad, y=top + 3.46, w=cw - 2 * pad, h=0.62,
             text="Stenberg: AI analyzers \"in the right hands\" do find real "
                  "bugs — what is broken is the process architecture, not the "
                  "model.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    # ---------- column 2: curl-slop asymmetry ----------
    ocean_box(s, c2, top, cw, bh)
    icon(s, "package-x", c2 + pad, top + 0.12, 0.42, "mid")
    text_box(s, x=c2 + 0.74, y=top + 0.12, w=cw - 1.30, h=0.62,
             text="2. curl-slop as a DDoS on maintainers [2]", size=12,
             bold=True, color=MID, line_spacing=1.06)
    add_image(s, ASSETS / "logos" / "curl-logo.png", c2 + cw - 0.56, top + 0.10,
              0.40, 0.40)
    text_box(s, x=c2 + cw - 0.92, y=top + 0.52, w=0.76, h=0.18,
             text="curl — official logo", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=c2 + pad, y=top + 0.84, w=cw - 2 * pad, h=0.44,
             text="A flood of LLM \"vulnerability reports\" into the curl bug "
                  "bounty.",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c2 + pad, top + 1.32, cw - 2 * pad, 0.78, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=c2 + 0.38, y=top + 1.36, w=cw - 0.76, h=0.70,
             text="Cost asymmetry: a fake takes seconds, refuting it takes "
                  "hours of a maintainer\u2019s time.",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c2 + pad, y=top + 2.22, w=cw - 2 * pad, h=0.72,
             text="Valid reports >15% \u2192 <5% (~1 in 20\u201330); volume grew "
                  "several-fold; the program was suspended and moved back to "
                  "HackerOne in March 2026.",
             size=9.5, color=DEEP, line_spacing=1.12)
    filled_rect(s, c2 + pad, top + 3.00, cw - 2 * pad, 1.02, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.07)
    icon(s, "message-square-warning", c2 + 0.36, top + 3.08, 0.30, "mid")
    text_box(s, x=c2 + 0.72, y=top + 3.07, w=cw - 1.00, h=0.28,
             text="matplotlib, February 2026 [5]", size=9.5, bold=True,
             color=DEEP)
    text_box(s, x=c2 + 0.36, y=top + 3.38, w=cw - 0.72, h=0.58,
             text="An AI agent wrote and published an essay against the "
                  "maintainer who closed its PR — the same economics, aimed "
                  "at a person.",
             size=9, color=DEEP, line_spacing=1.10)

    # ---------- column 3 (NEW, round-6): redistribution, not net gain ----------
    ocean_box(s, c3, top, cw, bh)
    icon(s, "scale", c3 + pad, top + 0.12, 0.42, "teal")
    text_box(s, x=c3 + 0.74, y=top + 0.12, w=cw - 0.98, h=0.62,
             text="3. Not a net gain, a redistribution [6]", size=12,
             bold=True, color=MID, line_spacing=1.06)
    text_box(s, x=c3 + pad, y=top + 0.80, w=cw - 2 * pad, h=0.78,
             text="Xu et al.: 2,755 GitHub repositories, 1,699 contributors, "
                  "12 months before and after Copilot. The \"core\" = top 25% "
                  "by commits BEFORE, the \"periphery\" = the other 75%.",
             size=9, italic=True, color=SLATE, line_spacing=1.14)
    filled_rect(s, c3 + pad, top + 1.62, cw - 2 * pad, 0.64, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.07)
    text_box(s, x=c3 + 0.38, y=top + 1.66, w=cw - 0.76, h=0.56,
             text="Periphery (juniors): commits +43.5%, PRs +17.7%",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    filled_rect(s, c3 + pad, top + 2.32, cw - 2 * pad, 0.64, GOLD_TINT,
                stroke=GOLD, stroke_pt=1.6, radius=True, radius_adj=0.07)
    text_box(s, x=c3 + 0.38, y=top + 2.36, w=cw - 0.76, h=0.56,
             text="Core (seniors): own commits \u221219%, reviewing others\u2019 +6.5%",
             size=10, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.10)
    text_box(s, x=c3 + pad, y=top + 3.06, w=cw - 2 * pad, h=0.28,
             text="PR rework after submission: +2.4%.", size=9.5, color=DEEP)
    text_box(s, x=c3 + pad, y=top + 3.38, w=cw - 2 * pad, h=0.68,
             text="\"Productivity went up overall\" — but the gain lands on "
                  "one group and the new review work on another, and there "
                  "are three times fewer of them.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "In none of the three did AI \"make things worse\" — it removed the "
        "limiter on volume while the cost of checking stayed the same. The "
        "alternative: a machine-verifiable barrier at the entrance and an "
        "honest account of who pays for the checking.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme (EN caption bake): Evil Kermit — the inner temptation to
    # skip reading the diff and rubber-stamp instead (callback to column 1).
    add_image(s, WEB / "band-evil-kermit-en.png", 9.29, 6.38, 3.51, 0.58)
    refs_of_slide(s, "s28", y=7.00, size=7.5)
    notes_with_sources(s, "s28")
    return s


# ============================================================
# s28 — security practice: Lethal Trifecta + 4 controls (round-6 b4 rebuild)
# ============================================================
def s28(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "Security — break the lethal trifecta architecturally",
                size=24, w=12.0, h=0.82)

    # Round-6 block-4 (owner ask: «simplify, keep only what matters, decode
    # every term for those who are new to it»). Kept: the lethal-trifecta
    # definition + the 4 controls. Dropped from the visible layer: the
    # four-vendor stack paragraph (GitHub/Google/AWS/Anthropic) — that space
    # now carries a full inline decoding of every surviving term. The vendor
    # examples stay in the speaker notes, where ref [3] still anchors them.

    # left: Lethal Trifecta — 3 conditions
    lx, lw = 0.55, 5.85
    top = 1.44
    ocean_box(s, lx, top, lw, 4.18)
    text_box(s, x=lx + 0.24, y=top + 0.10, w=lw - 0.48, h=0.70,
             text="The lethal trifecta (Willison, June 2025 [1]; Fowler [2]) — "
                  "no single property is dangerous on its own, only the "
                  "intersection of all three:",
             size=12, bold=True, color=MID, line_spacing=1.08)
    tri = [
        ("link", "untrusted content",
         "issues, emails, web pages — you did not write them"),
        ("key", "secrets and private data",
         "keys, tokens, database access"),
        ("arrow-right-left", "outbound transfer (egress)",
         "a channel outward: data can leave the perimeter"),
    ]
    ty = top + 0.86
    for i, (ic, head, sub) in enumerate(tri):
        y = ty + i * 0.88
        filled_rect(s, lx + 0.24, y, lw - 0.48, 0.76, SOFT_GREY, stroke=LIGHT,
                    stroke_pt=1.2, radius=True, radius_adj=0.07)
        icon(s, ic, lx + 0.40, y + 0.16, 0.44, "mid")
        text_box(s, x=lx + 0.98, y=y + 0.08, w=lw - 1.24, h=0.34,
                 text=f"{i+1}. {head}", size=11.5, bold=True, color=DEEP)
        text_box(s, x=lx + 0.98, y=y + 0.44, w=lw - 1.24, h=0.28, text=sub,
                 size=10, italic=True, color=SLATE)
    text_box(s, x=lx + 0.24, y=top + 3.56, w=lw - 0.48, h=0.60,
             text="All three at once make a ready-made leak channel: the "
                  "agent\u2019s instruction is swapped through text it read "
                  "(prompt injection) \u2192 grab a secret \u2192 send it out.",
             size=10, italic=True, color=MID, line_spacing=1.12)

    # right: 4 controls, each decoded inline
    rx, rw = 6.65, 6.15
    ocean_box(s, rx, top, rw, 4.18)
    text_box(s, x=rx + 0.24, y=top + 0.10, w=rw - 0.48, h=0.32,
             text="Four controls that break the trifecta",
             size=12.5, bold=True, color=MID, line_spacing=1.0)
    ctrls = [
        ("least-privilege (minimum necessary access)",
         "the agent is given only the access without which the task cannot be "
         "done. No key — nothing to leak.", 0.64),
        ("sandbox (an isolated environment)",
         "the agent works in a sandbox: its mistake physically cannot reach "
         "prod.", 0.50),
        ("egress-allowlist (a whitelist of recipients)",
         "it is listed in advance where data may be sent at all; everything "
         "else is closed.", 0.64),
        ("SAST gate (a mandatory automated scan)",
         "SAST (static application security testing) — static analysis of code "
         "for vulnerabilities before it runs; secret-scanning — hunting for "
         "leaked keys and tokens; SCA (software composition analysis) — "
         "checking third-party libraries (the supply chain) for known "
         "vulnerabilities.",
         1.06),
    ]
    cy = top + 0.48
    for i, (term, expl, hh) in enumerate(ctrls):
        chip(s, rx + 0.24, cy + 0.03, 0.30, 0.28, str(i + 1), fill=TEAL,
             color=WHITE, size=10)
        text_box(s, x=rx + 0.64, y=cy, w=rw - 0.90, h=0.28, text=term,
                 size=11, bold=True, color=DEEP)
        text_box(s, x=rx + 0.64, y=cy + 0.28, w=rw - 0.90, h=hh - 0.28,
                 text=expl, size=9.5, color=SLATE, line_spacing=1.12)
        cy += hh + 0.06
    # caveat — the anti-hype half, kept because it is the judgment of the phase
    filled_rect(s, rx + 0.24, top + 3.58, rw - 0.48, 0.50, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.3, radius=True, radius_adj=0.08)
    text_box(s, x=rx + 0.40, y=top + 3.61, w=rw - 0.80, h=0.44,
             text="\"The first AI to stop a zero-day attack\" — one curated "
                  "case; \"AI finds 50% of vulnerabilities\" — the vendor\u2019s "
                  "own measurements on its own code [3].",
             size=9, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Durable pattern: a mandatory automated scan as a gate + an "
        "architectural break of the trifecta. The scan is necessary but NOT "
        "sufficient: thinking through what can go wrong at all is the "
        "human\u2019s work.",
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
# s30b (NEW, #162 round 3) — Amazon Q wiper incident, third
# mechanistically distinct supply-chain failure class
# ============================================================
def s30b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Trust is also needed in what the AI tool itself is made of",
        size=20, w=12.3, h=0.82)

    lx, lw = 0.55, 6.55
    rx, rw = 7.30, 5.50
    top = 1.44

    ocean_box(s, lx, top, lw, 4.10)
    icon(s, "package-x", lx + 0.22, top + 0.16, 0.48, "mid")
    text_box(s, x=lx + 0.84, y=top + 0.20, w=lw - 1.90, h=0.36,
             text="Amazon Q Developer, July 2025 [1]", size=13, bold=True,
             color=MID)
    add_image(s, ASSETS / "logos" / "aws-logo.png", lx + lw - 1.02, top + 0.16,
              0.72, 0.43)
    text_box(s, x=lx + lw - 1.10, y=top + 0.58, w=0.88, h=0.16,
             text="AWS · Wikimedia", size=6.5, italic=True, color=LIGHT,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=top + 0.68, w=lw - 0.48, h=1.36,
             text="An unaudited outside contributor merged a PR carrying a "
                  "\"system cleaner\" system prompt (aws s3 rb, stopping EC2, "
                  "deleting IAM users) into the official release of the VS "
                  "Code extension.",
             size=11, color=DEEP, line_spacing=1.18)
    text_box(s, x=lx + 0.24, y=top + 2.06, w=lw - 0.48, h=0.60,
             text="~1 million", size=24, bold=True, color=TEAL)
    text_box(s, x=lx + 0.24, y=top + 2.60, w=lw - 0.48, h=0.44,
             text="developers on release v1.84.0, before the v1.85.0 patch [2].",
             size=10.5, italic=True, color=DEEP)
    filled_rect(s, lx + 0.24, top + 3.14, lw - 0.48, 0.80, SOFT_GREY,
                stroke=SLATE, stroke_pt=0.8, radius=True, radius_adj=0.08)
    text_box(s, x=lx + 0.40, y=top + 3.20, w=lw - 0.80, h=0.68,
             text="The attack failed technically (the prompt\u2019s formatting "
                  "broke execution) — that is luck, not control.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.14,
             anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "layers", rx + 0.22, top + 0.16, 0.46, "teal")
    text_box(s, x=rx + 0.80, y=top + 0.20, w=rw - 1.04, h=0.36,
             text="Three mechanically different fronts", size=12.5, bold=True,
             color=MID)
    fronts = [
        ("Slopsquatting", "trust in a package name that AI advice "
         "recommended."),
        ("CamoLeak", "trust in someone else\u2019s untrusted text (a PR comment) "
         "inside the agent\u2019s context."),
        ("Amazon Q", "trust in the supply chain of the tool itself — not in "
         "its output and not in its input, but in what it is made of."),
    ]
    fy = top + 0.72
    for head, body in fronts:
        text_box(s, x=rx + 0.24, y=fy, w=rw - 0.48, h=0.30, text=head,
                 size=12, bold=True, color=DEEP)
        text_box(s, x=rx + 0.24, y=fy + 0.32, w=rw - 0.48, h=0.72, text=body,
                 size=10.5, color=DEEP, line_spacing=1.14)
        fy += 1.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Review is needed not only for the code your agent writes, but for the "
        "code the AI tool itself is made of.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s30b")
    notes_with_sources(s, "s30b")
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
    text_box(s, x=rx + 0.88, y=1.66, w=rw - 1.95, h=0.56,
             text="CamoLeak (prompt injection in a dev agent · Legit Security) [2]",
             size=11.5, bold=True, color=MID, line_spacing=1.05)
    add_image(s, ASSETS / "logos" / "copilot-logo.png", rx + rw - 0.86,
              1.62, 0.40, 0.40)
    text_box(s, x=rx + rw - 1.02, y=2.03, w=0.72, h=0.16,
             text="GitHub Copilot", size=6.5, italic=True,
             color=LIGHT, align=PP_ALIGN.CENTER)
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
    # Round-5 meme (EN caption bake): Domino Effect — one hallucinated package
    # name cascading into a full exploit chain (slopsquatting, left column).
    add_image(s, WEB / "band-domino-effect-en.png", 10.02, 6.40, 2.78, 0.64)
    refs_of_slide(s, "s31")
    notes_with_sources(s, "s31")
    return s
