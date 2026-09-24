"""Лекция 4 v4 — Band 2 (s11–s20): требования-провал, архитектура, реализация."""
from _helpers_en import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    right_arrow, circle, chip, connector, add_image, icon, slide_title,
    gold_callout, teal_callout, footer, src, speaker_notes, load_notes, notes_with_sources, refs_of_slide,
    build_section_divider, ref_list, refs_of, link_run, URLS,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE, COVER_OUTLINE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT, ICONS, CHARTS, ASSETS, WEB,
    FONT_MONO,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

SCR = ASSETS / "screenshots"


# ============================================================
# s11 — prompt-and-pray (iceberg hero + case + second failure)
# ============================================================
def s11(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "prompt-and-pray: the bug is not in the code, but in a requirement nobody checked",
        size=22, w=12.2, h=0.85)

    # left: iceberg ironic illustration
    lx, lw = 0.55, 4.55
    ocean_box(s, lx - 0.05, 1.55, lw + 0.10, 4.05, fill=WHITE, stroke=LIGHT)
    add_image(s, SCR / "s11-iceberg.jpg", lx + 0.08, 1.66, lw - 0.06, 3.05)
    text_box(s, x=lx + 0.12, y=4.78, w=lw - 0.12, h=0.78,
             text="The visible 'works in the demo' is the tip; below the water "
                  "are dozens of unstated assumptions the model defaulted on.",
             size=11, italic=True, color=MID, line_spacing=1.12,
             align=PP_ALIGN.CENTER)

    # right: case analysis
    rx, rw = 5.35, 7.45
    ocean_box(s, rx, 1.55, rw, 1.95)
    text_runs(s, rx + 0.24, 1.68, rw - 0.48, 1.72, [
        {"text": "prompt-and-pray", "size": 14, "bold": True, "color": MID},
        {"text": " — one vague prompt ('build me a booking system') "
                 "and hope. This skips the discipline: no requirements artifact, no "
                 "human checkpoint between intent and code.",
         "size": 12, "color": DEEP},
        {"text": "The model silently fills in the decisions: a booking in the past? "
                 "overlapping bookings? who cancels someone else's? time zones? — for "
                 "each it takes a plausible default. It 'works' in the demo, breaks on "
                 "the first real conflict.",
         "size": 12, "color": DEEP, "newpara": True, "space_before": 6,
         "line_spacing": 1.14},
    ])
    # coварство strip
    filled_rect(s, rx, 3.62, rw, 0.78, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=3.70, w=rw - 0.48, h=0.64,
             text="The code is correct relative to what the model assumed. "
                  "The bug is not in the code — it is that nobody checked the "
                  "assumptions; they are invisible in the code.",
             size=11.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.12)
    # second failure — overclaim спека=истина
    filled_rect(s, rx, 4.50, rw, 1.04, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.05)
    text_runs(s, rx + 0.24, 4.56, rw - 0.48, 0.92, [
        {"text": "The mirror-image extreme (Encarnacao, 'The Emperor's New Code'): ",
         "size": 10.5, "bold": True, "color": SLATE, "line_spacing": 1.12},
        {"text": "'the spec = the single truth, you need not read the code'. But a spec "
                 "underspecifies behavior; 'I'll regenerate from the spec' is a new "
                 "guess, not the same product. The code remains the source of truth.",
         "size": 10.5, "color": DEEP, "line_spacing": 1.12},
    ])

    gold_callout(
        s, 0.55, 5.70, 12.25, 0.58,
        "The bottleneck is not the model's ability to write code, but the precision "
        "of stating intent (essential complexity, Brooks [1]). "
        "The alternative is not 'no AI', but restoring the human checkpoint: "
        "requirements accepted before code [2].",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s12")
    notes_with_sources(s, "s12")
    return s


# ============================================================
# s12 — section divider Раздел 2 (Архитектура)
# ============================================================
def s12(p):
    return build_section_divider(
        p, here_idx=2,
        subtitle="Architecture — before code, and it must be managed",
        bridge="After requirements comes not code straight away, but architecture: "
               "deciding what to assemble the system from. This is essential "
               "complexity, led by the human; the leading practices — ADR, fitness "
               "functions, architecture-as-code — teach you to manage it with AI, "
               "not delegate it to AI.",
        sid="s13",
        tag="Thin phase · human leads · 1 failure")


# ============================================================
# s13 — architecture necessity (3-node chain + failure) [in-bucket]
# ============================================================
def s13(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "After requirements comes architecture, not code straight away",
                size=25, w=12.0, h=0.85)

    # left: three-node chain, middle highlighted
    lx, lw = 0.55, 6.10
    ocean_box(s, lx, 1.55, lw, 4.05)
    nodes = [
        ("what is needed", "requirements", LIGHT, False),
        ("what to assemble from", "architecture", GOLD, True),
        ("how to write", "code", LIGHT, False),
    ]
    ny = 1.85
    nw = lw - 0.60
    for i, (name, sub, col, hi) in enumerate(nodes):
        y = ny + i * 1.02
        if hi:
            filled_rect(s, lx + 0.30, y, nw, 0.86, GOLD_TINT, stroke=GOLD,
                        stroke_pt=2.0, radius=True, radius_adj=0.08)
        else:
            filled_rect(s, lx + 0.30, y, nw, 0.86, SURFACE, stroke=col,
                        stroke_pt=1.3, radius=True, radius_adj=0.08)
        text_box(s, x=lx + 0.52, y=y + 0.12, w=nw - 0.60, h=0.36, text=name,
                 size=15, bold=True, color=DEEP)
        text_box(s, x=lx + 0.52, y=y + 0.48, w=nw - 0.60, h=0.32, text=sub,
                 size=11.5, italic=True, color=(MID if hi else SLATE))
        if hi:
            text_box(s, x=lx + lw - 1.6, y=y + 0.08, w=1.35, h=0.7,
                     text="cannot\nskip", size=10.5, bold=True,
                     color=GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_spacing=0.95)
        if i < 2:
            text_box(s, x=lx + 0.30, y=y + 0.84, w=nw, h=0.20, text="▼",
                     size=13, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.30, y=4.98, w=nw, h=0.52,
             text="The phase's output is a small number of hard, hard-to-reverse "
                  "forks: component boundaries, the data model, the priority of "
                  "quality attributes.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.08)

    # right: failure of skipping the phase
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.55, rw, 4.05)
    text_box(s, x=rx + 0.24, y=1.68, w=rw - 0.48, h=0.40,
             text="Jump straight to code →", size=13.5, bold=True, color=MID)
    filled_rect(s, rx + 0.24, 2.18, rw - 0.48, 1.10, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "triangle-alert", rx + 0.42, 2.34, 0.46, "light")
    text_box(s, x=rx + 1.02, y=2.30, w=rw - 1.30, h=0.94,
             text="Architecture erosion — the gap between what was intended and "
                  "what was implemented, a decay in maintainability.",
             size=12, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    filled_rect(s, rx + 0.24, 3.42, rw - 0.48, 1.40, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.06)
    icon(s, "bomb", rx + 0.42, 3.58, 0.46, "light")
    text_box(s, x=rx + 1.02, y=3.52, w=rw - 1.30, h=1.24,
             text="Codebase cognitive debt (Thoughtworks Radar, Hold ring [2]): "
                  "the gap between how the system is built and the team's "
                  "understanding — it 'lives in people's heads', not in artifacts. "
                  "The remedy Radar names — architectural fitness functions [3].",
             size=11.5, color=DEEP, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.66,
        "'Deciding what to build' is essential complexity (Brooks, 'No Silver "
        "Bullet', 1986 [1]): a trade-off choice is not delegated. AI is useful only "
        "at the periphery — options, explaining a pattern, a draft diagram.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s14")
    notes_with_sources(s, "s14")
    return s


# ============================================================
# s14 — architecture approaches matrix (4 cols × 4 rows)
# ============================================================
def s14(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Four practices for managing architecture with AI (tools are secondary)",
        size=23, w=12.2, h=0.82)

    cols = [
        ("gavel", "ADR", MID),
        ("shield-check", "Fitness function", TEAL),
        ("layout-grid", "C4 / arch-as-code", MID),
        ("refresh-cw", "Evolutionary arch.", TEAL),
    ]
    rows = [
        ("What it is",
         ["Half a page of an immutable record per decision (context·decision·"
          "status·consequences); stores the 'why'",
          "Auto-check of an architectural attribute on every commit "
          "('payment does not depend on the UI'; 'response < 200 ms')",
          "Architecture machine-readably (C4: Context/Container/Component/Code; "
          "DSL — PlantUML/Mermaid/Structurizr)",
          "ADR + fitness functions + arch-as-code together = incrementality + "
          "managed change"]),
        ("Who prescribes it",
         ["Nygard 2011 [1]; Radar — ADOPT [4]",
          "Thoughtworks; Rebecca Parsons [4]",
          "Simon Brown (C4) [3]; Structurizr",
          "Ford, Parsons, Kua [2]"]),
        ("AI role (secondary)",
         ["edits, cross-checks — but the human decides and justifies",
          "convenient for writing fitness functions; they also validate generated code",
          "reads as context, generates diagrams; drift detection — "
          "Structurizr (model vs code)",
          "executes inside each of the three practices"]),
        ("Where the human is",
         ["the fork's author = the ADR's author",
          "decides which invariant is critical",
          "owns the textual model",
          "holds the direction of evolution"]),
    ]
    x0 = 0.55
    total = 12.25
    gap = 0.14
    cw = (total - gap * 3) / 4     # ~2.95
    top = 1.50
    # header row with icons
    hh = 0.72
    for i, (ic, name, col) in enumerate(cols):
        x = x0 + i * (cw + gap)
        filled_rect(s, x, top, cw, hh, col, radius=True, radius_adj=0.10)
        icon(s, ic, x + 0.14, top + 0.10, 0.5, "white")
        text_box(s, x=x + 0.72, y=top + 0.08, w=cw - 0.82, h=hh - 0.10,
                 text=name, size=12.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)
    # body rows
    row_h = [0.98, 0.62, 0.72, 0.50]
    ry = top + hh + 0.08
    for r, (label, cells) in enumerate(rows):
        rh = row_h[r]
        # row label chip on far-left overlap? Instead put label as tiny left tab
        for i in range(4):
            x = x0 + i * (cw + gap)
            fill = SURFACE if r % 2 == 0 else WHITE
            filled_rect(s, x, ry, cw, rh, fill, stroke=SOFT_GREY, stroke_pt=1.0,
                        radius=True, radius_adj=0.05)
            if i == 0:
                text_box(s, x=x + 0.12, y=ry + 0.04, w=cw - 0.24, h=0.22,
                         text=label.upper(), size=8.5, bold=True, color=LIGHT)
                tb_y = ry + 0.26
                tb_h = rh - 0.30
            else:
                tb_y = ry + 0.08
                tb_h = rh - 0.14
            text_box(s, x=x + 0.12, y=tb_y, w=cw - 0.24, h=tb_h,
                     text=cells[i], size=9.5, color=DEEP, line_spacing=1.04)
        ry += rh + 0.06

    gold_callout(
        s, 0.55, 5.94, 12.25, 0.66,
        "The durable pattern: automatic architectural control on every "
        "commit. Vendor hype: 'our product will ensure the architecture itself'. "
        "The human owns the 'why', AI codes and checks.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s15", y=7.08)
    notes_with_sources(s, "s15")
    return s


# ============================================================
# s15 — poisoned context (cycle + caveat + alternative) [in-bucket]
# ============================================================
def s15(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Poisoned context: AI does not tell 'how it ended up' from 'how it's right'",
        size=22, w=12.2, h=0.82)

    # top caveat #261 band
    filled_rect(s, 0.55, 1.44, 12.25, 0.56, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.06)
    text_box(s, x=0.80, y=1.51, w=11.75, h=0.44,
             text="This happens WHEN the architecture is not described and there is "
                  "no process for managing it. With practices in place (ADR, fitness "
                  "functions, arch-as-code) the loop breaks.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    # left: poisoning cycle
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 2.14, lw, 3.42)
    text_box(s, x=lx + 0.24, y=2.24, w=lw - 0.48, h=0.36,
             text="The poisoning loop (Böckeler 2026, Thoughtworks) [1]",
             size=12.5, bold=True, color=MID)
    loop = [
        ("bad design", GOLD, True),
        ("AI copies ('how it's done here')", MID, False),
        ("worse design", LIGHT, False),
        ("AI copies even more confidently", MID, False),
    ]
    ly = 2.70
    for i, (txt, col, start) in enumerate(loop):
        y = ly + i * 0.62
        filled_rect(s, lx + 0.30, y, lw - 0.60, 0.48,
                    (GOLD_TINT if start else SURFACE),
                    stroke=(GOLD if start else col), stroke_pt=(1.8 if start else 1.2),
                    radius=True, radius_adj=0.10)
        if start:
            circle(s, lx + 0.40, y + 0.13, 0.22, GOLD)
        text_box(s, x=lx + (0.74 if start else 0.48), y=y + 0.03, w=lw - 1.1,
                 h=0.42, text=txt, size=11.5, bold=start, color=DEEP,
                 anchor=MSO_ANCHOR.MIDDLE)
        if i < 3:
            text_box(s, x=lx + 0.30, y=y + 0.46, w=lw - 0.60, h=0.16, text="↓",
                     size=12, bold=True, color=LIGHT, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.24, y=5.16, w=lw - 0.48, h=0.34,
             text="Böckeler, honestly: 'we don't yet have a good way to mitigate this'.",
             size=10.5, italic=True, color=SLATE)

    # right: alternative (3 plates, bridge to s14)
    rx, rw = 6.85, 5.95
    alts = [
        ("user-check", "The human owns the forks",
         "makes the architectural decisions; AI at the periphery under human choice."),
        ("gavel", "ADR [2]",
         "human-written context 'we decided X because Y, rejected Z' — "
         "shared understanding against poisoning."),
        ("shield-check", "Fitness functions + modular code [3]",
         "deterministic invariants break the loop; clear components give "
         "managed context."),
    ]
    ay = 2.14
    for i, (ic, head, body) in enumerate(alts):
        y = ay + i * 1.16
        ocean_box(s, rx, y, rw, 1.04)
        icon(s, ic, rx + 0.22, y + 0.24, 0.5, "teal")
        text_box(s, x=rx + 0.86, y=y + 0.12, w=rw - 1.06, h=0.34, text=head,
                 size=12.5, bold=True, color=MID)
        text_box(s, x=rx + 0.86, y=y + 0.46, w=rw - 1.06, h=0.52, text=body,
                 size=10.5, color=DEEP, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "AI sees a pattern and continues it — it does not tell a good example from a "
        "bad one. The worse the existing architecture, the more strongly AI entrenches it.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s16")
    notes_with_sources(s, "s16")
    return s


# ============================================================
# s16 — section divider Раздел 3 (Реализация)
# ============================================================
def s16(p):
    return build_section_divider(
        p, here_idx=3,
        subtitle="Implementation — discipline and harness",
        bridge="Here AI writes code, and the phase is strong — but strong under "
               "discipline. Three practices hold reliability: split into small "
               "verifiable units, maintain a persistent memory layer in the "
               "repository, and surround the model with a deterministic harness.",
        sid="s17",
        tag="Strong phase · three practices · 2 failures")


# ============================================================
# s17 — small units + explore→plan→code→commit pipeline
# ============================================================
def s17(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Working discipline: small verifiable units + the explore→plan→code→commit loop",
        size=21, w=12.3, h=0.82)

    # pipeline main visual — 4 stages with RIGHT_ARROW
    stages = [
        ("scan-search", "explore", "explore the code"),
        ("clipboard-list", "plan", "approve the plan"),
        ("code", "code", "write"),
        ("git-merge", "commit", "commit"),
    ]
    n = len(stages)
    x0 = 0.55
    total = 12.25
    aw = 0.55                       # arrow width
    sw = (total - aw * (n - 1)) / n  # stage width ~2.65
    py = 1.55
    ph = 1.28
    for i, (ic, name, owner) in enumerate(stages):
        x = x0 + i * (sw + aw)
        locked = i < 2
        ocean_box(s, x, py, sw, ph,
                  fill=(GOLD_TINT if locked else SURFACE),
                  stroke=(GOLD if locked else MID), stroke_pt=1.6)
        icon(s, ic, x + 0.20, py + 0.18, 0.5, "gold" if locked else "mid")
        text_box(s, x=x + 0.80, y=py + 0.18, w=sw - 0.95, h=0.42, text=name,
                 size=15, bold=True, color=DEEP, font="DejaVu Sans Mono")
        text_box(s, x=x + 0.20, y=py + 0.72, w=sw - 0.36, h=0.44, text=owner,
                 size=11, italic=True, color=SLATE)
        if i < n - 1:
            right_arrow(s, x + sw + 0.03, py + ph / 2 - 0.14, aw - 0.06, 0.28,
                        fill=LIGHT)
    text_box(s, x=0.55, y=2.90, w=12.25, h=0.32,
             text="The order is enforced: generation before exploration and a plan "
                  "is prompt-and-pray at the code level.   — the explore→plan→"
                  "code→commit loop, Anthropic [1]",
             size=11.5, italic=True, bold=True, color=MID, align=PP_ALIGN.CENTER)

    # bottom-left: small units
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.36, lw, 2.14)
    icon(s, "split", lx + 0.24, 3.50, 0.5, "mid")
    text_box(s, x=lx + 0.88, y=3.54, w=lw - 1.10, h=0.40,
             text="Small verifiable units", size=13, bold=True, color=MID)
    text_box(s, x=lx + 0.24, y=4.02, w=lw - 0.48, h=1.42,
             text="Each piece is implemented and verified in isolation: AI gets a "
                  "deterministic self-check, the human gets a small diff that can "
                  "actually be reviewed. Osmani [2]: the smaller the AI's proposal, "
                  "the more real the review; a giant diff goes unread.",
             size=11, color=DEEP, line_spacing=1.16)

    # bottom-right: role split
    rx, rw = 6.85, 5.95
    filled_rect(s, rx, 3.36, rw, 1.02, TEAL_TINT, stroke=TEAL, stroke_pt=1.4,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 3.46, rw - 0.48, 0.86, [
        {"text": "AI takes the accidental complexity", "size": 12, "bold": True,
         "color": TEAL},
        {"text": " (boilerplate, a routine handler). ", "size": 12,
         "color": DEEP},
        {"text": "The human takes the essential", "size": 12, "bold": True,
         "color": DEEP},
        {"text": ": what we're building, what's risky, what's correct, whether it can merge. [3]",
         "size": 12, "color": DEEP},
    ])
    filled_rect(s, rx, 4.50, rw, 1.00, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_box(s, x=rx + 0.24, y=4.58, w=rw - 0.48, h=0.86,
             text="AI takes part in two philosophies — in the editor (synchronously) "
                  "and asynchronously (in isolation → PR); this is a property of the "
                  "mode, we'll cover it secondarily.",
             size=11, italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The discipline of the loop and the small diff is not bureaucracy, but a way "
        "to keep AI in the zone where the human really controls the result.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s18")
    notes_with_sources(s, "s18")
    return s


# ============================================================
# s18 — persistent memory layer (architecture: dev ↔ repo → agent)
# ============================================================
def s18(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "A persistent memory layer in the repository — what the agent reads every session",
        size=21, w=12.3, h=0.82)

    # architecture row: DEVELOPER — REPO — AGENT
    ay = 1.55
    ah = 1.60
    # developer (human, curates)
    dx, dw = 0.55, 2.70
    ocean_box(s, dx, ay, dw, ah)
    icon(s, "user-check", dx + dw / 2 - 0.32, ay + 0.22, 0.64, "teal")
    text_box(s, x=dx + 0.1, y=ay + 0.94, w=dw - 0.2, h=0.34, text="DEVELOPER",
             size=12.5, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=dx + 0.1, y=ay + 1.24, w=dw - 0.2, h=0.30, text="curates the layer",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER)
    # repo (persistent layer)
    rx2, rw2 = 4.10, 5.10
    ocean_box(s, rx2, ay, rw2, ah, fill=SURFACE, stroke=MID, stroke_pt=1.8)
    icon(s, "database", rx2 + 0.22, ay + 0.20, 0.5, "mid")
    text_box(s, x=rx2 + 0.82, y=ay + 0.22, w=rw2 - 1.0, h=0.36,
             text="REPOSITORY — the persistent layer", size=12.5, bold=True,
             color=MID)
    text_box(s, x=rx2 + 0.24, y=ay + 0.66, w=rw2 - 0.48, h=0.86,
             text="AGENTS.md (the agents.md standard, Linux Foundation [1]; "
                  "build/test commands, style, guardrails; the analog of CLAUDE.md) · "
                  "memory notes · the operational history of tasks. "
                  "Rule: lead with commands, not explanations.",
             size=10.5, color=DEEP, line_spacing=1.12)
    # agent (stateless, reads each session)
    gx, gw = 9.55, 3.25
    ocean_box(s, gx, ay, gw, ah)
    icon(s, "bot", gx + gw / 2 - 0.32, ay + 0.22, 0.64, "mid")
    text_box(s, x=gx + 0.1, y=ay + 0.94, w=gw - 0.2, h=0.34,
             text="AGENT (stateless)", size=12.5, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=gx + 0.1, y=ay + 1.24, w=gw - 0.2, h=0.30,
             text="reads the layer every session", size=10.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER)
    # arrows
    connector(s, dx + dw, ay + ah / 2, rx2, ay + ah / 2, color=TEAL, width=2.4)
    right_arrow(s, rx2 + rw2 + 0.02, ay + ah / 2 - 0.14, 0.30, 0.28, fill=MID)

    # context-engineering block
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 3.36, lw, 2.14)
    text_box(s, x=lx + 0.24, y=3.48, w=lw - 0.48, h=0.36,
             text="context engineering — 3 curation primitives (Anthropic) [3]",
             size=12.5, bold=True, color=MID)
    prims = ["JIT retrieval", "compaction", "memory notes"]
    px = lx + 0.30
    for pr in prims:
        chip(s, px, 3.92, 1.85, 0.42, pr, fill=TEAL, color=WHITE, size=11)
        px += 1.95
    text_box(s, x=lx + 0.24, y=4.50, w=lw - 0.48, h=0.92,
             text="Principle: more context != better. Curate it right, not just "
                  "accumulate.",
             size=11, color=DEEP, line_spacing=1.14)

    # failure: context rot
    rx3, rw3 = 6.85, 5.95
    filled_rect(s, rx3, 3.36, rw3, 2.14, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.05)
    icon(s, "flame", rx3 + 0.24, 3.50, 0.5, "light")
    text_box(s, x=rx3 + 0.88, y=3.54, w=rw3 - 1.10, h=0.40,
             text="context rot (Chroma, 18 models) [2]", size=12.5, bold=True,
             color=DEEP)
    text_box(s, x=rx3 + 0.24, y=4.04, w=rw3 - 0.48, h=0.78,
             text="Retrieval accuracy drops non-linearly as input grows — "
                  "degradation starts BEFORE the window overflows. 'Stale "
                  "context rots'.",
             size=11, color=DEEP, line_spacing=1.14)
    text_box(s, x=rx3 + 0.24, y=4.86, w=rw3 - 0.48, h=0.58,
             text="Baseline: a memory demo — peak ~172k vs ~334k tokens without memory "
                  "— a cookbook demonstration of direction, not a controlled multiplier.",
             size=10, italic=True, color=SLATE, line_spacing=1.1)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Context lives in the repository, not in the prompt. The durable pattern is "
        "a curated persistent layer; the hype is 'our AGENTS.md will decide everything itself'.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s19")
    notes_with_sources(s, "s19")
    return s


