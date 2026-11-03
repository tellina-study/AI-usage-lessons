# -*- coding: utf-8 -*-
"""РАЗВИЛКА РЕШЕНИЯ `razvilka:` — критерий и два настоящих случая.

Перенос приёма §2.13 из `library/lectures/lec-08/rework-v5/
PERENOS-PRIYOMOV.md`: `image/s05` — вопрос в рамке сверху («Критерий задан
физикой и проверяемыми условиями?»), две ветки ДА / НЕТ, и под каждой —
настоящий случай с одинаковой тройкой строк: Инструмент / Результат /
Ограничения.

ЧТО ЭТА ФОРМА УТВЕРЖДАЕТ: «вот по какому признаку выбирают», и сразу — два
случая, разведённые этим признаком. Это прямая работа на правило курса
«≥30 % провалов, ограничений и альтернатив» (`CLAUDE.md`): критерий «когда
ИИ не нужен» показан РАЗВИЛКОЙ, а не оговоркой в конце абзаца.

ГЛАВНЫЙ СТОРОЖ ФОРМЫ — ОДИНАКОВЫЙ НАБОР СТРОК В ОБЕИХ ВЕТКАХ, И В ТОМ ЖЕ
ПОРЯДКЕ: «Одинаковость раскладки обязательна: сравнивают только то, что
разложено одинаково» (§2.13 переноса). Ветка «да» с тройкой «Инструмент /
Результат / Ограничения» и ветка «нет» с другой тройкой — это не развилка
одного признака, а два случая, сравнивать которые нечем.

ВОПРОС — ПЛАШКА `#21295C` С БЕЛЫМ ТЕКСТОМ, ветки — линии `#1C7293` с
подписями ДА / НЕТ. Золота в этой форме нет: она утверждает критерий и
случай, а не величину, и вводить золото ради самого правила «не реже раза
на кадр» значило бы раскрасить то, что ничего не выделяет (решение — на
уровне деки, не этой формы, см. `itog.py`/`vyvody.py` за соседство на
кадре).

Контракт фронтматтера:

    razvilka:
      vopros: "Критерий задан физикой и проверяемыми условиями?"
      da:
        image: "assets/screenshots/s42-peregorodka.png"   # необязательно
        head: "Бионическая перегородка"
        rows:
          - {label: "Инструмент", text: "САПР и оптимизация, не генеративная модель"}
          - {label: "Результат", text: "65 кг → 35 кг"}
          - {label: "Ограничения", text: "спора об авторстве нет"}
      net:
        head: "Баннеры журнала"
        rows: [...]                 # ТЕ ЖЕ label, в том же порядке
"""
from dataclasses import dataclass
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import floor, metrics, prims, report
from .theme import DEEP, LIGHT, MID, SURFACE, WHITE

TOP_KEYS = {"vopros", "da", "net"}
BRANCH_KEYS = {"image", "head", "rows"}
ROW_KEYS = {"label", "text"}


@dataclass(frozen=True)
class RazvilkaStyle:
    q_pad: float = 0.16
    q_pt: float = 16.0               # пол видимого слоя
    q_ls: float = 1.14
    q_gap: float = 0.16              # вопрос — линии веток
    tie_h: float = 0.30              # линия от вопроса до ветки
    tie_w: float = 0.026
    lab_pt: float = 13.0             # пол видимого слоя, подпись ДА/НЕТ
    gap: float = 0.30                # просвет между ветками
    pad: float = 0.16
    img_h: float = 1.75
    img_gap: float = 0.10
    head_pt: float = 15.0            # пол видимого слоя
    head_ls: float = 1.10
    head_gap: float = 0.10
    row_label_pt: float = 12.5       # пол видимого слоя
    row_text_pt: float = 12.5        # пол видимого слоя
    row_ls: float = 1.14
    row_label_gap: float = 0.03
    row_gap: float = 0.08
    min_branch_w: float = 2.80
    max_rows: int = 4
    min_rows: int = 2


