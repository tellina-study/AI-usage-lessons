#!/usr/bin/env python3
"""Схемы блока «Скиллы» новой деки (n33–n58) — рисуются программно (PIL).

Свой генератор раздела: не импортирует make_figures*.py других сессий, чтобы
правка их палитры или вспомогательных функций не меняла эти четыре схемы.

Схемы намеренно НИЗКИЕ (высота 300–420 при ширине 2400): на всех четырёх
слайдах кроме схемы стоит таблица и моноширинная карточка, и высокая схема
съела бы их место. Каждая строка проверяется на ширину — что не влезло,
печатается в конце, а не обрезается молча.

Запуск: python3 make_figures_skilly.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
PALE = (0xE6, 0xEC, 0xF3); ROSE = (0xF7, 0xE6, 0xE4); W = (255, 255, 255)

OUT = Path(__file__).parent / "figures"; OUT.mkdir(exist_ok=True)
CW = 2400
WARN = []


def f(sz, b=False, m=False):
    return ImageFont.truetype(FM if m else (FB if b else F), sz)


def head(d, txt, sz=23):
    d.text((40, 16), txt, font=f(sz, True), fill=DEEP)


def cline(d, y, txt, sz=20, col=INK, b=False):
    fo = f(sz, b); tw = d.textlength(txt, font=fo)
    if tw > CW - 60:
        WARN.append(f"шире канвы: {txt[:56]!r}")
    d.text(((CW - tw) // 2, y), txt, font=fo, fill=col)


def plate(d, x, y, w, h, lines, fc, tc=INK, sz=21, b=False, m=False, pad=18):
    """Плашка с текстом по левому краю, вертикально по центру."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fc)
    fo = f(sz, b, m); step = sz + 9
    cy = y + (h - (len(lines) * step - 9)) // 2
    for i, ln in enumerate(lines):
        if d.textlength(ln, font=fo) > w - 2 * pad:
            WARN.append(f"шире плашки: {ln[:56]!r}")
        d.text((x + pad, cy + i * step), ln, font=fo, fill=tc)


