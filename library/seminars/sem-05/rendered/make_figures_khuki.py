#!/usr/bin/env python3
"""Схемы блока «Хуки» новой деки Семинара 5 — слайды n06–n32.

Рисуются программно (PIL), а не описываются словами. Файл принадлежит сессии
блока «Хуки»; make_figures.py / make_figures_skill.py / make_figures_mcp.py /
make_figures_otkrytie.py этой сессией не трогаются.

Масштаб подписей — тот же, что в make_figures.py: полотно 2400 px вставляется
шириной 12,2″ на канву 13,333″, поэтому 38 px читается как 14 pt, 30 px — как
11 pt. Ниже 30 px не опускаться: на проекторе не читается.

  khuki-n07-stsena.png      n07  три кадра сцены: правка → коммит → main
  khuki-n12-ustroystvo.png  n12  ПОЛНАЯ СТРУКТУРА хука: пять блоков одним экраном
  khuki-n15-proval.png      n15  шесть форм команды: одна отклонена, пять мимо
  khuki-n18-stsena.png      n18  два пути одной правки, барьер на одном
  khuki-n22-kletki.png      n22  решётка «момент × жёсткость», целевая клетка
  khuki-n26-stsena.png      n26  одна задача, двадцать правок, цикл на каждой
  khuki-n29-umnozhenie.png  n29  узкий матчер против широкого, один масштаб
  khuki-n32-sloi.png        n32  два уровня настроек в один вызов
"""
from PIL import Image, ImageDraw
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from PIL import ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FMB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); WARM = (0xFF, 0xF7, 0xE2); PALE = (0xE6, 0xEE, 0xF4)

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)
WARN = []


def f(sz, b=False, m=False):
    if m:
        return ImageFont.truetype(FMB if b else FM, sz)
    return ImageFont.truetype(FB if b else F, sz)


def fit(d, txt, fo, limit, where):
    if d.textlength(txt, font=fo) > limit:
        WARN.append(f"{where}: шире отведённого — {txt[:54]!r}")


def box(d, x, y, w, h, lines, fc, tc=W, sz=32, b=True, m=False, r=12, pad=18,
        outline=None, where="?"):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    if isinstance(lines, str):
        lines = [lines]
    th = len(lines) * (sz + 8) - 8
    cy = y + (h - th) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        tw = d.textlength(ln, font=fo)
        d.text((x + (w - tw) // 2, cy + i * (sz + 8)), ln, font=fo, fill=tc)


def lbox(d, x, y, w, h, lines, fc, tc=INK, sz=30, b=False, m=False, r=12,
         pad=20, outline=None, where="?"):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    th = len(lines) * (sz + 9) - 9
    cy = y + (h - th) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        d.text((x + pad, cy + i * (sz + 9)), ln, font=fo, fill=tc)


def arrow(d, x1, y1, x2, y2, col=MID, wd=5, head=16):
    import math
    d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42)),
               (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))],
              fill=col)


