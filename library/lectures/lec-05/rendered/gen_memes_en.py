"""Lecture 5 (EN) — meme overlay generation (Directive 2) via PIL.

EN twin of gen_memes.py: SAME evergreen meme templates (imgflip template
gallery, assets/meme_templates/*.jpg — already chosen, not re-picked here),
same layouts/panel geometry, English captions instead of Russian. Same
no-lec-2-collision set (Spider-Man / One-Does-Not-Simply / Distracted
Boyfriend / Drake / Anakin-Padme / Woman-Yelling-at-Cat / Disaster Girl /
Sad Pablo / Bernie / Trade Offer / Is-This-A-Pigeon / Clown / Balloon /
They're-The-Same-Picture / Gru's Plan). Attribution captions are NOT drawn on
the image (deck rule: no photo-attribution on slide).

Each meme resolves to the same slide claim as its RU counterpart, translated,
not re-interpreted. Full log (slide -> template -> EN caption -> claim) is in
iteration-log.md.

Output: assets/memes-en/<slide>-<concept>.jpg
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REND = Path(__file__).resolve().parent
TPL = REND / "assets/meme_templates"
OUT = REND / "assets/memes-en"
OUT.mkdir(parents=True, exist_ok=True)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

WHITE = (255, 255, 255)
BLACK = (18, 18, 18)


def font(size):
    return ImageFont.truetype(FONT_BOLD, size)


def _wrap(draw, text, f, max_width, stroke_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), trial, font=f, stroke_width=stroke_width)
        if bbox[2] - bbox[0] > max_width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def meme_text(draw, xy, text, size, *, fill=WHITE, stroke_fill=BLACK,
              stroke_width=4, align="center", anchor="mm", max_width=None,
              line_spacing=1.12):
    f = font(size)
    if max_width is not None:
        text = _wrap(draw, text, f, max_width, stroke_width)
    draw.multiline_text(xy, text, font=f, fill=fill, stroke_fill=stroke_fill,
                        stroke_width=stroke_width, align=align, anchor=anchor,
                        spacing=(size * (line_spacing - 1)))


def top_band(name_in, name_out, caption, *, band_frac=0.26, size=34,
             min_size=22):
    """Add a white caption band on top of the template (never covers subject),
    black text. For templates without safe dark text-space."""
    im = Image.open(TPL / name_in).convert("RGB")
    w, h = im.size
    band_h = int(h * band_frac)
    canvas = Image.new("RGB", (w, h + band_h), WHITE)
    canvas.paste(im, (0, band_h))
    draw = ImageDraw.Draw(canvas)
    # shrink font until it fits the band in <=2 lines
    sz = size
    while sz >= min_size:
        f = font(sz)
        wrapped = _wrap(draw, caption, f, w - 40, 0)
        bbox = draw.multiline_textbbox((0, 0), wrapped, font=f, spacing=sz * 0.12)
        if bbox[3] - bbox[1] <= band_h - 16 and (bbox[2] - bbox[0]) <= w - 30:
            break
        sz -= 2
    meme_text(draw, (w / 2, band_h / 2), caption, sz, fill=BLACK,
              stroke_fill=None, stroke_width=0, anchor="mm", max_width=w - 40)
    canvas.save(OUT / name_out, quality=92)
    print(f"OK {name_out} {canvas.size}")


def overlay(name_in, name_out, captions):
    """captions: list of (rel_x, rel_y, text, size, kw). rel in [0,1].
    White text + black stroke (classic), on dark-safe areas."""
    im = Image.open(TPL / name_in).convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    for rx, ry, text, size, kw in captions:
        meme_text(draw, (w * rx, h * ry), text, size, **kw)
    im.save(OUT / name_out, quality=92)
    print(f"OK {name_out} {im.size}")


# ============================================================
# s01 — Spider-Man Pointing at Spider-Man. Resolves: "building is nearly
#   free" and "~95% of pilots capture zero value" — both true at once,
#   neither cancels the other.
# ============================================================
def s01_spiderman_pointing():
    im = Image.open(TPL / "spiderman-pointing.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    meme_text(draw, (w * 0.235, h * 0.86),
              "building is\nnearly free", 24, fill=WHITE, stroke_fill=BLACK,
              stroke_width=4, anchor="mm", max_width=w * 0.34)
    meme_text(draw, (w * 0.745, h * 0.86),
              "value is zero\nfor 95%", 24, fill=WHITE, stroke_fill=BLACK,
              stroke_width=4, anchor="mm", max_width=w * 0.34)
    im.save(OUT / "s01-spiderman-pointing.jpg", quality=92)
    print("OK s01-spiderman-pointing.jpg", im.size)


# ============================================================
# s02 — One Does Not Simply (you cannot simply turn building into value)
# ============================================================
def s02_one_does_not_simply():
    overlay("one-does-not-simply.jpg", "s02-one-does-not-simply.jpg", [
        (0.5, 0.09, "one does not simply", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=880)),
        (0.5, 0.88, "turn building into value", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=1000)),
    ])


# ============================================================
# s07 — Distracted Boyfriend (asking colleagues in the office distracts from
#   real users). Resolves: there are no facts inside the building.
# ============================================================
def s07_distracted_boyfriend():
    overlay("distracted-boyfriend.jpg", "s07-distracted-boyfriend.jpg", [
        (0.27, 0.62, "friends'\nopinion", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=340)),
        (0.60, 0.14, "the team", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=340)),
        (0.86, 0.20, "real\nusers", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=300)),
    ])


# ============================================================
# s14 — Drake (Design: reject "jump to the solution", pick "the problem
#   first")
# ============================================================
def s14_drake_double_diamond():
    overlay("drake.jpg", "s14-drake.jpg", [
        (0.76, 0.25, "jump straight\nto the\nsolution", 40,
         dict(fill=BLACK, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=520)),
        (0.76, 0.75, "the right\nproblem\nfirst", 40,
         dict(fill=BLACK, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=520)),
    ])


# ============================================================
# s21 — Anakin/Padme 4-panel. Panels: TL Anakin (statement) / TR Padme
#   (smiling, agreeing) / BL Anakin (escalates) / BR Padme (smile fades,
#   "...right?").
# ============================================================
def s21_anakin_padme():
    im = Image.open(TPL / "anakin-padme.png").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    hw, hh = w // 2, h // 2
    panels = [
        (0.25, 0.90, "code is now\nnearly free"),
        (0.75, 0.90, "so the product\nwill work out?"),
        (0.25, 1.90, "ONLY the code is\nfree, not the judgment"),
        (0.75, 1.90, "...right?"),
    ]
    for cx_frac, cy_row, txt in panels:
        cx = w * cx_frac
        cy = hh * cy_row if cy_row <= 1 else h - hh * (2 - cy_row)
        # cy_row encodes: 0.90 -> near bottom of top row, 1.90 -> near bottom
        # of bottom row (both panels' caption strips sit at each half's foot)
        y = (hh - int(hh * 0.14)) if cy_row < 1 else (h - int(hh * 0.14))
        meme_text(draw, (cx, y), txt, 22, fill=WHITE, stroke_fill=BLACK,
                  stroke_width=4, anchor="mm", max_width=int(hw * 0.92))
    im.save(OUT / "s21-anakin-padme.jpg", quality=92)
    print("OK s21-anakin-padme.jpg", im.size)


# ============================================================
# s28 — Woman Yelling at Cat (Measure: "the metric went up!" vs "is the
#   effect even real?"). Resolves: AI eroded trust in metrics.
# ============================================================
def s28_woman_yelling_cat():
    overlay("woman-yelling-cat.jpg", "s28-woman-yelling-cat.jpg", [
        (0.25, 0.10, "\"the metric\nwent up!\"", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=310)),
        (0.75, 0.10, "is the effect\neven real?", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=310)),
    ])


# ============================================================
# s36 — Disaster Girl (Support: the product is on fire in prod, dashboards
#   green)
# ============================================================
def s36_disaster_girl():
    overlay("disaster-girl.jpg", "s36-disaster-girl.jpg", [
        (0.5, 0.07, "product on fire\nin prod, 24/7", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=680)),
        (0.5, 0.92, "and the dashboard\nis green", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=680)),
    ])


# ============================================================
# s44 — Sad Pablo Escobar (Governance: waiting for the promised ROI from the
#   AI pilot)
# ============================================================
def s44_sad_pablo():
    overlay("sad-pablo.jpg", "s44-sad-pablo.jpg", [
        (0.5, 0.08, "waiting for ROI", 32,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=760)),
        (0.5, 0.90, "from the AI pilot", 32,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=760)),
    ])


# ============================================================
# Content-slide memes (1-2 per section)
# ============================================================

# s09 — Bernie asking (Mom Test: ask about the past, not about the idea)
def s09_bernie():
    top_band("bernie-asking.jpg", "s09-bernie.jpg",
             "I'm once again asking you to tell me about your past, "
             "not about my idea",
             band_frac=0.30, size=30)


# s16 — Bernie asking, same template reused with a distinct caption (no
# joke duplication): here it's the "heuristics are a linter, not a live-user
# test" plea from s16's own claim.
def s16_bernie():
    top_band("bernie-asking.jpg", "s16-bernie.jpg",
             "I'm once again asking you: heuristics are a linter, "
             "not a live-user test",
             band_frac=0.30, size=27)


# s12 — Trade Offer ("I receive / you receive"): the synthetic panel offers
#   7/7 approval, but what you actually get for a go/no-go call is the 3/7
#   real verdict — the only one that counts.
def s12_trade_offer():
    im = Image.open(TPL / "trade-offer.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # Cover the stock template's own baked-in banner + "i receive" / "you
    # receive" captions with FULLY OPAQUE bands sized to their actual extent
    # (top ~19% of the frame), then draw fresh EN text on top.
    header_h = int(h * 0.285)
    draw.rectangle([(0, 0), (w, header_h)], fill=(24, 24, 26))
    draw.rectangle([(0, 0), (w, int(h * 0.075))], fill=(200, 40, 30))
    meme_text(draw, (w * 0.5, int(h * 0.038)), "⚠ TRADE OFFER ⚠", 24,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.94))
    meme_text(draw, (w * 0.26, int(h * 0.125)), "I receive:", 19,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.42))
    meme_text(draw, (w * 0.76, int(h * 0.125)), "you receive:", 19,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.42))
    meme_text(draw, (w * 0.26, int(h * 0.20)), "7 of 7:\nsynth panel says yes",
              16, fill=(240, 220, 100), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.44))
    meme_text(draw, (w * 0.76, int(h * 0.20)), "3 of 7:\nreal people say yes",
              16, fill=(240, 220, 100), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.44))
    meme_text(draw, (w * 0.5, h * 0.965),
              "the go/no-go call rides on the RIGHT card only", 18,
              fill=WHITE, stroke_fill=BLACK, stroke_width=4, anchor="mm",
              max_width=int(w * 0.92))
    im.save(OUT / "s12-trade-offer.jpg", quality=92)
    print("OK s12-trade-offer.jpg", im.size)


# s18 — Is This A Pigeon (AI: "is this an accessible interface?" — WCAG 29%)
def s18_pigeon():
    overlay("is-this-a-pigeon.jpg", "s18-pigeon.jpg", [
        (0.28, 0.07, "AI interface generator", 27,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=460)),
        (0.62, 0.86, "is this an accessible interface?", 27,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=900)),
    ])


# s19 — Clown Applying Makeup (safety features bolted on AFTER launch, as a
#   retrofit)
def s19_clown():
    im = Image.open(TPL / "clown-makeup.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # 4 vertical panels; text on the LEFT of each panel (image is a clown on
    # the right of each). Use white text + stroke centred in left area.
    labels = [
        (0.13, "launch it for engagement"),
        (0.38, "\"who could get hurt?\" — later"),
        (0.63, "a tragedy and a lawsuit"),
        (0.88, "now let's add safeguards"),
    ]
    for ry, txt in labels:
        meme_text(draw, (w * 0.30, h * ry), txt, 24, fill=WHITE,
                  stroke_fill=BLACK, stroke_width=5, anchor="mm",
                  max_width=int(w * 0.5))
    im.save(OUT / "s19-clown.jpg", quality=92)
    print("OK s19-clown.jpg", im.size)


# s26 — Running Away Balloon (100% rollout at once, no canary stage — missed)
def s26_balloon():
    overlay("running-away-balloon.jpg", "s26-balloon.jpg", [
        (0.30, 0.10, "Google", 28,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=300)),
        (0.72, 0.30, "100% rollout at once", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=430)),
        (0.30, 0.88, "1% canary rollout", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=520)),
    ])


# s33 — "Corporate Needs You To Find The Differences" / "They're The Same
#   Picture": Facebook claimed love/wow/sad were friendlier engagement
#   signals, separate from "angry" — but internally all 5 were weighted
#   identically x5. "Spot the difference" -> "there is no difference, they're
#   weighted the same."
def s33_same_picture():
    im = Image.open(TPL / "they-are-same-picture.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # top half (0..~0.585h) is the "spot the difference" photo; template's
    # own caption band sits at y~0.42-0.505h — cover fully with opaque black
    # and redraw a single-language EN line, sized to actually fit ONE line.
    band_top, band_bot = int(h * 0.415), int(h * 0.585)
    draw.rectangle([(0, band_top), (w, band_bot)], fill=(0, 0, 0))
    meme_text(draw, (w * 0.5, (band_top + band_bot) // 2),
              "\"spot the difference: love/wow/sad and angry\"", 22,
              fill=(255, 235, 59), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.92))
    # bottom half's own caption band sits at the very bottom ~0.925-1.0h
    bottom_top = int(h * 0.925)
    draw.rectangle([(0, bottom_top), (w, h)], fill=(0, 0, 0))
    meme_text(draw, (w * 0.5, (bottom_top + h) // 2),
              "\"all 5 weighted x5 — no difference\"", 26, fill=(255, 235, 59),
              stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.9))
    im.save(OUT / "s33-same-picture.jpg", quality=92)
    print("OK s33-same-picture.jpg", im.size)


# s39 — Gru's Plan 4-panel escalation: "dashboards stayed green (panels
#   1-3), then: trust had already been dropping for weeks (panel 4 twist)."
def s39_grus_plan():
    """Blank card sits on the RIGHT ~55-95% of each quadrant (not centred) —
    text must land there, not over Gru's face on the left ~0-55%."""
    im = Image.open(TPL / "grus-plan.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    hw, hh = w // 2, h // 2
    card_cx_frac = 0.755   # centre of the blank card within each half-width
    panels = [
        (0, 0, "dashboard\ngreen"),
        (hw, 0, "dashboard\nstill\ngreen"),
        (0, hh, "dashboard green\nfor a month\nnow"),
        (hw, hh, "trust dropped for\nweeks — dashboard\nnever noticed"),
    ]
    for ox, oy, txt in panels:
        cx = ox + hw * card_cx_frac
        cy = oy + hh * 0.5
        meme_text(draw, (cx, cy), txt, 18, fill=(20, 20, 20),
                  stroke_fill=None, stroke_width=0, anchor="mm",
                  max_width=int(hw * 0.34))
    im.save(OUT / "s39-grus-plan.jpg", quality=92)
    print("OK s39-grus-plan.jpg", im.size)


# s47 — no meme (same as RU): the payoff is best served by a data chart
#   (gen_charts_en funnel chart), avoiding template duplication.


if __name__ == "__main__":
    # section dividers + cover + hook
    s01_spiderman_pointing()
    s02_one_does_not_simply()
    s07_distracted_boyfriend()
    s14_drake_double_diamond()
    s21_anakin_padme()
    s28_woman_yelling_cat()
    s36_disaster_girl()
    s44_sad_pablo()
    # content slides (s09_bernie defined but unused, mirrors RU gen_memes.py
    # — the s09 slide itself does not embed a meme)
    s16_bernie()
    s12_trade_offer()
    s18_pigeon()
    s19_clown()
    s26_balloon()
    s33_same_picture()
    s39_grus_plan()