# ============================================================
# s18b — the honest limit of EACH of the four context levels (#172 EN sync
# of the round-6 RU rebuild). Four cards, strictly parallel to the four
# levels of the preceding slide: same order, same alternating mid/teal.
# ============================================================
def s18b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Every level has its own limit — the risk changes, it does not disappear",
        size=21, w=12.3, h=0.74)

    cards = [
        ("shield-alert", "mid", MID, "LEVEL 1 · INSTRUCTIONS",
         "A stale file is worse than no file",
         "A missing file the agent makes up for by asking; a stale one it "
         "trusts literally.\n\nIt prescribes a build command that was replaced "
         "long ago — the agent keeps running it and burns turns for nothing."),
        ("layers", "teal", TEAL, "LEVEL 2 · SESSION",
         "Compaction loses, JIT will not ask",
         "Summarization is lossy: \"do not use library X\" may not survive into "
         "the summary, and the agent will propose exactly that. No error is "
         "raised.\n\nJIT is symmetric: what the agent does not know exists, it "
         "will never request."),
        ("clock", "mid", MID, "LEVEL 3 · HISTORY",
         "Ages more quietly than instructions",
         "There is one instruction file — it gets re-read along with the "
         "project. An archive of write-ups is dozens of documents.\n\nThe agent "
         "finds them by relevance, not by currency, and proposes a workaround "
         "for a problem closed long ago."),
        ("lock", "teal", TEAL, "LEVEL 4 · MEMORY",
         "Entrenches a wrong conclusion",
         "Memory accumulates on its own, so it cannot be proofread line by line "
         "like a file.\n\nA wrong belief, once retained and read only by the "
         "agent itself, keeps being reproduced — it needs periodic checking "
         "from outside, not editing."),
    ]
    cw, gap = 2.95, 0.15
    x0 = 0.55
    top = 1.42
    ch = 3.34
    for i, (ic, var, col, lvl, head, body) in enumerate(cards):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, top, cw, ch, fill=SURFACE, stroke=col, stroke_pt=1.5)
        icon(s, ic, x + 0.22, top + 0.18, 0.44, var)
        text_box(s, x=x + 0.22, y=top + 0.72, w=cw - 0.44, h=0.20, text=lvl,
                 size=8.5, bold=True, color=LIGHT, line_spacing=1.0)
        text_box(s, x=x + 0.22, y=top + 0.94, w=cw - 0.44, h=0.56, text=head,
                 size=12.5, bold=True, color=col, line_spacing=1.06)
        text_box(s, x=x + 0.22, y=top + 1.50, w=cw - 0.44, h=1.74, text=body,
                 size=9.5, color=DEEP, line_spacing=1.16)

    filled_rect(s, 0.55, 4.92, 12.25, 0.60, SOFT_GREY, stroke=LIGHT,
                stroke_pt=1.0, radius=True, radius_adj=0.08)
    text_box(s, x=0.79, y=4.99, w=11.8, h=0.46,
             text="No curation technique removes the risk — each one trades one "
                  "risk for another. That is a limit of the technique itself, not "
                  "a consequence of applying it carelessly.",
             size=12, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "Hence the allocation rule: a decision you cannot afford to lose silently "
        "is not trusted to level 2 — it is recorded at level 1, the only one that "
        "is not compressed between turns.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s18b")
    notes_with_sources(s, "s18b")
    return s


