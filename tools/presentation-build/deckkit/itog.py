# -*- coding: utf-8 -*-
"""НИЖНЯЯ ПЛАШКА-ВЫВОД `itog:` — одна строка вместо стены прозы.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: вывод кадра. Не состав счёта (это полоса плашек),
не порядок (схема), не величину (кадр одного числа) — а ту единственную
фразу, ради которой кадр показан. Утверждение у неё ровно одно, и поэтому
строка у неё ровно одна.

ЗАЧЕМ ЗАВЕДЕНА, адресно. Разбор образцов (`PERENOS-PRIYOMOV.md` §2.6):
«почти на каждом кадре образца — полоса во всю ширину внизу: „Итог: …“,
„Вывод: …“, „Основной дефицит: …“. Одна-две строки, крупнее тела, в рамке.
У нас внизу кадра стоит СТЕНА ПРОЗЫ — три-четыре абзаца разбора. Видно на
наших s20 и s60: нижний блок занимает половину кадра и читается дольше, чем
лектор говорит». Там же названа цена перевода: «это самый дешёвый и самый
массовый выигрыш переноса» — проза уезжает в заметки, где ей и место по
нашим же правилам, на кадре остаётся одна строка вывода.

ПОЧЕМУ ЯРЛЫК — ЗАЛИВКА, А НЕ ЦВЕТ БУКВ. Главное правило перевода (§1 того же
файла): в образце фон тёмно-синий и золото работает ТЕКСТОМ (6,85 : 1 на
`#21295C`). У нас фон светлый, и то же золото текстом даёт **1,99 : 1 при
пороге 3,0** на белом и 1,85 на поверхности `#F4F7FA`. Это не мнение, это
замер `contrast.py`, и он уже ловил ровно эту ошибку на шестидесяти кадрах
Лекции 7 из ста девяти. Поэтому здесь золото — ЗАЛИВКА ярлыка, а текст
поверх неё глубокий `#21295C`: та же пара, развёрнутая в другую сторону,
даёт те же 6,85 : 1 и проходит оба порога. Правило блокирующее: золотой
текст на светлом в этой форме не появится никаким ключом, его просто нет.

ПОЧЕМУ КЕГЛЬ КРУПНЕЕ ТЕЛА. Вывод читают первым после заголовка, а не
последним. Ступень вверх от номинала тела деки (15 → 17 пт) — это то, что
отличает вывод от последнего абзаца разбора; на одном кегле с телом полоса
читается как ещё один абзац, только в рамке. Деке со своим номиналом служит
`style_for(base_pt)`, а не правка числа по месту.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не держит абзац. Третья строка — `[итог]`, и это
не придирка к объёму: фраза, которой нужно три строки, не вывод, а разбор, и
место ей в заметках. Форма, молча растянувшаяся на полкадра, вернула бы ту
самую стену прозы, от которой заведена.

Контракт фронтматтера:

    itog:
      yarlyk: "Что переехало"
      text: "подтверждение подлинности стало отдельной оплачиваемой работой"
"""
from dataclasses import dataclass, replace

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, markup, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, SURFACE

# Ключи, которые форма ЧИТАЕТ. Всё прочее называется `[итог]`: молчащий ключ
# хуже отсутствующего — порядный `arrows` на `s36` стоял, не читался, и
# закрывал находку от следующего читателя (README-formy, договор формы, п. 5).
KEYS = {"yarlyk", "text"}


@dataclass(frozen=True)
class ItogStyle:
    pad: float = 0.20            # поле внутри полосы
    chip_pt: float = 14.0        # пол видимого слоя, см. `floor.py`
    chip_pad: float = 0.15       # поле внутри ярлыка, с каждой стороны
    chip_h: float = 0.36
    chip_gap: float = 0.24       # просвет между ярлыком и строкой вывода
    text_pt: float = 17.0        # ступень ВВЕРХ от номинала тела (15 пт)
    text_ls: float = 1.16
    max_lines: int = 2           # третья строка — не вывод, а абзац
    max_yarlyk: int = 24         # знаков
    max_yarlyk_words: int = 3
    min_h: float = 0.68


DEFAULT = ItogStyle()


def style_for(base_pt, st=DEFAULT, step=2.0):
    """Стиль под номинал тела КОНКРЕТНОЙ деки: вывод на ступень крупнее.

    Числа 15 и 17 — номинал Лекции 7 и ступень от него; у деки с другим
    номиналом ступень обязана считаться от ЕЁ числа, иначе «крупнее тела»
    перестаёт быть правдой ровно там, где дека набрана плотнее обычного."""
    return replace(st, text_pt=float(base_pt) + step)


def itog_of(sl_or_sid, raw=None, st=DEFAULT):
    """Поле `itog` → разобранный вывод или None.

    Принимает и кадр (как `figure_of`), и пару «sid + словарь» (как
    `axis_of`): форма зовётся из двух мест — из раскладки деки по полю
    кадра и из пробы по готовому словарю, — и заводить два имени одному
    разбору значило бы развести две реализации одного смысла."""
    if raw is None:
        sid, raw = sl_or_sid.sid, sl_or_sid.meta.get("itog")
    else:
        sid = sl_or_sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[итог] {sid}: поле `itog` — {type(raw).__name__}, а "
                    "должно быть yarlyk/text")
        return None
    unknown = sorted(set(raw) - KEYS)
    if unknown:
        report.warn(
            f"[итог] {sid}: ключ(и) {' · '.join(unknown)} форма не читает — "
            "полоса вывода держит ровно ярлык и строку. Молчащий ключ хуже "
            "отсутствующего: он выглядит учтённым")
    text = str(raw.get("text") or "").strip()
    if not text:
        report.warn(f"[итог] {sid}: в `itog` нет `text` — полосе вывода "
                    "нечего вывести")
        return None
    return {"yarlyk": str(raw.get("yarlyk") or "").strip(), "text": text}


