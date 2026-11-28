# -*- coding: utf-8 -*-
"""ИКОНКИ `ikonki:` — растровая иконка рядом с подписью, строкой-карточкой
или сеткой карточек N×M.

issue #355 §9.6: в ядре иконок не было вовсе. У Лекции 10 — ручной
pipeline (`assets/icons/*.png`, Lucide SVG → `rsvg-convert`, перекрашенные
в палитру заранее, не на лету) и ПОВТОРЯЮЩИЙСЯ раскладочный приём: строка
карточек с иконкой (`build_lec10_p1.py:493`, `stage_row`), сетка 2×2
(`build_lec10_p1.py:632`) и иконка рядом со стрелкой в схеме шага
(`build_lec10_p1.py:1043`) — три кадра писали одну и ту же геометрию
заново, потому что поднимать было некуда.

ЧЕГО ЭТОТ МОДУЛЬ НЕ ДЕЛАЕТ. Не ходит в сеть и не вызывает `rsvg-convert`:
сборка деки не имеет сетевых побочных эффектов (то же правило, что держит
`media.resolve_media`/`convert_if_needed` на конвертации локального файла).
Картинка берётся из каталога иконок деки (`icon_dir`, обычно
`<lec-root>/rendered/assets/icons/`), который заполняет ОТДЕЛЬНЫЙ
не-сборочный скрипт `fetch_icons.py` — Lucide SVG → `rsvg-convert` → PNG,
уже перекрашенный в палитру. Файла нет — `[иконка]` в отчёт, кадр
собирается без неё: тот же договор, что у `media.media_path` на
отсутствующем снимке.

Контракт фронтматтера:

    ikonki:
      mode: row                 # row (умолчание) | grid
      rows:                      # mode: row — приём `stage_row`
        - label: "Растениеводство — поле"
          arrows: true           # стрелка между карточками ряда
          items:
            - {icon: "sprout", text: "Севооборот и подготовка почвы"}
            - {icon: "wheat", text: "Посев"}
            - {icon: "leaf", text: "Защита растений", gold: true}
      cols: 2                    # mode: grid — сетка N колонок
      cards:
        - {icon: "users", text: "Дефицит рабочих рук"}
        - {icon: "handshake", text: "Консолидация", gold: true}

Заливка карточки — `prims.tint_box(tone="gold" if gold else "light")`:
иконки сразу встают на тинты, поднятые §9.7, а не на произвольный цвет."""
from pptx.enum.text import MSO_ANCHOR

from . import metrics, prims, report
from .theme import DEEP, GOLD, MID

KEYS = {"mode", "rows", "cols", "cards"}

LABEL_PT = 11.0
CARD_PT = 11.0
ICON_SIZE = 0.34
ROW_CARD_H = 0.58
ROW_GAP = 0.18
ROW_ARROW_GAP = 0.32
GRID_CARD_H = 0.90
GRID_ICON_SIZE = 0.40
GRID_GAP = 0.20
GRID_PT = 12.0


def draw_icon(s, icon_dir, name, x, y, size, *, tag=""):
    """PNG `{icon_dir}/{name}-48.png` (или `-96.png`, `.png`) квадратом
    `size`×`size`. Имя пустое или файла нет — `[иконка]` в отчёт, `False`
    — кадр собирается без неё, не падает."""
    name = (name or "").strip()
    if not name:
        return False
    for suffix in ("-48.png", "-96.png", ".png"):
        p = icon_dir / f"{name}{suffix}"
        if p.exists():
            prims.add_image(s, p, x, y, size, size, tag=tag or f"иконка/{name}")
            report.PRIM["иконка"] += 1
            return True
    report.warn(f"[иконка] {tag or name}: файла нет в «{icon_dir}» ни в "
                f"одном из размеров — кадр собирается без иконки «{name}»")
    return False


def ikonki_of(sl):
    """Поле `ikonki` → разобранный словарь или `None`. Чужая форма поля не
    роняет сборку: кадр собирается без иконок, предупреждение называет,
    чего не хватило — тот же договор, что у `plates.plates_of`."""
    raw = sl.meta.get("ikonki")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, dict):
        report.warn(f"[иконки] {sl.sid}: поле `ikonki` — "
                    f"{type(raw).__name__}, а должно быть словарём")
        return None
    mode = str(raw.get("mode") or "row").strip()
    if mode == "grid":
        cards = raw.get("cards") or []
        if not isinstance(cards, list) or not cards:
            report.warn(f"[иконки] {sl.sid}: `mode: grid` без `cards`")
            return None
        return {"mode": "grid", "cols": max(1, int(raw.get("cols") or 2)),
                "cards": cards}
    rows = raw.get("rows") or []
    if not isinstance(rows, list) or not rows:
        report.warn(f"[иконки] {sl.sid}: `mode: row` без `rows`")
        return None
    return {"mode": "row", "rows": rows}


def row_h(row, w, *, card_h=ROW_CARD_H, label_pt=LABEL_PT):
    h = 0.0
    label = str(row.get("label") or "").strip()
    if label:
        h += metrics.est_h(label, label_pt, w, 1.10, True) + 0.06
    return h + card_h


