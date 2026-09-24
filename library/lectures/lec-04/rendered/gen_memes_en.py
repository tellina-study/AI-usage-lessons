"""EN twin of gen_memes_r5.py — bakes ENGLISH captions onto the SAME blank
imgflip templates (assets/web/memes-src/*.jpg) used by the RU deck, writing
`assets/web/band-<name>-en.png`.

Issue #172 (EN parity). The RU composites (`band-<name>.png`) have Russian
captions baked into the pixels, so they cannot be reused in the English deck —
only the blank source templates are language-agnostic. Composition technique,
crop boxes, panel geometry and palette are copied verbatim from gen_memes_r5.py
so the EN strips are pixel-compatible drop-ins at the same slide coordinates.

EN-sync block 4 covers the three strips used by slides s28 (review failure /
complacency), s31 (slopsquatting) and s32 (Replit). Running this script is
additive — it never overwrites a RU `band-<name>.png`.

Attribution: assets/web/attribution.md (unchanged; no attribution text is baked
onto slides — deck convention).

Build: python3 gen_memes_en.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).parent / "assets/web"
SRC = WEB / "memes-src"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

DPI = 300  # internal bake resolution -> crisp at small slide-embed sizes
DEEP = (33, 41, 92)            # #21295C
SURFACE = (244, 247, 250)      # #F4F7FA
LIGHT_STROKE = (28, 114, 147)  # #1C7293
WHITE = (255, 255, 255)


def font(sz):
    return ImageFont.truetype(FONT_BOLD, sz)


def compose_strip_en(name, crop_box, caption_lines, *, img_h_in=0.64,
                     font_pt=13, ext="jpg"):
    """Same geometry as gen_memes_r5.compose_strip, EN caption, `-en` output."""
    src = Image.open(SRC / f"{name}.{ext}").convert("RGB")
    crop = src.crop(crop_box)
    img_h_px = round(img_h_in * DPI)
    ratio = crop.width / crop.height
    img_w_px = round(img_h_px * ratio)
    crop = crop.resize((img_w_px, img_h_px), Image.LANCZOS)

    f = font(round(font_pt / 72 * DPI))
    td = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    pad = round(0.09 * DPI)
    panel_w_px = round(max(td.textlength(ln, font=f)
                           for ln in caption_lines)) + 2 * pad
    panel_h_px = img_h_px

    canvas = Image.new("RGB", (img_w_px + panel_w_px, img_h_px), WHITE)
    canvas.paste(crop, (0, 0))
    panel = Image.new("RGB", (panel_w_px, panel_h_px), SURFACE)
    pd = ImageDraw.Draw(panel)
    pd.rectangle([1, 1, panel_w_px - 2, panel_h_px - 2], outline=LIGHT_STROKE,
                 width=max(2, round(0.018 * DPI)))
    asc, desc = f.getmetrics()
    lh = round((asc + desc) * 1.14)
    y0 = (panel_h_px - lh * len(caption_lines)) // 2
    for i, ln in enumerate(caption_lines):
        pd.text(((panel_w_px - pd.textlength(ln, font=f)) / 2, y0 + i * lh),
                ln, font=f, fill=DEEP)
    canvas.paste(panel, (img_w_px, 0))
    out = WEB / f"band-{name}-en.png"
    canvas.save(out)
    print(f"OK {out.name} {canvas.size} -> embed "
          f"{canvas.width / DPI:.2f}x{canvas.height / DPI:.2f}in")
    return out


if __name__ == "__main__":
    # s28 display (review complacency / rubber-stamp) — Evil Kermit
    compose_strip_en("evil-kermit", (0, 0, 700, 325),
                     ['"I should read the diff"', '"eh, good enough"'])

    # s31 display (slopsquatting) — Domino Effect (cascading chain)
    compose_strip_en("domino-effect", (350, 60, 820, 565),
                     ["one fake package", "name -> full exploit"])

    # s32 display (Replit culmination) — Boardroom Suggestion, panel 3 only
    compose_strip_en("boardroom-panel3", (0, 0, 500, 216),
                     ['"do not touch!" —', "the agent commits anyway"])
