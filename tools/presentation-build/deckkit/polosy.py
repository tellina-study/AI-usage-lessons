# -*- coding: utf-8 -*-
"""ПАРНЫЕ ПОЛОСЫ `polosy:` — классический режим против режима модели, и
обязательно В ОДНОЙ ЕДИНИЦЕ.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: разрыв между двумя способами сделать одну и ту же
работу — РАССТОЯНИЕМ, а не двумя цифрами в тексте. Полоса классического
режима и полоса режима модели идут одна под другой, на одной прямой, с одной
подписанной единицей.

ОТКУДА ОНА ВЗЯТА. `PERENOS-PRIYOMOV.md` §2.3: в образцах (`media/s05`,
`image/s04`) три строки «одно изображение / минута озвучки / выпуск
микродрамы», у каждой две полосы, значение подписью у конца полосы,
логарифмическая ось внизу с явной подписью, а к паре пририсован множитель —
«×1 000–4 500 к заказу».

ПОЧЕМУ ЭТО ПРЯМО НАШЕ ПРАВИЛО, А НЕ ПРОСТО КРАСИВЫЙ ПРИЁМ. Канон разбора
(§5.13, `CLAUDE.md` § «Строение раздела») требует, чтобы у классического
режима и у режима модели ЕДИНИЦА БЫЛА ОДНА: выигрыш, посчитанный от нуля
вместо классического режима, не принимается, а «168 человеко-часов» против
«$40» — это не сравнение. Полоса делает нарушение ВИДИМЫМ: разные единицы на
одной оси нарисовать нельзя. Поэтому главный сторож здесь не про вёрстку, а
про единицу (`check_polosy`, два его первых куска).

РОДСТВО С ОСЬЮ. Это близкий родственник `axis.py` (`scheme: kind: shkala`), и
родство не внешнее: у обеих форм положение несёт смысл, у обеих поэтому
общей природы сторожа — разные базы запрещены, единица обязана быть названа.
Разбор чисел («0,042» с запятой, «1 000» с пробелом) и шаг сетки взяты
ОТТУДА, а не переписаны: две формулы одного числа расходятся на первой
правке. Разница между формами — в том, что ось кладёт на прямую N РАЗНЫХ
величин, а эта — N ПАР «было / стало», и пара не раскладывается на две
засечки: тогда потерялось бы, что сравнивают именно эти две, а не все четыре
между собой.

ЗАЧЕМ ЛОГАРИФМИЧЕСКАЯ ШКАЛА И ЧЕМ ОНА ОПАСНА. Настоящие пары этой лекции
отличаются в тысячи раз ($50–150 против $0,034–0,05). На линейной шкале
полоса модели короче засечки — её просто нет на экране, и «в три тысячи раз
дешевле» превращается в «ноль против всего». Логарифм это чинит и тут же
заводит свою ложь: зал, не знающий, что шкала логарифмическая, читает
вчетверо более короткую полосу как «вчетверо дешевле». Поэтому подпись оси
ОБЯЗАНА нести слово «логарифмическая», и это сторож, а не рекомендация.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не красит значения золотом: золото `#F0AB00`
текстом на белом даёт 1,99 : 1 при пороге 3,0 (`contrast.py`, правило
перевода §1 того же файла). Золото здесь — ЗАЛИВКА плашки множителя с тёмным
текстом поверх (6,85 : 1). Не рисует третью полосу в паре: пара это пара.

Контракт фронтматтера:

    polosy:
      unit: "доллары за одну пробу · шкала логарифмическая"
      scale: log                 # log | linear
      caption: "…"               # необязательна
      klassika_name: "Классический режим"   # необязательны, это умолчания
      model_name: "С моделью"
      rows:
        - label: "Одно изображение 1024×1024"
          klassika: {value: 100, text: "$50–150"}
          model:    {value: 0.042, text: "$0,034–0,05"}
          mnozhitel: "×1 000–4 500 к заказу"
"""
import math
import re
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import axis, floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, OUTLINE, SLATE, TEAL

NEEDS_ROWS = False          # полосы читают `rows` САМИ: у строки не `steps`,
                            # а пара «классика / модель», и общий разбор
                            # рядов схемы её не знает

