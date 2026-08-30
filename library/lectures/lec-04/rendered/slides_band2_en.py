"""Лекция 4 v4 — Band 2 (s11–s20): требования-провал, архитектура, реализация."""
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
    cyr = 1.72
    per = 3
    cwid = (lw - 0.56 - 0.2 * (per - 1)) / per
    for i, ch in enumerate(checks):
        col = i % per
        row = i // per
        x = lx + 0.28 + col * (cwid + 0.2)
        y = cyr + row * 0.56
        chip(s, x, y, cwid, 0.44, ch, fill=MID, color=WHITE, size=9.5)
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
         "of developers named their top frustration 'solutions that are almost right, "
         "but not quite'."),
        ("GitClear · 211M lines, 2020-2024 [2]",
         "clones 8.3% → 12.3%; refactored ~25% → <10%; churn 3.3% → 5.7%. "
         "(Correlation, not an RCT.)"),
        ("The knowledge paradox (Osmani) [1]",
         "seniors challenge the AI's output, juniors accept it ('a house of cards') — AI "
         "amplifies the experienced more."),
    ]
    ny = 1.52
    for i, (head, body) in enumerate(nums):
        y = ny + i * 1.14
        ocean_box(s, rx, y, rw, 1.02)
        text_box(s, x=rx + 0.24, y=y + 0.10, w=rw - 0.48, h=0.32, text=head,
                 size=12.5, bold=True, color=MID)
        text_box(s, x=rx + 0.24, y=y + 0.42, w=rw - 0.48, h=0.56, text=body,
                 size=11, color=DEEP, line_spacing=1.12)

    gold_callout(
        s, 0.55, 5.72, 12.25, 0.62,
        "The alternative — small verifiable units + a harness + reading the diff "
        "before accept; duplication and churn metrics in CI as a gate. Merge is always the human.",
        size=12.5, bold=True, align=PP_ALIGN.CENTER)
    refs_of_slide(s, "s21")
    notes_with_sources(s, "s21")
    return s
