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

Собирает сегодня ОДИН композит (и его EN-близнеца):

    k3-n8n-nastroyka-uzlov.png      две панели настройки узлов версии 2
                                     (Extract amount, Amount over
                                     threshold?), подписаны именем узла.

ОТКЛЮЧЕНО волной 2б (issue #292) — `k3-n8n-variants-real(-en).png` и
`k3-n8n-reshenie-real(-en).png`: те же четыре имени собирает
`make_figures_crops.py` волны 1б, и по БОЛЕЕ УЗКИМ прямоугольникам, поднявшим
кегль подписей интерфейса выше пола 7,5 pt. Прогон этого файла возвращал бы
прежний, заваленный кегль молча. Подробности и способ снять отключение — у
блока `_OTKLYUCHENO` ниже.

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


# ── ВОЛНА 2б «конфетки» (issue #292): ЧЕТЫРЕ ЦЕЛИ ОТКЛЮЧЕНЫ ────────────────
#
# `k3-n8n-variants-real(-en).png` и `k3-n8n-reshenie-real(-en).png` с волны 1б
# собираются `make_figures_crops.py` — по ПЕРЕКРОПЛЕННЫМ, узким
# прямоугольникам, поднявшим кегль подписей интерфейса выше пола 7,5 pt
# (там же, в шапке того файла, замеры «было → стало»: reshenie 5,7 pt,
# variants 4,8 pt — обе ниже пола). Этот файл режет те же снимки СТАРЫМИ,
# широкими прямоугольниками, и его прогон молча возвращал бы прежний кегль.
#
# Тот файл честно назвал ловушку в своём комментарии и оставил её жить,
# потому что ЭТОТ файл был вне его волны. Волна 2б закрывает её здесь:
# функции-композиты оставлены на месте (в них записано, какими были старые
# прямоугольники — это история, а не мусор), но `save` по этим четырём
# именам больше не вызывается. Два оставшихся имени
# (`k3-n8n-nastroyka-uzlov(-en).png`) собирает только этот файл, у них
# пересечения нет, и они пишутся как прежде.
#
# Снять отключение можно ровно одним способом: привести прямоугольники
# `crop1`/`crop2`/`crop_model` в соответствие с `make_figures_crops.py` и
# замерить кегль — не раньше.
_OTKLYUCHENO = (
    "k3-n8n-variants-real.png", "k3-n8n-variants-real-en.png",
    "k3-n8n-reshenie-real.png", "k3-n8n-reshenie-real-en.png",
)


def skip(name):
    print(f"   ПРОПУЩЕНО {name}: источник — make_figures_crops.py "
          f"(волна 1б, перекроп под пол кегля 7,5 pt)")


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


skip("k3-n8n-variants-real.png")          # было: save(variants_composite(), …)


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


skip("k3-n8n-reshenie-real.png")          # было: save(reshenie_composite(), …)

print("\nготово: k3-n8n-nastroyka-uzlov.png. "
      f"Отключено целей: {len(_OTKLYUCHENO)} — их собирает make_figures_crops.py.")


# ── EN companions (issue #274, EN track, Кейс 3) ─────────────────────────────
#
# Подписи — РИСОВАННЫЙ ТЕКСТ (caption_bar), а не пиксели настоящего
# интерфейса, поэтому их можно и нужно перевести; нижележащие кропы живого
# стенда не трогаются — те же файлы `RAW/*.png`, что и у русских композитов
# выше. EN-варианты собраны отдельными функциями (не через fig_toolkit
# --lang/fig_strings_en.py: тот словарь общий на все рисовалки кейсов этого
# занятия, и правка его из зоны одного переводчика — Кейс 3 — рисковала бы
# столкнуться с параллельными переводчиками других кейсов). Имя выходного
# файла задаётся явно строкой в save(), без языкового патча `_save`.

def variants_composite_en():
    raw1 = Image.open(RAW / "case3-variant-clearer-prompt.png").convert("RGB")
    raw2 = Image.open(RAW / "case3-variant-calculator.png").convert("RGB")
    crop1 = raw1.crop((170, 425, 1470, 790))
    crop2 = raw2.crop((170, 425, 1400, 790))

    left = stack_caption_and_crop(
        crop1,
        "Action #1 — clearer rule in the prompt",
        "Measured: 100/100 on the extended set")
    right = stack_caption_and_crop(
        crop2,
        "Action #2 — model with a calculator",
        "Measured: 56/100 — worse than every other option")
    return hcompose([left, right])


skip("k3-n8n-variants-real-en.png")       # было: save(variants_composite_en(), …)


def nastroyka_uzlov_composite_en():
    raw_extract = Image.open(RAW / "case3-extract-amount.png").convert("RGB")
    raw_if = Image.open(RAW / "case3-if-threshold.png").convert("RGB")
    crop_extract = raw_extract.crop((0, 0, 1180, 580))
    crop_if = raw_if.crop((0, 0, 1280, 580))

    left = stack_caption_and_crop(
        crop_extract,
        "Node “Extract amount” (Information Extractor)",
        "Schema: amount_rub — number, required field")
    right = stack_caption_and_crop(
        crop_if,
        "Node “Amount over threshold?” (IF)",
        "Condition: amount_rub is greater than 3000")
    return hcompose([left, right])


save(nastroyka_uzlov_composite_en(), "k3-n8n-nastroyka-uzlov-en.png")


def reshenie_composite_en():
    """Левая половина — тот же уже готовый кроп канваса `k3-n8n-if-uzel-real.png`
    (узел не подписан собственным текстом — на нём нет кириллицы помимо имён
    узлов n8n, которые и в RU, и в EN деке читаются одинаково, см. glossary.en
    note о UI-строках). Правая половина — тот же кроп панели промпта версии 1
    (`case3a-model-decides.png`): сам промпт на экране остаётся на русском
    (честное исключение — бот обслуживает русскоязычный учебный центр), на EN
    меняется только рисованная подпись бара."""
    left_raw = Image.open(OUT / "k3-n8n-if-uzel-real.png").convert("RGB")
    raw_model = Image.open(RAW / "case3a-model-decides.png").convert("RGB")
    crop_model = raw_model.crop((0, 0, 1160, 358))

    left = stack_caption_and_crop(
        left_raw,
        "Node “Amount over threshold?” (IF) — version 2",
        "Condition in code: number compared with number")
    right = stack_caption_and_crop(
        crop_model,
        "Node “Decide refund (model)” — version 1",
        "The rule lives inside the prompt text (shown in Russian — real screen)")
    return hcompose([left, right])


skip("k3-n8n-reshenie-real-en.png")       # было: save(reshenie_composite_en(), …)

print("\nEN done: k3-n8n-nastroyka-uzlov-en.png. "
      "variants/reshenie are produced by make_figures_crops.py — see the "
      "note above.")