# Ключи, которые форма ДЕЙСТВИТЕЛЬНО читает. Перечни закрытые — договор
# формы №5 («называть ключ, которого не читает»): молчащий ключ хуже
# отсутствующего, на `s36` Лекции 7 это уже стоило круга.
TOP_KEYS = {"unit", "scale", "rows", "caption", "klassika_name",
            "model_name"}
ROW_KEYS = {"label", "klassika", "model", "mnozhitel", "unit"}
SIDE_KEYS = {"value", "text", "unit"}

SCALES = ("log", "linear")

# Слово, без которого логарифмическая ось врёт. Корень, а не точная форма:
# «шкала логарифмическая», «логарифмический масштаб», «по логарифму» —
# всё это называет шкалу, и придираться к падежу здесь не к чему.
LOG_WORD = re.compile(r"логарифм", re.I)

# Род единицы по приметам в ПОДПИСИ значения. Перечень закрытый и короткий
# нарочно: он не разбирает фразу, он ловит тот случай, который бывает, —
# одна строка в деньгах, другая в часах. Половина сторожа, которая работает
# без объявления автором; вторая, надёжная, — явный `unit` у строки.
UNIT_KINDS = (
    ("деньги", re.compile(r"[$€₽]|руб|долл|цент|евро", re.I)),
    ("время", re.compile(r"\bчас|\bч\b|\bмин|\bсут|\bдн[ейя]|\bнедел"
                         r"|\bмесяц|\bгод", re.I)),
    ("масса", re.compile(r"\bкг\b|\bграмм|\bтонн", re.I)),
    ("штуки", re.compile(r"\bшт\b|\bштук|\bед\b", re.I)),
)


@dataclass(frozen=True)
class PolosyStyle:
    lab_w: float = 2.45         # ПРЕДЕЛ колонки подписи строки слева
    lab_w_min: float = 1.10
    lab_gap: float = 0.14
    lab_pt: float = 13.0
    lab_ls: float = 1.12
    bar_h: float = 0.28
    bar_gap: float = 0.10       # просвет между полосами ПАРЫ
    row_gap: float = 0.26       # просвет между парами
    val_pt: float = 14.0
    val_gap: float = 0.10       # просвет конец полосы — подпись значения
    val_w_max: float = 2.10
    val_w_min: float = 0.70
    mn_w: float = 2.00          # колонка плашки множителя справа
    mn_gap: float = 0.16
    mn_pt: float = 12.0         # пол видимого слоя, см. `floor.py`
    leg_h: float = 0.24         # шапка: какая полоса чья
    leg_gap: float = 0.12
    leg_pt: float = 12.0        # пол видимого слоя
    leg_sw: float = 0.26        # образец цвета в шапке
    line_h: float = 0.045
    tick_h: float = 0.14
    tick_w: float = 0.045
    tick_pt: float = 12.0       # пол видимого слоя
    tick_lab_h: float = 0.23
    axis_gap: float = 0.14      # просвет последняя пара — ось
    unit_pt: float = 12.0       # пол видимого слоя
    unit_gap: float = 0.10
    unit_ls: float = 1.10
    cap_pt: float = 12.0        # пол видимого слоя
    cap_ls: float = 1.14
    cap_gap: float = 0.08
    grid: bool = True           # бледные линии сетки по засечкам
    max_rows: int = 5           # шестая строка — отказ
    min_bar: float = 0.06       # короче этого полосы на экране нет
    min_plot_w: float = 2.60    # уже этого шкала не шкала


DEFAULT = PolosyStyle()


def _side_of(sid, rown, name, raw):
    """Одна сторона пары → {v, shown, unit} или None."""
    if raw is None:
        report.warn(
            f"[полосы] {sid}: в строке {rown} нет стороны «{name}» — форма "
            "называется парными полосами, и пара в ней обязана быть полной: "
            "одна полоса сравнения не делает")
        return None
    if not isinstance(raw, dict):
        raw = {"value": raw}
    unknown = set(raw) - SIDE_KEYS
    if unknown:
        report.warn(f"[полосы] {sid}: строка {rown}, сторона «{name}» — "
                    f"ключи {', '.join(sorted(unknown))} ядро не читает")
    v = axis._num(raw.get("value"))
    if v is None:
        report.warn(
            f"[полосы] {sid}: в строке {rown} у стороны «{name}» значение "
            f"«{raw.get('value')}» не число — длину полосы от него не "
            "отложить. Словесная величина живёт плашкой, не полосой")
        return None
    shown = str(raw.get("text") or raw.get("value")).strip()
    return {"v": v, "shown": shown, "unit": str(raw.get("unit") or "").strip()}


