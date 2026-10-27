"""
Generate stylized PNG assets for Lec 8 slides — Phase 6+7 visual loop completion.

Replaces all [ FRAME ], [ news screenshot ], [ frame ], [ playable 3D world ]
placeholders with semantically-rich illustrations:
- News-card mocks (s21-s25, s28, s29) — Bloomberg/Bird&Bird/Court docket/RIAA/Reed Smith/Futurism stylized
- Service-frame mocks (s07 Sora, s08 character grid, s09 ElevenLabs, s10 Genie, s10a Kandinsky+Kling)
- All use Ocean palette + Lucide-style icons.

Output: /tmp/lec-08-wt/library/lectures/lec-08/assets/screenshots/*.png
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/tmp/lec-08-wt/library/lectures/lec-08")
OUT = ROOT / "assets/screenshots"
OUT.mkdir(parents=True, exist_ok=True)

# === Ocean Palette ===
DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
LIGHT = (0x1C, 0x72, 0x93)
TEAL = (0x02, 0x80, 0x90)
SURFACE = (0xF4, 0xF7, 0xFA)
WHITE = (0xFF, 0xFF, 0xFF)
GOLD = (0xF0, 0xAB, 0x00)
SLATE = (0x6B, 0x76, 0x85)
GOLD_TINT = (0xFE, 0xF5, 0xE0)
TEAL_TINT = (0xE6, 0xF2, 0xF4)
SOFT_GREY = (0xE5, 0xEA, 0xF0)


# Font discovery
def font(size, bold=False, italic=False):
    """Find a serif/sans font."""
    candidates_bold = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    candidates_italic = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    ]
    candidates_regular = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    if bold:
        chain = candidates_bold + candidates_regular
    elif italic:
        chain = candidates_italic + candidates_regular
    else:
        chain = candidates_regular
    for p in chain:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text_wrap(text, font_obj, max_width):
    """Word-wrap text to fit max_width."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        bbox = font_obj.getbbox(test)
        w = bbox[2] - bbox[0]
        if w > max_width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


# =========================================================================
# News card template — used for s21-s25, s28, s29
# =========================================================================
def make_news_card(filename, source_label, source_color, headline, sub_lines,
                   accent_quote=None, width=1140, height=720,
                   meta_chip=None):
    """Generate a stylized news article card.

    source_label — e.g. "BLOOMBERG LAW" / "BIRD & BIRD" / "REUTERS"
    source_color — banner color
    headline — main headline (large bold)
    sub_lines — list of paragraph lines (body text)
    accent_quote — optional pull-quote (gold-tinted box)
    meta_chip — optional small chip in top right (e.g. date)
    """
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    # Outer frame
    rounded_rect(draw, (8, 8, width - 8, height - 8), radius=18,
                 outline=LIGHT, width=2)
    # Source banner
    banner_h = 88
    rounded_rect(draw, (8, 8, width - 8, banner_h),
                 radius=18, fill=source_color)
    # Cover bottom-radius hack
    draw.rectangle((8, banner_h - 30, width - 8, banner_h), fill=source_color)
    f_src = font(28, bold=True)
    draw.text((40, 28), source_label, font=f_src, fill=WHITE)
    if meta_chip:
        f_meta = font(20, bold=True)
        bbox = f_meta.getbbox(meta_chip)
        cw = bbox[2] - bbox[0] + 24
        draw.rounded_rectangle((width - 40 - cw, 24, width - 40, 64),
                                radius=18, fill=WHITE)
        draw.text((width - 40 - cw + 12, 32), meta_chip, font=f_meta, fill=source_color)

    # Headline
    f_head = font(42, bold=True)
    f_body = font(22)
    headline_lines = text_wrap(headline, f_head, width - 100)
    y_cursor = banner_h + 36
    for line in headline_lines:
        draw.text((40, y_cursor), line, font=f_head, fill=DEEP)
        y_cursor += 52
    y_cursor += 20
    # Decorative rule under headline
    draw.rectangle((40, y_cursor, 220, y_cursor + 4), fill=GOLD)
    y_cursor += 28

    # Sub paragraph(s)
    for para in sub_lines:
        para_lines = text_wrap(para, f_body, width - 100)
        for line in para_lines:
            draw.text((40, y_cursor), line, font=f_body, fill=SLATE)
            y_cursor += 32
        y_cursor += 14

    # Optional pull-quote box
    if accent_quote:
        box_y = y_cursor + 10
        box_h = 110
        if box_y + box_h > height - 60:
            box_h = max(80, height - 70 - box_y)
        rounded_rect(draw, (40, box_y, width - 40, box_y + box_h),
                     radius=14, fill=GOLD_TINT, outline=GOLD, width=2)
        f_quote = font(22, italic=True)
        quote_lines = text_wrap(accent_quote, f_quote, width - 140)[:3]
        qy = box_y + 18
        for line in quote_lines:
            draw.text((60, qy), line, font=f_quote, fill=DEEP)
            qy += 30

    img.save(OUT / filename, "PNG", optimize=True)
    print(f"  ✓ {filename}")