# ============================================================
# s19 — harness gate (model in centre, deterministic frame + feedback loop)
# ============================================================
def s19(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(s, "A deterministic scaffold-gate around a non-deterministic model",
                size=23, w=12.2, h=0.82)

    # left: model surrounded by frame
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.55, lw, 3.95)
    # frame checks (top row)
    checks = ["linters", "structural tests", "fitness functions",
              "SAST gate", "least-privilege", "sandbox"]
    cx = lx + 0.28
    cyr = 1.66
    per = 3
    cwid = (lw - 0.56 - 0.2 * (per - 1)) / per
    for i, ch in enumerate(checks):
        col = i % per
        row = i // per
        x = lx + 0.28 + col * (cwid + 0.2)
        y = cyr + row * 0.52
        chip(s, x, y, cwid, 0.44, ch, fill=MID, color=WHITE, size=9.5)
    # acronym gloss for the two non-obvious chips (#162 round 6 block 1 /
    # #172 EN sync, README §5.8b: expand at the FIRST VISIBLE use, not only
    # in the speaker notes)
    text_box(s, x=lx + 0.28, y=2.66, w=lw - 0.56, h=0.34,
             text="SAST — static application security testing: analysis of code "
                  "for vulnerabilities without running it. least-privilege — the "
                  "minimum rights needed, nothing more.",
             size=9.5, italic=True, color=MID, line_spacing=1.08)
    # model in centre
    circle(s, lx + lw / 2 - 0.62, 3.02, 1.24, GOLD_TINT, stroke=GOLD,
           stroke_pt=2.0)
    icon(s, "cpu", lx + lw / 2 - 0.34, 3.16, 0.56, "gold")
    text_box(s, x=lx + lw / 2 - 0.9, y=3.72, w=1.8, h=0.34,
             text="MODEL", size=11.5, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.28, y=4.40, w=lw - 0.56, h=0.86,
             text="Reliability is not 'give the model more freedom', but narrowing "
                  "its decision space. The model is non-deterministic (one prompt "
                  "→ different answers); the harness is deterministic (a test either "
                  "passed or not).",
             size=10.5, color=DEEP, line_spacing=1.12, align=PP_ALIGN.CENTER)
    text_box(s, x=lx + 0.28, y=5.24, w=lw - 0.56, h=0.24,
             text="— Böckeler 2026, harness engineering [1]",
             size=9, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)

    # right: feedback loop + honest limit
    rx, rw = 6.85, 5.95
    ocean_box(s, rx, 1.55, rw, 1.95)
    text_box(s, x=rx + 0.24, y=1.66, w=rw - 0.48, h=0.36,
             text="The feedback loop — the main mechanism", size=12.5,
             bold=True, color=MID)
    text_box(s, x=rx + 0.24, y=2.06, w=rw - 0.48, h=1.36,
             text="The agent stalls → that's a signal of a hole in the scaffold → add "
                  "the missing piece back:\n"
                  "• a command was missing → into AGENTS.md\n"
                  "• an invariant was violated → a fitness function [3]\n"
                  "• unsafe → a SAST gate",
             size=11, color=DEEP, line_spacing=1.22)
    # honest limit (in-bucket)
    filled_rect(s, rx, 3.62, rw, 0.90, TEAL_TINT, stroke=TEAL, stroke_pt=1.5,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 3.72, rw - 0.48, 0.72, [
        {"text": "Guardrails != verification. ", "size": 12, "bold": True,
         "color": TEAL},
        {"text": "A linter knows the code is formatted — it does not know whether it "
                 "solves the right problem. The scaffold does not check behavior.",
         "size": 11.5, "color": DEEP, "line_spacing": 1.12},
    ])
    # three layers
    filled_rect(s, rx, 4.64, rw, 0.86, SOFT_GREY, stroke=LIGHT, stroke_pt=1.0,
                radius=True, radius_adj=0.06)
    text_runs(s, rx + 0.24, 4.71, rw - 0.48, 0.74, [
        {"text": "Three layers, none replaces another: harness + behavioral "
                 "tests + human at merge. ", "size": 11.5, "bold": True,
         "color": DEEP, "line_spacing": 1.10},
        {"text": "Willison: 'review it — or it's not engineering' (vibe engineering) [2].",
         "size": 10, "italic": True, "color": LIGHT},
    ], anchor=MSO_ANCHOR.MIDDLE)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "A deterministic scaffold holds the non-deterministic model: we narrow the "
        "decision space, not give more freedom.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20")
    notes_with_sources(s, "s20")
    return s