def polosy_of(sl, st=DEFAULT):
    """Поле `polosy` кадра → разобранная форма или None."""
    return parse(sl.sid, sl.meta.get("polosy"), None, st)


def parse(sid, raw, rows=None, st=DEFAULT):
    """Разбор поля. Чужая форма поля не роняет сборку — она называется
    `[полосы]`, и кадр собирается без формы."""
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[полосы] {sid}: поле `polosy` — {type(raw).__name__}, "
                    "а должно быть unit/scale/rows")
        return None
    unknown = set(raw) - TOP_KEYS
    if unknown:
        report.warn(f"[полосы] {sid}: ключи {', '.join(sorted(unknown))} "
                    "ядро не читает — молчащий ключ хуже отсутствующего")
    rr = raw.get("rows")
    if not isinstance(rr, list) or not rr:
        report.warn(f"[полосы] {sid}: у формы `polosy` нет `rows` — это пары "
                    "«классический режим / режим модели», а не ряды шагов")
        return None
    scale = str(raw.get("scale") or "linear").strip().lower()
    if scale not in SCALES:
        report.warn(f"[полосы] {sid}: шкала «{scale}» ядру неизвестна — есть "
                    f"{' · '.join(SCALES)}; взята линейная")
        scale = "linear"
    out = []
    for i, r in enumerate(rr, 1):
        if not isinstance(r, dict):
            report.warn(f"[полосы] {sid}: строка {i} не label/klassika/model")
            continue
        unknown = set(r) - ROW_KEYS
        if unknown:
            report.warn(f"[полосы] {sid}: строка {i} — ключи "
                        f"{', '.join(sorted(unknown))} ядро не читает")
        k = _side_of(sid, i, "klassika", r.get("klassika"))
        m = _side_of(sid, i, "model", r.get("model"))
        if k is None or m is None:
            continue
        out.append({"label": str(r.get("label") or "").strip(),
                    "k": k, "m": m,
                    "mnozhitel": str(r.get("mnozhitel") or "").strip(),
                    "unit": str(r.get("unit") or "").strip()})
    if not out:
        return None
    return {"kind": "polosy", "rows": out, "scale": scale,
            "unit": str(raw.get("unit") or "").strip(),
            "caption": str(raw.get("caption") or "").strip(),
            "klassika_name": str(raw.get("klassika_name")
                                 or "Классический режим").strip(),
            "model_name": str(raw.get("model_name") or "С моделью").strip()}


# ── шкала ───────────────────────────────────────────────────────────


def _vals(d):
    return [s["v"] for r in d["rows"] for s in (r["k"], r["m"])]


def _pos(d):
    """Значения, которые вообще можно положить на шкалу."""
    return [v for v in _vals(d) if v > 0] if d["scale"] == "log" else _vals(d)


def span(d, st=DEFAULT):
    """Предел шкалы: (нижний, верхний) в ЗНАЧЕНИЯХ.

    Логарифмическая идёт по целым порядкам — засечки 0,01 · 0,1 · 1 · 10 ·
    100 читаются как границы, а 0,042…100 читалось бы как данные. Нижний
    порядок при этом опускается ещё на один, когда наименьшая величина сама
    стоит на круглом порядке: иначе её полоса имеет НУЛЕВУЮ длину — то есть
    самая дешёвая строка кадра исчезает с экрана, а форма молчит.

    Линейная всегда идёт ОТ НУЛЯ: полоса, начатая не от нуля, врёт длиной —
    это её физическое свойство, а не настройка."""
    vals = _pos(d) or [1.0]
    lo_v, hi_v = min(vals), max(vals)
    if d["scale"] == "log":
        lo_e = math.floor(math.log10(lo_v))
        if math.log10(lo_v) - lo_e < 0.15:
            lo_e -= 1
        hi_e = math.ceil(math.log10(hi_v))
        if hi_e <= lo_e:
            hi_e = lo_e + 1
        return 10.0 ** lo_e, 10.0 ** hi_e
    step = axis._step(hi_v if hi_v > 0 else 1.0)
    hi = math.ceil(hi_v / step) * step if hi_v > 0 else step
    return 0.0, (hi if hi > 0 else step)


