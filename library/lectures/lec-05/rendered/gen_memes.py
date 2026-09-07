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
# s01 — Spider-Man Pointing at Spider-Man (REPLACES This-Is-Fine — GATE-B
#   fix, audit 2026-09-07: This-Is-Fine collides with Lecture 2 AND its
#   "denial of an ongoing disaster" meaning is a tonal mismatch — s01's claim
#   is TWO SIMULTANEOUSLY TRUE FACTS pointing at each other, not denial.
#   Two identical Spider-Men accusing each other = exactly that structure.
#   Resolves: «сборка почти бесплатна» и «ценности почти никто не извлёк» —
#   оба факта истинны одновременно, ни один не отменяет другой.
# ============================================================
def s01_spiderman_pointing():
    im = Image.open(TPL / "spiderman-pointing.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    meme_text(draw, (w * 0.235, h * 0.86),
              "сборка\nпочти бесплатна", 24, fill=WHITE, stroke_fill=BLACK,
              stroke_width=4, anchor="mm", max_width=w * 0.34)
    meme_text(draw, (w * 0.745, h * 0.86),
              "ценность —\nноль у 95%", 24, fill=WHITE, stroke_fill=BLACK,
              stroke_width=4, anchor="mm", max_width=w * 0.34)
    im.save(OUT / "s01-spiderman-pointing.jpg", quality=92)
    print("OK s01-spiderman-pointing.jpg", im.size)


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
# s21 — Anakin/Padmé 4-panel (REPLACES Expanding Brain — GATE-B fix, audit
#   2026-09-07: expanding-brain collides with Lecture 2). "…right?" escalating
#   disbelief format fits the divider's own claim: сборка кода почти
#   бесплатна — и это НЕ решает узкое место продукта, «...ведь так?»
#   Panels: TL Anakin (statement) / TR Padmé (smiling, agreeing) /
#   BL Anakin (escalates) / BR Padmé (smile fades, «...right?»).
# ============================================================
def s21_anakin_padme():
    im = Image.open(TPL / "anakin-padme.png").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    hw, hh = w // 2, h // 2
    panels = [
        (0.25, 0.90, "код теперь\nпочти бесплатный"),
        (0.75, 0.90, "значит, продукт\nполучится?"),
        (0.25, 1.90, "бесплатный ТОЛЬКО\nкод, не суждение"),
        (0.75, 1.90, "...ведь так?"),
    ]
    for cx_frac, cy_row, txt in panels:
        cx = w * cx_frac
        cy = hh * cy_row if cy_row <= 1 else h - hh * (2 - cy_row)
        # cy_row encodes: 0.90 -> near bottom of top row, 1.90 -> near bottom
        # of bottom row (both panels' caption strips sit at each half's foot)
        y = (hh - int(hh * 0.14)) if cy_row < 1 else (h - int(hh * 0.14))
        meme_text(draw, (cx, y), txt, 22, fill=WHITE, stroke_fill=BLACK,
                  stroke_width=4, anchor="mm", max_width=int(hw * 0.92))
    im.save(OUT / "s21-anakin-padme.jpg", quality=92)
    print("OK s21-anakin-padme.jpg", im.size)


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


# s12 — Trade Offer (REPLACES Surprised Pikachu — GATE-B fix, audit
#   2026-09-07: pikachu collides with Lecture 2; shocked-affect also didn't
#   map cleanly onto a 7/7-vs-3/7 statistics contrast). "I receive / you
#   receive" format is a sharp fit: synthetic panel offers 7/7 approval, but
#   what you actually get for a go/no-go decision is the 3/7 real verdict —
#   the only one that counts.
def s12_trade_offer():
    im = Image.open(TPL / "trade-offer.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # Cover the stock template's own baked-in English banner + "i receive" /
    # "you receive" captions with FULLY OPAQUE bands sized to their actual
    # extent (top ~19% of the frame), then draw fresh RU text on top — no
    # double-exposed English underneath.
    header_h = int(h * 0.285)
    draw.rectangle([(0, 0), (w, header_h)], fill=(24, 24, 26))
    draw.rectangle([(0, 0), (w, int(h * 0.075))], fill=(200, 40, 30))
    meme_text(draw, (w * 0.5, int(h * 0.038)), "⚠ ПРЕДЛОЖЕНИЕ ⚠", 24,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.94))
    meme_text(draw, (w * 0.26, int(h * 0.125)), "я получаю:", 19,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.42))
    meme_text(draw, (w * 0.76, int(h * 0.125)), "вы получаете:", 19,
              fill=WHITE, stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.42))
    meme_text(draw, (w * 0.26, int(h * 0.20)), "7 из 7:\nсинт-панель «да»", 16,
              fill=(240, 220, 100), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.44))
    meme_text(draw, (w * 0.76, int(h * 0.20)), "3 из 7:\nреальные люди «да»", 16,
              fill=(240, 220, 100), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.44))
    meme_text(draw, (w * 0.5, h * 0.965),
              "решение «продолжать/стоп» — только по правой карточке", 18,
              fill=WHITE, stroke_fill=BLACK, stroke_width=4, anchor="mm",
              max_width=int(w * 0.92))
    im.save(OUT / "s12-trade-offer.jpg", quality=92)
    print("OK s12-trade-offer.jpg", im.size)


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


