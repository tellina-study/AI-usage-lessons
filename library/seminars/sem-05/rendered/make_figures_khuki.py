#!/usr/bin/env python3
"""Схемы блока «Хуки» новой деки Семинара 5 — слайды n06–n32.

Рисуются программно (PIL), а не описываются словами. Файл принадлежит сессии
блока «Хуки»; make_figures.py / make_figures_skill.py / make_figures_mcp.py /
make_figures_otkrytie.py этой сессией не трогаются.

Масштаб подписей — тот же, что в make_figures.py: полотно 2400 px вставляется
шириной 12,2″ на канву 13,333″, поэтому 38 px читается как 14 pt, 30 px — как
11 pt. Ниже 30 px не опускаться: на проекторе не читается.

  khuki-n12-ustroystvo.png  n12  ПОЛНАЯ СТРУКТУРА хука: пять блоков одним экраном
  khuki-n15-proval.png      n15  шесть форм команды: одна отклонена, пять мимо
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
import deck_kit as K                      # общий набор: проверка наложений и подписей
CL = K.Claims(tol=2)                     # была локальная копия _claim — снята,
                                         # алгоритм жил в трёх экземплярах


def f(sz, b=False, m=False):
    if m:
        return ImageFont.truetype(FMB if b else FM, sz)
    return ImageFont.truetype(FB if b else F, sz)


def fit(d, txt, fo, limit, where):
    if d.textlength(txt, font=fo) > limit:
        WARN.append(f"{where}: шире отведённого — {txt[:54]!r}")


def box(d, x, y, w, h, lines, fc, tc=W, sz=32, b=True, m=False, r=12, pad=18,
        outline=None, where="?"):
    CL.claim(x, y, w, h, where)
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    if isinstance(lines, str):
        lines = [lines]
    for _ln in lines:
        CL.label(_ln, where)
    th = len(lines) * (sz + 8) - 8
    cy = y + (h - th) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        tw = d.textlength(ln, font=fo)
        d.text((x + (w - tw) // 2, cy + i * (sz + 8)), ln, font=fo, fill=tc)


def lbox(d, x, y, w, h, lines, fc, tc=INK, sz=30, b=False, m=False, r=12,
         pad=20, outline=None, where="?"):
    CL.claim(x, y, w, h, where)
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
    txt = CL.label(txt, "подпись")
    fo = f(sz, b)
    fit(d, txt, fo, Wd - 80, "подпись")
    tw = d.textlength(txt, font=fo)
    d.text(((Wd - tw) // 2, y), txt, font=fo, fill=col)


def head(d, txt, sz=34):
    d.text((40, 18), CL.label(txt, "заголовок схемы"), font=f(sz, True), fill=DEEP)


def save(im, name):
    im.save(OUT / name)
    CL.rects.clear()   # новое полотно — новый набор прямоугольников


# ── n07 — схема отменена ─────────────────────────────────────────────────────
# Слайд показывает CLAUDE.md демо-репозитория ЦЕЛИКОМ, 20 строк, 845 знаков —
# это его единственная работа: зал читает файл и сам видит, чего в нём нет.
# Со схемой листинг ложился на дно кегля (7,5 pt, «ниже приём не умеет») и с
# задних рядов не читался. Три кадра сцены проговариваются в заметках, а
# красная плашка схемы дублировала ## Assertion слайда.
# Сессии рендерера: снять запись "n07" из FIGS.

# ── n12. Полная структура хука: пять блоков одним экраном ────────────────────
# Структурный слайд по требованию владельца: «у нас нигде не прописаны
# структурно варианты вызова и работы хука».
# ВАЖНО ПРО РАЗМЕР. g_content кладёт схему как K.figure(..., WIDTH, mh if mh
# else 4.3): когда композиция помещается, mh приходит None и высота режется
# потолком 4,3″. Поэтому ширину слайда занимает только схема с соотношением
# 12,23/4,3 = 2,84 и выше; при 2400×1080 (2,22) схема упиралась в потолок
# высоты и занимала 78% ширины — с полями по бокам и мелким текстом, БЕЗ
# единого предупреждения от сборки. Находка сессии блока «Скиллы», у них тот
# же случай. Отсюда полотно 2400×844.
im = Image.new("RGB", (2400, 844), W); d = ImageDraw.Draw(im)
head(d, "Хук целиком: где объявлен, когда запускается, что получает, чем отвечает, что с этим делает среда", sz=32)

def blocknum(n, x, y):
    box(d, x, y, 46, 46, str(n), DEEP, sz=27, r=23, pad=6, where="+n12 номер")

# 1 — где объявляется
blocknum(1, 60, 70)
d.text((120, 78), "ГДЕ ОБЪЯВЛЯЕТСЯ", font=f(28, True), fill=DEEP)
lbox(d, 60, 126, 1090, 160,
     ["signup-landing/.claude/settings.json   — файл в git, едет с клоном",
      "",
      "hooks → PreToolUse → [ { matcher, hooks: [ { command, timeout } ] } ]",
      "  где       событие       на что          что          сколько",
      "  живёт     запуска       реагировать     запустить    ждать"],
     SURF, sz=24, m=True, where="n12 блок 1")

# 2 — когда запускается
blocknum(2, 1250, 70)
d.text((1310, 78), "КОГДА ЗАПУСКАЕТСЯ — событий 33, нам нужно одно", font=f(28, True), fill=DEEP)
ev = [("вызов инструмента", GOLD, DEEP), ("сессия", SURF, INK), ("ход", SURF, INK),
      ("файлы", SURF, INK), ("субагенты", SURF, INK), ("модель, сжатие", SURF, INK)]
for k, (name, fc, tc) in enumerate(ev):
    xx = 1250 + (k % 3) * 366
    yy = 126 + (k // 3) * 62
    lbox(d, xx, yy, 352, 52, [name], fc, tc=tc, sz=23, b=(fc is GOLD), where="n12 событие")
d.text((1250, 256), "золотом — единственное событие, на которое мы вешаем барьер",
       font=f(23), fill=MUTE)

# 3 — что приходит на вход
blocknum(3, 60, 320)
d.text((120, 328), "ЧТО ПРИХОДИТ НА ВХОД — описание предстоящего вызова", font=f(28, True), fill=DEEP)
lbox(d, 60, 376, 1090, 150,
     ["{ \"tool_name\":  \"Bash\",                    какой инструмент",
      "  \"tool_input\": { \"command\": \"git commit …\" }  его аргументы",
      "  \"cwd\":        \"/path/to/repo\",             рабочий каталог",
      "  \"permission_mode\": \"default\" }             режим прав"],
     SURF, sz=24, m=True, where="n12 блок 3")

# 4 — чем отвечает
blocknum(4, 1250, 320)
d.text((1310, 328), "ЧЕМ ОТВЕЧАЕТ — два канала", font=f(28, True), fill=DEEP)
lbox(d, 1250, 376, 1090, 60,
     ["код возврата:  0 — решение напечатано   ·   2 — блокировать"],
     SURF, sz=24, m=True, where="n12 блок 4 код")
for k, (t_, fc) in enumerate([("запретить", RED), ("спросить", GOLD), ("разрешить", TEAL)]):
    box(d, 1250 + k * 370, 448, 350, 62, t_, fc,
        tc=DEEP if fc is GOLD else W, sz=26, where="n12 решение")
d.text((1250, 522), "решение — одно из трёх; поля нет → среда идёт обычным порядком",
       font=f(23), fill=MUTE)

# 5 — что среда делает с ответом
blocknum(5, 60, 570)
d.text((120, 578), "ЧТО СРЕДА ДЕЛАЕТ С ОТВЕТОМ", font=f(28, True), fill=DEEP)
steps = [("модель собрала\nаргументы", SURF, INK), ("сработало\nсобытие", GOLD, DEEP),
         ("хук получил\nописание", SURF, INK), ("хук напечатал\nрешение", SURF, INK),
         ("среда применила:\nвызов идёт или нет", MID, W)]
x = 60
for k, (t_, fc, tc) in enumerate(steps):
    box(d, x, 626, 400, 104, t_.split("\n"), fc, tc=tc, sz=24, where="n12 конвейер")
    if k < 4: arrow(d, x + 406, 678, x + 448, 678, col=LIGHT, wd=5, head=16)
    x += 454
lbox(d, 60, 752, 2280, 68,
     ["Запрет сильнее разрешения. Причину при запрете читает агент; при «спросить» и «разрешить» — только человек."],
     WARM, sz=25, b=True, outline=GOLD, where="n12 итог")
save(im, "khuki-n12-ustroystvo.png")

# ── n13 — схема отменена ─────────────────────────────────────────────────────
# Прежняя khuki-n13-sborka.png («вопрос → уровень структуры») дублировала
# структурный слайд n12 и воспроизводила ровно то, на что жаловался владелец
# («два раза записано одно и то же»). Слайд теперь несёт таблицу вариантов.
# Сессии рендерера: снять запись "n13" из FIGS в build_sem05.py.

# ── n15. Шесть форм команды ──────────────────────────────────────────────────
# Раскладка в ДВЕ колонки по три: на слайде схеме достаётся 1,95″ по высоте,
# и при одной колонке (492 px, соотн. 4,88) она ужималась до 78% ширины —
# «слайд полупустой по бокам». Две колонки дают соотн. ~7,5 и полную ширину.
im = Image.new("RGB", (2400, 322), W); d = ImageDraw.Draw(im)
head(d, "Шесть форм одной команды: отклонена одна", sz=30)
forms = [
    ("git commit", True),
    ("git commit  (ветка trunk)", False),
    ("git -C . commit", False),
    ("/usr/bin/git commit", False),
    ("env git commit", False),
    ("… && git commit  (2-я строка)", False),
]
for k, (txt, denied) in enumerate(forms):
    cx = 60 + (k % 2) * 1180
    cy = 66 + (k // 2) * 58
    fc = RED if denied else SURF
    tc = W if denied else INK
    lbox(d, cx, cy, 720, 50, [txt], fc, tc=tc, sz=25, m=True, where="n15 форма")
    box(d, cx + 736, cy, 384, 50,
        "ОТКЛОНЁН" if denied else "барьер молчит",
        RED if denied else MUTE, sz=25, where="n15 исход")
box(d, 60, 250, 2280, 54,
    "из шести форм отклонена одна · исполняемый файл с правильным именем — не барьер",
    DEEP, sz=30, where="n15 итог")
save(im, "khuki-n15-proval.png")

# ── n18 — схема отменена ───────────────────────────────────────
# n18 стал двухчастной сценой (проблема → пауза → диагноз) по требованию владельца.
# Две таблицы, вопрос и вывод вместе со схемой не помещаются: композиция уходила
# на 8,06″ при полотне 7,50″. Диагноз словами в нижней таблице сильнее иллюстрации,
# поэтому схема снята.
# Сессии рендерера: снять запись из FIGS в build_sem05.py.

# ── n22 — схема отменена ─────────────────────────────────────────────────────
# Решётка «момент × жёсткость» показывала те же пять клеток, что и таблица
# разбора под ней, только без причин. Схеме на слайде оставалось 1,42″: она
# садилась до 61–72% ширины и читалась вставленной миниатюрой, а не главным
# объектом. Ничего, чего нет в тексте, она не несла: обе оси названы в стебле
# вопроса n20, вырожденная шестая клетка — в его заметках.
# Сессии рендерера: снять запись "n22" из FIGS.

# ── n29. Узкий матчер против широкого ───────────────────────────────────────
# Схеме достаётся 1,79″ — самый узкий слот из четырёх. Выноска снята: её
# текст («одна и та же машина и проект, разница — матчер») дословно есть в
# плашке слайда. Соотн. ~6,9, ширина полная.
im = Image.new("RGB", (2400, 348), W); d = ImageDraw.Draw(im)
head(d, "Один масштаб: что платит задача при узком и при широком матчере", sz=28)
base_y, maxh = 250, 168
bars = [("узкий матчер\n1 срабатывание", 27, "27 мс за задачу", TEAL),
        ("широкий матчер\n40 срабатываний", 51000, "51 с за задачу", RED)]
x = 380
for label, val, note, col in bars:
    h = max(12, int(maxh * (val / 51000)))
    d.rounded_rectangle([x, base_y - h, x + 520, base_y], radius=10, fill=col)
    fo = f(30, True); tw = d.textlength(note, font=fo)
    d.text((x + (520 - tw) // 2, base_y - h - 42), note, font=fo, fill=col)
    for k, ln in enumerate(label.split("\n")):
        fo2 = f(27, k == 0); tw = d.textlength(ln, font=fo2)
        d.text((x + (520 - tw) // 2, base_y + 12 + k * 34), ln, font=fo2, fill=INK)
    x += 1120
d.line([60, base_y, 2340, base_y], fill=MUTE, width=3)
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
     ["владелец репозитория видит проектные хуки,", "а личные участников — не видит"],
     WARM, sz=30, b=True, outline=GOLD, where="n32 оговорка")
save(im, "khuki-n32-sloi.png")

print("схемы блока «Хуки»:")
for p in sorted(OUT.glob("khuki-*.png")):
    print("  ", p.name)
WARN.extend(CL.report())
if WARN:
    print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
    for w in dict.fromkeys(WARN):
        print("  ", w)
else:
    print("\nпредупреждений нет: весь текст укладывается в отведённые блоки")
