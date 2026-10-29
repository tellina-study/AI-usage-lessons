# -*- coding: utf-8 -*-
"""АРХИТЕКТУРА `arhitektura:` — устройство модели с разбором ВНУТРИ боксов.

Владелец курса, разбор деки Лекции 8: «не хватает схем/архитектур работы
моделей с комментариями». Разбор образцов
(`library/lectures/lec-08/rework-v5/PERENOS-PRIYOMOV.md` §2.11) назвал, чего
именно не хватает: не схемы — схемы есть, — а того, что комментарий стоит
ВНУТРИ блока, а не абзацем под рисунком. В образце `image/s08` три бокса в
ряд, и внутри каждого не ярлык, а три строки по существу: «Сжатие:
изображение 1024×1024 сжимается в латент 128×128×16. Потеря: восстановление
на 4 каналах даёт 25,12 дБ против 28,62 дБ на 16».

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ — и чем отличается от схемы рядами, с которой её
легко спутать. `scheme.py` утверждает ПОРЯДОК: сначала одно, потом другое,
и стрелка там несущая. Эта форма утверждает УСТРОЙСТВО: из чего модель
состоит, какую работу делает каждая часть, где у неё узкое место и что
теряется на переходе. Стрелки здесь есть, но они не главное: убрать из
боксов разбор — и останется та же схема рядами, для которой уже есть свой
модуль. Поэтому блок БЕЗ `lines` называется `[архитектура]`, а не рисуется:
пустой бокс превращает эту форму в чужую.

Контракт фронтматтера:

    arhitektura:
      blocks:
        - head: "Текстовый кодировщик"
          role: "вход"
          lines:
            - "переводит слова в векторы"
            - "чужая замороженная модель, своей не учат"
        - head: "Сеть расшумления"
          role: "работа"
          lines:
            - "от 1 до 50 проходов"
            - "работает в латентном пространстве, не с пикселями"
        - head: "Автокодировщик"
          role: "выход · узкое место"
          uzkoe: true
          lines:
            - "изображение 1024×1024 сжимается в латент 128×128×16"
            - "восстановление на 4 каналах даёт 25,12 дБ против 28,62 на 16"
      vynoska:
        at: 2                 # НОМЕР БЛОКА С НУЛЯ: 2 — это третий блок
        text: "размытое декодировщиком ДО генерации не вернётся никогда"

ПРЕДЕЛ «ЧЕТЫРЕ КЛЕТКИ В РЯДУ» ДЕРЖИТСЯ И ЗДЕСЬ. Он из правила курса, а не из
вёрстки (владелец, 2026-10-08: «не надо вот этот длинный пайплайн»), и
форма, у которой в боксах ещё и разбор, перебирает его раньше всех прочих:
пятый бокс на той же ширине оставляет под строку разбора 2,3 дюйма. Поэтому
пятый блок НАЗЫВАЕТСЯ, а не ужимается кеглем. Нижняя граница тоже есть:
один бокс — не устройство, а плашка, и для неё есть `plates.py`.

ЗОЛОТО ЗДЕСЬ — ЗАЛИВКА, А НЕ ТЕКСТ, и это не вкус. У нас светлый лист, и
`#F0AB00` текстом на белом даёт 1,99 : 1 при пороге 3,0 — замер
`contrast.py`, тот самый, что поймал 60 кадров Лекции 7. Поэтому узкое место
носит золотую ОБВОДКУ (толще обычной) и ярлык роли на золотой ЗАЛИВКЕ с
тёмным текстом поверх (6,85 : 1). Золотой подписи в этой форме нет ни одной
и быть не может.

УЗКОЕ МЕСТО ОДНО. Два бокса с `uzkoe: true` — это уже не узкое место, а два
выделенных блока, то есть выделение, которое ничего не выделяет. Называется
`[архитектура]`.
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, TEAL_TINT

# Ключи, которые ядро ДЕЙСТВИТЕЛЬНО читает. Перечни закрытые по той же
# причине, что у `scheme.SCHEME_KEYS`: ключ, который молча выбрасывают, хуже
# отсутствующего — автор считает кадр починенным, а на экране не изменилось
# ничего.
ARH_KEYS = {"blocks", "vynoska"}
BLOCK_KEYS = {"head", "role", "lines", "uzkoe"}
VYN_KEYS = {"at", "text"}


@dataclass(frozen=True)
class ArhStyle:
    pad: float = 0.14              # поле внутри бокса
    gap: float = 0.10              # просвет бокс — стрелка
    arrow_w: float = 0.30
    arrow_h: float = 0.16
    role_h: float = 0.28           # полоса ярлыка роли
    role_pt: float = 12.0          # пол видимого слоя, см. `floor.py`
    role_gap: float = 0.10
    head_hi: float = 16.0
    head_lo: float = 12.0          # пол видимого слоя, см. `floor.py`
    head_rows: int = 2
    head_ls: float = 1.10
    head_gap: float = 0.10
    line_hi: float = 13.5
    line_lo: float = 12.0          # пол видимого слоя, см. `floor.py`
    line_rows: int = 3             # строк переноса на ОДНУ строку разбора
    line_ls: float = 1.14
    line_sb: float = 4.0           # отбивка между строками разбора, пунктов
    box_min_h: float = 1.20
    vyn_gap: float = 0.06          # от низа боксов до точки указателя
    vyn_stem: float = 0.30         # длина отвеса указателя
    vyn_rule: float = 0.024        # толщина линии указателя
    vyn_dot: float = 0.13
    vyn_pt: float = 13.0
    vyn_ls: float = 1.16
    vyn_pad: float = 0.13          # поле внутри плашки выноски
    uzkoe_pt: float = 2.5          # толщина золотой обводки узкого места
    max_blocks: int = 4            # владелец: «не надо длинный пайплайн»
    min_blocks: int = 2
    max_lines: int = 4             # строк разбора в одном боксе
    min_box_w: float = 1.70        # уже этого разбор внутри не читается


DEFAULT = ArhStyle()


def _unknown(sid, got, known, where):
    extra = [k for k in got if k not in known]
    if extra:
        report.warn(
            f"[архитектура] {sid}: {where} — ключ"
            f"{'и' if len(extra) > 1 else ''} "
            + ", ".join(f"`{k}`" for k in sorted(extra))
            + " ядро не читает, и на кадре он не скажется ничем")


def arhitektura_of(sl, st=DEFAULT):
    """Поле `arhitektura` → разобранное устройство или None.

    Чужая форма поля не роняет сборку: она называется `[архитектура]`, и
    кадр собирается без схемы — тот же договор, что у `figure_of` и
    `scheme_of`."""
    raw = sl.meta.get("arhitektura")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[архитектура] {sl.sid}: поле `arhitektura` — "
                    f"{type(raw).__name__}, а должно быть blocks/vynoska")
        return None
    _unknown(sl.sid, raw, ARH_KEYS, "в `arhitektura`")
    bb = raw.get("blocks")
    if not isinstance(bb, list) or not bb:
        report.warn(f"[архитектура] {sl.sid}: в `arhitektura` нет `blocks`")
        return None
    blocks = []
    for i, b in enumerate(bb, 1):
        if not isinstance(b, dict):
            report.warn(f"[архитектура] {sl.sid}: блок {i} не "
                        "head/role/lines")
            continue
        _unknown(sl.sid, b, BLOCK_KEYS, f"в блоке «{b.get('head') or i}»")
        head = str(b.get("head") or "").strip()
        lines = [str(x).strip() for x in (b.get("lines") or [])
                 if str(x).strip()]
        if not head:
            report.warn(f"[архитектура] {sl.sid}: у блока {i} нет `head` — "
                        "безымянная часть устройства ничего не называет")
            continue
        blocks.append({"head": head,
                       "role": str(b.get("role") or "").strip(),
                       "lines": lines,
                       "uzkoe": bool(b.get("uzkoe"))})
    if not blocks:
        return None
    vyn = None
    vr = raw.get("vynoska")
    if isinstance(vr, dict):
        _unknown(sl.sid, vr, VYN_KEYS, "в `vynoska`")
        txt = str(vr.get("text") or "").strip()
        at = vr.get("at")
        if txt:
            try:
                at = int(at)
            except (TypeError, ValueError):
                report.warn(
                    f"[архитектура] {sl.sid}: у выноски не названо `at` — "
                    "номер блока, к которому идёт указатель (с нуля). "
                    "Указатель, не привязанный к блоку, — просто линия")
                at = None
            if at is not None:
                vyn = {"at": at, "text": txt}
    elif vr not in (None, "", [], {}):
        report.warn(f"[архитектура] {sl.sid}: `vynoska` — "
                    f"{type(vr).__name__}, а должна быть at/text")
    return {"blocks": blocks, "vynoska": vyn}


# ── мера ────────────────────────────────────────────────────────────


def _box_w(d, w, st):
    n = len(d["blocks"])
    return (w - (n - 1) * (st.arrow_w + 2 * st.gap)) / max(n, 1)


def _iw(d, w, st):
    """Ширина ПОД ИЗМЕРЕНИЕ переноса внутри бокса — с запасом `W_SAFE`, тем
    же, с каким меряет `metrics`: запас нужен решению «сколько строк»."""
    return max(0.3, (_box_w(d, w, st) - 2 * st.pad) * metrics.W_SAFE)


def _line_h(size, ls):
    return size * ls * metrics.LH / 72.0 * metrics.SAFE


def _longest(text, f):
    """Самое ШИРОКОЕ слово: перенос идёт по пробелам, и слово шире бокса
    LibreOffice разорвёт посреди корня."""
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def _fits(text, f, iw, rows, bold=False):
    if metrics.n_lines(text, f, iw, bold) > rows:
        return False
    return metrics.text_w(_longest(text, f), f, True) <= iw * 72.0


def head_size(d, w, st=DEFAULT):
    """Один кегль на ВСЕ заголовки боксов: наибольший, при котором каждый
    встаёт в две строки и ни одно слово не шире бокса. Один на все нарочно —
    разные кегли у соседних боксов читаются как разная важность частей."""
    iw = _iw(d, w, st)
    f = st.head_hi
    while f > st.head_lo:
        if all(_fits(b["head"], f, iw, st.head_rows, True)
               for b in d["blocks"]):
            break
        f -= 0.5
    return f


def line_size(d, w, st=DEFAULT):
    """Один кегль на ВСЕ строки разбора, по той же причине."""
    iw = _iw(d, w, st)
    f = st.line_hi
    while f > st.line_lo:
        if all(_fits(t, f, iw, st.line_rows)
               for b in d["blocks"] for t in b["lines"]):
            break
        f -= 0.5
    return f


def _lines_h(b, f, iw, st):
    if not b["lines"]:
        return 0.0
    h = sum(min(st.line_rows, metrics.n_lines(t, f, iw))
            * _line_h(f, st.line_ls) for t in b["lines"])
    return h + (len(b["lines"]) - 1) * st.line_sb / 72.0


def box_h(d, w, st=DEFAULT):
    """Высота бокса — одна на все: разной высоты боксы в ряду читаются как
    части разного веса, а здесь они части одного устройства."""
    iw = _iw(d, w, st)
    hf, lf = head_size(d, w, st), line_size(d, w, st)
    best = st.box_min_h
    for b in d["blocks"]:
        h = 2 * st.pad
        if b["role"]:
            h += st.role_h + st.role_gap
        h += min(st.head_rows, metrics.n_lines(b["head"], hf, iw, True)) \
            * _line_h(hf, st.head_ls)
        if b["lines"]:
            h += st.head_gap + _lines_h(b, lf, iw, st)
        best = max(best, h)
    return best


def vyn_h(d, w, st=DEFAULT):
    if not d["vynoska"]:
        return 0.0
    iw = max(0.3, w - 2 * st.vyn_pad)
    return (st.vyn_gap + st.vyn_stem + 2 * st.vyn_pad
            + metrics.est_h(d["vynoska"]["text"], st.vyn_pt, iw, st.vyn_ls))


def arhitektura_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра.

    Мера и рисование берут числа отсюда, из одного места: две формулы
    одного числа расходятся на первой правке."""
    return box_h(d, w, st) + vyn_h(d, w, st)


