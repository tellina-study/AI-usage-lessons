# -*- coding: utf-8 -*-
"""ТАЙМЛАЙН `timeline:` — две разновидности одной формы.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ, и почему разновидностей именно две:

* **СТАДИИ** (по умолчанию) — «все идут одним путём, но стоят в разных
  местах». Горизонтальная линия, на ней именованные стадии процесса, под
  линией — привязки, каждая своей выноской к своей точке. Утверждение несёт
  ПОЛОЖЕНИЕ привязки на линии: три страны, названные текстом, читаются
  перечнем; те же три, расставленные по стадиям, читаются расхождением.
* **СРОКИ** (`mode: sroki`) — «во столько раз быстрее», и это утверждение
  несёт ДЛИНА полосы. Две-четыре полосы разной длины на ОДНОЙ шкале, с
  названной единицей.

Обе взяты из разбора образцов (`PERENOS-PRIYOMOV.md` §2.5): «`image/s11` —
горизонтальная линия, пять именованных точек стадии процесса, и под ней
четыре страны, каждая привязана указателем к своей точке; `media/s07` — две
полосы сравнения сроков: исторический образец (14 лет) и нынешний переход
(18 месяцев), разной длины, на одной шкале».

ФЛАГОВ СТРАН ЗДЕСЬ НЕТ, И ЭТО РЕШЕНИЕ, А НЕ ПРОБЕЛ. §2.5 того же файла:
«Страны — СЛОВАМИ, без флагов (флаг на кадре курса читается как
политический знак, нам это не нужно)». Поэтому привязка — это ярлык
золотой заливкой со словом («США», «ЕС») и строка разбора под ним; рисовать
флаг форме нечем, и добавлять нечего.

ЗОЛОТО — ЗАЛИВКА, НЕ БУКВЫ. Общее правило перевода (§1): у образца фон
тёмный и золото работает текстом (6,85 : 1), у нас фон светлый и то же
золото текстом даёт 1,99 при пороге 3,0 (замер `contrast.py`). Ярлык
привязки и плашка срока — заливка `#F0AB00`, текст поверх неё `#21295C`.

ЧЕГО ЭТА ФОРМА НЕ ДЕЛАЕТ. Не растягивает линию по КАЛЕНДАРЮ: стадии стоят
на равных расстояниях, потому что это стадии процесса, а не даты. Форма,
которая расставила бы их по годам, утверждала бы «между первой и второй
прошло вдвое больше, чем между второй и третьей», — а этого содержания у
стадий нет. Где расстояние несёт смысл — там `mode: sroki` либо ось
(`scheme: kind: shkala`).

Контракт фронтматтера — СТАДИИ:

    timeline:
      unit: "стадия судебного пути"
      stages: ["Иск подан", "Мировое без признания вины", "Закон принят",
               "Закон в силе", "Окончательное решение"]
      marks:
        - at: 0
          head: "США"
          text: "авторства у сгенерированного без человека нет; решение
                 окончательное"
        - at: 2
          head: "ЕС"
          text: "раскрытие и маркировка обязательны; закон в силе с 2026 года"

Контракт фронтматтера — СРОКИ:

    timeline:
      mode: sroki
      unit: "месяцы"
      rows:
        - {label: "Исторический образец: нелинейный монтаж", value: 168,
           text: "14 лет до полного замещения плёнки"}
        - {label: "Генеративный звук", value: 18,
           text: "18 месяцев: с 10 % до более половины суточной загрузки"}
"""
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, markup, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, OUTLINE, SURFACE, TEAL

NEEDS_ROWS = False          # таймлайн читает `stages`/`marks` либо `rows`

MODES = ("stadii", "sroki")

# Ключи, которые форма ЧИТАЕТ, — по разновидности. Всё прочее называется
# `[таймлайн]`: молчащий ключ выглядит учтённым и закрывает находку от
# следующего читателя (README-formy, общий договор формы, п. 5).
KEYS_STADII = {"mode", "unit", "stages", "marks", "caption"}
KEYS_SROKI = {"mode", "unit", "rows", "caption"}
MARK_KEYS = {"at", "head", "text"}
ROW_KEYS = {"label", "value", "text"}