def _frac(v, d, st=DEFAULT):
    """Доля длины полосы от ширины шкалы, 0…1."""
    lo, hi = span(d, st)
    if d["scale"] == "log":
        if v <= 0:
            return 0.0
        return (math.log10(v) - math.log10(lo)) \
            / (math.log10(hi) - math.log10(lo))
    return 0.0 if hi <= lo else (v - lo) / (hi - lo)


def ticks(d, st=DEFAULT):
    """Засечки шкалы: [(значение, подпись)]."""
    lo, hi = span(d, st)
    if d["scale"] == "log":
        lo_e, hi_e = int(round(math.log10(lo))), int(round(math.log10(hi)))
        out = []
        for e in range(lo_e, hi_e + 1):
            v = 10.0 ** e
            if e >= 0:
                s = f"{v:,.0f}".replace(",", " ")
            else:
                s = f"{v:.{-e}f}".replace(".", ",")
            out.append((v, s))
        return out
    step = axis._step(hi - lo)
    n = int(round((hi - lo) / step))
    return [(lo + i * step, axis._fmt(lo + i * step, step))
            for i in range(n + 1)]


# ── колонки и высоты ────────────────────────────────────────────────


def _val_w(d, st=DEFAULT):
    """Полоса справа от шкалы, отданная подписям значений. Меряется по
    САМОЙ ШИРОКОЙ подписи, а не берётся числом: подпись, которой не хватило
    места, переносится на вторую строку и садится на соседнюю полосу
    пары — ровно тот дефект, о котором говорит `check_polosy`."""
    need = max([metrics.text_w(s["shown"], st.val_pt, True) / 72.0
                for r in d["rows"] for s in (r["k"], r["m"])] or [0.0])
    return max(st.val_w_min, min(st.val_w_max, need + 0.08))


def has_mn(d):
    return any(r["mnozhitel"] for r in d["rows"])


def lab_w(d, st=DEFAULT):
    """Колонка подписей строк — МЕРЕНАЯ, а не постоянная.

    Постоянные 2,45" отдавали пустоте почти дюйм там, где подписи короткие
    («Отбор кадров», «Сборка и сведение»), и дюйм этот отнимался у ШКАЛЫ —
    то есть у единственного, что эта форма показывает. Замерено на
    демонстрационном кадре: шкала 7,10" против 8,00". Предел `lab_w`
    остаётся: подпись длиннее него переносится, а не съедает шкалу."""
    need = max([metrics.text_w(r["label"], st.lab_pt) / 72.0
                for r in d["rows"] if r["label"]] or [0.0])
    if need <= 0.0:
        return 0.0
    return max(st.lab_w_min, min(st.lab_w, need + 0.10))


def cols(d, w, st=DEFAULT):
    """Геометрия колонок: (ширина подписи, x шкалы, ширина шкалы,
    x множителя, ширина колонки подписей значений). Одно место на меру и
    на рисование: две формулы одного числа расходятся на первой правке."""
    vw = _val_w(d, st)
    lw = lab_w(d, st)
    mn = (st.mn_gap + st.mn_w) if has_mn(d) else 0.0
    off = lw + (st.lab_gap if lw else 0.0)
    plot = w - off - st.val_gap - vw - mn
    return (lw, off, plot, w - st.mn_w if has_mn(d) else None, vw)


def row_h(row, lw, st=DEFAULT):
    """Высота пары: две полосы с просветом, но не меньше, чем нужно её
    подписи слева."""
    pair = 2 * st.bar_h + st.bar_gap
    lab = metrics.est_h(row["label"], st.lab_pt, lw, st.lab_ls) \
        if (row["label"] and lw) else 0.0
    return max(pair, lab)


def axis_block_h(d, w, st=DEFAULT):
    """Ось под полосами: прямая · засечки · подписи засечек · единица."""
    h = st.axis_gap + st.line_h + st.tick_h + st.tick_lab_h
    if d["unit"]:
        _, _, plot, _, _ = cols(d, w, st)
        h += st.unit_gap + metrics.est_h(d["unit"], st.unit_pt,
                                         max(plot, 1.0), st.unit_ls, True)
    return h


