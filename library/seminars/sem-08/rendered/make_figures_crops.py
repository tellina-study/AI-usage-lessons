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

──────────────────────────────────────────────────────────────────────────────
ДОПИСАНО ВОЛНОЙ 1б (тот же issue #292). Всё, что выше, — волна 1а и её четыре
файла; они пересобираются этим скриптом без изменений. Ниже, с заголовка
«ВОЛНА 1б», добавлен перекроп ВОСЬМИ фигур по её же аудиту — отсюда фраза
«трогаются ровно четыре файла» выше относится только к разделу волны 1а.
Полный список файлов волны 1б, методика замера кегля и то, что кропом НЕ
чинится, — в шапке её раздела.
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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ВОЛНА 1б — перекроп восьми фигур по вердиктам аудита волны 1а            ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# Волна 1а прошла все `*-real.png` и назвала дефекты; здесь они чинятся
# единственным доступным средством — границей прямоугольника. Ни один пиксель
# внутри кропа не перерисовывается; рисуются только полосы подписей у двух
# композитов (`caption_bar` выше), и они явно нарисованы.
#
# ПЕРЕКРАИВАЮТСЯ (все — НА МЕСТО, под теми же именами):
#   k1-n8n-versiya1-real.png · k1-n8n-versiya2-real.png
#   k2-n8n-mehanika-real.png · k2-n8n-jev-real.png
#   k3-n8n-if-uzel-real.png  · k3-n8n-reshenie-real(-en).png
#   k3-n8n-variants-real(-en).png · k4-n8n-vetvlenie-real.png
#
# ЛОВУШКА ЗАКРЫТА волной 2б (issue #292). `k3-n8n-reshenie-real(-en).png` и
# `k3-n8n-variants-real(-en).png` умел собирать и соседний скрипт
# `make_figure_k3_real_captions.py` — по СТАРЫМ, широким прямоугольникам, то
# есть его прогон молча возвращал сюда прежний, заваленный кегль. Волна 2б
# отключила там ровно эти четыре цели (блок `_OTKLYUCHENO` в том файле):
# функции-композиты оставлены как история, `save` по этим именам больше не
# вызывается, прогон печатает «ПРОПУЩЕНО … источник — make_figures_crops.py».
# Проверено не чтением кода: хэши обоих файлов до и после прогона того
# скрипта совпали. Источник этих четырёх имён — ЭТОТ файл, и теперь это
# свойство кода, а не договорённость.
#
# ─── Как здесь меряется кегль (и почему цифра не одна, а две) ──────────────
#
# МЕТОДИКА БРИФА (та же, что у волны 1а): фигура встаёт в полосу 12,23″ при
# потолке высоты 4,3″, видимый кегль = высота строки подписи в пикселях
# ИСХОДНИКА × пункты-на-пиксель. Пол — 7,5 pt. За высоту строки взяты 14 px:
# именно эта величина воспроизводит обе цифры аудита волны 1а для фигур,
# которые он завалил (reshenie 5,7 pt и variants 4,8 pt), поэтому «было →
# стало» в отчёте считается в одной шкале. Для справки: подпись узла n8n на
# этих снимках — 12 px без выносных элементов и 15 px с ними.
#
# ЗАМЕР ПО СОБРАННОЙ ДЕКЕ (добавлен этой волной). Потолок 4,3″ — допущение, а
# не факт: сколько высоты досталось фигуре на самом деле, видно в уже
# собранном `rendered/sem-08.pptx`. Измерено там (python-pptx, ширина×высота
# картинки на слайде):
#     n11/n14 (k1)        12,23 × 3,49″ — упирается в ШИРИНУ, допущение верно
#     n22  (mehanika)     10,56 × 3,45″
#     n23  (jev)          10,84 × 3,21″
#     n31  (variants)      8,60 × 1,60″  ← фигуре досталось 1,60″ высоты
#     n34  (reshenie)     12,23 × 2,68″
#     n49a (vetvlenie)    12,23 × 3,79″
# На n31 над фигурой стоят ЧЕТЫРЕ текстовых блока, и вёрстка ужимает схему до
# 70% отведённой ширины — ниже собственного порога сборщика
# (`deck_kit.FIG_MIN_FILL = 0.80`). Это значит: пол 7,5 pt на этом слайде не
# берётся НИКАКИМ кропом, потому что упор не в кроп. Названо в отчёте волны,
# чинится на уровне слайда, здесь не чинится.
#
# ─── Что кропом не чинится вовсе ──────────────────────────────────────────
# Наложенные друг на друга подписи «Result screen» / «Model (notification)» /
# «Form Ending» на канвасе Кейса 1 и соседские подписи вокруг узла `Jev` —
# это РАСКЛАДКА УЗЛОВ НА ХОЛСТЕ СТЕНДА. Прямоугольник не умеет раздвигать то,
# что на холсте лежит внахлёст; лечится только перестановкой узлов в n8n, то
# есть записью на стенд — вне зоны этой волны. Сказано прямо, а не обойдено.


def _ratio_note(name, w, h, prev_ar):
    """Соотношение сторон — не косметика: сборщик вписывает фигуру в 12,23″ ×
    отведённую высоту и РУГАЕТСЯ, если по ширине вышло меньше 80% полосы
    (`deck_kit.figure`: «СХЕМА ЗАЖАТА»). Поэтому каждый перекроп печатает,
    куда уехало соотношение, — чтобы волна пересборки видела это числом, а не
    узнавала из предупреждения."""
    ar = w / h
    mark = "=" if abs(ar - prev_ar) < 0.08 else ("↓" if ar < prev_ar else "↑")
    print(f"   пропорция [{name}]: было {prev_ar:.2f} → стало {ar:.2f} {mark}")


def _before_after(raw, old_box, new_box, name, prev_ar):
    """Общая печать «было → стало». «Было» считается не по файлу на диске, а
    по ПРЕЖНЕМУ прямоугольнику того же исходника (приём `tsepochka_rekrop`):
    иначе после первой же перезаписи сравнение поехало бы с новым файлом
    самим с собой."""
    before, after = raw.crop(old_box), raw.crop(new_box)
    bw, bh = before.size
    aw, ah = after.size
    print(f"   пустая сетка [{name}]: было {_empty_grid_share(before):.0%} "
          f"({bw}×{bh}, кроп {old_box}), стало {_empty_grid_share(after):.0%} "
          f"({aw}×{ah}, кроп {new_box})")
    _ratio_note(name, aw, ah, prev_ar)
    return after


# ── Кейс 1: два канваса одним и тем же прямоугольником (n11, n14) ──────────
#
# Прямоугольник у обеих версий ОБЯЗАН совпадать до пикселя: два кадра
# накладываются один на другой без сдвига, и структурная разница версий (у
# версии 1 на месте `Result screen` стоит лишний блок модели) видна по месту.
# Старый общий прямоугольник — (260, 250, 1730, 670), 1470×420.
#
# Новый — (288, 248, 1660, 648), 1372×400. Что срезано и почему:
#   слева  260→288  пустая сетка до значка-молнии триггера (контент
#                   начинается на x=292, замерено по не-фоновым пикселям);
#   справа 1730→1660 кнопка «+» (добавить узел) на x≈1676–1695 — элемент
#                   интерфейса, не шаг процесса, канон `test_stend_real()`;
#   снизу  670→648  пустая полоса под подписями «Request form» и «Model*»
#                   (нижняя строка текста кончается на y=638; 10 px запаса —
#                   первый прогон резал на 643, и подпись вставала впритык
#                   к рамке, что на проекторе читается как обрезка).
# Весь путь остаётся в кадре целиком: Request form → Extract fields →
# Vocabulary check → Write row → Compose notification… → Notify coordinator
# (Telegram), с пометками «Model*» и — у версии 1 — блоком «Result screen
# Model (notification)».
#
# ЧЕСТНО ПРО ПУСТОТУ. Ниже ~70% этот кадр не опускается и не может: шесть
# узлов лежат на холсте РЕДКОЙ ДИАГОНАЛЬЮ из левого нижнего угла в правый
# верхний, и прямоугольник, который держит оба конца, обязан держать и два
# пустых угла между ними. Ушли поля по краям, диагональ осталась. Собрать
# кадр плотнее можно только выбросив приём заявки (левую треть) — а его
# называет текст слайда n11, так что это была бы правка слайда, не кропа.
K1_BOX = (288, 248, 1660, 648)
K1_OLD = (260, 250, 1730, 670)

for _src, _out in (("case1-before.png", "k1-n8n-versiya1-real.png"),
                   ("case1-after.png", "k1-n8n-versiya2-real.png")):
    _raw = Image.open(RAW / _src).convert("RGB")
    save(_before_after(_raw, K1_OLD, K1_BOX, _out, 3.50), _out,
         note=f"кроп {K1_BOX} из {_src}, 1:1")


# ── Кейс 2, обзор процесса (n22): нижние подписи больше не обрублены ───────
def mehanika_rekrop():
    """ЗАМЕНА `k2-n8n-mehanika-real.png`.

    Было: (390, 300, 1600, 695) файла `case2-dedup-prod-jev.png`, 1210×395.
    Нижний край резал подпись `Exact duplicate in window?` ровно по второй
    строке («window?» занимает y 683–695) и обрубал «manual» под `Normalize
    + hash`. Справа в кадр входила кнопка «+» на x≈1555–1575.

    Стало: (376, 308, 1520, 709), 1144×401. Нижняя граница отодвинута на
    y=709 — это 12 px запаса под последней строкой подписей и при этом на
    2 px ВЫШЕ, чем начинаются подписи соседних узлов `Write row · not
    parsed` и `Result screen · not parsed` (их текст идёт с y=711): запас
    взят ровно до того места, где он начал бы тащить в кадр чужое.
    Правая граница 1520 оставляет выходную точку `Result screen` и обрезает
    соединитель с кнопкой «+». Левая 376 — пустая сетка до значка-молнии
    (контент с x=412).

    Ширина 1144 выбрана НЕ по контенту (он кончается на x=1512, хватило бы
    1136), а по пропорции: при высоте 401 соотношение 2,85 — нижняя граница,
    при которой вёрстка n22 даёт фигуре прежние ~86% полосы. Отними ещё
    сотню пикселей ширины — и выигрыш в кегле съест предупреждение «СХЕМА
    ЗАЖАТА».

    ЧТО НЕ ПОЧИНЕНО И ПОЧЕМУ. Карточка чужого узла `Write row · not parsed`
    физически лежит поверх подписи `Normalize + hash` на самом холсте
    (x 1018–1087, y 607–699 против подписи на y 662–676). Это нахлёст
    раскладки стенда, а не кропа: любой прямоугольник, который держит
    `Normalize + hash` и `Exact duplicate in window?` сразу, держит и её.
    """
    raw = Image.open(RAW / "case2-dedup-prod-jev.png").convert("RGB")
    return _before_after(raw, (390, 300, 1600, 695), (376, 308, 1520, 709),
                         "k2-n8n-mehanika-real.png", 3.06)


save(mehanika_rekrop(), "k2-n8n-mehanika-real.png",
     note="кроп (376,308,1520,709) из case2-dedup-prod-jev.png, 1:1")


# ── Кейс 2, узел Jev (n23): карточка целиком ───────────────────────────────
def jev_rekrop():
    """ЗАМЕНА `k2-n8n-jev-real.png`.

    Было: (1010, 742, 1570, 908) того же канваса, ×2. Верхняя граница 742
    резала карточку узла (её верх — y=716), то есть зал видел узел без
    крышки; правая треть кадра была пустой сеткой.

    Стало: (872, 706, 1442, 896), ×2. Карточка `Jev decision (reworded?)`
    (x 1147–1244, y 716–811) входит целиком, вместе с обеими строками имени
    (y 823–857), подписью `POST: https://openrouter.ai/…` (x 1099–1285,
    y 862–878) и петлёй соединителя, которая возвращает ответ назад
    (нижняя дуга на y 881–893). Пустая правая треть срезана.

    ЧЕСТНО ПРО «ЧУЖИЕ УЗЛЫ ВОН» — ЭТОГО СДЕЛАТЬ НЕЛЬЗЯ. Подписи соседей
    `Write row · not parsed` (x 952–1115) и `Result screen · not parsed`
    + `Form Ending` (x 1221–1362) лежат на холсте в ТОЙ ЖЕ горизонтальной
    полосе y 711–766, что и верхняя половина карточки Jev. Прямоугольник,
    который держит карточку целиком, обязан пройти через эту полосу —
    выбор только между «чужая подпись видна целиком» и «чужая подпись
    обрезана посреди слова». Выбрано первое: целая подпись читается как
    соседний узел плотного холста (ровно так её и называет backup слайда
    n23), обрубок читается как брак печати. Убрать их совсем можно только
    раздвинув узлы в n8n, то есть записью на стенд — вне зоны волны.

    Ширина 570 при высоте 190 (соотношение 3,0) — опять пропорция, а не
    контент: сам контент укладывается в 410 px, но при соотношении ~2,2
    вёрстка n23 ужала бы фигуру ниже порога `FIG_MIN_FILL`. Добавленные
    160 px — пустая сетка, поровну слева и справа.
    """
    raw = Image.open(RAW / "case2-dedup-prod-jev.png").convert("RGB")
    crop = _before_after(raw, (1010, 742, 1570, 908), (872, 706, 1442, 896),
                         "k2-n8n-jev-real.png", 3.37)
    return crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)