# s33 — "Corporate Needs You To Find The Differences" / "They're The Same
#   Picture" (REPLACES Change My Mind — GATE-B fix, audit 2026-09-07:
#   Change-My-Mind is a debate-provocation format, but "Facebook amplified
#   all 5 reactions x5" is a settled factual finding, not an opinion up for
#   debate — format/content mismatch). This format dramatizes the actual
#   reveal directly: Facebook claimed "love/wow/sad" were just friendlier
#   engagement signals, separate from "angry" — but internally they were ALL
#   weighted identically x5. "Spot the difference" -> "there is no
#   difference, they're weighted the same."
def s33_same_picture():
    im = Image.open(TPL / "they-are-same-picture.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # top half (0..~0.585h) is the "spot the difference" photo; template's
    # own caption band sits at y~0.42-0.505h — cover fully with opaque black
    # and redraw a single-language RU line, sized to actually fit ONE line.
    band_top, band_bot = int(h * 0.415), int(h * 0.585)
    draw.rectangle([(0, band_top), (w, band_bot)], fill=(0, 0, 0))
    meme_text(draw, (w * 0.5, (band_top + band_bot) // 2),
              "«найдите разницу: любовь/восторг/грусть и гнев»", 24,
              fill=(255, 235, 59), stroke_fill=None, stroke_width=0,
              anchor="mm", max_width=int(w * 0.92))
    # bottom half's own caption band sits at the very bottom ~0.925-1.0h
    bottom_top = int(h * 0.925)
    draw.rectangle([(0, bottom_top), (w, h)], fill=(0, 0, 0))
    meme_text(draw, (w * 0.5, (bottom_top + h) // 2),
              "«все 5 весят ×5 — разницы нет»", 26, fill=(255, 235, 59),
              stroke_fill=None, stroke_width=0, anchor="mm",
              max_width=int(w * 0.9))
    im.save(OUT / "s33-same-picture.jpg", quality=92)
    print("OK s33-same-picture.jpg", im.size)


# s39 — Gru's Plan (REPLACES Hide the Pain Harold — GATE-B fix, audit
#   2026-09-07: Harold's meaning is "smiling to hide personal suffering,"
#   which needs an extra inferential step for a monitoring-gap claim; Gru's
#   Plan 4-panel escalation — 3 confident panels then a realization twist —
#   is a direct structural match for "dashboards stayed green (panels 1-3),
#   then: trust had already been dropping for weeks (panel 4 twist)."
def s39_grus_plan():
    """Blank card sits on the RIGHT ~55-95% of each quadrant (not centred) —
    text must land there, not over Gru's face on the left ~0-55%."""
    im = Image.open(TPL / "grus-plan.jpg").convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    hw, hh = w // 2, h // 2
    card_cx_frac = 0.755   # centre of the blank card within each half-width
    panels = [
        (0, 0, "дашборд\nзелёный"),
        (hw, 0, "дашборд\nвсё ещё\nзелёный"),
        (0, hh, "дашборд\nзелёный\nуже месяц"),
        (hw, hh, "доверие падает\nнедели — дашборд\nне заметил"),
    ]
    for ox, oy, txt in panels:
        cx = ox + hw * card_cx_frac
        cy = oy + hh * 0.5
        meme_text(draw, (cx, cy), txt, 20, fill=(20, 20, 20),
                  stroke_fill=None, stroke_width=0, anchor="mm",
                  max_width=int(hw * 0.34))
    im.save(OUT / "s39-grus-plan.jpg", quality=92)
    print("OK s39-grus-plan.jpg", im.size)


# s47 — Drake reused? NO — use One-Does-Not-Simply already at s02. Use
#   Woman-Yelling? at s28. s47 needs its own: use Surprised-Pikachu? at s12.
#   -> use Sad-Pablo? at s44. Distinct template needed. Use Change-My-Mind? s33.
#   All big templates assigned. Reuse Drake is forbidden (dup). s47's payoff is
#   best served by a data chart (gen_charts funnel) — SKIP meme, chart instead.
#   (documented: s47 uses funnel chart, not a meme, to avoid template dup.)


if __name__ == "__main__":
    # section dividers + cover + hook
    s01_spiderman_pointing()
    s02_one_does_not_simply()
    s07_distracted_boyfriend()
    s14_drake_double_diamond()
    s21_anakin_padme()
    s28_woman_yelling_cat()
    s36_disaster_girl()
    s44_sad_pablo()
    # content slides
    s16_bernie()
    s12_trade_offer()
    s18_pigeon()
    s19_clown()
    s26_balloon()
    s33_same_picture()
    s39_grus_plan()