# ============================================================
# s20b — Skills: what a skill is actually worth in development
# (three real dev skills + the boundary + the honest cross-vendor limit)
# ============================================================
def s20b(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "In development, a skill pays off on a rare but repeatable procedure",
        size=20, w=12.25, h=0.60)

    # ---- LEFT: three genuinely common dev skills (majority of visual weight)
    lx, lw = 0.55, 7.30
    text_box(s, x=lx, y=1.08, w=lw, h=0.28,
             text="WHAT DEVELOPERS ACTUALLY MOVE INTO A SKILL",
             size=12, bold=True, color=LIGHT)

    dev_skills = [
        ("terminal", "teal", TEAL,
         "Run every check with one command",
         "Linter → type check → tests (ruff/mypy/pytest or eslint/tsc/vitest) "
         "are invoked in a single call, instead of being reconstructed from "
         "scratch against this repository's conventions."),
        ("database", "mid", MID,
         "A throwaway database for an integration test",
         "How to bring up a real Postgres or Kafka in a container for the "
         "duration of a run and tear it down after. The procedure is written "
         "down — the agent is not recalling the configuration from memory."),
        ("file-code", "teal", TEAL,
         "Building documentation from the code",
         "Walk the project structure and its dependencies, assemble the README "
         "and the architecture decision records. Many steps, needed rarely — "
         "exactly the profile a skill exists for."),
    ]
    cy, chh, cgap = 1.38, 1.22, 0.10
    for ic, var, col, head, body in dev_skills:
        ocean_box(s, lx, cy, lw, chh)
        icon(s, ic, lx + 0.22, cy + 0.16, 0.44, var)
        text_box(s, x=lx + 0.82, y=cy + 0.14, w=lw - 1.04, h=0.30,
                 text=head, size=13, bold=True, color=col)
        text_box(s, x=lx + 0.82, y=cy + 0.48, w=lw - 1.04, h=0.62,
                 text=body, size=11, color=DEEP, line_spacing=1.12)
        cy += chh + cgap

    # example line — one token per card, same convention as the deck's matrices
    text_runs(s, lx, cy + 0.08, lw, 0.28, [
        {"text": "Example:  ", "size": 10, "bold": True, "color": SLATE},
        {"text": "lint+type-check+test skill", "size": 9,
         "italic": True, "color": TEAL, "font": FONT_MONO},
        {"text": "  ·  ", "size": 9, "color": SLATE},
        {"text": "testcontainers-docker skill", "size": 9, "italic": True,
         "color": MID, "font": FONT_MONO},
        {"text": "  ·  ", "size": 9, "color": SLATE},
        {"text": "README Generator skill", "size": 9, "italic": True,
         "color": TEAL, "font": FONT_MONO},
    ])

    # ---- RIGHT: the boundary — when a skill is the WRONG answer
    rx, rw = 8.05, 4.77
    ocean_box(s, rx, 1.08, rw, 1.56, fill=SOFT_GREY, stroke=SLATE,
              stroke_pt=1.2)
    icon(s, "circle-slash", rx + 0.20, 1.18, 0.40, "mid")
    text_box(s, x=rx + 0.72, y=1.20, w=rw - 0.92, h=0.28,
             text="When a skill is not the answer", size=12.5, bold=True,
             color=DEEP)
    # each line kept short enough to NOT wrap — a wrapped bullet loses its
    # hanging indent here and reads as a fifth item
    text_box(s, x=rx + 0.22, y=1.58, w=rw - 0.44, h=1.08,
             text="• needed every turn (build, tests) — that is AGENTS.md\n"
                  "• a one-off task — just ask for it in chat\n"
                  "• one fact, not a procedure — a line in AGENTS.md\n"
                  "• \"everything at once\" — the model will not pick it",
             size=10.5, color=DEEP, line_spacing=1.30)

    # loading-mode mechanic — kept, but compact (this is WHY the split works)
    my = 3.02
    filled_rect(s, rx, my, rw, 1.10, SURFACE, stroke=LIGHT, stroke_pt=1.2,
                radius=True, radius_adj=0.08)
    text_runs(s, rx + 0.20, my + 0.14, rw - 0.40, 0.88, [
        {"text": "AGENTS.md", "size": 11, "bold": True, "color": MID},
        {"text": " — in context every turn; you pay for it always.",
         "size": 10.5, "color": DEEP},
        {"text": "SKILL.md", "size": 11, "bold": True, "color": TEAL,
         "newpara": True, "space_before": 4},
        {"text": " — loaded only on call; until then it costs zero.",
         "size": 10.5, "color": DEEP},
    ], line_spacing=1.14)

    text_box(s, x=rx, y=4.34, w=rw, h=1.10,
             text="Honestly: the format is open (the Agent Skills standard) and "
                  "confirmed in Codex CLI, but Cursor has no on-demand layer — "
                  "there the rules are always active. \"The tool supports "
                  "skills\" is worth double-checking.",
             size=10.5, italic=True, color=SLATE, line_spacing=1.16)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The dividing rule: needed every turn — into AGENTS.md; rare but "
        "detailed — into a skill; once — just say it in chat.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20b")
    notes_with_sources(s, "s20b")
    return s


