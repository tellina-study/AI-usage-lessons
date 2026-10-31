# -*- coding: utf-8 -*-
"""ПИКТОГРАММНАЯ СЕТКА `piktogrammy:` — доля, нарисованная в натуре.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: долю как ПЛОЩАДЬ. «5 из 100» словами проходит
мимо внимания — число маленькое, предложение короткое, зал его слышит и не
удерживает. Пять золотых фигурок среди девяноста пяти контурных не проходит
мимо: доля здесь не сообщается, она занимает место на экране, и глаз меряет
её сам (`PERENOS-PRIYOMOV.md` §2.8, образец `media/s08`).

ЧЕМ ОНА НЕ ЯВЛЯЕТСЯ. Не круговой диаграммой и не полосой с процентом. У
круга и полосы доля — отношение двух длин, которое всё равно приходится
читать подписью; здесь доля — счётные единицы того же рода, что знаменатель,
и подпись называет не процент, а ЧТО ДЕЛАЛИ пять и что делали девяносто
пять. Форма поэтому берёт целые штуки, а не проценты: «5 из 100 человек»
рисуется, «5 % рынка» — нет.

ЗНАМЕНАТЕЛЬ ОБЯЗАТЕЛЕН, И ЭТО НЕ ФОРМАЛЬНОСТЬ. Правило курса (`CLAUDE.md`
§ «Baseline / Counterfactual Mandate»): всякая измеримая величина обязана
иметь базу. Сто фигурок без слова о том, фигурки ЧЕГО это, — самая
убедительная форма неинтерпретируемого числа, какая здесь есть: «5 из 100»
читается одинаково и про людей кампании, и про кадры ролика, и про доли
рынка, а выводы из этих трёх разные. Поэтому `znamenatel` проверяется как
содержание, печатается на кадре и повторяется в каждой подписи.

ЗОЛОТО — ЗАЛИВКА ФИГУРОК. Общее правило перевода (§1): золото у нас
заливка, не цвет букв (1,99 : 1 на белом при пороге 3,0, замер
`contrast.py`). Здесь это совпало с содержанием: доля и обязана быть
залитой, остаток — контурным.

ОТКУДА ФИГУРКА. Внешних иконок эта среда не умеет — ни mermaid, ни
ImageMagick, ни rsvg (`notes/mcp-limitations.md` [#301-5]), и это не
ограничение, а предпочтение: фигура, нарисованная в pptx, выходит векторной
и правится, вставленная картинка — нет. Фигурка собрана из двух фигур:
круг-голова (скруглённый прямоугольник с предельным скруглением — при
квадратной рамке это окружность) и трапеция-туловище.

Контракт фронтматтера:

    piktogrammy:
      vsego: 100
      dolya: 5
      znamenatel: "человек в кампании"
      podpis_doli: "генерировали"
      podpis_ostatka: "отбирали, склеивали, браковали"
"""
import math
from dataclasses import dataclass

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, WHITE

KEYS = {"vsego", "dolya", "znamenatel", "podpis_doli", "podpis_ostatka"}


@dataclass(frozen=True)
class PiktoStyle:
    grid_h_max: float = 3.30     # сколько сетка вправе отнять у тела
    fig_h_max: float = 0.46      # выше фигурка начинает читаться картинкой
    fig_ar: float = 0.62         # ширина фигурки к её высоте
    head_frac: float = 0.34      # голова — доля высоты фигурки
    neck_frac: float = 0.05
    gap_x_frac: float = 0.46     # просвет между фигурками, в долях ширины
    gap_y_frac: float = 0.20     # то же по вертикали, в долях высоты
    stroke_pt: float = 1.0       # обводка контурной фигурки
    znam_pt: float = 15.0
    znam_h: float = 0.30
    znam_gap: float = 0.22
    col_gap: float = 0.46        # «сетка → подписи»
    leg_num_pt: float = 18.0
    leg_txt_pt: float = 14.0
    leg_ls: float = 1.16
    leg_gap: float = 0.30        # между двумя подписями
    leg_fig_gap: float = 0.18    # «образчик фигурки → текст подписи»
    leg_fig_k: float = 1.5       # образчик крупнее фигурки сетки
    min_vsego: int = 10
    max_vsego: int = 200


DEFAULT = PiktoStyle()