def draw_row(s, icon_dir, row, x, y, w, *, card_h=ROW_CARD_H,
            icon_size=ICON_SIZE, label_pt=LABEL_PT, card_pt=CARD_PT,
            tag=""):
    """Строка карточек «иконка + подпись» (приём `stage_row`): ряд ровных
    боксов, слева иконка, справа текст, по заказу — стрелка между
    карточками. Возвращает занятую высоту."""
    items = row.get("items") or []
    if not isinstance(items, list) or not items:
        report.warn(f"[иконки] {tag}: строка без `items` — не рисуется")
        return 0.0
    arrows = bool(row.get("arrows"))
    gap = ROW_ARROW_GAP if arrows else ROW_GAP
    yy = y
    label = str(row.get("label") or "").strip()
    if label:
        lh = metrics.est_h(label, label_pt, w, 1.10, True)
        prims.text_box(s, x, yy, w, lh, label, size=label_pt, bold=True,
                       color=MID, ls=1.10, tag=f"{tag}/подпись-строки")
        yy += lh + 0.06
    n = len(items)
    bw = max(0.3, (w - (n - 1) * gap) / n)
    bx = x
    for i, it in enumerate(items):
        if not isinstance(it, dict):
            report.warn(f"[иконки] {tag}: пункт {i + 1} не словарь")
            bx += bw + gap
            continue
        gold = bool(it.get("gold"))
        ctag = f"{tag}/карточка{i + 1}"
        prims.tint_box(s, bx, yy, bw, card_h, tone="gold" if gold else "light",
                       count="иконка-карточка")
        has_icon = draw_icon(s, icon_dir, it.get("icon"),
                             bx + 0.10, yy + (card_h - icon_size) / 2,
                             icon_size, tag=ctag)
        tx = bx + (0.10 + icon_size + 0.08 if has_icon else 0.14)
        tw = max(0.3, bx + bw - 0.10 - tx)
        text = str(it.get("text") or "").strip()
        if text:
            prims.text_box(s, tx, yy + 0.04, tw, card_h - 0.08, text,
                           size=card_pt, bold=True,
                           color=GOLD if gold else DEEP, ls=1.05,
                           anchor=MSO_ANCHOR.MIDDLE, tag=ctag)
        else:
            report.warn(f"[иконки] {ctag}: карточка без `text`")
        if arrows and i < n - 1:
            prims.arrow_lr(s, bx + bw + gap / 2 - 0.14,
                          yy + card_h / 2 - 0.10, 0.28, 0.20)
        bx += bw + gap
    return yy + card_h - y


def grid_h(cards, cols, *, card_h=GRID_CARD_H, gap=GRID_GAP):
    rows = -(-len(cards) // max(1, cols))
    return rows * card_h + (rows - 1) * gap


def draw_grid(s, icon_dir, cards, x, y, w, cols, *, card_h=GRID_CARD_H,
             icon_size=GRID_ICON_SIZE, gap=GRID_GAP, text_pt=GRID_PT,
             tag=""):
    """Сетка карточек N×M «иконка + подпись» (приём k-07). Возвращает
    занятую высоту."""
    cols = max(1, cols)
    cw = max(0.3, (w - (cols - 1) * gap) / cols)
    for i, it in enumerate(cards):
        col, r = i % cols, i // cols
        cx, cy = x + col * (cw + gap), y + r * (card_h + gap)
        ctag = f"{tag}/карточка{i + 1}"
        if not isinstance(it, dict):
            report.warn(f"[иконки] {ctag}: не словарь")
            continue
        gold = bool(it.get("gold"))
        prims.tint_box(s, cx, cy, cw, card_h, tone="gold" if gold else "light",
                       count="иконка-карточка")
        has_icon = draw_icon(s, icon_dir, it.get("icon"), cx + 0.14, cy + 0.14,
                             icon_size, tag=ctag)
        tx = cx + (0.14 + icon_size + 0.10 if has_icon else 0.16)
        tw = max(0.3, cx + cw - 0.14 - tx)
        text = str(it.get("text") or "").strip()
        if text:
            prims.text_box(s, tx, cy + 0.12, tw, card_h - 0.24, text,
                           size=text_pt, bold=True,
                           color=GOLD if gold else DEEP, ls=1.08, tag=ctag)
        else:
            report.warn(f"[иконки] {ctag}: карточка без `text`")
    return grid_h(cards, cols, card_h=card_h, gap=gap)


def ikonki_h(data, w):
    """Высота всего блока `ikonki` — то, что он отнимает у тела кадра."""
    if data["mode"] == "grid":
        return grid_h(data["cards"], data["cols"])
    rows = data["rows"]
    return (sum(row_h(r, w) for r in rows if isinstance(r, dict))
            + ROW_GAP * max(0, len(rows) - 1))


def draw_ikonki(s, icon_dir, data, x, y, w, tag=""):
    """Диспетчер по `mode` — то же место, что `scheme.draw_scheme` держит
    для `kind`. Возвращает занятую высоту."""
    if data["mode"] == "grid":
        return draw_grid(s, icon_dir, data["cards"], x, y, w, data["cols"],
                         tag=tag)
    yy = y
    for i, row in enumerate(data["rows"]):
        if not isinstance(row, dict):
            report.warn(f"[иконки] {tag}/ряд{i + 1}: не словарь")
            continue
        if i:
            yy += ROW_GAP
        yy += draw_row(s, icon_dir, row, x, yy, w, tag=f"{tag}/ряд{i + 1}")
    return yy - y