save(jev_rekrop(), "k2-n8n-jev-real.png",
     note="кроп (872,706,1442,896) из case2-dedup-prod-jev.png, ×2",
     src_scale=2)


# ── Кейс 4, точка ветвления (n49a): подписи целиком ────────────────────────
def vetvlenie_rekrop():
    """ЗАМЕНА `k4-n8n-vetvlenie-real.png` (прежний кроп — `make_figures_k4.py:
    vetvlenie_real()`, он остаётся в том файле как есть; источником считать
    этот).

    Было: (820, 258, 1800, 562) файла `case4-telegram-image.png`, 980×304.
    Нижний край 562 резал подписи `Write row` и `Result screen` (строка
    занимает y 543–554) и срезал `Form Ending` (y 567–578) целиком; справа
    в кадр заходила кнопка «+» (x≈1795–1815).

    Стало: (815, 248, 1790, 585), 975×337. Низ отодвинут на 585 — 7 px под
    последней строкой; верх поднят на 248 (карточки начинаются с y=258),
    право сдвинуто на 1790: соединитель-обрубок остаётся, кнопка «+» уходит.
    В кадре по-прежнему `Write row` → развилка на `Result screen` и вверх на
    `Compose notification (template)` → `Fetch card image (HTTP)` →
    `Send card (Telegram photo)`, с подписями `GET: https://picsum.photos/8…`
    и `sendPhoto: message`.
    """
    raw = Image.open(RAW / "case4-telegram-image.png").convert("RGB")
    return _before_after(raw, (820, 258, 1800, 562), (815, 248, 1790, 585),
                         "k4-n8n-vetvlenie-real.png", 3.22)


