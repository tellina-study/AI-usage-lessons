# -*- coding: utf-8 -*-
"""СХЕМА-КОНВЕЙЕР `scheme:` — порядок работы без полотна текста.

Владелец, разбор 2026-10-08: «две-три таких схемки простых нарисовать
наглядных и убрать полотно текста — будет лучше»; «типа текст → модель → …,
только не надо вот этот длинный пайплайн».

Контракт фронтматтера:

    scheme:
      caption: "подпись под схемой, необязательна"
      rows:
        - label: "Без модели"
          steps: ["чертёж", "вычитка инженером", "подпись"]
        - label: "С моделью"
          steps:
            - "чертёж"
            - {text: "модель отбирает спорное", ai: true}
            - "вычитка инженером"

Шаг с участием модели выделяется обводкой Gold. Определяется двумя
способами, и ЯВНЫЙ сильнее: поле `ai: true` у шага, иначе вхождение
«модель» / «нейросет» / «ИИ» / «машинн» в текст. Второй способ нужен, чтобы
схему можно было написать списком строк, первый — чтобы шаг «инженер
проверяет то, что отобрала модель» не считался шагом модели.

Больше четырёх шагов в ряду — `[схема]`: владелец прямо запретил длинные
конвейеры. По РЯДАМ предел мягче («один-два» из наказа круга заруби́ло бы
первую же настоящую схему — карта цикла изделия легла тремя рядами по 4·3·3,
и ни один ряд не длинный): предел три ряда, четвёртый — это тот же длинный
конвейер, сложенный вчетверо.

РАЗНОГЛАСИЕ ДВУХ СБОРЩИКОВ, РАЗОБРАННОЕ В ПОЛЬЗУ lec-06. Схем две, и они
не настройки одной:

* lec-06 ПОДБИРАЕТ один кегль на все шаги схемы — наибольший, при котором
  каждый шаг укладывается в три строки и ни одно его слово не шире бокса, —
  даёт боксу одну высоту на всю схему, выделяет шаг модели золотом и
  отдельно проверяет тесный бокс (`SCH_MIN_STEP_W`);
* lec-07 набирает шаги фиксированными 11,5 пт, даёт каждому ряду свою
  высоту и ни шага модели, ни тесного бокса не знает.

Взят lec-06 целиком, и это ОСОЗНАННЫЙ отказ от второй версии, а не сведение
её к набору чисел. Причина: фиксированный кегль переносит решение «влезает
ли» на предупреждение `[ширина]` от примитива надписи, то есть сообщает о
беде вместо того, чтобы её не допустить; подобранный кегль сначала пробует
уложиться. Выделение шага модели золотом — не украшение: схема «без модели /
с моделью» без него не сравнение, а два списка.

ЦЕНА ЭТОГО РЕШЕНИЯ, названная заранее: перевод Лекции 7 на это ядро
(этап 2) ПЕРЕНАБЕРЁТ её схемы — кегли шагов станут подобранными, высоты
рядов одинаковыми. Это видимая правка, и принимать её надо глазами.
"""
import re
from dataclasses import dataclass

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, GOLD, LIGHT, MID, SURFACE, WHITE

# «модел…» без «моделирован…»: стадия цикла «3. Моделирование» — не шаг
# модели, и золотом её выделять нельзя. Поймано на настоящем `s02`, где
# карта цикла изделия получила золотую обводку на стадии расчётов.
AI_WORD = re.compile(r"модел(?!иров)|нейросет|нейронн|машинн"
                     r"|\bии\b|\bai\b", re.I)


