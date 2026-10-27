#!/usr/bin/env python3
"""Строит два composite-кропа для деки Семинара 9, Кейс 6 (issue #299, владелец 2026-10-27):

1. `k6-zoom-data-porog-granitsa.png` — поле "дата", НАСТОЯЩАЯ граница порога чтения:
   quarter (424×518, последнее читаемое разрешение, 5/5 по README) против
   eighth (212×259, первое нечитаемое, 0/5). Старый кроп (`k6-zoom-data-porog.png`,
   остаётся на n72a) показывал крайности (full vs thirtysecond) — этот кроп показывает
   именно порог, не края диапазона.
2. `k6-zoom-summa-melkaya.png` — поле "сумма" на самом мелком разрешении (thirtysecond,
   53×64) рядом с полным размером. Несущая находка: сумма НЕ сломалась ни разу из 26
   попыток (README, Замер 4.1) — контринтуитивный результат, которого раньше не было
   проиллюстрировано ни одним кропом в деке.

Метод идентичен уже применённому для `k6-zoom-data-porog.png` (git 142659a71): один и тот
же регион поля вырезается из НАСТОЯЩЕГО файла каждого разрешения (не пересжимается из
full — то есть сравниваются буквально те же байты, что уходили в модель), затем
увеличивается: LANCZOS для читаемой/крупной стороны, NEAREST для нечитаемой/блочной — без
сглаживания, честно показывает блочность (а не домысленные моделью пиксели).

Координаты регионов (date_full_box / amount_full_box ниже) получены не "на глаз": сначала
вычислена bbox текста на ЧИСТОМ canvas (1200×1600) через реальный рендер шрифта
(`ImageFont.getbbox`, те же draw-координаты, что в `generate_receipts.py:draw_receipt`),
затем эта bbox спроецирована на фото через bbox самой бумаги квитанции на фото
(порог яркости между "бумага" и "стол", найденный по гистограмме). Результат проверен
визуально (кроп увеличен и прочитан) перед тем, как зафиксирован в этом файле.

Запуск:
    python3 build_k6_field_crops.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
RES = HERE / "receipts" / "resolution"
OUT = HERE.parent.parent / "rendered" / "figures"

NAVY = (20, 40, 80)   # тот же navy, что в k6-zoom-data-porog.png (проверено пипеткой)
GOLD = (200, 120, 0)  # тот же gold, что в k6-zoom-data-porog.png (проверено пипеткой)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TITLE_FONT = ImageFont.truetype(FONT_BOLD, 26)
MARGIN = 20
GAP = 40
TITLE_H = 70  # измерено по исходному k6-zoom-data-porog.png — картинка начинается с y=70

# Регион поля "дата" (label+value, с отступом) на receipt-01-full.png (1698×2074, scale=1.0).
DATE_FULL_BOX = (275, 593, 565, 692)
# Регион поля "сумма" (label+value, с отступом) на receipt-01-full.png.
AMOUNT_FULL_BOX = (280, 1040, 800, 1185)


def build_composite(left_img, left_title, left_color, right_img, right_title,
                     right_color, out_path, panel_height):
    tmp = Image.new("RGB", (10, 10))
    d0 = ImageDraw.Draw(tmp)

    def scaled(img):
        w, h = img.size
        new_h = panel_height
        new_w = round(w * new_h / h)
        return new_w, new_h

    def text_w(s):
        bbox = d0.textbbox((0, 0), s, font=TITLE_FONT)
        return bbox[2] - bbox[0]

    lw_img, lh = scaled(left_img)
    rw_img, rh = scaled(right_img)
    # ширина панели = максимум из (ширина увеличенной картинки, ширина заголовка) —
    # иначе длинный заголовок обрезается по правому краю (поймано на первой версии).
    lw = max(lw_img, text_w(left_title))
    rw = max(rw_img, text_w(right_title))

    left_up = left_img.resize((lw_img, lh), Image.LANCZOS)
    right_up = right_img.resize((rw_img, rh), Image.NEAREST)

    total_w = MARGIN + lw + GAP + rw + MARGIN
    total_h = TITLE_H + panel_height
    canvas = Image.new("RGB", (total_w, total_h), "white")
    d = ImageDraw.Draw(canvas)
    left_x = MARGIN
    right_x = MARGIN + lw + GAP
    d.text((left_x, 10), left_title, font=TITLE_FONT, fill=left_color)
    d.text((right_x, 10), right_title, font=TITLE_FONT, fill=right_color)
    canvas.paste(left_up, (left_x, TITLE_H))
    canvas.paste(right_up, (right_x, TITLE_H))
    canvas.save(out_path)
    print(f"-> {out_path} {canvas.size}")


def main():
    quarter_box = tuple(round(v * 0.25) for v in DATE_FULL_BOX)
    eighth_box = tuple(round(v * 0.125) for v in DATE_FULL_BOX)
    quarter_im = Image.open(RES / "receipt-01-quarter.png").crop(quarter_box)
    eighth_im = Image.open(RES / "receipt-01-eighth.png").crop(eighth_box)
    build_composite(
        quarter_im, "Четверть, 424×518 — дата читается (5/5)", NAVY,
        eighth_im, "Восьмая, 212×259 — дата НЕ читается (0/5)", GOLD,
        OUT / "k6-zoom-data-porog-granitsa.png", panel_height=248,
    )

    thirtysecond_box = tuple(round(v * 0.03125) for v in AMOUNT_FULL_BOX)
    full_im = Image.open(RES / "receipt-01-full.png").crop(AMOUNT_FULL_BOX)
    thirtysecond_im = Image.open(RES / "receipt-01-thirtysecond.png").crop(thirtysecond_box)
    build_composite(
        full_im, "Полный размер, 1698×2074 — сумма читается", NAVY,
        thirtysecond_im, "1/32, 53×64 — сумма читается (5/5)", GOLD,
        OUT / "k6-zoom-summa-melkaya.png", panel_height=220,
    )

    # Слайд n72b несёт только ОДИН `figure:` в фронтматтере (однослайдовый
    # формат деки — см. deck_config.figure_for), поэтому для него собирается
    # третий файл: те же два готовых composite сверху вниз, не пересобранные
    # заново из кропов — просто сложены в один холст с отступом.
    top = Image.open(OUT / "k6-zoom-data-porog-granitsa.png")
    bottom = Image.open(OUT / "k6-zoom-summa-melkaya.png")
    pad = 30
    w = max(top.width, bottom.width)
    h = top.height + pad + bottom.height
    combined = Image.new("RGB", (w, h), "white")
    combined.paste(top, ((w - top.width) // 2, 0))
    combined.paste(bottom, ((w - bottom.width) // 2, top.height + pad))
    combined_path = OUT / "k6-zoom-granitsy-oba-polya.png"
    combined.save(combined_path)
    print(f"-> {combined_path} {combined.size}")


if __name__ == "__main__":
    main()