# Сколько фигурок в ряду. Десять — потому что ряд из десяти пересчитывается
# взглядом без счёта, и сотня тогда читается квадратом десять на десять.
# Числу, которое на десять не делится, берётся ближайший делитель, дающий
# не больше двенадцати рядов: ряд из тринадцати уже считают по одной.
_COLS = (10, 12, 9, 8, 7, 6, 5, 4)


def grid_cols(vsego):
    if vsego % 10 == 0:
        return 10
    for c in _COLS:
        if vsego % c == 0 and vsego // c <= 12:
            return c
    return 10


def _int(raw):
    if isinstance(raw, bool):
        return None
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(round(raw)) if abs(raw - round(raw)) < 1e-9 else None
    s = str(raw or "").strip().replace(" ", "").replace(" ", "")
    try:
        return int(s)
    except ValueError:
        return None


def pikto_of(sl_or_sid, raw=None, st=DEFAULT):
    """Поле `piktogrammy` → разобранная сетка или None."""
    if raw is None:
        sid, raw = sl_or_sid.sid, sl_or_sid.meta.get("piktogrammy")
    else:
        sid = sl_or_sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[пиктограммы] {sid}: поле `piktogrammy` — "
                    f"{type(raw).__name__}, а должно быть vsego/dolya/"
                    "znamenatel")
        return None
    bad = sorted(set(raw) - KEYS)
    if bad:
        report.warn(
            f"[пиктограммы] {sid}: ключ(и) {' · '.join(bad)} форма не "
            "читает. Молчащий ключ хуже отсутствующего: он выглядит учтённым")
    vsego, dolya = _int(raw.get("vsego")), _int(raw.get("dolya"))
    if vsego is None:
        report.warn(
            f"[пиктограммы] {sid}: `vsego` = «{raw.get('vsego')}» — не целое "
            "число. Сетка рисует ШТУКИ, и дробной штуки не бывает: долю в "
            "процентах показывают осью, а не фигурками")
        return None
    if dolya is None:
        report.warn(
            f"[пиктограммы] {sid}: `dolya` = «{raw.get('dolya')}» — не целое "
            "число. Золотых фигурок столько, сколько сказано; половину "
            "фигурки нарисовать нечем")
        return None
    return {"vsego": vsego, "dolya": dolya,
            "znamenatel": str(raw.get("znamenatel") or "").strip(),
            "podpis_doli": str(raw.get("podpis_doli") or "").strip(),
            "podpis_ostatka": str(raw.get("podpis_ostatka") or "").strip()}


# ── геометрия ───────────────────────────────────────────────────────


def grid_shape(d, st=DEFAULT):
    """(столбцов, рядов, ширина фигурки, высота фигурки, просвет по x,
    просвет по y). Одно место на меру и на рисование."""
    cols = grid_cols(max(d["vsego"], 1))
    rows = max(1, math.ceil(max(d["vsego"], 1) / cols))
    gy_k = st.gap_y_frac
    fh = min(st.fig_h_max,
             st.grid_h_max / (rows + (rows - 1) * gy_k))
    fw = fh * st.fig_ar
    return cols, rows, fw, fh, fw * st.gap_x_frac, fh * gy_k


def grid_w(d, st=DEFAULT):
    cols, _r, fw, _fh, gx, _gy = grid_shape(d, st)
    return cols * fw + (cols - 1) * gx


def grid_h(d, st=DEFAULT):
    _c, rows, _fw, fh, _gx, gy = grid_shape(d, st)
    return rows * fh + (rows - 1) * gy


def leg_w(d, w, st=DEFAULT):
    return max(1.2, w - grid_w(d, st) - st.col_gap)


def _leg_runs(count, podpis, total, st):
    """Подпись одной группы: число СО СВОЕЙ БАЗОЙ, затем что делали.

    База повторена в каждой подписи нарочно. Строка «5 — генерировали»
    верна только пока зал помнит, из скольких; строка «5 из 100 —
    генерировали» верна сама по себе, а кадр читают и по снимку, без
    лектора."""
    return [{"text": f"{count} из {total}", "size": st.leg_num_pt,
             "bold": True, "color": DEEP},
            {"text": f"  {podpis}" if podpis else "", "size": st.leg_txt_pt,
             "color": DEEP}]


def leg_h(d, w, st=DEFAULT):
    lw = leg_w(d, w, st)
    _c, _r, fw, _fh, _gx, _gy = grid_shape(d, st)
    tw = max(0.4, lw - fw * st.leg_fig_k - st.leg_fig_gap)
    h, n = 0.0, 0
    for cnt, pod in ((d["dolya"], d["podpis_doli"]),
                     (d["vsego"] - d["dolya"], d["podpis_ostatka"])):
        if cnt <= 0:
            continue
        h += metrics.runs_h(_leg_runs(cnt, pod, d["vsego"], st), tw,
                            st.leg_ls)
        n += 1
    return h + st.leg_gap * max(0, n - 1)