# ============================================================
# s20c — MCP for a coding agent (agent + 3 servers + subset bar +
# risk → mitigation, bridging to the lethal trifecta)
# ============================================================
def s20c(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "MCP removes the human bridge — at the cost of narrower system access",
        size=20, w=12.3, h=0.60)

    # top: agent + 3 MCP server cards
    ay = 1.26
    ah = 1.42
    agx, agw = 0.55, 2.10
    ocean_box(s, agx, ay, agw, ah)
    icon(s, "bot", agx + agw / 2 - 0.27, ay + 0.14, 0.54, "mid")
    text_box(s, x=agx + 0.06, y=ay + 0.74, w=agw - 0.12, h=0.28,
             text="AGENT", size=12, bold=True, color=DEEP, align=PP_ALIGN.CENTER)
    text_box(s, x=agx + 0.06, y=ay + 1.02, w=agw - 0.12, h=0.40,
             text="built in: files + shell", size=9.5, italic=True,
             color=SLATE, align=PP_ALIGN.CENTER, line_spacing=1.05)

    cards = [
        ("boxes", "GitHub MCP", "issues, pull requests, builds — by toolsets "
         "that are enabled selectively"),
        ("scan-search", "Playwright MCP", "the browser: a structural tree of "
         "elements instead of a screenshot; clicks, fills in forms"),
        ("link", "Filesystem MCP", "a class of servers: access to directories "
         "OUTSIDE the working copy — a neighboring repo, a shared disk"),
    ]
    cx0 = agx + agw + 0.55
    ctotal = 13.333 - 0.55 - cx0
    cgap = 0.18
    ccw = (ctotal - cgap * 2) / 3
    # single connector rail ABOVE the cards (clear of all body text)
    rail_y = ay - 0.14
    connector(s, agx + agw / 2, ay, agx + agw / 2, rail_y, color=TEAL,
              width=1.6, dash="dash")
    connector(s, agx + agw / 2, rail_y, cx0 + 2 * (ccw + cgap) + ccw / 2, rail_y,
              color=TEAL, width=1.6, dash="dash")
    for i, (ic, name, body) in enumerate(cards):
        x = cx0 + i * (ccw + cgap)
        ocean_box(s, x, ay, ccw, ah)
        icon(s, ic, x + 0.18, ay + 0.12, 0.40, "teal")
        text_box(s, x=x + 0.66, y=ay + 0.14, w=ccw - 0.82, h=0.32,
                 text=name, size=12, bold=True, color=MID)
        text_box(s, x=x + 0.18, y=ay + 0.52, w=ccw - 0.36, h=0.82,
                 text=body, size=9.5, color=DEEP, line_spacing=1.10)
        connector(s, x + ccw / 2, rail_y, x + ccw / 2, ay, color=TEAL,
                  width=1.6, dash="dash")

    # ---- MCP vs direct API / command line: an MCP server is a SUBSET ----
    ny = ay + ah + 0.14
    nh = 1.08
    ocean_box(s, 0.55, ny, 12.25, nh)
    text_box(s, x=0.79, y=ny + 0.10, w=5.10, h=0.28,
             text="MCP is narrower than direct access", size=12.5, bold=True,
             color=MID)
    b1y = ny + 0.42
    filled_rect(s, 0.79, b1y, 4.90, 0.26, SOFT_GREY, stroke=SLATE,
                stroke_pt=0.75, radius=True, radius_adj=0.30)
    text_box(s, x=0.91, y=b1y + 0.01, w=4.70, h=0.24,
             text="the system's full interface: its API and its terminal command",
             size=9, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    b2y = b1y + 0.32
    filled_rect(s, 0.79, b2y, 2.15, 0.26, MID, radius=True, radius_adj=0.30)
    text_box(s, x=0.91, y=b2y + 0.01, w=1.95, h=0.24,
             text="the MCP toolset", size=9, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=3.06, y=b2y + 0.01, w=2.90, h=0.24,
             text="— a subset, not the whole interface", size=9,
             italic=True, color=SLATE, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=6.15, y=ny + 0.12, w=6.45, h=0.86,
             text="The server publishes a curated set of tools rather than the "
                  "system's whole interface: what is not in the set is out of "
                  "reach for the agent, even if the system can do it. And every "
                  "tool schema occupies context permanently — so where the agent "
                  "already has a shell, a narrow command is often cheaper than an "
                  "MCP call.",
             size=10, color=DEEP, line_spacing=1.14)

    # ---- risk  →  mitigation (explicit, sequential) ----
    by = ny + nh + 0.14
    bh = 1.52
    lwb = 5.75
    ocean_box(s, 0.55, by, lwb, bh, fill=SOFT_GREY, stroke=SLATE, stroke_pt=1.2)
    icon(s, "shield-alert", 0.77, by + 0.12, 0.40, "mid")
    text_box(s, x=1.25, y=by + 0.14, w=lwb - 0.92, h=0.28,
             text="The danger: one connection — two corners out of three",
             size=11, bold=True, color=DEEP)
    text_box(s, x=0.77, y=by + 0.46, w=lwb - 0.44, h=1.00,
             text="The lethal trifecta: access to data + a channel out + "
                  "untrusted content. One server usually grants the first two at "
                  "once, and the third arrives through the same channel. "
                  "Documented: instructions hidden in public issues exfiltrated "
                  "private-repository data through the pull requests the agent "
                  "created.",
             size=9.5, color=DEEP, line_spacing=1.10)

    right_arrow(s, 6.42, by + bh / 2 - 0.20, 0.50, 0.40, fill=GOLD)

    rwb = 5.75
    rxb = 7.05
    ocean_box(s, rxb, by, rwb, bh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.5)
    icon(s, "shield-check", rxb + 0.22, by + 0.12, 0.40, "teal")
    text_box(s, x=rxb + 0.70, y=by + 0.14, w=rwb - 0.92, h=0.28,
             text="What closes it", size=11.5, bold=True, color=TEAL)
    text_box(s, x=rxb + 0.22, y=by + 0.44, w=rwb - 0.44, h=1.02,
             text="1. Read-only by default — write tools are skipped, even if "
                  "the agent asked for them.\n"
                  "2. Write access is opened for a specific task, as a separate "
                  "decision, not an out-of-the-box setting.\n"
                  "3. The fewest servers connected — fewer corners, less context.",
             size=9.5, color=DEEP, line_spacing=1.10)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "This is a risk, not a convenience: read-only by default, and write "
        "access opened deliberately and per task.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20c")
    notes_with_sources(s, "s20c")
    return s