def polosy_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    lw = lab_w(d, st)
    h = st.leg_h + st.leg_gap
    h += sum(row_h(r, lw, st) for r in d["rows"])
    h += st.row_gap * max(0, len(d["rows"]) - 1)
    h += axis_block_h(d, w, st)
    if d["caption"]:
        h += st.cap_gap + metrics.est_h(d["caption"], st.cap_pt, w,
                                        st.cap_ls, False, True)
    return h


# ── сторож ──────────────────────────────────────────────────────────


def _kinds(text):
    return {name for name, rx in UNIT_KINDS if rx.search(text or "")}


def check_polosy(sid, d, w, st=DEFAULT):
    """`[полосы]`: РАЗНЫЕ ЕДИНИЦЫ · единица не названа · логарифм не
    назван · одна строка · шестая строка · величина ≤ 0 при логарифме ·
    подписи значений сойдутся · полоса короче засечки · шкале не осталось
    ширины.

    «Значение не число» сюда не попало нарочно: такую строку разбор уже
    снял и назвал — повторять её здесь значило бы считать один дефект
    дважды."""
    # 1. ЕДИНИЦЫ. Главный сторож формы: она утверждает сравнение, а
    # сравнивать в разных единицах нельзя. Две половины — объявленная
    # автором и подсмотренная в подписях.
    declared = {u for r in d["rows"]
                for u in (r["unit"], r["k"]["unit"], r["m"]["unit"]) if u}
    if len(declared) > 1:
        report.warn(
            f"[полосы] {sid}: у строк РАЗНЫЕ единицы "
            f"({' · '.join(sorted(declared))}) — на одну шкалу их класть "
            "нельзя: это сравнение, которого нет. Единица у формы одна, она "
            "в `unit`; величины разных единиц живут отдельными кадрами")
    seen = [(r["label"] or f"строка {i}",
             _kinds(r["k"]["shown"]) | _kinds(r["m"]["shown"]))
            for i, r in enumerate(d["rows"], 1)]
    named = [(n, k) for n, k in seen if k]
    for (n1, k1), (n2, k2) in zip(named, named[1:]):
        if not (k1 & k2):
            report.warn(
                f"[полосы] {sid}: «{n1}» считана в единицах рода "
                f"«{'/'.join(sorted(k1))}», а «{n2}» — рода "
                f"«{'/'.join(sorted(k2))}». Одна шкала на обе означала бы, "
                "что их длины сравнимы, а они не сравнимы")
            break
    if not d["unit"]:
        report.warn(
            f"[полосы] {sid}: у шкалы не названа ЕДИНИЦА (`unit`) — без неё "
            "длины сравнимы только на вид: «$0,04» и «0,04 часа» ложатся на "
            "шкалу одинаково хорошо и значат разное")
    elif d["scale"] == "log" and not LOG_WORD.search(d["unit"]):
        report.warn(
            f"[полосы] {sid}: шкала логарифмическая, а подпись «{d['unit']}» "
            "об этом не говорит — зал прочтёт вдвое более короткую полосу "
            "как «вдвое дешевле», тогда как она в сто раз дешевле. Слово "
            "«логарифмическая» в подписи обязательно")
    # 2. ЧИСЛО СТРОК.
    n = len(d["rows"])
    if n < 2:
        report.warn(
            f"[полосы] {sid}: строка одна — пара без соседних пар это кадр "
            "одного сравнения, и он читается `figure:` либо осью. Парные "
            "полосы заводят, когда сравнений несколько и важно, что они "
            "считаны в одной единице")
    if n > st.max_rows:
        report.warn(
            f"[полосы] {sid}: строк {n} (> {st.max_rows}) — это уже график, "
            f"а не {st.max_rows} пар на экране: подписи мельчают, а пара "
            "перестаёт читаться парой")
    # 3. ВЕЛИЧИНЫ И ШКАЛА.
    if d["scale"] == "log":
        for i, r in enumerate(d["rows"], 1):
            for name, s in (("klassika", r["k"]), ("model", r["m"])):
                if s["v"] <= 0:
                    report.warn(
                        f"[полосы] {sid}: строка {i}, сторона «{name}» — "
                        f"величина {s['v']} не больше нуля, а логарифма у "
                        "нуля и отрицательных нет. Либо линейная шкала, "
                        "либо величина названа неверно")
    _, _, plot, _, vw = cols(d, w, st)
    if plot < st.min_plot_w:
        report.warn(
            f"[полосы] {sid}: под шкалу осталось {plot:.2f}\" (нужно хотя бы "
            f"{st.min_plot_w:.2f}\") — подписи строк и значений съели кадр. "
            "Сокращают подписи, а не шкалу: шкала короче этого перестаёт "
            "показывать разницу")
    for i, r in enumerate(d["rows"], 1):
        for name, s in (("klassika", r["k"]), ("model", r["m"])):
            bar = _frac(s["v"], d, st) * plot
            if bar < st.min_bar:
                tail = ("Это случай для `scale: log`: логарифм для того и "
                        "заведён" if d["scale"] != "log" else
                        "Задайте шкалу поуже либо снимите эту строку")
                report.warn(
                    f"[полосы] {sid}: строка {i}, «{name}» — полоса длиной "
                    f"{bar:.3f}\" при засечке {st.tick_h:.2f}\": на экране "
                    "её нет, и «в тысячу раз дешевле» читается как «ноль "
                    f"против всего». {tail}")
            # Подпись начинается за концом полосы и живёт до правого края
            # своей колонки: свободного места ровно столько.
            free = plot - bar + vw
            need = metrics.text_w(s["shown"], st.val_pt, True) / 72.0
            if need > free:
                report.warn(
                    f"[полосы] {sid}: строка {i}, подпись «{s['shown']}» "
                    f"просит {need:.2f}\", а после своей полосы остаётся "
                    f"{free:.2f}\" — она перенесётся на вторую строку и "
                    "сядет на соседнюю полосу пары. Сокращают подпись "
                    "значения либо подпись строки слева")