save(vetvlenie_rekrop(), "k4-n8n-vetvlenie-real.png",
     note="кроп (815,248,1790,585) из case4-telegram-image.png, 1:1")


# ── Кейс 3: два композита и общий для них кроп канваса ─────────────────────
#
# `caption_bar()` выше красит подстроку в один цвет (SUBT). У композитов
# Кейса 3 подстрока «Измерено: 100/100…» с самого начала шла ЗОЛОТОМ — это
# смысловая метка измеренного результата, а не украшение, и терять её при
# перекропе нельзя. Отсюда две местные обёртки: они повторяют `column()` и
# `compose()`, добавляя цвет подстроки и масштаб колонки.

GOLD = (0xF0, 0xAB, 0x00)


def _caption_bar_c(w, h, plan, sub_color):
    im = Image.new("RGB", (w, h), MID)
    d = ImageDraw.Draw(im)
    y = 14
    for ln in plan["tl"]:
        d.text((PAD, y), ln, font=plan["ft"], fill=W)
        y += plan["th"]
    y += 6
    for ln in plan["sl"]:
        d.text((PAD, y), ln, font=plan["fs"], fill=sub_color)
        y += plan["sh"]
    return im


def compose_c(parts):
    """`parts` — список (кроп, заголовок, подстрока). Подстрока со словом
    `100/100` красится золотом (как в `make_figure_k3_real_captions.py`),
    остальные — светло-голубым. Высота полосы подписи общая на композит,
    чтобы подписи стояли в одну линию."""
    plans = [caption_plan(c.width, t, s) for c, t, s in parts]
    cap_h = max(p["h"] for p in plans)
    body = max(c.height for c, _, _ in parts)
    cols = []
    for (c, _, s), p in zip(parts, plans):
        out = Image.new("RGB", (c.width, cap_h + body), W)
        out.paste(_caption_bar_c(c.width, cap_h, p,
                                 GOLD if "100/100" in s else SUBT), (0, 0))
        y = cap_h + (body - c.height) // 2
        out.paste(c, (0, y))
        d = ImageDraw.Draw(out)
        d.line([(0, cap_h), (c.width, cap_h)], fill=DEEP, width=2)
        d.rectangle([0, y, c.width - 1, y + c.height - 1], outline=LIGHT, width=2)
        cols.append(out)
    w = sum(c.width for c in cols) + GAP * (len(cols) - 1)
    out = Image.new("RGB", (w, cap_h + body), W)
    x = 0
    for i, c in enumerate(cols):
        out.paste(c, (x, 0))
        x += c.width + (GAP if i < len(cols) - 1 else 0)
    return out


