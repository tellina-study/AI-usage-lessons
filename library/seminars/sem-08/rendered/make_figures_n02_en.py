#!/usr/bin/env python3
"""EN-вариант фигуры `n02` (issue #172/#274, первый круг EN-трека занятия):
`shov-s7-obzor-klassifikatsii-en.png` — тот же настоящий снимок живого
холста n8n, что и в русской фигуре, с английской подписью снизу.

**Почему не через `fig_toolkit`.** Фигура `n02` — не программная схема, а
аннотированный СКРИНШОТ: `sem-07/rendered/annotate_shots.py`, функция
`annotate`, кладёт нумерованные кружки и текстовую подпись поверх настоящего
кадра `n8n-holst-stage1.png` (интерфейс не перерисован). У `fig_toolkit`
нет понятия «снимок экрана» — его `T()`/`set_lang()` патчат `ImageDraw.text`
для ПРОГРАММНЫХ фигур; снимку это не нужно и не подходит.

**Почему не правка `sem-07/rendered/annotate_shots.py`.** Правило «чужая
папка семинара не правится» (CLAUDE.md, Anti-Patterns): файл Семинара 7
не трогаем. Эта функция — ЛОКАЛЬНАЯ копия `annotate()` (та же логика,
дословно), вызванная ровно один раз, с теми же координатами меток и тем же
исходным кадром, но с английской подписью. Кружки с цифрами 1–6 — не текст,
а геометрия с арабскими цифрами (ASCII), поэтому языка не имеют и не
меняются между RU и EN вовсе; переводится только двухстрочная подпись в
нижней полосе.

Исходный кадр читается НАПРЯМУЮ из `sem-07/rendered/figures/n8n-holst-stage1.png`
(то же самое чтение, каким `annotate_shots.py` собрал `obzor-k1.png`, которую
`sem-08/rendered/figures/shov-s7-obzor-klassifikatsii.png` копирует без
изменений, см. `slides/n02-shov-s7-s8.md` backup) — чтение, не запись: ничего
в папке Семинара 7 этим скриптом не создаётся и не меняется.

Перевод подписи сверен с `glossary.en.yaml` этого занятия, где термин есть
(`extract/extraction`); для шагов без отдельной записи в словаре — прямой
перевод формулировки `annotate_shots.py`, не слайда (та же подпись, что и
на RU-фигуре, а не формулировка из текста `n02-shov-s7-s8.md`).

Запуск: `python3 make_figures_n02_en.py` (из `rendered/` папки Семинара 8).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SEM07_FIGURES = Path(__file__).resolve().parents[2] / "sem-07" / "rendered" / "figures"
OUT = Path(__file__).resolve().parent / "figures"

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TEAL, INK, W = (0x02, 0x80, 0x90), (0x14, 0x1B, 0x2E), (255, 255, 255)
SURF = (0xF4, 0xF7, 0xFA)

# Дословная копия `annotate()` из `sem-07/rendered/annotate_shots.py` —
# не импорт (см. докстринг выше). Единственное отличие: исходный снимок
# читается из ЧУЖОЙ папки по абсолютному пути (только чтение), а результат
# всегда уходит в СВОЮ.
def annotate(src_path, dst_name, marks, caption, color=TEAL):
    """`marks` — (номер, x, y) в координатах ИСХОДНОГО снимка."""
    im = Image.open(src_path).convert("RGB")
    w, h = im.size
    band = 150
    out = Image.new("RGB", (w, h + band), W)
    out.paste(im, (0, 0))
    d = ImageDraw.Draw(out)
    r = 34
    for num, x, y in marks:
        d.ellipse([x - r, y - r, x + r, y + r], fill=color, outline=W, width=5)
        f = ImageFont.truetype(FB, 40)
        tw = d.textlength(str(num), font=f)
        d.text((x - tw / 2, y - 26), str(num), font=f, fill=W)
    d.rectangle([0, h, w, h + band], fill=SURF)
    f = ImageFont.truetype(F, 34)
    y = h + 26
    for line in caption:
        d.text((40, y), line, font=f, fill=INK)
        y += 46
    OUT.mkdir(exist_ok=True)
    out.save(OUT / dst_name)
    print(f"{dst_name}: {out.size[0]}×{out.size[1]}")


def main():
    # Те же метки и тот же исходный кадр, что у RU `obzor-k1.png`
    # (sem-07/rendered/annotate_shots.py, вызов `obzor-k1.png`) — переведена
    # только подпись снизу.
    annotate(
        SEM07_FIGURES / "n8n-holst-stage1.png",
        "shov-s7-obzor-klassifikatsii-en.png",
        [(1, 140, 48), (2, 620, 48), (3, 565, 600), (4, 1110, 48),
         (5, 1580, 48), (6, 2065, 48)],
        ["1 form — the process's entry point   ·   2 extraction — pulls values out of the text   ·   3 model — the second node of the step",
         "4 lookup check against the reference list   ·   5 write the row   ·   6 result screen — prints the whole trail"],
    )


if __name__ == "__main__":
    main()
