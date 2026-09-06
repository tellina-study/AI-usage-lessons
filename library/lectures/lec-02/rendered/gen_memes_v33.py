"""
Лекция 2 v3.3 (issue #183, round 5) — генерация мем-оверлеев через PIL для
новых визуалов (s11, s15, s39). Тот же подход, что gen_memes_v32.py:
draw_meme_text (белый текст, чёрная обводка) добавляется поверх готового
шаблона; подписи-источники НЕ рисуются на картинке (правило деки, см.
attribution.md).

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
# s15 — Spider-Man Pointing at Spider-Man (similarity ≠ релевантность)
#   Подписи над каждым персонажем: "Похожие векторы" / "Один смысл?" —
#   классическая метафора "выглядят одинаково, а не факт что об одном".
#   Добавляем компактную полосу текста сверху изображения (не перекрывает
#   персонажей), т.к. оригинальный шаблон не имеет пустого поля.
# ============================================================
def gen_spiderman_similarity():
    src = WEB / "spiderman-pointing-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 800x450
    # Расширяем канвас сверху на белую полосу под подпись (не мнём картинку)
    band_h = int(h * 0.34)
    canvas = Image.new("RGB", (w, h + band_h), (255, 255, 255))
    canvas.paste(im, (0, band_h))
    draw = ImageDraw.Draw(canvas)
    draw_meme_text(draw, (w / 2, band_h / 2),
                   "«похожи» — не факт что «об одном»",
                   size=34, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w - 30, line_spacing=1.15)
    out = WEB / "spiderman-similarity.jpg"
    canvas.save(out, quality=92)
    print(f"OK {out} {canvas.size}")


# ============================================================
# s11 — Always Has Been (стоимость русского токена — «всегда так было»)
#   Классический формат: астронавт-1 удивлён открытием, астронавт-2 с
#   пистолетом отвечает "always has been". Подпись сверху единой строкой
#   (свободное чёрное небо в верхней трети кадра — безопасно для текста).
# ============================================================
def gen_always_has_been_ru_cost():
    src = WEB / "always-has-been-template.png"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 960x540
    draw = ImageDraw.Draw(im)
    # Верхняя треть — чёрное небо со звёздами, безопасно для белого текста
    draw_meme_text(draw, (w * 0.30, h * 0.10),
                   "русский токен дороже?",
                   size=34, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=5, align="center", anchor="mm",
                   max_width=w * 0.5, line_spacing=1.1)
    draw_meme_text(draw, (w * 0.82, h * 0.32),
                   "always has been",
                   size=30, fill=(255, 255, 255), stroke_fill=(0, 0, 0),
                   stroke_width=5, align="center", anchor="mm",
                   max_width=w * 0.34, line_spacing=1.1)
    out = WEB / "always-has-been-ru-cost.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s39 — Two Buttons (LLM vs обычный код — трудный выбор инструмента)
#   Верхняя панель: 2 кнопки с подписями "LLM" / "обычный код" над самими
#   кнопками (белые прямоугольники-шаблоны уже пустые — подписи внутри
#   верхней панели, не перекрывают лицо в нижней панели).
# ============================================================
def gen_twobuttons_llm_vs_code():
    src = WEB / "twobuttons-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 600x908, верхняя панель ~0..47%
    draw = ImageDraw.Draw(im)
    top_h = h * 0.47
    # Левая кнопка (~x 0.05..0.45), правая (~x 0.55..0.95) — подписи чуть
    # выше кружков-кнопок (кнопки расположены на белых карточках примерно
    # в середине верхней панели по вертикали)
    draw_meme_text(draw, (w * 0.24, top_h * 0.30), "LLM",
                   size=32, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w * 0.34)
    draw_meme_text(draw, (w * 0.75, top_h * 0.28), "обычный\nкод",
                   size=24, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w * 0.30, line_spacing=1.0)
    out = WEB / "twobuttons-llm-vs-code.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


if __name__ == "__main__":
    gen_spiderman_similarity()
    gen_always_has_been_ru_cost()
    gen_twobuttons_llm_vs_code()
