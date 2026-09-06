"""
Лекция 2 v3.3 (issue #183, round 2 доработки образов) — регенерация мем-
оверлеев ПОД УВЕЛИЧЕННЫЕ размеры вставки + новые оверлеи для Группы B.

Причина регенерации: в round 1 подписи рисовались под вставку ~1-1.5" ширины;
после увеличения образов до 2.2-3" прежние размеры шрифта (24-34px) дают
~8-9pt на слайде — нечитаемо с проектора. Здесь размеры пересчитаны так,
чтобы на итоговой ширине вставки текст был ≥10.5pt (обычно 12-18pt).

Подписи-источники НЕ рисуются (правило деки — только attribution.md).
Шрифт: DejaVuSans-Bold (кириллица + латиница).
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
    """Классическая мем-вёрстка: белый текст, толстая чёрная обводка."""
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
# s15 — Spider-Man Pointing (вставка ~3.0" ширины → шрифт 52px ≈ 14pt)
# ============================================================
def gen_spiderman_similarity():
    src = WEB / "spiderman-pointing-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 800x450
    band_h = int(h * 0.36)
    canvas = Image.new("RGB", (w, h + band_h), (255, 255, 255))
    canvas.paste(im, (0, band_h))
    draw = ImageDraw.Draw(canvas)
    draw_meme_text(draw, (w / 2, band_h / 2),
                   "«похожи» — не факт что «об одном»",
                   size=52, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w - 40, line_spacing=1.1)
    out = WEB / "spiderman-similarity.jpg"
    canvas.save(out, quality=92)
    print(f"OK {out.name} {canvas.size}")


# ============================================================
# s11 — Always Has Been (вставка ~3.0" ширины → 54px ≈ 12pt / 48px ≈ 11pt)
# ============================================================
def gen_always_has_been_ru_cost():
    src = WEB / "always-has-been-template.png"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 960x540
    draw = ImageDraw.Draw(im)
    draw_meme_text(draw, (w * 0.30, h * 0.11),
                   "русский токен дороже?",
                   size=54, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   max_width=w * 0.56, line_spacing=1.1)
    draw_meme_text(draw, (w * 0.78, h * 0.30),
                   "always has been",
                   size=48, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   max_width=w * 0.42, line_spacing=1.1)
    out = WEB / "always-has-been-ru-cost.jpg"
    im.save(out, quality=92)
    print(f"OK {out.name} {im.size}")


# ============================================================
# s39 — Two Buttons (вставка ~2.3" ширины → LLM 52px ≈ 14.5pt,
#   «обычный код» 38px ≈ 10.6pt); crop верхней панели до y=400 (обе кнопки
#   + начало руки, ratio 1.5 — компактнее в правой колонке)
# ============================================================
def gen_twobuttons_llm_vs_code():
    src = WEB / "twobuttons-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 600x908
    draw = ImageDraw.Draw(im)
    top_h = h * 0.47
    draw_meme_text(draw, (w * 0.24, top_h * 0.28), "LLM",
                   size=52, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w * 0.36)
    draw_meme_text(draw, (w * 0.75, top_h * 0.26), "обычный\nкод",
                   size=38, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   line_spacing=1.0)
    out_full = WEB / "twobuttons-llm-vs-code.jpg"
    im.save(out_full, quality=92)
    crop = im.crop((0, 0, 600, 400))
    out_top = WEB / "twobuttons-llm-vs-code-toponly.jpg"
    crop.save(out_top, quality=92)
    print(f"OK {out_full.name} {im.size}; {out_top.name} {crop.size}")


# ============================================================
# s09 — Math Lady / Confused Lady (вставка ~2.7" → 64px ≈ 18pt):
#   подпись в мем-стиле «[123][456][78]?» — недоумение от того, как
#   токенизатор нарезал число
# ============================================================
def gen_mathlady_tokens():
    src = WEB / "mathlady-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 681x445
    draw = ImageDraw.Draw(im)
    draw_meme_text(draw, (w / 2, h * 0.10), "[123][456][78]?",
                   size=64, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm")
    out = WEB / "mathlady-tokens.jpg"
    im.save(out, quality=92)
    print(f"OK {out.name} {im.size}")


# ============================================================
# s30 — Gandalf You Shall Not Pass (вставка ~2.8" → 76px ≈ 12.8pt):
#   подпись снизу «невалидный токен не пройдёт» — прямая метафора
#   маскирования невалидных токенов конечным автоматом
# ============================================================
def gen_gandalf_token():
    src = WEB / "gandalf-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 1200x586
    draw = ImageDraw.Draw(im)
    draw_meme_text(draw, (w / 2, h * 0.90),
                   "НЕВАЛИДНЫЙ ТОКЕН НЕ ПРОЙДЁТ",
                   size=54, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=6, align="center", anchor="mm",
                   line_spacing=1.05)
    out = WEB / "gandalf-token.jpg"
    im.save(out, quality=92)
    print(f"OK {out.name} {im.size}")


# ============================================================
# s32 — Joker burning money (YouTube maxres thumbnail): crop letterbox
#   (чёрные полосы сверху/снизу) + бейдж «1080p FULL HD» слева-снизу.
#   Итог ~1090x610, ratio 1.79 — под слот 1.8"x1.0" в верхнем контейнере.
# ============================================================
def gen_joker_crop():
    src = WEB / "joker-burning-money-yt.jpg"
    im = Image.open(src).convert("RGB")
    crop = im.crop((190, 55, 1280, 665))
    out = WEB / "joker-burning-money.jpg"
    crop.save(out, quality=92)
    print(f"OK {out.name} {crop.size}")


# ============================================================
# s25 — needle in haystack: умеренный кроп (не «агрессивный» round-1,
#   показывавший только сено) — иголка по центру занимает ~30% ширины,
#   контекст стога сохранён.
# ============================================================
def gen_needle_crop():
    src = WEB / "needle-haystack-wikimedia.jpg"
    im = Image.open(src).convert("RGB")  # 1200x836, иголка ~x480-830 y510-610
    crop = im.crop((250, 180, 1180, 836))
    out = WEB / "needle-haystack-crop.jpg"
    crop.save(out, quality=92)
    print(f"OK {out.name} {crop.size}")


if __name__ == "__main__":
    gen_needle_crop()
    gen_spiderman_similarity()
    gen_always_has_been_ru_cost()
    gen_twobuttons_llm_vs_code()
    gen_mathlady_tokens()
    gen_gandalf_token()
    gen_joker_crop()
