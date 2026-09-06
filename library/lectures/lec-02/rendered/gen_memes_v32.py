"""
Лекция 2 v3.2 (issue #183 round 4) — генерация мем-оверлеев через PIL.
Owner-фидбек: "я просил мемы и иллюстрации, но вижу только 1 мем (пират) и
1 хорошую иллюстрацию (кости)!" — заменяем скриншоты/научные диаграммы/
титульные страницы на узнаваемые мем-форматы с текстом, наложенным через
ImageDraw (классическая мем-вёрстка: белый текст, чёрная обводка).

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
    """Классическая мем-вёрстка: белый текст, толстая чёрная обводка.
    Простой word-wrap если max_width задан."""
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
# s08 — Expanding Brain (4 панели): гонка патчей strawberry/cranberry
# ============================================================
def gen_expanding_brain():
    src = WEB / "expanding-brain-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 804x992
    panel_h = h / 4
    draw = ImageDraw.Draw(im)
    panels = [
        "GPT-5.2:\n2 r в strawberry",
        "GPT-5.5: strawberry ✓\ncranberry ✗",
        "GPT-5.6:\ncranberry ✓",
        "StrawberryBench:\nвсё ещё 60%",
    ]
    left_w = w * 0.5  # белая левая колонка панелей ~50%
    for i, txt in enumerate(panels):
        cy = panel_h * i + panel_h / 2
        draw_meme_text(draw, (left_w / 2, cy), txt, size=40,
                       fill=(20, 20, 20), stroke_fill=None, stroke_width=0,
                       align="center", anchor="mm", max_width=left_w - 30,
                       line_spacing=1.15)
    out = WEB / "expanding-brain-strawberry.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s10 — Magikarp (замена скриншота Playground, SolidGoldMagikarp)
#   Просто ресайз/паддинг для встраивания — подпись рисуем на слайде через
#   text_box (не на самой картинке), картинка остаётся официальным
#   артворком без наложения.
# ============================================================
def prep_magikarp():
    src = WEB / "magikarp-official.png"
    im = Image.open(src).convert("RGB")
    # Лёгкий паддинг + белый фон уже есть; ничего не меняем, просто
    # проверим размер и пересохраним как чистый PNG.
    out = WEB / "magikarp-clean.png"
    im.save(out)
    print(f"OK {out} {im.size}")


# ============================================================
# s12a — Pam «They're the same picture» (word2vec similarity)
#   Шаблон уже содержит английскую надпись "Corporate needs you..." —
#   оставляем как есть (это часть узнаваемого формата), добавляем свою
#   русскую подпись СНИЗУ отдельным текстовым блоком на слайде (не на
#   картинке) — см. build_lec02.py section_divider. Просто копируем файл
#   под чистым именем для консистентности.
# ============================================================
def prep_pam():
    src = WEB / "pam-same-picture-template.jpg"
    im = Image.open(src).convert("RGB")
    out = WEB / "pam-same-picture.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s18a — Spotlight (луч высвечивает одно, вокруг темнота)
# ============================================================
def prep_spotlight():
    src = WEB / "spotlight-template.jpg"
    im = Image.open(src).convert("RGB")
    out = WEB / "spotlight-clean.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s31 — горшочек каши (кадр из мультфильма 1984, Союзмультфильм)
# ============================================================
def prep_gorshochek():
    src = WEB / "gorshochek-yt1-max.jpg"
    im = Image.open(src).convert("RGB")
    # Кроп чёрных полос по бокам (pillarbox 1280x720 -> убираем чёрные
    # вертикальные полосы ~120px с каждой стороны, видно на превью).
    w, h = im.size
    crop_left = int(w * 0.094)
    crop_right = w - crop_left
    im2 = im.crop((crop_left, 0, crop_right, h))
    out = WEB / "gorshochek-1984-crop.jpg"
    im2.save(out, quality=92)
    print(f"OK {out} {im2.size}")


# ============================================================
# s33a — Chonk chart (котики по размеру) — заменяем матрёшку опционально
# ============================================================
def gen_chonk_chart():
    """Собственный chonk-chart с 4 категориями по размеру модели
    (котики недоступны лицензионно чисто, поэтому строим Ocean-palette
    сравнительную шкалу с эмодзи-подобными котами через текст — fallback,
    см. iteration-log: используем матрёшку, chonk chart не потребовался)."""
    pass


# ============================================================
# s35a — Pepe Silvia (Charlie Day, conspiracy board — сборка конвейера)
# ============================================================
def prep_pepe_silvia():
    src = WEB / "pepe-silvia-template.jpg"
    im = Image.open(src).convert("RGB")
    out = WEB / "pepe-silvia.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


# ============================================================
# s05a — Surprised Pikachu (робот/токенизация: уверенно неправильно)
# ============================================================
def gen_surprised_pikachu():
    src = WEB / "surprised-pikachu-template.jpg"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 1704x2102, белая полоса верх ~0..27%
    draw = ImageDraw.Draw(im)
    blank_h = h * 0.27
    draw_meme_text(draw, (w / 2, blank_h / 2), "модель уверенно отвечает "
                   "неправильно —\nона видит куски, не буквы",
                   size=68, fill=(20, 20, 20), stroke_fill=None,
                   stroke_width=0, align="center", anchor="mm",
                   max_width=w - 140, line_spacing=1.2)
    out = WEB / "surprised-pikachu-tokenize.jpg"
    im.save(out, quality=92)
    print(f"OK {out} {im.size}")


if __name__ == "__main__":
    gen_expanding_brain()
    prep_magikarp()
    prep_pam()
    prep_spotlight()
    prep_gorshochek()
    prep_pepe_silvia()
    gen_surprised_pikachu()