DEFAULT = RazvilkaStyle()


# ── разбор поля ─────────────────────────────────────────────────────


def _row_of(sid, branch, i, raw):
    if not isinstance(raw, dict):
        report.warn(f"[развилка] {sid}: «{branch}», строка {i} — "
                    f"{type(raw).__name__}, а должна быть label/text")
        return None
    unknown = sorted(set(raw) - ROW_KEYS)
    if unknown:
        report.warn(f"[развилка] {sid}: «{branch}», строка {i} — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    label = str(raw.get("label") or "").strip()
    text = str(raw.get("text") or "").strip()
    if not label:
        report.warn(f"[развилка] {sid}: «{branch}», строка {i} без "
                    "`label` — без имени строки сравнение строк по имени "
                    "не построить")
    if not text:
        report.warn(f"[развилка] {sid}: «{branch}», строка {i} без `text`")
    if not label and not text:
        return None
    return {"label": label, "text": text}


def _branch_of(sid, name, raw, root=None):
    if not isinstance(raw, dict):
        report.warn(f"[развилка] {sid}: «{name}» — {type(raw).__name__}, а "
                    "должно быть image/head/rows")
        return None
    unknown = sorted(set(raw) - BRANCH_KEYS)
    if unknown:
        report.warn(f"[развилка] {sid}: «{name}» — ключ(и) "
                    f"{' · '.join(unknown)} ядро не читает")
    head = str(raw.get("head") or "").strip()
    if not head:
        report.warn(f"[развилка] {sid}: у ветки «{name}» нет `head` — "
                    "случай без названия ничего не называет")
    img = str(raw.get("image") or "").strip()
    path, exists = None, False
    if img:
        path = Path(img) if Path(img).is_absolute() else Path(root or ".") / img
        exists = path.exists()
        if not exists:
            report.warn(f"[развилка] {sid}: у ветки «{name}» изображения "
                        f"«{img}» нет на диске (искали {path})")
    rr = raw.get("rows")
    if not isinstance(rr, list) or not rr:
        report.warn(f"[развилка] {sid}: у ветки «{name}» нет `rows`")
        return None
    rows = []
    for i, r in enumerate(rr, 1):
        rw = _row_of(sid, name, i, r)
        if rw:
            rows.append(rw)
    if not rows:
        return None
    return {"head": head, "image": img, "path": path, "exists": exists,
            "rows": rows}


def razvilka_of(sl, st=DEFAULT, root=None):
    """Поле `razvilka` → разобранная развилка или None.

    `root` — каталог выпуска, от которого считается `da.image`/`net.image`,
    ровно как `media.media_path`/`vynoski.vynoski_of` считают свой путь:
    от папки выпуска, а не от корня репозитория
    (`notes/mcp-limitations.md` [#301-4])."""
    raw = sl.meta.get("razvilka")
    sid = sl.sid
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[развилка] {sid}: поле `razvilka` — "
                    f"{type(raw).__name__}, а должно быть vopros/da/net")
        return None
    unknown = sorted(set(raw) - TOP_KEYS)
    if unknown:
        report.warn(f"[развилка] {sid}: ключ(и) {' · '.join(unknown)} ядро "
                    "не читает")
    vopros = str(raw.get("vopros") or "").strip()
    if not vopros:
        report.warn(f"[развилка] {sid}: в `razvilka` нет `vopros` — "
                    "развилка без названного критерия — это просто два "
                    "случая рядом")
    da = _branch_of(sid, "da", raw.get("da"), root)
    net = _branch_of(sid, "net", raw.get("net"), root)
    if da is None or net is None or not vopros:
        return None
    da_labels = [r["label"] for r in da["rows"]]
    net_labels = [r["label"] for r in net["rows"]]
    if da_labels != net_labels:
        report.warn(
            f"[развилка] {sid}: набор строк разный — «да» "
            f"({' · '.join(da_labels) or '—'}), «нет» "
            f"({' · '.join(net_labels) or '—'}). Сравнивают только "
            "одинаково разложенное: строки обязаны идти в одном порядке и "
            "под одними именами в обеих ветках")
    return {"vopros": vopros, "da": da, "net": net}


