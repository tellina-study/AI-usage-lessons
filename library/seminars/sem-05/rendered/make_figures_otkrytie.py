#!/usr/bin/env python3
"""Схемы открытия (s01–s06) и сборки оси (s46–s50) — рисуются программно (PIL).

Почему отдельный файл. Схемы s01/s03/s06 были нарисованы кодом, который в общую
ветку не попал: при вливании раздела уехали только готовые PNG, а генератор
остался в чужом worktree. Пересобрать их было нечем. Здесь он восстановлен —
s01 и s06 воспроизводятся байт-в-байт по замыслу, s03 не воспроизводится, потому
что слайд снят (повтор Семинара 4). Чужие `make_figures*.py` не тронуты.

Масштаб подписей тот же, что у make_figures.py: картинка шириной 12,2″ на канве
13,333″, полотно 2400 px → 1 px ≈ 0,366 pt. Кегль 38 px читается как 14 pt,
30 px — как 11 pt. Ниже 30 px не опускаться: на проекторе не читается.

  hero-barier.png     s01  правило, которое не удержало, и пять сегментов барьера
  karta-stupeney.png  s06  карта занятия: три ступени сегодня, две на следующем
  pravilo-poryadka.png    s05  три вопроса, по которым раскладывается любое усиление
  itog-chto-razlozheno.png     s49  что разложено по артефакту, а что не разложено ничем
  itog-tri-korziny.png         s50  три корзины переноса на свой репозиторий
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); GHOST = (0x4C, 0x5C, 0x93); DIMTX = (0x9F, 0xAE, 0xC4)
GH = (0xB6, 0xC2, 0xD2); GOLDTX = (0x8A, 0x63, 0x05); PALE = (0xE6, 0xEE, 0xF4)

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)


def f(sz, b=False, m=False):
    return ImageFont.truetype(FM if m else (FB if b else F), sz)


def label(d, x, y, s, sz=21, col=INK, b=False, m=False):
    d.text((x, y), s, font=f(sz, b, m), fill=col)


def clabel(d, cx, y, s, sz=21, col=INK, b=False, m=False):
    fo = f(sz, b, m)
    d.text((cx - d.textlength(s, font=fo) / 2, y), s, font=fo, fill=col)


def center(d, y, s, sz=21, col=INK, b=False, wd=2400):
    clabel(d, wd / 2, y, s, sz, col, b)


def fit(d, s, sz, maxw, b=False, m=False, floor=30):
    while sz > floor and d.textlength(s, font=f(sz, b, m)) > maxw:
        sz -= 2
    return sz


def wrap(d, s, sz, maxw, b=False, m=False):
    lines, cur = [], ""
    for wd_ in s.split():
        cand = (cur + " " + wd_).strip()
        if d.textlength(cand, font=f(sz, b, m)) <= maxw or not cur:
            cur = cand
        else:
            lines.append(cur); cur = wd_
    if cur:
        lines.append(cur)
    return lines


def wrapped(d, cx, y, s, sz, maxw, col=INK, b=False, lh=None):
    """Центрированный абзац с переносом. Возвращает нижнюю границу."""
    lh = lh or sz + 10
    for i, ln in enumerate(wrap(d, s, sz, maxw, b)):
        clabel(d, cx, y + i * lh, ln, sz, col, b)
        y += 0
        last = i
    return y + (last + 1) * lh


def box(d, x, y, w, h, txt, fc, tc=W, sz=20, b=True, m=False):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fc)
    fo = f(sz, b, m); lines = txt.split("\n")
    th = len(lines) * (sz + 6) - 6; cy = y + (h - th) // 2
    for i, ln in enumerate(lines):
        d.text((x + (w - d.textlength(ln, font=fo)) // 2, cy + i * (sz + 6)), ln, font=fo, fill=tc)


def panel(d, x, y, w, h, fill=SURF, line=LIGHT, r=14, width=3):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=line, width=width)


def dashbox(d, x, y, w, h, col, dash=18, gap=12, width=3, r=10):
    """Прямоугольник пунктиром — «здесь чего-то нет, и мы об этом говорим вслух»."""
    def seg(x1, y1, x2, y2):
        L = math.hypot(x2 - x1, y2 - y1)
        if L == 0:
            return
        ux, uy, t_ = (x2 - x1) / L, (y2 - y1) / L, 0.0
        while t_ < L:
            e = min(t_ + dash, L)
            d.line([x1 + ux * t_, y1 + uy * t_, x1 + ux * e, y1 + uy * e], fill=col, width=width)
            t_ = e + gap
    seg(x + r, y, x + w - r, y); seg(x + r, y + h, x + w - r, y + h)
    seg(x, y + r, x, y + h - r); seg(x + w, y + r, x + w, y + h - r)


def arrow(d, x1, y1, x2, y2, col=MID, wd=4, head=14, text=None, sz=17, above=True):
    d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4)),
               (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))], fill=col)
    if text:
        fo = f(sz, True); tw = d.textlength(text, font=fo)
        ty = (min(y1, y2) - sz - 9) if above else (max(y1, y2) + 8)
        d.text(((x1 + x2 - tw) // 2, ty), text, font=fo, fill=col)


def lock(d, cx, cy, s, col):
    d.arc([cx - s * 0.55, cy - s * 1.05, cx + s * 0.55, cy + s * 0.15], 180, 360,
          fill=col, width=max(3, s // 6))
    d.rounded_rectangle([cx - s * 0.8, cy - s * 0.1, cx + s * 0.8, cy + s * 0.95],
                        radius=s // 4, fill=col)


def save(im, name):
    im.save(OUT / name)


# ── s01 · обложка: просьба и пять способов сделать из неё барьер ─────────────
im = Image.new("RGB", (2400, 612), DEEP); d = ImageDraw.Draw(im)
d.line([50, 556, 2350, 556], fill=LIGHT, width=5)

d.rounded_rectangle([70, 352, 360, 552], radius=12, fill=W)
clabel(d, 215, 384, "правило", 34, INK, b=True)
for i, s in enumerate(("записано", "прочитано")):
    clabel(d, 215, 438 + i * 32, s, 21, MUTE)
clabel(d, 215, 508, "нарушено", 24, RED, b=True)

x = 560
for name, role in (("хук", "исполняемый барьер"), ("скилл", "загрузка по требованию"),
                   ("MCP", "доступ наружу")):
    d.rounded_rectangle([x, 236, x + 300, 556], radius=14, fill=GOLD)
    lock(d, x + 150, 306, 32, DEEP)
    clabel(d, x + 150, 398, name, 32, DEEP, b=True)
    ly = 452
    for ln in wrap(d, role, 19, 268):
        clabel(d, x + 150, ly, ln, 19, (0x5A, 0x44, 0x08)); ly += 28
    x += 340
for name in ("субагент", "процесс"):
    dashbox(d, x, 336, 300, 220, GHOST)
    clabel(d, x + 150, 430, name, 28, DIMTX, b=True)
    x += 340

arrow(d, 390, 452, 536, 452, col=LIGHT, head=20, wd=6)
d.line([560, 184, 1500, 184], fill=GOLD, width=4)
clabel(d, 1030, 130, "сегодня — три", 26, GOLD, b=True)
d.line([1580, 184, 2340, 184], fill=GHOST, width=4)
clabel(d, 1960, 130, "следующее занятие — две", 26, DIMTX)
save(im, "hero-barier.png")


# ── s06 · карта занятия: три ступени сегодня, две на следующем ───────────────
im = Image.new("RGB", (2400, 600), W); d = ImageDraw.Draw(im)
x = 50
# расшифровка сокращения даётся на ПЕРВОМ видимом употреблении в деке, а не
# во фронтматтере: до этого она жила в таблице s05, которой больше нет
for num, name, gloss, role, art in (
        ("3", "хук", "", "исполняемый барьер", ".claude/settings.json"),
        ("4", "скилл", "", "загрузка по требованию", ".claude/skills/deploy/SKILL.md"),
        ("5", "MCP", "Model Context Protocol", "доступ наружу", ".mcp.json")):
    d.rounded_rectangle([x, 150, x + 420, 410], radius=14, fill=MID)
    d.rounded_rectangle([x + 16, 166, x + 76, 226], radius=10, fill=GOLD)
    clabel(d, x + 46, 180, num, 26, DEEP, b=True)
    clabel(d, x + 250, 182, name, 30, W, b=True)
    if gloss:
        clabel(d, x + 210, 224, gloss, 19, (0xA8, 0xBE, 0xD4))
    clabel(d, x + 210, 252, role, 20, (0xCD, 0xDC, 0xE8))
    d.rounded_rectangle([x + 20, 300, x + 400, 380], radius=10, fill=(0x18, 0x20, 0x3A))
    clabel(d, x + 210, 330, art, fit(d, art, 17, 360, m=True), (0xE8, 0xEF, 0xF7), m=True)
    x += 470
for num, name in (("6", "субагент"), ("7", "процесс")):
    dashbox(d, x, 150, 420, 260, GH)
    clabel(d, x + 210, 244, num + " · " + name, 28, (0x8B, 0x9A, 0xAD), b=True)
    x += 470
d.line([50, 108, 1410, 108], fill=GOLD, width=4)
clabel(d, 730, 62, "сегодня", 24, GOLDTX, b=True)
d.line([1460, 108, 2350, 108], fill=GH, width=4)
clabel(d, 1905, 62, "следующее занятие", 24, (0x8B, 0x9A, 0xAD))

panel(d, 50, 466, 710, 104)
clabel(d, 405, 490, "на входе в занятие", 20, MUTE)
clabel(d, 405, 522, ".claude/ нет вовсе", 21, INK, b=True, m=True)
arrow(d, 800, 518, 1600, 518, col=MID, head=18, wd=5)
panel(d, 1640, 466, 710, 104, line=GOLD)
clabel(d, 1995, 490, "на выходе", 20, MUTE)
clabel(d, 1995, 522, ".claude/ и .mcp.json", 21, INK, b=True, m=True)
save(im, "karta-stupeney.png")


# ── s05 · три вопроса, по которым раскладывается любое усиление ──────────────
im = Image.new("RGB", (2400, 780), W); d = ImageDraw.Draw(im)

# вход
panel(d, 40, 300, 420, 160, fill=PALE, line=LIGHT)
clabel(d, 250, 332, "любое усиление", 30, INK, b=True)
clabel(d, 250, 382, "и то, которого", 22, MUTE)
clabel(d, 250, 412, "в пяти карточках нет", 22, MUTE)

# воронка 1
panel(d, 540, 240, 560, 280, line=LIGHT)
d.rounded_rectangle([540, 240, 1100, 306], radius=14, fill=LIGHT)
clabel(d, 820, 258, "1 · цена завести", 30, W, b=True)
y = 336
for ln in wrap(d, "Она одинакова в любом проекте?", 30, 500):
    clabel(d, 820, y, ln, 30, INK, b=True); y += 40
clabel(d, 820, 452, "если да — кандидат в день 0", 22, MUTE)

# воронка 2 (верх) и воронка 3 (низ)
panel(d, 1240, 60, 560, 250, line=TEAL)
d.rounded_rectangle([1240, 60, 1800, 126], radius=14, fill=TEAL)
clabel(d, 1520, 78, "2 · цена не завести", 30, W, b=True)
y = 156
for ln in wrap(d, "Наступает тихо, а видна поздно?", 30, 500):
    clabel(d, 1520, y, ln, 30, INK, b=True); y += 40
clabel(d, 1520, 252, "если да — ждать нечего", 22, MUTE)

panel(d, 1240, 450, 560, 250, line=MID)
d.rounded_rectangle([1240, 450, 1800, 516], radius=14, fill=MID)
clabel(d, 1520, 468, "3 · сигнал", 30, W, b=True)
y = 546
for ln in wrap(d, "Он уже прозвучал здесь, в этом репозитории?", 30, 500):
    clabel(d, 1520, y, ln, 30, INK, b=True); y += 40

# исходы
box(d, 1880, 110, 470, 150, "ДЕНЬ 0\nзавожу независимо\nот проекта", GOLD, DEEP, 26)
box(d, 1880, 452, 470, 110, "ЗАВОЖУ СЕЙЧАС", MID, W, 28)
panel(d, 1880, 590, 470, 110, fill=SURF, line=MUTE)
clabel(d, 2115, 612, "ЖДУ", 28, INK, b=True)
clabel(d, 2115, 652, "и это решение, не забывчивость",
       fit(d, "и это решение, не забывчивость", 20, 440), MUTE)

# связи
arrow(d, 460, 380, 534, 380, col=LIGHT, wd=5, head=16)
arrow(d, 1100, 330, 1236, 200, col=TEAL, wd=5, head=16, text="да")
arrow(d, 1800, 180, 1876, 180, col=TEAL, wd=5, head=16, text="да")
arrow(d, 1800, 610, 1876, 640, col=MUTE, wd=5, head=16, text="нет", above=False)

# дорожка хука — единственная карточка, разобранная вслух: она входит в поток
# на общем входе и доезжает до исхода, а не стоит подписью сбоку
d.rounded_rectangle([60, 520, 440, 596], radius=12, fill=GOLD)
clabel(d, 250, 542, "хук — разбираем вслух",
       fit(d, "хук — разбираем вслух", 27, 330, True), DEEP, b=True)
d.line([250, 500, 250, 520], fill=GOLD, width=9)
d.line([448, 558, 494, 558, 494, 420, 534, 420], fill=GOLD, width=9, joint="curve")
arrow(d, 510, 420, 534, 420, col=GOLD, wd=9, head=20)
d.line([1100, 430, 1180, 430, 1180, 560, 1210, 560], fill=GOLD, width=9, joint="curve")
arrow(d, 1190, 560, 1236, 560, col=GOLD, wd=9, head=20)
label(d, 1108, 378, "нет", 24, GOLDTX, b=True)
arrow(d, 1800, 560, 1876, 512, col=GOLD, wd=9, head=20, text="да")

center(d, 728, "Шестое усиление, которого сегодня нет в списке, раскладывается этими же тремя вопросами.",
       26, INK, b=True)
save(im, "pravilo-poryadka.png")


# ── s49 · что разложено по артефакту, а что не разложено ничем ───────────────
im = Image.new("RGB", (2400, 640), W); d = ImageDraw.Draw(im)
label(d, 60, 24, "ступень", 22, MUTE)
label(d, 420, 24, "что показало занятие", 22, MUTE)
label(d, 1580, 24, "чем это проверяется", 22, MUTE)
d.line([60, 62, 2340, 62], fill=GH, width=2)

rows = [("хук", "сигнал прозвучал ещё на прошлом занятии — заведён первым",
         "файл в ветке · коммит 9803643 · самотест"),
        ("скилл", "сигнал пришёл сегодня, на своей ступени — заведён следом",
         "описание-триггер, по которому идёт выбор"),
        ("MCP", "сигнал подключения пришёл сегодня, права его не ждали",
         "список прав, из которого вычеркнуто лишнее")]
y = 86
for name, what, how in rows:
    box(d, 60, y, 330, 88, name, MID, W, 30)
    panel(d, 410, y, 1130, 88, fill=SURF, line=LIGHT)
    clabel(d, 975, y + 22, what, fit(d, what, 26, 1080), INK)
    clabel(d, 975, y + 54, "", 22, MUTE)
    panel(d, 1560, y, 780, 88, fill=(0xE0, 0xF1, 0xF2), line=TEAL)
    clabel(d, 1950, y + 30, how, fit(d, how, 24, 740), INK)
    y += 108
for name in ("субагент", "процесс"):
    dashbox(d, 60, y, 330, 88, GH)
    clabel(d, 225, y + 30, name, 30, MUTE, b=True)
    dashbox(d, 410, y, 1130, 88, GH)
    clabel(d, 975, y + 30, "не разложено", 26, GH, b=True)
    dashbox(d, 1560, y, 780, 88, GH)
    clabel(d, 1950, y + 30, "нечем", 26, GH, b=True)
    y += 108
save(im, "itog-chto-razlozheno.png")


# ── s50 · три корзины переноса на свой репозиторий ───────────────────────────
im = Image.new("RGB", (2400, 600), W); d = ImageDraw.Draw(im)
x = 390
for name in ("хук", "скилл", "доступ наружу"):
    box(d, x, 30, 540, 86, name, MID, W, 30)
    x += 560
center(d, 140, "три сегодняшних — по своему рабочему репозиторию", 24, MUTE)

baskets = [(MID, "сигнал прозвучал", "завожу на этой неделе"),
           (LIGHT, "сигнала нет", "жду — и это решение, не забывчивость"),
           (TEAL, "не нужно вообще", "и я могу сказать, почему")]
x = 40
for col, head, sub in baskets:
    panel(d, x, 200, 740, 300, fill=SURF, line=col)
    d.rounded_rectangle([x, 200, x + 740, 282], radius=14, fill=col)
    clabel(d, x + 370, 224, head, fit(d, head, 34, 690, True), W, True)
    y = 330
    for ln in wrap(d, sub, 28, 660):
        clabel(d, x + 370, y, ln, 28, INK); y += 40
    dashbox(d, x + 60, y + 24, 620, 96, GH)
    clabel(d, x + 370, y + 58, "сюда — ваши", 24, GH, b=True)
    x += 780
center(d, 536, "Третья корзина — такой же законный исход, как первые две.", 28, INK, b=True)
save(im, "itog-tri-korziny.png")


print("схемы открытия и сборки оси:",
      *[p.name for p in sorted(OUT.glob("s0[167]-*.png")) + sorted(OUT.glob("s5[78]-*.png"))])
