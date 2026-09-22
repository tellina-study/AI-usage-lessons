"""Round-5 (issue owner ask, 2026-09-22) — real imgflip meme templates +
RU captions baked via PIL, replacing/augmenting round-4's logo-badge-only
pass. Font/stroke conventions ported from lec-02/gen_memes_v33_r2.py +
lec-03/make_memes_v6.py; the single composition technique used here
(`compose_strip`: cropped character + bordered Ocean-surface caption panel
side by side) is new for this deck — see iteration-log-part2.md Round-5
"Why a new 'band' composite technique" for why (this deck's boxes are too
packed for lec-02/03's on-image column captions to fit anywhere).

Blank templates: assets/web/memes-src/*.jpg + .url sidecar (imgflip direct
URL, no API/auth). Composites: assets/web/band-*.png. Attribution: assets/web/
attribution.md only — no attribution text baked onto slides (deck convention).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).parent / "assets/web"
SRC = WEB / "memes-src"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

DPI = 300  # internal bake resolution -> crisp at small slide-embed sizes
DEEP = (33, 41, 92)      # #21295C
MID = (6, 90, 130)       # #065A82
SURFACE = (244, 247, 250)  # #F4F7FA
LIGHT_STROKE = (28, 114, 147)  # #1C7293
WHITE = (255, 255, 255)
BLACK = (15, 15, 15)


def font(sz, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, sz)


def compose_strip(name, crop_box, caption_lines, *, img_h_in=0.64,
                  font_pt=15.5, panel_fill=SURFACE, text_color=DEEP,
                  border_color=LIGHT_STROKE, ext="jpg", flip=False):
    """Crop the recognizable character(s) out of the source template, place
    at fixed height, append a caption panel (Ocean surface tint, bordered)
    to the right sized to fit 1-2 short lines at `font_pt`. Used for the
    5 'bottom-band' slots (~0.6-0.65in tall gap between gold_callout and
    refs_of_slide on this deck's dense slides — see iteration-log)."""
    src = Image.open(SRC / f"{name}.{ext}").convert("RGB")
    crop = src.crop(crop_box)
    if flip:
        crop = crop.transpose(Image.FLIP_LEFT_RIGHT)
    img_h_px = round(img_h_in * DPI)
    ratio = crop.width / crop.height
    img_w_px = round(img_h_px * ratio)
    crop = crop.resize((img_w_px, img_h_px), Image.LANCZOS)

    font_px = round(font_pt / 72 * DPI)
    f = font(font_px, True)
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
    out = WEB / f"band-{name}.png"
    canvas.save(out)
    print(f"OK {out.name} {canvas.size} -> embed {canvas.width/DPI:.2f}x{canvas.height/DPI:.2f}in")
    return out


if __name__ == "__main__":
    # 1. s15 — poisoned-context loop: X, X Everywhere (Buzz/Woody)
    compose_strip("x-everywhere", (300, 100, 1750, 1350),
                 ["плохой паттерн,", "плохой паттерн везде"], font_pt=13)

    # 2. s21-func (anti-hype benchmarks) — Mocking Spongebob
    compose_strip("mocking-spongebob", (0, 0, 502, 353),
                 ["фРоНтИр,", "в 4 рАзА бЫсТрЕе"], font_pt=13)

    # 3. s27-func (review complacency / rubber-stamp) — Evil Kermit
    compose_strip("evil-kermit", (0, 0, 700, 325),
                 ["«надо прочитать diff»", "«и так сойдёт»"], font_pt=13)

    # 4. s30-func (slopsquatting) — Domino Effect (cascading chain)
    compose_strip("domino-effect", (350, 60, 820, 565),
                 ["одно фейк-имя", "пакета → эксплойт"], font_pt=13)

    # 5. s18-func (persistent instructions / context rot) — Monkey Puppet
    #    (crop to one panel, away from the oversized blank caption area)
    compose_strip("monkey-puppet", (0, 260, 470, 768),
                 ["решение тихо", "исчезло при сжатии"], font_pt=13)

    # 6. s20-func (70%-problem, "почти правильный код") — Hide the Pain
    #    Harold: BOTH panels merged side-by-side (same face, same smile —
    #    the joke IS that nothing visibly changes) + one caption panel.
    harold = Image.open(SRC / "hide-the-pain-harold.jpg").convert("RGB")
    h_top = harold.crop((0, 0, 480, 296))
    h_bot = harold.crop((0, 305, 480, 601))
    merged_h = Image.new("RGB", (960, 296), WHITE)
    merged_h.paste(h_top, (0, 0))
    merged_h.paste(h_bot, (480, 0))
    merged_h.save(SRC / "hide-the-pain-harold-merged.jpg", quality=92)
    compose_strip("hide-the-pain-harold-merged", (0, 0, 960, 296),
                 ["выглядит нормально —", "падает в 3 часа ночи"], font_pt=13.5)

    # 7. s31-func (Replit culmination) — Boardroom Suggestion, panel 3 only
    #    (the consequence split: ignored warning -> defenestration) — swaps
    #    round-4's small Replit logo badge (see iteration-log Round-5 §7).
    board = Image.open(SRC / "boardroom-suggestion.jpg").convert("RGB")
    panel3 = board.crop((0, 433, 500, 649))
    panel3.save(SRC / "boardroom-panel3.jpg", quality=92)
    compose_strip("boardroom-panel3", (0, 0, 500, 216),
                 ["«не трогать!» —", "агент всё равно коммитит"], font_pt=13)
