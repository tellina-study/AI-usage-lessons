"""Общий тулкит для программных схем Семинара 6 (PIL).

Перенесён по образцу `sem-05/rendered/make_figures_ramka.py` /
`make_figures_mcp.py` — тот же набор примитивов (коробка, пунктирная коробка,
стрелка, центрированная подпись, перенос по словам, измерение влезания), но
переписан заново для sem-06 (копия, не импорт — `sem-05/**` не трогается).
Палитра Ocean — те же HEX, что в `deck_kit.py`.

── ЯЗЫК СХЕМ (issue 225, EN-трек) ──────────────────────────────────────────

Подписи схем нарисованы ПИКСЕЛЯМИ, поэтому проверка кириллицы по собранной
`.pptx` их не видит, а зал видит: английская дека вышла с одиннадцатью
русскими схемами (`qa/render-en.md` §6.1). Чинится здесь — одним аргументом,
по образцу `build_sem06.set_lang` и `make_deck_yaml.LANGS`:

    python3 make_figures_mcp.py              # русские схемы, как было
    python3 make_figures_mcp.py --lang en    # те же схемы по-английски

Аргумент разбирается ЗДЕСЬ, а не в четырёх рисовалках: все четыре начинаются
с `from fig_toolkit import *`, и второй копии разбора нет ни в одной.

**Где происходит перевод и почему именно там.** Не у литералов в рисовалках
(их больше трёхсот, и правка каждого — это вторая копия схемы), а в двух
методах PIL, через которые строка ОБЯЗАТЕЛЬНО проходит на пути к холсту:
`ImageDraw.text` (рисование) и `ImageDraw.textlength` (измерение). Из этого
следует главное свойство: рисуем и меряем мы всегда ОДНУ И ТУ ЖЕ строку, и
разойтись в языке они не могут в принципе. Центрирование, перенос по словам и
сторож `fit` считают по английской ширине автоматически, без правок.

Исключения, где перевод стоит РАНЬШЕ патча (строка приходит целой, а дальше
режется на куски, которые словарём уже не опознать): `wrap`, `box`, `fit`.

Переводится только строка, в которой ЕСТЬ кириллица. Отсюда два следствия:
двойной перевод невозможен (английская строка словарём не ищется), а
кириллица, которой в словаре нет, не исчезает молча — она попадает в `MISS`
и печатается `report()` списком.

Словарь — `fig_strings_en.py`, английское значение каждой строки взято из
замка `tools/lecture-production/glossary-ru-en.md` (части C и D).
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
import re
import sys

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FMB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); WARM = (0xFF, 0xF7, 0xE2); PALE = (0xE6, 0xEE, 0xF4)
GHOST = (0x4A, 0x57, 0x74); DIMTX = (0x8B, 0x9A, 0xAD); GOLDTX = (0xC8, 0x8E, 0x08)
DARKCARD = (0x18, 0x20, 0x3A); GOLDINK = (0x5A, 0x44, 0x08)
GREY_FILL = (0xC9, 0xD1, 0xDB); GREY_TX = (0x55, 0x60, 0x70)
SOFT_GREY = (0xE5, 0xEA, 0xF0)

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)
WARN = []

LANGS = ("ru", "en")
LANG = "ru"
TR = {}
FIGKEYS = {}      # схема → её строки: по ней считаются недошедшие (см. `report`)
MISS = []          # кириллица, которой нет в словаре: дыра, а не пустое место
WHOLE = []         # то же, но пришедшее ЦЕЛОЙ строкой (ключ словаря, не обрывок)
USED = set()       # какие строки словаря дошли до холста
_FONTS = []        # кегли (px) текущей схемы — для замера пола кегля
DREW = []          # (имя файла, размер холста, минимальный кегль px)
CYR = re.compile(r"[А-Яа-яЁё]")


def set_lang(lang):
    """Переключить язык подписей. Трогает ровно перевод и имя выходного файла;
    композиция, цвета и координаты от языка не зависят — а где однажды начнут
    (английская строка шире), это будет видно в самой рисовалке по `LANG`."""
    global LANG, TR
    if lang not in LANGS:
        raise SystemExit(f"--lang принимает {'/'.join(LANGS)}, передано «{lang}»")
    LANG = lang
    if lang == "en":
        from fig_strings_en import STRINGS, BY_FIG
        TR = STRINGS
        FIGKEYS.update(BY_FIG)


def T(s, record="draw"):
    """Строка, какой она выйдет на холст. Русская при `--lang ru`; английская
    из словаря при `--lang en`; при промахе — русская, но с записью в `MISS`.

    `record` различает ТРИ случая, и различает их затем, чтобы список промахов
    был списком строк, а не каскадом их обрывков:
      «whole» — строка пришла целой (`wrap`/`box`/`fit`), это ключ словаря;
      «draw»  — строка пришла на рисование (может быть куском переносa);
      None    — только измерение (`textlength` зовётся по кускам, их не писать).
    """
    if LANG == "ru" or not isinstance(s, str):
        return s
    v = TR.get(s)
    if v is not None:
        USED.add(s)
        return v
    # Промахом считается только КИРИЛЛИЦА: ровно она вышла бы на холст чужим
    # языком. Строка без кириллицы по умолчанию годна как есть (`local`,
    # `.mcp.json`, `tool call`), но ключом быть может — так переписаны числа
    # «1 365» → «1,365»: разделитель тысяч у русского и английского разный, а
    # кириллицы в числе нет, и сторож бы его не заметил.
    if CYR.search(s) and s.strip() and record:
        (WHOLE if record == "whole" else MISS).append(s)
    return s


def sz(ru_px, en_px):
    """Кегль подписи: русский и английский.

    Пол деки задан в ПУНКТАХ (7,5 pt), а кегль схемы живёт в пикселях холста,
    и переводной коэффициент у двух языков разный: `deck_kit.figure` ужимает
    схему целиком, когда ей не хватает высоты, а английский заголовок слайда
    встаёт в две строки чаще русского и высоту отбирает. На n18 английская
    схема из-за этого стоит при 164,5 px·дюйм⁻¹ против русских 157,6, и один
    и тот же кегль в пикселях даёт ей примерно на 0,33 pt меньше (0,31 при
    16 px, 0,33 при 17, 0,34 при 18).

    Отсюда и назначение функции: там, где одного числа пикселей на два языка
    не хватает, числа два. Остаётся ОДИН такой случай — нижняя подпись n18
    (17 px по-русски, 18 по-английски). Русской хватает 17 px — 7,77 pt;
    английской на 17 px не хватило бы (7,44 pt при её собственных 164,5
    px·дюйм⁻¹), а 18 px по-русски разорвали бы строку надвое с висячим
    словом. Подробности и замеры — у самой подписи в make_figures_mcp.py.

    На n16 оба языка сошлись на одном кегле (17 px), и `sz` там больше не
    зовётся — вместо неё стоит число. Пол обеих русских схем поднят над 7,5 pt
    в этой же правке; замер по обоим языкам — qa/kegl-shem-ru.md, прежний
    замер английских — qa/shemy-en.md."""
    return ru_px if LANG == "ru" else en_px


def outname(name):
    """Английская схема — ОТДЕЛЬНЫЙ файл рядом с русским, та же приставка
    `-en`, что у `sem-06-en.pptx`. Русские PNG английский прогон не трогает."""
    return name if LANG == "ru" else re.sub(r"\.png$", "-en.png", name)


# ── Патч двух методов PIL (см. докстринг модуля) ────────────────────────────
_PIL_TEXT = ImageDraw.ImageDraw.text
_PIL_LEN = ImageDraw.ImageDraw.textlength
_PIL_SAVE = Image.Image.save


def _text(self, xy, text, *a, **k):
    if k.get("font") is not None:
        _FONTS.append(k["font"].size)
    return _PIL_TEXT(self, xy, T(text), *a, **k)


def _textlength(self, text, *a, **k):
    return _PIL_LEN(self, T(text, record=None), *a, **k)


def _save(self, fp, *a, **k):
    """Сохранение схемы: имя получает языковую приставку, а сама схема —
    строку в `DREW` с замером пола кегля (на глаз кегль схем мерили дважды и
    дважды ошиблись — см. backup n30)."""
    if isinstance(fp, (str, Path)) and Path(fp).parent == OUT:
        p = OUT / outname(Path(fp).name)
        DREW.append((p.name, self.size, min(_FONTS) if _FONTS else None))
        _FONTS.clear()
        return _PIL_SAVE(self, p, *a, **k)
    return _PIL_SAVE(self, fp, *a, **k)


ImageDraw.ImageDraw.text = _text
ImageDraw.ImageDraw.textlength = _textlength
Image.Image.save = _save

if "--lang" in sys.argv:
    _i = sys.argv.index("--lang")
    set_lang(sys.argv[_i + 1] if _i + 1 < len(sys.argv) else "")


def f(sz, b=False, m=False):
    return ImageFont.truetype((FMB if b else FM) if m else (FB if b else F), sz)


def fit(d, txt, fo, limit, where):
    txt = T(txt, "whole")   # ругаться обязаны на ту строку, которая выйдет на холст
    if d.textlength(txt, font=fo) > limit:
        WARN.append(f"{where}: шире отведённого на "
                    f"{d.textlength(txt, font=fo) - limit:.0f} px — {txt[:56]!r}")


def wrap(d, txt, fo, limit):
    """Перенос по словам: длинная строка на схеме не обрезается и не
    выезжает — она становится двумя. Ширину меряем тем шрифтом, которым
    будем рисовать."""
    out, cur = [], ""
    for wd in T(txt, "whole").split():   # перевод ДО разрезания: куски словарём не ищутся
        probe = (cur + " " + wd).strip()
        if cur and d.textlength(probe, font=fo) > limit:
            out.append(cur); cur = wd
        else:
            cur = probe
    if cur:
        out.append(cur)
    return out


def lines_at(d, x, y, lines, fo, col, lh, center=None):
    for i, ln in enumerate(lines):
        xx = x if center is None else center - d.textlength(ln, font=fo) / 2
        d.text((xx, y + i * lh), ln, font=fo, fill=col)


def clabel(d, cx, y, txt, sz, col=INK, b=False, m=False, where="?", limit=None):
    """Подпись по центру. `limit` — ширина, в которую она обязана уложиться."""
    fo = f(sz, b, m)
    if limit:
        fit(d, txt, fo, limit, where)
    d.text((cx - d.textlength(txt, font=fo) / 2, y), txt, font=fo, fill=col)


def box(d, x, y, w, h, lines, fc, tc=W, sz=32, b=True, m=False, r=12, pad=18,
        outline=None, where="?"):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fc,
                        outline=outline, width=3 if outline else 0)
    fo = f(sz, b, m)
    if isinstance(lines, str):
        lines = T(lines, "whole").split("\n")   # перевод ДО разрезания; EN вправе дать другое число строк
    else:
        # Перевод вправе дать ДРУГОЕ число строк: русская подпись в одну строку
        # по-английски бывает шире коробки, и разбить её — честнее, чем мельчить.
        lines = [x for l in lines for x in T(l, "whole").split("\n")]
    lh = sz + 8
    cy = y + (h - (len(lines) * lh - 8)) // 2
    for i, ln in enumerate(lines):
        fit(d, ln, fo, w - 2 * pad, where)
        d.text((x + (w - d.textlength(ln, font=fo)) / 2, cy + i * lh), ln,
               font=fo, fill=tc)


def dashbox(d, x, y, w, h, col, dash=18, gap=12, width=3, r=10, bg=W):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, outline=col, width=width)
    for sx in range(int(x) + r, int(x + w) - r, dash + gap):
        d.rectangle([sx + dash, y - 1, sx + dash + gap, y + width], fill=bg)
        d.rectangle([sx + dash, y + h - width - 1, sx + dash + gap, y + h + 1], fill=bg)
    for sy in range(int(y) + r, int(y + h) - r, dash + gap):
        d.rectangle([x - 1, sy + dash, x + width, sy + dash + gap], fill=bg)
        d.rectangle([x + w - width - 1, sy + dash, x + w + 1, sy + dash + gap], fill=bg)


def arrow(d, x1, y1, x2, y2, col=MID, wd=5, head=16, dash=False):
    if dash:
        seg, gap = 14, 10
        total = math.hypot(x2 - x1, y2 - y1)
        n = max(int(total // (seg + gap)), 1)
        ux, uy = (x2 - x1) / total, (y2 - y1) / total
        p = 0.0
        while p < total - seg:
            sx, sy = x1 + ux * p, y1 + uy * p
            ex, ey = x1 + ux * min(p + seg, total), y1 + uy * min(p + seg, total)
            d.line([sx, sy, ex, ey], fill=col, width=wd)
            p += seg + gap
    else:
        d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42)),
               (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))],
              fill=col)


def xmark(d, cx, cy, s, col=RED, wd=5):
    d.line([cx - s, cy - s, cx + s, cy + s], fill=col, width=wd)
    d.line([cx - s, cy + s, cx + s, cy - s], fill=col, width=wd)


def check_outline(d, cx, cy, s, col):
    """Незалитая галочка — вопрос задан, не отвечен."""
    d.line([cx - s, cy, cx - s * 0.25, cy + s * 0.7], fill=col, width=max(4, s // 5))
    d.line([cx - s * 0.25, cy + s * 0.7, cx + s, cy - s * 0.6], fill=col, width=max(4, s // 5))


def lock(d, cx, cy, s, col):
    d.rounded_rectangle([cx - s, cy, cx + s, cy + s * 1.35], radius=s // 3, fill=col)
    d.arc([cx - s * 0.62, cy - s * 0.95, cx + s * 0.62, cy + s * 0.35], 180, 360,
          fill=col, width=max(4, s // 4))


def head(d, txt, sz=34, col=DEEP, x=40, y=18):
    d.text((x, y), txt, font=f(sz, True), fill=col)


def save(im, name):
    im.save(OUT / name)               # имя получает языковую приставку в патче `_save`
    print("  ", outname(name), im.size)


def cover_backdrop(w, h, top_frac, bottom_frac):
    """Подложка обложки — продолжение градиента самого слайда (DEEP→MID→LIGHT,
    45°), не своя заливка. Перенесено из sem-05 `make_figures_ramka.py`
    буквально (формула и назначение те же: холст — нижняя полоса слайда)."""
    stops = ((0.0, DEEP), (0.55, MID), (1.0, LIGHT))

    def at(t):
        t = min(max(t, 0.0), 1.0)
        for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
            if t <= p1:
                k = (t - p0) / (p1 - p0)
                return tuple(round(a + (b - a) * k) for a, b in zip(c0, c1))
        return stops[-1][1]

    im = Image.new("RGB", (w, h))
    dd = ImageDraw.Draw(im)
    span = bottom_frac - top_frac
    step = 4
    for px in range(0, w, step):
        for py in range(0, h, step):
            t = (px / w + top_frac + span * py / h) / 2
            dd.rectangle([px, py, px + step - 1, py + step - 1], fill=at(t))
    return im


def report():
    print(f"схемы sem-06 ({LANG}):")
    for nm, size, mn in DREW:
        print(f"   {nm}  {size[0]}×{size[1]} px  пол кегля {mn} px")
    if LANG == "en":
        whole = list(dict.fromkeys(WHOLE))
        rest = [m for m in dict.fromkeys(MISS)
                if not any(m in w for w in whole) and m not in whole]
        if whole or rest:
            print(f"\nНЕТ В СЛОВАРЕ ({len(whole) + len(rest)} строк) — "
                  f"вышли бы на холст по-русски:")
            for m_ in whole + rest:
                print(f"   {m_!r}")
        else:
            print("\nсловарь закрыл все кириллические строки: промахов нет")
        # Считаются ТОЛЬКО строки схем, нарисованных этим прогоном: словарь
        # общий на четыре рисовалки, и чужие строки в нём не промах.
        mine = {k for nm, _s, _m in DREW
                for k in FIGKEYS.get(re.sub(r"-en\.png$", ".png", nm), ())}
        dead = [k for k in mine if k not in USED]
        if dead:
            print(f"\nСТРОКИ СЛОВАРЯ, НЕ ДОШЕДШИЕ ДО ХОЛСТА ({len(dead)}) — "
                  f"опечатка в ключе либо строка снята со схемы:")
            for k_ in dead:
                print(f"   {k_!r}")
    if WARN:
        print("\nПРЕДУПРЕЖДЕНИЯ (текст шире отведённого места):")
        for w_ in dict.fromkeys(WARN):
            print("  ", w_)
    else:
        print("\nпредупреждений нет: весь текст укладывается в отведённые блоки")