# =========================================================================
# Service-frame card — used for s07, s10
# =========================================================================
def make_service_frame(filename, service_label, prompt_line,
                       caption_lines, accent_color=MID, width=1100, height=900,
                       url_line=None, tagline=None):
    """Generate a stylized service interface mockup (Sora 2 / Genie 3 /etc)."""
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    # Outer frame
    rounded_rect(draw, (8, 8, width - 8, height - 8), radius=20,
                 outline=LIGHT, width=2)
    # Top app bar
    bar_h = 70
    rounded_rect(draw, (8, 8, width - 8, bar_h),
                 radius=20, fill=accent_color)
    draw.rectangle((8, bar_h - 30, width - 8, bar_h), fill=accent_color)
    f_svc = font(26, bold=True)
    draw.text((30, 22), service_label, font=f_svc, fill=WHITE)
    # Window controls
    for i, color in enumerate([(0xFF, 0x5F, 0x57), (0xFE, 0xBC, 0x2E), (0x28, 0xC9, 0x40)]):
        cx = width - 60 - i * 28
        draw.ellipse((cx - 8, 26, cx + 8, 42), fill=color)

    # Prompt bar
    py = bar_h + 30
    rounded_rect(draw, (30, py, width - 30, py + 60),
                 radius=14, fill=SURFACE, outline=LIGHT, width=1)
    f_prompt = font(22)
    draw.text((50, py + 18), prompt_line, font=f_prompt, fill=SLATE)
    # Generate button
    btn_w = 160
    rounded_rect(draw, (width - 30 - btn_w - 8, py + 8, width - 38, py + 52),
                 radius=10, fill=GOLD)
    f_btn = font(20, bold=True)
    bbox = f_btn.getbbox("ГЕНЕРИРОВАТЬ")
    bw = bbox[2] - bbox[0]
    draw.text((width - 38 - btn_w/2 - bw/2 - 4, py + 18), "ГЕНЕРИРОВАТЬ", font=f_btn, fill=DEEP)

    # Output preview frame
    out_y = py + 90
    out_h = height - out_y - 140
    rounded_rect(draw, (30, out_y, width - 30, out_y + out_h),
                 radius=18, fill=DEEP)
    # Stylized "video frame" with abstract gradient look
    for i in range(0, out_h - 20, 6):
        alpha = i / (out_h - 20)
        c = (int(DEEP[0] + (LIGHT[0] - DEEP[0]) * alpha),
             int(DEEP[1] + (LIGHT[1] - DEEP[1]) * alpha),
             int(DEEP[2] + (LIGHT[2] - DEEP[2]) * alpha))
        draw.rectangle((50, out_y + 20 + i, width - 50, out_y + 24 + i), fill=c)

    # Play button overlay
    cx = width // 2
    cy = out_y + out_h // 2
    draw.ellipse((cx - 60, cy - 60, cx + 60, cy + 60), fill=WHITE, outline=GOLD, width=3)
    triangle = [(cx - 18, cy - 28), (cx + 30, cy), (cx - 18, cy + 28)]
    draw.polygon(triangle, fill=GOLD)
    # Frame timecode chip
    f_chip = font(18, bold=True)
    rounded_rect(draw, (width - 200, out_y + out_h - 50, width - 50, out_y + out_h - 20),
                 radius=14, fill=GOLD_TINT, outline=GOLD, width=1)
    if tagline:
        draw.text((width - 192, out_y + out_h - 45), tagline, font=f_chip, fill=DEEP)
    else:
        draw.text((width - 192, out_y + out_h - 45), "1080p · 25s", font=f_chip, fill=DEEP)

    # Caption text below
    y_cap = out_y + out_h + 18
    f_cap = font(20, bold=True)
    for line in caption_lines:
        draw.text((30, y_cap), line, font=f_cap, fill=DEEP)
        y_cap += 32

    # URL bar at the bottom
    if url_line:
        f_url = font(16, italic=True)
        draw.text((30, height - 36), url_line, font=f_url, fill=LIGHT)

    img.save(OUT / filename, "PNG", optimize=True)
    print(f"  ✓ {filename}")


