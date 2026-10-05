#!/usr/bin/env python3
"""Схемы раздела «Субагент» Семинара 6 — n41, n51, n58.

Рисуются программно (PIL). Холст 1600 px = 12,23″ рабочей ширины слайда
(та же мерка, что в `sem-05/rendered/make_figures_mcp.py` § «Схемы раздела
MCP» — 20 px ≈ 11 pt), высоты подобраны под `FIG_NATURAL_H=4.3″`
(`deck_kit.FIG_NATURAL_H`) с небольшим запасом по ширине заполнения.

  subagent-n41-vhod-vyhod-roli.png     n41   вход / выход роли + 3 состояния списка
  subagent-n51-signal-ne-dohodit.png   n51   две полосы: ожидание vs факт
  subagent-n58-granitsa-dvukh-rolei.png n58  две зоны ответственности + промежуток
"""
from fig_toolkit import *

MW = 1600
CODEBG = (0x16, 0x1C, 0x30)


def mtext(d, x, y, t, sz=23, col=INK, b=False, m=False, strike=False):
    fo = f(sz, b, m)
    d.text((x, y), t, font=fo, fill=col)
    w = d.textlength(t, font=fo)
    if strike:
        d.line([x - 4, y + sz * 0.58, x + w + 4, y + sz * 0.58], fill=DEEP, width=3)
    return w


