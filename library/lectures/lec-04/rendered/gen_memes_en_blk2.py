"""EN twins of the round-5 meme composites — EN-Sync Block 2 (issue #172).

The RU composites in assets/web/band-*.png have Russian captions baked into
the pixels, so they cannot be reused in the EN deck. This script re-bakes the
ones owned by Block 2 (slide s16 — the poisoned-context loop) with English
captions, using the SAME blank imgflip templates (assets/web/memes-src/*.jpg)
and the same compose_strip geometry/typography as gen_memes_r5.py, so the EN
and RU decks stay visually identical apart from the caption language.

Output: assets/web-en/band-*.png. Attribution: assets/web/attribution.md
(unchanged — the same source templates).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).parent / "assets/web"
SRC = WEB / "memes-src"
OUT_DIR = Path(__file__).parent / "assets/web-en"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DPI = 300  # internal bake resolution -> crisp at small slide-embed sizes
DEEP = (33, 41, 92)          # #21295C
SURFACE = (244, 247, 250)    # #F4F7FA
LIGHT_STROKE = (28, 114, 147)  # #1C7293
WHITE = (255, 255, 255)


def compose_strip(name, crop_box, caption_lines, *, img_h_in=0.64,
                  font_pt=15.5, panel_fill=SURFACE, text_color=DEEP,
                  border_color=LIGHT_STROKE, ext="jpg", flip=False):
    """Identical geometry to gen_memes_r5.compose_strip — see that file."""
    src = Image.open(SRC / f"{name}.{ext}").convert("RGB")
    crop = src.crop(crop_box)
    if flip:
        crop = crop.transpose(Image.FLIP_LEFT_RIGHT)
    img_h_px = round(img_h_in * DPI)
    ratio = crop.width / crop.height
    img_w_px = round(img_h_px * ratio)
    crop = crop.resize((img_w_px, img_h_px), Image.LANCZOS)

    font_px = round(font_pt / 72 * DPI)
    f = ImageFont.truetype(FONT_BOLD, font_px)
    tmp = Image.new("RGB", (10, 10))
    td = ImageDraw.Draw(tmp)
    pad = round(0.09 * DPI)
    max_line_w = max(td.textlength(ln, font=f) for ln in caption_lines)
    panel_w_px = round(max_line_w) + 2 * pad
    panel_h_px = img_h_px

    canvas = Image.new("RGB", (img_w_px + panel_w_px, img_h_px), WHITE)
    canvas.paste(crop, (0, 0))
    panel = Image.new("RGB", (panel_w_px, panel_h_px), panel_fill)
    pd = ImageDraw.Draw(panel)
    pd.rectangle([1, 1, panel_w_px - 2, panel_h_px - 2], outline=border_color,
                 width=max(2, round(0.018 * DPI)))
    asc, desc = f.getmetrics()
    lh = round((asc + desc) * 1.14)
    total_h = lh * len(caption_lines)
    y0 = (panel_h_px - total_h) // 2
    for i, ln in enumerate(caption_lines):
        tw = pd.textlength(ln, font=f)
        pd.text(((panel_w_px - tw) / 2, y0 + i * lh), ln, font=f,
                fill=text_color)
    canvas.paste(panel, (img_w_px, 0))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"band-{name}.png"
    canvas.save(out)
    print(f"OK {out.name} {canvas.size} -> embed "
          f"{canvas.width/DPI:.2f}x{canvas.height/DPI:.2f}in")
    return out


if __name__ == "__main__":
    # s16 (poisoned-context loop) — X, X Everywhere (Buzz/Woody).
    # RU: «плохой паттерн, / плохой паттерн везде»
    compose_strip("x-everywhere", (300, 100, 1750, 1350),
                  ["bad pattern,", "bad pattern everywhere"], font_pt=13)

    # s18 (four levels of agent context) — Monkey Puppet: the silent-failure
    # mode of compaction (a rejected decision can vanish from the summary with
    # no error). RU: «решение тихо / исчезло при сжатии»
    compose_strip("monkey-puppet", (0, 260, 470, 768),
                  ["a decision quietly", "vanished in compaction"], font_pt=13)