def pikto_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что она отнимает у тела кадра."""
    return st.znam_h + st.znam_gap + max(grid_h(d, st), leg_h(d, w, st))


# ── сторожа ─────────────────────────────────────────────────────────


def check_pikto(sid, d, w, st=DEFAULT):
    """`[пиктограммы]`: нет знаменателя · доля больше целого · целое
    слишком велико либо слишком мало · группа без подписи."""
    if not d["znamenatel"]:
        report.warn(
            f"[пиктограммы] {sid}: не назван ЗНАМЕНАТЕЛЬ (`znamenatel`) — "
            f"{d['vsego']} фигурок ЧЕГО. Без него доля не "
            "интерпретируется: «5 из 100» читается одинаково про людей, "
            "про кадры и про доли рынка, а выводы из них разные "
            "(CLAUDE.md § «Baseline / Counterfactual Mandate»)")
    if d["dolya"] > d["vsego"]:
        report.warn(
            f"[пиктограммы] {sid}: доля {d['dolya']} больше целого "
            f"{d['vsego']} — части, которая больше своего целого, не "
            "бывает. Либо знаменатель назван не тот, либо это две разные "
            "базы и форма здесь не та")
    if d["dolya"] < 0:
        report.warn(
            f"[пиктограммы] {sid}: доля {d['dolya']} отрицательна — "
            "фигурок со знаком минус не бывает")
    elif d["dolya"] == 0:
        report.warn(
            f"[пиктограммы] {sid}: доля 0 — золотых фигурок на кадре не "
            "будет, и форма покажет ровно то же, что пустая сетка. "
            "Отсутствие доли утверждают словом, а не сотней контуров")
    if d["vsego"] > st.max_vsego:
        report.warn(
            f"[пиктограммы] {sid}: целое {d['vsego']} (> {st.max_vsego}) — "
            f"{d['vsego']} фигурок на кадре сольются в заливку, и доля "
            "перестанет пересчитываться взглядом. Приведите к сотне "
            "(«столько-то из ста») либо возьмите ось")
    if d["vsego"] < st.min_vsego:
        report.warn(
            f"[пиктограммы] {sid}: целое {d['vsego']} (< {st.min_vsego}) — "
            "на таком целом доля читается перечислением, а не площадью. "
            "Это кадр одного числа (`figure:`), а не сетка")
    if not d["podpis_doli"]:
        report.warn(
            f"[пиктограммы] {sid}: у доли нет подписи (`podpis_doli`) — "
            "золотые фигурки показывают, СКОЛЬКО, и молчат о том, ЧТО они "
            "делали; без этого сетка не утверждение, а узор")
    if d["vsego"] - d["dolya"] > 0 and not d["podpis_ostatka"]:
        report.warn(
            f"[пиктограммы] {sid}: у остатка нет подписи "
            "(`podpis_ostatka`) — а он здесь и есть содержание: «95 "
            "отбирали» это то, куда переехала работа")
    need = grid_w(d, st) + st.col_gap + 1.2
    if need > w:
        report.warn(
            f"[пиктограммы] {sid}: сетке с подписями нужно {need:.2f}\" при "
            f"колонке {w:.2f}\" — подписи сядут на фигурки")


# ── рисование ───────────────────────────────────────────────────────


def _trapezoid(s, x, y, w, h, *, fill, stroke, stroke_pt, adj=0.20):
    """Туловище фигурки.

    ПОЧЕМУ НЕ ЧЕРЕЗ `prims`. Трапеции в `prims.py` нет, а править ядро
    этим кругом нельзя: по его файлам идут ещё три нити, и правка в общем
    примитиве двигала бы их деки (`regress_decks` прогоняется отдельным
    шагом оркестратора). Поэтому фигура создаётся здесь, но всё, что в
    `prims` про ПОВЕДЕНИЕ фигуры, берётся оттуда: снятие тени темы
    (`no_shadow`, без него LibreOffice рисует мягкую тень по ссылке темы —
    `notes/mcp-limitations.md` [#223-8]) и счёт примитивов. Когда ядро
    снова можно будет трогать, эта функция переезжает в `prims` целиком."""
    shp = s.shapes.add_shape(MSO_SHAPE.TRAPEZOID, Inches(x), Inches(y),
                             Inches(w), Inches(h))
    try:
        shp.adjustments[0] = adj
    except Exception:
        pass
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if stroke is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = stroke
        shp.line.width = Pt(stroke_pt)
    prims.no_shadow(shp)
    report.PRIM["фигурка"] += 1
    return shp


def figurka(s, x, y, fw, fh, *, gold, st=DEFAULT):
    """Одна человеческая пиктограмма: круг-голова и трапеция-туловище.

    Доля — ЗАЛИВКА золотом, остаток — контур `#1C7293` без заливки. Разница
    держится не цветом линии, а наличием заливки: на снимке с задних рядов
    залитая фигурка читается пятном, контурная — нет, и это ровно то
    различение, ради которого форма существует."""
    hd = fh * st.head_frac
    neck = fh * st.neck_frac
    fill = GOLD if gold else None
    stroke = None if gold else LIGHT
    prims.rect(s, x + (fw - hd) / 2, y, hd, hd,
               GOLD if gold else WHITE,
               stroke=stroke, stroke_pt=st.stroke_pt,
               radius=True, radius_adj=0.5, count="фигурка")
    _trapezoid(s, x, y + hd + neck, fw, fh - hd - neck,
               fill=fill, stroke=stroke, stroke_pt=st.stroke_pt)


def draw_pikto(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Знаменатель строкой, сетка слева, подписи справа.
    Возвращает занятую высоту."""
    tag = tag or sid
    cols, rows, fw, fh, gx, gy = grid_shape(d, st)
    floor.pt(st.znam_pt, tag, "знаменатель сетки")
    prims.text_box(s, x, y, w, st.znam_h,
                   f"{d['vsego']} {d['znamenatel']}".strip(),
                   size=st.znam_pt, bold=True, color=MID, ls=1.0,
                   tag=f"{tag}/знаменатель", quiet=True)
    gy0 = y + st.znam_h + st.znam_gap
    n_gold = max(0, min(d["dolya"], d["vsego"]))
    for k in range(max(d["vsego"], 0)):
        r, c = divmod(k, cols)
        figurka(s, x + c * (fw + gx), gy0 + r * (fh + gy), fw, fh,
                gold=k < n_gold, st=st)
    if n_gold:
        report.GOLD_SEEN.add(sid)
    # Подписи справа, по центру высоты сетки: сетка узкая и высокая, и
    # прижатые к её верху подписи оставляли бы под собой мёртвое поле во
    # всю правую половину кадра.
    lx = x + grid_w(d, st) + st.col_gap
    lw = leg_w(d, w, st)
    sfw, sfh = fw * st.leg_fig_k, fh * st.leg_fig_k
    tw = max(0.4, lw - sfw - st.leg_fig_gap)
    items = [(d["dolya"], d["podpis_doli"], True),
             (d["vsego"] - d["dolya"], d["podpis_ostatka"], False)]
    items = [it for it in items if it[0] > 0]
    total = sum(metrics.runs_h(_leg_runs(c, p, d["vsego"], st), tw, st.leg_ls)
                for c, p, _g in items) + st.leg_gap * max(0, len(items) - 1)
    ly = gy0 + max(0.0, (grid_h(d, st) - total) / 2)
    for cnt, pod, gold in items:
        runs = _leg_runs(cnt, pod, d["vsego"], st)
        hh = metrics.runs_h(runs, tw, st.leg_ls)
        figurka(s, lx, ly + max(0.0, (hh - sfh) / 2), sfw, sfh, gold=gold,
                st=st)
        floor.pt(st.leg_txt_pt, tag, "подпись группы")
        prims.text_runs(s, lx + sfw + st.leg_fig_gap, ly, tw, hh, runs,
                        ls=st.leg_ls, align=PP_ALIGN.LEFT,
                        anchor=MSO_ANCHOR.MIDDLE,
                        tag=f"{tag}/подпись-{'доли' if gold else 'остатка'}")
        ly += hh + st.leg_gap
    report.PRIM["пиктограммы"] += 1
    return pikto_h(d, w, st)


# ── общий договор формы: parse · height · check · draw ───────────────

def parse(sid, raw, rows=None):
    return pikto_of(sid, raw)


def height(d, w):
    return pikto_h(d, w)


def check(sid, d, w):
    return check_pikto(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_pikto(s, sid, d, x, y, w, tag=tag)