def _to_height(im, h):
    """Увеличить кроп до заданной высоты (LANCZOS). Нужно ровно затем, чтобы
    две колонки композита стояли вровень по нижнему краю: когда правая
    панель втрое ниже левого канваса, треть кадра уходит в белизну — ту же
    беду волна 1а чинила подбором нижней границы в `k3_extract_panel()`."""
    if im.height == h:
        return im, 1.0
    k = h / im.height
    return im.resize((round(im.width * k), h), Image.LANCZOS), k


def _to_width(im, w):
    """То же, но по ЗАДАННОЙ ШИРИНЕ. Ширина колонки — это ещё и ширина её
    подписи: `caption_plan` ломает заголовок на две строки, как только тот
    перестаёт помещаться, и полоса подписи вырастает на целую строку.
    У композита n34 английский заголовок на 9 px длиннее русского — ровно
    столько, чтобы EN-версия ТОЙ ЖЕ фигуры оказалась на 56 px выше русской и
    встала на слайд с другой пропорцией. Поэтому правая колонка там задаётся
    шириной (660 px — с запасом под оба заголовка), а не высотой."""
    k = w / im.width
    return im.resize((w, round(im.height * k)), Image.LANCZOS), k


# ── k3-n8n-if-uzel-real.png: сам кроп канваса (n34, левая половина) ────────
#
# Было: (700, 360, 1650, 650) файла `case3-process-b-code.png`, 950×290.
# Нижняя граница 650 срезала подпись `Result screen (approve)` (строка занимает
# y 636–655) и её `Form Ending` целиком; справа в кадр входили две кнопки «+»
# (x 1435–1455).
#
# Стало: (526, 366, 1430, 679), 904×313. Нижняя граница 679 — под `Form
# Ending` ветки approve (кончается на y=676) и ВЫШЕ кружка подузла `Model
# (extraction)` (начинается на y=680): запас взят ровно до того места, где он
# начал бы тащить в кадр пунктирную ветку модели, которой на этом слайде не
# о чем говорить. Правая 1430 убирает обе «+». Левая 526 добавляет узел
# `Refund request` — он не был нужен содержательно, но даёт композиту n34 те
# самые ~260 px ширины, без которых соотношение сторон падает ниже
# `FIG_MIN_FILL`; то есть это не «лишний узел», а плата за пропорцию, и
# заодно кадр читается как весь путь версии 2, а не как его середина.
#
# Оборванный снизу пунктир с подписью `Model` остаётся в кадре — это
# соединение с подузлом модели, уходящее за край. Так на холсте и есть.
K3_IF_BOX = (526, 366, 1430, 679)

