#!/usr/bin/env python3
"""Волна 1г «конфетки» Семинара 8 (issue #292) — три НОВЫЕ фигуры ЖИВОГО шага
генерации карточки Кейса 4.

Решение владельца 2026-10-22 (вариант «б»): генерация должна реально стоять на
стенде. Она собрана (`stend/sborka.py: stage_4_generate`, workflow
`Yg4CcRdssgX3lfvw`), прогнана шесть раз (`stend/run_k4_generation.py`) и
измерена (`stend/k4-generatsiya-izmereniya-2026-10-22.md`). Здесь — кадры.

    k4-gen-tsepochka-real.png   кроп холста: развилка после записи заявки и
                                 ветка генерации целиком — пять узлов от
                                 шаблона текста до отправки фото
    k4-gen-panel-crop-real.png   панель узла генерации: адрес запроса с
                                 credential — и тело запроса, где видно, что
                                 просят картинку
    tg-k4-gen-kartochka.png      мокап Telegram с НАСТОЯЩЕЙ сгенерированной
                                 карточкой выполнения 600 и дословной подписью

ИСТОЧНИКИ. Холст и панель — `stend/n8n-screenshots-raw/case4-generatsiya-*.png`
(1900×1100, Playwright, живой стенд, сняты 2026-10-22 скриптом
`shoot_k4_generation.py`). Картинка в мокапе — файл, скачанный ОБРАТНО из
Telegram по `file_id` доставленного сообщения (`k4-gen-card-exec600-telegram.jpg`),
то есть ровно те пиксели, которые увидел получатель, уже после пережатия
Telegram'ом. Подпись пузыря — поле `result.caption` того же сообщения
(`message_id 16`), слово в слово.

ЧТО НА КАРТОЧКЕ НАПИСАНО НЕВЕРНО — И ПОЧЕМУ ЭТО НЕ ЧИНИТСЯ ЗДЕСЬ. Модель
получила точную строку и нарисовала «зяявка» вместо «заявка» и «заняятия»
вместо «занятия». Так во всех пяти удачных прогонах (см. раздел «Что видно
глазами» в файле измерений). Это измеренный результат шага, а не брак кадра:
подрисовывать буквы в сгенерированной картинке — подделка ровно того места,
ради которого кадр и ставится.

ЧТО НЕ ТРОГАЕТСЯ. `make_figures_crops.py`, `make_figures_k4.py` и
`make_figures_telegram.py` этим файлом не пересобираются — он только читает те
же исходники и пишет три НОВЫХ имени. Рамка чата берётся импортом из
`make_figures_telegram` (его `main()` под `if __name__`, импорт ничего не
перерисовывает), а разметка подписей — ПОВТОРЕНА здесь числами, не
импортирована: `make_figures_crops` при импорте выполнил бы себя целиком и
переписал двенадцать чужих фигур. Цена названа, а не спрятана: если полоса
подписи там изменится, этот файл правится руками.

Запуск: `python3 make_figures_k4gen.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import make_figures_telegram as tg

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

BAND_IN = 12.23        # ширина полосы контента слайда (deck_config.WIDTH)
FIG_MAX_H_IN = 4.3     # потолок высоты фигуры (deck_kit.FIG_NATURAL_H)
KEGL_FLOOR_PT = 7.5    # пол кегля на скринах (план §3.6)

PAD = 24
GAP = 30
SCALE = 2              # ×2 LANCZOS: проектор не ловит ступеньки на мелком тексте

CANVAS_RAW = "case4-generatsiya-holst-2026-10-22.png"
PANEL_RAW = "case4-generatsiya-uzel-2026-10-22.png"

# ── прямоугольники кропов, по исходникам 1900×1100 ─────────────────────────
#
# Цепочка. Левая граница 716 взята так, чтобы в кадр вошёл узел `Write row`:
# ветка генерации не висит в воздухе, она отходит от той же записи заявки, что
# и экран результата, — и развилка на кадре видна. Правая 1800 — сразу за
# узлом отправки, до вертикальной панели кнопок у правого края интерфейса.
# Верх 318 и низ 585 режут по карточкам узлов обеих строк вместе с их
# подписями: выше нет ничего, кроме пустой сетки и вкладок
# `Editor/Executions/Evaluations`, ниже — пустая сетка и кнопка `Execute
# workflow`. Низ подобран дважды: по 545 кадр резал нижний ряд ПОД карточками,
# и `Write row` с `Result screen` стояли в кадре безымянными коробками — хуже,
# чем не показать их вовсе. Ни id воркфлоу, ни бейджа `Published`, ни хлебных
# крошек в кадр не попадает (канон кропа — `make_figures_k2.py:
# test_stend_real()`).
CHAIN_BOX = (716, 318, 1800, 585)

# Панель узла генерации. ТРИ прямоугольника с ОДНОГО скрина:
# A1 — `Method` = POST и адрес chat/completions: это обычный HTTP-запрос;
# A2 — `Authentication`/`Credential Type`/`OpenRouter account`: ключ взят из
#      credential стенда, а не вписан в узел;
# B  — поле `JSON`: тело запроса, где стоит то единственное, чем этот вызов
#      отличается от текстового, — `modalities: ['image', 'text']`.
# Между A2 и B на панели лежат четыре нетронутых переключателя (`Send Query
# Parameters`/`Send Headers`/`Send Body`/`Body Content Type`), y≈500–830; взять
# их одним прямоугольником — значит отдать им треть кадра. Пропуск назван.
#
# Почему три колонки, а не две (замер при сборке): две колонки дают композит
# 830×470, пропорция 1,77 — на слайде он упирается в потолок высоты 4,3″ и
# занимает 7,59″ из 12,23″, то есть 62% полосы, и ловит `СХЕМА ЗАЖАТА`
# (`deck_kit`: FIG_MIN_FILL 80%). Три колонки — пропорция 4,6, полоса занята
# целиком, кегль интерфейса 12 px = 8,4 pt, выше пола 7,5 pt.
PANEL_A1 = (752, 158, 1152, 292)
PANEL_A2 = (752, 296, 1152, 482)
PANEL_B = (752, 832, 1152, 978)

_MEASURE = ImageDraw.Draw(Image.new("RGB", (8, 8)))


def _font(sz, bold=False):
    return ImageFont.truetype(FB if bold else F, sz)


def _wrap(text, font, avail):
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
    for fs in range(max_fs, min_fs - 1, -1):
        f = _font(fs, bold)
        lines = _wrap(text, f, avail)
        if len(lines) <= max_lines and all(
                _MEASURE.textlength(ln, font=f) <= avail for ln in lines):
            return f, lines, fs
    f = _font(min_fs, bold)
    return f, _wrap(text, f, avail)[:max_lines], min_fs


def caption_plan(w, title, subtitle):
    avail = w - 2 * PAD
    ft, tl, tfs = _fit(title, avail, max_fs=25, min_fs=17, max_lines=2, bold=True)
    fs_, sl, sfs = _fit(subtitle, avail, max_fs=21, min_fs=15, max_lines=2, bold=True)
    th, sh = int(tfs * 1.22), int(sfs * 1.24)
    return dict(ft=ft, tl=tl, th=th, fs=fs_, sl=sl, sh=sh,
                h=14 + th * len(tl) + 6 + sh * len(sl) + 14)


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


def column(crop, plan, cap_h, body_h):
    out = Image.new("RGB", (crop.width, cap_h + body_h), W)
    out.paste(caption_bar(crop.width, cap_h, plan), (0, 0))
    y = cap_h + (body_h - crop.height) // 2
    out.paste(crop, (0, y))
    d = ImageDraw.Draw(out)
    d.line([(0, cap_h), (crop.width, cap_h)], fill=DEEP, width=2)
    d.rectangle([0, y, crop.width - 1, y + crop.height - 1], outline=LIGHT, width=2)
    return out


def compose(parts):
    """Полосы подписей выровнены по низу, рамки кропов начинаются на одном
    уровне — высота подписи и высота тела считаются по всему композиту."""
    plans = [caption_plan(c.width, t, s) for c, t, s in parts]
    cap_h = max(p["h"] for p in plans)
    body_h = max(c.height for c, _, _ in parts)
    cols = [column(c, p, cap_h, body_h) for (c, _, _), p in zip(parts, plans)]
    total_w = sum(c.width for c in cols) + GAP * (len(cols) - 1)
    out = Image.new("RGB", (total_w, cap_h + body_h), W)
    x = 0
    for c in cols:
        out.paste(c, (x, 0))
        x += c.width + GAP
    return out


def _kegl(name, im, src_px_per_fig_px):
    """Сколько пунктов на слайде даёт один пиксель ИСХОДНОГО скрина.

    `src_px_per_fig_px` — во сколько раз кроп увеличен при сборке: один
    пиксель исходника занимает столько пикселей PNG, и кегль на экране зала
    считается от него, а не от размера файла (как в `make_figures_crops._kegl`)."""
    w_in = min(BAND_IN, FIG_MAX_H_IN * im.width / im.height)
    pt = w_in * 72 / im.width * src_px_per_fig_px
    flag = "" if 12 * pt >= KEGL_FLOOR_PT - 0.05 else "   ← 12 px НИЖЕ ПОЛА 7,5 pt"
    print(f"   кегль [{name}]: {im.size}, пропорция {im.width / im.height:.2f}, "
          f"{w_in:.2f}″ на слайде → 12 px = {12 * pt:.1f} pt, "
          f"14 px = {14 * pt:.1f} pt, 17 px = {17 * pt:.1f} pt{flag}")


def chain():
    """Кроп ветки генерации. Один честный прямоугольник, увеличенный ×2."""
    src = Image.open(RAW / CANVAS_RAW).convert("RGB").crop(CHAIN_BOX)
    big = src.resize((src.width * SCALE, src.height * SCALE), Image.LANCZOS)
    out = Image.new("RGB", big.size, W)
    out.paste(big, (0, 0))
    ImageDraw.Draw(out).rectangle(
        [0, 0, out.width - 1, out.height - 1], outline=DEEP, width=2 * SCALE)
    return out


def panel():
    src = Image.open(RAW / PANEL_RAW).convert("RGB")
    return compose([
        (src.crop(PANEL_A1), "Узел «Generate card (OpenRouter image)»",
         "Запрос POST на chat/completions"),
        (src.crop(PANEL_A2), "Чем подписан запрос",
         "Ключ — из credential стенда, не из узла"),
        (src.crop(PANEL_B), "Тело запроса",
         "modalities: image — просим картинку, а не текст"),
    ])


# ── Дословная подпись доставленного сообщения ──────────────────────────────
# Выполнение 600, `result.caption`, `message_id 16`, 22.10.2026 13:55 МСК.
# Источник — `stend/n8n-screenshots-raw/exec-600-k4-generatsiya.json`.
T_K4_GEN = "Новая заявка от Олег: тема «перенос занятия»."


def telegram_card():
    photo = Image.open(RAW / "k4-gen-card-exec600-telegram.jpg").convert("RGB")
    return tg.canvas(tg.CHAT_NAME, tg.CHAT_SUB, [
        dict(text=T_K4_GEN, time_s="13:55", sender=tg.BOT_NAME, photo=photo),
    ])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    c = chain()
    c.save(OUT / "k4-gen-tsepochka-real.png")
    _kegl("k4-gen-tsepochka-real", c, SCALE)
    print(f"   провенанс: {CANVAS_RAW} {CHAIN_BOX} ×{SCALE} LANCZOS")

    p = panel()
    p.save(OUT / "k4-gen-panel-crop-real.png")
    _kegl("k4-gen-panel-crop-real", p, 1.0)
    print(f"   провенанс: {PANEL_RAW} {PANEL_A1} + {PANEL_A2} + {PANEL_B}")

    t = telegram_card()
    t.save(OUT / "tg-k4-gen-kartochka.png")
    print(f"   tg-k4-gen-kartochka.png {t.size}  "
          f"(карточка выполнения 600, подпись дословная)")


if __name__ == "__main__":
    main()