# ── мера ────────────────────────────────────────────────────────────


def _longest(text, f):
    return max(text.split(), key=lambda x: metrics.text_w(x, f, True),
               default="")


def branch_w(w, st=DEFAULT):
    return (w - st.gap) / 2.0


def q_h(d, w, st=DEFAULT):
    return 2 * st.q_pad + metrics.est_h(d["vopros"], st.q_pt,
                                        max(0.3, w - 2 * st.q_pad), st.q_ls,
                                        True)


def _row_h(row, inner, st):
    lh = metrics.est_h(row["label"], st.row_label_pt, inner, 1.08, True) \
        if row["label"] else 0.0
    th = metrics.est_h(row["text"], st.row_text_pt, inner, st.row_ls) \
        if row["text"] else 0.0
    gap = st.row_label_gap if (row["label"] and row["text"]) else 0.0
    return lh + gap + th


def _branch_body_h(branch, bw, st=DEFAULT):
    inner = max(0.3, bw - 2 * st.pad)
    h = 0.0
    if branch["image"]:
        h += st.img_h + st.img_gap
    h += metrics.est_h(branch["head"], st.head_pt, inner, st.head_ls, True)
    h += st.head_gap
    n = len(branch["rows"])
    h += sum(_row_h(r, inner, st) for r in branch["rows"]) \
        + st.row_gap * max(0, n - 1)
    return h + 2 * st.pad


def razvilka_h(d, w, st=DEFAULT):
    """Высота формы — она же то, что форма отнимает у тела кадра."""
    bw = branch_w(w, st)
    body = max(_branch_body_h(d["da"], bw, st),
               _branch_body_h(d["net"], bw, st))
    return q_h(d, w, st) + st.q_gap + st.tie_h + body


# ── сторож ──────────────────────────────────────────────────────────


def check_razvilka(sid, d, w, st=DEFAULT):
    """`[развилка]`: ветка тесная · строк больше предела · строка одна ·
    слово шире ветки."""
    bw = branch_w(w, st)
    if bw < st.min_branch_w:
        report.warn(f"[развилка] {sid}: ветка вышла {bw:.2f}\" "
                    f"(< {st.min_branch_w:.2f}\") — тройке строк в такой "
                    "ширине не хватит места")
    for name, branch in (("да", d["da"]), ("нет", d["net"])):
        n = len(branch["rows"])
        if n > st.max_rows:
            report.warn(f"[развилка] {sid}: у ветки «{name}» строк {n} "
                        f"(> {st.max_rows}) — развилка держит тройку-"
                        "четвёрку, не разбор")
        if n < st.min_rows:
            report.warn(f"[развилка] {sid}: у ветки «{name}» строка одна")
        inner = max(0.3, bw - 2 * st.pad)
        for i, r in enumerate(branch["rows"], 1):
            for text, pt_, bold in ((r["label"], st.row_label_pt, True),
                                    (r["text"], st.row_text_pt, False)):
                if not text:
                    continue
                long = _longest(text, pt_)
                if long and metrics.text_w(long, pt_, bold) > inner * 72.0:
                    report.warn(
                        f"[развилка] {sid}: ветка «{name}», строка {i} — "
                        f"слову «{long}» не хватает ширины {inner:.2f}\" "
                        f"на {pt_:.1f} пт")


# ── рисование ───────────────────────────────────────────────────────


