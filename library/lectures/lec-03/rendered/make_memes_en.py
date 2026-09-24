#!/usr/bin/env python3
"""EN meme pass (issue #185/#172, EN track) — English composites for the 15
real imgflip meme templates used across the Lecture 3 EN deck. Same templates,
same placement as make_memes.py + make_memes_v6.py (RU), but English captions.
Output PNGs (*-en.png) embedded via python-pptx in build_lec03_en.py.

No superlatives as empty intensifiers. No baked-in source attribution
(attribution.md only). Captions in classic meme style (bold DejaVu, high
contrast).

15 memes: s01-drake, s05-gru, s05a-changemymind, s05c-pigeon, s06-distracted,
s11-pooh, s12-rollsafe, s14-yoda, s15-doge, s19b-batman, s22c-pooh,
s22e-thisisfine, s24-alwayshasbeen, s27b-bus, s31-skeleton.

Plus 9 more (issue #196 EN parity, 55->67 slide track): s-fmt-twobuttons,
s-task-assistant-simply, s-task-tone-fry, s-task-extract-trade,
s-rag-elastic-cat, s-rag-chunk2-disaster, s-ft-eval-leftexit,
s-agent-when-clown, s-task-research-panik — EN captions for the same 9
templates used in make_memes_v6.py (RU), matching those exact box
geometries.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).parent / "assets/web"
SRC = WEB / "memes-src"
FONT = "/home/harness/.local/lo-sysroot/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/home/harness/.local/lo-sysroot/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

WHITE = (255, 255, 255)
BLACK = (18, 18, 18)


def font(sz, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_R, sz)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, text, box, fnt, fill=BLACK, align="left", valign="center",
               line_h=1.14):
    x, y, w, h = box
    lines = wrap(draw, text, fnt, w)
    asc, desc = fnt.getmetrics()
    lh = int((asc + desc) * line_h)
    total = lh * len(lines)
    if valign == "center":
        cy = y + (h - total) // 2
    elif valign == "bottom":
        cy = y + h - total
    else:
        cy = y
    for ln in lines:
        tw = draw.textlength(ln, font=fnt)
        if align == "center":
            cx = x + (w - tw) // 2
        elif align == "right":
            cx = x + w - tw
        else:
            cx = x
        draw.text((cx, cy), ln, font=fnt, fill=fill)
        cy += lh


def outline_block(draw, text, box, fnt, fill=WHITE, outline=BLACK, ow=3,
                  align="center", valign="top", line_h=1.12):
    x, y, w, h = box
    lines = wrap(draw, text, fnt, w)
    asc, desc = fnt.getmetrics()
    lh = int((asc + desc) * line_h)
    total = lh * len(lines)
    if valign == "center":
        cy = y + (h - total) // 2
    elif valign == "bottom":
        cy = y + h - total
    else:
        cy = y
    for ln in lines:
        tw = draw.textlength(ln, font=fnt)
        cx = x + (w - tw) // 2 if align == "center" else x
        for dx in range(-ow, ow + 1):
            for dy in range(-ow, ow + 1):
                if dx or dy:
                    draw.text((cx + dx, cy + dy), ln, font=fnt, fill=outline)
        draw.text((cx, cy), ln, font=fnt, fill=fill)
        cy += lh


def outline_text(draw, pos, text, fnt, fill=WHITE, outline=BLACK, ow=3):
    x, y = pos
    for dx in range(-ow, ow + 1):
        for dy in range(-ow, ow + 1):
            if dx or dy:
                draw.text((x + dx, y + dy), text, font=fnt, fill=outline)
    draw.text((x, y), text, font=fnt, fill=fill)


def fit_font(draw, text, max_w, start, bold=True, min_sz=16):
    sz = start
    while sz > min_sz:
        f = font(sz, bold)
        if all(draw.textlength(w, font=f) <= max_w for w in text.split()):
            return f
        sz -= 2
    return font(min_sz, bold)


# ------------------------------------------------------------------
# s01 — DRAKE reject/approve — complicate the prompt for accuracy vs
#        pick the architecture for the task.
# ------------------------------------------------------------------
def make_drake():
    img = Image.open(WEB / "drake-blank.jpg").convert("RGB")
    W, H = img.size            # 1200x1200, two 600px panels, right half white
    d = ImageDraw.Draw(img)
    cap_x = 620
    cap_w = W - cap_x - 30
    f = font(46)
    # top (reject)
    draw_block(d, "Complicate the prompt for accuracy: “you are an expert lawyer, reason step by step”",
               (cap_x, 20, cap_w, 560), f, fill=BLACK, align="left", valign="center")
    # bottom (approve)
    draw_block(d, "Pick the architecture for the task: context, RAG or a tool",
               (cap_x, 620, cap_w, 560), f, fill=BLACK, align="left", valign="center")
    out = WEB / "s01-drake-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s05 — GRU'S PLAN (4 panels) — escalating architecture “just in case”
#        with an absurd punchline in the 4th panel.
# ------------------------------------------------------------------
def make_gru():
    img = Image.open(SRC / "gru-plan.jpg").convert("RGB")
    W, H = img.size            # 700x449
    d = ImageDraw.Draw(img)
    pw, ph = W // 2, H // 2    # 350 x 224 per panel
    caps = [
        "Took one call\nwith a good prompt",
        "Added RAG\nand loops —\njust in case",
        "Wrapped it in\nmulti-agent\norchestration",
        "The task was\na three-line\nplain script",   # punchline (panel 4)
    ]
    bx0, bx1 = int(pw * 0.53), int(pw * 0.99)
    by0, by1 = int(ph * 0.10), int(ph * 0.92)
    for i, cap in enumerate(caps):
        r, c = divmod(i, 2)
        ox, oy = c * pw, r * ph
        box = (ox + bx0, oy + by0, bx1 - bx0, by1 - by0)
        d.rectangle([ox + bx0 - 2, oy + by0 - 2, ox + bx1 + 2, oy + by1 + 2],
                    fill=(214, 232, 234))
        f = fit_font(d, cap.replace("\n", " "), box[2] - 6, 19, True, 11)
        draw_block(d, cap.replace("\n", " "), (box[0] + 4, box[1], box[2] - 8, box[3]),
                   f, fill=BLACK, align="center", valign="center", line_h=1.12)
    out = WEB / "s05-gru-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s05a — CHANGE MY MIND — a role in the prompt does not make the answer
#        more accurate.
# ------------------------------------------------------------------
def make_change_my_mind():
    img = Image.open(SRC / "change-my-mind.jpg").convert("RGB")
    W, H = img.size            # 482x361
    d = ImageDraw.Draw(img)
    sx0, sy0, sx1, sy1 = 100, 300, 425, 349
    d.rectangle([sx0, sy0, sx1, sy1], fill=WHITE)
    txt = "“An expert role adds no accuracy”"
    f = fit_font(d, txt, sx1 - sx0 - 8, 20, True, 11)
    draw_block(d, txt, (sx0 + 4, sy0, sx1 - sx0 - 8, sy1 - sy0), f,
               fill=BLACK, align="center", valign="center", line_h=1.05)
    out = WEB / "s05a-changemymind-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s05c — IS THIS A PIGEON — a protocol role is mistaken for a hard boundary.
# ------------------------------------------------------------------
def make_pigeon():
    img = Image.open(SRC / "is-this-a-pigeon.jpg").convert("RGB")
    W, H = img.size            # 1587x1425
    d = ImageDraw.Draw(img)
    outline_block(d, "the system protocol role",
                  (int(W * 0.58), int(H * 0.02), int(W * 0.40), int(H * 0.12)),
                  font(56), align="center", valign="top", ow=4)
    outline_block(d, "“is a reliable boundary, right?”",
                  (int(W * 0.05), int(H * 0.86), int(W * 0.90), int(H * 0.12)),
                  font(66), align="center", valign="center", ow=5)
    out = WEB / "s05c-pigeon-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s06 — DISTRACTED BOYFRIEND — the model gets distracted from the real cause.
# ------------------------------------------------------------------
def make_distracted():
    img = Image.open(WEB / "distracted-blank.jpg").convert("RGB")
    W, H = img.size            # 1200x800
    d = ImageDraw.Draw(img)
    f = font(40)
    # other woman (red dress, left) = a nice out-loud explanation
    outline_text(d, (40, 470), "a nice out-loud", f)
    outline_text(d, (40, 515), "explanation", f)
    # boyfriend (center top) = the model
    outline_text(d, (600, 120), "the model", f)
    # girlfriend (right, betrayed) = the real cause of the answer
    outline_text(d, (930, 300), "the real", f)
    outline_text(d, (930, 345), "cause of", f)
    outline_text(d, (930, 390), "the answer", f)
    out = WEB / "s06-distracted-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s11 — TUXEDO POOH — raw RAG vs RAG grounded in a verifiable source.
# ------------------------------------------------------------------
def make_pooh():
    img = Image.open(SRC / "tuxedo-pooh.png").convert("RGB")
    W, H = img.size            # 800x582
    d = ImageDraw.Draw(img)
    cx0 = int(W * 0.44)
    cw = W - cx0 - 24
    draw_block(d, "“just ask the model — it knows everything”",
               (cx0, int(H * 0.03), cw, int(H * 0.44)), font(32),
               fill=BLACK, align="left", valign="center", line_h=1.16)
    draw_block(d, "RAG: an answer grounded in a verifiable source",
               (cx0, int(H * 0.52), cw, int(H * 0.44)), font(32),
               fill=BLACK, align="left", valign="center", line_h=1.16)
    out = WEB / "s11-pooh-en.png"
    img.save(out)
    return out


def make_pooh_memory():
    """s22c variant of Tuxedo Pooh: a flat file log vs a graph knowledge base."""
    img = Image.open(SRC / "tuxedo-pooh.png").convert("RGB")
    W, H = img.size
    d = ImageDraw.Draw(img)
    cx0 = int(W * 0.44)
    cw = W - cx0 - 24
    draw_block(d, "“just append facts to one text log”",
               (cx0, int(H * 0.03), cw, int(H * 0.44)), font(30),
               fill=BLACK, align="left", valign="center", line_h=1.14)
    draw_block(d, "a graph knowledge base — only when scale demands it",
               (cx0, int(H * 0.52), cw, int(H * 0.44)), font(30),
               fill=BLACK, align="left", valign="center", line_h=1.14)
    out = WEB / "s22c-pooh-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s12 — ROLL SAFE — you don't need RAG if the corpus fits in the context.
# ------------------------------------------------------------------
def make_roll_safe():
    img = Image.open(SRC / "roll-safe.jpg").convert("RGB")
    W, H = img.size            # 702x395
    d = ImageDraw.Draw(img)
    outline_block(d, "no RAG needed",
                  (12, 8, W - 24, int(H * 0.22)), font(46),
                  align="center", valign="top", ow=3)
    outline_block(d, "if the corpus fits in the context",
                  (12, int(H * 0.74), W - 24, int(H * 0.24)), font(38),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s12-rollsafe-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s15 — BUFF DOGE vs CHEEMS — PEFT (a strong choice) vs full fine-tuning.
# ------------------------------------------------------------------
def make_doge():
    img = Image.open(SRC / "buff-doge-cheems.png").convert("RGB")
    W, H = img.size            # 937x720
    d = ImageDraw.Draw(img)
    draw_block(d, "PEFT / LoRA:\ncheap, modular, lower forgetting risk",
               (20, int(H * 0.80), int(W * 0.48), int(H * 0.19)), font(28),
               fill=BLACK, align="center", valign="top", line_h=1.1)
    draw_block(d, "Full fine-tuning of\nall weights in 2026 —\nalmost never",
               (int(W * 0.55), int(H * 0.80), int(W * 0.43), int(H * 0.19)),
               font(28), fill=BLACK, align="center", valign="top", line_h=1.1)
    out = WEB / "s15-doge-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s19b — BATMAN SLAP — “an agent is just a pricier chat” → slap.
# ------------------------------------------------------------------
def make_batman():
    img = Image.open(SRC / "batman-slap.jpg").convert("RGB")
    W, H = img.size            # 400x387
    d = ImageDraw.Draw(img)
    f = fit_font(d, "an agent is just a pricier chat", 165, 19, True, 12)
    draw_block(d, "“an agent is just a pricier chat”",
               (18, 18, 165, 105), f, fill=BLACK, align="center",
               valign="center", line_h=1.06)
    f2 = fit_font(d, "it is a different cost class", 150, 19, True, 12)
    draw_block(d, "it is a different cost class",
               (238, 34, 150, 90), f2, fill=BLACK, align="center",
               valign="center", line_h=1.06)
    out = WEB / "s19b-batman-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s22e — THIS IS FINE — “an instruction file fixes everything” / room on fire.
# ------------------------------------------------------------------
def make_this_is_fine():
    img = Image.open(SRC / "this-is-fine.jpg").convert("RGB")
    W, H = img.size            # 580x282
    d = ImageDraw.Draw(img)
    bx0, by0, bx1, by1 = 360, 12, 566, 74
    d.rectangle([bx0, by0, bx1, by1], fill=WHITE)
    txt = "“the instruction file fixes it”"
    f = fit_font(d, txt, bx1 - bx0 - 6, 18, True, 10)
    draw_block(d, txt, (bx0 + 3, by0, bx1 - bx0 - 6, by1 - by0), f,
               fill=BLACK, align="center", valign="center", line_h=1.02)
    out = WEB / "s22e-thisisfine-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s24 — ALWAYS HAS BEEN — “data outside ZDR?” / “always has been”.
# ------------------------------------------------------------------
def make_always_has_been():
    img = Image.open(SRC / "always-has-been.png").convert("RGB")
    W, H = img.size            # 960x540
    d = ImageDraw.Draw(img)
    outline_block(d, "data outside ZDR?!",
                  (int(W * 0.32), int(H * 0.30), int(W * 0.34), int(H * 0.16)),
                  font(36), align="center", valign="top", ow=3)
    outline_block(d, "always has been",
                  (int(W * 0.58), int(H * 0.03), int(W * 0.40), int(H * 0.16)),
                  font(36), align="center", valign="top", ow=3)
    out = WEB / "s24-alwayshasbeen-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s14 — STAR WARS YODA — teacher→student: a large fine-tuned model passes
#       a skill to a small one (distillation).
# ------------------------------------------------------------------
def make_yoda():
    img = Image.open(SRC / "yoda.jpg").convert("RGB")
    W, H = img.size            # 620x713
    d = ImageDraw.Draw(img)
    outline_block(d, "teacher — a large fine-tuned model",
                  (10, 6, W - 20, int(H * 0.16)), font(32),
                  align="center", valign="top", ow=3)
    outline_block(d, "passes the skill to a small student",
                  (10, int(H * 0.83), W - 20, int(H * 0.16)), font(32),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s14-yoda-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s27b — TWO GUYS ON A BUS — sad (over-complicated agent) vs happy
#        (a thin default agent).
# ------------------------------------------------------------------
def make_two_guys_bus():
    img = Image.open(SRC / "two-guys-bus.jpg").convert("RGB")
    W, H = img.size            # 762x675
    d = ImageDraw.Draw(img)
    outline_block(d, "complicated it just in case",
                  (6, int(H * 0.60), int(W * 0.36), int(H * 0.30)),
                  font(24), align="center", valign="center", ow=3, line_h=1.06)
    outline_block(d, "started with a thin agent",
                  (int(W * 0.60), int(H * 0.04), int(W * 0.38), int(H * 0.26)),
                  font(24), align="center", valign="center", ow=3, line_h=1.06)
    out = WEB / "s27b-bus-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s31 — WAITING SKELETON — “waiting for your questions”. Light finale.
# ------------------------------------------------------------------
def make_skeleton():
    img = Image.open(SRC / "waiting-skeleton.jpg").convert("RGB")
    W, H = img.size            # 298x403
    d = ImageDraw.Draw(img)
    outline_block(d, "waiting for your questions",
                  (6, 4, W - 12, int(H * 0.20)), font(26),
                  align="center", valign="top", ow=3, line_h=1.04)
    out = WEB / "s31-skeleton-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-fmt-twobuttons — TWO BUTTONS — the output-format dilemma: force the
#        answer into JSON vs let the model reason freely (reasoning tax).
# ------------------------------------------------------------------
def make_two_buttons():
    img = Image.open(SRC / "two-buttons.jpg").convert("RGB")
    W, H = img.size            # 600x908
    d = ImageDraw.Draw(img)
    d.rectangle([70, 70, 300, 300], fill=WHITE)
    draw_block(d, "force the answer into JSON",
               (78, 90, 214, 190), font(27), fill=BLACK,
               align="center", valign="center", line_h=1.06)
    d.rectangle([315, 55, 545, 300], fill=WHITE)
    draw_block(d, "let it reason freely",
               (322, 80, 216, 190), font(30), fill=BLACK,
               align="center", valign="center", line_h=1.06)
    out = WEB / "s-fmt-twobuttons-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-assistant-simply — ONE DOES NOT SIMPLY — you can't skip the
#        one-shot / tool-use rungs and jump straight to a full agent.
# ------------------------------------------------------------------
def make_one_does_not():
    img = Image.open(SRC / "one-does-not-simply.jpg").convert("RGB")
    W, H = img.size            # 568x335
    d = ImageDraw.Draw(img)
    outline_block(d, "one does not simply",
                  (10, 6, W - 20, int(H * 0.20)), font(34),
                  align="center", valign="top", ow=3)
    outline_block(d, "jump straight to an agent",
                  (10, int(H * 0.78), W - 20, int(H * 0.20)), font(34),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s-task-assistant-simply-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-tone-fry — FUTURAMA FRY / NOT SURE IF — AI detectors are not
#        reliable evidence of authorship.
# ------------------------------------------------------------------
def make_futurama_fry():
    img = Image.open(SRC / "futurama-fry.jpg").convert("RGB")
    W, H = img.size            # 552x414
    d = ImageDraw.Draw(img)
    outline_block(d, "not sure if a human wrote this",
                  (10, 6, W - 20, int(H * 0.22)), font(32),
                  align="center", valign="top", ow=3)
    outline_block(d, "or the detector is lying again",
                  (10, int(H * 0.76), W - 20, int(H * 0.22)), font(32),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s-task-tone-fry-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-extract-trade — TRADE OFFER — the honest exchange of constrained
#        decoding: you give a JSON schema, you get ~100% compliance.
# ------------------------------------------------------------------
def make_trade_offer():
    img = Image.open(SRC / "trade-offer.jpg").convert("RGB")
    W, H = img.size            # 607x794
    d = ImageDraw.Draw(img)
    # cover the red "TRADE OFFER" banner — keep the red panel, EN text
    d.rectangle([118, 34, 490, 96], fill=(230, 57, 53))
    outline_block(d, "FAIR TRADE",
                  (120, 40, 368, 54), font(34), fill=WHITE, outline=BLACK,
                  ow=2, align="center", valign="center")
    # cover the "i receive:" / "you receive:" banner labels (dark panels)
    d.rectangle([44, 138, 250, 350], fill=(28, 24, 48))
    d.rectangle([340, 138, 560, 350], fill=(28, 24, 48))
    draw_block(d, "you give:",
               (52, 144, 190, 34), font(24), fill=WHITE,
               align="left", valign="top")
    draw_block(d, "a JSON\nschema",
               (52, 186, 190, 150), font(26), fill=WHITE,
               align="left", valign="top", line_h=1.12)
    draw_block(d, "you get:",
               (348, 144, 205, 34), font(24), fill=WHITE,
               align="left", valign="top")
    draw_block(d, "~100%\ncompliance",
               (348, 186, 205, 150), font(26), fill=WHITE,
               align="left", valign="top", line_h=1.12)
    out = WEB / "s-task-extract-trade-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-rag-elastic-cat — WOMAN YELLING AT A CAT — judgment call: do you
#        really need a dedicated vector database.
# ------------------------------------------------------------------
def make_woman_cat():
    img = Image.open(SRC / "woman-yelling-cat.jpg").convert("RGB")
    W, H = img.size            # 680x438
    d = ImageDraw.Draw(img)
    half = W // 2
    outline_block(d, "“we need a vector DB, now!”",
                  (6, 4, half - 12, int(H * 0.30)), font(26),
                  align="center", valign="top", ow=3, line_h=1.05)
    outline_block(d, "you have 3M chunks — Postgres is fine",
                  (half + 6, 4, half - 12, int(H * 0.30)), font(22),
                  align="center", valign="top", ow=3, line_h=1.05)
    out = WEB / "s-rag-elastic-cat-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-rag-chunk2-disaster — DISASTER GIRL — the quiet failure: hyped-up
#        semantic chunking, tables silently fall apart.
# ------------------------------------------------------------------
def make_disaster_girl():
    img = Image.open(SRC / "disaster-girl.jpg").convert("RGB")
    W, H = img.size            # 500x375
    d = ImageDraw.Draw(img)
    outline_block(d, "shipped semantic chunking on hype",
                  (10, 6, W - 20, int(H * 0.24)), font(26),
                  align="center", valign="top", ow=3, line_h=1.04)
    outline_block(d, "tables silently fell apart",
                  (10, int(H * 0.74), W - 20, int(H * 0.24)), font(30),
                  align="center", valign="bottom", ow=3, line_h=1.04)
    out = WEB / "s-rag-chunk2-disaster-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-ft-eval-leftexit — LEFT EXIT 12 OFF RAMP — swerving off rigorous
#        eval onto a pretty benchmark number.
# ------------------------------------------------------------------
def make_left_exit():
    img = Image.open(SRC / "left-exit-12.jpg").convert("RGB")
    W, H = img.size            # 804x767
    d = ImageDraw.Draw(img)
    outline_block(d, "rigorous eval: held-out + A/B",
                  (150, 96, 210, 70), font(19),
                  align="center", valign="center", ow=3, line_h=1.02)
    outline_block(d, "a pretty benchmark number",
                  (392, 96, 200, 70), font(21),
                  align="center", valign="center", ow=3, line_h=1.02)
    out = WEB / "s-ft-eval-leftexit-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-agent-when-clown — CLOWN APPLYING MAKEUP — 4-panel escalation from
#        a slightly unpredictable task to multi-agent, punchline: p^n
#        reliability math.
# ------------------------------------------------------------------
def make_clown_agents():
    img = Image.open(SRC / "clown-makeup.jpg").convert("RGB")
    W, H = img.size            # 750x798
    d = ImageDraw.Draw(img)
    caps = [
        "the task is a bit unpredictable",
        "I'll grab an agent",
        "I'll grab multi-agent",
        "0.95²⁰ ≈ 36% reliability",
    ]
    ys = [10, 210, 410, 610]
    hs = [180, 180, 180, 150]
    for cap, y, h in zip(caps, ys, hs):
        draw_block(d, cap, (24, y, 380, h), font(28),
                   fill=BLACK, align="left", valign="center", line_h=1.06)
    out = WEB / "s-agent-when-clown-en.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-rag-research-panik — PANIK/KALM/PANIK (imgflip 226297822) — the citation
#        checking cycle: agent hands back a report with links → some links
#        even resolve → 3-13% of the URLs are just fabricated. Left white
#        column (3 panels), "Panik/Kalm/Panik" baked in on the right.
#        Panels: y=[10..295],[305..585],[600..870]; x=[15..300].
# ------------------------------------------------------------------
def make_panik_kalm():
    img = Image.open(SRC / "panik-kalm-panik.png").convert("RGB")
    W, H = img.size            # 640x881
    d = ImageDraw.Draw(img)
    lx, lw = 18, 288
    panels = [
        ("agent hands back\na report with\ncitations", 14, 288),
        ("some links\neven resolve", 306, 578),
        ("3-13% of URLs\nare just\nfabricated", 596, 866),
    ]
    for txt, y0, y1 in panels:
        f = fit_font(d, txt.replace("\n", " "), lw - 10, 30, True, 15)
        draw_block(d, txt.replace("\n", " "), (lx, y0, lw, y1 - y0), f,
                   fill=BLACK, align="center", valign="center", line_h=1.1)
    out = WEB / "s-task-research-panik-en.png"
    img.save(out)
    return out


ALL = [
    make_drake, make_gru, make_change_my_mind, make_pigeon, make_distracted,
    make_pooh, make_pooh_memory, make_roll_safe, make_doge, make_batman,
    make_this_is_fine, make_always_has_been, make_yoda, make_two_guys_bus,
    make_skeleton,
    make_two_buttons, make_one_does_not, make_futurama_fry, make_trade_offer,
    make_woman_cat, make_disaster_girl, make_left_exit, make_clown_agents,
    make_panik_kalm,
]

if __name__ == "__main__":
    for fn in ALL:
        p = fn()
        print("wrote", p.name, Image.open(p).size)