@dataclass(frozen=True)
class TimelineStyle:
    # ── общее ────────────────────────────────────────────────────────
    unit_pt: float = 12.0        # пол видимого слоя, см. `floor.py`
    unit_h: float = 0.24
    unit_gap: float = 0.16
    cap_pt: float = 12.0
    cap_ls: float = 1.14
    cap_gap: float = 0.10
    # ── стадии ───────────────────────────────────────────────────────
    line_h: float = 0.055
    dot_d: float = 0.18
    stage_pt: float = 13.0
    stage_ls: float = 1.10
    stage_gap: float = 0.12      # просвет «подпись стадии → точка»
    lead_h: float = 0.36         # длина выноски от точки до коробки
    lead_w: float = 0.032        # толщина выноски
    box_pad: float = 0.14
    head_pt: float = 13.0        # пол видимого слоя
    head_h: float = 0.30
    head_pad: float = 0.14       # поле внутри ярлыка привязки
    head_gap: float = 0.09
    txt_pt: float = 12.5         # пол видимого слоя
    txt_ls: float = 1.14
    mark_w_max: float = 3.70
    mark_w_min: float = 1.55
    col_gap: float = 0.16        # просвет между коробками соседних стадий
    row_gap: float = 0.13        # между коробками ОДНОЙ стадии
    min_stages: int = 3
    max_stages: int = 6
    min_marks: int = 2
    max_marks: int = 5
    # ── сроки ────────────────────────────────────────────────────────
    lab_pt: float = 14.0
    lab_ls: float = 1.10
    bar_h: float = 0.34
    bar_gap: float = 0.09        # «подпись полосы → полоса»
    val_pt: float = 13.0
    val_pad: float = 0.15
    val_gap: float = 0.13        # «конец полосы → плашка значения»
    srok_txt_pt: float = 13.0
    srok_txt_ls: float = 1.14
    srok_txt_gap: float = 0.08
    srok_gap: float = 0.22       # между строками сроков
    min_bar: float = 0.12        # короче — полосы на экране нет
    min_rows: int = 2
    max_rows: int = 4
    rule_h: float = 0.035
    rule_gap: float = 0.16
    end_pt: float = 12.0
    end_h: float = 0.24


DEFAULT = TimelineStyle()


def _num(raw):
    """Число из значения срока. Принимает и число, и строку — «1 000» с
    пробелом-разделителем и «1,5» с запятой: во фронтматтере деки числа
    пишутся так же, как на экране."""
    if isinstance(raw, bool):
        return None
    if isinstance(raw, (int, float)):
        return float(raw)
    s = str(raw or "").strip().replace("−", "-").replace(" ", "") \
                              .replace(" ", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def _fmt(v):
    return (str(int(v)) if abs(v - round(v)) < 1e-9
            else f"{v:.1f}".replace(".", ","))


# ════════════════════════════════════════════════════════════════════
# разбор
# ════════════════════════════════════════════════════════════════════


def timeline_of(sl_or_sid, raw=None, st=DEFAULT):
    """Поле `timeline` → разобранный таймлайн или None.

    Принимает и кадр, и пару «sid + словарь» — по той же причине, что
    `itog.itog_of`: форма зовётся из раскладки деки и из пробы, и два
    имени одному разбору развели бы две реализации одного смысла."""
    if raw is None:
        sid, raw = sl_or_sid.sid, sl_or_sid.meta.get("timeline")
    else:
        sid = sl_or_sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[таймлайн] {sid}: поле `timeline` — "
                    f"{type(raw).__name__}, а должно быть "
                    "stages/marks либо mode: sroki + rows")
        return None
    mode = str(raw.get("mode") or "stadii").strip()
    if mode not in MODES:
        report.warn(
            f"[таймлайн] {sid}: разновидность «{mode}» не та — форма знает "
            f"{' и '.join(MODES)}. Стадии показывают, КТО ГДЕ стоит на "
            "общем пути; сроки — ВО СКОЛЬКО РАЗ быстрее, длиной полосы")
        return None
    return (_sroki_of if mode == "sroki" else _stadii_of)(sid, raw, st)


def _unknown(sid, raw, keys, where):
    bad = sorted(set(raw) - keys)
    if bad:
        report.warn(
            f"[таймлайн] {sid}: {where} — ключ(и) {' · '.join(bad)} форма не "
            "читает. Молчащий ключ хуже отсутствующего: он выглядит учтённым")