def chip_w(d, st=DEFAULT):
    """Ширина ярлыка по НАСТОЯЩЕЙ ширине его текста, а не по числу знаков."""
    if not d["yarlyk"]:
        return 0.0
    return metrics.text_w(d["yarlyk"], st.chip_pt, True) / 72.0 \
        + 2 * st.chip_pad


def text_w(d, w, st=DEFAULT):
    """Ширина, остающаяся строке вывода. Одно место на меру и на рисование."""
    cw = chip_w(d, st)
    return max(0.3, w - 2 * st.pad - cw - (st.chip_gap if cw else 0.0))


def _runs(d, st=DEFAULT):
    return markup.inline_runs(d["text"], st.text_pt, DEEP)


def n_lines(d, w, st=DEFAULT):
    """Сколько строк займёт вывод при этой ширине — число, по которому
    отказывает сторож. Считается ровно тем же разбором, каким рисуется."""
    return len(metrics.wrap_pieces(
        [(r["text"], r.get("size", st.text_pt), r.get("bold", False),
          r.get("italic", False)) for r in _runs(d, st)],
        text_w(d, w, st))) or 1


def itog_h(d, w, st=DEFAULT):
    """Высота полосы — она же то, что полоса отнимает у тела кадра."""
    th = metrics.runs_h(_runs(d, st), text_w(d, w, st), st.text_ls)
    body = max(th, st.chip_h if d["yarlyk"] else 0.0)
    return max(st.min_h, body + 2 * st.pad)


def itog_y(bot, d, w, st=DEFAULT):
    """Верх полосы, прижатой НИЗОМ к `bot`. Полоса стоит внизу кадра —
    считать её верх каждой деке самостоятельно значило бы завести столько
    же шансов разойтись с мерой."""
    return bot - itog_h(d, w, st)


def check_itog(sid, d, w, st=DEFAULT):
    """`[итог]`: третья строка · длинный ярлык · ярлык-фраза · ярлыка нет."""
    if not d["yarlyk"]:
        report.warn(
            f"[итог] {sid}: у полосы вывода не назван ЯРЛЫК (`yarlyk`) — "
            "без него полоса читается ещё одним абзацем тела, а не выводом, "
            "и золотого акцента на кадре не остаётся")
    else:
        n = len(d["yarlyk"])
        if n > st.max_yarlyk:
            report.warn(
                f"[итог] {sid}: ярлык «{d['yarlyk']}» — {n} знаков "
                f"(> {st.max_yarlyk}): это уже не ярлык, а начало вывода. "
                "Ярлык называет РОД вывода («Итог», «Цена», «Что "
                "переехало»), сам вывод идёт в `text`")
        words = len(d["yarlyk"].split())
        if words > st.max_yarlyk_words:
            report.warn(
                f"[итог] {sid}: в ярлыке «{d['yarlyk']}» {words} слова "
                f"(> {st.max_yarlyk_words}) — ярлык читают боковым зрением, "
                "по форме и цвету; фраза этого не даёт")
    ln = n_lines(d, w, st)
    if ln > st.max_lines:
        report.warn(
            f"[итог] {sid}: вывод занимает {ln} строки (> {st.max_lines}) "
            f"при колонке {text_w(d, w, st):.2f}\" — это не вывод, а абзац "
            "разбора. Место абзаца в заметках; на кадре остаётся одна фраза")


def draw_itog(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Полоса во всю ширину: ярлык золотой заливкой, вывод рядом.
    Возвращает занятую высоту."""
    tag = tag or sid
    h = itog_h(d, w, st)
    prims.ocean_box(s, x, y, w, h, fill=SURFACE, stroke=LIGHT, stroke_pt=1.5)
    cx = x + st.pad
    if d["yarlyk"]:
        cw = chip_w(d, st)
        floor.pt(st.chip_pt, tag, "ярлык вывода")
        # Золото — ЗАЛИВКА, текст поверх неё DEEP. Пара даёт 6,85 : 1 и
        # проходит оба порога WCAG; та же пара наоборот (золотой текст на
        # светлом) — 1,99 при пороге 3,0, см. шапку модуля.
        prims.chip(s, cx, y + (h - st.chip_h) / 2, cw, st.chip_h,
                   d["yarlyk"], fill=GOLD, color=DEEP, size=st.chip_pt,
                   bold=True, tag=f"{tag}/ярлык")
        report.GOLD_SEEN.add(sid)
        cx += cw + st.chip_gap
    tw = text_w(d, w, st)
    runs = _runs(d, st)
    floor.pt(st.text_pt, tag, "строка вывода")
    th = metrics.runs_h(runs, tw, st.text_ls)
    prims.text_runs(s, cx, y + (h - th) / 2, tw, th, runs, ls=st.text_ls,
                    align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE,
                    tag=f"{tag}/вывод")
    report.PRIM["итог"] += 1
    return h


# ── общий договор формы: parse · height · check · draw ───────────────

def parse(sid, raw, rows=None):
    return itog_of(sid, raw)


def height(d, w):
    return itog_h(d, w)


def check(sid, d, w):
    return check_itog(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_itog(s, sid, d, x, y, w, tag=tag)
