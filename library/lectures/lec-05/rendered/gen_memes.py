"""Лекция 5 — генерация мем-оверлеев (Directive 2) через PIL.

Метод как в lec-02 `gen_memes_v33.py`: берём реальный evergreen мем-шаблон
(imgflip template gallery, скачан в assets/meme_templates/*.jpg с .url-логом),
накладываем русскую подпись (DejaVuSans-Bold, белый текст с чёрной обводкой —
классическая мем-вёрстка; либо чёрный текст на белой добавленной полосе, если
у шаблона нет свободного тёмного поля). Подписи-источники НЕ рисуются на
картинке (правило деки: no photo-attribution on slide).

Каждый мем резолвится к конкретному тезису слайда, не декоративен, не дублирует
шаблон/шутку другого мема. Полный лог (слайд → шаблон → RU-подпись → тезис) —
в iteration-log.md.

Выход: assets/memes/<slide>-<concept>.jpg
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REND = Path(__file__).resolve().parent
TPL = REND / "assets/meme_templates"
OUT = REND / "assets/memes"
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
# s01 — This Is Fine (сборка горит дёшево, ценности ноль — «всё нормально»)
#   Resolves: парадокс — сборка почти бесплатна, а ценность — нет.
# ============================================================
def s01_this_is_fine():
    im = Image.open(TPL / "this-is-fine.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # top panel of This-Is-Fine has room; use top band for clean 1-liner
    meme_text(draw, (w * 0.5, h * 0.09),
              "«код почти бесплатный»", 30, fill=WHITE, stroke_fill=BLACK,
              stroke_width=5, anchor="mm", max_width=w * 0.9)
    meme_text(draw, (w * 0.5, h * 0.60),
              "ценности — ноль", 30, fill=WHITE, stroke_fill=BLACK,
              stroke_width=5, anchor="mm", max_width=w * 0.7)
    im.save(OUT / "s01-this-is-fine.jpg", quality=92)
    print("OK s01-this-is-fine.jpg", im.size)


# ============================================================
# s02 — One Does Not Simply (нельзя просто превратить сборку в ценность)
# ============================================================
def s02_one_does_not_simply():
    overlay("one-does-not-simply.jpg", "s02-one-does-not-simply.jpg", [
        (0.5, 0.09, "нельзя просто взять", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=880)),
        (0.5, 0.88, "и превратить сборку в ценность", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=1000)),
    ])


# ============================================================
# s07 — Distracted Boyfriend (офисное «спросить у друзей» отвлекает от
#   реальных пользователей). Resolves: внутри офиса нет фактов.
# ============================================================
def s07_distracted_boyfriend():
    overlay("distracted-boyfriend.jpg", "s07-distracted-boyfriend.jpg", [
        (0.27, 0.62, "мнение\nдрузей", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=340)),
        (0.60, 0.14, "команда", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=340)),
        (0.86, 0.20, "реальные\nпользователи", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=300)),
    ])


# ============================================================
# s14 — Drake (Дизайн: отвергаем «сразу решение», выбираем «сначала проблема»)
# ============================================================
def s14_drake_double_diamond():
    overlay("drake.jpg", "s14-drake.jpg", [
        (0.76, 0.25, "прыгнуть\nсразу к\nрешению", 40,
         dict(fill=BLACK, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=520)),
        (0.76, 0.75, "сначала —\nправильная\nпроблема", 40,
         dict(fill=BLACK, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=520)),
    ])


# ============================================================
# s21 — Expanding Brain (Сборка: стоимость кода схлопнулась)
#   4 уровня: писать вручную → автодополнение → агент пишет модуль →
#   код почти бесплатный (узкое место сместилось).
# ============================================================
def s21_expanding_brain():
    im = Image.open(TPL / "expanding-brain.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # 4 panels stacked; text goes in the LEFT ~48% (dark on brain side varies)
    # expanding-brain left column is where text usually goes on white bg
    labels = [
        (0.125, "писать код руками"),
        (0.375, "автодополнение"),
        (0.625, "агент пишет модуль"),
        (0.875, "сборка ≈ бесплатна"),
    ]
    # left half is image (brains), text panel is actually on the LEFT in this
    # template variant? imgflip Expanding-Brain: brains on RIGHT, text LEFT.
    for ry, txt in labels:
        meme_text(draw, (w * 0.25, h * ry), txt, 30, fill=BLACK,
                  stroke_fill=None, stroke_width=0, anchor="mm",
                  max_width=int(w * 0.44))
    im.save(OUT / "s21-expanding-brain.jpg", quality=92)
    print("OK s21-expanding-brain.jpg", im.size)


# ============================================================
# s28 — Woman Yelling at Cat (Измерение: «выглядит отлично!» vs «а реален ли
#   эффект?»). Resolves: AI снизил доверие метрике.
# ============================================================
def s28_woman_yelling_cat():
    overlay("woman-yelling-cat.jpg", "s28-woman-yelling-cat.jpg", [
        (0.25, 0.10, "«метрика выросла!»", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=310)),
        (0.75, 0.10, "а эффект реален?", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=310)),
    ])


# ============================================================
# s36 — Disaster Girl (Поддержка: продукт в проде «горит», а метрики зелёные)
# ============================================================
def s36_disaster_girl():
    overlay("disaster-girl.jpg", "s36-disaster-girl.jpg", [
        (0.5, 0.07, "продукт в проде 24/7", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=680)),
        (0.5, 0.92, "а дашборд зелёный", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=680)),
    ])


# ============================================================
# s44 — Sad Pablo Escobar (Управление: жду обещанный ROI от ИИ-пилота)
# GATE-B fix: caption baked "AI-пилота" (Latin) into the raster image itself
# — the AI->ИИ cascade over build-script text/markdown does not touch text
# already burned into a PNG, so this needed a separate regenerate.
# ============================================================
def s44_sad_pablo():
    overlay("sad-pablo.jpg", "s44-sad-pablo.jpg", [
        (0.5, 0.08, "жду ROI", 32,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=760)),
        (0.5, 0.90, "от ИИ-пилота", 32,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=760)),
    ])


# ============================================================
# Content-slide memes (1-2 per section)
# ============================================================

# s09 — Bernie asking (Mom Test: спрашивай про прошлое, не про идею)
def s09_bernie():
    top_band("bernie-asking.jpg", "s09-bernie.jpg",
             "я снова прошу: расскажите про ваше прошлое, а не про мою идею",
             band_frac=0.30, size=32)


# s16 — Bernie asking, GATE-B replacement meme (Design section lost its
# only non-serious-case meme when the s19 clown was removed for tonal
# reasons — this restores >=1 tasteful content meme in Раздел 2). Distinct
# caption from s09's use of the same template (no joke duplication): here
# it is the "линтер, не замена живому тесту" plea from s16's own claim.
def s16_bernie():
    top_band("bernie-asking.jpg", "s16-bernie.jpg",
             "я снова прошу: эвристики — линтер, а не тест на живом пользователе",
             band_frac=0.30, size=28)


# s12 — Surprised Pikachu (синт-панель: 7/7! реальные: 3/7)
def s12_pikachu():
    """The stock imgflip Surprised-Pikachu template has a genuine ~40%-tall
    BLANK WHITE band above the face (not cropped/stretched — verified against
    the raw template pixels). GATE-B fix: crop that oversized band down to a
    normal top-caption strip, then set BLACK text (not white+stroke, which is
    invisible on white) sized to actually fill the strip; add a matching
    bottom white band (instead of overlaying near the frame edge, which
    clipped) so both captions are fully legible and nothing touches the
    image border. Net effect: correct 1:1-ish aspect (no stretch happens
    downstream either — add_image() in _helpers.py already preserves aspect;
    the *visual* stretch students perceived was actually the oversized blank
    band + illegible caption reading as "broken")."""
    im = Image.open(TPL / "surprised-pikachu.jpg").convert("RGB")
    w, h = im.size
    # crop the excess blank white area: keep a slim ~14% top strip instead
    # of the stock ~40% band (face starts at y=0.40h per pixel-scan).
    face_top = int(h * 0.40)
    keep_band = int(h * 0.16)
    cropped = im.crop((0, face_top - keep_band, w, h))
    cw, ch = cropped.size
    # add a bottom white band of matching height for the second caption so
    # text never overlays the character's face and never touches the edge.
    bottom_band = int(ch * 0.16)
    canvas = Image.new("RGB", (cw, ch + bottom_band), WHITE)
    canvas.paste(cropped, (0, 0))
    draw = ImageDraw.Draw(canvas)
    # top caption: BLACK text (band is white — white+stroke was illegible)
    meme_text(draw, (cw * 0.5, keep_band * 0.5),
              "синт-панель: «7 из 7 задач»", 34, fill=BLACK,
              stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=cw * 0.92)
    # bottom caption: BLACK text on the new white band, fully inside frame
    meme_text(draw, (cw * 0.5, ch + bottom_band * 0.5),
              "реальные люди: 3 из 7", 34, fill=BLACK,
              stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=cw * 0.92)
    canvas.save(OUT / "s12-pikachu.jpg", quality=92)
    print("OK s12-pikachu.jpg", canvas.size)


# s18 — Is This A Pigeon (ИИ: «это доступный интерфейс?» — WCAG 29%)
def s18_pigeon():
    overlay("is-this-a-pigeon.jpg", "s18-pigeon.jpg", [
        (0.28, 0.07, "ИИ-генератор интерфейса", 27,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=460)),
        (0.62, 0.86, "это доступный интерфейс?", 30,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=900)),
    ])


# s19 — Clown Applying Makeup (safety-фичи докручены ПОСЛЕ запуска, ретрофитом)
def s19_clown():
    im = Image.open(TPL / "clown-makeup.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # 4 vertical panels; text on the LEFT of each panel (image is a clown on
    # the right of each). Use white text + stroke centred in left area.
    labels = [
        (0.13, "запускаем ради вовлечённости"),
        (0.38, "«кто может пострадать?» — потом"),
        (0.63, "трагедия и иск"),
        (0.88, "теперь добавим защиту"),
    ]
    for ry, txt in labels:
        meme_text(draw, (w * 0.30, h * ry), txt, 26, fill=WHITE,
                  stroke_fill=BLACK, stroke_width=5, anchor="mm",
                  max_width=int(w * 0.5))
    im.save(OUT / "s19-clown.jpg", quality=92)
    print("OK s19-clown.jpg", im.size)


# s26 — Running Away Balloon (запуск на 100% сразу, канареечная раскатка — мимо)
def s26_balloon():
    overlay("running-away-balloon.jpg", "s26-balloon.jpg", [
        (0.30, 0.10, "Google", 28,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=300)),
        (0.72, 0.30, "раскатка на 100% сразу", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=430)),
        (0.30, 0.88, "канареечная раскатка 1%", 26,
         dict(fill=WHITE, stroke_fill=BLACK, stroke_width=5, anchor="mm",
              max_width=520)),
    ])


# s33 — Change My Mind (все 5 реакций ×5, не только «гнев»)
def s33_change_my_mind():
    top_band("change-my-mind.jpg", "s33-change-my-mind.jpg",
             "Facebook усилил ВСЕ 5 реакций ×5 — не только «гнев»",
             band_frac=0.24, size=32)


# s39 — Hide the Pain Harold (дашборд зелёный, а доверие уже падает)
def s39_harold():
    top_band("hide-the-pain-harold.jpg", "s39-harold.jpg",
             "все метрики зелёные, а доверие пользователей падает уже недели",
             band_frac=0.30, size=30)


# s47 — Drake reused? NO — use One-Does-Not-Simply already at s02. Use
#   Woman-Yelling? at s28. s47 needs its own: use Surprised-Pikachu? at s12.
#   -> use Sad-Pablo? at s44. Distinct template needed. Use Change-My-Mind? s33.
#   All big templates assigned. Reuse Drake is forbidden (dup). s47's payoff is
#   best served by a data chart (gen_charts funnel) — SKIP meme, chart instead.
#   (documented: s47 uses funnel chart, not a meme, to avoid template dup.)


if __name__ == "__main__":
    # section dividers + cover + hook
    s01_this_is_fine()
    s02_one_does_not_simply()
    s07_distracted_boyfriend()
    s14_drake_double_diamond()
    s21_expanding_brain()
    s28_woman_yelling_cat()
    s36_disaster_girl()
    s44_sad_pablo()
    # content slides
    s09_bernie()
    s16_bernie()
    s12_pikachu()
    s18_pigeon()
    s19_clown()
    s26_balloon()
    s33_change_my_mind()
    s39_harold()
