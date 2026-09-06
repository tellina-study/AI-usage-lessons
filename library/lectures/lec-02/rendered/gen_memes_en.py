"""
Lecture 2 EN (issue #188) — meme overlay regeneration with EN captions.

Only regenerates memes that have RU text baked into image pixels (via PIL
draw_meme_text) in the RU builder. Bare templates with no baked text (Pam,
Pepe Silvia, Spotlight, dice, matryoshka, needle-haystack, Joker crop, xkcd)
are reused as-is from assets/web/ — no regeneration needed for those.

Technique ported from gen_memes_v33_r2.py (same draw_meme_text helper,
same font, same stroke conventions) — only strings changed to EN, and each
output file gets an -en suffix so RU and EN assets coexist in assets/web/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).resolve().parent / "assets/web"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size):
    return ImageFont.truetype(FONT_BOLD, size)


def draw_meme_text(draw, xy, text, size, *, fill=(255, 255, 255),
                   stroke_fill=(0, 0, 0), stroke_width=4, align="center",
                   anchor=None, max_width=None, line_spacing=1.15):
    """Classic meme layout: white text, thick black stroke (or plain
    dark text when stroke_width=0) — same helper as gen_memes_v33_r2.py."""
    f = font(size)
    if max_width is not None:
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
        text = "\n".join(lines)
    draw.multiline_text(xy, text, font=f, fill=fill, stroke_fill=stroke_fill,
                        stroke_width=stroke_width, align=align, anchor=anchor,
                        spacing=(size * (line_spacing - 1)))


# ============================================================
# s05a — Surprised Pikachu: "the model confidently answers wrong — it
# sees chunks, not letters"
# ============================================================
def gen_surprised_pikachu_en():
    src = WEB / "surprised-pikachu-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 1704x2102, blank top band ~0..27%
    draw = ImageDraw.Draw(im)
    blank_h = h * 0.27
    draw_meme_text(draw, (w / 2, blank_h / 2),
                   "the model confidently gives a wrong answer —\n"
                   "it sees chunks, not letters",
                   size=64, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w - 140, line_spacing=1.2)
    out = WEB / "surprised-pikachu-tokenize-en.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s08 — Expanding Brain (4 panels): patch-race strawberry/cranberry
# ============================================================
def gen_expanding_brain_en():
    src = WEB / "expanding-brain-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 804x992
    panel_h = h / 4
    draw = ImageDraw.Draw(im)
    panels = [
        "GPT-5.2:\n2 r's in strawberry",
        "GPT-5.5: strawberry ✓\ncranberry ✗",
        "GPT-5.6:\ncranberry ✓",
        "StrawberryBench:\nstill 60%",
    ]
    left_w = w * 0.5  # white left column of the panels ~50%
    for i, txt in enumerate(panels):
        cy = panel_h * i + panel_h / 2
        draw_meme_text(draw, (left_w / 2, cy), txt, size=38,
                       fill=(20, 20, 20), stroke_fill=None, stroke_width=0,
                       align="center", anchor="mm", max_width=left_w - 30,
                       line_spacing=1.15)
    out = WEB / "expanding-brain-strawberry-en.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s11 — Always Has Been: "the Russian token costs more? / always has
# been"
# ============================================================
def gen_always_has_been_en():
    src = WEB / "always-has-been-template.png"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 960x540
    draw = ImageDraw.Draw(im)
    draw_meme_text(draw, (w * 0.30, h * 0.11),
                   "the Russian token\ncosts more?",
                   size=48, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   max_width=w * 0.56, line_spacing=1.1)
    draw_meme_text(draw, (w * 0.78, h * 0.30),
                   "always has been",
                   size=44, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   max_width=w * 0.42, line_spacing=1.1)
    out = WEB / "always-has-been-ru-cost-en.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s39 — Two Buttons: "LLM" / "plain code"
# ============================================================
def gen_twobuttons_en():
    src = WEB / "twobuttons-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 600x908
    draw = ImageDraw.Draw(im)
    top_h = h * 0.47
    draw_meme_text(draw, (w * 0.24, top_h * 0.28), "LLM",
                   size=52, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w * 0.36)
    draw_meme_text(draw, (w * 0.75, top_h * 0.26), "plain\ncode",
                   size=38, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   line_spacing=1.0)
    out_full = WEB / "twobuttons-llm-vs-code-en.jpg"
    im.save(out_full, quality=92)
    crop = im.crop((0, 0, 600, 400))
    out_top = WEB / "twobuttons-llm-vs-code-toponly-en.jpg"
    crop.save(out_top, quality=92)
    print(f"OK {out_full.name} {im.size}; {out_top.name} {crop.size}")


# ============================================================
# s09 — Math Lady: "[123][456][78]?" (symbols only — no RU baked in,
# but regenerated with the same overlay for consistency/traceability;
# not strictly required since s09 reuses the RU asset unchanged per
# brief)
# ============================================================
# (Not regenerated — mathlady-tokens.jpg has no RU text baked in,
# reused as-is; see brief.)


# ============================================================
# s30 — Gandalf You Shall Not Pass: "INVALID TOKEN SHALL NOT PASS"
# ============================================================
def gen_gandalf_en():
    src = WEB / "gandalf-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 1200x586
    draw = ImageDraw.Draw(im)
    draw_meme_text(draw, (w / 2, h * 0.90),
                   "INVALID TOKEN SHALL NOT PASS",
                   size=54, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   line_spacing=1.05)
    out = WEB / "gandalf-token-en.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s15 — Spider-Man pointing at Spider-Man: "similar" != "about the
# same thing"
# ============================================================
def gen_spiderman_similarity_en():
    src = WEB / "spiderman-pointing-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 800x450
    band_h = int(h * 0.36)
    canvas = Image.new("RGB", (w, h + band_h), (255, 255, 255))
    canvas.paste(im, (0, band_h))
    draw = ImageDraw.Draw(canvas)
    draw_meme_text(draw, (w / 2, band_h / 2),
                   "“similar” doesn't mean “about the same thing”",
                   size=44, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w - 40, line_spacing=1.1)
    out = WEB / "spiderman-similarity-en.jpg"
    canvas.save(out, quality=92)
    print(f"OK {out.name} {canvas.size}")


if __name__ == "__main__":
    gen_surprised_pikachu_en()
    gen_expanding_brain_en()
    gen_always_has_been_en()
    gen_twobuttons_en()
    gen_gandalf_en()
    gen_spiderman_similarity_en()
