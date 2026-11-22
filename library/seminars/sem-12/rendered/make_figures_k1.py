#!/usr/bin/env python3
"""Программные схемы + настоящие изображения Семинара 12, Кейс 1
(«Что процесс пишет в индекс»), слайды n10–n24.

Источники чисел и фактов — `stend/zamery-k1/README.md` (целиком, включая
дополнение 2026-11-21) и `research/01-opisaniya-i-indeks.md`. Корпус — те же
30 сканов CORD, что Семинар 10 (`sem-10/stend/corpus/cord_sample/`,
read-only, НЕ копируется и не правится).

Два НАСТОЯЩИХ скриншота живого стенда (не схема — канон
`proektirovanie-keysa-i-voprosa.md` §2, `notes/mcp-limitations.md` [#233-8],
обход снят 2026-10-20) сняты `stend/zamery-k1/shoot_webhook_node.py` на
воркфлоу `s10-raw-openrouter` (id `S4AMVj1hVmcs4fe8`) и лежат в
`stend/zamery-k1/n8n-screenshots-raw/` — копируются сюда без перерисовки,
только лёгкий crop/safety-паддинг через Pillow (ImageMagick в этой среде
недоступна, см. `notes/mcp-limitations.md`).

    python3 make_figures_k1.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent.parent / "sem-10" / "stend" / "corpus" / "cord_sample"
RAW_SHOTS = HERE.parent / "stend" / "zamery-k1" / "n8n-screenshots-raw"

W_PX, H_PX = 1600, 680


# ── n11 — схема постановки (правило С1) ─────────────────────────────────────
# Сплошное — поток, уже работающий: фотография попадает в архив, модель её
# свободно описывает абзацем, абзац лежит в архиве как есть. Пунктирная
# золотая стрелка указывает на узел «что именно записать об изображении» —
# единственный шаг, который этот кейс решает заново.
SCENE_W_PX = 1700


def k1_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 420), W)
    d = ImageDraw.Draw(im)
    head(d, "Куда в потоке архива встаёт решение, что записать об изображении", sz=26)
    d.text((40, 58),
            "приём фотографии и генеративное описание уже работают — вопрос в том, "
            "чем именно описание должно быть",
            font=f(18), fill=LIGHT)

    y1, h1 = 120, 120
    nodes = [
        ("Фото в архив", "выпускной, открытый урок, стенд"),
        ("Модель описывает", "связный абзац, 3-6 предложений"),
        ("Абзац лежит в архиве", "ждёт запроса через месяц"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (SCENE_W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=19,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 290, 110
    goal_w = node_w + 60
    goal_x = xs[1] + node_w / 2 - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Решаем сегодня:", "чем именно описание должно быть"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, goal_x + goal_w / 2, y2, xs[1] + node_w / 2, y1 + h1,
          col=GOLD, wd=4, dash=True)

    save(im, "k1-shema-postanovka.png")


# ── n13 — реальный скан с сеткой патчей/тайлов ──────────────────────────────
# Настоящее изображение из корпуса CORD (read-only), поверх — наша разметка
# сеткой: кадр режется на патчи, патчи становятся входными токенами модели.
# Это не подделка (правило no-mock-fallbacks требует отличать «наша разметка
# на настоящем снимке» от «стилизованной карточки вместо снимка») — исходный
# скан не перерисован ни одним пикселем, только наложена сетка и подпись.
def k1_scan_grid():
    src = CORPUS / "receipt_28.jpg"
    photo = Image.open(src).convert("RGB")
    # вписываем в высоту ~720 px, сохраняя пропорции
    target_h = 720
    scale = target_h / photo.height
    photo = photo.resize((round(photo.width * scale), target_h), Image.LANCZOS)
    pad_top, pad_side, pad_bottom = 70, 40, 90
    canvas_w = photo.width + 2 * pad_side + 560
    canvas_h = pad_top + target_h + pad_bottom
    im = Image.new("RGB", (canvas_w, canvas_h), W)
    d = ImageDraw.Draw(im)
    head(d, "Настоящий скан CORD с нашей сеткой патчей", sz=26)
    im.paste(photo, (pad_side, pad_top))

    # сетка патчей поверх снимка — рисуем прямо на канве (после paste), т.к.
    # ImageDraw уже привязан к im
    cols, rows = 6, 9
    cw, ch = photo.width / cols, photo.height / rows
    for c in range(1, cols):
        x = pad_side + c * cw
        d.line([x, pad_top, x, pad_top + target_h], fill=(0x02, 0x80, 0x90, 160), width=2)
    for r in range(1, rows):
        y = pad_top + r * ch
        d.line([pad_side, y, pad_side + photo.width, y], fill=(0x02, 0x80, 0x90, 160), width=2)
    d.rectangle([pad_side, pad_top, pad_side + photo.width, pad_top + target_h],
                outline=LIGHT, width=3)

    # подпись-плашка справа от снимка
    rx = pad_side + photo.width + 36
    rw = canvas_w - rx - 30
    box(d, rx, pad_top + 40, rw, 170,
        [f"{cols}×{rows} = {cols * rows} патчей", "каждый патч → входные токены"],
        SURF, tc=DEEP, sz=22, outline=TEAL, where="подпись сетки")
    box(d, rx, pad_top + 230, rw, 170,
        ["Чем выше разрешение,", "тем больше патчей — и дороже вызов"],
        SURF, tc=DEEP, sz=20, outline=LIGHT, where="подпись цены")
    clabel(d, rx + rw / 2, pad_top + target_h - 60,
           "настоящий чек, корпус CORD", 15, MUTE, where="подпись корпуса")

    save(im, "k1-scan-grid.png")


# ── n14 — recall@1: 3 варианта × лёгкие/трудные запросы ─────────────────────
def _fmt_recall(n):
    """Подпись лёгкой полосы — произносимой дробью от сырья (16 запросов),
    не десятичной долей: «13 из 16», не «0,8125»."""
    return f"{n} из 16"


def k1_recall_chart():
    im = Image.new("RGB", (W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Доля запросов, где нужный документ оказался первым", sz=27)
    d.text((40, 56), "16 лёгких запросов (синяя полоса) и 3 трудных (бирюзовая)",
           font=f(18), fill=LIGHT)

    # Лёгкая полоса — ЧИСЛИТЕЛЬ из 16 запросов (13/16 = 0,8125 и т.д., сырьё
    # `stend/zamery-k1/README.md`, свод Замера №1); доля на кадре подаётся
    # произносимой дробью «13 из 16», не «0,8125».
    rows = [
        ("Поля", 13, 0.0),
        ("Подпись", 1, 0.0),
        ("Гибрид", 0, 0.0),
    ]
    chart_x, max_w = 360, 950
    bar_h, gap = 90, 46
    y = 150
    for name, light, hard in rows:
        clabel(d, chart_x - 170, y + bar_h / 2 - 12, name, 24, DEEP, b=True,
               where=f"метка {name}")
        # Синяя (MID) полоса — ЛЁГКИЕ запросы (16 штук), бирюзовая (TEAL) —
        # ТРУДНЫЕ (3 штуки). Цвет и подпись обязаны совпадать буквально —
        # P0-находка прошлого круга: подпись называла цвета наоборот тому,
        # что на самом деле нарисовано. `fit()` проверяет, что подпись не
        # вылезет за правый край холста (прошлый круг этого не проверял —
        # «0,8125 — лёгкие запросы» у «Поля» вышло за холст и обрезалось).
        lw = max(6, int(max_w * light / 16))
        d.rounded_rectangle([chart_x, y, chart_x + lw, y + bar_h * 0.55], radius=8,
                             fill=MID)
        clabel(d, chart_x + lw + 90, y + 16, _fmt_recall(light), 22, MID, b=True,
               where=f"число (лёгкие) {name}")
        hw = max(4, int(max_w * hard)) if hard > 0 else 4
        yy = y + bar_h * 0.62
        d.rounded_rectangle([chart_x, yy, chart_x + hw, yy + bar_h * 0.3], radius=6,
                             fill=TEAL)
        clabel(d, chart_x + hw + 90, yy - 2, f"{hard:.1f}".replace(".", ","), 17, TEAL,
               where=f"число (трудные) {name}")
        y += bar_h + gap

    save(im, "k1-recall-chart.png")


# ── n15 — каскад одной ошибки извлечения на три вопроса ─────────────────────
# Никаких системных id на кадре (receipt_NN, кодов запросов Л4/Л6/Л13) — зал
# узнаёт чек и вопрос по тому, что на них написано человеческим языком, не по
# нашим внутренним меткам. Формулировки — rework/section-1-keys-1.md.
def k1_cascade_diagram():
    im = Image.new("RGB", (W_PX, 520), W)
    d = ImageDraw.Draw(im)
    head(d, "Одна ошибка извлечения — три сломанных вопроса", sz=25)

    bx, by, bw, bh = 120, 110, 560, 150
    box(d, bx, by, bw, bh,
        ["Чек на 36 000: «поля» предсказали 14 000", "модель взяла сдачу вместо суммы покупки"],
        W, tc=RED, sz=19, outline=RED, where="узел ошибки")
    d.text((bx, by + bh + 14),
           "причина: в тексте чека рядом «сдача 14 000» и «итог 36 000» —",
           font=f(16), fill=MUTE)
    d.text((bx, by + bh + 38),
           "модель прочитала не ту строку",
           font=f(16), fill=MUTE)

    targets = [
        ("вопрос про вторую по малости сумму", "чужое место в ранжировании"),
        ("вопрос про третью по малости сумму", "сдвиг рангов той же ошибкой"),
        ("вопрос «ближе всего к 35 000»", "14 000 слишком далеко — не попало в первую тройку"),
    ]
    tx = bx + bw + 120
    tw = W_PX - tx - 40
    ty, th, tgap = 70, 120, 28
    cy0 = by + bh / 2
    for i, (q, why) in enumerate(targets):
        ty_i = ty + i * (th + tgap)
        box(d, tx, ty_i, tw, th, [q, why], SURF, tc=DEEP, sz=17,
            outline=LIGHT, where=f"цель {i + 1}")
        arrow(d, bx + bw, cy0, tx, ty_i + th / 2, col=RED, wd=3)
    save(im, "k1-cascade-diagram.png")


# ── n16 — вырожденный отказ: один документ отвечает почти на любой запрос ──
# Никаких system-id на кадре (было «receipt_08», «top-1») — документ назван
# тем, что в нём написано, «топ» — по-русски.
def k1_attractor_diagram():
    im = Image.new("RGB", (W_PX, 610), W)
    d = ImageDraw.Draw(im)
    head(d, "Один документ архива отвечает почти на любой запрос", sz=25)

    doc_w, doc_h = 460, 170
    doc_x = W_PX - doc_w - 90
    doc_y = 190
    box(d, doc_x, doc_y, doc_w, doc_h,
        ["чек с фразой «итоговая сумма 50,000»", "(гибрид)",
         "16 из 16 запросов (показаны 6 из 16)"],
        W, tc=DEEP, sz=17, outline=GOLD, where="документ-получатель")

    queries = ["наибольшая сумма", "наименьшая сумма", "диапазон 150–160 тыс",
               "ближе всего к 45 000", "третья по величине", "вторая по малости"]
    qx = 90
    qy0, qh, qgap = 70, 58, 20
    for i, q in enumerate(queries):
        qy = qy0 + i * (qh + qgap)
        box(d, qx, qy, 420, qh, [q], SURF, tc=DEEP, sz=16, outline=LIGHT,
            where=f"запрос {i}")
        arrow(d, qx + 420, qy + qh / 2, doc_x, doc_y + doc_h / 2, col=TEAL, wd=2)

    d.text((90, qy0 + len(queries) * (qh + qgap) + 20),
           "разные вопросы, разные формулировки — первым почти всегда выходит один и тот же чек",
           font=f(17), fill=MUTE)
    save(im, "k1-attractor-diagram.png")


# ── n20 — деградация: один скан × 2 раскладки × 3 разрешения (настоящие) ───
# Реальный поворот/обрезка — ДОСЛОВНО та же функция, что
# `stend/zamery-k1/harness2_lite.py::hard_layout_data_url`: поворот 12° +
# обрезка 4% с каждого края. Разрешение — та же шкала, что `SCALE_STEPS`.
def k1_degradation_grid():
    src = CORPUS / "receipt_00.jpg"
    orig = Image.open(src).convert("RGB")
    ow, oh = orig.size

    def easy(scale):
        tw, th = max(1, round(ow * scale)), max(1, round(oh * scale))
        return orig.resize((tw, th), Image.LANCZOS)

    def hard(scale):
        tw, th = max(1, round(ow * scale)), max(1, round(oh * scale))
        im2 = orig.rotate(12, expand=True, fillcolor=(255, 255, 255))
        ww, hh = im2.size
        im2 = im2.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
        return im2.resize((tw, th), Image.LANCZOS)

    steps = [("1/1", 1.0), ("1/16", 1 / 16), ("1/32", 1 / 32)]
    cell_h = 300
    cell_w = 230
    pad = 30
    label_h = 46
    label_col_w = 230
    cols, rows = 3, 2
    canvas_w = label_col_w + cols * cell_w + (cols + 1) * pad
    canvas_h = rows * (cell_h + label_h) + (rows + 1) * pad + 90
    im = Image.new("RGB", (canvas_w, canvas_h), W)
    d = ImageDraw.Draw(im)
    head(d, "Один скан, два способа снять, три разрешения", sz=26)
    d.text((pad, 60), "1/1 — полное разрешение · 1/16 и 1/32 — доля стороны кадра",
           font=f(16), fill=LIGHT)

    row_labels = [["лёгкий", "случай"], ["трудный случай:", "поворот 12°,", "обрезка 4%"]]
    for ri, maker in enumerate((easy, hard)):
        y0 = 90 + ri * (cell_h + label_h + pad)
        lbl = row_labels[ri]
        ly = y0 + cell_h / 2 - (len(lbl) * 24) / 2
        for k, ln in enumerate(lbl):
            d.text((pad, ly + k * 24), ln, font=f(17, True), fill=DEEP)
        for ci, (name, scale) in enumerate(steps):
            thumb = maker(scale)
            # масштабируем превью под клетку, сохраняя пропорции, крупно —
            # мелкие разрешения увеличены для показа деградации, а не чтобы
            # соврать про реальный размер файла (подпись называет реальные точки)
            disp = thumb.copy()
            ratio = min(cell_w / disp.width, cell_h / disp.height)
            disp = disp.resize((max(1, round(disp.width * ratio)),
                                 max(1, round(disp.height * ratio))), Image.NEAREST
                                if scale < 0.1 else Image.LANCZOS)
            x0 = label_col_w + pad + ci * (cell_w + pad)
            cx = x0 + (cell_w - disp.width) // 2
            cy = y0 + (cell_h - disp.height) // 2
            d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h], outline=LIGHT, width=2)
            im.paste(disp, (cx, cy))
            cap = f"{name} · {thumb.width}×{thumb.height} точек"
            clabel(d, x0 + cell_w / 2, y0 + cell_h + 8, cap, 14, MUTE,
                   where=f"подпись {name}/{ri}")
    save(im, "k1-degradation-grid.png")


# ── n21/n22 — пропуски против ложных тревог по разрешениям ──────────────────
def k1_fp_miss_chart():
    # Высота 640, не 560: строка-вывод под столбиками рисуется на y≈606 —
    # на холсте 560 она МОЛЧА обрезалась и на кадр не попадала вовсе
    # (замечено глазами при перерендере 2026-11-22).
    im = Image.new("RGB", (W_PX, 640), W)
    d = ImageDraw.Draw(im)
    head(d, "Пропуски против ложных тревог — лёгкий случай", sz=26)

    # Имена шагов — по-русски, с реальным разрешением той же стороны, что
    # на k1-degradation-grid.png (receipt_00, 432 px по длинной стороне на
    # полном разрешении, 432/16≈27 px, 432/32≈14 px) — не ключи JSON
    # (`full`/`sixteenth`/`thirtysecond`), которые были нарисованы раньше.
    # Числители/знаменатели — из сырья `stend/zamery-k1/raw/
    # case2_personal_data_results.json` (summary, лёгкая раскладка): пропуски
    # считаются из 6 позитивных чеков, ложные тревоги — из 9 негативных;
    # 0/6=0,000 · 1/6=0,167 · 2/6=0,333 и 5/9=0,556 · 7/9=0,778 · 6/9=0,667 —
    # те же доли, что были на фигуре, теперь со знаменателем на кадре.
    data = [
        ("полное (432 точки)", 0, 5),
        ("1/16 (27 точек)", 1, 7),
        ("1/32 (14 точек)", 2, 6),
    ]
    miss_total, fp_total = 6, 9
    chart_x, chart_w = 420, 1080
    bar_h, gap = 110, 50
    y = 120
    for name, miss_n, fp_n in data:
        miss, fp = miss_n / miss_total, fp_n / fp_total
        clabel(d, chart_x - 230, y + bar_h / 2 - 14, name, 22, DEEP, b=True,
               where=f"метка {name}")
        mw = max(4, int(chart_w * miss))
        d.rounded_rectangle([chart_x, y, chart_x + mw, y + bar_h * 0.42], radius=8,
                             fill=TEAL)
        d.text((chart_x + mw + 14, y - 2),
               f"пропуски {miss_n} из {miss_total} ({miss:.3f})".replace(".", ","),
               font=f(18), fill=TEAL)
        fw = max(6, int(chart_w * fp))
        yy = y + bar_h * 0.5
        d.rounded_rectangle([chart_x, yy, chart_x + fw, yy + bar_h * 0.42], radius=8,
                             fill=(0xB3, 0x26, 0x1E))
        d.text((chart_x + fw + 14, yy - 2),
               f"ложные тревоги {fp_n} из {fp_total} ({fp:.3f})".replace(".", ","),
               font=f(18, True), fill=(0xB3, 0x26, 0x1E))
        y += bar_h + gap
    d.text((chart_x, y + 6),
           "ложных тревог больше, чем пропусков, на пяти клетках из шести; "
           "на полном разрешении пропусков нет вовсе",
           font=f(17), fill=MUTE)
    save(im, "k1-fp-miss-chart.png")


# ── n18/n19 — настоящие скриншоты живого стенда ─────────────────────────────
# Копируются БЕЗ перерисовки из stend/zamery-k1/n8n-screenshots-raw/
# (сняты shoot_webhook_node.py на воркфлоу s10-raw-openrouter,
# id S4AMVj1hVmcs4fe8 — вебхук всех 300+ вызовов этого кейса).
def k1_n8n_real():
    """Два настоящих скриншота живого стенда (canvas + панель узла HTTP
    Request) сведены в ОДНУ фигуру бок о бок — ни один пиксель внутри каждого
    скрина не перерисован, только Pillow-композиция (crop + paste на общий
    холст), тот же эффект, что `convert +append` в ImageMagick, которой в
    этой среде нет."""
    src_canvas = RAW_SHOTS / "raw-openrouter-canvas.png"
    src_panel = RAW_SHOTS / "raw-openrouter-httpnode-panel.png"
    if not src_canvas.exists() or not src_panel.exists():
        WARN.append("НЕ НАЙДЕНЫ СКРИНЫ [raw-openrouter-canvas.png / "
                    "raw-openrouter-httpnode-panel.png]: ожидался результат "
                    "shoot_webhook_node.py — проверь, что он прогонялся")
        return

    canvas = Image.open(src_canvas).convert("RGB")
    panel_full = Image.open(src_panel).convert("RGB")
    # Панель узла обрезана по высоте до самого информативного поля —
    # Method…Credential Type (POST, URL-шаблон, предустановленный credential
    # OpenRouter) — без изменения ни одного пикселя внутри обрезанной области.
    panel = panel_full.crop((0, 0, panel_full.width, min(760, panel_full.height)))

    gap = 36
    target_h = max(canvas.height, panel.height)

    def fit_h(im, h):
        if im.height == h:
            return im
        w = round(im.width * h / im.height)
        return im.resize((w, h), Image.LANCZOS)

    canvas_r = fit_h(canvas, target_h)
    panel_r = fit_h(panel, target_h)
    out_w = canvas_r.width + gap + panel_r.width
    out = Image.new("RGB", (out_w, target_h), W)
    out.paste(canvas_r, (0, 0))
    out.paste(panel_r, (canvas_r.width + gap, 0))
    d = ImageDraw.Draw(out)
    d.line([canvas_r.width + gap // 2, 10, canvas_r.width + gap // 2, target_h - 10],
           fill=SOFT_GREY, width=2)
    save(out, "k1-n8n-infra-real.png")


if __name__ == "__main__":
    k1_shema_postanovka()
    k1_scan_grid()
    k1_recall_chart()
    k1_cascade_diagram()
    k1_attractor_diagram()
    k1_degradation_grid()
    k1_fp_miss_chart()
    k1_n8n_real()
    report()