_raw_b = Image.open(RAW / "case3-process-b-code.png").convert("RGB")
save(_before_after(_raw_b, (700, 360, 1650, 650), K3_IF_BOX,
                   "k3-n8n-if-uzel-real.png", 3.28),
     "k3-n8n-if-uzel-real.png",
     note="кроп (526,366,1430,679) из case3-process-b-code.png, 1:1")


# ── k3-n8n-reshenie-real(-en).png (n34) ────────────────────────────────────
#
# Было: 2146×470 — левая половина прежним кропом канваса, правая — кроп
# (0, 0, 1160, 358) файла `case3a-model-decides.png`. В правой половине
# лежало ТРИ лишних куска: колонка иконок приложения по левому краю окна
# (x 0–42), подсказка n8n «Save time with an example of how this node works»
# (y 122–152) и целая колонка `INPUT` (x 55–735), пустая на момент съёмки.
# Из-за них композит был вдвое шире нужного, и кегль падал до 5,7 pt.
#
# Стало: правая половина — (752, 160, 1150, 358), 398×198: только центральная
# колонка `Parameters` и ровно те поля, ради которых слайд существует —
# `Source for Prompt (User Message)` = «Define below» и блок `Prompt (User
# Message)` с текстом правила. Тот же канон, что у панельных кропов волны 1а:
# колонки `INPUT`/`OUTPUT` в кадр не входят вовсе.
#
# Текст промпта обрезан САМИМ интерфейсом n8n на «…эскалироват» (textarea
# ограниченной высоты) — это не наша граница, и она не скрывается: полная
# формулировка правила по-прежнему несёт заметка слайда.
#
# Правая панель увеличена до высоты левого кропа (×1,63), чтобы колонки
# встали вровень. Увеличение не меняет видимый кегль панели в худшую сторону
# — наоборот, панель получает в 1,63 раза больше ширины слайда на тот же
# текст, чем левый канвас.
K3_PANEL_BOX = (752, 160, 1150, 358)


