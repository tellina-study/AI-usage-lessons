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


ALL = [
    make_gru, make_change_my_mind, make_pigeon, make_pooh, make_pooh_memory,
    make_roll_safe, make_doge, make_batman, make_this_is_fine,
    make_always_has_been,
]

if __name__ == "__main__":
    for fn in ALL:
        p = fn()
        print("wrote", p.name, Image.open(p).size)