# ============================================================
# s20e — task-logging layer: three patterns as a progression of complexity
# (+ the fourth option: the tracker). Presents BEFORE s20d, per the
# round-3 order swap that the RU deck carries.
# ============================================================
def s20e(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Task logging is grown to fit the task, not taken at maximum",
        size=20, w=12.3, h=0.60)

    x0 = 0.55
    total = 12.25
    gap = 0.16
    cw = (total - gap * 2) / 3

    # progression caption — the ordering principle, stated outright
    text_box(s, x=x0, y=1.06, w=total, h=0.26,
             text="COMPLEXITY GROWS LEFT TO RIGHT:  one file  →  a set of files "
                  "in one folder  →  a folder structure",
             size=11, bold=True, color=LIGHT)

    cols = [
        ("list-ordered", "(a) One file — a shared log", LIGHT),
        ("clipboard-list", "(b) A folder, one file per task", MID),
        ("file-stack", "(c) A folder per task + files", DEEP),
    ]
    rows = [
        ("Solo or a team",
         ["A team — one shared chronology, but frequent merge conflicts",
          "A mid-sized team — fewer conflicts",
          "One developer or a small team; breeds directories"]),
        ("Task lifetime",
         ["Short, frequent",
          "\"1 context window = 1 pull request\"",
          "Long-lived, complex"]),
        ("Audit trail",
         ["Chronological — \"what and when\"",
          "Partial — outcome + structured fields",
          "Detailed — intermediate steps of the reasoning"]),
    ]
    examples = ["notes/decisions.md", "Backlog.md", "notes/research/*.md"]

    top = 1.30
    hh = 0.52
    for i, (ic, name, col) in enumerate(cols):
        x = x0 + i * (cw + gap)
        filled_rect(s, x, top, cw, hh, col, radius=True, radius_adj=0.12)
        icon(s, ic, x + 0.14, top + 0.06, 0.40, "white")
        text_box(s, x=x + 0.62, y=top + 0.03, w=cw - 0.72, h=hh - 0.06,
                 text=name, size=11.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.98)

    row_h = [0.80, 0.58, 0.72]
    ry = top + hh + 0.06
    for r, (label, cells) in enumerate(rows):
        rh = row_h[r]
        for i in range(3):
            x = x0 + i * (cw + gap)
            fill = SURFACE if r % 2 == 0 else WHITE
            filled_rect(s, x, ry, cw, rh, fill, stroke=SOFT_GREY, stroke_pt=1.0,
                        radius=True, radius_adj=0.06)
            if i == 0:
                text_box(s, x=x + 0.14, y=ry + 0.04, w=cw - 0.28, h=0.24,
                         text=label.upper(), size=12, bold=True, color=LIGHT)
                tb_y = ry + 0.30
                tb_h = rh - 0.36
            else:
                tb_y = ry + 0.07
                tb_h = rh - 0.14
            text_box(s, x=x + 0.14, y=tb_y, w=cw - 0.28, h=tb_h,
                     text=cells[i], size=13, color=DEEP, line_spacing=1.06)
        ry += rh + 0.06

    # compact example line — one token per column, not a full sentence
    ey = ry + 0.00
    text_runs(s, x0, ey, total, 0.30, [
        {"text": "Example:  ", "size": 11, "bold": True, "color": SLATE},
        {"text": examples[0], "size": 11, "italic": True, "color": LIGHT,
         "font": FONT_MONO},
        {"text": "   ·   ", "size": 11, "color": SLATE},
        {"text": examples[1], "size": 11, "italic": True, "color": MID,
         "font": FONT_MONO},
        {"text": "   ·   ", "size": 11, "color": SLATE},
        {"text": examples[2], "size": 11, "italic": True, "color": DEEP,
         "font": FONT_MONO},
    ])

    # ---- the fourth option: keep the log in the tracker, not in the repo ----
    ny = ey + 0.32
    nh = 1.14
    lwn = 8.20
    ocean_box(s, x0, ny, lwn, nh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.4)
    icon(s, "layout-grid", x0 + 0.18, ny + 0.08, 0.38, "teal")
    text_box(s, x=x0 + 0.64, y=ny + 0.09, w=lwn - 0.84, h=0.26,
             text="A fourth option — the log in the tracker (Jira, Linear, "
                  "GitHub Issues)",
             size=11, bold=True, color=TEAL)
    text_runs(s, x0 + 0.18, ny + 0.44, lwn - 0.36, 0.64, [
        {"text": "For: ", "size": 9.5, "bold": True, "color": TEAL},
        {"text": "visible to non-technical participants, fits the process the "
                 "team already has, keeps the repository clean.",
         "size": 9.5, "color": DEEP},
        {"text": "Against: ", "size": 9.5, "bold": True, "color": DEEP,
         "newpara": True, "space_before": 2},
        {"text": "it sits outside the agent's file context — you need a bridge "
                 "over MCP or an API; an extra external dependency and a network "
                 "call instead of a local read.",
         "size": 9.5, "color": DEEP},
    ], line_spacing=1.08)

    rxn = x0 + lwn + 0.10
    rwn = total - lwn - 0.10
    filled_rect(s, rxn, ny, rwn, nh, SOFT_GREY, stroke=SLATE, stroke_pt=0.75,
                radius=True, radius_adj=0.08)
    text_runs(s, rxn + 0.16, ny + 0.10, rwn - 0.32, 0.94, [
        {"text": "Not a task log at all: ", "size": 9.5, "bold": True,
         "color": SLATE},
        {"text": "the built-in TodoWrite/Task* lives inside one session; commit "
                 "history as the only log — workable, but formalized nowhere.",
         "size": 9.5, "italic": True, "color": SLATE},
    ], line_spacing=1.08)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The criterion is compound: who works + how long the task lives + why an "
        "audit trail is needed — not whatever came to hand first.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20e")
    notes_with_sources(s, "s20e")
    return s


# ============================================================
# s20d — git conventions as a team agreement (commit / branch / PR),
# built from "why", not from syntax. Presents AFTER s20e.
# ============================================================
def s20d(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Git conventions are a team agreement, not a requirement of git",
        size=19, w=12.3, h=0.58)

    x0 = 0.55
    total = 12.25

    # ---- what a "convention" even is: the meaning before the syntax ----
    dy = 1.06
    ocean_box(s, x0, dy, total, 0.78, fill=TEAL_TINT, stroke=TEAL,
              stroke_pt=1.4)
    icon(s, "users", x0 + 0.20, dy + 0.18, 0.42, "teal")
    text_box(s, x=x0 + 0.76, y=dy + 0.10, w=total - 0.96, h=0.62,
             text="Git itself is indifferent to what a commit message says and "
                  "how a branch is named — it checks none of it. A convention is "
                  "a voluntary team agreement, written down in AGENTS.md: shape "
                  "the history the same way every time, so that both a human and "
                  "a program can parse it. An agent follows only the agreement it "
                  "can see written down.",
             size=11, color=DEEP, line_spacing=1.14)

    # ---- three conventions: what it IS, and what breaks without it ----
    cy = 1.94
    ch = 3.30
    gap = 0.20
    cw = (total - gap * 2) / 3
    cols = [
        ("git-compare", "Commit", MID, "mid",
         "An agreed-in-advance shape for the first line of a commit: first a "
         "marker for \"what kind of change is this\", then the description.",
         "feat(auth): sign-in with a one-time code\nfix(api): do not drop the "
         "header on retry",
         "That marker is read by a program, not a human: from it, the release "
         "changelog and the new version number assemble themselves (fix → 2.4.1, "
         "feat → 2.5.0). An agent commits an order of magnitude more often than a "
         "human — there is no longer anyone to re-read every commit by eye."),
        ("git-branch", "Branch", TEAL, "teal",
         "Task type, a slash, a short lowercase description. For an agent's "
         "branches — dedicated prefixes.",
         "claude/security-patch\nai/refactor-auth-flow",
         "The branch name is the only thing a reviewer sees before opening the "
         "changes. The prefix says immediately that an agent drove this branch, "
         "and such branches can carry their own rule. Without an agreement the "
         "branch list reads \"test2\" and \"fix-final\"."),
        ("git-pull-request", "Description", MID, "mid",
         "A pull request — the window where changes are shown to a human before "
         "they reach shared code.",
         "Why → What changed → What was not touched →\n"
         "How it was checked → Risks → Deferred",
         "The reviewer spends time on checking, not on reconstructing the intent. "
         "The biggest saving is the \"what was not touched\" line: no hunting for "
         "side effects where there were none. Without a template every request is "
         "shaped differently. The agent fills the template in as it works."),
    ]
    for i, (ic, tag, col, var, what, mono, why) in enumerate(cols):
        x = x0 + i * (cw + gap)
        ocean_box(s, x, cy, cw, ch)
        chip(s, x + 0.20, cy + 0.14, 1.55, 0.34, tag, fill=col, color=WHITE,
             size=11)
        icon(s, ic, x + cw - 0.62, cy + 0.12, 0.40, var)
        text_box(s, x=x + 0.20, y=cy + 0.58, w=cw - 0.40, h=0.20,
                 text="WHAT IT IS", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.20, y=cy + 0.80, w=cw - 0.40, h=0.52,
                 text=what, size=9.5, color=DEEP, line_spacing=1.14)
        filled_rect(s, x + 0.20, cy + 1.36, cw - 0.40, 0.42, WHITE,
                    stroke=SOFT_GREY, stroke_pt=1.0, radius=True,
                    radius_adj=0.10)
        text_box(s, x=x + 0.30, y=cy + 1.42, w=cw - 0.60, h=0.32,
                 text=mono, size=8, color=SLATE, font=FONT_MONO,
                 line_spacing=1.12)
        text_box(s, x=x + 0.20, y=cy + 1.86, w=cw - 0.40, h=0.20,
                 text="WHY IT IS NEEDED", size=9, bold=True, color=LIGHT)
        text_box(s, x=x + 0.20, y=cy + 2.08, w=cw - 0.40, h=1.10,
                 text=why, size=9.5, color=DEEP, line_spacing=1.12)

    text_box(s, x=x0, y=cy + ch + 0.10, w=total, h=0.30,
             text="A rule common to all three: an agent never commits straight "
                  "into the shared branch — every task gets its own. The same "
                  "thing this course asks of people.",
             size=10.5, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
             line_spacing=1.08)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "An agreement written down nowhere does not work: an agent follows only "
        "the rule it can see in AGENTS.md.",
        size=13, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20d")
    notes_with_sources(s, "s20d")
    return s