# =========================================================================
# Character-consistency grid — 2x2 stylized "frames" with character
# =========================================================================
def make_character_grid(filename, width=1100, height=900):
    """Generate 2x2 grid showing same stylized character across 4 scenes."""
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (8, 8, width - 8, height - 8), radius=18,
                 outline=LIGHT, width=2)

    # Header banner
    bar_h = 70
    rounded_rect(draw, (8, 8, width - 8, bar_h),
                 radius=18, fill=MID)
    draw.rectangle((8, bar_h - 30, width - 8, bar_h), fill=MID)
    f_h = font(26, bold=True)
    draw.text((30, 22), "MIDJOURNEY · Omni Reference v7", font=f_h, fill=WHITE)

    # 2x2 grid of frames
    grid_top = bar_h + 30
    grid_bottom = height - 80
    grid_h_total = grid_bottom - grid_top
    cell_gap = 18
    cell_w = (width - 60 - cell_gap) / 2
    cell_h = (grid_h_total - cell_gap) / 2

    scenes = [
        ("Scene 1 · Desert", (0xE8, 0xC4, 0x80), "Same character"),
        ("Scene 2 · City", (0x52, 0x70, 0x9C), "Same outfit"),
        ("Scene 3 · Forest", (0x4F, 0x7A, 0x5E), "Same pose"),
        ("Scene 4 · Studio", (0xC9, 0x8B, 0x5C), "Same face"),
    ]
    f_lbl = font(20, bold=True)
    f_sub = font(16, italic=True)
    for i, (title, bgc, sub) in enumerate(scenes):
        row = i // 2
        col = i % 2
        x = 30 + col * (cell_w + cell_gap)
        y = grid_top + row * (cell_h + cell_gap)
        # Frame background (scene-specific muted color)
        rounded_rect(draw, (x, y, x + cell_w, y + cell_h),
                     radius=14, fill=bgc)
        # Character silhouette (simple stylized humanoid)
        char_cx = x + cell_w / 2
        char_cy = y + cell_h / 2 + 20
        # Head
        head_r = 36
        draw.ellipse((char_cx - head_r, char_cy - 100, char_cx + head_r, char_cy - 100 + head_r * 2),
                     fill=(0xF5, 0xDC, 0xC5), outline=DEEP, width=2)
        # Body
        draw.polygon([
            (char_cx - 50, char_cy + 80),
            (char_cx + 50, char_cy + 80),
            (char_cx + 35, char_cy - 30),
            (char_cx - 35, char_cy - 30),
        ], fill=DEEP, outline=WHITE)
        # Label chip
        rounded_rect(draw, (x + 10, y + 10, x + 220, y + 38),
                     radius=8, fill=WHITE, outline=DEEP, width=1)
        draw.text((x + 22, y + 14), title, font=f_lbl, fill=DEEP)
        # Sub
        draw.text((x + 12, y + cell_h - 28), sub, font=f_sub, fill=WHITE)

    # Caption
    f_cap = font(18, italic=True)
    draw.text((30, height - 50), "Один character — 4 разных сцены — visual identity preserved",
              font=f_cap, fill=LIGHT)

    img.save(OUT / filename, "PNG", optimize=True)
    print(f"  ✓ {filename}")