# ── сторожа ─────────────────────────────────────────────────────────


def check_arhitektura(sid, d, w, st=DEFAULT):
    """`[архитектура]`: пятый блок · один блок · два узких места · блок без
    разбора · пятая строка разбора · строка не влезла на полу · тесный бокс ·
    разорванное слово · выноска в никуда. Каждое — про то, что видно на
    экране, а не про вкус."""
    n = len(d["blocks"])
    if n > st.max_blocks:
        report.warn(
            f"[архитектура] {sid}: блоков {n} (> {st.max_blocks}) — предел "
            "«четыре клетки в ряду» из правила курса держится и здесь: "
            "владелец, 2026-10-08, «не надо вот этот длинный пайплайн». "
            "Пятый бокс не ужимают кеглем — устройство разносят на два "
            "кадра либо сворачивают соседние части в одну")
    if n < st.min_blocks:
        report.warn(
            f"[архитектура] {sid}: блок один — устройства из одной части не "
            "выходит, это плашка (`blocks:`), а не архитектура")
    uz = [b["head"] for b in d["blocks"] if b["uzkoe"]]
    if len(uz) > 1:
        report.warn(
            f"[архитектура] {sid}: узких мест объявлено {len(uz)} "
            f"({', '.join(uz)}) — узкое место по определению одно; "
            "выделение, которое досталось половине боксов, не выделяет "
            "ничего")
    for i, b in enumerate(d["blocks"], 1):
        if not b["lines"]:
            report.warn(
                f"[архитектура] {sid}: у блока «{b['head']}» нет `lines` — "
                "эта форма существует ради разбора ВНУТРИ бокса; без него "
                "она превращается в схему рядами, для которой есть "
                "`scheme:`")
        if len(b["lines"]) > st.max_lines:
            report.warn(
                f"[архитектура] {sid}: в блоке «{b['head']}» строк разбора "
                f"{len(b['lines'])} (> {st.max_lines}) — дальше бокс "
                "читается абзацем, то есть тем самым полотном текста, от "
                "которого форма уводит")
    iw = _iw(d, w, st)
    bw = _box_w(d, w, st)
    if bw < st.min_box_w:
        report.warn(
            f"[архитектура] {sid}: бокс вышел {bw:.2f}\" "
            f"(< {st.min_box_w:.2f}\") — разбор внутри такого бокса "
            "набирается столбиком по два слова; блоков больше, чем держит "
            "эта ширина")
    hf, lf = head_size(d, w, st), line_size(d, w, st)
    for b in d["blocks"]:
        for text, f, rows, bold, what in (
                [(b["head"], hf, st.head_rows, True, "заголовок блока")]
                + [(t, lf, st.line_rows, False, "строка разбора")
                   for t in b["lines"]]):
            long = _longest(text, f)
            if long and metrics.text_w(long, f, True) > iw * 72.0:
                report.warn(
                    f"[архитектура] {sid}: слову «{long}» нужно "
                    f"{metrics.text_w(long, f, True) / 72.0:.2f}\" при "
                    f"{f:.1f} пт, а бокс вышел {iw:.2f}\" — слово будет "
                    "разорвано переносом посреди корня")
            elif metrics.n_lines(text, f, iw, bold) > rows:
                report.warn(
                    f"[архитектура] {sid}: {what} «{text[:44]}…» не влезает "
                    f"и на {f:.1f} пт — это пол видимого слоя, ниже текст с "
                    "задних рядов не читается. Строку сокращают, а не "
                    "ужимают")
        if b["role"]:
            need = metrics.text_w(b["role"], st.role_pt, True) / 72.0
            if need > (bw - 2 * st.pad - 0.12) * metrics.W_SAFE:
                report.warn(
                    f"[архитектура] {sid}: ярлык роли «{b['role']}» просит "
                    f"{need:.2f}\" при полосе "
                    f"{bw - 2 * st.pad - 0.12:.2f}\" — ярлык это одно-два "
                    "слова, остальное идёт строкой разбора")
    v = d["vynoska"]
    if v and not 0 <= v["at"] < n:
        report.warn(
            f"[архитектура] {sid}: выноска указывает на блок {v['at']}, а "
            f"блоков {n} (считая с нуля, крайний — {n - 1}) — указатель "
            "уйдёт мимо кадра")


