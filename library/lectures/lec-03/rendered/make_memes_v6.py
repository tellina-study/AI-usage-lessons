#!/usr/bin/env python3
"""v6 meme pass (issue #185) — «мемы по всему тексту дека», а не только на 4
явно запрошенных слайдах. Реальные узнаваемые imgflip-шаблоны (blank из
imgflip API, id-подтверждены) + русские подписи через PIL. Английские baked-in
подписи (там где есть) перекрыты белым и переписаны по-русски. Атрибуция —
только assets/web/attribution.md; на слайдах источников нет.

Замена (owner: «мем с мозгом был уже»): s05 Expanding Brain → Gru's Plan
(эскалация архитектуры «на всякий случай» с абсурдной развязкой в 4-й панели).

Русские подписи БЕЗ превосходных форм и транслита. Composite'ы вжигаются
через add_image в build_v3.py.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WEB = Path(__file__).parent / "assets/web"
SRC = WEB / "memes-src"
FONT = "/home/harness/.local/lo-sysroot/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/home/harness/.local/lo-sysroot/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

WHITE = (255, 255, 255)
BLACK = (18, 18, 18)


def font(sz, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_R, sz)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, text, box, fnt, fill=BLACK, align="left", valign="center",
               line_h=1.14):
    x, y, w, h = box
    lines = wrap(draw, text, fnt, w)
    asc, desc = fnt.getmetrics()
    lh = int((asc + desc) * line_h)
    total = lh * len(lines)
    if valign == "center":
        cy = y + (h - total) // 2
    elif valign == "bottom":
        cy = y + h - total
    else:
        cy = y
    for ln in lines:
        tw = draw.textlength(ln, font=fnt)
        if align == "center":
            cx = x + (w - tw) // 2
        elif align == "right":
            cx = x + w - tw
        else:
            cx = x
        draw.text((cx, cy), ln, font=fnt, fill=fill)
        cy += lh


def outline_block(draw, text, box, fnt, fill=WHITE, outline=BLACK, ow=3,
                  align="center", valign="top", line_h=1.12):
    """Classic white-with-black-outline caption (top/bottom меме-стиль)."""
    x, y, w, h = box
    lines = wrap(draw, text, fnt, w)
    asc, desc = fnt.getmetrics()
    lh = int((asc + desc) * line_h)
    total = lh * len(lines)
    if valign == "center":
        cy = y + (h - total) // 2
    elif valign == "bottom":
        cy = y + h - total
    else:
        cy = y
    for ln in lines:
        tw = draw.textlength(ln, font=fnt)
        cx = x + (w - tw) // 2 if align == "center" else x
        for dx in range(-ow, ow + 1):
            for dy in range(-ow, ow + 1):
                if dx or dy:
                    draw.text((cx + dx, cy + dy), ln, font=fnt, fill=outline)
        draw.text((cx, cy), ln, font=fnt, fill=fill)
        cy += lh


def fit_font(draw, text, max_w, start, bold=True, min_sz=16):
    """Shrink font until the longest word fits max_w (avoid mid-word overflow)."""
    sz = start
    while sz > min_sz:
        f = font(sz, bold)
        if all(draw.textlength(w, font=f) <= max_w for w in text.split()):
            return f
        sz -= 2
    return font(min_sz, bold)


# ------------------------------------------------------------------
# s05 — GRU'S PLAN (4 панели) — эскалация архитектуры «на всякий случай»
#       с абсурдной развязкой в 4-й панели. Замена Expanding Brain.
#       Каждая панель ~350x224; синяя доска справа ≈ x[185..345].
# ------------------------------------------------------------------
def make_gru():
    img = Image.open(SRC / "gru-plan.jpg").convert("RGB")
    W, H = img.size            # 700x449
    d = ImageDraw.Draw(img)
    pw, ph = W // 2, H // 2    # 350 x 224 per panel
    caps = [
        "Взял один вызов\nс хорошим промптом",
        "Добавил RAG\nи петли —\nна всякий случай",
        "Обвязал\nмульти-агентной\nоркестрацией",
        "Задача была\nна три строки\nобычного кода",   # punchline (4-я панель)
    ]
    # доска справа в каждой панели: локальные коорд. внутри панели
    bx0, bx1 = int(pw * 0.53), int(pw * 0.99)
    by0, by1 = int(ph * 0.10), int(ph * 0.92)
    for i, cap in enumerate(caps):
        r, c = divmod(i, 2)
        ox, oy = c * pw, r * ph
        box = (ox + bx0, oy + by0, bx1 - bx0, by1 - by0)
        # перекрыть доску белым для чистого фона под текст
        d.rectangle([ox + bx0 - 2, oy + by0 - 2, ox + bx1 + 2, oy + by1 + 2],
                    fill=(214, 232, 234))
        f = fit_font(d, cap.replace("\n", " "), box[2] - 6, 19, True, 12)
        draw_block(d, cap.replace("\n", " "), (box[0] + 4, box[1], box[2] - 8, box[3]),
                   f, fill=BLACK, align="center", valign="center", line_h=1.12)
    out = WEB / "s05-gru-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s05a — CHANGE MY MIND — «роль в промпте не делает ответ точнее».
#        Табличка внизу x≈[128..372] y≈[300..345]; перекрыть и переписать.
# ------------------------------------------------------------------
def make_change_my_mind():
    img = Image.open(SRC / "change-my-mind.jpg").convert("RGB")
    W, H = img.size            # 482x361
    d = ImageDraw.Draw(img)
    # белый sign уже белый; перекрыть baked-in "CHANGE MY MIND" целиком
    # (табличка чуть под наклоном → берём с запасом по правому краю)
    sx0, sy0, sx1, sy1 = 100, 300, 425, 349
    d.rectangle([sx0, sy0, sx1, sy1], fill=WHITE)
    txt = "«Роль эксперта не повышает точность»"
    f = fit_font(d, txt, sx1 - sx0 - 8, 20, True, 12)
    draw_block(d, txt, (sx0 + 4, sy0, sx1 - sx0 - 8, sy1 - sy0), f,
               fill=BLACK, align="center", valign="center", line_h=1.05)
    out = WEB / "s05a-changemymind-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s05c — IS THIS A PIGEON — протокольную роль принимают за гарантию границы.
#        Метка на бабочке (сверху-справа) + нижний баннер-вопрос.
# ------------------------------------------------------------------
def make_pigeon():
    img = Image.open(SRC / "is-this-a-pigeon.jpg").convert("RGB")
    W, H = img.size            # 1587x1425
    d = ImageDraw.Draw(img)
    # метка «протокольная роль system» у бабочки (верх-право)
    outline_block(d, "протокольная роль system",
                  (int(W * 0.60), int(H * 0.02), int(W * 0.38), int(H * 0.12)),
                  font(58), align="center", valign="top", ow=4)
    # нижний баннер-вопрос
    outline_block(d, "«это ведь надёжная граница?»",
                  (int(W * 0.05), int(H * 0.86), int(W * 0.90), int(H * 0.12)),
                  font(70), align="center", valign="center", ow=5)
    out = WEB / "s05c-pigeon-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s11 — TUXEDO POOH — RAG «сырой» vs RAG с опорой на источник (провенанс).
#        Правая половина x≈[350..800] белая; 2 строки-подписи.
# ------------------------------------------------------------------
def make_pooh():
    img = Image.open(SRC / "tuxedo-pooh.png").convert("RGB")
    W, H = img.size            # 800x582
    d = ImageDraw.Draw(img)
    cx0 = int(W * 0.44)
    cw = W - cx0 - 24
    # top row (обычный Пух) — «сложить всё в веса модели»
    draw_block(d, "«просто спросить модель — она же всё знает»",
               (cx0, int(H * 0.03), cw, int(H * 0.44)), font(34),
               fill=BLACK, align="left", valign="center", line_h=1.16)
    # bottom row (тукседо Пух) — «RAG с опорой на проверяемый источник»
    draw_block(d, "RAG: ответ с опорой на проверяемый источник",
               (cx0, int(H * 0.52), cw, int(H * 0.44)), font(34),
               fill=BLACK, align="left", valign="center", line_h=1.16)
    out = WEB / "s11-pooh-ru.png"
    img.save(out)
    return out


def make_pooh_memory():
    """s22c-вариант Tuxedo Pooh: плоский файл-лог vs граф-база знаний памяти."""
    img = Image.open(SRC / "tuxedo-pooh.png").convert("RGB")
    W, H = img.size
    d = ImageDraw.Draw(img)
    cx0 = int(W * 0.44)
    cw = W - cx0 - 24
    draw_block(d, "«просто дописывать факты в один текстовый лог»",
               (cx0, int(H * 0.03), cw, int(H * 0.44)), font(32),
               fill=BLACK, align="left", valign="center", line_h=1.14)
    draw_block(d, "граф-база знаний — но только под требование масштаба",
               (cx0, int(H * 0.52), cw, int(H * 0.44)), font(32),
               fill=BLACK, align="left", valign="center", line_h=1.14)
    out = WEB / "s22c-pooh-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s12 — ROLL SAFE — «не нужен RAG, если корпус влезает в контекст».
#        Классический top/bottom outline-caption.
# ------------------------------------------------------------------
def make_roll_safe():
    img = Image.open(SRC / "roll-safe.jpg").convert("RGB")
    W, H = img.size            # 702x395
    d = ImageDraw.Draw(img)
    outline_block(d, "не нужен RAG",
                  (12, 8, W - 24, int(H * 0.22)), font(46),
                  align="center", valign="top", ow=3)
    outline_block(d, "если корпус влезает в контекст",
                  (12, int(H * 0.74), W - 24, int(H * 0.24)), font(40),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s12-rollsafe-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s15 — BUFF DOGE vs CHEEMS — PEFT (сильный выбор) vs полное дообучение.
#        Подписи под каждой собакой.
# ------------------------------------------------------------------
def make_doge():
    img = Image.open(SRC / "buff-doge-cheems.png").convert("RGB")
    W, H = img.size            # 937x720
    d = ImageDraw.Draw(img)
    # buff (лево) — PEFT / LoRA
    draw_block(d, "PEFT / LoRA:\nдёшево, модульно, ниже риск забывания",
               (20, int(H * 0.80), int(W * 0.48), int(H * 0.19)), font(30),
               fill=BLACK, align="center", valign="top", line_h=1.1)
    # cheems (право) — полное дообучение
    draw_block(d, "Полное дообучение\nвсех весов в 2026 —\nпочти никогда",
               (int(W * 0.55), int(H * 0.80), int(W * 0.43), int(H * 0.19)),
               font(30), fill=BLACK, align="center", valign="top", line_h=1.1)
    out = WEB / "s15-doge-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s19b — BATMAN SLAP — «агент — это просто чат подороже» → пощёчина.
#        Два облака сверху: лево (Робин) x≈[20..190], право (Бэтмен) x≈[250..390].
# ------------------------------------------------------------------
def make_batman():
    img = Image.open(SRC / "batman-slap.jpg").convert("RGB")
    W, H = img.size            # 400x387
    d = ImageDraw.Draw(img)
    # облако Робина (лево-верх)
    draw_block(d, "«агент — это просто чат подороже»",
               (18, 18, 165, 105), font(19), fill=BLACK, align="center",
               valign="center", line_h=1.06)
    # облако Бэтмена (право-верх)
    draw_block(d, "это другой порядок цены",
               (238, 34, 150, 90), font(19), fill=BLACK, align="center",
               valign="center", line_h=1.06)
    out = WEB / "s19b-batman-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s22e — THIS IS FINE — «файл-инструкция всё чинит» / комната в огне.
#        Перекрыть baked-in "THIS IS FINE." в облаке правой панели.
# ------------------------------------------------------------------
def make_this_is_fine():
    img = Image.open(SRC / "this-is-fine.jpg").convert("RGB")
    W, H = img.size            # 580x282
    d = ImageDraw.Draw(img)
    # облако в правой панели: x≈[360..565] y≈[14..70] — перекрыть белым
    bx0, by0, bx1, by1 = 360, 12, 566, 74
    d.rectangle([bx0, by0, bx1, by1], fill=WHITE)
    txt = "«файл-инструкция всё починит»"
    f = fit_font(d, txt, bx1 - bx0 - 6, 18, True, 11)
    draw_block(d, txt, (bx0 + 3, by0, bx1 - bx0 - 6, by1 - by0), f,
               fill=BLACK, align="center", valign="center", line_h=1.02)
    out = WEB / "s22e-thisisfine-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s24 — ALWAYS HAS BEEN — «данные вне ZDR?» / «так было всегда».
#        Космонавт-1 (центр, смотрит на Землю) + космонавт-2 (право, с пистолетом).
# ------------------------------------------------------------------
def make_always_has_been():
    img = Image.open(SRC / "always-has-been.png").convert("RGB")
    W, H = img.size            # 960x540
    d = ImageDraw.Draw(img)
    # реплика первого космонавта (над ним, центр)
    outline_block(d, "данные вне ZDR?!",
                  (int(W * 0.34), int(H * 0.30), int(W * 0.30), int(H * 0.16)),
                  font(38), align="center", valign="top", ow=3)
    # реплика второго (над пистолетом, право-верх)
    outline_block(d, "так было всегда",
                  (int(W * 0.60), int(H * 0.03), int(W * 0.38), int(H * 0.16)),
                  font(38), align="center", valign="top", ow=3)
    out = WEB / "s24-alwayshasbeen-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s14 — STAR WARS YODA — учитель→ученик: большая дообученная модель
#       передаёт умение маленькой (дистилляция). Чистый шаблон без baked-in.
#       Верхняя полоса (тёмное небо) + нижняя (одежда) — outline-подписи.
# ------------------------------------------------------------------
def make_yoda():
    img = Image.open(SRC / "yoda.jpg").convert("RGB")
    W, H = img.size            # 620x713
    d = ImageDraw.Draw(img)
    outline_block(d, "учитель — большая дообученная модель",
                  (10, 6, W - 20, int(H * 0.16)), font(34),
                  align="center", valign="top", ow=3)
    outline_block(d, "передаёт умение маленькому ученику",
                  (10, int(H * 0.83), W - 20, int(H * 0.16)), font(34),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s14-yoda-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s27b — TWO GUYS ON A BUS — грустный (пере-усложнённый агент) vs довольный
#        (тонкий агент по умолчанию, смотрит на закат). Чистый шаблон.
#        Подпись у грустного (лево-низ) + у довольного (право-центр).
# ------------------------------------------------------------------
def make_two_guys_bus():
    img = Image.open(SRC / "two-guys-bus.jpg").convert("RGB")
    W, H = img.size            # 762x675
    d = ImageDraw.Draw(img)
    # грустный (лево) — усложнил на всякий случай
    outline_block(d, "усложнил на всякий случай",
                  (6, int(H * 0.60), int(W * 0.36), int(H * 0.30)),
                  font(26), align="center", valign="center", ow=3, line_h=1.06)
    # довольный (право) — начал с тонкого агента
    outline_block(d, "начал с тонкого агента",
                  (int(W * 0.60), int(H * 0.04), int(W * 0.38), int(H * 0.26)),
                  font(26), align="center", valign="center", ow=3, line_h=1.06)
    out = WEB / "s27b-bus-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s31 — WAITING SKELETON — «жду ваши вопросы». Чистый шаблон, лёгкий финал.
#        Верхняя полоса (небо/трава) — одна outline-подпись.
# ------------------------------------------------------------------
def make_skeleton():
    img = Image.open(SRC / "waiting-skeleton.jpg").convert("RGB")
    W, H = img.size            # 298x403
    d = ImageDraw.Draw(img)
    outline_block(d, "жду ваши вопросы",
                  (6, 4, W - 12, int(H * 0.20)), font(28),
                  align="center", valign="top", ow=3, line_h=1.04)
    out = WEB / "s31-skeleton-ru.png"
    img.save(out)
    return out


# ==================================================================
# WAVE 1 (issue #196) — 5 fresh templates for новые §1-слайды.
# Ни один не переиспользует ранее занятый шаблон дека.
# ==================================================================

# ------------------------------------------------------------------
# s-fmt — TWO BUTTONS (Daily Struggle, imgflip 87743020) — дилемма формата
#         ВЫХОДА: «заставить рассуждающий ответ в JSON» vs «дать свободно
#         рассуждать». Пот на лбу = reasoning tax. Подписи на белых кнопках.
#         Кнопки: левая ≈ x[135..270] y[95..250]; правая ≈ x[300..470] y[70..230].
# ------------------------------------------------------------------
def make_two_buttons():
    img = Image.open(SRC / "two-buttons.jpg").convert("RGB")
    W, H = img.size            # 600x908
    d = ImageDraw.Draw(img)
    # левая кнопка-панель — перекрыть белым для чистой подписи
    d.rectangle([70, 70, 300, 300], fill=WHITE)
    draw_block(d, "принудить\nответ в JSON",
               (78, 90, 214, 190), font(30), fill=BLACK,
               align="center", valign="center", line_h=1.06)
    # правая кнопка-панель
    d.rectangle([315, 55, 545, 300], fill=WHITE)
    draw_block(d, "дать свободно\nрассуждать",
               (322, 80, 216, 190), font(30), fill=BLACK,
               align="center", valign="center", line_h=1.06)
    out = WEB / "s-fmt-twobuttons-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-assistant — ONE DOES NOT SIMPLY (imgflip 61579) — «нельзя просто так
#        взять и прыгнуть сразу к агенту». Классический top/bottom outline.
# ------------------------------------------------------------------
def make_one_does_not():
    img = Image.open(SRC / "one-does-not-simply.jpg").convert("RGB")
    W, H = img.size            # 568x335
    d = ImageDraw.Draw(img)
    outline_block(d, "нельзя просто так взять",
                  (10, 6, W - 20, int(H * 0.20)), font(34),
                  align="center", valign="top", ow=3)
    outline_block(d, "и прыгнуть сразу к агенту",
                  (10, int(H * 0.78), W - 20, int(H * 0.20)), font(34),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s-task-assistant-simply-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-tone — FUTURAMA FRY / NOT SURE IF (imgflip 61520) — «не пойму:
#        текст написал человек или ИИ» — ненадёжность детекторов. Прищур Фрая.
#        Классический top/bottom outline.
# ------------------------------------------------------------------
def make_futurama_fry():
    img = Image.open(SRC / "futurama-fry.jpg").convert("RGB")
    W, H = img.size            # 552x414
    d = ImageDraw.Draw(img)
    outline_block(d, "не пойму: текст написал человек",
                  (10, 6, W - 20, int(H * 0.22)), font(32),
                  align="center", valign="top", ow=3)
    outline_block(d, "или детектор снова врёт",
                  (10, int(H * 0.76), W - 20, int(H * 0.22)), font(32),
                  align="center", valign="bottom", ow=3)
    out = WEB / "s-task-tone-fry-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-research — PANIK / KALM / PANIK (imgflip 226297822) — цикл проверки
#        цитаты: нашёл ссылку → она резолвится → URL сфабрикован. Левый белый
#        столбец (3 панели), «Panik/Kalm/Panik» уже вжжены справа. RU-подписи
#        в левые панели. Панели: y≈[10..295],[305..585],[600..870]; x≈[15..300].
# ------------------------------------------------------------------
def make_panik_kalm():
    img = Image.open(SRC / "panik-kalm-panik.png").convert("RGB")
    W, H = img.size            # 640x881
    d = ImageDraw.Draw(img)
    lx, lw = 18, 288
    panels = [
        ("агент дал\nотчёт со\nссылками", 14, 288),
        ("часть ссылок\nдаже резолвится", 306, 578),
        ("3–13% URL\nпросто\nсфабрикованы", 596, 866),
    ]
    for txt, y0, y1 in panels:
        f = fit_font(d, txt.replace("\n", " "), lw - 10, 30, True, 15)
        draw_block(d, txt.replace("\n", " "), (lx, y0, lw, y1 - y0), f,
                   fill=BLACK, align="center", valign="center", line_h=1.1)
    out = WEB / "s-task-research-panik-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-task-extract — TRADE OFFER (imgflip 309868304) — честный обмен: «ты даёшь
#        JSON-схему — я даю ~100% соответствия» (constrained decoding). Baked-in
#        английские «TRADE OFFER / i receive / you receive» перекрыты RU.
#        Баннер ≈ x[135..475] y[38..92]; «i receive:» ≈ x[55..205] y[145..180];
#        «you receive:» ≈ x[350..545] y[145..180].
# ------------------------------------------------------------------
def make_trade_offer():
    img = Image.open(SRC / "trade-offer.jpg").convert("RGB")
    W, H = img.size            # 607x794
    d = ImageDraw.Draw(img)
    # перекрыть красный баннер «TRADE OFFER» — оставить красный фон, RU-текст
    d.rectangle([118, 34, 490, 96], fill=(230, 57, 53))
    outline_block(d, "ЧЕСТНЫЙ ОБМЕН",
                  (120, 40, 368, 54), font(34), fill=WHITE, outline=BLACK,
                  ow=2, align="center", valign="center")
    # перекрыть «i receive:» и «you receive:» баннерные подписи (тёмный фон-плашка)
    d.rectangle([44, 138, 250, 350], fill=(28, 24, 48))
    d.rectangle([340, 138, 560, 350], fill=(28, 24, 48))
    draw_block(d, "ты даёшь:",
               (52, 144, 190, 34), font(24), fill=WHITE,
               align="left", valign="top")
    draw_block(d, "JSON-схему\nвыхода",
               (52, 186, 190, 150), font(26), fill=WHITE,
               align="left", valign="top", line_h=1.12)
    draw_block(d, "получаешь:",
               (348, 144, 205, 34), font(24), fill=WHITE,
               align="left", valign="top")
    draw_block(d, "~100%\nпо схеме",
               (348, 186, 205, 150), font(26), fill=WHITE,
               align="left", valign="top", line_h=1.12)
    out = WEB / "s-task-extract-trade-ru.png"
    img.save(out)
    return out


# ==================================================================
# WAVE 2 (issue #196) — 2 fresh templates для §2 RAG judgment-слайдов.
# Ни один не переиспользует ранее занятый шаблон дека. Только на 2 слайда,
# где мем несёт тезис суждения (s-rag-elastic, s-rag-chunk2); схемные слайды
# (hybrid, stack, chunk1, design) остаются чистыми диаграммами/таблицами.
# ==================================================================

# ------------------------------------------------------------------
# s-rag-elastic — WOMAN YELLING AT A CAT (imgflip 188390779) — суждение
#        «а нужна ли мне выделенная векторная БД». Левая панель (две женщины,
#        кричат «нам нужна векторная БД!») ≈ x[0..340]; правая (кот за столом,
#        «у тебя 3 млн чанков — хватит Postgres») ≈ x[340..680]. Классические
#        белые outline-подписи сверху каждой панели.
# ------------------------------------------------------------------
def make_woman_cat():
    img = Image.open(SRC / "woman-yelling-cat.jpg").convert("RGB")
    W, H = img.size            # 680x438
    d = ImageDraw.Draw(img)
    half = W // 2
    # левая панель — крик команды
    outline_block(d, "«срочно ставим векторную БД!»",
                  (6, 4, half - 12, int(H * 0.30)), font(26),
                  align="center", valign="top", ow=3, line_h=1.05)
    # правая панель — спокойный кот
    outline_block(d, "у тебя 3 млн чанков — хватит Postgres",
                  (half + 6, 4, half - 12, int(H * 0.30)), font(24),
                  align="center", valign="top", ow=3, line_h=1.05)
    out = WEB / "s-rag-elastic-cat-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-rag-chunk2 — DISASTER GIRL (imgflip 97984) — тихий провал: команда
#        внедрила «умный» semantic chunking (девочка улыбается), а таблицы в
#        документах тихо разъехались (дом горит на фоне). Классический
#        top/bottom outline-caption.
# ------------------------------------------------------------------
def make_disaster_girl():
    img = Image.open(SRC / "disaster-girl.jpg").convert("RGB")
    W, H = img.size            # 500x375
    d = ImageDraw.Draw(img)
    outline_block(d, "внедрили semantic chunking по хайпу",
                  (10, 6, W - 20, int(H * 0.24)), font(28),
                  align="center", valign="top", ow=3, line_h=1.04)
    outline_block(d, "таблицы тихо разъехались",
                  (10, int(H * 0.74), W - 20, int(H * 0.24)), font(30),
                  align="center", valign="bottom", ow=3, line_h=1.04)
    out = WEB / "s-rag-chunk2-disaster-ru.png"
    img.save(out)
    return out


# ==================================================================
# WAVE 3 (issue #196) — 2 fresh templates для §3/§4 judgment-слайдов.
# Ни один не переиспользует ранее занятый шаблон дека (23 уже занято).
# Только на 2 слайда, где мем несёт тезис суждения (s-ft-eval, s-agent-when);
# table/diagram-слайды (s-ft-cost, s22-паттерны, s-agent-frameworks) — чистые.
# ==================================================================

# ------------------------------------------------------------------
# s-ft-eval — LEFT EXIT 12 OFF RAMP (imgflip 124822590) — тезис «оценка
#        сложнее обучения»: машина резко сворачивает с прямого пути «строгая
#        оценка (held-out + A/B)» на съезд «красивое число на бенчмарке».
#        Верхняя панель — дорожный знак: прямо (левая стрелка) ≈ x[300..365],
#        съезд (правая стрелка) ≈ x[375..520]; обе на высоте y[110..185].
#        Нижняя панель (авто в заносе) — без подписи. Размер 804x767.
# ------------------------------------------------------------------
def make_left_exit():
    img = Image.open(SRC / "left-exit-12.jpg").convert("RGB")
    W, H = img.size            # 804x767
    d = ImageDraw.Draw(img)
    # прямой путь — над левой стрелкой
    outline_block(d, "строгая оценка: held-out + A/B",
                  (150, 96, 210, 70), font(21),
                  align="center", valign="center", ow=3, line_h=1.02)
    # съезд — над/справа от правой стрелки
    outline_block(d, "красивое число на бенчмарке",
                  (392, 96, 200, 70), font(21),
                  align="center", valign="center", ow=3, line_h=1.02)
    out = WEB / "s-ft-eval-leftexit-ru.png"
    img.save(out)
    return out


# ------------------------------------------------------------------
# s-agent-when — CLOWN APPLYING MAKEUP (imgflip 141136560) — 4 панели
#        эскалации: «задача чуть непредсказуема» → «возьму агента» → «возьму
#        мульти-агент» → «0,95²⁰ ≈ 36% надёжности». Лица справа (x[420..640]),
#        левая половина — белая, туда RU-подписи. Панели по вертикали:
#        y[10..190], [210..390], [410..590], [610..760]. Размер 750x798.
# ------------------------------------------------------------------
def make_clown_agents():
    img = Image.open(SRC / "clown-makeup.jpg").convert("RGB")
    W, H = img.size            # 750x798
    d = ImageDraw.Draw(img)
    caps = [
        "задача чуть непредсказуема",
        "возьму агента",
        "возьму мульти-агент",
        "0,95²⁰ ≈ 36% надёжности",
    ]
    ys = [10, 210, 410, 610]
    hs = [180, 180, 180, 150]
    for cap, y, h in zip(caps, ys, hs):
        draw_block(d, cap, (24, y, 380, h), font(30),
                   fill=BLACK, align="left", valign="center", line_h=1.06)
    out = WEB / "s-agent-when-clown-ru.png"
    img.save(out)
    return out


ALL = [
    make_gru, make_change_my_mind, make_pigeon, make_pooh, make_pooh_memory,
    make_roll_safe, make_doge, make_batman, make_this_is_fine,
    make_always_has_been,
    make_yoda, make_two_guys_bus, make_skeleton,
    # WAVE 1 (#196)
    make_two_buttons, make_one_does_not, make_futurama_fry, make_panik_kalm,
    make_trade_offer,
    # WAVE 2 (#196)
    make_woman_cat, make_disaster_girl,
    # WAVE 3 (#196)
    make_left_exit, make_clown_agents,
]

if __name__ == "__main__":
    for fn in ALL:
        p = fn()
        print("wrote", p.name, Image.open(p).size)
