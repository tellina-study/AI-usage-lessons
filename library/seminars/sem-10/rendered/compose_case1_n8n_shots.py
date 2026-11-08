#!/usr/bin/env python3
"""Кроп настоящих скринов живого стенда для Кейса 1 (issue #311) — заменяет
программную схему `case1-n8n-vector-scheme.png` (`make_figures_sem10.py::
case1_scheme`) тремя кадрами слоя 2: холст и два развёрнутых поля настройки
узлов. Та же техника, что `sem-09/rendered/crop_k3_panel_tight.py`: это НЕ
пересъёмка и не стилизация (канон §3 проектирования — системные id/служебные
детали на экран не выносятся, но настоящий скрин заменять рисованной
карточкой нельзя), а дообрезка уже снятых пикселей живого стенда
(`stend/n8n_shots.py`, `stend/n8n-screenshots-raw/`) — ImageMagick в этом
окружении недоступен (`which convert` пусто), поэтому кроп сделан тем же
инструментом, что и сам тулкит схем (`Pillow`/`PIL`), один в один с эффектом
`convert -crop`.

Источники (не трогаются, остаются как документация прогона):
  stend/n8n-screenshots-raw/case1-canvas.png            2552×768
  stend/n8n-screenshots-raw/case1-vector-store-panel.png 1286×1090
  stend/n8n-screenshots-raw/case1-answer-panel.png       846×1122

Границы кропа найдены тем же способом, что в `crop_k3_panel_tight.py`:
профиль нечисто-белых строк/столбцов самого кадра, без выдумывания числа:
  - холст: справа убран висящий «+»-коннектор ПОСЛЕ узла Result screen
    (контент кончается ~2460px, оставлен запас до 2500px); сверху/снизу —
    без изменений, кадр и так тесно обрезан вокруг главного пути узлов.
  - панель Simple Vector Store: сверху убраны вкладки Parameters/Settings +
    поля Mode/Language (служебная часть интерфейса, не код узла); снизу —
    подсказка Pillow-тулкита «Type $ for a list...». Остаётся заголовок
    «JavaScript» + сам код.
  - панель Answer (RAG): сверху убран блок «Save time with an example» и
    поле «Source for Prompt»; снизу — переключатели Require Specific Output
    Format / Enable Fallback Model / Chat Messages. Остаётся заголовок
    «Prompt (User Message)» + само тело промта.

Запуск: `python3 compose_case1_n8n_shots.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image

RAW = Path(__file__).resolve().parents[1] / "stend" / "n8n-screenshots-raw"
OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

CROPS = (
    ("case1-canvas.png", (0, 0, 2500, 700), "case1-n8n-canvas-real.png"),
    ("case1-vector-store-panel.png", (0, 380, 1286, 935), "case1-n8n-vector-panel-real.png"),
    ("case1-answer-panel.png", (0, 298, 846, 632), "case1-n8n-answer-panel-real.png"),
)


def main():
    for src_name, box, out_name in CROPS:
        src = RAW / src_name
        im = Image.open(src)
        before = im.size
        cropped = im.crop(box)
        cropped.save(OUT / out_name)
        print(f"  {src_name}  {before} -> {out_name}  {cropped.size}")


if __name__ == "__main__":
    main()