def _stadii_of(sid, raw, st):
    _unknown(sid, raw, KEYS_STADII, "стадии")
    stages = raw.get("stages")
    if not isinstance(stages, list) or not stages:
        report.warn(
            f"[таймлайн] {sid}: у разновидности «стадии» нет `stages` — "
            "линия без именованных точек не линия пути, а черта")
        return None
    names = []
    for i, sname in enumerate(stages, 1):
        t = str(sname or "").strip()
        if not t:
            report.warn(f"[таймлайн] {sid}: стадия {i} без названия — точка "
                        "на линии, о которой нечего сказать")
        names.append(t)
    mm = raw.get("marks")
    if not isinstance(mm, list):
        mm = []
    marks = []
    for i, m in enumerate(mm, 1):
        if not isinstance(m, dict):
            report.warn(f"[таймлайн] {sid}: привязка {i} не at/head/text")
            continue
        _unknown(sid, m, MARK_KEYS, f"привязка {i}")
        at = m.get("at")
        if isinstance(at, bool) or not isinstance(at, int):
            at_n = _num(at)
            if at_n is None or abs(at_n - round(at_n)) > 1e-9:
                report.warn(
                    f"[таймлайн] {sid}: у привязки «{m.get('head') or i}» "
                    f"`at` = «{at}» — это НОМЕР стадии (от 0), а не "
                    "название и не дата")
                continue
            at = int(round(at_n))
        if not 0 <= at < len(names):
            report.warn(
                f"[таймлайн] {sid}: привязка «{m.get('head') or i}» указывает "
                f"на стадию {at}, а стадий {len(names)} (номера от 0 до "
                f"{len(names) - 1}) — привязывать не к чему")
            continue
        marks.append({"at": at,
                      "head": str(m.get("head") or "").strip(),
                      "text": str(m.get("text") or "").strip()})
    return {"mode": "stadii", "stages": names, "marks": marks,
            "unit": str(raw.get("unit") or "").strip(),
            "caption": str(raw.get("caption") or "").strip()}


def _sroki_of(sid, raw, st):
    _unknown(sid, raw, KEYS_SROKI, "сроки")
    rr = raw.get("rows")
    if not isinstance(rr, list) or not rr:
        report.warn(
            f"[таймлайн] {sid}: у разновидности «сроки» нет `rows` — "
            "сравнивать длиной нечего")
        return None
    rows = []
    for i, r in enumerate(rr, 1):
        if not isinstance(r, dict):
            report.warn(f"[таймлайн] {sid}: срок {i} не label/value/text")
            continue
        _unknown(sid, r, ROW_KEYS, f"срок {i}")
        v = _num(r.get("value"))
        if v is None:
            report.warn(
                f"[таймлайн] {sid}: у срока «{r.get('label') or i}» значение "
                f"«{r.get('value')}» не число — длину полосы отложить не от "
                "чего. Словесный срок живёт плашкой, не полосой")
            continue
        if v <= 0:
            report.warn(
                f"[таймлайн] {sid}: у срока «{r.get('label') or i}» значение "
                f"{_fmt(v)} — полосы нулевой и отрицательной длины не бывает")
            continue
        rows.append({"label": str(r.get("label") or "").strip(),
                     "v": v, "shown": _fmt(v),
                     "text": str(r.get("text") or "").strip()})
    if not rows:
        return None
    return {"mode": "sroki", "rows": rows,
            "unit": str(raw.get("unit") or "").strip(),
            "caption": str(raw.get("caption") or "").strip()}


# ════════════════════════════════════════════════════════════════════
# стадии: геометрия
# ════════════════════════════════════════════════════════════════════


def lane_w(d, w, st=DEFAULT):
    """Ширина дорожки подписи одной стадии.

    Выведена, а не назначена: крайние подписи центрируются на крайних
    точках, значит поле с каждой стороны ровно половина дорожки, и тогда
    `n·lane = w`. Назначенное число поле и дорожку рассогласовывает —
    первая и последняя подписи уезжают за край кадра, а `[высота]` этого
    не видит: надпись не наезжает ни на что, она просто вне страницы
    (`notes/mcp-limitations.md` [#301-7])."""
    return w / max(len(d["stages"]), 1)


def stage_x(i, d, x, w, st=DEFAULT):
    n = len(d["stages"])
    if n < 2:
        return x + w / 2
    side = lane_w(d, w, st) / 2
    return x + side + (w - 2 * side) * i / (n - 1)