@dataclass(frozen=True)
class SchemeStyle:
    lab_w: float = 1.70            # колонка подписи ряда слева
    lab_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    lab_gap: float = 0.10
    step_hi: float = 13.5
    step_lo: float = 12.0          # пол видимого слоя, см. `floor.py`
    step_rows: int = 3             # строк текста в боксе шага
    step_pad: float = 0.09
    step_ls: float = 1.08
    box_min_h: float = 0.52
    box_extra: float = 0.20
    arrow_w: float = 0.30
    arrow_h: float = 0.16
    gap: float = 0.09              # просвет бокс — стрелка
    nogap: float = 0.16            # просвет бокс — бокс, когда стрелок нет
    row_gap: float = 0.18
    cap_pt: float = 12.0           # пол видимого слоя, см. `floor.py`
    cap_ls: float = 1.14
    cap_gap: float = 0.08
    ai_by_word: bool = True        # узнавать шаг модели шаблоном по словам
    max_steps: int = 4             # владелец: «не надо длинный пайплайн»
    max_rows: int = 3
    min_step_w: float = 0.95       # уже этого бокс не читается


DEFAULT = SchemeStyle()
# Числа Лекции 6 пришпилены теми, какими они были до поднятия пола видимого
# слоя в `DEFAULT` (круг #229). Пока здесь стояло `LEC06 = DEFAULT`, набор
# означал «что осталось от умолчаний сегодня», и первое же изменение
# умолчаний сдвинуло бы деку, прочитанную залу.
LEC06 = SchemeStyle(lab_pt=11.5, step_lo=9.0, cap_pt=11.0)


def scheme_of(sl, st=DEFAULT):
    """Поле `scheme` → разобранная схема или None."""
    raw = sl.meta.get("scheme")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[схема] {sl.sid}: поле `scheme` — "
                    f"{type(raw).__name__}, а должно быть caption/rows")
        return None
    rr = raw.get("rows")
    if not isinstance(rr, list) or not rr:
        report.warn(f"[схема] {sl.sid}: в `scheme` нет `rows`")
        return None
    rows = []
    for i, r in enumerate(rr, 1):
        if not isinstance(r, dict):
            report.warn(f"[схема] {sl.sid}: ряд {i} не label/steps")
            continue
        steps = []
        for item in (r.get("steps") or []):
            if isinstance(item, dict):
                t = str(item.get("text") or item.get("step") or "").strip()
                flag = item.get("ai")
            else:
                t, flag = str(item).strip(), None
            # ЯВНОЕ сильнее шаблона — в обе стороны, и `ai: false` тоже.
            # `ai_by_word=False` снимает шаблон целиком: дека, у которой он
            # измеренно врёт, объявляет шаг модели сама. Замерено на Лекции 7
            # (17 схем): шаблон золотит пять шагов, четыре из них по ошибке
            # («Отказ от модели бизнеса» — модель БИЗНЕСА, «Распечатка вывода
            # модели» — документ на столе, а не шаг), и пропускает те две
            # схемы, где шаг модели настоящий и в них весь смысл (`s18`
            # «без модели / с моделью», `s62` «было / стало»): там слово
            # «модель» стоит в ПОДПИСИ ряда, а не в тексте шага.
            if flag is not None:
                ai = bool(flag)
            else:
                ai = bool(AI_WORD.search(t)) if st.ai_by_word else False
            if t:
                steps.append({"text": t, "ai": ai})
        if not steps:
            report.warn(f"[схема] {sl.sid}: в ряду {i} нет шагов")
            continue
        rows.append({"label": str(r.get("label") or "").strip(),
                     "steps": steps})
    if not rows:
        return None
    sch = {"caption": str(raw.get("caption") or "").strip(), "rows": rows}
    sch["lab_w"] = st.lab_w if any(r["label"] for r in rows) else 0.0
    # `arrows: false` — ряд не конвейер, а перечень: четыре участника надзора
    # стоят рядом, и стрелка между ними соврала бы о порядке, которого нет.
    # Поле читается явно: ядро, которое его молча игнорировало, рисовало на
    # таком ряду три стрелки (`s70` Лекции 7) — то есть превращало состав
    # участников в последовательность.
    sch["arrows"] = raw.get("arrows", True) is not False
    return sch


def _box_gap(sch, st):
    """Просвет между боксами: со стрелкой внутри либо без неё."""
    if sch.get("arrows", True):
        return st.arrow_w + 2 * st.gap
    return st.nogap