# ── рисование ───────────────────────────────────────────────────────


def _legend(s, d, x, y, x_plot, st, tag):
    """Шапка: какая полоса чья. Одна на всю форму, а не подпись у каждой из
    десяти полос — повторённое десять раз имя перестаёт читаться именем."""
    floor.pt(st.leg_pt, tag, "шапка полос")
    cx = x + x_plot
    for name, col in ((d["klassika_name"], DEEP), (d["model_name"], TEAL)):
        prims.rect(s, cx, y + (st.leg_h - 0.13) / 2, st.leg_sw, 0.13, col,
                   count="полоса")
        tw = metrics.text_w(name, st.leg_pt, True) / 72.0 + 0.10
        prims.text_box(s, cx + st.leg_sw + 0.08, y, tw, st.leg_h, name,
                       size=st.leg_pt, bold=True, color=col,
                       anchor=MSO_ANCHOR.MIDDLE, ls=1.0,
                       tag=f"{tag}/шапка", quiet=True)
        cx += st.leg_sw + 0.08 + tw + 0.34


def _axis(s, d, x, y, x_plot, plot, st, tag):
    """Прямая, засечки, их подписи и строка единицы. Возвращает низ."""
    px = x + x_plot
    prims.rect(s, px, y, plot, st.line_h, LIGHT, count="ось")
    tt = ticks(d, st)
    # Подписи засечек прореживаются, когда их ширина больше просвета: лучше
    # подписать каждую вторую границу, чем нарисовать кашу из цифр.
    step = 1
    if len(tt) > 1:
        gap = plot / (len(tt) - 1)
        need = max(metrics.text_w(s2, st.tick_pt) / 72.0 for _, s2 in tt)
        while step < len(tt) and gap * step < need + 0.14:
            step += 1
    floor.pt(st.tick_pt, tag, "подпись засечки шкалы")
    for i, (v, lab) in enumerate(tt):
        tx = px + _frac(v, d, st) * plot
        prims.rect(s, tx - st.tick_w / 2, y + st.line_h, st.tick_w,
                   st.tick_h, LIGHT, count="засечка")
        if i % step:
            continue
        prims.text_box(s, tx - 0.60, y + st.line_h + st.tick_h + 0.02, 1.20,
                       st.tick_lab_h, lab, size=st.tick_pt, color=SLATE,
                       align=PP_ALIGN.CENTER, ls=1.0, tag=f"{tag}/засечка",
                       quiet=True)
    cy = y + st.line_h + st.tick_h + st.tick_lab_h
    if d["unit"]:
        floor.pt(st.unit_pt, tag, "единица шкалы")
        # Высота строки единицы МЕРИТСЯ, а не берётся числом: при
        # фиксированных 0,24" переполнение молча садится на подписи засечек
        # (`notes/mcp-limitations.md` [#301-8], кадр s96 Лекции 8).
        uh = metrics.est_h(d["unit"], st.unit_pt, plot, st.unit_ls, True)
        prims.text_box(s, px, cy + st.unit_gap, plot, uh, d["unit"],
                       size=st.unit_pt, bold=True, color=MID,
                       align=PP_ALIGN.CENTER, ls=st.unit_ls,
                       tag=f"{tag}/единица")
        cy += st.unit_gap + uh
    return cy