# ── рисование ───────────────────────────────────────────────────────


def _draw_block(s, sid, b, x, y, bw, bh, hf, lf, st, tag):
    prims.ocean_box(s, x, y, bw, bh, fill=SURFACE,
                    stroke=GOLD if b["uzkoe"] else LIGHT,
                    stroke_pt=st.uzkoe_pt if b["uzkoe"] else 1.5)
    iw = max(0.3, bw - 2 * st.pad)
    cy = y + st.pad
    if b["role"]:
        # ЗОЛОТО ЗАЛИВКОЙ, не текстом: на светлом листе `#F0AB00` буквами
        # даёт 1,99 : 1 при пороге 3,0 (`contrast.py`). Тёмный текст на
        # золоте — 6,85 : 1.
        floor.pt(st.role_pt, tag, "ярлык роли блока")
        prims.rect(s, x + st.pad, cy, iw, st.role_h,
                   GOLD if b["uzkoe"] else TEAL_TINT, radius=True,
                   radius_adj=0.38, count="акцент")
        prims.text_box(s, x + st.pad + 0.06, cy, iw - 0.12, st.role_h,
                       b["role"], size=st.role_pt, bold=True,
                       color=DEEP if b["uzkoe"] else MID,
                       align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                       ls=1.05, tag=f"{tag}/роль")
        if b["uzkoe"]:
            report.GOLD_SEEN.add(sid)
        cy += st.role_h + st.role_gap
    hh = min(st.head_rows,
             metrics.n_lines(b["head"], hf, iw * metrics.W_SAFE, True)) \
        * _line_h(hf, st.head_ls)
    prims.text_box(s, x + st.pad, cy, iw, hh, b["head"], size=hf, bold=True,
                   color=DEEP, ls=st.head_ls, tag=f"{tag}/заголовок")
    cy += hh
    if not b["lines"]:
        return
    cy += st.head_gap
    runs = []
    for j, t in enumerate(b["lines"]):
        if j:
            runs.append({"text": "", "size": lf, "newpara": True,
                         "space_before": st.line_sb})
        runs.append({"text": t, "size": lf, "color": DEEP})
    # Разбор держится ПО СЕРЕДИНЕ оставшегося места, а не по его верху.
    # Высота бокса одна на все (части одного устройства не бывают разного
    # веса), поэтому у блока с коротким разбором остаётся слабина — и
    # сваленная целиком вниз она читается «здесь текст не дописали».
    # Поделённая пополам, она читается полем. Поймано глазом на первом же
    # снимке: у левого бокса внизу пустовало 0,45".
    prims.text_runs(s, x + st.pad, cy, iw, y + bh - st.pad - cy, runs,
                    ls=st.line_ls, anchor=MSO_ANCHOR.MIDDLE,
                    tag=f"{tag}/разбор")