def _step_w(sch, n, w, st):
    avail = w - sch["lab_w"] - (st.lab_gap if sch["lab_w"] else 0.0)
    return (avail - (n - 1) * _box_gap(sch, st)) / max(n, 1)


def _step_iw(sch, r, w, st):
    """Ширина ПОД ИЗМЕРЕНИЕ переноса внутри бокса шага — с тем же запасом
    `W_SAFE`, по той же причине: запас нужен решению «сколько строк»."""
    return max(0.3, (_step_w(sch, len(r["steps"]), w, st) - 2 * st.step_pad)
               * metrics.W_SAFE)


def _rows(text, f, iw):
    """Строк, которые займёт текст шага. `\n` — РАЗРЫВ АБЗАЦА, а не пробел:
    `text_box` рисует его отдельным абзацем, и мера обязана считать так же.
    Прежде здесь стоял `n_lines` по всей строке: он считал «Разработчик\nкон-
    тролирует…» одним потоком и недомеривал карточку участника на строку —
    бокс выходил ниже текста (`s70` Лекции 7). Та же арифметика, что в
    `metrics.est_h`, который `\n` делит с самого начала."""
    return sum(metrics.n_lines(p, f, iw, True) for p in text.split("\n"))


def _longest(text, f):
    """Самое ШИРОКОЕ слово шага: перенос идёт по пробелам, и слово шире
    бокса LibreOffice разорвёт посреди корня. На первой же настоящей схеме
    так вышло «Прототипировани/е»."""
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def _step_fits(sch, f, w, st):
    for r in sch["rows"]:
        iw = _step_iw(sch, r, w, st)
        for step in r["steps"]:
            if _rows(step["text"], f, iw) > st.step_rows:
                return False
            if metrics.text_w(_longest(step["text"], f), f, True) > iw * 72.0:
                return False
    return True


def step_size(sch, w, st=DEFAULT):
    """Один кегль на все шаги схемы: наибольший, при котором каждый шаг
    укладывается в свой бокс в три строки И ни одно слово не шире бокса."""
    f = st.step_hi
    while f > st.step_lo:
        if _step_fits(sch, f, w, st):
            break
        f -= 0.5
    return f


def _line_h(size, ls):
    return size * ls * metrics.LH / 72.0 * metrics.SAFE


def _box_h(sch, w, f, st):
    rows = max(min(st.step_rows,
                   _rows(step["text"], f,
                         max(0.3, _step_w(sch, len(r["steps"]), w, st)
                             - 2 * st.step_pad)))
               for r in sch["rows"] for step in r["steps"])
    return max(st.box_min_h, rows * _line_h(f, st.step_ls) + st.box_extra)


def _cap_h(sch, w, st):
    if not sch["caption"]:
        return 0.0
    return st.cap_gap + metrics.n_lines(sch["caption"], st.cap_pt, w) \
        * _line_h(st.cap_pt, st.cap_ls)


def scheme_h(sch, w, st=DEFAULT):
    """Высота схемы — она же то, что схема отнимает у тела кадра."""
    bh = _box_h(sch, w, step_size(sch, w, st), st)
    n = len(sch["rows"])
    return n * bh + st.row_gap * (n - 1) + _cap_h(sch, w, st)