def draw_polosy(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Пары полос, ось снизу, подпись. Возвращает занятую высоту."""
    tag = tag or sid
    lw, x_plot, plot, x_mn, vw = cols(d, w, st)
    top = y
    _legend(s, d, x, y, x_plot, st, tag)
    y += st.leg_h + st.leg_gap
    if st.grid:
        # Бледные линии по засечкам. Рисуются ДО полос, а не после:
        # порядок вставки фигур в PPTX и есть порядок слоёв, и сетка,
        # положенная поверх, перечёркивала бы полосу, длину которой
        # помогает прочесть.
        gh = sum(row_h(r, lw, st) for r in d["rows"]) \
            + st.row_gap * max(0, len(d["rows"]) - 1) + st.axis_gap
        for v, _lab in ticks(d, st):
            gx = x + x_plot + _frac(v, d, st) * plot
            prims.rect(s, gx - 0.005, y, 0.01, gh, OUTLINE, count="сетка")
    for i, r in enumerate(d["rows"], 1):
        rh = row_h(r, lw, st)
        pair = 2 * st.bar_h + st.bar_gap
        py = y + (rh - pair) / 2
        if r["label"] and lw:
            floor.pt(st.lab_pt, tag, "подпись строки полос")
            lh = metrics.est_h(r["label"], st.lab_pt, lw, st.lab_ls)
            prims.text_box(s, x, y + (rh - lh) / 2, lw, lh, r["label"],
                           size=st.lab_pt, color=DEEP, ls=st.lab_ls,
                           tag=f"{tag}/строка{i}")
        for k, (side, col) in enumerate(((r["k"], DEEP), (r["m"], TEAL))):
            by = py + k * (st.bar_h + st.bar_gap)
            bar = max(0.0, _frac(side["v"], d, st) * plot)
            prims.rect(s, x + x_plot, by, max(bar, 0.01), st.bar_h, col,
                       count="полоса")
            floor.pt(st.val_pt, tag, "подпись значения полосы")
            prims.text_box(s, x + x_plot + bar + st.val_gap, by,
                           vw + st.val_gap, st.bar_h, side["shown"],
                           size=st.val_pt, bold=True, color=DEEP,
                           anchor=MSO_ANCHOR.MIDDLE, ls=1.0,
                           tag=f"{tag}/значение{i}-{k + 1}", quiet=True)
        if r["mnozhitel"] and x_mn is not None:
            # Плашка стоит МЕЖДУ полосами пары по высоте — на той самой
            # разнице, о которой она говорит, — и в своей колонке по
            # ширине, чтобы никогда не сойтись с подписью значения.
            floor.pt(st.mn_pt, tag, "множитель пары")
            mh = min(pair, 0.62)
            prims.chip(s, x + x_mn, py + (pair - mh) / 2, st.mn_w, mh,
                       r["mnozhitel"], fill=GOLD, color=DEEP,
                       size=st.mn_pt, tag=f"{tag}/множитель{i}")
            report.GOLD_SEEN.add(sid)
        y += rh + (st.row_gap if i < len(d["rows"]) else 0.0)
    y += st.axis_gap
    y = _axis(s, d, x, y, x_plot, plot, st, tag)
    if d["caption"]:
        floor.pt(st.cap_pt, tag, "подпись формы")
        ch = metrics.est_h(d["caption"], st.cap_pt, w, st.cap_ls, False, True)
        prims.text_box(s, x, y + st.cap_gap, w, ch, d["caption"],
                       size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        y += st.cap_gap + ch
    report.PRIM["парные полосы"] += 1
    return y - top


# ── общий договор формы ─────────────────────────────────────────────


def height(d, w):
    return polosy_h(d, w)


def check(sid, d, w):
    return check_polosy(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_polosy(s, sid, d, x, y, w, tag=tag)