def _draw_branch(s, branch, x, y, bw, bh, st, tag):
    prims.ocean_box(s, x, y, bw, bh, fill=SURFACE, stroke=LIGHT,
                    stroke_pt=1.5)
    inner = max(0.3, bw - 2 * st.pad)
    cx = x + st.pad
    cy = y + st.pad
    if branch["image"]:
        prims.add_image(s, branch["path"], cx, cy, inner, st.img_h,
                        tag=f"{tag}/изображение")
        cy += st.img_h + st.img_gap
    floor.pt(st.head_pt, tag, "заголовок ветки развилки")
    hh = metrics.est_h(branch["head"], st.head_pt, inner, st.head_ls, True)
    prims.text_box(s, cx, cy, inner, hh, branch["head"], size=st.head_pt,
                   bold=True, color=DEEP, ls=st.head_ls,
                   tag=f"{tag}/заголовок")
    cy += hh + st.head_gap
    n = len(branch["rows"])
    for i, r in enumerate(branch["rows"], 1):
        if r["label"]:
            floor.pt(st.row_label_pt, tag, "ярлык строки развилки")
            lh = metrics.est_h(r["label"], st.row_label_pt, inner, 1.08, True)
            prims.text_box(s, cx, cy, inner, lh, r["label"],
                           size=st.row_label_pt, bold=True, color=MID,
                           ls=1.08, tag=f"{tag}/строка{i}/ярлык")
            cy += lh + (st.row_label_gap if r["text"] else 0.0)
        if r["text"]:
            floor.pt(st.row_text_pt, tag, "текст строки развилки")
            th = metrics.est_h(r["text"], st.row_text_pt, inner, st.row_ls)
            prims.text_box(s, cx, cy, inner, th, r["text"],
                           size=st.row_text_pt, color=DEEP, ls=st.row_ls,
                           tag=f"{tag}/строка{i}/текст")
            cy += th
        if i < n:
            cy += st.row_gap


def draw_razvilka(s, sid, d, x, y, w, st=DEFAULT, tag=None):
    """Вопрос сверху, две линии-ветки с подписями ДА/НЕТ, под ними —
    настоящие случаи с одинаковой раскладкой строк. Возвращает занятую
    высоту."""
    tag = tag or sid
    top = y
    qh = q_h(d, w, st)
    prims.rect(s, x, y, w, qh, DEEP, radius=True, radius_adj=0.10,
               count="вопрос развилки")
    floor.pt(st.q_pt, tag, "вопрос развилки")
    prims.text_box(s, x + st.q_pad, y, w - 2 * st.q_pad, qh, d["vopros"],
                   size=st.q_pt, bold=True, color=WHITE,
                   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                   ls=st.q_ls, tag=f"{tag}/вопрос")
    y += qh + st.q_gap
    bw = branch_w(w, st)
    bh = max(_branch_body_h(d["da"], bw, st), _branch_body_h(d["net"], bw, st))
    centers = (x + bw / 2, x + bw + st.gap + bw / 2)
    floor.pt(st.lab_pt, tag, "подпись ветки развилки")
    # Подпись ветки стоит РЯДОМ с линией, а не поверх неё: буквы и линия в
    # одной точке читаются нечитаемой кашей (поймано глазом на первом же
    # снимке — «Д|А», линия шла прямо сквозь литеры).
    for cx, lab in zip(centers, ("ДА", "НЕТ")):
        prims.rect(s, cx - st.tie_w / 2, y, st.tie_w, st.tie_h, LIGHT,
                   count="ветка развилки")
        lw = metrics.text_w(lab, st.lab_pt, True) / 72.0
        prims.text_box(s, cx + st.tie_w / 2 + 0.06, y + (st.tie_h - 0.20) / 2,
                       lw + 0.06, 0.20, lab, size=st.lab_pt, bold=True,
                       color=LIGHT, align=PP_ALIGN.LEFT, ls=1.0,
                       tag=f"{tag}/подпись-{lab}", quiet=True)
    y += st.tie_h
    _draw_branch(s, d["da"], x, y, bw, bh, st, f"{tag}/да")
    _draw_branch(s, d["net"], x + bw + st.gap, y, bw, bh, st, f"{tag}/нет")
    y += bh
    report.PRIM["развилка"] += 1
    return y - top
