#!/usr/bin/env python3
"""Волна 1а «конфетки» Семинара 8 (issue #292) — КРОПЫ настоящих скринов
живого стенда n8n: перекроп цепочки Кейса 4 и три новых панельных композита
крупным планом (план `qa/PLAN-KONFETKA-INSTRUKTSII-2026-10-22.md` §4.9, §5.3).

Почему отдельный файл, а не дописка в `make_figures_k2/k3/k4.py`: те скрипты
при запуске переписывают ВСЕ свои фигуры разом, а в этом круге правок рядом
работает вторая сессия (слайды + `tools/seminar-build` + пересборка деки).
Здесь трогаются ровно четыре файла в `figures/`, перечисленные ниже, и
ничего больше. Стиль подписей и провенанса — `make_figure_k3_real_captions.py`;
канон кропа (срезать хлебные крошки, вкладки, бейдж `Published`, панель зума,
кнопку `Execute workflow`, панель `Logs`, левую колонку иконок — на кадре не
должно быть ни workflow id, ни execution id) — `make_figures_k2.py:
test_stend_real()`.

    k4-n8n-tsepochka-real.png   ЗАМЕНЁН (задача 1). Был кроп (0,0,1900,440)
                                 всего холста: ~69% кадра — пустая сетка
                                 слева, три узла сидели в правой пятине.
                                 Стал — прямоугольник вокруг самих трёх
                                 узлов, увеличенный 2× (приём
                                 `k2-n8n-jev-real.png`).
    k2-panel-hash-crop-real.png  НОВЫЙ (задача 2). Поле `normalized_hash`
                                 с выражением + единственное условие `IF`.
    k3-panel-extract-crop-real.png НОВЫЙ. Схема ответа на одно число +
                                 условие «строго больше 3000».
    k4-panel-uzly-crop-real.png  НОВЫЙ. Выражение шаблона + адрес запроса +
                                 операция отправки картинки.

Три новых файла — ЗАГОТОВКИ под будущие слайды §4.9 (n22a/n34a/n50a в их
переделанном виде). Нынешние `k2-n8n-panels-real.png`,
`k3-n8n-nastroyka-uzlov.png`, `k4-uzly-nastroyka-real.png` НЕ трогаются: на
них стоят сегодняшние слайды.

Источник всех кропов — `stend/n8n-screenshots-raw/*.png` (1900×1100,
Playwright, живой стенд https://n8n.lessons.tellian.io, сняты 2026-10-20).
Кроп режется заново из необрезанного файла, чтобы граница была проверяема по
исходнику; пиксели внутри прямоугольника не перерисовываются. Единственное,
что рисуется поверх, — полосы подписей (`caption_bar`), и они явно нарисованы,
а не вырезаны из интерфейса.

Увеличение (`SCALE`) никак не меняет кегль на экране зала: фигура всё равно
вписывается в полосу 12,23″ (`deck_config.py: WIDTH`), и видимый кегль задаёт
ШИРИНА КРОПА В ПИКСЕЛЯХ ИСХОДНИКА, а не размер PNG. Увеличение нужно только
затем, чтобы проектор не ловил ступеньки на мелком тексте. Замеры кегля — в
`_kegl()` ниже, печатаются при запуске.

Запуск: `python3 make_figures_crops.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"

# Палитра Ocean — те же HEX, что в tools/seminar-build/fig_toolkit.py.
DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
SUBT = (0xBF, 0xDD, 0xEA)
LIGHT = (0x1C, 0x72, 0x93)
W = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BAND_IN = 12.23        # ширина полосы контента слайда, дюймы (deck_config.WIDTH)
FIG_MAX_H_IN = 4.3     # потолок высоты фигуры (deck_kit.FIG_NATURAL_H)

CAP_H = 90             # полоса подписи над кропом
GAP = 30               # зазор между колонками
PAD = 24


def _font(sz, bold=False):
    return ImageFont.truetype(FB if bold else F, sz)


def _kegl(name, fig_w_px, fig_h_px, src_px_per_fig_px=1.0):
    """Сколько пунктов на слайде даёт один пиксель ИСХОДНОГО скрина.

    Фигура вписывается в прямоугольник 12,23″ × 4,3″ с сохранением пропорций,
    поэтому ширина на слайде — это либо вся полоса, либо то, что осталось от
    упора в высоту. `src_px_per_fig_px` — во сколько раз кроп увеличен при
    сборке (1,0 — не увеличен): увеличение делит пункты на пиксель PNG, но
    кегль исходного текста от этого не меняется, что и показывает печать.
    """
    w_in = min(BAND_IN, FIG_MAX_H_IN * fig_w_px / fig_h_px)
    pt_per_png_px = w_in * 72 / fig_w_px
    pt_per_src_px = pt_per_png_px * src_px_per_fig_px
    print(f"   кегль [{name}]: {w_in:.2f}″ на слайде, "
          f"{pt_per_src_px:.3f} pt на пиксель исходника → "
          f"текст интерфейса 12 px = {12 * pt_per_src_px:.1f} pt, "
          f"14 px = {14 * pt_per_src_px:.1f} pt, "
          f"17 px = {17 * pt_per_src_px:.1f} pt")
    return pt_per_src_px


def _empty_grid_share(im, tile=16):
    """Доля кадра, занятая ПУСТОЙ сеткой холста n8n. Фон холста — ровный
    (245,245,245) с точками через 16 px; карточка узла — чистый белый, поэтому
    узлы в «пустое» не попадают. Плитка 16×16 считается пустой, если 98% её
    пикселей — фон (одна точка сетки на плитку порога не ломает)."""
    a = np.array(im.convert("RGB")).astype(int)
    grid = (np.abs(a - 245) <= 3).all(axis=2)
    h, w = grid.shape
    th, tw = h // tile, w // tile
    g = grid[:th * tile, :tw * tile].reshape(th, tile, tw, tile).mean(axis=(1, 3))
    return float((g >= 0.98).mean())


_MEASURE = ImageDraw.Draw(Image.new("RGB", (8, 8)))


def _wrap(text, font, avail):
    """Разбить строку по словам под доступную ширину. Возвращает список строк
    (может быть длиннее `max_lines` — это решает `_fit`)."""
    words, lines, cur = text.split(), [], ""
    for wd in words:
        probe = f"{cur} {wd}".strip()
        if cur and _MEASURE.textlength(probe, font=font) > avail:
            lines.append(cur)
            cur = wd
        else:
            cur = probe
    if cur:
        lines.append(cur)
    return lines


def _fit(text, avail, *, max_fs, min_fs, max_lines, bold):
    """Подобрать кегль, при котором строка укладывается в `max_lines` строк
    шириной `avail`. Самый крупный подходящий — и ни одной обрезки по краю:
    первый прогон этого скрипта как раз показал обрезанные подписи у узкой
    колонки (`Поле normalized_hash: нижни|`), подбор заведён из-за него."""
    for fs in range(max_fs, min_fs - 1, -1):
        f = _font(fs, bold)
        lines = _wrap(text, f, avail)
        if len(lines) <= max_lines and all(
                _MEASURE.textlength(ln, font=f) <= avail for ln in lines):
            return f, lines, fs
    f = _font(min_fs, bold)
    return f, _wrap(text, f, avail)[:max_lines], min_fs


def caption_plan(w, title, subtitle):
    """Разметка полосы подписи: шрифты, строки и нужная высота."""
    avail = w - 2 * PAD
    ft, tl, tfs = _fit(title, avail, max_fs=25, min_fs=17, max_lines=2, bold=True)
    fs_, sl, sfs = _fit(subtitle, avail, max_fs=21, min_fs=15, max_lines=2, bold=True)
    th, sh = int(tfs * 1.22), int(sfs * 1.24)
    h = 14 + th * len(tl) + 6 + sh * len(sl) + 14
    return dict(ft=ft, tl=tl, th=th, fs=fs_, sl=sl, sh=sh, h=h)


def caption_bar(w, h, plan):
    im = Image.new("RGB", (w, h), MID)
    d = ImageDraw.Draw(im)
    y = 14
    for ln in plan["tl"]:
        d.text((PAD, y), ln, font=plan["ft"], fill=W)
        y += plan["th"]
    y += 6
    for ln in plan["sl"]:
        d.text((PAD, y), ln, font=plan["fs"], fill=SUBT)
        y += plan["sh"]
    return im


def column(crop, plan, *, cap_h, body_h):
    """Колонка композита: полоса подписи сверху, под ней кроп в рамке.

    `cap_h` общая на весь композит (полосы подписей выровнены по низу),
    `body_h` — высота тела (у самой высокой колонки равна высоте её кропа).
    Кроп ниже тела центрируется по вертикали: короткая панель читается как
    короткая панель, а не как обрезанная сверху."""
    out = Image.new("RGB", (crop.width, cap_h + body_h), W)
    out.paste(caption_bar(crop.width, cap_h, plan), (0, 0))
    y = cap_h + (body_h - crop.height) // 2
    out.paste(crop, (0, y))
    d = ImageDraw.Draw(out)
    d.line([(0, cap_h), (crop.width, cap_h)], fill=DEEP, width=2)
    d.rectangle([0, y, crop.width - 1, y + crop.height - 1], outline=LIGHT, width=2)
    return out


def compose(parts):
    """`parts` — список (кроп, заголовок, подстрока). Высота полосы подписи и
    высота тела считаются по всему композиту разом, чтобы подписи стояли в
    одну линию, а рамки кропов начинались на одном уровне."""
    plans = [caption_plan(c.width, t, s) for c, t, s in parts]
    cap_h = max(p["h"] for p in plans)
    body = max(c.height for c, _, _ in parts)
    cols = [column(c, p, cap_h=cap_h, body_h=body)
            for (c, _, _), p in zip(parts, plans)]
    w = sum(c.width for c in cols) + GAP * (len(cols) - 1)
    out = Image.new("RGB", (w, cap_h + body), W)
    x = 0
    for i, c in enumerate(cols):
        out.paste(c, (x, 0))
        x += c.width
        if i < len(cols) - 1:
            x += GAP
    return out


def save(im, name, *, note="", src_scale=1.0):
    p = OUT / name
    im.save(p)
    print("  ", name, im.size, note)
    _kegl(name, im.width, im.height, src_scale)
    return p


# ── Задача 1: перекроп цепочки Кейса 4 (слайд n50) ──────────────────────────
def tsepochka_rekrop():
    """ЗАМЕНА `k4-n8n-tsepochka-real.png` (план §5.3).

    Было: кроп (0, 0, 1900, 440) файла `case4-telegram-image.png` — весь
    верх холста. Три разбираемых узла занимали правую пятину кадра, слева
    лежала пустая сетка, сверху — хлебная крошка с названием воркфлоу,
    вкладки Editor/Executions/Evaluations и бейдж `Published`. Замер пустой
    сетки по `_empty_grid_share`: 69% кадра.

    Стало: прямоугольник (1118, 246, 1786, 432) того же исходника — ровно
    три узла карточки с подписями:
        `Compose notification (template)` (manual)
          → `Fetch card image (HTTP)` (GET: https://picsum.photos/8…)
          → `Send card (Telegram photo)` (sendPhoto: message)
    Границы взяты не на глаз, а по разметке содержимого исходника (разбор
    колонок/строк по не-фоновым пикселям): подписи узлов занимают x
    1130–1298, 1355–1546, 1611–1770; карточки узлов — y 255–355; подподписи
    кончаются на y 424. Кроп кладёт по ~12 px поля вокруг этого и на том
    останавливается.

    Что срезано сознательно: хлебная крошка и название воркфлоу, вкладки,
    бейдж `Published`, левая колонка иконок приложения, правая плавающая
    панель зума/поиска, кнопка «Execute workflow», панель `Logs` — то же
    правило, что у `test_stend_real()`: ни workflow id, ни execution id на
    кадре. Справа срезана и кнопка «+» (добавить узел) на x≈1795–1815 —
    часть интерфейса, не шаг процесса. Слева срезаны `Request form` →
    `Extract fields` → `Vocabulary check` → `Write row` (они левее x=1100) и
    узел `Result screen` (ниже y=435) — приём заявки уже показан фигурой
    Кейса 1 и отдельной фигурой точки ветвления
    (`k4-n8n-vetvlenie-real.png`, n49a); здесь кадр отвечает на один вопрос —
    из каких трёх шагов собрана и отправлена карточка.

    Увеличение 2× (LANCZOS) — приём `k2-n8n-jev-real.png`: исходный кроп
    668×186 для PNG мелковат, на проекторе видны ступеньки.

    ЧЕСТНО ПРО ПОРОГ «не более ~20% пустой сетки» (план §5.3): этот кадр даёт
    около 40%, и ниже ~35% для ЦЕПОЧКИ ИЗ ТРЁХ УЗЛОВ в одном прямоугольнике
    не опускается в принципе — между карточками узлов на холсте n8n лежат
    промежутки по ~145 px со стрелкой посередине, и они внутри любого
    прямоугольника, который держит все три узла сразу. Что действительно
    ушло — СПЛОШНОЙ мёртвый угол: в прежнем кадре пустая сетка лежала одним
    куском в 55% ширины слева, в новом нет ни одной пустой области шире
    промежутка между соседними узлами. Опустить метрику ниже можно только
    склейкой трёх отдельных кропов по узлу — то есть отказом от одного
    честного прямоугольника; на это нужно отдельное решение, здесь оно не
    принималось.
    """
    raw = Image.open(RAW / "case4-telegram-image.png").convert("RGB")
    box = (1118, 246, 1786, 432)
    crop = raw.crop(box)
    # «Было» считается не по файлу на диске, а по ПРЕЖНЕМУ прямоугольнику того
    # же исходника — иначе после первой же замены сравнение поехало бы с новым
    # файлом самим с собой.
    before = raw.crop((0, 0, 1900, 440))
    print(f"   пустая сетка: было {_empty_grid_share(before):.0%} "
          f"(кроп 0,0,1900,440 — {before.width}×{before.height}), "
          f"стало {_empty_grid_share(crop):.0%} ({crop.width}×{crop.height})")
    SCALE = 2
    return crop.resize((crop.width * SCALE, crop.height * SCALE), Image.LANCZOS), SCALE


# `--preview` кладёт перекроп под временным именем: посмотреть глазами ПРЕЖДЕ,
# чем переписать файл, на который уже ссылается слайд n50.
PREVIEW = "--preview" in _sys.argv
_im, _sc = tsepochka_rekrop()
save(_im, "_preview-k4-n8n-tsepochka-real.png" if PREVIEW
     else "k4-n8n-tsepochka-real.png",
     note="кроп (1118,246,1786,432) из case4-telegram-image.png, ×2",
     src_scale=_sc)


# ── Задача 2: панельные кропы крупным планом (план §4.9) ────────────────────
#
# Общее правило кропов ниже: берётся ТОЛЬКО центральная колонка `Parameters`
# панели узла — то поле (или два), ради которого слайд существует. Колонки
# `INPUT` слева и `OUTPUT` справа в кадр не входят вовсе: на части этих
# скринов они пусты («No input data» — предыдущие шаги перед съёмкой не
# прогонялись), и показывать пустую колонку значило бы показывать свойство
# момента съёмки вместо устройства узла.

def k2_hash_panel():
    """НОВЫЙ `k2-panel-hash-crop-real.png` — Кейс 2, два поля крупно.

    Левая колонка: `stend/n8n-screenshots-raw/case2-normalize-hash.png`,
    кроп (775, 232, 1150, 358) — узел `Normalize + hash` (Set), блок
    `Fields to Set` → поле `normalized_hash`, тип `String` и строка
    выражения целиком:
        {{ $('Request form').item.json['Что нужно']
           .toLowerCase().trim().replace(/\\s+/g, ' ') }}
    Ниже по панели на исходнике идут ещё два поля
    (`recent_same_contact_text`, `recent_same_contact_hash`) — они срезаны
    сознательно: слайд §4.9 показывает ОДНО ключевое поле крупно, полный
    перечень полей остаётся в заметках.

    Правая колонка: `case2-exact-duplicate-if.png`, кроп (645, 118, 1252,
    218) — узел `Exact duplicate in window?` (IF), заголовок `Conditions` и
    единственное условие: `{{ $json.normalized_hash }}` **is equal to**
    `{{ $json.recent_same_contact_hash }}`. Ровно столько и есть — никакой
    второй строки под обрезом не прячется, условие на узле одно.
    """
    a = Image.open(RAW / "case2-normalize-hash.png").convert("RGB").crop(
        (775, 232, 1150, 358))
    b = Image.open(RAW / "case2-exact-duplicate-if.png").convert("RGB").crop(
        (645, 118, 1252, 218))
    return compose([
        (a, "Узел «Normalize + hash» (Set)",
         "Поле normalized_hash: нижний регистр, пробелы схлопнуты"),
        (b, "Узел «Exact duplicate in window?» (IF)",
         "Одно условие: хэш равен хэшу предыдущей заявки"),
    ])


save(k2_hash_panel(), "k2-panel-hash-crop-real.png",
     note="case2-normalize-hash (775,232,1150,358) + case2-exact-duplicate-if (645,118,1252,218)")


def k3_extract_panel():
    """НОВЫЙ `k3-panel-extract-crop-real.png` — Кейс 3, два поля крупно.

    Левая колонка: `case3-extract-amount.png`, кроп (752, 256, 1150, 560) —
    узел `Extract amount` (Information Extractor), подпись `Input Schema` и
    сама схема целиком, все 12 строк: объект с единственным свойством
    `amount_rub` типа `number`, описанием «сумма возврата в рублях,
    указанная в тексте» и этим же полем в `required`. Схема взята целиком, а
    не одной строкой, именно потому что урок кейса — «на выходе модели одно
    число и ничего кроме»: обрезок схемы этого не доказывает.

    Правая колонка: `case3-if-threshold.png`, кроп (645, 118, 1252, 322) —
    узел `Amount over threshold?` (IF): `{{ $json.output.amount_rub }}`
    **is greater than** `3000`. Порог виден числом в поле, а не пересказан.
    Нижняя граница кропа взята НЕ по последней строке условия, а на две
    строки ниже — так, чтобы в кадр вошли `+ Add condition` (видно, что
    условие на узле одно, второго под обрезом нет) и выключенный
    `Convert types where required` (число сравнивается с числом без
    приведения типов — ровно то, чем этот узел отличается от правила внутри
    промпта). Первый прогон резал на y=215, и тогда правая колонка была
    втрое ниже левой: треть кадра уходила в случайную белизну (план §3.3).

    Пропорции колонок всё равно разные (схема высокая, условие низкое) —
    короткая колонка центрируется по высоте тела, см. `column()`.
    """
    a = Image.open(RAW / "case3-extract-amount.png").convert("RGB").crop(
        (752, 256, 1150, 560))
    b = Image.open(RAW / "case3-if-threshold.png").convert("RGB").crop(
        (645, 118, 1252, 322))
    return compose([
        (a, "Узел «Extract amount» (Information Extractor)",
         "Схема ответа: одно число amount_rub, обязательное"),
        (b, "Узел «Amount over threshold?» (IF)",
         "Условие: amount_rub строго больше 3000"),
    ])


save(k3_extract_panel(), "k3-panel-extract-crop-real.png",
     note="case3-extract-amount (752,256,1150,560) + case3-if-threshold (645,118,1252,322)")


def k4_uzly_panel():
    """НОВЫЙ `k4-panel-uzly-crop-real.png` — Кейс 4, три поля крупно.

    Колонка 1: `case4-compose-notification.png`, кроп (770, 232, 1150, 416) —
    узел `Compose notification (template)` (Set), поле `notification_text`,
    тип `String` и выражение шаблона целиком (пять строк, тот же приём
    подстановки значений, что в Кейсе 1).

    Колонка 2: `case4-fetch-image.png`, кроп (752, 158, 1150, 290) — узел
    `Fetch card image (HTTP)`: `Method` = GET и `URL` =
    https://picsum.photos/800/450. Ниже на панели — `Authentication`/`Send
    Query Parameters`/`Send Headers`/`Send Body` (все по умолчанию, ни один
    не тронут) и ещё ниже `Response Format` = File / `Put Output in Field` =
    data. Эти два последних поля в кадр НЕ попали: они лежат на y≈630–900
    исходника, то есть через весь блок нетронутых переключателей, и взять их
    в тот же прямоугольник нельзя. На прежнем композите
    (`k4-uzly-nastroyka-real.png`, n50a) они показаны двухполосным кропом с
    явной подписью о пропуске — здесь, где слайд §4.9 просит одно-два поля
    крупно, выбраны адрес запроса и метод, а формат ответа остаётся за
    заметками. Это назван пропуск, а не незамеченный.

    Колонка 3: `case4-send-telegram.png`, кроп (752, 182, 1150, 312) — узел
    `Send card (Telegram photo)`: `Resource` = Message, `Operation` = Send
    Photo. Кроп НАМЕРЕННО кончается на y=312: следующее поле панели —
    `Chat ID` с личным числовым id тестового аккаунта стенда (y≈344–372).
    На прежнем композите его приходилось закрывать нарисованной заглушкой;
    здесь он просто не входит в прямоугольник, что честнее — закрывать
    нечего.
    """
    a = Image.open(RAW / "case4-compose-notification.png").convert("RGB").crop(
        (770, 232, 1150, 416))
    b = Image.open(RAW / "case4-fetch-image.png").convert("RGB").crop(
        (752, 158, 1150, 290))
    c = Image.open(RAW / "case4-send-telegram.png").convert("RGB").crop(
        (752, 182, 1150, 312))
    return compose([
        (a, "Узел «Compose notification (template)»",
         "Поле notification_text: подстановка значений в шаблон"),
        (b, "Узел «Fetch card image (HTTP)»",
         "Запрос GET по адресу картинки"),
        (c, "Узел «Send card (Telegram photo)»",
         "Операция Send Photo — картинка, а не текст"),
    ])


save(k4_uzly_panel(), "k4-panel-uzly-crop-real.png",
     note="case4-compose (770,232,1150,416) + case4-fetch (752,158,1150,290) "
          "+ case4-send (752,182,1150,312)")


# ── Задача 3: таблица заявок стенда, строки буквального повтора (n23a) ──────
DT_RAW = "datatable-requests-2026-10-22.png"
DT_HEAD = (123, 132, 2295, 201)      # строка заголовков столбцов
DT_ROWS = (123, 1126, 2295, 1524)    # строки 15–20
DT_GAP = 56                          # полоса с честной подписью о пропуске


def datatable_povtor(label):
    """`k2-datatable-povtor-real.png` — НАСТОЯЩАЯ таблица данных живого
    стенда (n8n Data Table `requests`, 31 строка), снятая 2026-10-22
    скриптом `shoot_datatable.py` (вход в интерфейс, только чтение: ни один
    воркфлоу не прогонялся, ни одна строка не менялась).

    Исходник — `stend/n8n-screenshots-raw/datatable-requests-2026-10-22.png`,
    3000×1900 (окно 1500×950, плотность 2× ради чёткости мелкого текста на
    проекторе), светлая тема.

    Кадр собран из ДВУХ кусков ОДНОГО И ТОГО ЖЕ снимка, разнесённых по
    вертикали, с явной полосой-подписью между ними — тот же приём и та же
    честность, что у двухполосного кропа узла `Fetch` в
    `make_figures_k4.py: uzly_nastroyka()`:
      · (123, 132, 2295, 201) — строка заголовков столбцов;
      · (123, 1126, 2295, 1524) — строки 15–20.

    Почему не вся первая страница таблицы разом. Во-первых, кегль: 20 строк
    в полосе 12,23″ дают около 5,6 pt на строку — вдвое ниже пола 7,5 pt.
    Во-вторых, между заголовком и нижним кустом повторов лежат две строки
    мусорного тестового ввода («ывавыаыв» — кто-то проверял форму, стуча по
    клавиатуре); на слайде они читаются неряшливостью стенда и уводят вопрос
    зала в сторону. Прокрутка списка не помогает: строка заголовков в этой
    таблице НЕ прилипшая — прокрутив до строки 20, теряешь имена столбцов
    (проверено, кадр `…-tail.png` рядом с исходником).

    ЧТО В КАДРЕ. Строки 15 и 16 — Пётр, одна и та же заявка «Здравствуйте!
    Хочу записаться на ку…», поданная 12 и 13 октября. Строки 17–20 — Анна,
    четыре подряд с ОДНИМ И ТЕМ ЖЕ текстом «Можно перенести занятие со
    вторника? И подскажите, как оплатить.», причём 17 и 18 различаются по
    метке времени на 15 МИЛЛИСЕКУНД (10:15:01.752 и 10:15:01.767), а 19 и 20
    — на 14 мс. Это и есть буквальный повтор, ради которого кадр снят.

    СТОЛБЦЫ СПРАВА СРЕЗАНЫ (`topic`, `urgency`, `contact_from_text`): кадр
    ровно на тех пяти столбцах, которые отвечают на вопрос «одно и то же или
    нет». Срез не косметический, у него есть цена — на срезанном `topic`
    видно, что четыре ОДИНАКОВЫХ текста получили РАЗНЫЕ темы («другое»,
    «другое», «перенос занятия», «оплата»); это отдельная находка про
    устойчивость разметки, её место — своя фигура и свой разбор, а не угол
    этого кадра.

    ЧЕГО В КАДРЕ НЕТ, честно: текст заявки обрезан самим интерфейсом n8n по
    ширине столбца («…со вторни»), а не нашим кропом. Расширить столбец
    можно было бы только потянув его границу в интерфейсе — то есть записав
    что-то в состояние стенда, а стенд в этой волне открыт только на чтение.
    Полный текст всех строк сохранён рядом с исходником
    (`datatable-requests-2026-10-22-text.txt`) и должен уйти в заметки
    слайда.
    """
    raw = Image.open(RAW / DT_RAW).convert("RGB")
    head, rows = raw.crop(DT_HEAD), raw.crop(DT_ROWS)
    w = head.width
    im = Image.new("RGB", (w, head.height + DT_GAP + rows.height), W)
    im.paste(head, (0, 0))
    im.paste(rows, (0, head.height + DT_GAP))
    d = ImageDraw.Draw(im)
    y0, y1 = head.height, head.height + DT_GAP
    d.line([(0, y0 + 6), (w, y0 + 6)], fill=(0xD8, 0xDE, 0xE6), width=3)
    d.line([(0, y1 - 6), (w, y1 - 6)], fill=(0xD8, 0xDE, 0xE6), width=3)
    f = _font(26, True)
    d.text(((w - _MEASURE.textlength(label, font=f)) / 2, y0 + 14), label,
           font=f, fill=(0x6B, 0x75, 0x80))
    d.rectangle([0, 0, w - 1, im.height - 1], outline=LIGHT, width=3)
    return im


# `src_scale=2`: этот снимок сделан с плотностью 2 (deviceScaleFactor), то
# есть 12 пунктов интерфейса занимают на нём 24 пикселя. Без этой поправки
# замер кегля соврал бы ровно вдвое в опасную сторону.
save(datatable_povtor("⋯ строки 1–14 той же страницы таблицы пропущены ⋯"),
     "k2-datatable-povtor-real.png",
     note=f"{DT_RAW} {DT_HEAD} + {DT_ROWS}", src_scale=2)
save(datatable_povtor("⋯ rows 1–14 of the same table page are omitted ⋯"),
     "k2-datatable-povtor-real-en.png", src_scale=2)


# ── EN-спутники трёх новых композитов (Bilingual Production Rule, #172) ─────
#
# Переводится ТОЛЬКО нарисованная полоса подписи; кропы живого стенда те же
# самые файлы и те же прямоугольники — интерфейс n8n на них и так английский.
# Отдельными функциями, без общего словаря `fig_strings_en.py`: он один на все
# рисовалки занятия, а рядом работает вторая сессия.

def k2_hash_panel_en():
    a = Image.open(RAW / "case2-normalize-hash.png").convert("RGB").crop(
        (775, 232, 1150, 358))
    b = Image.open(RAW / "case2-exact-duplicate-if.png").convert("RGB").crop(
        (645, 118, 1252, 218))
    return compose([
        (a, "Node “Normalize + hash” (Set)",
         "Field normalized_hash: lowercase, whitespace collapsed"),
        (b, "Node “Exact duplicate in window?” (IF)",
         "One condition: hash equals the previous request’s hash"),
    ])


def k3_extract_panel_en():
    a = Image.open(RAW / "case3-extract-amount.png").convert("RGB").crop(
        (752, 256, 1150, 560))
    b = Image.open(RAW / "case3-if-threshold.png").convert("RGB").crop(
        (645, 118, 1252, 322))
    return compose([
        (a, "Node “Extract amount” (Information Extractor)",
         "Answer schema: one number amount_rub, required"),
        (b, "Node “Amount over threshold?” (IF)",
         "Condition: amount_rub is strictly greater than 3000"),
    ])


def k4_uzly_panel_en():
    a = Image.open(RAW / "case4-compose-notification.png").convert("RGB").crop(
        (770, 232, 1150, 416))
    b = Image.open(RAW / "case4-fetch-image.png").convert("RGB").crop(
        (752, 158, 1150, 290))
    c = Image.open(RAW / "case4-send-telegram.png").convert("RGB").crop(
        (752, 182, 1150, 312))
    return compose([
        (a, "Node “Compose notification (template)”",
         "Field notification_text: values substituted into a template"),
        (b, "Node “Fetch card image (HTTP)”",
         "GET request to the image address"),
        (c, "Node “Send card (Telegram photo)”",
         "Operation Send Photo — a picture, not a text message"),
    ])


save(k2_hash_panel_en(), "k2-panel-hash-crop-real-en.png")
save(k3_extract_panel_en(), "k3-panel-extract-crop-real-en.png")
save(k4_uzly_panel_en(), "k4-panel-uzly-crop-real-en.png")

print("\nготово: 1 заменён (k4-n8n-tsepochka-real.png), 6 новых "
      "(три панельных композита + их EN-спутники).")