# ============================================================
# s20g — secrets are a separate contract: the Register .env case +
# the permissions.deny Bash bypass + the 3-layer scanner defense
# ============================================================
def s20g(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Secrets are a separate contract: .gitignore does not mean \"the agent "
           "will not read it either\"",
        size=18.5, w=12.3, h=0.82)

    lx, lw = 0.55, 6.55
    rx, rw = 7.30, 5.50
    top = 1.44

    # --- LEFT: Register incident + permissions.deny limit ---
    ocean_box(s, lx, top, lw, 1.98)
    icon(s, "key", lx + 0.22, top + 0.14, 0.46, "mid")
    text_box(s, x=lx + 0.82, y=top + 0.18, w=lw - 1.06, h=0.36,
             text="The Register, 2026-01-28 [1]", size=12.5, bold=True,
             color=MID)
    text_box(s, x=lx + 0.24, y=top + 0.62, w=lw - 0.48, h=0.80,
             text="Claude Code (v2.1.12) read .env despite both .gitignore and "
                  ".claudeignore — it warns about credentials and prints the "
                  "contents anyway. At least 4 open issues.",
             size=10.5, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.24, top + 1.44, lw - 0.48, 0.48, TEAL_TINT,
                stroke=TEAL, stroke_pt=1.2, radius=True, radius_adj=0.10)
    text_box(s, x=lx + 0.40, y=top + 1.49, w=lw - 0.80, h=0.38,
             text='"Ignored by git" and "ignored by Claude Code" are two '
                  'different things.',
             size=9.5, italic=True, color=DEEP, font=FONT_MONO,
             anchor=MSO_ANCHOR.MIDDLE)

    ocean_box(s, lx, top + 2.14, lw, 1.90, fill=SOFT_GREY, stroke=LIGHT,
              stroke_pt=1.0)
    icon(s, "shield-alert", lx + 0.22, top + 2.28, 0.44, "mid")
    text_box(s, x=lx + 0.80, y=top + 2.30, w=lw - 1.04, h=0.36,
             text="permissions.deny does not block Bash", size=12, bold=True,
             color=DEEP)
    text_box(s, x=lx + 0.24, y=top + 2.72, w=lw - 0.48, h=1.20,
             text="deny(Read(./.env)) blocks the built-in file tool — but "
                  "`cat .env` through Bash walks around the rule. Two independent "
                  "contracts: closing this needs OS-level sandboxing.",
             size=10.5, color=DEEP, line_spacing=1.16)

    # --- RIGHT: 3-layer defense ---
    layers = [
        ("1", "pre-commit hook (Gitleaks)", "local and fast — but bypassable "
         "with --no-verify: an advisory barrier, not a binding one."),
        ("2", "CI gate (Gitleaks + TruffleHog verified)", "on every PR — a "
         "binding gate: CI cannot be dodged by branching around the hook."),
        ("3", "server-side push protection", "at the git-hosting level — holds "
         "even when client hooks are bypassed."),
    ]
    ocean_box(s, rx, top, rw, 4.10, fill=SURFACE, stroke=MID, stroke_pt=1.6)
    icon(s, "lock", rx + 0.22, top + 0.16, 0.46, "teal")
    text_box(s, x=rx + 0.82, y=top + 0.20, w=rw - 1.04, h=0.36,
             text="A three-layer defense", size=13, bold=True, color=MID)
    ly = top + 0.72
    for num, head, body in layers:
        circle(s, rx + 0.24, ly, 0.36, MID)
        text_box(s, x=rx + 0.24, y=ly, w=0.36, h=0.36, text=num, size=13,
                 bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
        text_box(s, x=rx + 0.72, y=ly - 0.02, w=rw - 0.98, h=0.32, text=head,
                 size=11.5, bold=True, color=DEEP, line_spacing=1.0)
        text_box(s, x=rx + 0.72, y=ly + 0.32, w=rw - 0.98, h=0.62, text=body,
                 size=10, color=DEEP, line_spacing=1.14)
        ly += 1.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "What you commit and what the agent is allowed to read are two different, "
        "independently configured contracts; closing one does not close the other.",
        size=12, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20g")
    notes_with_sources(s, "s20g")
    return s


# ============================================================
# s20f — git worktree: "a folder per session" AS A DIAGRAM (#162 r6 / #172).
# The two-panel schema carries the meaning; the row "HISTORY .git" is
# deliberately identical in both panels.
# ============================================================
def _down_arrow(s, cx, y, h=0.22, w=0.17, fill=LIGHT):
    """Vertical flow arrow for the s20f schema (sibling of right_arrow)."""
    shp = s.shapes.add_shape(MSO_SHAPE.DOWN_ARROW,
                             Inches(cx - w / 2), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    try:
        from _helpers_en import disable_shadow
        disable_shadow(shp)
    except Exception:
        pass
    return shp


def s20f(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "Every parallel session gets its own folder; all they share is the history",
        size=20, w=12.3, h=0.58)

    # ---------- geometry of the two-panel schema ----------
    labx, labw = 0.55, 1.00
    pax, pbx, pw = 1.66, 7.38, 5.42
    ptop, phh = 0.98, 2.88
    pad = 0.16
    innw = pw - pad * 2
    cw = (innw - 0.12 * 2) / 3            # session chip / folder cell width

    r1y, r1h = 1.38, 0.54                 # SESSIONS
    r2y, r2h = 2.14, 0.62                 # FILES IN PROGRESS
    r3y, r3h = 2.98, 0.54                 # HISTORY .git

    # ---------- row labels (the grid is read once, not twice) ----------
    for yy, hh, lab in ((r1y, r1h, "SESSIONS"),
                        (r2y, r2h, "FILES\nIN PROGRESS"),
                        (r3y, r3h, "HISTORY\n.git")):
        text_box(s, x=labx, y=yy - 0.06, w=labw, h=hh + 0.12,
                 text=lab, size=9.5, bold=True, color=LIGHT,
                 align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.06)

    sessions = ["Session A", "Session B", "Session C"]

    # =========== PANEL A — without worktree ===========
    ocean_box(s, pax, ptop, pw, phh, fill=WHITE, stroke=SLATE, stroke_pt=1.2)
    icon(s, "triangle-alert", pax + pad, ptop + 0.06, 0.34, "gold")
    text_box(s, x=pax + pad + 0.44, y=ptop + 0.06, w=pw - pad * 2 - 0.44, h=0.30,
             text="Without worktree — one folder for everyone", size=12,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    for i, name in enumerate(sessions):
        x = pax + pad + i * (cw + 0.12)
        chip(s, x, r1y, cw, r1h, name, fill=MID, color=WHITE, size=11)
        _down_arrow(s, x + cw / 2, r1y + r1h + 0.02, 0.20, 0.17, SLATE)

    filled_rect(s, pax + pad, r2y, innw, r2h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.08)
    icon(s, "file-stack", pax + pad + 0.14, r2y + 0.13, 0.34, "mid")
    text_box(s, x=pax + pad + 0.56, y=r2y + 0.06, w=innw - 0.70, h=0.24,
             text="one working copy for all", size=10.5, bold=True,
             color=DEEP)
    text_box(s, x=pax + pad + 0.56, y=r2y + 0.30, w=innw - 0.70, h=0.26,
             text="uncommitted edits sit in the very same files",
             size=9.5, color=SLATE)
    _down_arrow(s, pax + pw / 2, r2y + r2h + 0.06, 0.20, 0.17, SLATE)

    filled_rect(s, pax + pad, r3y, innw, r3h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.09)
    icon(s, "git-branch", pax + pad + 0.14, r3y + 0.09, 0.34, "mid")
    text_box(s, x=pax + pad + 0.56, y=r3y + 0.04, w=innw - 0.70, h=r3h - 0.08,
             text="one repository history", size=10.5, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=pax, y=ptop + phh + 0.06, w=pw, h=0.36,
             text="What breaks: one session silently switches another's working "
                  "tree — claude-code #60295. This course lost hours to it.",
             size=10, color=SLATE, line_spacing=1.12)

    # =========== PANEL B — with worktree ===========
    ocean_box(s, pbx, ptop, pw, phh, fill=SURFACE, stroke=TEAL, stroke_pt=1.6)
    icon(s, "shield-check", pbx + pad, ptop + 0.06, 0.34, "teal")
    text_box(s, x=pbx + pad + 0.44, y=ptop + 0.06, w=pw - pad * 2 - 0.44, h=0.30,
             text="With worktree — a folder of its own per session", size=12,
             bold=True, color=TEAL, anchor=MSO_ANCHOR.MIDDLE)

    folders = ["/wt-a", "/wt-b", "/wt-c"]
    for i, (name, path_) in enumerate(zip(sessions, folders)):
        x = pbx + pad + i * (cw + 0.12)
        chip(s, x, r1y, cw, r1h, name, fill=MID, color=WHITE, size=11)
        _down_arrow(s, x + cw / 2, r1y + r1h + 0.02, 0.20, 0.17, TEAL)
        filled_rect(s, x, r2y, cw, r2h, TEAL_TINT, stroke=TEAL, stroke_pt=1.3,
                    radius=True, radius_adj=0.10)
        text_box(s, x=x + 0.06, y=r2y + 0.06, w=cw - 0.12, h=0.24,
                 text=path_, size=10.5, bold=True, color=TEAL,
                 font=FONT_MONO, align=PP_ALIGN.CENTER)
        text_box(s, x=x + 0.06, y=r2y + 0.30, w=cw - 0.12, h=0.26,
                 text="its own branch", size=9.5, color=SLATE,
                 align=PP_ALIGN.CENTER)
        _down_arrow(s, x + cw / 2, r2y + r2h + 0.06, 0.20, 0.17, TEAL)

    filled_rect(s, pbx + pad, r3y, innw, r3h, SOFT_GREY, stroke=SLATE,
                stroke_pt=1.2, radius=True, radius_adj=0.09)
    icon(s, "git-branch", pbx + pad + 0.14, r3y + 0.09, 0.34, "mid")
    text_box(s, x=pbx + pad + 0.56, y=r3y + 0.04, w=innw - 0.70, h=r3h - 0.08,
             text="the same history — this level did not change", size=10.5,
             bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)

    text_box(s, x=pbx, y=ptop + phh + 0.06, w=pw, h=0.36,
             text="What changes: only the files are separated. Branches and "
                  "commits stay shared — the folder is a view on the same "
                  "history, not a copy.",
             size=10, color=SLATE, line_spacing=1.12)

    # ---------- bottom band: commands · enforcement · the honest caveat ----------
    by, bh = 4.32, 1.20
    c1x, c1w = 0.55, 4.10
    c2x, c2w = 4.80, 3.50
    c3x, c3w = 8.50, 4.30

    ocean_box(s, c1x, by, c1w, bh)
    text_box(s, x=c1x + 0.18, y=by + 0.08, w=c1w - 0.36, h=0.22,
             text="Two commands — and the folder is ready", size=10.5,
             bold=True, color=MID)
    for i, line in enumerate(["git worktree add --detach /wt-a <commit>",
                              "cd /wt-a && git checkout -b task-A"]):
        text_box(s, x=c1x + 0.18, y=by + 0.34 + i * 0.25, w=c1w - 0.36, h=0.23,
                 text=line, size=9, color=SLATE, font=FONT_MONO,
                 line_spacing=1.0)
    text_box(s, x=c1x + 0.18, y=by + 0.86, w=c1w - 0.36, h=0.26,
             text="Cheaper than cloning: the history is not duplicated.",
             size=9.5, italic=True, color=SLATE)

    ocean_box(s, c2x, by, c2w, bh, fill=TEAL_TINT, stroke=TEAL, stroke_pt=1.4)
    icon(s, "lock", c2x + 0.16, by + 0.10, 0.32, "teal")
    text_box(s, x=c2x + 0.54, y=by + 0.10, w=c2w - 0.70, h=0.22,
             text="Not on trust alone", size=10.5, bold=True, color=TEAL)
    text_box(s, x=c2x + 0.16, y=by + 0.38, w=c2w - 0.32, h=0.64,
             text="Claude Code blocks edits whose working directory is outside "
                  "the assigned folder: a neighboring session cannot be touched "
                  "even by mistake.",
             size=9.5, color=DEEP, line_spacing=1.12)

    filled_rect(s, c3x, by, c3w, bh, SOFT_GREY, stroke=SLATE, stroke_pt=0.9,
                radius=True, radius_adj=0.07)
    text_box(s, x=c3x + 0.16, y=by + 0.10, w=c3w - 0.32, h=0.22,
             text="The boundary: a shared .git is a shared lock", size=10.5,
             bold=True, color=SLATE)
    text_box(s, x=c3x + 0.16, y=by + 0.36, w=c3w - 0.32, h=0.72,
             text="The files are separated, but .git is one for everyone: 8 of 13 "
                  "parallel agents lost unsaved work on the .git/index.lock. At 5 "
                  "sessions — occasionally; at 10+ — almost certainly.",
             size=9.5, italic=True, color=SLATE, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The worktree mechanic is older than any AI agent; what is new is only the "
        "frequency: parallel sessions make a shared folder an expensive mistake "
        "every day.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s20f", size=8.0)
    notes_with_sources(s, "s20f")
    return s


# ============================================================
# s20 — 70% problem (curve + 3 numbers) [in-bucket]
# ============================================================
def s20(p):
    s = blank(p)
    set_slide_bg(s, WHITE)
    slide_title(
        s, "The 70% problem: AI speeds up the first 70%, but not the last 30% — understanding",
        size=22, w=12.2, h=0.82)

    # left: 70% curve concept
    lx, lw = 0.55, 6.05
    ocean_box(s, lx, 1.52, lw, 4.02)
    # a simple two-part bar showing 70% fast / 30% hard
    by = 1.98
    filled_rect(s, lx + 0.30, by, (lw - 0.60) * 0.70, 0.70, TEAL,
                radius=True, radius_adj=0.10)
    filled_rect(s, lx + 0.30 + (lw - 0.60) * 0.70, by, (lw - 0.60) * 0.30, 0.70,
                GOLD, radius=True, radius_adj=0.10)
    text_box(s, x=lx + 0.30, y=by + 0.16, w=(lw - 0.60) * 0.70, h=0.4,
             text="first ~70% — fast, cheap", size=11, bold=True,
             color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30 + (lw - 0.60) * 0.70, y=by + 0.10,
             w=(lw - 0.60) * 0.30, h=0.5,
             text="last 20-30%", size=10, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text_box(s, x=lx + 0.30, y=by + 0.80, w=lw - 0.60, h=0.90,
             text="The last 20-30% — edge cases, error handling, "
                  "security, integration, behavior under load — stay "
                  "just as hard and require senior oversight. The gap is "
                  "structural: the system's specifics are absent from the training data.",
             size=10.5, color=DEEP, line_spacing=1.14)
    filled_rect(s, lx + 0.30, 3.86, lw - 0.60, 1.44, GOLD_TINT, stroke=GOLD,
                stroke_pt=1.6, radius=True, radius_adj=0.05)
    text_box(s, x=lx + 0.52, y=3.96, w=lw - 1.04, h=1.28,
             text="'Almost right' code is costlier than obviously wrong code: it passes "
                  "a quick glance and breaks on an edge case. Work shifts from "
                  "writing to debugging someone else's plausible logic.",
             size=11, bold=True, color=DEEP, line_spacing=1.16,
             anchor=MSO_ANCHOR.MIDDLE)

    # right: three numbers with baseline
    rx, rw = 6.85, 5.95
    nums = [
        ("Stack Overflow 2025: 66%",
         "of developers named their top frustration 'solutions that are almost "
         "right, but not quite'.", 0.82),
        ("GitClear · two independent measurements [2]",
         "211M lines (2020-24): clones 8.3→12.3%, refactoring ~25→<10%, "
         "churn 3.3→5.7%.\n"
         "623M changes (2023-26): refactoring 21→3.8% (-70%), duplicates "
         "40.3→73.0 per M lines (+81%), churn +15%.\n"
         "(Both are correlation, not an RCT.)",
         1.30),
        ("The knowledge paradox (Osmani) [1]",
         "seniors challenge the AI's output, juniors accept it ('a house of "
         "cards') — AI amplifies the experienced more.", 0.72),
    ]
    ny = 1.48
    for i, (head, body, bh) in enumerate(nums):
        y = ny
        ocean_box(s, rx, y, rw, 0.32 + bh)
        text_box(s, x=rx + 0.24, y=y + 0.08, w=rw - 0.48, h=0.30, text=head,
                 size=12, bold=True, color=MID)
        text_box(s, x=rx + 0.24, y=y + 0.40, w=rw - 0.48, h=bh - 0.06,
                 text=body, size=10, color=DEEP, line_spacing=1.10)
        ny += 0.32 + bh + 0.10

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The alternative — small verifiable units + a harness + reading the diff "
        "before accept; duplication and churn metrics in CI as a gate. Merge is always the human.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    # Round-5 meme (EN caption twin): Hide the Pain Harold — both panels, same
    # face, same smile; the point is that NOTHING visibly changes, exactly like
    # "almost right" code.
    add_image(s, WEB / "band-hide-the-pain-harold-merged-en.png", 8.56, 6.40,
              4.24, 0.64)
    refs_of_slide(s, "s21")
    notes_with_sources(s, "s21")
    return s
