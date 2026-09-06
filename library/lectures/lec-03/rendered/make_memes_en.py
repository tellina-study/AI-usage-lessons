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


ALL = [
    make_drake, make_gru, make_change_my_mind, make_pigeon, make_distracted,
    make_pooh, make_pooh_memory, make_roll_safe, make_doge, make_batman,
    make_this_is_fine, make_always_has_been, make_yoda, make_two_guys_bus,
    make_skeleton,
]

if __name__ == "__main__":
    for fn in ALL:
        p = fn()
        print("wrote", p.name, Image.open(p).size)