def stages_h(d, w, st=DEFAULT):
    """Высота дорожки подписей стадий — по тому, что в ней написано.

    Постоянным числом эта высота лгала бы в обе стороны (замер оси,
    `axis.lanes_h`): однострочная подпись оставляет пустоту, трёхстрочная
    молча лезет в заголовок кадра."""
    lw = lane_w(d, w, st)
    return max((metrics.est_h(t, st.stage_pt, lw, st.stage_ls, True)
                for t in d["stages"] if t), default=st.stage_pt / 72.0)


def line_cy(d, y, w, st=DEFAULT):
    """Центр линии при блоке, начатом в `y`. Одно место на меру и на
    рисование: две формулы одного числа расходятся на первой правке."""
    return y + stages_h(d, w, st) + st.stage_gap + st.dot_d / 2


def _cols(d):
    """Стадии, на которых стоят привязки, по порядку слева направо."""
    return sorted({m["at"] for m in d["marks"]})


def _slots(d):
    """Привязка → (столбец, ярус). Ярус нужен там, где на одну стадию
    село больше одной привязки: накладывать их друг на друга нельзя, и
    разводятся они ВНИЗ, оставаясь на своём столбце."""
    out, seen = {}, {}
    for i, m in enumerate(d["marks"]):
        r = seen.get(m["at"], 0)
        seen[m["at"]] = r + 1
        out[i] = (m["at"], r)
    return out


def mark_w(d, w, st=DEFAULT):
    """Ширина коробки привязки: одна на все, по числу занятых столбцов."""
    n = max(len(_cols(d)), 1)
    return max(st.mark_w_min,
               min(st.mark_w_max, (w - (n - 1) * st.col_gap) / n))


def _head_w(head, st):
    if not head:
        return 0.0
    return metrics.text_w(head, st.head_pt, True) / 72.0 + 2 * st.head_pad


def mark_h(m, bw, st=DEFAULT):
    """Высота одной коробки привязки."""
    iw = max(0.3, bw - 2 * st.box_pad)
    h = 2 * st.box_pad
    if m["head"]:
        h += st.head_h + st.head_gap
    if m["text"]:
        h += metrics.est_h(m["text"], st.txt_pt, iw, st.txt_ls)
    return h


def tier_h(d, w, st=DEFAULT):
    """Высота каждого яруса привязок — наибольшая по ярусу, а не по кадру:
    ярус стоит одной строкой, и его низ задаёт самая высокая коробка."""
    bw = mark_w(d, w, st)
    slots, out = _slots(d), {}
    for i, m in enumerate(d["marks"]):
        _, r = slots[i]
        out[r] = max(out.get(r, 0.0), mark_h(m, bw, st))
    return [out[r] for r in sorted(out)]


def mark_box_x(i, d, x, w, st=DEFAULT):
    """Левый край коробки привязки: по центру своей точки, с зажимом в
    поля кадра. Зажим именно здесь, а не при рисовании: мера наложений
    обязана видеть те же числа, что рисунок."""
    bw = mark_w(d, w, st)
    cx = stage_x(d["marks"][i]["at"], d, x, w, st)
    return max(x, min(cx - bw / 2, x + w - bw))


def stadii_h(d, w, st=DEFAULT):
    """Высота таймлайна стадий — она же то, что он отнимает у тела кадра."""
    h = stages_h(d, w, st) + st.stage_gap + st.dot_d
    tiers = tier_h(d, w, st)
    if tiers:
        h += st.lead_h + sum(tiers) + st.row_gap * (len(tiers) - 1)
    if d["unit"]:
        h += st.unit_gap + st.unit_h
    if d["caption"]:
        h += st.cap_gap + metrics.est_h(d["caption"], st.cap_pt, w,
                                        st.cap_ls, False, True)
    return h


# ════════════════════════════════════════════════════════════════════
# сроки: геометрия
# ════════════════════════════════════════════════════════════════════


def val_w(d, st=DEFAULT):
    """Место под плашку значения — по САМОМУ ШИРОКОМУ значению набора.

    Место резервируется заранее и у всех строк одинаковое, поэтому самая
    длинная полоса никогда не упрётся в свою плашку: иначе значение села
    бы поверх конца полосы ровно у того срока, ради которого форма и
    поставлена."""
    return max((metrics.text_w(r["shown"], st.val_pt, True) / 72.0
                for r in d["rows"]), default=0.4) + 2 * st.val_pad