def check_scheme(sid, sch, w, st=DEFAULT):
    """Блокирующие `[схема]`: длинный конвейер, разорванное слово, тесный
    бокс. Каждое — про то, что видно на экране, а не про вкус."""
    for i, r in enumerate(sch["rows"], 1):
        if len(r["steps"]) > st.max_steps:
            report.warn(
                f"[схема] {sid}: в ряду «{r['label'] or i}» "
                f"{len(r['steps'])} шагов (> {st.max_steps}) — длинный "
                "конвейер владельцем запрещён: «не надо вот этот длинный "
                "пайплайн»")
    if len(sch["rows"]) > st.max_rows:
        report.warn(
            f"[схема] {sid}: рядов {len(sch['rows'])} (> {st.max_rows}) — "
            "схема перестала быть сравнением и стала тем самым длинным "
            "конвейером, который запрещён")
    f = step_size(sch, w, st)
    for r in sch["rows"]:
        iw = _step_iw(sch, r, w, st)
        for step in r["steps"]:
            long = _longest(step["text"], f)
            if long and metrics.text_w(long, f, True) > iw * 72.0:
                report.warn(
                    f"[схема] {sid}: слову «{long}» нужно "
                    f"{metrics.text_w(long, f, True) / 72.0:.2f}\" при "
                    f"{f:.1f} пт, а бокс шага вышел {iw:.2f}\" — слово "
                    "будет разорвано переносом посреди корня")
    narrow = min(_step_w(sch, len(r["steps"]), w, st) for r in sch["rows"])
    if narrow < st.min_step_w:
        report.warn(
            f"[схема] {sid}: бокс шага вышел {narrow:.2f}\" "
            f"(< {st.min_step_w:.2f}\") — шагов в ряду или кадра на слайде "
            "слишком много для этой ширины")


def draw_scheme(s, sid, sch, x, y, w, st=DEFAULT, tag=None):
    """Схема-конвейер: ряды боксов со стрелками, подпись ряда слева.
    Возвращает занятую высоту."""
    tag = tag or sid
    f = step_size(sch, w, st)
    # Три класса текста схемы — против пола видимого слоя. Шаг назван
    # отдельно от подписи ряда и подписи схемы нарочно: подбирается только
    # он, остальные два — числа набора, и правятся они по-разному.
    floor.pt(f, tag, "шаг схемы")
    if any(r["label"] for r in sch["rows"]):
        floor.pt(st.lab_pt, tag, "подпись ряда схемы")
    if sch["caption"]:
        floor.pt(st.cap_pt, tag, "подпись схемы")
    bh = _box_h(sch, w, f, st)
    cy = y
    for i, r in enumerate(sch["rows"], 1):
        if r["label"]:
            prims.text_box(s, x, cy + 0.04, sch["lab_w"] - 0.12, bh - 0.08,
                           r["label"], size=st.lab_pt, bold=True, color=MID,
                           anchor=MSO_ANCHOR.MIDDLE, ls=1.10,
                           tag=f"{tag}/ряд{i}")
        cx = x + sch["lab_w"] + (st.lab_gap if sch["lab_w"] else 0.0)
        sw = _step_w(sch, len(r["steps"]), w, st)
        for j, step in enumerate(r["steps"], 1):
            if j > 1:
                if sch.get("arrows", True):
                    prims.arrow(s, cx + st.gap, cy + bh / 2 - st.arrow_h / 2,
                                st.arrow_w, st.arrow_h, LIGHT)
                cx += _box_gap(sch, st)
            prims.ocean_box(s, cx, cy, sw, bh,
                            fill=WHITE if step["ai"] else SURFACE,
                            stroke=GOLD if step["ai"] else LIGHT,
                            stroke_pt=2.0 if step["ai"] else 1.3)
            if step["ai"]:
                report.GOLD_SEEN.add(sid)
            prims.text_box(s, cx + st.step_pad, cy + 0.05,
                           sw - 2 * st.step_pad, bh - 0.10, step["text"],
                           size=f, bold=step["ai"], color=DEEP,
                           align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                           ls=st.step_ls, tag=f"{tag}/шаг{i}.{j}")
            cx += sw
        cy += bh + st.row_gap
    cy -= st.row_gap
    ch = _cap_h(sch, w, st)
    if ch:
        prims.text_box(s, x, cy + st.cap_gap, w, ch - st.cap_gap,
                       sch["caption"], size=st.cap_pt, italic=True,
                       color=LIGHT, ls=st.cap_ls, tag=f"{tag}/подпись")
        cy += ch
    report.PRIM["схема"] += 1
    return cy - y