def caption(d, y, txt, sz=34, col=DEEP, b=True, Wd=2400):
    fo = f(sz, b)
    fit(d, txt, fo, Wd - 80, "подпись")
    tw = d.textlength(txt, font=fo)
    d.text(((Wd - tw) // 2, y), txt, font=fo, fill=col)


def head(d, txt, sz=34):
    d.text((40, 18), txt, font=f(sz, True), fill=DEEP)


def save(im, name):
    im.save(OUT / name)


# ── n07. Три кадра сцены ─────────────────────────────────────────────────────
im = Image.new("RGB", (2400, 410), W); d = ImageDraw.Draw(im)
head(d, "Одна сессия, три кадра — и ни одного нарушенного правила")
frames = [
    ("1", ["агент правит", "валидацию формы"], MID),
    ("2", ["`git commit`"], MID),
    ("3", ["коммит лёг", "в main"], RED),
]
x = 90
for num, lines, col in frames:
    box(d, x, 88, 560, 168, lines, SURF, tc=INK, sz=36, b=True, where="n07 кадр")
    box(d, x + 18, 104, 56, 56, num, col, sz=32, r=28, pad=6, where="n07 номер")
    x += 700
for cx in (700, 1400):
    arrow(d, cx - 40, 172, cx + 55, 172, col=LIGHT, wd=6, head=20)
box(d, 90, 290, 2220, 88,
    "правило не нарушено: правила про ветки в файле нет", RED, sz=40,
    where="n07 плашка")
save(im, "khuki-n07-stsena.png")

# ── n12. Полная структура хука: пять блоков одним экраном ────────────────────
# Структурный слайд по требованию владельца: «у нас нигде не прописаны
# структурно варианты вызова и работы хука». Такты Б и разборы дальше
# работают как напоминания об этой карте.
im = Image.new("RGB", (2400, 1080), W); d = ImageDraw.Draw(im)
head(d, "Хук целиком: где объявлен, когда запускается, что получает, чем отвечает, что с этим делает среда")

def blocknum(n, x, y):
    box(d, x, y, 52, 52, str(n), DEEP, sz=30, r=26, pad=6, where="n12 номер")

# 1 — где объявляется
blocknum(1, 60, 92)
d.text((128, 100), "ГДЕ ОБЪЯВЛЯЕТСЯ", font=f(30, True), fill=DEEP)
lbox(d, 60, 156, 1090, 196,
     ["signup-landing/.claude/settings.json   — файл под контролем версий,",
      "                                         поэтому едет с клоном",
      "",
      "hooks → PreToolUse → [ { matcher, hooks: [ { command, timeout } ] } ]",
      "  где       событие       на что            что            сколько",
      "  живёт     запуска       реагировать       запустить      ждать"],
     SURF, sz=25, m=True, where="n12 блок 1")

# 2 — когда запускается
blocknum(2, 1250, 92)
d.text((1318, 100), "КОГДА ЗАПУСКАЕТСЯ — событий 33, нам нужно одно", font=f(30, True), fill=DEEP)
ev = [("вызов инструмента", "до · после", GOLD, DEEP),
      ("сессия", "старт · конец", SURF, INK),
      ("ход", "запрос · стоп", SURF, INK),
      ("файлы", "правка · каталог", SURF, INK),
      ("субагенты", "старт · конец", SURF, INK),
      ("модель, сжатие", "смена · сжатие", SURF, INK)]
yy = 156
for i, (name, sub, fc, tc) in enumerate(ev):
    xx = 1250 + (i % 2) * 560
    if i % 2 == 0 and i: yy += 68
    lbox(d, xx, yy, 540, 58, [f"{name} — {sub}"], fc, tc=tc, sz=23,
         b=(fc is GOLD), where="n12 событие")
d.text((1250, 366), "золотом — то единственное событие, на которое мы вешаем барьер",
       font=f(24), fill=MUTE)

# 3 — что приходит на вход
blocknum(3, 60, 420)
d.text((128, 428), "ЧТО ПРИХОДИТ НА ВХОД — описание предстоящего вызова", font=f(30, True), fill=DEEP)
lbox(d, 60, 484, 1090, 196,
     ["{ \"tool_name\":   \"Bash\",                    какой инструмент",
      "  \"tool_input\":  { \"command\": \"git commit …\" }   его аргументы",
      "  \"cwd\":         \"/path/to/repo\",             рабочий каталог",
      "  \"permission_mode\": \"default\" }              режим прав"],
     SURF, sz=25, m=True, where="n12 блок 3")

# 4 — чем отвечает
blocknum(4, 1250, 420)
d.text((1318, 428), "ЧЕМ ОТВЕЧАЕТ — два канала", font=f(30, True), fill=DEEP)
lbox(d, 1250, 484, 1090, 88,
     ["код возврата:  0 — решение напечатано   ·   2 — блокировать"],
     SURF, sz=25, m=True, where="n12 блок 4 код")
for i, (t_, fc) in enumerate([("запретить", RED), ("спросить", GOLD), ("разрешить", TEAL)]):
    box(d, 1250 + i * 370, 592, 350, 88, t_, fc,
        tc=DEEP if fc is GOLD else W, sz=28, where="n12 решение")
d.text((1250, 692), "решение — одно из трёх; поля нет → среда идёт обычным порядком",
       font=f(24), fill=MUTE)

# 5 — что среда делает с ответом
blocknum(5, 60, 748)
d.text((128, 756), "ЧТО СРЕДА ДЕЛАЕТ С ОТВЕТОМ", font=f(30, True), fill=DEEP)
steps = [("модель собрала\nаргументы", SURF, INK), ("сработало\nсобытие", GOLD, DEEP),
         ("хук получил\nописание", SURF, INK), ("хук напечатал\nрешение", SURF, INK),
         ("среда применила:\nвызов идёт или нет", MID, W)]
x = 60
for i, (t_, fc, tc) in enumerate(steps):
    box(d, x, 812, 400, 130, t_.split("\n"), fc, tc=tc, sz=26, where="n12 конвейер")
    if i < 4: arrow(d, x + 406, 877, x + 448, 877, col=LIGHT, wd=5, head=16)
    x += 454
lbox(d, 60, 962, 2280, 84,
     ["Запрет сильнее разрешения. Причину при запрете читает агент; при «спросить» и «разрешить» — только человек."],
     WARM, sz=27, b=True, outline=GOLD, where="n12 итог")
save(im, "khuki-n12-ustroystvo.png")

# ── n13 — схема отменена ─────────────────────────────────────────────────────
# Прежняя khuki-n13-sborka.png («вопрос → уровень структуры») дублировала
# структурный слайд n12 и воспроизводила ровно то, на что жаловался владелец
# («два раза записано одно и то же»). Слайд теперь несёт таблицу вариантов.
# Сессии рендерера: снять запись "n13" из FIGS в build_sem05.py.

# ── n15. Шесть форм команды ──────────────────────────────────────────────────
im = Image.new("RGB", (2400, 506), W); d = ImageDraw.Draw(im)
head(d, "Шесть форм одной команды: отклонена одна")
forms = [
    ("git commit", True),
    ("git commit  (ветка trunk)", False),
    ("git -C . commit", False),
    ("/usr/bin/git commit", False),
    ("env git commit", False),
    ("… && git commit  (2-я строка)", False),
]
y = 84
for txt, denied in forms:
    fc = RED if denied else SURF
    tc = W if denied else INK
    lbox(d, 60, y, 1180, 54, [txt], fc, tc=tc, sz=30, m=True, where="n15 форма")
    if denied:
        box(d, 1290, y, 460, 54, "ОТКЛОНЁН", RED, sz=30, where="n15 исход")
    else:
        box(d, 1290, y, 460, 54, "барьер молчит", MUTE, sz=30, where="n15 исход")
    y += 58
lbox(d, 1810, 84, 530, 336,
     ["из шести форм", "отклонена одна", "", "четыре из пяти", "нашёл внешний", "тест"],
     WARM, sz=32, b=True, outline=GOLD, where="n15 база")
box(d, 60, 440, 2280, 52,
    "исполняемый файл с правильным именем — не барьер", DEEP, sz=36,
    where="n15 итог")
save(im, "khuki-n15-proval.png")

# ── n18. Два пути одной правки ───────────────────────────────────────────────
im = Image.new("RGB", (2400, 560), W); d = ImageDraw.Draw(im)
head(d, "Одна и та же правка файла — два пути, барьер только на одном")
box(d, 900, 95, 600, 90, "правка файла", DEEP, sz=36, where="n18 вход")
arrow(d, 1050, 195, 700, 265, col=LIGHT, wd=6, head=18)
arrow(d, 1350, 195, 1700, 265, col=LIGHT, wd=6, head=18)
box(d, 300, 275, 800, 90, "через Edit / Write", MID, sz=34, where="n18 путь 1")
box(d, 1300, 275, 800, 90, "через Bash: sed -i", MID, sz=34, where="n18 путь 2")
arrow(d, 700, 375, 700, 425, col=LIGHT, wd=6, head=18)
arrow(d, 1700, 375, 1700, 425, col=LIGHT, wd=6, head=18)
box(d, 300, 435, 800, 90, "матчер совпал → барьер", GOLD, tc=DEEP, sz=34,
    where="n18 исход 1")
box(d, 1300, 435, 800, 90, "матчер не совпал → тишина", RED, sz=34,
    where="n18 исход 2")
save(im, "khuki-n18-stsena.png")

# ── n22. Решётка «момент × жёсткость» ────────────────────────────────────────
im = Image.new("RGB", (2400, 640), W); d = ImageDraw.Draw(im)
head(d, "Две оси: когда вмешиваться и насколько жёстко")
cols = ["до вызова", "после вызова"]
rws = ["запретить", "спросить", "разрешить"]
x0, y0, cw, ch = 560, 120, 780, 118
for j, c in enumerate(cols):
    box(d, x0 + j * (cw + 20), y0, cw, 66, c, DEEP, sz=34, where="n22 колонка")
for i, r in enumerate(rws):
    box(d, 60, y0 + 86 + i * (ch + 14), 470, ch, r, MID, sz=34, where="n22 строка")
cells = {
    (0, 0): ("ЦЕЛЕВОЙ", GOLD, DEEP),
    (0, 1): ("протокол, не запрет", SURF, INK),
    (1, 0): ("так отвечает наш хук\nв соседней клетке", SURF, INK),
    (1, 1): ("бессмысленно", SURF, MUTE),
    (2, 0): ("снова текст", SURF, INK),
    (2, 1): ("вырождено", PALE, MUTE),
}
for (i, j), (txt, fc, tc) in cells.items():
    box(d, x0 + j * (cw + 20), y0 + 86 + i * (ch + 14), cw, ch,
        txt.split("\n"), fc, tc=tc, sz=30,
        b=(fc is GOLD), where="n22 клетка")
save(im, "khuki-n22-kletki.png")

# ── n26. Одна задача, двадцать правок ────────────────────────────────────────
im = Image.new("RGB", (2400, 470), W); d = ImageDraw.Draw(im)
head(d, "Одна задача, двадцать правок — и полный цикл проверок на каждой")
d.rounded_rectangle([60, 110, 2340, 176], radius=12, fill=DEEP)
fo = f(32, True)
d.text((92, 128), "задача", font=fo, fill=W)
n = 20
step = (2340 - 320) / n
for i in range(n):
    x = 320 + i * step
    d.line([x, 176, x, 250], fill=LIGHT, width=4)
    d.rounded_rectangle([x - 34, 250, x + 34, 330], radius=8, fill=WARM,
                        outline=GOLD, width=2)
caption(d, 356, "на каждой правке — синтаксис + сборка, и так двадцать раз", sz=34,
        col=INK)
caption(d, 410, "ни одного сообщения об ошибке", sz=32, col=RED)
save(im, "khuki-n26-stsena.png")

# ── n29. Узкий матчер против широкого ────────────────────────────────────────
im = Image.new("RGB", (2400, 440), W); d = ImageDraw.Draw(im)
head(d, "Один масштаб: что платит задача при узком и при широком матчере")
base_y, maxh = 330, 208
# 27 мс против 51 000 мс — логарифм невозможен наглядно, поэтому
# показываем полосу узкого как видимый минимум и подписываем кратность.
bars = [
    ("узкий матчер\n1 срабатывание", 27, "27 мс за задачу", TEAL),
    ("широкий матчер\n40 срабатываний", 51000, "51 с за задачу", RED),
]
x = 380
for label, val, note, col in bars:
    h = max(14, int(maxh * (val / 51000)))
    d.rounded_rectangle([x, base_y - h, x + 520, base_y], radius=10, fill=col)
    fo = f(34, True)
    tw = d.textlength(note, font=fo)
    d.text((x + (520 - tw) // 2, base_y - h - 48), note, font=fo, fill=col)
    for k, ln in enumerate(label.split("\n")):
        fo2 = f(32, k == 0)
        tw = d.textlength(ln, font=fo2)
        d.text((x + (520 - tw) // 2, base_y + 16 + k * 40), ln, font=fo2, fill=INK)
    x += 1120
d.line([60, base_y, 2340, base_y], fill=MUTE, width=3)
lbox(d, 80, 96, 620, 118,
     ["одна и та же", "машина и проект,", "разница — матчер"],
     WARM, sz=32, b=True, outline=GOLD, where="n29 выноска")
save(im, "khuki-n29-umnozhenie.png")

# ── n32. Два уровня настроек ─────────────────────────────────────────────────
im = Image.new("RGB", (2400, 520), W); d = ImageDraw.Draw(im)
head(d, "Списки хуков не перекрываются — они объединяются")
box(d, 120, 110, 900, 110, "личные настройки: свой хук", MID, sz=34,
    where="n32 уровень 1")
box(d, 120, 250, 900, 110, "настройки проекта: свой хук", MID, sz=34,
    where="n32 уровень 2")
box(d, 1480, 175, 800, 120, "один и тот же вызов", DEEP, sz=36,
    where="n32 вызов")
arrow(d, 1040, 165, 1460, 220, col=LIGHT, wd=6, head=18)
arrow(d, 1040, 305, 1460, 250, col=LIGHT, wd=6, head=18)
box(d, 1480, 320, 800, 100, "платит сумму обоих", RED, sz=34, where="n32 итог")
lbox(d, 120, 400, 1240, 100,
     ["владелец репозитория второй уровень видит,", "а первый — не видит вовсе"],
     WARM, sz=30, b=True, outline=GOLD, where="n32 оговорка")
save(im, "khuki-n32-sloi.png")

print("схемы блока «Хуки»:")
for p in sorted(OUT.glob("khuki-*.png")):
    print("  ", p.name)
if WARN:
    print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
    for w in dict.fromkeys(WARN):
        print("  ", w)
else:
    print("\nпредупреждений нет: весь текст укладывается в отведённые блоки")