def bar_max(d, w, st=DEFAULT):
    return max(0.3, w - val_w(d, st) - st.val_gap)


def bar_w(r, d, w, st=DEFAULT):
    vmax = max(x["v"] for x in d["rows"])
    return bar_max(d, w, st) * r["v"] / vmax


def srok_row_h(r, w, st=DEFAULT):
    h = 0.0
    if r["label"]:
        h += metrics.est_h(r["label"], st.lab_pt, w, st.lab_ls, True) \
            + st.bar_gap
    h += st.bar_h
    if r["text"]:
        h += st.srok_txt_gap + metrics.est_h(r["text"], st.srok_txt_pt, w,
                                             st.srok_txt_ls)
    return h


def sroki_h(d, w, st=DEFAULT):
    """Высота сравнения сроков — она же то, что оно отнимает у тела."""
    h = sum(srok_row_h(r, w, st) for r in d["rows"]) \
        + st.srok_gap * (len(d["rows"]) - 1)
    h += st.rule_gap + st.rule_h + st.end_h
    if d["unit"]:
        h += st.unit_gap + st.unit_h
    if d["caption"]:
        h += st.cap_gap + metrics.est_h(d["caption"], st.cap_pt, w,
                                        st.cap_ls, False, True)
    return h


def timeline_h(d, w, st=DEFAULT):
    return (sroki_h if d["mode"] == "sroki" else stadii_h)(d, w, st)


# ════════════════════════════════════════════════════════════════════
# сторожа
# ════════════════════════════════════════════════════════════════════


def check_timeline(sid, d, w, st=DEFAULT):
    if not d["unit"]:
        report.warn(
            f"[таймлайн] {sid}: не названа ЕДИНИЦА (`unit`) — что именно "
            "отложено по линии. Без неё зал читает линию как календарь, а "
            "стадии стоят на равных расстояниях и календарём не являются")
    if d["mode"] == "sroki":
        _check_sroki(sid, d, w, st)
    else:
        _check_stadii(sid, d, w, st)


def _check_stadii(sid, d, w, st):
    """`[таймлайн]`: стадий мало или много · привязок мало или много ·
    привязка без головы либо без текста · подписи стадий сошлись ·
    коробки соседних столбцов наехали друг на друга."""
    n = len(d["stages"])
    if n < st.min_stages:
        report.warn(
            f"[таймлайн] {sid}: стадий {n} (< {st.min_stages}) — путь из "
            "двух точек это не путь, а пара. Две величины сравнивают осью "
            "(`scheme: kind: shkala`) либо двумя столбцами")
    if n > st.max_stages:
        report.warn(
            f"[таймлайн] {sid}: стадий {n} (> {st.max_stages}) — подписи "
            f"встают в дорожку {lane_w(d, w, st):.2f}\" и сходятся. Это "
            "уже не линия пути, а таблица стадий")
    k = len(d["marks"])
    if k < st.min_marks:
        report.warn(
            f"[таймлайн] {sid}: привязок {k} (< {st.min_marks}) — линия "
            "утверждает «все идут одним путём, но СТОЯТ В РАЗНЫХ МЕСТАХ»; "
            "одной привязке расходиться не с кем")
    if k > st.max_marks:
        report.warn(
            f"[таймлайн] {sid}: привязок {k} (> {st.max_marks}) — выноски "
            "перепутаются, и кадр перестанет читаться за один взгляд")
    for i, m in enumerate(d["marks"], 1):
        if not m["head"]:
            report.warn(
                f"[таймлайн] {sid}: у привязки {i} нет `head` — ярлыка, "
                "которым она названа (кто именно стоит на этой стадии). "
                "Золотой заливки на кадре при этом тоже не остаётся")
        if not m["text"]:
            report.warn(
                f"[таймлайн] {sid}: у привязки «{m['head'] or i}» нет "
                "`text` — ярлык без разбора утверждает только «они тут "
                "есть», а форма заведена показать, ЧЕМ они тут отличаются")
    # Подписи стадий сошлись — мерой по НАСТОЯЩЕЙ ширине слова, а не по
    # числу знаков: перенос идёт по пробелам, и рвётся строка на длинном
    # слове, а не на средней ширине (`metrics.longest_word_w`).
    lw = lane_w(d, w, st)
    for i, t in enumerate(d["stages"]):
        if not t:
            continue
        need = metrics.longest_word_w(t, st.stage_pt, True) / 72.0
        if need > lw * metrics.W_SAFE:
            report.warn(
                f"[таймлайн] {sid}: подписи стадии «{t}» нужно {need:.2f}\" "
                f"на слово, а дорожка {lw:.2f}\" — на экране слово разорвёт "
                "посреди корня либо надвинет на соседнюю стадию. Сокращают "
                "название стадии, а не кегль")
    # Коробки привязок наехали. Считается по тем же числам, какими они
    # рисуются (`mark_box_x`), и ЯРУСАМИ: разведённые по вертикали
    # коробки одной стадии наложением не являются — это и есть разведение.
    bw, slots = mark_w(d, w, st), _slots(d)
    by_tier = {}
    for i in range(len(d["marks"])):
        by_tier.setdefault(slots[i][1], []).append(i)
    for tier, idx in sorted(by_tier.items()):
        idx = sorted(idx, key=lambda i: d["marks"][i]["at"])
        for a, b in zip(idx, idx[1:]):
            xa = mark_box_x(a, d, 0.0, w, st)
            xb = mark_box_x(b, d, 0.0, w, st)
            if xb - xa < bw:
                report.warn(
                    f"[таймлайн] {sid}: привязки «{d['marks'][a]['head'] or a}»"
                    f" и «{d['marks'][b]['head'] or b}» на ярусе {tier + 1} "
                    f"стоят в {xb - xa:.2f}\" друг от друга при коробке "
                    f"{bw:.2f}\" — на экране они наложатся. Разнесите их по "
                    "стадиям, сократите разбор либо снимите одну привязку")