def mcent(d, y, t, sz=23, col=INK, b=False):
    fo = f(sz, b)
    d.text(((MW - d.textlength(t, font=fo)) // 2, y), t, font=fo, fill=col)


def mpanel(d, x, y, w, h, title=None, *, fill=SURF, stroke=LIGHT, tsz=22, tcol=DEEP, r=12, sw=3):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)
    if title:
        d.text((x + 18, y + 12), title, font=f(tsz, True), fill=tcol)


def msave(name):
    print("  ", name)


# ═══════════════════════════════════════════════════════════════════════════
# n41 — роль целиком: вход, выход, три состояния списка инструментов
#
# Три колонки В ОДИН РЯД, не два яруса (ход 1 полотна был 1600×820 — втрое
# ниже своей ширины, чем позволяет бюджет g_content: `deck_kit.FIG_NATURAL_H`
# = 4,3″ при ширине 12,23″ держит соотношение ≤ 0,35; схема ужалась до 71%
# ширины и напечатала «СХЕМА ЗАЖАТА» при сборке. Та же информация, уложенная
# в одну строку колонок, укладывается в соотношение без переверстки состава.
#
# Круг после прожарок (issue 225, P1-2): красный был в «чего физически НЕТ»,
# в подписи «промежуточные вызовы не видны» и в строке «опечатка в имени
# списка» — палитра его не содержит (tools/presentation-build/README.md §5).
# Все три — на SOFT_GREY/GHOST/DEEP: тот же тёмно-синий, что держит вес
# предупреждения в остальной деке, без спектрального красного.
# ═══════════════════════════════════════════════════════════════════════════
H41 = 580
im = Image.new("RGB", (MW, H41), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Вход роли, выход роли — и что значит список инструментов", 24, DEEP, b=True)

CY0 = 50
# ── колонка 1: вход ─────────────────────────────────────────────────────────
C1X, C1W = 20, 580
mpanel(d, C1X, CY0, C1W, 330, "НА ВХОДЕ", fill=SURF, stroke=MID, tcol=MID, tsz=19)
inputs = [
    "системный промпт роли — тело её файла",
    "рабочий каталог",
    "задача от вызывающей сессии (не дословна)",
    "иерархия файлов инструкций, всеми уровнями",
    "снимок репозитория на момент старта",
]
y = CY0 + 44
for it in inputs:
    d.ellipse([C1X + 18, y + 6, C1X + 28, y + 16], fill=TEAL)
    lines_ = wrap(d, it, f(16), C1W - 56)
    for k, ln in enumerate(lines_):
        mtext(d, C1X + 38, y + k * 21, ln, 16, INK)
    y += 21 * len(lines_) + 7

mpanel(d, C1X, CY0 + 338, C1W, 120, None, fill=SOFT_GREY, stroke=GHOST)
mtext(d, C1X + 16, CY0 + 350, "чего физически НЕТ:", 16, DEEP, b=True)
for k, ln in enumerate(["история переписки сессии", "автопамять", "уже прочитанные файлы"]):
    mtext(d, C1X + 16, CY0 + 378 + k * 24, "✘  " + ln, 15, DEEP)

# ── колонка 2: выход ────────────────────────────────────────────────────────
C2X, C2W = 620, 460
mpanel(d, C2X, CY0, C2W, 160, "НА ВЫХОДЕ", fill=SURF, stroke=MID, tcol=MID, tsz=19)
box(d, C2X + C2W // 2 - 170, CY0 + 54, 340, 76, ["только итоговый текст"], GOLD, tc=DEEP, sz=20)
mtext(d, C2X + 16, CY0 + 138, "✘  промежуточные вызовы не видны", 15, DEEP)

mpanel(d, C2X, CY0 + 172, C2W, 140, None, fill=W, stroke=SOFT_GREY)
mtext(d, C2X + 16, CY0 + 184, "канал односторонний:", 16, DEEP, b=True)
arrow(d, C2X + 32, CY0 + 220, C2X + C2W - 32, CY0 + 220, col=MID, wd=4)
mtext(d, C2X + 32, CY0 + 226, "задача →", 14, MUTE)
mtext(d, C2X + C2W - 96, CY0 + 226, "роль", 14, MUTE)
arrow(d, C2X + C2W - 32, CY0 + 268, C2X + 32, CY0 + 268, col=GOLD, wd=4)
mtext(d, C2X + 32, CY0 + 274, "итог ←", 14, MUTE)
mtext(d, C2X + C2W - 96, CY0 + 274, "роль", 14, MUTE)

mpanel(d, C2X, CY0 + 320, C2W, 60, None, fill=SURF, stroke=LIGHT)
for k, ln in enumerate(wrap(d, "проверить состав инструментов — одной командой", f(16), C2W - 32)):
    mtext(d, C2X + 16, CY0 + 332 + k * 20, ln, 16, INK)

# ── колонка 3: строка tools — три состояния, стопкой ────────────────────────
C3X, C3W = 1100, 480
mtext(d, C3X, CY0, "Строка tools: — три состояния", 18, DEEP, b=True)
states = [
    (MID, "список НЕ указан вовсе", "роль получает ВСЕ инструменты субагентов —\nпротивоположность «без инструментов»"),
    (TEAL, "список явно пуст", "роль без единого инструмента — но живая"),
    (DEEP, "опечатка в имени списка", "харнесс не запускает роль вовсе"),
]
sy = CY0 + 34
SCH = 92
for col, head_, body in states:
    mpanel(d, C3X, sy, C3W, SCH, None, fill=SURF, stroke=col)
    d.rectangle([C3X, sy, C3X + 8, sy + SCH], fill=col)
    mtext(d, C3X + 22, sy + 12, head_, 16, col, b=True)
    for k, ln in enumerate(body.split("\n")):
        mtext(d, C3X + 22, sy + 38 + k * 20, ln, 14, INK)
    sy += SCH + 14

im = im.crop((0, 0, MW, 572))
im.save(OUT / "subagent-n41-vhod-vyhod-roli.png")
msave("subagent-n41-vhod-vyhod-roli.png")


# ═══════════════════════════════════════════════════════════════════════════
# n51 — сигнал не доходит: ожидание vs факт, две полосы
#
# Круг после прожарок (issue 225, P1-2): вся нижняя полоса («ФАКТ») была
# залита красным — запрещённый цвет (tools/presentation-build/README.md §5).
# Замена — DEEP (самый тёмный тон палитры): ряд «ОЖИДАНИЕ» держит TEAL/MID/
# GOLD, ряд «ФАКТ» целиком DEEP — контраст между «как должно быть» и «как
# вышло на самом деле» держится цветом тона, не спектральным красным.
# ═══════════════════════════════════════════════════════════════════════════
H51 = 560
im = Image.new("RGB", (MW, H51), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Хук внутри субагента сказал «deny» — а вызов выполнился", 25, DEEP, b=True)

BX = [30, 430, 900]
BW_ = [370, 440, 640]
BH_ = 96


def lane(y, tag, tagcol, boxes, arrow_col, arrow_label, broken=False):
    lw = d.textlength(tag, font=f(20, True))
    d.rounded_rectangle([20, y, 40 + lw, y + 34], radius=10, fill=tagcol)
    d.text((30, y + 6), tag, font=f(20, True), fill=W)
    by = y + 48
    for (bx, bw), txt, fc, tc in boxes:
        box(d, bx, by, bw, BH_, txt, fc, tc=tc, sz=19)
    # стрелка между 2-й и 3-й коробкой несёт вывод ("остановлен"/"исполнился")
    x1 = boxes[0][0][0] + boxes[0][0][1]
    x2 = boxes[1][0][0]
    arrow(d, x1 + 6, by + BH_ // 2, x2 - 6, by + BH_ // 2, col=arrow_col, wd=5,
          dash=broken)
    if broken:
        xmark(d, (x1 + x2) // 2, by + BH_ // 2, 13, DEEP, wd=5)
    lw2 = d.textlength(arrow_label, font=f(16, True))
    d.text(((x1 + x2) / 2 - lw2 / 2, by - 24), arrow_label, font=f(16, True),
           fill=(DEEP if broken else TEAL))
    x3 = boxes[1][0][0] + boxes[1][0][1]
    x4 = boxes[2][0][0]
    arrow(d, x3 + 6, by + BH_ // 2, x4 - 6, by + BH_ // 2, col=MID, wd=5)
    return by + BH_


lane(70, "ОЖИДАНИЕ", TEAL,
     [((BX[0], BW_[0]), "хук в субагенте:\n«deny»", MID, W),
      ((BX[1], BW_[1]), "решение доходит\nдо родителя", TEAL, W),
      ((BX[2], BW_[2]), "вызов остановлен", GOLD, DEEP)],
     TEAL, "доходит")

lane(260, "ФАКТ", DEEP,
     [((BX[0], BW_[0]), "хук в субагенте:\n«deny»", MID, W),
      ((BX[1], BW_[1]), "решение НЕ доходит\nдо родителя", DEEP, W),
      ((BX[2], BW_[2]), "вызов исполняется", DEEP, W)],
     DEEP, "не доходит", broken=True)

# Два случая текстом НЕ дублируются здесь: слайд n51.md уже несёт их своими
# блоками («Случай 1.» / «Случай 2.» + замыкающая цитата), и `g_content`
# рисует их ПОД этой схемой — ровно так, как просит visual.primary («под
# схемой — два коротких случая текстом»). Повтор в самой картинке дал
# видимое наложение двух одинаковых по смыслу панелей (iter 2 → снято).
im = im.crop((0, 0, MW, 424))
im.save(OUT / "subagent-n51-signal-ne-dohodit.png")
msave("subagent-n51-signal-ne-dohodit.png")


# ═══════════════════════════════════════════════════════════════════════════
# n58 — граница в обе стороны: две зоны + промежуток между ними
#
# Круг после прожарок (issue 225). Два отдельных дефекта на одном экране:
#
# P1-2 (красный запрещён палитрой) — оба «НЕ для:» бокса и пунктирный
# «промежуток» были залиты/обведены красным. Замена: нейтральный
# SOFT_GREY/GHOST + DEEP текст для боксов-границ, GHOST для пунктира
# промежутка — тот же тёмно-синий регистр, что держит вес остальных
# предупреждений деки.
#
# Находка читателя (reader-roast, п.1): правый бокс («тестировщик») на вид
# был РАВНОЦЕННОЙ готовой границей наравне с левым («НЕ для: ревью
# архитектурных решений»), хотя по источнику (section-2-subagent-part1c.md
# n62 «Речь») это НЕ готовая граница, а открытая задача: «тестировщику
# нужна симметричная строка… по-доменному, не абстрактно» — строка ещё НЕ
# написана. Одинаковый сплошной «НЕ для:» стиль на обоих боксах стирал эту
# разницу. Починка — левый бокс остаётся сплошным (готовая граница), правый
# становится ПУНКТИРНЫМ, той же грамматикой, что у «честного пробела»
# (dashbox, не заливка): визуально читается как «ещё не заполнено», не как
# вторая готовая граница. Текст не выдуман — дословно по источнику.
# ═══════════════════════════════════════════════════════════════════════════
H58 = 480
im = Image.new("RGB", (MW, H58), W); d = ImageDraw.Draw(im)
mtext(d, 20, 6, "Промежуток между ролями закрывает явная граница в обе стороны", 25, DEEP, b=True)

ZY, ZH = 70, 260
ZW = 640
GAPW = MW - 2 * 30 - 2 * ZW
ZX1, ZX2 = 30, 30 + ZW + GAPW

mpanel(d, ZX1, ZY, ZW, ZH, None, fill=SURF, stroke=MID, sw=4)
mtext(d, ZX1 + 24, ZY + 18, "диф-ревьюер", 26, MID, b=True)
mtext(d, ZX1 + 24, ZY + 56, "зона: код, построчно", 19, INK)
mpanel(d, ZX1 + 24, ZY + 150, ZW - 48, 86, None, fill=SOFT_GREY, stroke=GHOST)
mtext(d, ZX1 + 40, ZY + 164, "НЕ для:", 18, DEEP, b=True)
for k, ln in enumerate(wrap(d, "ревью архитектурных решений — это отдельная роль", f(18), ZW - 100)):
    mtext(d, ZX1 + 40, ZY + 190 + k * 24, ln, 18, INK)

mpanel(d, ZX2, ZY, ZW, ZH, None, fill=SURF, stroke=TEAL, sw=4)
mtext(d, ZX2 + 24, ZY + 18, "тестировщик", 26, TEAL, b=True)
mtext(d, ZX2 + 24, ZY + 56, "зона: поведение формы", 19, INK)
dashbox(d, ZX2 + 24, ZY + 150, ZW - 48, 108, GHOST, dash=10, gap=7, width=2)
mtext(d, ZX2 + 40, ZY + 164, "пока не написано:", 18, GHOST, b=True)
for k, ln in enumerate(wrap(d, "своя граница — симметричная диф-ревьюеру, по-доменному, не абстрактно",
                            f(18), ZW - 100)):
    mtext(d, ZX2 + 40, ZY + 190 + k * 24, ln, 18, GHOST)

# промежуток
gx1, gx2 = ZX1 + ZW, ZX2
dashbox(d, gx1 + 10, ZY + 30, gx2 - gx1 - 20, ZH - 60, GHOST, dash=12, gap=9, width=3)
glabel = ["промежуток,", "не поручен", "ни одной роли"]
gy = ZY + 60
for ln in glabel:
    lw = d.textlength(ln, font=f(17, True))
    d.text(((gx1 + gx2) / 2 - lw / 2, gy), ln, font=f(17, True), fill=GHOST)
    gy += 24

# золотая планка слева — та же грамматика, что у `form_formula` (итог, не
# заливка целиком: гость один раз на слайде, см. deck_kit.py «Грамматика
# деки»); у этого слайда ## Visual пуст, и единственный текст, несущий вес
# итога, — вот эта подпись, так что золото здесь, а не внутри самих зон.
d.rounded_rectangle([30, ZY + ZH + 24, 38, ZY + ZH + 80], radius=4, fill=GOLD)
mtext(d, 54, ZY + ZH + 28, "Граница делает промежуток видимым тому, кто читает оба описания рядом —", 21, DEEP, b=True)
mtext(d, 54, ZY + ZH + 56, "не убирает сам промежуток.", 21, DEEP, b=True)
im.save(OUT / "subagent-n58-granitsa-dvukh-rolei.png")
msave("subagent-n58-granitsa-dvukh-rolei.png")

report()