K3_PANEL_W = 660          # ширина правой колонки n34, см. `_to_width`


def reshenie_composite_new(lang="ru"):
    left = Image.open(OUT / "k3-n8n-if-uzel-real.png").convert("RGB")
    right, k = _to_width(
        Image.open(RAW / "case3a-model-decides.png").convert("RGB")
        .crop(K3_PANEL_BOX), K3_PANEL_W)
    if lang == "ru":
        parts = [(left, "Узел «Amount over threshold?» (IF) — версия 2",
                  "Условие в коде: число сравнивается с числом"),
                 (right, "Узел «Decide refund (model)» — версия 1",
                  "Правило — внутри текста промпта")]
    else:
        parts = [(left, "Node “Amount over threshold?” (IF) — version 2",
                  "Condition in code: number compared with number"),
                 (right, "Node “Decide refund (model)” — version 1",
                  # Короче русского оригинала сознательно: длинная строка
                  # уводила подпись на вторую строку и делала EN-композит
                  # на 56 px выше русского — две языковые версии одной
                  # фигуры разъехались бы по пропорции и встали на слайд
                  # по-разному. Оговорка «экран русский» сохранена.
                  "Rule inside the prompt text (screen in Russian)")]
    print(f"   правая панель увеличена ×{k:.2f} до ширины {K3_PANEL_W} px")
    return compose_c(parts)


for _lang, _name in (("ru", "k3-n8n-reshenie-real.png"),
                     ("en", "k3-n8n-reshenie-real-en.png")):
    _im = reshenie_composite_new(_lang)
    _ratio_note(_name, _im.width, _im.height, 4.57)
    save(_im, _name, note=f"канвас {K3_IF_BOX} + панель {K3_PANEL_BOX}")


