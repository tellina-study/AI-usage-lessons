"""Лекция 5 — Band 6: двенадцать слайдов-практик (issue #212).

Владелец забраковал деку тем, что приёмы работы с ИИ жили только в примерах:
«а где они в слайдах по шагам?». Эта полоса отвечает ровно на этот вопрос —
по одному слайду на приём, и у всех двенадцати одна и та же несущая форма
карточки, которую видно с любого слайда полосы:

    МЕХАНИЗМ   — пронумерованные шаги, по которым приём повторяется;
    АРТЕФАКТ   — моноширинный листинг путей в репозитории;
    КРИТЕРИЙ   — бирюзовая плашка: по чему видно, что сработало;
    ГРАНИЦА    — золотой блок, визуально тяжелее остальных трёх: без него
                 практика противоречит разборам провалов той же лекции;
    ОПОРА      — какую прошлую лекцию приём переиспользует.

Ни один из пяти блоков не выбрасывается. Где текст не влезал, сокращена
формулировка внутри блока — полная версия приходит в заметки докладчика из
slides/*.md через notes_with_sources.

Слайды: s11a s11b (Раздел 1) · s17a (Раздел 2) · s24a s24b s24c (Раздел 3) ·
s30a s31a (Раздел 4) · s38a s38b (Раздел 5) · s45a s45b (Раздел 6).

Palette Ocean LOCKED, motif «Ocean rounded box», Gold ≥1×/слайд.
Хронометраж и методические комментарии в видимом слое запрещены.
Локальные примитивы держатся здесь: общий _helpers.py в это время правит
другой агент.
"""
import math
import re

from _helpers import (
    blank, set_slide_bg, text_box, text_runs, ocean_box, filled_rect,
    circle, chip, connector, icon, slide_title, src, check_point,
    right_arrow, notes_with_sources,
    DEEP, MID, LIGHT, TEAL, SURFACE, WHITE, GOLD, SLATE,
    GOLD_TINT, TEAL_TINT, SOFT_GREY, MID_TINT,
    FONT_BODY, FONT_MONO, SLIDES_DIR,
)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN


# ============================================================
# Геометрия карточки практики — одна на все двенадцать слайдов
# ============================================================
X0 = 0.55            # левый край полосы-подписи
LBL_W = 1.26         # ширина колонки-подписи
GAPX = 0.16
CX = X0 + LBL_W + GAPX          # левый край колонки содержания
RIGHT = 12.80
CW = RIGHT - CX                 # ≈ 10.83
PAD = 0.20
PAD_Y = 0.10
TOP = 0.84
RGAP = 0.07

KIND = {
    "mech": dict(lab=MID,   labc=WHITE, fill=SURFACE,   stroke=LIGHT, pt=1.5),
    "art":  dict(lab=SLATE, labc=WHITE, fill=SURFACE,   stroke=LIGHT, pt=1.5),
    "crit": dict(lab=TEAL,  labc=WHITE, fill=TEAL_TINT, stroke=TEAL,  pt=1.5),
    "edge": dict(lab=GOLD,  labc=DEEP,  fill=GOLD_TINT, stroke=GOLD,  pt=2.5),
}


# ============================================================
# Измерение: сколько места ТЕКСТ реально займёт. Калибровано на первом
# прогоне этой же полосы (150 dpi, DejaVu Sans): ~120 символов на дюйм
# ширины при 10,5 pt обычным и ~112 жирным.
# ============================================================
WARN = []
_TOP = [TOP]
_SID = [""]
_TAIL = [0.0]
_BAND = ["", 0.0]          # подпись текущей полосы и её нижняя граница


def est_lines(text, size, w, *, bold=False):
    k = (114.0 if bold else 122.0) / max(size, 1.0)
    n = 0
    for para in text.split("\n"):
        plain = para.replace("**", "")
        n += max(1, math.ceil(len(plain) / max(1.0, w * k)))
    return n


def est_h(text, size, w, *, bold=False, ls=1.15, extra=0.05):
    return est_lines(text, size, w, bold=bold) * size * ls * 1.09 / 72.0 + extra


def _check(need, given, y, what):
    """Ругаемся в консоль сборки, а не молча обрезаем: переполнение на этих
    слайдах — главный риск, и видеть его надо числом, а не глазами."""
    if need > given + 0.02:
        WARN.append(f"{_SID[0]} {_BAND[0]}: {what} не влезает — надо {need:.2f}\", "
                    f"дано {given:.2f}\"")
    if y + need > _BAND[1] + 0.02 and _BAND[1] > 0:
        WARN.append(f"{_SID[0]} {_BAND[0]}: {what} вылезает за полосу на "
                    f"{y + need - _BAND[1]:.2f}\"")


