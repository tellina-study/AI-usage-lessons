#!/usr/bin/env python3
"""Галерея шести настоящих размеров `receipt-01` — такт n73a Кейса 6, issue #299.

Экспозиция замера «единый вызов против двух шагов» (`zamery-k6-edinyy`, С2
канона — «структура теста ДО результатов») ссылалась на входные картинки
только таблицей чисел. Владелец курса на разборе 2026-10-29 повторил
просьбу показать сами картинки, в полном размере, трижды за один проход
деки (РАЗБОР-2026-10-29.md, К6-10) — до этого коммита картинок не было ни
на одном такте Кейса 6, кроме двух кропов границы (n72a/n72b, см.
`build_k6_field_crops.py`), которые режут поле, а не показывают файл
целиком.

Этот скрипт кладёт все шесть файлов `receipts/resolution/receipt-01-*.png`
рядом, с ОБЩИМ коэффициентом масштабирования — то есть не выравнивает их
по одной высоте показа (как сделано в `build_k6_field_crops.py` для пары
читается/не читается), а показывает НАСТОЯЩЕЕ соотношение размеров: кадр
`thirtysecond` (53×64 пикс.) на этой картинке действительно в тридцать два
раза меньше `full` (1698×2074), а не искусственно подогнан под читаемость.
Это и есть ответ на «сколько картинок — пять» (и шестая) владельца:
зритель видит настоящее соотношение, не выдуманное.

Коэффициент — 0,2 (как у `full`, так получается высота около 415 пикс.,
удобно для одного ряда на слайде 16:9). LANCZOS для всех — здесь не нужна
блочность NEAREST из `build_k6_field_crops.py` (та показывала, что получает
МОДЕЛЬ на одном конкретном разрешении без сглаживания; здесь задача другая —
дать зрителю опознать документ на крупных кадрах и честно увидеть, что
мелкие кадры опознать нельзя).

Запуск: `python3 build_k6_gallery.py` (из этой папки).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
RES = HERE / "receipts" / "resolution"
OUT = HERE.parent.parent / "rendered" / "figures"

SCALE = 0.2
GAP = 22
MARGIN = 30
LABEL_H = 56
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LABEL_FONT = ImageFont.truetype(FONT_BOLD, 20)
NAVY = (20, 40, 80)
GOLD = (200, 120, 0)

# (файл, подпись, подпись-то-же-цветом-что-итог) — порядок как в n70/n71.
# «меньше» опущено во всех, кроме первого, — слово общее для всей строки
# подписей и повторять его шесть раз незачем (та же экономия, что С11).
PANELS = [
    ("full", "исходный\n1698×2074", NAVY),
    ("half", "вдвое меньше\n849×1037", NAVY),
    ("quarter", "в 4 раза\n424×518", NAVY),
    ("eighth", "в 8 раз\n212×259", NAVY),
    ("sixteenth", "в 16 раз\n106×129", NAVY),
    ("thirtysecond", "в 32 раза\n53×64", GOLD),
]


SLOT_W = 226  # фиксированная ширина «дорожки» под каждую картинку: подписи не
# умещаются под настоящей шириной мелких кадров (11–42 пикс.) — три самых
# мелких накладывались друг на друга в первой версии, и соседние подписи
# налезали друг на друга даже при первой починке (190 пикс. ещё тесно для
# «вдвое меньше» 24pt). Слот один и тот же для всех шести, картинка внутри
# него прижата к НИЖНЕМУ краю и центрирована по горизонтали — так видно, что
# слот пустеет, а не что подпись ужалась.


def main():
    imgs = []
    for name, label, color in PANELS:
        im = Image.open(RES / f"receipt-01-{name}.png")
        w, h = im.size
        new_w, new_h = round(w * SCALE), round(h * SCALE)
        imgs.append((im.resize((new_w, new_h), Image.LANCZOS), label, color))

    panel_h = max(h for (im, _l, _c) in imgs for h in (im.size[1],))
    total_w = MARGIN * 2 + SLOT_W * len(imgs) + GAP * (len(imgs) - 1)
    total_h = panel_h + LABEL_H + MARGIN * 2

    canvas = Image.new("RGB", (total_w, total_h), "white")
    d = ImageDraw.Draw(canvas)
    x = MARGIN
    for im, label, color in imgs:
        w, h = im.size
        # картинки прижаты к низу общего ряда (панели разной высоты) — так
        # подписи все на одной строке, а не пляшут по вертикали.
        canvas.paste(im, (x + round((SLOT_W - w) / 2), MARGIN + (panel_h - h)))
        lines = label.split("\n")
        ly = MARGIN + panel_h + 8
        for line in lines:
            bbox = d.textbbox((0, 0), line, font=LABEL_FONT)
            lw = bbox[2] - bbox[0]
            d.text((x + SLOT_W / 2 - lw / 2, ly), line, font=LABEL_FONT, fill=color)
            ly += 26
        x += SLOT_W + GAP

    out_path = OUT / "k6-galereya-shesti-razmerov.png"
    canvas.save(out_path)
    print(f"-> {out_path} {canvas.size}")


if __name__ == "__main__":
    main()