def _draw_vynoska(s, d, v, x, y_top, w, bw, st, tag):
    """Указатель: точка на нижней грани нужного бокса, короткий отвес и
    плашка с текстом во всю ширину под ним.

    ПЕРВАЯ РЕДАКЦИЯ ВЕЛА УГОЛКОМ — отвес вниз, затем горизонталь до левого
    поля, под ней строка без рамки. На снимке горизонталь прошла подо всеми
    тремя боксами во всю ширину кадра и прочиталась НЕ указателем, а
    декоративной линейкой под схемой — ровно тем приёмом, который запрещён
    прямым правилом (`CLAUDE.md`, anti-pattern 1). Поймано глазом, не
    прогоном: длина линии ни одной проверке пакета не видна.

    Чинится тем, что горизонталь не нужна вовсе, если текст лежит в
    плашке: отвес падает из бокса в ВЕРХНЮЮ ГРАНЬ плашки, и этого хватает,
    чтобы читалось «вот эта мысль — про этот бокс». Отвес стал короче
    (0,30"), плашка держит текст рамкой, линий во всю ширину на кадре не
    осталось."""
    at = max(0, min(v["at"], len(d["blocks"]) - 1))
    cx = x + at * (bw + st.arrow_w + 2 * st.gap) + bw / 2
    y_dot = y_top + st.vyn_gap
    prims.rect(s, cx - st.vyn_rule / 2, y_dot, st.vyn_rule, st.vyn_stem,
               MID, count="акцент")
    prims.rect(s, cx - st.vyn_dot / 2, y_dot - st.vyn_dot / 2,
               st.vyn_dot, st.vyn_dot, MID, radius=True, radius_adj=0.5,
               count="акцент")
    floor.pt(st.vyn_pt, tag, "выноска архитектуры")
    iw = max(0.3, w - 2 * st.vyn_pad)
    th = metrics.est_h(v["text"], st.vyn_pt, iw, st.vyn_ls)
    y_box = y_dot + st.vyn_stem
    prims.ocean_box(s, x, y_box, w, th + 2 * st.vyn_pad)
    prims.text_box(s, x + st.vyn_pad, y_box + st.vyn_pad, iw, th, v["text"],
                   size=st.vyn_pt, color=DEEP, ls=st.vyn_ls,
                   tag=f"{tag}/выноска")


def draw_arhitektura(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Устройство: боксы в ряд со стрелками, разбор внутри, выноска снизу.
    Возвращает занятую высоту."""
    tag = tag or sid
    hf, lf = head_size(d, w, st), line_size(d, w, st)
    floor.pt(hf, tag, "заголовок блока архитектуры")
    floor.pt(lf, tag, "строка разбора архитектуры")
    bw, bh = _box_w(d, w, st), box_h(d, w, st)
    cx = x
    for i, b in enumerate(d["blocks"], 1):
        if i > 1:
            prims.arrow(s, cx + st.gap, y + bh / 2 - st.arrow_h / 2,
                        st.arrow_w, st.arrow_h, LIGHT)
            cx += st.arrow_w + 2 * st.gap
        _draw_block(s, sid, b, cx, y, bw, bh, hf, lf, st, f"{tag}/блок{i}")
        cx += bw
    if d["vynoska"]:
        _draw_vynoska(s, d, d["vynoska"], x, y + bh, w, bw, st, tag)
    report.PRIM["архитектура"] += 1
    return arhitektura_h(d, w, st)