def cplate(d, x, y, w, h, lines, fc, tc=W, sz=21, b=True, m=False):
    """Плашка с текстом по центру."""
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fc)
    fo = f(sz, b, m); step = sz + 9
    cy = y + (h - (len(lines) * step - 9)) // 2
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=fo)
        if tw > w - 16:
            WARN.append(f"шире плашки: {ln[:56]!r}")
        d.text((x + (w - tw) // 2, cy + i * step), ln, font=fo, fill=tc)


def bar(d, x, y, w, h, frac, fc, bg=PALE):
    d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=bg)
    if frac > 0:
        d.rounded_rectangle([x, y, x + max(int(w * frac), 12), y + h], radius=6, fill=fc)


# ── n40. Двойная оплата: скилл вынесли, копию оставили ───────────────────────
im = Image.new("RGB", (CW, 360), W); d = ImageDraw.Draw(im)
head(d, "Одна процедура, два места — и платят за неё дважды с 17 мая 2026")
plate(d, 40, 70, 1090, 118,
      ["скилл  .claude/skills/pre-user-gate/SKILL.md   —  165 строк",
       "грузится, когда его выбрали по описанию"],
      SURF, sz=22, m=False)
plate(d, 1270, 70, 1090, 118,
      ["копия  CLAUDE.md, строки 252–279            —   28 строк",
       "грузится при старте КАЖДОЙ сессии, без исключений"],
      ROSE, sz=22)
cplate(d, 1140, 106, 120, 46, ["то же"], MUTE, sz=18)
# полоса времени
d.text((40, 218), "17.05.2026", font=f(19, True), fill=MUTE)
d.text((2200, 218), "сегодня", font=f(19, True), fill=MUTE)
bar(d, 40, 248, 2320, 34, 1.0, GOLD)
cline(d, 252, "четыре с половиной месяца — оба файла в контексте одновременно", 21, DEEP, True)
cline(d, 308, "Вынос сделан правильно. Не сделана зачистка — и стоит это дороже, чем не выносить вовсе.",
      21, RED, True)
im.save(OUT / "skilly-dvoynaya-oplata.png")

# ── n41. Цена отбора ────────────────────────────────────────────────────────
im = Image.new("RGB", (CW, 420), W); d = ImageDraw.Draw(im)
head(d, "Прирост дал отобранный скилл — и вот насколько отобранное отличается от среднего")
d.text((40, 74), "успешных прохождений: те же 87 задач, те же 18 связок модели со средой",
       font=f(21, True), fill=INK)
for i, (lbl, val, frac, col) in enumerate(
        [("без скиллов", "33,9%", 0.339, MID), ("с курированными", "50,5%", 0.505, TEAL)]):
    y = 112 + i * 62
    d.text((40, y + 4), lbl, font=f(20), fill=MUTE)
    bar(d, 330, y, 1500, 40, frac, col)
    d.text((1850, y + 4), val, font=f(22, True), fill=col)
d.text((2000, 143), "+16,6 п.п.", font=f(24, True), fill=GOLD)
d.text((40, 250), "качество по одной и той же 12-балльной рубрике", font=f(21, True), fill=INK)
for i, (lbl, val, frac, col) in enumerate(
        [("каталоги, корпус 47 150+", "6,2 / 12", 6.2 / 12, MUTE),
         ("отобранные для замера", "10,1 / 12", 10.1 / 12, LIGHT)]):
    y = 288 + i * 48
    d.text((40, y + 2), lbl, font=f(20), fill=MUTE)
    bar(d, 620, y, 1210, 30, frac, col)
    d.text((1850, y + 2), val, font=f(21, True), fill=col)
cline(d, 388, "Разница между 6,2 и 10,1 по одной рубрике и есть цена отбора.", 21, DEEP, True)
im.save(OUT / "skilly-otbor.png")

# ── n52. Налог на перечень ──────────────────────────────────────────────────
im = Image.new("RGB", (CW, 330), W); d = ImageDraw.Draw(im)
head(d, "Перечень скиллов этого репозитория: что в нём лежит и за что платится каждый ход")
names = ["build-deck", "catalog-docs", "compile-wiki", "diagram-refresh", "extract-links",
         "impact-check", "issue-from-change", "pre-user-gate", "publish-article",
         "query-kb", "reflect", "sync-library", "update-lecture"]
x0, pw, gap = 40, 168, 12
for i, nm in enumerate(names):
    live = nm == "pre-user-gate"
    x = x0 + i * (pw + gap)
    cplate(d, x, 74, pw, 96,
           [nm, "описание" if live else "имя вместо", "написано" if live else "описания"],
           GOLD if live else PALE, tc=DEEP if live else MUTE, sz=15, b=live)
cplate(d, 40, 196, 1140, 58, ["12 из 13 сработать по смыслу не могут"], ROSE, tc=RED, sz=22)
cplate(d, 1220, 196, 1140, 58,
       ["~100 токенов × 13 = ~1 300 в каждом ходу, из них ~1 200 впустую"], SURF, tc=DEEP, sz=22)
cline(d, 284, "Платится за каждый скилл независимо от того, вызывался ли он хоть раз — включая эту сессию.",
      21, INK)
im.save(OUT / "skilly-nalog.png")

# ── n57. Вредит и релевантный ───────────────────────────────────────────────
im = Image.new("RGB", (CW, 380), W); d = ImageDraw.Draw(im)
head(d, "307 подтверждённых случаев вреда: из чего они складываются и кто их дал")
cplate(d, 40, 74, 1120, 64, ["125 функциональных — работа сделана неверно"], MID, sz=22)
cplate(d, 1240, 74, 1120, 64, ["182 стоимостных — работа сделана дороже"], LIGHT, sz=22)
d.text((40, 164), "из 125 функциональных:", font=f(21, True), fill=INK)
bar(d, 400, 160, 1430, 40, 0.688, RED)
d.text((1850, 164), "86 = 68,8%", font=f(22, True), fill=RED)
plate(d, 40, 222, 2320, 56,
      ["86 из 125 дали скиллы, которые выглядели ПОДХОДЯЩИМИ задаче — не лишние и не подсунутые"],
      ROSE, tc=RED, sz=22, b=True)
plate(d, 40, 296, 2320, 56,
      ["и отдельно: скиллы с исполняемым кодом внутри уязвимы в 2,12 раза чаще — тот же корпус 31 132, различие только в наличии скрипта"],
      SURF, tc=DEEP, sz=21)
im.save(OUT / "skilly-relevantnyy-vred.png")

print("схемы блока «Скиллы»:", *[p.name for p in sorted(OUT.glob("skilly-*.png"))])
if WARN:
    print("ПРЕДУПРЕЖДЕНИЯ ПО ШИРИНЕ:", len(WARN))
    for w in dict.fromkeys(WARN):
        print("  -", w)
else:
    print("по ширине всё влезло")