def _check_sroki(sid, d, w, st):
    """`[таймлайн]`: сроков мало или много · полоса не видна · срок без
    подписи."""
    n = len(d["rows"])
    if n < st.min_rows:
        report.warn(
            f"[таймлайн] {sid}: сроков {n} (< {st.min_rows}) — сравнение "
            "длиной требует второй длины. Одна величина во весь кадр — это "
            "`figure:`")
    if n > st.max_rows:
        report.warn(
            f"[таймлайн] {sid}: сроков {n} (> {st.max_rows}) — полосы "
            "перестают сравниваться попарно, и кадр превращается в график")
    for r in d["rows"]:
        if not r["label"]:
            report.warn(
                f"[таймлайн] {sid}: у срока «{r['shown']}» нет `label` — "
                "полоса без имени сравнивается ни с чем")
        bw = bar_w(r, d, w, st)
        if bw < st.min_bar:
            report.warn(
                f"[таймлайн] {sid}: полоса срока «{r['label'] or r['shown']}»"
                f" выходит {bw:.2f}\" (< {st.min_bar:.2f}\") — на экране её "
                "нет. Разрыв величин слишком велик для одной шкалы: такое "
                "отношение называют числом («в девять раз»), а не длиной")


# ════════════════════════════════════════════════════════════════════
# рисование
# ════════════════════════════════════════════════════════════════════


def _lead(s, x1, y1, x2, y2, st, color=MID):
    """Выноска «колено»: вниз от точки, вбок, вниз к коробке.

    Наклонной линией это было бы одной фигурой, но наклонную в pptx даёт
    либо соединитель, либо повёрнутый прямоугольник: первый не держит
    толщину на печати, второй считается тригонометрией в двух местах
    сразу. Колено из трёх прямоугольников рисуется теми же примитивами,
    какими нарисован весь кадр, и читается не хуже."""
    if abs(x2 - x1) < 0.02:
        prims.rect(s, x1 - st.lead_w / 2, y1, st.lead_w, max(0.0, y2 - y1),
                   color, count="выноска")
        return
    ey = (y1 + y2) / 2
    prims.rect(s, x1 - st.lead_w / 2, y1, st.lead_w, max(0.0, ey - y1),
               color, count="выноска")
    lo, hi = min(x1, x2), max(x1, x2)
    prims.rect(s, lo, ey - st.lead_w / 2, hi - lo + st.lead_w, st.lead_w,
               color, count="выноска")
    prims.rect(s, x2 - st.lead_w / 2, ey, st.lead_w, max(0.0, y2 - ey),
               color, count="выноска")