# ── k3-n8n-variants-real(-en).png (n31) ────────────────────────────────────
#
# Было: 2566×477 — кропы (170, 425, 1470, 790) и (170, 425, 1400, 790). Оба
# начинались на x=170 при том, что контент начинается на x=532 и x=604
# соответственно: 360 и 430 пикселей слева были ЧИСТОЙ пустой сеткой, плюс
# в оба кадра входили кнопки «+» справа. Кегль 4,8 pt — ниже пола.
#
# Стало: (766, 404, 1430, 768) и (854, 404, 1358, 750) — 664×364 и 504×346,
# правая колонка увеличена до высоты левой. Границы подобраны по замеру
# не-фоновых пикселей, а потом проверены глазами: первый прогон резал на
# x=786 слева, и подпись подузла «Model (extraction)» (она начинается на
# x=773, левее своего кружка) выходила из кадра как «odel (extraction)».
#
# ЧТО СОЗНАТЕЛЬНО ВЫБРОШЕНО: узлы-триггеры `Refund request` (слева) и
# `Diag trigger` (справа). Это не экономия места ради экономии: при них
# композит выходит ~1750 px шириной и кегль ~7,0 pt — НИЖЕ пола, то есть
# фигура остаётся нечитаемой и перекроп бессмыслен. Триггер при этом —
# единственный узел, который у двух вариантов одинаков по смыслу и ничего
# не добавляет к сравнению; вопрос кадра — чем отличается УЗЕЛ РЕШЕНИЯ и что
# к нему подвешено (слева `Model (decision, Qwen2.5)`, справа `Agent model`
# + `Calculator`), и ровно это в кадре и остаётся, вместе с экранами
# результата. Входящая стрелка от срезанного триггера оставлена обрубком —
# видно, что слева что-то было.
#
# ЦЕНА, НАЗВАННАЯ ЧЕСТНО. Соотношение сторон падает с 5,38 до ~2,5. На
# слайде n31 фигуре отведено 1,60″ высоты (замер по собранной деке, см.
# шапку раздела), и при таком соотношении вёрстка поставит её шириной около
# 5,9″ вместо нынешних 8,6″ — то есть на слайде фигура станет МЕНЬШЕ, хотя
# текста на ней станет видно БОЛЬШЕ (кегль по методике брифа 4,8 → ~9 pt, по
# фактической вставке 3,4 → ~5,0 pt). Упор здесь не в кроп, а в слайд: над
# фигурой стоят четыре текстовых блока, и сборщик уже сейчас ужимает её до
# 70% полосы при собственном пороге 80%. Разводится это на уровне n31
# (своя страница для фигуры либо меньше блоков над ней) — вне зоны волны.
K3_V1_BOX = (766, 404, 1430, 768)
K3_V2_BOX = (854, 404, 1358, 750)


def variants_composite_new(lang="ru"):
    raw1 = Image.open(RAW / "case3-variant-clearer-prompt.png").convert("RGB")
    raw2 = Image.open(RAW / "case3-variant-calculator.png").convert("RGB")
    left = _before_after(raw1, (170, 425, 1470, 790), K3_V1_BOX,
                         "variants · слева «яснее правило»", 3.56)
    right_raw = _before_after(raw2, (170, 425, 1400, 790), K3_V2_BOX,
                              "variants · справа «калькулятор»", 3.37)
    right, k = _to_height(right_raw, left.height)
    print(f"   правая колонка увеличена ×{k:.2f} до высоты левой")
    if lang == "ru":
        parts = [(left, "Действие №1 — яснее правило в промте",
                  "Измерено: 100/100 на расширенном наборе"),
                 (right, "Действие №2 — модель с инструментом-калькулятором",
                  "Измерено: 56/100 — хуже всех вариантов")]
    else:
        parts = [(left, "Action #1 — clearer rule in the prompt",
                  "Measured: 100/100 on the extended set"),
                 (right, "Action #2 — model with a calculator",
                  "Measured: 56/100 — worse than every other option")]
    return compose_c(parts)


for _lang, _name in (("ru", "k3-n8n-variants-real.png"),
                     ("en", "k3-n8n-variants-real-en.png")):
    _im = variants_composite_new(_lang)
    _ratio_note(_name, _im.width, _im.height, 5.38)
    save(_im, _name, note=f"кропы {K3_V1_BOX} + {K3_V2_BOX}")


print("\nволна 1б: перекроено 8 фигур (+2 EN-спутника). "
      "Источник k3-n8n-reshenie/variants — ОТНЫНЕ этот файл, "
      "не make_figure_k3_real_captions.py.")
