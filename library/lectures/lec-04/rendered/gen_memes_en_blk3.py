"""EN caption twins of the round-5 meme composites — block 3 only (#172).

The blank imgflip templates in assets/web/memes-src/ are language-neutral and
are reused as-is; only the bordered caption panel is re-baked in English. The
composition technique (`compose_strip`) is copied verbatim from
gen_memes_r5.py so the EN strip is pixel-compatible with its RU twin — same
crop, same height, same Ocean-surface panel.

Naming convention for the EN twins (please follow it in the other EN blocks):
    RU  assets/web/band-<name>.png
    EN  assets/web/band-<name>-en.png

Block 3 owns exactly one of the seven round-5 composites:
    band-hide-the-pain-harold-merged-en.png  (slide s20, the 70% problem)

Run: python3 gen_memes_en_blk3.py
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


def compose_strip(name, crop_box, caption_lines, *, out_name, img_h_in=0.64,
                  font_pt=15.5, panel_fill=SURFACE, text_color=DEEP,
                  border_color=LIGHT_STROKE, ext="jpg"):
    src = Image.open(SRC / f"{name}.{ext}").convert("RGB")
    crop = src.crop(crop_box)
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
    out = WEB / out_name
    canvas.save(out)
    print(f"OK {out.name} {canvas.size} -> embed "
          f"{canvas.width/DPI:.2f}x{canvas.height/DPI:.2f}in")
    return out


if __name__ == "__main__":
    # s20 (the 70% problem, "almost right" code) — Hide the Pain Harold,
    # both panels merged side by side. The merged source is produced by
    # gen_memes_r5.py and is language-neutral, so it is reused as-is.
    compose_strip("hide-the-pain-harold-merged", (0, 0, 960, 296),
                  ["looks fine —", "falls over at 3 a.m."], font_pt=13.5,
                  out_name="band-hide-the-pain-harold-merged-en.png")