def _tail(s, sid, d, x, y, w, st, tag):
    """Единица и подпись под любой разновидностью. Возвращает новый низ."""
    if d["unit"]:
        y += st.unit_gap
        floor.pt(st.unit_pt, tag, "единица таймлайна")
        prims.text_box(s, x, y, w, st.unit_h, d["unit"], size=st.unit_pt,
                       bold=True, color=MID, align=PP_ALIGN.CENTER, ls=1.0,
                       tag=f"{tag}/единица", quiet=True)
        y += st.unit_h
    if d["caption"]:
        floor.pt(st.cap_pt, tag, "подпись таймлайна")
        ch = metrics.est_h(d["caption"], st.cap_pt, w, st.cap_ls, False, True)
        prims.text_box(s, x, y + st.cap_gap, w, ch, d["caption"],
                       size=st.cap_pt, italic=True, color=LIGHT,
                       ls=st.cap_ls, tag=f"{tag}/подпись")
        y += st.cap_gap + ch
    return y


def draw_stadii(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Линия со стадиями и привязками под ней. Возвращает занятую высоту."""
    tag = tag or sid
    lw = lane_w(d, w, st)
    up_h = stages_h(d, w, st)
    cy = line_cy(d, y, w, st)
    # Линия выходит за крайние точки на половину поля: путь не кончается
    # на последней названной стадии, и обрубленная по точкам линия
    # утверждала бы обратное.
    prims.rect(s, x + lw / 4, cy - st.line_h / 2, w - lw / 2, st.line_h,
               LIGHT, count="линия")
    for i, t in enumerate(d["stages"]):
        sx = stage_x(i, d, x, w, st)
        prims.rect(s, sx - st.dot_d / 2, cy - st.dot_d / 2, st.dot_d,
                   st.dot_d, MID, radius=True, radius_adj=0.5, count="точка")
        if not t:
            continue
        floor.pt(st.stage_pt, tag, "подпись стадии")
        prims.text_box(s, sx - lw / 2, y, lw, up_h, t, size=st.stage_pt,
                       bold=True, color=DEEP, align=PP_ALIGN.CENTER,
                       anchor=MSO_ANCHOR.BOTTOM, ls=st.stage_ls,
                       tag=f"{tag}/стадия{i + 1}")
    bw, slots, tiers = mark_w(d, w, st), _slots(d), tier_h(d, w, st)
    tops = []
    t0 = cy + st.dot_d / 2 + st.lead_h
    for r, th in enumerate(tiers):
        tops.append(t0)
        t0 += th + st.row_gap
    last_bottom = {}            # столбец → низ коробки предыдущего яруса
    for i, m in enumerate(d["marks"]):
        col, tier = slots[i]
        bx, by = mark_box_x(i, d, x, w, st), tops[tier]
        bh = mark_h(m, bw, st)
        if tier == 0:
            _lead(s, stage_x(col, d, x, w, st), cy + st.dot_d / 2,
                  bx + bw / 2, by, st)
        else:
            # Ярус ниже первого висит на СВОЕЙ стадии через коробку выше:
            # вести к нему отдельную выноску от точки значило бы провести
            # её сквозь чужую коробку.
            prims.rect(s, bx + bw / 2 - st.lead_w / 2, last_bottom[col],
                       st.lead_w, max(0.0, by - last_bottom[col]), LIGHT,
                       count="выноска")
        last_bottom[col] = by + bh
        prims.ocean_box(s, bx, by, bw, bh, fill=SURFACE, stroke=LIGHT,
                        stroke_pt=1.3)
        iy = by + st.box_pad
        if m["head"]:
            floor.pt(st.head_pt, tag, "ярлык привязки")
            prims.chip(s, bx + st.box_pad, iy, _head_w(m["head"], st),
                       st.head_h, m["head"], fill=GOLD, color=DEEP,
                       size=st.head_pt, bold=True, tag=f"{tag}/ярлык{i + 1}")
            report.GOLD_SEEN.add(sid)
            iy += st.head_h + st.head_gap
        if m["text"]:
            iw = bw - 2 * st.box_pad
            floor.pt(st.txt_pt, tag, "разбор привязки")
            th = metrics.est_h(m["text"], st.txt_pt, iw, st.txt_ls)
            prims.text_box(s, bx + st.box_pad, iy, iw, th, m["text"],
                           size=st.txt_pt, color=DEEP, ls=st.txt_ls,
                           tag=f"{tag}/привязка{i + 1}")
    bot = y + stages_h(d, w, st) + st.stage_gap + st.dot_d
    if tiers:
        bot += st.lead_h + sum(tiers) + st.row_gap * (len(tiers) - 1)
    bot = _tail(s, sid, d, x, bot, w, st, tag)
    report.PRIM["таймлайн"] += 1
    return bot - y


def draw_sroki(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Полосы сроков на одной шкале. Возвращает занятую высоту."""
    tag = tag or sid
    vw, bmax = val_w(d, st), bar_max(d, w, st)
    cy = y
    for i, r in enumerate(d["rows"]):
        if r["label"]:
            floor.pt(st.lab_pt, tag, "подпись срока")
            lh = metrics.est_h(r["label"], st.lab_pt, w, st.lab_ls, True)
            prims.text_box(s, x, cy, w, lh, r["label"], size=st.lab_pt,
                           bold=True, color=DEEP, ls=st.lab_ls,
                           tag=f"{tag}/срок{i + 1}")
            cy += lh + st.bar_gap
        bw = bar_w(r, d, w, st)
        # Первая полоса — классический либо исторический образец, с
        # которым сравнивают; остальные — то, что с ним сравнивают. Цвета
        # взяты из правила перевода §2.3: классика DEEP, модель TEAL.
        prims.rect(s, x, cy, max(bw, 0.02), st.bar_h,
                   DEEP if i == 0 else TEAL, count="полоса срока")
        floor.pt(st.val_pt, tag, "значение срока")
        prims.chip(s, x + bw + st.val_gap, cy, vw, st.bar_h, r["shown"],
                   fill=GOLD, color=DEEP, size=st.val_pt, bold=True,
                   tag=f"{tag}/значение{i + 1}")
        report.GOLD_SEEN.add(sid)
        cy += st.bar_h
        if r["text"]:
            floor.pt(st.srok_txt_pt, tag, "разбор срока")
            th = metrics.est_h(r["text"], st.srok_txt_pt, w, st.srok_txt_ls)
            prims.text_box(s, x, cy + st.srok_txt_gap, w, th, r["text"],
                           size=st.srok_txt_pt, color=DEEP,
                           ls=st.srok_txt_ls, tag=f"{tag}/разбор{i + 1}")
            cy += st.srok_txt_gap + th
        if i < len(d["rows"]) - 1:
            cy += st.srok_gap
    # Шкала под полосами: без неё «одна шкала» остаётся обещанием. Концы
    # названы по той же причине, по какой они названы у оси — окно без
    # подписанных границ читается как «от нуля до всего».
    cy += st.rule_gap
    prims.rect(s, x, cy, bmax, st.rule_h, OUTLINE, count="шкала")
    vmax = max(r["v"] for r in d["rows"])
    floor.pt(st.end_pt, tag, "конец шкалы сроков")
    prims.text_box(s, x, cy + st.rule_h + 0.02, 0.9, st.end_h, "0",
                   size=st.end_pt, color=LIGHT, ls=1.0, tag=f"{tag}/ноль",
                   quiet=True)
    prims.text_box(s, x + bmax - 0.9, cy + st.rule_h + 0.02, 0.9,
                   st.end_h, _fmt(vmax), size=st.end_pt, color=LIGHT,
                   align=PP_ALIGN.RIGHT, ls=1.0, tag=f"{tag}/предел",
                   quiet=True)
    cy += st.rule_h + st.end_h
    cy = _tail(s, sid, d, x, cy, w, st, tag)
    report.PRIM["таймлайн"] += 1
    return cy - y


def draw_timeline(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    f = draw_sroki if d["mode"] == "sroki" else draw_stadii
    return f(s, sid, d, x, y, w, st, tag)


# ── общий договор формы: parse · height · check · draw ───────────────

def parse(sid, raw, rows=None):
    return timeline_of(sid, raw)


def height(d, w):
    return timeline_h(d, w)


def check(sid, d, w):
    return check_timeline(sid, d, w)


def draw(s, sid, d, x, y, w, tag=None):
    return draw_timeline(s, sid, d, x, y, w, tag=tag)
