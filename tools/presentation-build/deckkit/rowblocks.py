# -*- coding: utf-8 -*-
"""СТРОЧНЫЕ БЛОКИ `row_blocks:` — стек полноширинных блоков, не таблица.

§9 требований к форме даёт разбору «механизм / объяснение / последствия»
ДВЕ формы: таблицу (`columns`, три столбца через `mid`) либо строчные
блоки. Владелец, уточняя форму: «надо чтобы была структура в таблице или
строчных блоках — механизм, объяснение, последствия». Таблица готова
первой (#244, сессия кадров допуска); этот модуль — вторая форма, под
кадры, где владелец явно потребовал полноценное объяснение-предложение на
пункт («объяснение должно читаться без голоса лектора»), а не короткую
фразу в клетку — с 5-6 пунктами такой текст либо не влезает в столбец
`columns`, либо сжимается до нечитаемого (найдено сессией кадров о
влиянии ИИ на человека, #244, кадры `vliyanie-na-vracha`/`-patsienta`).

ЧЕМ ОТЛИЧАЕТСЯ ОТ `columns`. `columns` выравнивает пункты ПАРАМИ по
горизонтали — строка одного столбца стоит напротив строки другого, и
сторож `[пары]` это проверяет. Здесь пар нет: каждый блок — отдельная
коробка с НЕЗАВИСИМОЙ высотой, и если у одного пункта объяснение на три
строки, а у соседнего на одну, короткий не тянется и не ломает раскладку
длинного. Сторожу `[пары]` здесь нечего делать — он не вызывается вовсе.

Контракт фронтматтера:

    row_blocks:
      - {mechanism: "Якорение", explanation: "Заключение врача сдвигается
         к подсказке модели, даже когда она заведомо неверна.",
         metric: "23,6 против 92,8 верных из ста. 220 врачей"}
      - ...

`mechanism` — одним-двумя словами, то, что запомнят (полужирным, кегль не
ужимается: короткое слово не бывает слишком длинным). `explanation` —
самостоятельное предложение, без чисел (обычным начертанием). `metric` —
необязателен; когда есть, несёт замер (полужирным, бирюзой). Высота блока
— по собственному содержимому; кегль `explanation`/`metric` общий на ВЕСЬ
стек и подбирается лестницей, как у `columns.ITEM_HI/LO` — иначе пункты
набрались бы вразнобой, и глаз спотыкался бы о смену кегля посреди списка.
"""
from . import floor, metrics, prims, report
from .theme import DEEP, MID, SURFACE, TEAL

GAP = 0.14             # между блоками
PAD = 0.14              # поле внутри блока
ROW_GAP = 0.05           # между строками механизм/объяснение/последствия
MECH_PT = 13.5           # фиксирован: короткое слово не ужимается
BODY_HI, BODY_LO, BODY_FLOOR = 13.0, 11.0, 10.0
BODY_LS = 1.22
MIN_BLOCK_H = 0.50


def row_blocks_of(sl):
    """Поле `row_blocks` → список пунктов, или None. Чужая форма поля не
    роняет сборку — называется предупреждением `[строчные-блоки]`."""
    raw = sl.meta.get("row_blocks")
    if raw in (None, "", [], {}):
        return None
    if not isinstance(raw, list):
        report.warn(f"[строчные-блоки] {sl.sid}: поле `row_blocks` — "
                    f"{type(raw).__name__}, а должно быть списком")
        return None
    out = []
    for i, it in enumerate(raw, 1):
        if not isinstance(it, dict):
            report.warn(f"[строчные-блоки] {sl.sid}: пункт {i} не словарь")
            continue
        mech = str(it.get("mechanism") or "").strip()
        expl = str(it.get("explanation") or "").strip()
        metric = str(it.get("metric") or "").strip()
        if not mech or not expl:
            report.warn(f"[строчные-блоки] {sl.sid}: пункт {i} без "
                        "`mechanism` или `explanation`")
            continue
        out.append({"mechanism": mech, "explanation": expl,
                    "metric": metric})
    return out or None


def _block_h(item, iw, body_pt):
    h = 2 * PAD
    h += metrics.est_h(item["mechanism"], MECH_PT, iw, 1.14, True)
    h += ROW_GAP
    h += metrics.est_h(item["explanation"], body_pt, iw, BODY_LS)
    if item["metric"]:
        h += ROW_GAP
        h += metrics.est_h(item["metric"], body_pt, iw, 1.16, True)
    return max(MIN_BLOCK_H, h)


def row_blocks_h(items, w, *, floor_only=False):
    """Высота всего стека на подобранном кегле. `floor_only` меряет сразу
    на дне лестницы — используется, когда бюджет уже известен заранее и
    пересчитывать весь подбор незачем."""
    iw = max(0.3, w - 2 * PAD)
    body_pt = BODY_FLOOR if floor_only else BODY_HI
    heights = [_block_h(it, iw, body_pt) for it in items]
    return sum(heights) + GAP * (len(items) - 1)


def draw_row_blocks(s, sid, items, x, y, w, h, tag=None):
    """Стек блоков «механизм / объяснение / последствия», каждый — своя
    высота, без парного выравнивания. Кегль `explanation`/`metric` общий на
    стек, подбирается лестницей сверху вниз; не влезло и на дне —
    `[высота]`, блокирующее, как и везде в этом сборщике. Возвращает
    занятую высоту."""
    tag = tag or sid
    n = len(items)
    if n == 0:
        return 0.0
    iw = max(0.3, w - 2 * PAD)
    body_pt, heights, total = BODY_FLOOR, None, None
    f = BODY_HI
    while f >= BODY_FLOOR - 1e-9:
        hs = [_block_h(it, iw, f) for it in items]
        t = sum(hs) + GAP * (n - 1)
        if t <= h + 0.02:
            body_pt, heights, total = f, hs, t
            break
        f = round(f - 0.5, 1)
    if heights is None:
        body_pt = BODY_FLOOR
        heights = [_block_h(it, iw, body_pt) for it in items]
        total = sum(heights) + GAP * (n - 1)
        report.warn(
            f"[высота] {tag}/строчные-блоки: нужно {total:.2f}\" при "
            f"бюджете {h:.2f}\" даже на дне лестницы {BODY_FLOOR:.1f} пт — "
            f"{n} пунктов не умещаются, короче объяснения или меньше "
            "пунктов")
    floor.pt(body_pt, tag, "строчный блок, объяснение")
    yy = y
    for it, bh in zip(items, heights):
        prims.ocean_box(s, x, yy, w, bh, fill=SURFACE)
        ty = yy + PAD
        mh = metrics.est_h(it["mechanism"], MECH_PT, iw, 1.14, True)
        prims.text_box(s, x + PAD, ty, iw, mh, it["mechanism"],
                       size=MECH_PT, bold=True, color=MID, ls=1.14,
                       tag=f"{tag}/блок-механизм")
        ty += mh + ROW_GAP
        eh = metrics.est_h(it["explanation"], body_pt, iw, BODY_LS)
        prims.text_box(s, x + PAD, ty, iw, eh, it["explanation"],
                       size=body_pt, color=DEEP, ls=BODY_LS,
                       tag=f"{tag}/блок-объяснение")
        ty += eh
        if it["metric"]:
            ty += ROW_GAP
            mth = metrics.est_h(it["metric"], body_pt, iw, 1.16, True)
            prims.text_box(s, x + PAD, ty, iw, mth, it["metric"],
                           size=body_pt, bold=True, color=TEAL, ls=1.16,
                           tag=f"{tag}/блок-последствие")
        yy += bh + GAP
    report.PRIM["строчные блоки"] += 1
    return total