class Cursor:
    """Полосы карточки укладываются сверху вниз сами: у слайда задаётся
    только высота содержания полосы, вертикальная бухгалтерия — здесь."""

    def __init__(self, top=None):
        self.y = _TOP[0] if top is None else top

    def band(self, slide, kind, label, h):
        x, y, w, hh = row(slide, self.y, h, kind, label)
        self.y += h + RGAP
        return x, y, w, hh

    def text(self, slide, kind, label, text, *, size=10.5, bold=False,
             bold_color=MID, min_h=0.0, pad=0.10):
        ch = max(min_h, est_h(text, size, CW - 2 * PAD, bold=bold) + pad)
        x, y, w, h = self.band(slide, kind, label, ch + 2 * PAD_Y)
        md_box(slide, x, y, w, h, text, size=size, base_bold=bold,
               color=DEEP, bold_color=(DEEP if bold else bold_color),
               line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
        return x, y, w, h

    def crit(self, slide, text, *, size=10.0, label="КРИТЕРИЙ"):
        return self.text(slide, "crit", label, text, size=size,
                         bold_color=TEAL)

    def edge(self, slide, text, *, size=10.0, label="ГРАНИЦА", min_h=0.0):
        return self.text(slide, "edge", label, text, size=size, bold=True,
                         min_h=min_h)


def row(slide, y, h, kind, label):
    """Одна полоса карточки: подпись слева + контейнер содержания справа.
    Возвращает (x, y, w, h) внутренней области содержания."""
    k = KIND[kind]
    ocean_box(slide, X0, y, LBL_W, h, fill=k["lab"], stroke=k["lab"],
              stroke_pt=1.0)
    text_box(slide, x=X0 + 0.05, y=y, w=LBL_W - 0.10, h=h, text=label,
             size=9.5, bold=True, color=k["labc"], align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
    ocean_box(slide, CX, y, CW, h, fill=k["fill"], stroke=k["stroke"],
              stroke_pt=k["pt"])
    _BAND[0] = label
    _BAND[1] = y + h - PAD_Y
    return CX + PAD, y + PAD_Y, CW - 2 * PAD, h - 2 * PAD_Y


# ============================================================
# Текстовые примитивы полосы
# ============================================================
def md_box(slide, x, y, w, h, text, *, size=10.5, color=DEEP, bold_color=MID,
           line_spacing=1.15, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
           font=FONT_BODY, space_before=None, base_bold=False):
    """Текст с разметкой **жирным**: один вызов вместо ручной сборки runs."""
    runs = []
    first_line = True
    for line in text.split("\n"):
        newp = not first_line
        first_line = False
        started = False
        for part in re.split(r'(\*\*.+?\*\*)', line):
            if not part:
                continue
            b = part.startswith("**") and part.endswith("**")
            txt = part[2:-2] if b else part
            cfg = {"text": txt, "size": size,
                   "bold": (True if b else base_bold),
                   "color": (bold_color if b else color)}
            if newp and not started:
                cfg["newpara"] = True
                if space_before is not None:
                    cfg["space_before"] = space_before
            started = True
            runs.append(cfg)
        if not started:
            cfg = {"text": " ", "size": size, "color": color}
            if newp:
                cfg["newpara"] = True
            runs.append(cfg)
    _check(est_h(text, size, w, bold=base_bold, ls=line_spacing), h, y,
           "текст")
    return text_runs(slide, x, y, w, h, runs, align=align, anchor=anchor,
                     line_spacing=line_spacing, font=font)


STEP_IND = 0.34


def steps_h(items, w, size, *, gap=0.07):
    """Сколько места займут пронумерованные шаги — считается до отрисовки,
    чтобы высота полосы бралась из содержания, а не из глазомера."""
    hs = [est_h(t, size, w - STEP_IND) for t in items]
    return sum(hs) + gap * (len(hs) - 1)


def steps(slide, x, y, w, items, *, size=10.5, gap=0.07, num_fill=MID,
          bold_color=MID, start=1, line_spacing=1.15):
    """Пронумерованные шаги: кружок с номером + текст. items = [text, ...]."""
    yy = y
    n = start
    for txt in items:
        h = est_h(txt, size, w - STEP_IND, ls=line_spacing)
        circle(slide, x, yy + 0.015, 0.235, num_fill)
        text_box(slide, x=x, y=yy + 0.015, w=0.235, h=0.235, text=str(n),
                 size=8.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        md_box(slide, x + 0.34, yy, w - 0.34, h, txt, size=size,
               bold_color=bold_color, line_spacing=line_spacing)
        yy += h + gap
        n += 1
    return yy


def mono_fit(lines, w, size, pitch, pad=0.13):
    """Кегль и шаг листинга, ужатые под ширину коробки: длинная строка пути
    не должна вылезать за рамку, а сама рамка — за полосу."""
    longest = max(len(l) for l in lines)
    avail_pt = (w - 2 * pad - 0.08) * 72.0
    if longest * size * 0.615 > avail_pt:
        size = max(6.6, avail_pt / (longest * 0.615))
        pitch = min(pitch, size * 0.0198)
    return size, pitch


def mono_h(lines, w, *, size=8.5, pitch=0.168, pad=0.13):
    size, pitch = mono_fit(lines, w, size, pitch, pad)
    return len(lines) * pitch + 2 * pad


def mono_box(slide, x, y, w, lines, *, size=8.5, pitch=0.168, pad=0.13,
             fill=WHITE, stroke=SOFT_GREY, stroke_pt=1.1, color=DEEP,
             comment_color=SLATE, h=None):
    """Белая коробка с моноширинным листингом артефакта. Комментарии после
    «#» приглушаются, чтобы путь читался первым."""
    size, pitch = mono_fit(lines, w, size, pitch, pad)
    hh = h if h is not None else len(lines) * pitch + 2 * pad
    _check(len(lines) * pitch + 2 * pad, hh, y, "листинг")
    ocean_box(slide, x, y, w, hh, fill=fill, stroke=stroke,
              stroke_pt=stroke_pt, radius_pt=7.0)
    for j, line in enumerate(lines):
        yy = y + pad + j * pitch
        if "#" in line:
            head, tail = line.split("#", 1)
            runs = []
            if head:
                runs.append({"text": head, "size": size, "color": color,
                             "font": FONT_MONO})
            runs.append({"text": "#" + tail, "size": size,
                         "color": comment_color, "font": FONT_MONO})
            text_runs(slide, x + pad, yy, w - 2 * pad, pitch + 0.04, runs,
                      line_spacing=1.0, font=FONT_MONO)
        else:
            text_box(slide, x=x + pad, y=yy, w=w - 2 * pad, h=pitch + 0.04,
                     text=line, size=size, color=color, font=FONT_MONO,
                     line_spacing=1.0)
    return y + hh


def support(slide, y, text, *, h=None, size=10.0):
    """«Опора на пройденное» — тонкая строка под карточкой, легче четырёх
    полос: бирюзовая вертикальная засечка + подпись + одна фраза."""
    if h is None:
        h = max(0.30, est_h(text, size, RIGHT - X0 - 1.90) + 0.04)
    filled_rect(slide, X0, y + 0.02, 0.055, h - 0.04, TEAL)
    text_runs(slide, X0 + 0.20, y, RIGHT - X0 - 0.20, h,
              [{"text": "ОПОРА НА ПРОЙДЕННОЕ   ", "size": 9.0, "bold": True,
                "color": TEAL},
               {"text": text, "size": size, "color": SLATE, "italic": True}],
              anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)
    _TAIL[0] = y + h
    if _TAIL[0] > 7.00:
        WARN.append(f"{_SID[0]} ОПОРА: хвост ниже 7.00\" — {_TAIL[0]:.2f}\"")


def badge_question(sid):
    """Печатный вопрос залу из блока «[Бейдж-пауза]» соответствующего .md.
    Читается на сборке: блок добавляет другой агент, и слайд подхватывает
    его без правки этого файла. Нет блока — нет бейджа."""
    files = list(SLIDES_DIR.glob(f"{sid}-*.md"))
    if not files:
        return ""
    md = files[0].read_text(encoding="utf-8")
    body = md.split("## Speaker notes")[0]
    m = re.search(r'\[Бейдж-пауза\]\s*\n+\*\*(.+?)\*\*', body, re.DOTALL)
    if not m:
        return ""
    q = re.sub(r'\s+', ' ', m.group(1)).strip()
    return re.sub(r'^Вопрос залу\s*[:—-]\s*', '', q)


def badge(slide, sid, y=None, *, h=None, size=11.0):
    """Бейдж с печатным вопросом залу — последний блок перед ссылками."""
    q = badge_question(sid)
    if not q:
        return
    if y is None:
        y = _TAIL[0] + 0.06
    if h is None:
        h = max(0.50, est_h(q, size, RIGHT - X0 - 1.15, bold=True) + 0.10)
    check_point(slide, X0, y, RIGHT - X0, q, h=h, size=size)
    _TAIL[0] = y + h
    if _TAIL[0] > 7.00:
        WARN.append(f"{_SID[0]} БЕЙДЖ: хвост ниже 7.00\" — {_TAIL[0]:.2f}\"")


def head(p, title, *, sid="", size=19, y=0.13, h=None):
    """Заголовок-утверждение: высота считается из длины, и от неё же —
    верх карточки, чтобы двухстрочный заголовок не съезжал на первую полосу."""
    _SID[0] = sid
    _TAIL[0] = 0.0
    s = blank(p)
    set_slide_bg(s, WHITE)
    if h is None:
        h = est_h(title, size, 11.80, bold=True, ls=1.10, extra=0.04)
    slide_title(s, title, size=size, y=y, h=h, w=12.25)
    _TOP[0] = y + h + 0.10
    return s


def tiny(slide, x, y, w, text, *, size=8.6, color=SLATE, align=PP_ALIGN.LEFT,
         h=0.22, bold=False, italic=True):
    text_box(slide, x=x, y=y, w=w, h=h, text=text, size=size, color=color,
             italic=italic, bold=bold, align=align, line_spacing=1.05)


# ============================================================
# s11a — панель-оппонент из субагентов (schema_matrix)
# ============================================================
def s11a(p):
    sid = "s11a"
    s = head(p, "Панель субагентов правит гайд интервью — и ничего "
                "не говорит о продукте", sid=sid, size=18)
    C = Cursor()

    # ── МЕХАНИЗМ ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 1.83)
    steps(s, x, y, w, [
        ("Персона — **отдельный файл-агент со своим контекстным "
               "окном**, а не абзац внутри общего диалога: субагенты не видят "
               "ответов друг друга и не сходятся незаметно к одному голосу."),
        ("Профиль пишется в формате JTBD — работы, ради которой продукт "
               "нанимают: что делал перед тем, как начал искать решение; чем "
               "пользуется сейчас; во что обходится в часах и деньгах; что "
               "попробовал и бросил. Не «Анна, 34, любит удобные интерфейсы»."),
        ("Один и тот же гайд прогоняется через всех персон."),
        ("Смотрят на **две производные**, а не на содержание ответов: "
               "вопрос с одинаковым ответом у всех ничего не различает — "
               "переписать; ответ гипотетическим будущим («я бы этим "
               "пользовался») нарушает правило спрашивать о конкретном "
               "прошлом — переписать."),
    ], size=9.8)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.47)
    mono_box(s, x, y, 4.95, [
        "research/",
        "  personas/            # файл на персону,",
        "    b2b-ops-lead.md    # версионируется",
        "    solo-founder.md",
        "  guide.md             # v1 → v2; в диффе видно,",
        "                       # какой вопрос и по какому сигналу",
    ], h=h)

    # правее — мелкая схема: пять изолированных персон → один правленый гайд
    rx = x + 5.20
    rw = w - 5.20
    pw, pg = 0.58, 0.16
    tot = 5 * pw + 4 * pg
    sx = rx + (rw - tot) / 2.0
    for i in range(5):
        px = sx + i * (pw + pg)
        ocean_box(s, px, y, pw, 0.36, fill=MID_TINT, stroke=LIGHT,
                  stroke_pt=1.0, radius_pt=6.0)
        icon(s, "users", px + (pw - 0.22) / 2, y + 0.07, 0.22, "mid")
        if i < 4:
            connector(s, px + pw, y + 0.18, px + pw + pg, y + 0.18,
                      color=SLATE, width=1.0, dash="dash")
    icon(s, "x", sx + tot / 2 - 0.09, y + 0.09, 0.18, "gold")
    tiny(s, rx, y + 0.40, rw, "не видят ответов друг друга — изоляция есть, "
                              "независимости нет", align=PP_ALIGN.CENTER)
    connector(s, rx + rw / 2, y + 0.64, rx + rw / 2, y + 0.80, color=MID,
              width=2.0, arrow_end=True)
    ocean_box(s, rx + (rw - 3.5) / 2, y + 0.82, 3.5, 0.34, fill=GOLD_TINT,
              stroke=GOLD, stroke_pt=1.5, radius_pt=8.0)
    text_box(s, x=rx + (rw - 3.5) / 2, y=y + 0.82, w=3.5, h=0.34,
             text="наружу выходит только гайд v2", size=10, bold=True,
             color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Доля переписанных вопросов видна диффом · доля вопросов "
           "«одинаковый ответ у всех» падает от версии к версии · пилотное "
           "живое интервью по правленому гайду даёт таймлайн «первая мысль — "
           "почти-решение — отказ — выбор», а не список предпочтений.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "Ни один ответ персоны не идёт в решение и не цитируется как "
           "данные: наружу выходит только правленый гайд. Отдельное окно даёт "
           "изоляцию, но не независимость — веса и распределение те же, "
           "поэтому **пять субагентов дают пять коррелированных выборок, а не "
           "пять человек**. Сверка с реальным опросом: средние "
           "воспроизводятся, разброс схлопывается — отклонение **16 против "
           "31** у живых. Неправильный запуск виден по выводу о продукте.",
           size=10.0, label="ГРАНИЦА")

    support(s, C.y + 0.02,
            "Лекция 3 — субагент как отдельный слот со своей ценой настройки: "
            "для короткого гайда эта цена не окупается.")
    badge(s, sid)
    src(s, X0, 7.04, 11.5,
        "Сверка синтетических ответов с реальным национальным опросом — "
        "Bisbee, Clinton, Dorff, Kenkel, Larson, Political Analysis, 2024")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s11b — поиск по корпусу обращений (process)
# ============================================================
def s11b(p):
    sid = "s11b"
    s = head(p, "Три шага по корпусу обращений — и ни одной гипотезы "
                "без трёх дословных цитат", sid=sid, size=17)
    C = Cursor()

    # ── МЕХАНИЗМ: три шага слева направо ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 1.76)
    cards = [
        ("database", "ИНДЕКСАЦИЯ", MID,
         "Один тикет — один фрагмент с обязательными метаданными: дата, "
         "продукт, сегмент, канал, признак повторного обращения. Без них "
         "корпус — мешок текста: не отфильтровать ни устаревшее, ни "
         "нерелевантное."),
        ("search-check", "ИЗВЛЕЧЕНИЕ", LIGHT,
         "Гибридный поиск — лексический BM25 плюс плотные векторные "
         "представления — с переранжированием. Чисто векторный поиск по "
         "тикетам плохо ловит коды ошибок и номера заказов."),
        ("group", "КЛАСТЕРИЗАЦИЯ", TEAL,
         "Фрагменты группируются в темы боли, к каждому кластеру — двухшаговый "
         "синтез: сначала каждый тикет по отдельности, потом между тикетами. "
         "Пропуск первого шага — потеря 20–40% детали."),
    ]
    cw_ = 3.18
    arr = 0.34
    sx = x + (w - (3 * cw_ + 2 * arr)) / 2.0
    for i, (ic, name, col, body) in enumerate(cards):
        cx_ = sx + i * (cw_ + arr)
        filled_rect(s, cx_, y, cw_, 0.34, col, radius=True, radius_adj=0.14)
        icon(s, ic, cx_ + 0.10, y + 0.06, 0.22, "white")
        text_box(s, x=cx_ + 0.38, y=y, w=cw_ - 0.46, h=0.34,
                 text=f"{i + 1}. {name}", size=10.5, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        md_box(s, cx_ + 0.04, y + 0.40, cw_ - 0.08, h - 0.40, body, size=9.5,
               line_spacing=1.14)
        if i < 2:
            right_arrow(s, cx_ + cw_ + 0.05, y + 0.08, arr - 0.10, 0.20,
                        fill=LIGHT)

    # ── АРТЕФАКТ: одна таблица ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.10)
    tiny(s, x, y, w, "Одна таблица — и в ней гипотеза не существует без "
                     "прослеживаемости до тикета:")
    cols = [("Кластер", 1.60), ("Тикетов", 1.00), ("Цитаты с номером", 2.35),
            ("Гипотеза «вера — тест — дата»", 3.00),
            ("К какому сегменту идти живьём", 2.24)]
    cxx = x
    hy = y + 0.26
    for lab, ww in cols:
        filled_rect(s, cxx, hy, ww, 0.30, MID, radius=True, radius_adj=0.12)
        text_box(s, x=cxx + 0.06, y=hy, w=ww - 0.12, h=0.30, text=lab,
                 size=9.0, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        cxx += ww + 0.06
    ghost = ["тема боли", "N", "#____ · #____ · #____",
             "вера — тест — дата", "сегмент"]
    cxx = x
    for (lab, ww), g in zip(cols, ghost):
        ocean_box(s, cxx, hy + 0.32, ww, 0.30, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.0, radius_pt=6.0)
        text_box(s, x=cxx + 0.06, y=hy + 0.32, w=ww - 0.12, h=0.30, text=g,
                 size=9.0, italic=True, color=SLATE, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        cxx += ww + 0.06

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Каждая гипотеза прослеживается минимум до **трёх дословных цитат "
           "с номером тикета** · кластер без цитаты — артефакт модели, а не "
           "боль клиента, и вычёркивается · дальше уходит только гипотеза с "
           "записанным порогом.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    x, y, w, h = C.band(s, "edge", "ГРАНИЦА", 1.70)
    md_box(s, x, y, w - 2.55, h,
           "Корпус смещён **по построению**, а не по недосмотру: в нём есть "
           "только те, кто дошёл до жалобы. Объём этого не лечит — сто тысяч "
           "тикетов смещены ровно так же, как тысяча, потому что **не бывает "
           "тикета «мне нужно то, чего у вас вообще нет»**. Вопрос «чего у нас "
           "нет» закрывается другим инструментом — интервью с теми, кто "
           "отвалился. И второе: извлечение возвращает **похожие** обращения, "
           "а не важные. Десять тысяч жалоб на опечатку — это по-прежнему одна "
           "опечатка.",
           size=10.5, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)
    # воронка: из всех пользователей до корпуса доходит узкая полоска
    fx = x + w - 2.35
    ocean_box(s, fx, y + 0.02, 2.30, h - 0.04, fill=WHITE, stroke=GOLD,
              stroke_pt=1.2, radius_pt=7.0)
    icon(s, "funnel", fx + 0.12, y + 0.16, 0.30, "gold")
    text_box(s, x=fx + 0.50, y=y + 0.12, w=1.70, h=0.38,
             text="кто дошёл до жалобы", size=9.0, bold=True, color=DEEP,
             line_spacing=1.05)
    filled_rect(s, fx + 0.16, y + 0.60, 1.98, 0.20, LIGHT, radius=True,
                radius_adj=0.35)
    tiny(s, fx + 0.16, y + 0.80, 1.98, "все пользователи", size=8.0)
    filled_rect(s, fx + 0.16, y + 1.00, 0.40, 0.20, GOLD, radius=True,
                radius_adj=0.35)
    tiny(s, fx + 0.60, y + 1.00, 1.55, "корпус обращений", size=8.0,
         color=DEEP, bold=True, italic=False)

    support(s, C.y + 0.02, "Лекция 2 — векторные представления и кластеризация. "
                     "Лекция 3 — поиск с дополнением генерации: метаданные, "
                     "свежесть, гибридное извлечение, «вернул что-то не значит "
                     "вернул правильное».")
    src(s, X0, 7.04, 11.5,
        "Двухшаговый синтез — Тереза Торрес")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s17a — дизайн-система как автоматический гейт (schema_matrix)
# ============================================================
def s17a(p):
    sid = "s17a"
    s = head(p, "Три слоя дизайн-системы — контролем является только третий",
             sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: три слоя, уложенные снизу вверх по общей нижней границе ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.00)
    layers = [
        ("shield-check", "3", "ГЕЙТ В СБОРКЕ", TEAL, 1.00, 0.62,
         "Экран прогоняется движком проверки доступности (axe-core, pa11y, "
         "Lighthouse) с порогом, записанным числом заранее. Нарушение "
         "останавливает сборку. **Ни один из трёх движков не является "
         "ИИ-инструментом, и это часть урока.**"),
        ("component", "2", "СВОИ КОМПОНЕНТЫ", MID, 0.88, 0.50,
         "Генератору подаются собственные компоненты команды, а не общие "
         "шаблоны: меньше переделки — но это **снижение вероятности, не "
         "гарантия**."),
        ("palette", "1", "ТОКЕНЫ", LIGHT, 0.76, 0.50,
         "Машиночитаемый файл, а не картинка в макете: пары «фон/текст» с "
         "посчитанным контрастом, размеры целей нажатия, состояния фокуса."),
    ]
    yy = y
    for ic, num, name, col, frac, bh, body in layers:
        bw = w * frac
        ocean_box(s, x, yy, bw, bh, fill=WHITE, stroke=col,
                  stroke_pt=(2.2 if num == "3" else 1.2), radius_pt=8.0)
        filled_rect(s, x, yy, 2.30, bh, col, radius=True, radius_adj=0.10)
        icon(s, ic, x + 0.14, yy + (bh - 0.26) / 2, 0.26, "white")
        text_box(s, x=x + 0.46, y=yy, w=1.78, h=bh, text=f"{num}. {name}",
                 size=10.0, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.02)
        md_box(s, x + 2.44, yy + 0.04, bw - 2.56, bh - 0.08, body, size=9.5,
               line_spacing=1.13, anchor=MSO_ANCHOR.MIDDLE)
        yy += bh + 0.06

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.33)
    mono_box(s, x, y, 5.15, [
        "design/tokens.json     # контрасты и размеры",
        "                       # посчитаны, а не заявлены",
        "tests/a11y/            # прогон на каждый экран",
        "# + строка в критерии готовности:",
        "#   экран не готов без зелёного гейта",
    ], h=h)
    # две худшие измеренные величины — то, что гейт снимает детерминированно
    gx = x + 5.40
    gw = w - 5.40
    tiny(s, gx, y - 0.02, gw, "Доля экранов, проходящих два худших "
                              "измеренных критерия доступности, — оба "
                              "проверяются машиной:", size=9.0, h=0.34)
    for j, (lab, val) in enumerate([("контраст", 26.8),
                                    ("использование цвета", 19.2)]):
        by = y + 0.44 + j * 0.42
        text_box(s, x=gx, y=by, w=2.05, h=0.22, text=lab, size=9.5,
                 color=DEEP, line_spacing=1.0)
        bar_x, bar_w = gx + 2.15, gw - 2.95
        filled_rect(s, bar_x, by + 0.03, bar_w, 0.17, SOFT_GREY, radius=True,
                    radius_adj=0.35)
        filled_rect(s, bar_x, by + 0.03, bar_w * val / 100.0, 0.17, GOLD,
                    radius=True, radius_adj=0.35)
        text_box(s, x=bar_x + bar_w + 0.08, y=by, w=0.72, h=0.22,
                 text=f"{val:.1f}%".replace(".", ","), size=9.5, bold=True,
                 color=DEEP, line_spacing=1.0)


    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Доля сгенерированных экранов, проходящих гейт **с первого "
           "прогона**, растёт от итерации к итерации · нарушения по контрасту "
           "и использованию цвета уходят к нулю: оба детерминированно "
           "проверяемы машиной и не зависят от формулировки запроса.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    x, y, w, h = C.band(s, "edge", "ГРАНИЦА", 1.18)
    icon(s, "eye-off", x, y + 0.26, 0.34, "gold")
    md_box(s, x + 0.46, y, w - 0.46, h,
           "Гейт ловит только машинно-проверяемое: контраст, подписи, размер "
           "цели нажатия, порядок перехода фокуса. Он **не ловит «понятно ли "
           "это»**: экран может пройти гейт целиком и остаться непонятным, "
           "поэтому приём не заменяет ни обзор по эвристикам, ни тест с 5–8 "
           "живыми людьми — он снимает с обоих то, что дешевле поймать "
           "машиной. И **«попросите генератор сделать доступно» механизмом "
           "контроля не является**: механизм — число, останавливающее сборку.",
           size=10.5, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.13, anchor=MSO_ANCHOR.MIDDLE)

    support(s, C.y + 0.02,
            "Лекция 4 — тест-инвариант как автоматический надзор: та же "
            "конструкция, применённая не к модулям, а к интерфейсу.")
    badge(s, sid)
    src(s, X0, 7.04, 11.5,
        "26,8% и 19,2% соответствия — ACM Web4All, 2026")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s24a — право подняться по лестнице агентности (schema_matrix)
# ============================================================
def s24a(p):
    sid = "s24a"
    s = head(p, "Ступень автономии открывается доказательством — четыре "
                "пункта, которые предъявляют до перехода", size=18, sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: лестница уровней контроля + замок из четырёх пунктов ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.42)
    lw = 4.30
    md_box(s, x, y, lw, 0.46,
           "Релиз версионируется по **уровню контроля**, а не по набору "
           "функций:", size=10.0, line_spacing=1.12)
    rungs = [
        ("в3", "решает сам, с возвратом к человеку при затруднении", TEAL,
         1.00),
        ("в2", "предлагает решение на утверждение человеку", MID, 0.84),
        ("в1", "маршрутизирует обращения", LIGHT, 0.68),
    ]
    ry = y + 0.50
    for lab, txt, col, frac in rungs:
        bw = lw * frac
        filled_rect(s, x, ry, bw, 0.40, col, radius=True, radius_adj=0.14)
        text_box(s, x=x + 0.10, y=ry, w=0.42, h=0.40, text=lab, size=10.5,
                 bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        text_box(s, x=x + 0.56, y=ry, w=bw - 0.64, h=0.40, text=txt, size=9.0,
                 color=WHITE, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.04)
        ry += 0.46
    icon(s, "trending-up", x + lw - 0.32, y + 0.02, 0.28, "gold")
    tiny(s, x, ry + 0.02, lw, "тот же регулятор доверия в инструментах для "
                              "кода: подсказка-завершение → блок кода → "
                              "целый запрос на слияние", size=8.6)

    # замок: четыре пункта-ключа
    kx = x + lw + 0.30
    kw = w - lw - 0.30
    icon(s, "lock", kx, y - 0.02, 0.26, "gold")
    text_box(s, x=kx + 0.34, y=y - 0.02, w=kw - 0.34, h=0.26,
             text="ЧЕМ ОТКРЫВАЕТСЯ СЛЕДУЮЩАЯ СТУПЕНЬ — четыре пункта",
             size=10.0, bold=True, color=DEEP, line_spacing=1.0)
    steps(s, kx, y + 0.30, kw, [
        ("Эталонный набор с кейсами **того самого класса риска**, "
               "который открывает новая ступень, а не общего."),
        ("Порог для этого класса, записанный числом **до** прогона, и "
               "гейт на повторных прогонах — «успешен во всех попытках», а не "
               "«хотя бы в одной»: автоматический режим отвечает каждый раз."),
        ("Строки, добавленные в набор из **реальных отказов предыдущей "
               "ступени**, — и они зелёные."),
        ("**Записанный путь назад:** как функция возвращается на ступень "
               "ниже, за какое время и по чьему решению."),
    ], size=9.8, gap=0.05)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.16)
    mono_box(s, x, y, 5.95, [
        "releases/agency-level.md   # ступень функции, дата подъёма,",
        "                           # кто решил, путь назад",
        "evals/thresholds.yaml      # порог того класса риска,",
        "                           # который открывает ступень",
    ], h=h)
    cx_ = x + 6.20
    ocean_box(s, cx_, y, w - 6.20, h, fill=WHITE, stroke=SLATE, stroke_pt=1.2,
              radius_pt=7.0)
    icon(s, "octagon-alert", cx_ + 0.14, y + (h - 0.30) / 2, 0.30, "slate")
    md_box(s, cx_ + 0.54, y + 0.04, w - 6.80, h - 0.08,
           "**«Оператор давно ничего не правил»** — в этот файл не "
           "записывается: правом на переход не является.",
           size=9.5, color=SLATE, bold_color=DEEP, line_spacing=1.12,
           anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Все четыре пункта предъявлены **до** перехода, а не после · "
           "переход зафиксирован датой и именем решившего · путь назад "
           "проверен, а не описан.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "«Оператор давно ничего не правил» — не доказательство, а "
           "**отсутствие измерения**: если ступень не произвела ни одной "
           "записанной правки, на неё не смотрели, а не отработали "
           "безупречно. Всегда зелёный набор разрешения тоже не даёт — это "
           "насыщение, сломанный измеритель. Дословно: **не тестировали "
           "поведение при высоком контроле — не готовы давать высокую "
           "автономию.** Решение, необратимое по природе — юридически "
           "связывающее предложение, удаление промышленных данных, релиз на "
           "всю аудиторию без отката — моделью не принимается.",
           size=10.0, label="ГРАНИЦА")

    support(s, C.y + 0.02,
            "Лекция 4 — контракт без версии не контракт: ступень, дата и "
            "путь назад лежат в версионируемом файле.")
    src(s, X0, 7.04, 11.5,
        "50+ внедрений, непрерывная поставка ИИ-функций — Реганти и Бадам, "
        "19 августа 2025")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s24b — эталонный набор как исполняемая спецификация (schema_matrix)
# ============================================================
def s24b(p):
    sid = "s24b"
    s = head(p, "Эталонный набор — спецификация, которую исполняет сборка, "
                "а не документ", sid=sid, size=18)
    C = Cursor()

    # ── МЕХАНИЗМ: строка набора + пороги по классам риска ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.02)
    lw = 5.85
    md_box(s, x, y, lw, 0.24,
           "Набор живёт в репозитории как версионируемый файл. Строка — "
           "четыре поля:", size=9.8, line_spacing=1.10)
    mono_box(s, x, y + 0.30, lw, [
        '{"вход": "...",',
        ' "ожидаемый_ответ_или_рубрика": "...",',
        ' "класс_риска": "отказ_по_политике",',
        ' "источник": "инцидент-2026-04-11"}',
    ], size=9.0, pitch=0.162)
    md_box(s, x, y + 1.24, lw, 0.56,
           "**Источник обязателен и обязательно реальный:** начинают с 5–10 "
           "настоящих промышленных примеров — то же «реальное прошлое, а не "
           "правдоподобное», что и в интервью.",
           size=9.5, line_spacing=1.12)

    tx = x + lw + 0.30
    tw = w - lw - 0.30
    text_box(s, x=tx, y=y, w=tw, h=0.24,
             text="ПОРОГИ — числом, заранее, по классам риска", size=10.0,
             bold=True, color=DEEP, line_spacing=1.0)
    thr = [("Рутинный запрос", "не ниже 90%", MID_TINT, LIGHT, DEEP),
           ("Отказ по политике безопасности", "100%, без исключений",
            MID_TINT, LIGHT, DEEP),
           ("Ответ с юридическим последствием", "не через модель",
            TEAL_TINT, TEAL, TEAL)]
    ty = y + 0.28
    for lab, val, fl, st, vc in thr:
        ocean_box(s, tx, ty, tw, 0.38, fill=fl, stroke=st, stroke_pt=1.2,
                  radius_pt=7.0)
        text_box(s, x=tx + 0.14, y=ty, w=tw * 0.56, h=0.38, text=lab,
                 size=9.5, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.04)
        text_box(s, x=tx + tw * 0.58, y=ty, w=tw * 0.40, h=0.38, text=val,
                 size=9.5, bold=True, color=vc, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.RIGHT, line_spacing=1.04)
        ty += 0.42
    tiny(s, tx, ty + 0.02, tw, "последняя строка — не порог, а отказ от "
                               "инструмента: детерминированное правило "
                               "поверх модели", size=8.6)

    # ── АРТЕФАКТ + гейт и замыкание ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.14)
    mono_box(s, x, y, 5.05, [
        "evals/reference.jsonl     # строки набора",
        "evals/thresholds.yaml     # пороги по классам риска",
        "# + строка в гейте «продолжаем / закрываем»",
        "# + строка в критерии готовности",
    ], h=h)
    gx = x + 5.30
    gw = w - 5.30
    icon(s, "git-pull-request-closed", gx, y + 0.02, 0.26, "mid")
    md_box(s, gx + 0.34, y, gw - 0.34, 0.46,
           "**Гейт.** Прогон набора — команда в конвейере сборки, "
           "возвращающая ненулевой код при недоборе порога.",
           size=9.5, line_spacing=1.12)
    icon(s, "repeat", gx, y + 0.52, 0.26, "gold")
    md_box(s, gx + 0.34, y + 0.50, gw - 0.34, 0.48,
           "**Замыкание.** Каждый сбой возвращается строкой с источником "
           "«инцидент».", size=9.5, line_spacing=1.12)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Набор растёт после каждого инцидента — измеримо, по числу строк с "
           "источником «инцидент» · однажды пойманная регрессия не повторяется "
           "молча на следующем релизе.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "**Насыщение** — всегда зелёный набор ничего не измеряет: это "
           "сломанный измеритель, а не гарантия. **Переобучение под набор** — "
           "как только прохождение становится целью команды, набор перестаёт "
           "быть мерой. **Успех хотя бы раз против успеха всегда** — гейт на "
           "среднем проходе не даёт постоянства при повторных запусках. И "
           "зелёный набор формата «вопрос — ответ» не переносится на открытую "
           "генерацию.",
           size=10.0, label="ГРАНИЦА: три режима отказа")

    support(s, C.y + 0.02,
            "Лекция 4 — исполняемая спецификация и гейт прогона: тест, "
            "написанный до кода, переносится с кода на продукт без изменения "
            "конструкции.")
    badge(s, sid)
    src(s, X0, 7.04, 11.5,
        "5–10 реальных промышленных примеров на старте — рекомендация "
        "Anthropic")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s24c — чем исполняется гейт оценок (schema_matrix)
# ============================================================
def s24c(p):
    sid = "s24c"
    s = head(p, "Гейт исполняется тем же конвейером, что и тесты кода",
             sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: три исполнителя, колонки намеренно равны ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.30)
    tools = [
        ("terminal", "promptfoo", "promptfoo eval",
         "Код выхода **100** при падении балла ниже порога — сборка "
         "останавливается тем же механизмом, что и на проваленном тесте."),
        ("repeat-2", "claude plugin eval", "claude plugin eval --threshold",
         "Кейсы из каталога evals/ прогоняются **трижды**, а не один раз: "
         "разброс виден сразу, не только средний балл."),
        ("flask-conical", "DeepEval", "pytest",
         "Запускается тем же прогоном тестов, которым команда уже "
         "пользуется: отдельный шаг заводить не нужно."),
    ]
    cw_ = (w - 2 * 0.24) / 3.0
    for i, (ic, name, cmd, body) in enumerate(tools):
        cx_ = x + i * (cw_ + 0.24)
        ocean_box(s, cx_, y, cw_, 1.58, fill=WHITE, stroke=LIGHT,
                  stroke_pt=1.2, radius_pt=8.0)
        filled_rect(s, cx_, y, cw_, 0.36, MID, radius=True, radius_adj=0.12)
        icon(s, ic, cx_ + 0.12, y + 0.07, 0.22, "white")
        text_box(s, x=cx_ + 0.40, y=y, w=cw_ - 0.48, h=0.36, text=name,
                 size=10.5, bold=True, color=WHITE, font=FONT_MONO,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        mono_box(s, cx_ + 0.10, y + 0.44, cw_ - 0.20, [cmd], size=9.0,
                 pitch=0.19, pad=0.08, stroke=SOFT_GREY)
        md_box(s, cx_ + 0.12, y + 0.86, cw_ - 0.24, 0.64, body, size=9.3,
               line_spacing=1.13)
    ocean_box(s, x, y + 1.70, w, 0.36, fill=MID_TINT, stroke=LIGHT,
              stroke_pt=1.0, radius_pt=7.0)
    md_box(s, x + 0.16, y + 1.71, w - 0.32, 0.34,
           "**Стоит знать заранее:** единого термина для строки набора нет: "
           "goldens, examples, test cases, samples означают одно и то же.",
           size=9.5, line_spacing=1.10, anchor=MSO_ANCHOR.MIDDLE)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.02)
    mono_box(s, x, y, 5.05, [
        "evals/reference.jsonl    # наследуется у набора",
        "evals/thresholds.yaml    # наследуются пороги",
    ], h=h)
    md_box(s, x + 5.30, y, w - 5.30, h,
           "Своего артефакта у приёма нет: добавляется **шаг конвейера**, "
           "который запускает уже существующие два файла.",
           size=9.8, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Гейт **краснеет** на недоборе порога и останавливает слияние, а "
           "не пишет предупреждение в журнал.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА: шкала, где порог выше надёжности измерителя ──
    x, y, w, h = C.band(s, "edge", "ГРАНИЦА", 1.76)
    md_box(s, x, y, w - 3.55, h,
           "**Порог бессмыслен, если он выше надёжности того, чем "
           "измеряется.** Модель-судья согласуется с людьми примерно на 85% — "
           "на уровне, на котором люди согласуются между собой. Значит, гейт "
           "на 95% с таким судьёй измеряет надёжность **судьи**, а не "
           "системы. И число на маленьком наборе без оценки разброса — шум, а "
           "не сигнал.",
           size=10.0, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.13, anchor=MSO_ANCHOR.MIDDLE)
    sx = x + w - 3.35
    sw = 3.20
    bar_y = y + 0.80
    filled_rect(s, sx, bar_y, sw, 0.20, WHITE, stroke=SLATE, stroke_pt=1.0)
    filled_rect(s, sx, bar_y, sw * 0.85, 0.20, MID_TINT)
    for frac, lab, col, above in [(0.85, "надёжность судьи · 85%", MID, True),
                                  (0.95, "порог гейта · 95%", GOLD, False)]:
        mx = sx + sw * frac
        connector(s, mx, bar_y - 0.06, mx, bar_y + 0.26, color=col, width=2.5)
        if above:
            text_box(s, x=sx - 0.10, y=bar_y - 0.32, w=sw * frac + 0.10,
                     h=0.24, text=lab, size=8.6, bold=True, color=col,
                     align=PP_ALIGN.RIGHT, line_spacing=1.0)
        else:
            text_box(s, x=sx, y=bar_y + 0.28, w=sw, h=0.24, text=lab,
                     size=8.6, bold=True, color=col, align=PP_ALIGN.RIGHT,
                     line_spacing=1.0)
    tiny(s, sx, bar_y + 0.54, sw, "порог выше измерителя — измеряется "
                                  "измеритель", size=8.4, align=PP_ALIGN.RIGHT)

    support(s, C.y + 0.02,
            "Лекция 4 — гейт прогона в конвейере: красный шаг блокирует "
            "слияние. Меняется только объект проверки — не код, а ответ.")
    src(s, X0, 7.04, 11.5,
        "promptfoo — код выхода 100 · claude plugin eval — три прогона на "
        "кейс · DeepEval — запуск через pytest")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s30a — пред-регистрация эксперимента (schema_matrix)
# ============================================================
def s30a(p):
    sid = "s30a"
    s = head(p, "Файл коммитится до включения эксперимента — и дальше "
                "только дополняется", sid=sid, size=18)
    C = Cursor()

    # ── МЕХАНИЗМ: поля файла + порядок во времени ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.39)
    lw = 6.05
    md_box(s, x, y, lw, 0.42,
           "Подглядывание, подгонка и множественные сравнения держатся на "
           "одном: что считать успехом, решают **после** первых результатов.",
           size=9.8, line_spacing=1.12)
    ocean_box(s, x, y + 0.48, 2.90, 0.30, fill=GOLD_TINT, stroke=GOLD,
              stroke_pt=1.5, radius_pt=7.0)
    icon(s, "git-commit-horizontal", x + 0.10, y + 0.52, 0.22, "gold")
    text_box(s, x=x + 0.38, y=y + 0.48, w=2.44, h=0.30,
             text="коммит до включения", size=9.5, bold=True, color=DEEP,
             anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    mono_box(s, x, y + 0.82, lw, [
        "oec: конверсия в оплату        # с направлением: растёт",
        "guardrails: [время ответа, доля отписок]",
        "mde: 10% относительных",
        "sample_size: 31 200 на группу  # посчитан, не назначен",
        "unit: пользователь             # не запрос",
        "stopping_rule: ...",
        "decision_metric: oec           # ровно одна",
    ], size=8.8, pitch=0.158)

    rx = x + lw + 0.32
    rw = w - lw - 0.32
    text_box(s, x=rx, y=y, w=rw, h=0.24,
             text="ПОЧЕМУ ЭТО РАБОТАЕТ — порядок во времени",
             size=10.0, bold=True, color=DEEP, line_spacing=1.0)
    ax_y = y + 0.72
    connector(s, rx + 0.10, ax_y, rx + rw - 0.15, ax_y, color=SLATE,
              width=1.6, arrow_end=True)
    circle(s, rx + 0.30, ax_y - 0.10, 0.20, GOLD)
    text_box(s, x=rx + 0.02, y=ax_y - 0.52, w=1.90, h=0.36,
             text="коммит файла", size=9.0, bold=True, color=DEEP,
             align=PP_ALIGN.CENTER, line_spacing=1.04)
    circle(s, rx + rw - 0.85, ax_y - 0.10, 0.20, MID)
    text_box(s, x=rx + rw - 1.75, y=ax_y - 0.52, w=1.80, h=0.36,
             text="первый результат", size=9.0, bold=True, color=MID,
             align=PP_ALIGN.CENTER, line_spacing=1.04)
    connector(s, rx + 0.40, ax_y + 0.16, rx + rw - 0.85, ax_y + 0.16,
              color=GOLD, width=1.6, dash="dash")
    tiny(s, rx, ax_y + 0.26, rw, "правило остановки уже в истории с меткой "
                                 "раньше первого результата — подглядывание и "
                                 "перебор метрик физически невозможны",
         size=9.0, align=PP_ALIGN.CENTER)
    md_box(s, rx, ax_y + 0.86, rw, 0.40,
           "После включения файл **не редактируется** — только дополняется "
           "секцией «решение» с датой.", size=9.8, line_spacing=1.12)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 0.84)
    mono_box(s, x, y, 5.60, [
        "experiments/<имя>/preregistration.md",
        "  # статус, даты, владелец — в заголовке; каталог на работу",
    ], h=h)
    md_box(s, x + 5.85, y, w - 5.85, h,
           "Тот же приём, что и у единицы работы в репозитории: файл с полями "
           "в заголовке, живущий в истории изменений, а не в переписке.",
           size=9.8, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Решение принято по названной заранее метрике · если по другой — "
           "это зафиксировано как **отклонение с обоснованием**, а не тихо.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА: недостижимая выборка ──
    x, y, w, h = C.band(s, "edge", "ГРАНИЦА", 1.48)
    md_box(s, x, y, w - 3.20, h,
           "**Пред-регистрация не делает эксперимент валидным — она делает "
           "невалидность видимой.** Эффекта новизны она не лечит: для него "
           "нужна отдельная контрольная группа. И она не работает там, где "
           "выборки не хватает: честный вывод не «посмотрим на маленькой "
           "выборке», а пересмотр минимально значимого эффекта или "
           "качественный метод — **недостижимая выборка перестаёт быть "
           "источником причинного вывода вообще.**",
           size=10.0, color=DEEP, bold_color=DEEP, base_bold=True,
           line_spacing=1.12, anchor=MSO_ANCHOR.MIDDLE)
    bx = x + w - 3.00
    ocean_box(s, bx, y, 3.00, h, fill=WHITE, stroke=GOLD, stroke_pt=1.2,
              radius_pt=7.0)
    tiny(s, bx, y + 0.06, 3.00, "12+ недель до ответа", size=8.8,
         align=PP_ALIGN.CENTER, color=DEEP, bold=True, italic=False)
    base = y + h - 0.26
    for i, (val, cap, col, hh) in enumerate(
            [(31200, "нужно на группу", MID, 0.46),
             (5000, "есть в неделю", GOLD, 0.46 * 5000 / 31200)]):
        px = bx + 0.30 + i * 1.45
        filled_rect(s, px + 0.25, base - hh, 0.70, hh, col, radius=True,
                    radius_adj=0.08)
        text_box(s, x=px, y=base - hh - 0.22, w=1.20, h=0.20,
                 text=f"{val:,}".replace(",", " "), size=10.0, bold=True,
                 color=col, align=PP_ALIGN.CENTER, line_spacing=1.0)
        tiny(s, px, base + 0.02, 1.20, cap, size=8.2,
             align=PP_ALIGN.CENTER, color=DEEP)

    support(s, C.y + 0.02,
            "Лекция 4 — один файл на единицу работы и тест, написанный до "
            "кода: порог существует раньше результата, который он оценивает.")
    badge(s, sid)
    src(s, X0, 7.04, 11.5,
        "Расчёт мощности 31 200 на группу — иллюстративный")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s31a — петля оценок (process, замкнутый в кольцо)
# ============================================================
def s31a(p):
    sid = "s31a"
    s = head(p, "Петля замыкается не дашбордом, а строкой инцидента, "
                "вернувшейся в набор", sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: кольцо + три шага + порядок слоёв ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.40)
    lw = 4.55
    nodes = [("набор\nоценок", 0.00, 0.00, MID),
             ("развёртывание", 2.55, 0.00, LIGHT),
             ("живой трафик", 2.55, 1.12, TEAL),
             ("инцидент", 0.00, 1.12, SLATE)]
    nw, nh = 1.85, 0.52
    for lab, dx, dy, col in nodes:
        ocean_box(s, x + dx, y + dy, nw, nh, fill=WHITE, stroke=col,
                  stroke_pt=1.6, radius_pt=8.0)
        text_box(s, x=x + dx + 0.06, y=y + dy, w=nw - 0.12, h=nh, text=lab,
                 size=9.5, bold=True, color=col, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.04)
    connector(s, x + nw, y + nh / 2, x + 2.55, y + nh / 2, color=LIGHT,
              width=2.0, arrow_end=True)
    connector(s, x + 2.55 + nw / 2, y + nh, x + 2.55 + nw / 2, y + 1.12,
              color=LIGHT, width=2.0, arrow_end=True)
    connector(s, x + 2.55, y + 1.12 + nh / 2, x + nw, y + 1.12 + nh / 2,
              color=SLATE, width=2.0, arrow_end=True)
    connector(s, x + nw / 2, y + 1.12, x + nw / 2, y + nh, color=GOLD,
              width=4.0, arrow_end=True, arrow_len="lg", arrow_w="lg")
    icon(s, "refresh-cw", x + nw / 2 + 0.10, y + 0.66, 0.26, "gold")
    tiny(s, x, y + 1.70, lw - 0.20, "золотая стрелка и делает петлю петлёй: "
                                    "сбой возвращается отдельной строкой",
         size=8.8, color=DEEP)

    rx = x + lw
    rw = w - lw
    steps(s, rx, y, rw, [
        ("**Оценка до развёртывания** — прогон против курируемого набора: "
         "воспроизводимо, ловит известные регрессии."),
        ("**Оценка на живом трафике** — вскрывает длинный хвост входов, "
         "который не предвидел ни один фиксированный набор."),
        ("**Замыкание** — промышленный сбой возвращается в набор отдельной "
         "строкой, чтобы регрессия не повторилась молча."),
    ], size=9.8, gap=0.06)
    ladder = ["проверки на каждое изменение", "человек и модель-судья",
              "эксперимент на живых пользователях"]
    lwid = (rw - 2 * 0.26) / 3.0
    for i, lab in enumerate(ladder):
        px = rx + i * (lwid + 0.26)
        last = (i == 2)
        ocean_box(s, px, y + 1.38, lwid, 0.42,
                  fill=(GOLD_TINT if last else MID_TINT),
                  stroke=(GOLD if last else LIGHT), stroke_pt=1.2,
                  radius_pt=7.0)
        text_box(s, x=px + 0.06, y=y + 1.38, w=lwid - 0.12, h=0.42, text=lab,
                 size=8.8, bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.04)
        if i < 2:
            right_arrow(s, px + lwid + 0.04, y + 1.51, 0.18, 0.16, fill=LIGHT)
    tiny(s, rx, y + 1.84, rw, "эксперимент на живых пользователях — последняя "
                              "ступень, а не первая: он за оценками, потому "
                              "что дороже", size=8.8, color=DEEP)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.26)
    mono_box(s, x, y, 5.90, [
        "evals/reference.jsonl        # набор, растущий из инцидентов",
        "evals/judge-agreement.jsonl  # журнал согласия судьи",
        "                             # с человеческими метками",
    ], h=h)
    ax = x + 6.15
    aw = w - 6.15
    md_box(s, ax, y, aw, 0.34,
           "Без второго не понять, чему верить. **Митигации судьи:**",
           size=9.5, line_spacing=1.10)
    mit = ["перемешивать порядок ответов", "измерять согласие с метками",
           "сверять с судьёй другого семейства"]
    for i, m in enumerate(mit):
        chip(s, ax, y + 0.40 + i * 0.22, aw - 0.10, 0.20, m, fill=TEAL_TINT,
             stroke=TEAL, color=DEEP, size=8.2, bold=False)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Проверка насыщения: балл упёрся в потолок и перестал различать "
           "версии — набор **сдулся** и требует кейсов сложнее · планка "
           "привязана к цене ошибки через «успешен во всех попытках» · "
           "именованная база: переход на систематическую оценку поднял "
           "пропускную способность исправлений с **3 до 30 в день**.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "Модель-судья держит **80–85% согласия на лёгких категориях и "
           "падает ниже 60% на безопасности** — судья надёжен меньше всего "
           "там, где цена ошибки выше всего. Набор, который всегда зелёный, — "
           "не гарантия качества, а сломанный измеритель, ровно как тест, "
           "проходящий при любом изменении кода. И эксперимент на живых "
           "пользователях оценками **не заменяется**.",
           size=10.0, label="ГРАНИЦА")

    support(s, C.y + 0.02,
            "Лекция 4 — гейт прогона до слияния и петля «сбой — правка — "
            "проверка»: здесь она замкнута на качество ответа.")
    src(s, X0, 7.04, 11.5,
        "Трёхуровневая рамка — Хусейн · согласие судьи 85% / ниже 60% на "
        "безопасности · 3 → 30 исправлений в день — Notion")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s38a — наблюдаемость ИИ-компонента (schema_matrix)
# ============================================================
def s38a(p):
    sid = "s38a"
    s = head(p, "Трасса без версии — не трасса: три части наблюдаемости "
                "ИИ-компонента", sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: три части, каждая со своей мелкой схемой справа ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.55)
    tw_ = w - 3.85
    gx = x + w - 3.70
    steps(s, x, y, tw_, [
        ("**Трасса на каждый ответ с идентификаторами версий.** Промпт → "
         "извлечение → вызовы инструментов → ответ. Обязательны версии "
         "промпта, модели и конфигурации ограничителей: без них на разборе "
         "инцидента нельзя сказать, что изменилось. **Контракт без версии — "
         "не контракт.**"),
        ("**Бюджет ошибок считается на немедленно доступном прокси**, а не на "
         "отложенной истинной метке: правильность ответа часто известна не "
         "сразу. Прокси выбирается **один раз и записывается**, иначе на "
         "первом же инциденте начнётся спор, что считать ошибкой."),
        ("**Порог скорости сжигания калибруется на историческом разбросе этой "
         "же модели**, а не копируется из инфраструктурного норматива. "
         "Вариативность доходит до **15 процентных пунктов** между "
         "одинаковыми прогонами: абсолютный порог либо шумит, либо не "
         "срабатывает на реальном дрейфе вовсе."),
    ], size=9.8, gap=0.06)

    # схема (1): цепочка, в которой подсвечены версии, а не этапы
    chain = ["промпт", "извлечение", "инструменты", "ответ"]
    ccw = (3.70 - 3 * 0.08) / 4.0
    for i, lab in enumerate(chain):
        px = gx + i * (ccw + 0.08)
        ocean_box(s, px, y, ccw, 0.26, fill=WHITE, stroke=SOFT_GREY,
                  stroke_pt=1.0, radius_pt=5.0)
        text_box(s, x=px, y=y, w=ccw, h=0.26, text=lab, size=7.6, color=SLATE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        filled_rect(s, px + 0.10, y + 0.29, ccw - 0.20, 0.20, MID,
                    radius=True, radius_adj=0.30)
        text_box(s, x=px + 0.10, y=y + 0.29, w=ccw - 0.20, h=0.20,
                 text="версия", size=7.4, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
    tiny(s, gx, y + 0.51, 3.70, "подсвечены не этапы, а версии", size=8.2,
         align=PP_ALIGN.CENTER)

    # схема (2): четыре прокси, выбран и записан один
    prox = [("эскалации к человеку", True), ("явное «это не то»", False),
            ("отказ отвечать", False), ("повторные генерации", False)]
    for i, (lab, chosen) in enumerate(prox):
        py = y + 0.80 + i * 0.235
        ocean_box(s, gx, py, 3.70, 0.21,
                  fill=(GOLD_TINT if chosen else WHITE),
                  stroke=(GOLD if chosen else SOFT_GREY),
                  stroke_pt=(1.6 if chosen else 1.0), radius_pt=5.0)
        text_box(s, x=gx + 0.10, y=py, w=3.50, h=0.21,
                 text=(lab + ("   ← выбран один раз и записан" if chosen
                              else "")),
                 size=7.8, bold=chosen, color=(DEEP if chosen else SLATE),
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)

    # схема (3): порог внутри собственного разброса модели
    sy = y + 1.78
    filled_rect(s, gx, sy, 3.70, 0.22, WHITE, stroke=SLATE, stroke_pt=1.0)
    filled_rect(s, gx + 0.95, sy, 1.30, 0.22, TEAL_TINT)
    connector(s, gx + 2.25, sy - 0.05, gx + 2.25, sy + 0.27, color=GOLD,
              width=2.5)
    tiny(s, gx, sy + 0.26, 2.20, "собственный разброс этой модели", size=7.8,
         align=PP_ALIGN.CENTER)
    tiny(s, gx + 2.28, sy + 0.26, 1.42, "порог — внутри него", size=7.8,
         color=DEEP, bold=True, italic=False)

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.45)
    mono_box(s, x, y, 6.55, [
        "runbook-ai-quality.md",
        "  # «качество поехало» → откатить версию промпта →",
        "  # поднять порог эскалации → включить строгий",
        "  # ограничитель → кого будить",
        "# + дашборд на выбранном прокси",
        "# + запись «какой разброс нормален»: дата калибровки",
    ], h=h, size=8.6, pitch=0.16)
    md_box(s, x + 6.80, y, w - 6.80, h,
           "Регламент — не описание намерения, а последовательность действий "
           "с именами: **что откатить, что поднять, кого будить**.",
           size=9.8, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Проверяется не декларацией, а **плановым учением**: алерт "
           "срабатывает в заявленное окно · дежурный находит нужный раздел "
           "регламента · откат укладывается в заявленное время.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "Трассы по построению уходят во внешний сервис — **регулируемые "
           "данные туда нельзя** без редактирования на входе или "
           "развёртывания у себя. Прокси коррелирует с качеством, но **не "
           "равен ему**: путать частоту эскалаций с точностью в отчёте — "
           "способ обмануть себя. Калибровка **стареет вместе с моделью**, и "
           "незаверсионированный порог даёт то же ложное чувство "
           "защищённости, что незаверсионированный ограничитель.",
           size=10.0, label="ГРАНИЦА: тройная")

    support(s, C.y + 0.02,
            "Лекция 4 — слой логирования: вопрос не «логировать ли», а какая "
            "гранулярность соразмерна цене ошибки.")
    src(s, X0, 7.04, 11.5,
        "Вариация до 15 процентных пунктов между технически одинаковыми "
        "прогонами — Eval4NLP, 2025")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s38b — плановое учение на runbook (process)
# ============================================================
def s38b(p):
    sid = "s38b"
    s = head(p, "Четыре времени, измеренные на учении, — а не заявленные "
                "в регламенте", sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: чем вызывают деградацию + четыре засечки ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.48)
    md_box(s, x, y, w, 0.26,
           "Раз в несколько недель — запланированный прогон. Деградация "
           "вызывается искусственно, одним из трёх способов:",
           size=10.0, line_spacing=1.10)
    ways = ["подменить версию промпта на заведомо худшую на теневом трафике",
            "опустить порог ограничителя", "эмулировать всплеск отказов"]
    wwid = [4.45, 2.85, 2.85]
    wx = x
    for lab, ww in zip(ways, wwid):
        ocean_box(s, wx, y + 0.32, ww, 0.34, fill=MID_TINT, stroke=LIGHT,
                  stroke_pt=1.2, radius_pt=7.0)
        text_box(s, x=wx + 0.10, y=y + 0.32, w=ww - 0.20, h=0.34, text=lab,
                 size=9.0, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                 align=PP_ALIGN.CENTER, line_spacing=1.02)
        wx += ww + 0.12

    ty = y + 0.92
    text_box(s, x=x, y=ty - 0.06, w=w - 0.46, h=0.24,
             text="И замеряются четыре времени — поля пустые: число "
                  "берётся с учения, а не из регламента",
             size=10.0, bold=True, color=DEEP, line_spacing=1.0)
    marks = ["до срабатывания алерта",
             "до открытия регламента дежурным",
             "до срабатывания размыкателя",
             "до завершённого отката"]
    mw = (w - 3 * 0.16) / 4.0
    line_y = ty + 0.56
    connector(s, x, line_y, x + w, line_y, color=SLATE, width=1.6,
              arrow_end=True)
    for i, lab in enumerate(marks):
        px = x + i * (mw + 0.16)
        circle(s, px + mw / 2 - 0.13, line_y - 0.13, 0.26, MID)
        text_box(s, x=px + mw / 2 - 0.13, y=line_y - 0.13, w=0.26, h=0.26,
                 text=str(i + 1), size=8.5, bold=True, color=WHITE,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
        text_box(s, x=px, y=line_y - 0.40, w=mw, h=0.28, text=lab, size=8.6,
                 color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.BOTTOM,
                 line_spacing=1.04)
        ocean_box(s, px + mw / 2 - 0.55, line_y + 0.22, 1.10, 0.28,
                  fill=WHITE, stroke=GOLD, stroke_pt=1.4, radius_pt=6.0)
        text_box(s, x=px + mw / 2 - 0.55, y=line_y + 0.22, w=1.10, h=0.28,
                 text="___", size=10, bold=True, color=GOLD,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.0)
    icon(s, "timer", x + w - 0.30, ty + 0.02, 0.26, "gold")

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.16)
    mono_box(s, x, y, 6.20, [
        "ops/drills/<дата>-<сценарий>.md",
        "  # запись в формате разбора инцидента; дата в имени",
        "  # несущая: по каталогу видно, когда учение было",
        "# + дифф самого runbook-ai-quality.md",
    ], h=h)
    icon(s, "file-diff", x + 6.45, y + (h - 0.30) / 2, 0.30, "gold")
    md_box(s, x + 6.88, y, w - 6.88, h,
           "**Дифф регламента важнее записи:** правка и есть доказательство, "
           "что учение чему-то научило.",
           size=9.8, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Все четыре времени **измерены, а не заявлены** · учение, не "
           "давшее ни одной правки регламента, было слишком лёгким — тот же "
           "диагноз, что у сдувшегося набора оценок: измеритель, который "
           "всегда зелёный, ничего не измеряет.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "Учение проверяет только **известный** класс отказа. Тихий дрейф "
           "по определению не воспроизводится по кнопке — его признак именно "
           "в том, что ничего явно не ломается, — поэтому учение дополняет, а "
           "не заменяет мониторинг по сегментам и канал качественных сигналов "
           "от пользователей. **Если единственный механизм обнаружения — "
           "учение раз в квартал, это тот же дрейф с более длинным окном, "
           "только названный процессом.**",
           size=10.0, label="ГРАНИЦА", min_h=1.25)

    support(s, C.y + 0.02,
            "Лекция 4 — гейт прогона: проверка существует, только если её "
            "кто-то запускает и она умеет краснеть. Здесь запускают руками.")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s45a — стоимость на запрос из токенов (schema_matrix)
# ============================================================
def s45a(p):
    sid = "s45a"
    s = head(p, "Четыре множителя — и ни один из них не новый", sid=sid)
    C = Cursor()

    # ── МЕХАНИЗМ: формула плашками + что стоит за каждым множителем ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.42)
    text_box(s, x=x, y=y - 0.02, w=w, h=0.24,
             text="Стоимость одного взаимодействия:", size=10.0, bold=True,
             color=DEEP, line_spacing=1.0)
    parts = [("токены входа × цена входа\n+ токены выхода × цена выхода",
              MID, 4.30),
             ("среднее число\nшагов агента", LIGHT, 2.35),
             ("коэффициент\nповторных попыток", TEAL, 2.55)]
    fx = x
    fy = y + 0.26
    for i, (lab, col, ww) in enumerate(parts):
        ocean_box(s, fx, fy, ww, 0.60, fill=WHITE, stroke=col, stroke_pt=1.8,
                  radius_pt=8.0)
        text_box(s, x=fx + 0.08, y=fy, w=ww - 0.16, h=0.60, text=lab,
                 size=9.8, bold=True, color=col, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.08)
        fx += ww
        if i < 2:
            text_box(s, x=fx, y=fy, w=0.34, h=0.60, text="×", size=15,
                     bold=True, color=SLATE, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
            fx += 0.34
    icon(s, "calculator", x + w - 0.32, fy + 0.16, 0.28, "gold")

    text_box(s, x=x, y=y + 0.94, w=w, h=0.22,
             text="ЧТО СТОИТ ЗА КАЖДЫМ МНОЖИТЕЛЕМ", size=9.6, bold=True,
             color=DEEP, line_spacing=1.0)
    bullets = [
        ("**Длина в токенах зависит от языка.** Русскоязычный текст на ту же "
         "мысль даёт заметно больше токенов, чем англоязычный: продукт на "
         "русском платит за один и тот же смысл больше, и разница не "
         "исчезает от улучшения формулировки запроса."),
        ("**Токены рассуждения невидимы в ответе, но оплачиваются как "
         "выход** и в агентном сценарии часто составляют основную статью "
         "расхода. Дашборд, считающий только видимый ответ, занижает "
         "реальную стоимость."),
        ("**Кэширование входа меняет знаменатель:** повторяющийся системный "
         "промпт читается из кэша дешевле, чем пишется заново, и порог "
         "окупаемости кэша считают явно, а не принимают на веру."),
    ]
    bw = (w - 2 * 0.20) / 3.0
    for i, b in enumerate(bullets):
        px = x + i * (bw + 0.20)
        if i == 1:
            icon(s, "eye-off", px, y + 1.20, 0.22, "gold")
            md_box(s, px + 0.30, y + 1.18, bw - 0.30, 1.04, b, size=9.3,
                   line_spacing=1.13)
        else:
            md_box(s, px, y + 1.18, bw, 1.04, b, size=9.3, line_spacing=1.13)

    # ── АРТЕФАКТ: два файла одного решения в одном листинге + дашборд ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.64)
    mono_box(s, x, y, 6.30, [
        "pilots/<имя-пилота>/",
        "  unit-cost.md   # расчёт на единицу взаимодействия;",
        "                 # допущения явно: число шагов агента,",
        "                 # доля повторных попыток, средняя длина",
        "                 # ответа; рядом — ценность на запрос",
        "  go-kill.md     # критерий остановки пилота",
    ], h=h, size=8.6, pitch=0.168)
    dx = x + 6.55
    dw = w - 6.55
    tiny(s, dx, y - 0.02, dw, "Дашборд «стоимость на запрос по дням» — "
                              "не файл в репозитории:", size=8.8, h=0.30)
    cx0, cy0 = dx + 0.10, y + 0.30
    cwid, chgt = dw - 0.30, 0.86
    ocean_box(s, cx0, cy0, cwid, chgt, fill=WHITE, stroke=SOFT_GREY,
              stroke_pt=1.0, radius_pt=6.0)
    pts = [0.14, 0.26, 0.40, 0.58, 0.80]
    for i in range(len(pts) - 1):
        connector(s, cx0 + 0.18 + i * (cwid - 0.40) / 4,
                  cy0 + chgt - 0.10 - pts[i] * (chgt - 0.20),
                  cx0 + 0.18 + (i + 1) * (cwid - 0.40) / 4,
                  cy0 + chgt - 0.10 - pts[i + 1] * (chgt - 0.20),
                  color=MID, width=2.0)
    connector(s, cx0 + 0.14, cy0 + chgt - 0.10 - 0.62 * (chgt - 0.20),
              cx0 + cwid - 0.14, cy0 + chgt - 0.10 - 0.62 * (chgt - 0.20),
              color=TEAL, width=1.6, dash="dash")
    circle(s, cx0 + 0.18 + 3.1 * (cwid - 0.40) / 4 - 0.07,
           cy0 + chgt - 0.10 - 0.62 * (chgt - 0.20) - 0.07, 0.14, GOLD)
    tiny(s, dx, y + 1.22, dw, "синим — стоимость на запрос, бирюзовым — "
                              "ценность; золотая точка — день, когда они "
                              "сошлись", size=8.0, h=0.32)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Тренд считается по **собственному** паттерну использования, а не "
           "по чужому · рост средней длины ответа или числа шагов агента "
           "виден на дашборде **до** квартального счёта, а не после.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "**Падение цены токена не гарантирует падения расхода** — команды "
           "закономерно отвечают на удешевление увеличением числа шагов, и "
           "бремя доказательства лежит на утверждении «подешевеет само». "
           "**Стоимость на запрос — метрика-ограничитель, а не цель "
           "оптимизации:** оптимизировать её означает получить короткие и "
           "бесполезные ответы. И **сравнивать нужно с базовой линией без "
           "ИИ**: сколько стоил тот же результат человеком. Без этого "
           "знаменателя получается не юнит-экономика, а учёт расходов.",
           size=10.0, label="ГРАНИЦА: три пункта")

    support(s, C.y + 0.02,
            "Лекция 2 — токенизация, зависимость длины от языка, токены "
            "рассуждения, кэширование входа — переиспользованы прямо.")
    notes_with_sources(s, sid)
    return s


# ============================================================
# s45b — финансовый критерий до пилота (schema_matrix)
# ============================================================
def s45b(p):
    sid = "s45b"
    s = head(p, "Критерий записан до пилота — иначе это объяснение "
                "результата, а не критерий", sid=sid, size=17)
    C = Cursor()

    # ── МЕХАНИЗМ: одна заполненная форма + четыре проверки годности ──
    x, y, w, h = C.band(s, "mech", "МЕХАНИЗМ", 2.49)
    fw = 5.85
    ocean_box(s, x, y, fw, 0.32, fill=GOLD_TINT, stroke=GOLD, stroke_pt=1.5,
              radius_pt=7.0)
    icon(s, "calendar-clock", x + 0.10, y + 0.05, 0.22, "gold")
    text_box(s, x=x + 0.38, y=y, w=fw - 0.48, h=0.32,
             text="дата записи и имя записавшего — проверяются первыми",
             size=9.3, bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.0)
    ocean_box(s, x, y + 0.38, fw, 1.40, fill=WHITE, stroke=SOFT_GREY,
              stroke_pt=1.2, radius_pt=8.0)
    text_runs(s, x + 0.16, y + 0.46, fw - 0.32, 1.24, [
        {"text": "«Мы верим, что ИИ-разбор обращений ", "size": 10.0,
         "color": DEEP},
        {"text": "снизит стоимость на обращение с X₽ до Y₽", "size": 10.0,
         "bold": True, "color": MID},
        {"text": " при не-ухудшении удовлетворённости клиента ниже порога ",
         "size": 10.0, "color": DEEP},
        {"text": "Z", "size": 10.0, "bold": True, "color": TEAL},
        {"text": " и доле эскалаций не выше ", "size": 10.0, "color": DEEP},
        {"text": "W", "size": 10.0, "bold": True, "color": TEAL},
        {"text": "; проверим на ", "size": 10.0, "color": DEEP},
        {"text": "N обращениях за M недель", "size": 10.0, "bold": True,
         "color": LIGHT},
        {"text": "; владелец — ", "size": 10.0, "color": DEEP},
        {"text": "конкретный человек, отслеживающий это еженедельно",
         "size": 10.0, "bold": True, "color": GOLD},
        {"text": "».", "size": 10.0, "color": DEEP},
    ], line_spacing=1.16)
    tiny(s, x, y + 1.84, fw, "одна фраза несёт сразу четыре аппарата: "
                             "оптимизируемая величина · ограничители · объём "
                             "и срок · владелец", size=8.8, color=DEEP)

    kx = x + fw + 0.30
    kw = w - fw - 0.30
    icon(s, "clipboard-check", kx, y - 0.02, 0.24, "teal")
    text_box(s, x=kx + 0.32, y=y - 0.02, w=kw - 0.32, h=0.24,
             text="ЧЕТЫРЕ ПРОВЕРКИ ГОДНОСТИ — все до старта", size=10.0,
             bold=True, color=DEEP, line_spacing=1.0)
    checks = [
        ("**X₽ измерена на собственном процессе**, а не взята из обещания "
         "поставщика: чужая цифра описывает чужой процесс."),
        ("**У каждой величины есть единица и направление** («снизить с X₽ до "
         "Y₽»), а не одно намерение."),
        ("**Назван владелец** — человек с недельным ритмом: критерий без "
         "имени не проверяет никто."),
        ("**Существует исход «закрываем»**: гейт ставится ровно для того, "
         "чтобы отличать «данные сказали нет» от «мы устали»."),
    ]
    yy = y + 0.30
    for i, txt in enumerate(checks, start=1):
        hh = est_h(txt, 9.3, kw - 0.32)
        ocean_box(s, kx, yy + 0.02, 0.22, 0.22, fill=WHITE, stroke=TEAL,
                  stroke_pt=1.4, radius_pt=3.0)
        text_box(s, x=kx, y=yy + 0.02, w=0.22, h=0.22, text=str(i), size=8.0,
                 bold=True, color=TEAL, align=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
        md_box(s, kx + 0.32, yy, kw - 0.32, hh, txt, size=9.3,
               line_spacing=1.12)
        yy += hh + 0.05

    # ── АРТЕФАКТ ──
    x, y, w, h = C.band(s, "art", "АРТЕФАКТ", 1.33)
    mono_box(s, x, y, 6.10, [
        "pilots/<имя-пилота>/go-kill.md",
        "  # дата записи и имя записавшего",
        "  # X₽ — измерено на своём процессе",
        "  # Y₽, Z, W — единица и направление",
        "  # N обращений, M недель; владелец, ритм — еженедельно",
    ], h=h, size=8.6, pitch=0.168)
    icon(s, "door-open", x + 6.35, y + (h - 0.30) / 2, 0.30, "gold")
    md_box(s, x + 6.78, y, w - 6.78, h,
           "Тот же каталог пилота, что и у расчёта стоимости: расчёт и "
           "критерий остановки — **два файла одного решения**, а не два "
           "разных хозяйства.",
           size=9.8, line_spacing=1.14, anchor=MSO_ANCHOR.MIDDLE)

    # ── КРИТЕРИЙ ──
    C.crit(s,
           "Решение на гейте принято **против записанного** — с датой и "
           "именем, проверяемыми первыми.",
           size=10.0, label="КРИТЕРИЙ")

    # ── ГРАНИЦА ──
    C.edge(s,
           "**Если числа порога появились или изменились после включения "
           "пилота — это уже не критерий, а объяснение результата:** решение "
           "принято, а формулировка подогнана под него. Критерий без "
           "названного владельца не проверяет никто, а сравнение с отраслевым "
           "обещанием вместо собственной базовой линии превращает "
           "юнит-экономику в учёт расходов. Отсутствие этой конкретики — не "
           "«забыли посчитать окупаемость», а **отсутствие линейки, которой "
           "её измеряют**: по замеру таких компаний **60%**.",
           size=10.0, label="ГРАНИЦА")

    support(s, C.y + 0.02,
            "Лекция 4 — исполняемая спецификация: порог существует раньше "
            "результата. Тот же приём, применённый к решению финансировать.")
    src(s, X0, 7.04, 11.5,
        "60% компаний не отслеживают ни одного финансового показателя, "
        "привязанного к ценности ИИ — BCG AI Radar, январь 2025 (n=1803)")
    notes_with_sources(s, sid)
    return s


BUILDERS = [s11a, s11b, s17a, s24a, s24b, s24c, s30a, s31a, s38a, s38b,
            s45a, s45b]