# =========================================================================
# Side-by-side comparison frames (s10a Kandinsky vs Kling)
# =========================================================================
def make_kandinsky_vs_kling(filename, width=900, height=700):
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (4, 4, width - 4, height - 4), radius=16,
                 outline=LIGHT, width=2)
    # Title
    f_t = font(20, bold=True)
    draw.text((20, 16), "VIDEO QUALITY GAP · side-by-side", font=f_t, fill=TEAL)

    # 2 columns
    col_w = (width - 60) / 2
    col_y = 60
    col_h = height - col_y - 60
    # Kandinsky (left)
    rounded_rect(draw, (20, col_y, 20 + col_w, col_y + col_h),
                 radius=12, fill=SOFT_GREY, outline=LIGHT, width=2)
    # Stylized lower-res look — pixelated bands
    inner_x = 30
    inner_y = col_y + 40
    inner_w = col_w - 20
    inner_h = col_h - 80
    # Coarse pixel-block pattern
    block_size = 24
    for bx in range(int(inner_w // block_size)):
        for by in range(int(inner_h // block_size)):
            r = (DEEP[0] + bx * 4) % 255
            g = (MID[1] + by * 6) % 255
            b = (LIGHT[2] + (bx + by) * 3) % 255
            draw.rectangle((inner_x + bx * block_size, inner_y + by * block_size,
                            inner_x + (bx + 1) * block_size, inner_y + (by + 1) * block_size),
                           fill=(r, g, b))
    f_lbl = font(18, bold=True)
    rounded_rect(draw, (30, col_y + 10, 30 + 230, col_y + 38),
                 radius=8, fill=WHITE, outline=MID, width=1)
    draw.text((40, col_y + 14), "Kandinsky 5.0 Video", font=f_lbl, fill=MID)
    f_meta = font(14)
    draw.text((30, col_y + col_h - 32), "768×512 · 10 сек · Apache 2.0", font=f_meta, fill=SLATE)

    # Kling (right)
    rx = 40 + col_w
    rounded_rect(draw, (rx, col_y, rx + col_w, col_y + col_h),
                 radius=12, fill=DEEP, outline=GOLD, width=3)
    # Smooth high-res gradient
    inner_x = rx + 10
    inner_y = col_y + 40
    inner_w = col_w - 20
    inner_h = col_h - 80
    block_size = 4
    for bx in range(int(inner_w // block_size)):
        for by in range(int(inner_h // block_size)):
            alpha_y = by / (inner_h / block_size)
            r = int(DEEP[0] + (TEAL[0] - DEEP[0]) * alpha_y)
            g = int(DEEP[1] + (TEAL[1] - DEEP[1]) * alpha_y)
            b = int(DEEP[2] + (TEAL[2] - DEEP[2]) * alpha_y)
            draw.rectangle((inner_x + bx * block_size, inner_y + by * block_size,
                            inner_x + (bx + 1) * block_size, inner_y + (by + 1) * block_size),
                           fill=(r, g, b))
    rounded_rect(draw, (rx + 10, col_y + 10, rx + 10 + 130, col_y + 38),
                 radius=8, fill=WHITE, outline=GOLD, width=1)
    draw.text((rx + 22, col_y + 14), "Kling 3.0", font=f_lbl, fill=GOLD)
    draw.text((rx + 10, col_y + col_h - 32),
              "4K · 60 fps · 15 сек · ELO #1 (1243)", font=f_meta, fill=GOLD)

    img.save(OUT / filename, "PNG", optimize=True)
    print(f"  ✓ {filename}")


# =========================================================================
# Genie 3 playable world frame — stylized 3D scene
# =========================================================================
def make_genie_world(filename, width=1300, height=850):
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (8, 8, width - 8, height - 8), radius=18,
                 outline=LIGHT, width=2)
    # Top bar
    bar_h = 60
    rounded_rect(draw, (8, 8, width - 8, bar_h),
                 radius=18, fill=DEEP)
    draw.rectangle((8, bar_h - 30, width - 8, bar_h), fill=DEEP)
    f_t = font(22, bold=True)
    draw.text((30, 18), "GENIE 3 · DeepMind · playable 3D world", font=f_t, fill=WHITE)
    # FPS chip
    rounded_rect(draw, (width - 180, 14, width - 28, 50),
                 radius=10, fill=GOLD)
    f_fps = font(18, bold=True)
    draw.text((width - 168, 22), "24 fps · real-time", font=f_fps, fill=DEEP)

    # 3D scene area
    sy = bar_h + 30
    sh = height - sy - 60
    # Sky gradient
    for y in range(sy, sy + int(sh * 0.55)):
        alpha = (y - sy) / (sh * 0.55)
        r = int(0x6F + (0xE3 - 0x6F) * alpha)
        g = int(0x9A + (0xC9 - 0x9A) * alpha)
        b = int(0xC8 + (0x9D - 0xC8) * alpha)
        draw.rectangle((30, y, width - 30, y + 1), fill=(r, g, b))
    # Mountain silhouettes
    mountain_y = sy + int(sh * 0.40)
    draw.polygon([
        (30, sy + int(sh * 0.55)),
        (300, mountain_y),
        (520, sy + int(sh * 0.48)),
        (760, mountain_y - 40),
        (1000, sy + int(sh * 0.50)),
        (1270, sy + int(sh * 0.55)),
        (1270, sy + int(sh * 0.55)),
        (30, sy + int(sh * 0.55)),
    ], fill=(0x40, 0x5A, 0x77))
    # Ground
    for y in range(sy + int(sh * 0.55), sy + sh):
        alpha = (y - sy - sh * 0.55) / (sh * 0.45)
        r = int(0x5A + (0x2A - 0x5A) * alpha)
        g = int(0x6B + (0x40 - 0x6B) * alpha)
        b = int(0x42 + (0x20 - 0x42) * alpha)
        draw.rectangle((30, y, width - 30, y + 1), fill=(r, g, b))
    # Castle (centre)
    cx = width // 2
    cy = sy + int(sh * 0.42)
    # Main keep
    draw.rectangle((cx - 100, cy, cx + 100, cy + 200), fill=(0x60, 0x60, 0x6A))
    # Battlements
    for i in range(5):
        bx = cx - 100 + i * 50
        draw.rectangle((bx, cy - 20, bx + 30, cy), fill=(0x60, 0x60, 0x6A))
    # Towers
    draw.rectangle((cx - 130, cy - 30, cx - 80, cy + 200), fill=(0x55, 0x55, 0x5F))
    draw.rectangle((cx + 80, cy - 30, cx + 130, cy + 200), fill=(0x55, 0x55, 0x5F))
    # Tower roof (cone)
    draw.polygon([(cx - 135, cy - 30), (cx - 75, cy - 30), (cx - 105, cy - 90)],
                 fill=DEEP)
    draw.polygon([(cx + 75, cy - 30), (cx + 135, cy - 30), (cx + 105, cy - 90)],
                 fill=DEEP)
    # Flag
    draw.line([(cx, cy - 20), (cx, cy - 90)], fill=DEEP, width=3)
    draw.polygon([(cx, cy - 90), (cx + 30, cy - 80), (cx, cy - 70)],
                 fill=GOLD)
    # Door
    draw.rectangle((cx - 18, cy + 130, cx + 18, cy + 200), fill=DEEP)

    # WASD controls overlay (bottom-left)
    wx = 60
    wy = sy + sh - 130
    f_k = font(20, bold=True)
    for key_x, key_y, key in [
        (40, 0, "W"), (0, 40, "A"), (40, 40, "S"), (80, 40, "D"),
    ]:
        rounded_rect(draw, (wx + key_x, wy + key_y, wx + key_x + 36, wy + key_y + 36),
                     radius=6, fill=WHITE, outline=DEEP, width=2)
        bbox = f_k.getbbox(key)
        kw = bbox[2] - bbox[0]
        draw.text((wx + key_x + 18 - kw / 2, wy + key_y + 6), key, font=f_k, fill=DEEP)
    f_ctl = font(14, italic=True)
    draw.text((wx, wy + 90), "Free-roam controls · WASD",
              font=f_ctl, fill=WHITE)

    # Caption
    f_cap = font(16, italic=True)
    draw.text((30, height - 36),
              "Text → playable 3D world · medieval castle · light wind · interactive @ 24fps",
              font=f_cap, fill=LIGHT)

    img.save(OUT / filename, "PNG", optimize=True)
    print(f"  ✓ {filename}")


# =========================================================================
# Generate all assets
# =========================================================================
def main():
    print("Generating Lec 8 visual assets…")

    # ====== Service-frame mockups ======
    make_service_frame(
        "s07-sora2-frame.png",
        service_label="OpenAI Sora 2 · openai.com/index/sora-2/",
        prompt_line="cinematic, 25s narrative scene with sync audio and cameos",
        caption_lines=[
            "Sora 2 · Text-to-video с sync audio · cameos",
            "25 сек · 1080p · $0.10/сек · фев 2026",
        ],
        url_line="openai.com/index/sora-2/",
        tagline="1080p · 25s",
        accent_color=MID,
    )

    make_character_grid("s08-character-grid.png")

    make_genie_world("s10-genie3-world.png")

    make_kandinsky_vs_kling("s10a-kandinsky-vs-kling.png")

    # ElevenLabs voice library mock (compact)
    make_service_frame(
        "s09-elevenlabs.png",
        service_label="ElevenLabs · Voice Library",
        prompt_line="Search voices · multilingual · clone from 1 min audio",
        caption_lines=[
            "Voice Library · 32+ языков · production-grade",
            "<$1 за минуту dubbing · enterprise tier",
        ],
        url_line="elevenlabs.io/voice-library",
        tagline="<$1 / мин",
        accent_color=LIGHT,
    )

    # ====== News-card mocks ======
    make_news_card(
        "s21-nyt-bloomberg.png",
        source_label="BLOOMBERG LAW",
        source_color=DEEP,
        headline="OpenAI ordered to hand over 20M ChatGPT user logs in NYT lawsuit",
        sub_lines=[
            "Judge ordered OpenAI to preserve and produce 20 million ChatGPT user conversations as part of the New York Times copyright lawsuit.",
            "The court's discovery ruling marks the largest such order against an AI company. SJ deadline: 2 April 2026.",
        ],
        accent_quote="The regurgitation theory — that AI can reproduce training data verbatim — is now central to the case.",
        meta_chip="Dec 2023",
    )

    make_news_card(
        "s22-getty-bird.png",
        source_label="BIRD & BIRD",
        source_color=MID,
        headline="UK High Court rules Stability AI did not infringe Getty's primary copyright claims",
        sub_lines=[
            "On 4 November 2025 Mrs Justice Joanna Smith handed down judgment in Getty Images v Stability AI.",
            "The court held that AI model weights are not themselves 'copies' under sections 17–18 of the Copyright, Designs and Patents Act 1988 (CDPA).",
            "Trademark and passing-off claims remain pending. US case MTD: 10 February 2026.",
        ],
        accent_quote="Weights are not infringing copies under the CDPA — but US fair-use analysis remains untested.",
        meta_chip="04 Nov 2025",
    )

    make_news_card(
        "s23-andersen-docket.png",
        source_label="US DISTRICT COURT · ND CA · DOCKET",
        source_color=DEEP,
        headline="Andersen et al. v. Stability AI Ltd. — Class action survives motion to dismiss",
        sub_lines=[
            "Case 3:23-cv-00201-WHO. Plaintiffs: 10 named artists representing a putative class of working visual artists.",
            "Judge William Orrick (August 2024) denied Stability AI's motion to dismiss DMCA and right-of-publicity claims, allowing discovery to proceed.",
            "Third amended complaint filed 27 February 2026. Trial scheduled 8 September 2026.",
        ],
        accent_quote="Style 'in the manner of' may not be copyrightable, but DMCA + right-of-publicity claims survive MTD.",
        meta_chip="Jan 2023",
    )

    make_news_card(
        "s24-riaa-suno.png",
        source_label="RIAA · PRESS RELEASE",
        source_color=GOLD,
        headline="RIAA files mass copyright infringement suits against Suno and Udio",
        sub_lines=[
            "On 24 June 2024 the Recording Industry Association of America, on behalf of UMG, Warner, and Sony, filed parallel lawsuits in federal court.",
            "Outcome to date: UMG settled with Udio on 29 October 2025; Warner licensed Suno late 2025. Sony remains the last major actively litigating.",
            "Suno summary-judgment hearing scheduled July 2026.",
        ],
        accent_quote="Lawsuit-driven licensing — not all-AI-music-banned. Two of three majors settled into joint platforms.",
        meta_chip="24 Jun 2024",
    )

    make_news_card(
        "s25-thomson-reedsmith.png",
        source_label="REED SMITH · CLIENT ALERT",
        source_color=MID,
        headline="Thomson Reuters v. Ross Intelligence — first US fair-use rejection",
        sub_lines=[
            "Judge Stephanos Bibas (D. Del.) ruled February 2025 that 2,200 of 3,000 Westlaw editorial headnotes were infringed.",
            "Bibas applied the Warhol v. Goldsmith four-factor analysis and rejected Ross's fair-use defence.",
            "Caveat: Ross was a non-generative AI (legal search). LLM/diffusion test cases pending.",
        ],
        accent_quote="Fair use is not a default. Generative-AI test cases (NYT, Andersen, Getty US) will go further.",
        meta_chip="Feb 2025",
    )

    # ====== Marketing case visuals ======
    # s28 — Google AI Overview / Slop
    make_news_card(
        "s28-ai-overview-glue.png",
        source_label="GOOGLE AI OVERVIEW · live in production",
        source_color=GOLD,
        headline='"Add 1/8 cup of non-toxic glue to the sauce" — viral AI answer',
        sub_lines=[
            "Query: how to keep cheese from sliding off pizza?",
            "AI Overview cited an 11-year-old Reddit joke as authoritative recipe advice.",
            "Companion answer to 'how many rocks should I eat per day?' — pulled from The Onion satire.",
        ],
        accent_quote="Source quality > volume. Recursive training on unfiltered web → MAD (Nature 2024).",
        meta_chip="May 2024",
    )

    make_news_card(
        "s29-si-futurism.png",
        source_label="FUTURISM · INVESTIGATIVE",
        source_color=DEEP,
        headline="Sports Illustrated published articles by fake AI-generated writers",
        sub_lines=[
            "Investigation found articles credited to 'Drew Ortiz' — a wholly fictional author whose profile photo was AI-generated.",
            "Followed by Amazon Kindle 2023-24 (Authors Guild): only 19 of top 100 bestsellers had real human authors.",
            "Knockoff names imitated real jazz figures and financial advisors.",
        ],
        accent_quote="Legacy trust = key brand asset. AI-pseudonyms destroy it instantly.",
        meta_chip="Nov 2023",
    )

    # s26 — CNN Arup deepfake article card (extended quote)
    make_news_card(
        "s26-arup-cnn.png",
        source_label="CNN · BUSINESS",
        source_color=DEEP,
        headline="Finance worker pays out $25 million after video call with deepfake CFO",
        sub_lines=[
            "Hong Kong, Arup (UK engineering, designer of Sydney Opera House).",
            "Finance worker received email from 'CFO', joined video call featuring deepfake-CFO and multiple deepfake-colleagues, completed 15 wire transfers totalling HK$200 million (US$25.6M).",
            "Loss discovered when worker followed up with real headquarters.",
        ],
        accent_quote="Video call is no longer identity proof. Out-of-band verification is mandatory.",
        meta_chip="16 May 2024",
    )

    # s27 — NPR Korea headline (text-only sensitive case)
    make_news_card(
        "s27-korea-npr.png",
        source_label="NPR · INTERNATIONAL",
        source_color=MID,
        headline="South Korea grappling with a deepfake crisis in schools",
        sub_lines=[
            "Over 230 Telegram group chats discovered distributing deepfake imagery of classmates and teachers, generated from social-media selfies.",
            "6,500 takedown requests in first half of 2024 — 4× the 2023 figure.",
            "Of suspects identified, 74% aged 10-19 years.",
        ],
        accent_quote="Text-only headline by editorial choice — sensitive case. Numbers tell the story.",
        meta_chip="6 Sep 2024",
    )

    # s30 — Toys R Us Cannes sentiment (Marketing Interactive)
    make_news_card(
        "s30-toysrus-cannes.png",
        source_label="MARKETING INTERACTIVE",
        source_color=LIGHT,
        headline="Toys R Us Cannes 2024 AI ad — sentiment swing −10 percentage points",
        sub_lines=[
            "Cannes Lions 2024 nostalgic AI-generated ad campaign.",
            "Positive sentiment: 12.2% → 3.4% (−8.8pp); negative sentiment: 13.5% → 53.4% (+39.9pp).",
            "Industry response: Joe Russo (Avengers director) called the ad 'absolutely terrible'.",
        ],
        accent_quote="AI ad without human creative leadership = measurable brand damage. Sentiment, not CTR.",
        meta_chip="Jun 2024",
    )

    # s35 — YouTube creator survey
    make_news_card(
        "s35-youtube-socialblade.png",
        source_label="SOCIAL BLADE · CREATOR SURVEY",
        source_color=GOLD,
        headline="47.3% of YouTube creators dropped AI thumbnails after measuring impact",
        sub_lines=[
            "Survey of 1,247 creators with channels >100k subscribers, December 2025.",
            "Reported drops: −22% CTR for 'creepy skin' thumbnails; −19% CTR for mobile-text failures.",
            "First-15-second drop-off increased 61.8% when thumbnail promise didn't match content.",
        ],
        accent_quote="End-users notice and punish AI shortcuts. Measurable in CTR, retention, brand sentiment.",
        meta_chip="Dec 2025",
    )

    print("All assets generated.")


if __name__ == "__main__":
    main()
