#!/usr/bin/env python3
"""Кейс «Одобрение возврата» Семинара 8 (issue #274) — композиты из НАСТОЯЩИХ
скринов живого стенда n8n, с явной подписью над каждой половиной.

Повод (голосовая правка владельца, замечание 1 к Кейсу 3): композит
`k3-n8n-variants-real.png` (n31) клал два настоящих воркфлоу рядом БЕЗ
подписи, какой узел — это что: «подпиши явно... где версия 2 а где то что
отбросили и над ними дай описание, сейчас хрен поймешь в полотне текста что
есть что». ImageMagick (`convert`/`magick`) в этой среде не установлен —
подписи рисуются тем же PIL, что и программные схемы кейса
(`fig_toolkit.py`), тем же шрифтом и той же палитрой Ocean.

Два композита:

    k3-n8n-variants-real.png        n31 — два варианта измерения действий
                                     №1/№2 (яснее правило / калькулятор),
                                     подписаны результатом измерения.
    k3-n8n-nastroyka-uzlov.png      n34b (НОВЫЙ слайд) — две панели
                                     настройки узлов версии 2 (Extract
                                     amount, Amount over threshold?),
                                     подписаны именем узла.

Источник — RAW-скрины `stend/n8n-screenshots-raw/*.png` (Playwright,
2026-10-20, живой стенд https://n8n.lessons.tellian.io), не прежние
композиты: кроп режется заново из необрезанных файлов, чтобы граница кропа
была проверяема по исходнику, а не унаследована от предыдущего прогона.

Запуск: `python3 make_figure_k3_real_captions.py` (из `rendered/`).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"

# Палитра Ocean — те же HEX, что в tools/seminar-build/fig_toolkit.py.
DEEP = (0x21, 0x29, 0x5C)
MID = (0x06, 0x5A, 0x82)
GOLD = (0xF0, 0xAB, 0x00)
SUBT = (0xBF, 0xDD, 0xEA)   # светло-голубой — подстрока на тёмном Ocean-фоне
W = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

CAP_H = 112          # высота полосы подписи над каждой половиной
GAP = 36              # зазор между половинами (белый, с тонкой осевой чертой)
PAD = 28               # внутренний отступ подписи слева


def _font(sz, bold=False):
    return ImageFont.truetype(FB if bold else F, sz)


def caption_bar(w, h, title, subtitle):
    """Полоса подписи: фон Ocean MID, заголовок белым, подстрока крупным
    золотом/голубым — то самое «описание над каждой половиной», которого
    не хватало."""
    im = Image.new("RGB", (w, h), MID)
    d = ImageDraw.Draw(im)
    ft, fs = _font(27, True), _font(23, True)
    d.text((PAD, 18), title, font=ft, fill=W)
    d.text((PAD, 18 + 34), subtitle, font=fs, fill=GOLD if "100/100" in subtitle
           else SUBT)
    return im


def stack_caption_and_crop(crop, title, subtitle):
    cap = caption_bar(crop.width, CAP_H, title, subtitle)
    out = Image.new("RGB", (crop.width, CAP_H + crop.height), W)
    out.paste(cap, (0, 0))
    out.paste(crop, (0, CAP_H))
    # тонкая разделительная линия между подписью и скрином
    d = ImageDraw.Draw(out)
    d.line([(0, CAP_H), (crop.width, CAP_H)], fill=DEEP, width=2)
    return out


def hcompose(panels, gap=GAP):
    h = max(p.height for p in panels)
    w = sum(p.width for p in panels) + gap * (len(panels) - 1)
    out = Image.new("RGB", (w, h), W)
    x = 0
    for i, p in enumerate(panels):
        y = (h - p.height) // 2
        out.paste(p, (x, y))
        x += p.width
        if i < len(panels) - 1:
            d = ImageDraw.Draw(out)
            cx = x + gap // 2
            d.line([(cx, 8), (cx, h - 8)], fill=(0xD8, 0xDE, 0xE6), width=2)
            x += gap
    return out


def save(im, name):
    p = OUT / name
    im.save(p)
    print("  ", name, im.size)


# ── n31: два варианта измерения, подписанные явно ───────────────────────────
def variants_composite():
    raw1 = Image.open(RAW / "case3-variant-clearer-prompt.png").convert("RGB")
    raw2 = Image.open(RAW / "case3-variant-calculator.png").convert("RGB")
    crop1 = raw1.crop((170, 425, 1470, 790))   # «яснее правило» — воркфлоу целиком
    crop2 = raw2.crop((170, 425, 1400, 790))   # «калькулятор» — воркфлоу целиком

    left = stack_caption_and_crop(
        crop1,
        "Действие №1 — яснее правило в промте",
        "Измерено: 100/100 на расширенном наборе")
    right = stack_caption_and_crop(
        crop2,
        "Действие №2 — модель с калькулятором",
        "Измерено: 56/100 — хуже всех вариантов")
    return hcompose([left, right])


save(variants_composite(), "k3-n8n-variants-real.png")


# ── n34b (новый слайд): панели настройки узлов версии 2 ─────────────────────
def nastroyka_uzlov_composite():
    raw_extract = Image.open(RAW / "case3-extract-amount.png").convert("RGB")
    raw_if = Image.open(RAW / "case3-if-threshold.png").convert("RGB")
    crop_extract = raw_extract.crop((0, 0, 1180, 580))   # заголовок + Input Schema JSON
    crop_if = raw_if.crop((0, 0, 1280, 580))             # заголовок + условие + Options

    left = stack_caption_and_crop(
        crop_extract,
        "Узел «Extract amount» (Information Extractor)",
        "Схема: amount_rub — число, обязательное поле")
    right = stack_caption_and_crop(
        crop_if,
        "Узел «Amount over threshold?» (IF)",
        "Условие: amount_rub is greater than 3000")
    return hcompose([left, right])


save(nastroyka_uzlov_composite(), "k3-n8n-nastroyka-uzlov.png")


# ── n34 (замечание владельца 2026-10-20, круг 2): проза про промпт версии 1
# заменена настоящим скрином панели «Decide refund (model)» ──────────────────
def reshenie_composite():
    """Левая половина — уже готовый кроп канваса `k3-n8n-if-uzel-real.png`
    (узел `IF` версии 2, как на холсте). Правая половина — НОВЫЙ кроп
    `stend/n8n-screenshots-raw/case3a-model-decides.png` (0,0)-(1160,358):
    заголовок панели + колонка INPUT («Extract amount» → `output` →
    `amount_rub`) + блок `Prompt (User Message)` версии 1. Текст в поле
    промпта обрезан самим интерфейсом n8n на «...эскалироват» (textarea с
    ограниченной высотой, не наша обрезка) — подпись и заметки слайда это не
    скрывают, полную формулировку правила по-прежнему несёт speaker notes."""
    left_raw = Image.open(OUT / "k3-n8n-if-uzel-real.png").convert("RGB")
    raw_model = Image.open(RAW / "case3a-model-decides.png").convert("RGB")
    crop_model = raw_model.crop((0, 0, 1160, 358))

    left = stack_caption_and_crop(
        left_raw,
        "Узел «Amount over threshold?» (IF) — версия 2",
        "Условие в коде: число сравнивается с числом")
    right = stack_caption_and_crop(
        crop_model,
        "Узел «Decide refund (model)» — версия 1",
        "Правило — внутри текста промпта")
    return hcompose([left, right])


save(reshenie_composite(), "k3-n8n-reshenie-real.png")

print("\nготово: k3-n8n-variants-real.png (n31, подписан), "
      "k3-n8n-nastroyka-uzlov.png (n34a, подписан), "
      "k3-n8n-reshenie-real.png (n34, новый — IF-узел версии 2 рядом с "
      "панелью промпта версии 1)")
