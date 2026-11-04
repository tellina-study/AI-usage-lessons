#!/usr/bin/env python3
"""Кейс 2 — сборка фигур слайда из НАСТОЯЩИХ скриншотов живого n8n, не из
программной схемы. Источник — `stend/n8n-screenshots-raw/` (`stend/README.md`,
раздел «Экран канваса n8n — ИСПРАВЛЕНО 2026-11-01»): реальные снимки
`case2-canvas.png`, `case2-fixed-chunk-panel.png`, `case2-structural-chunk-panel.png`,
сняты `stend/n8n_shots.py` на `n8n.lessons.tellian.io`.

Инструмент — Pillow, не ImageMagick: в этой рабочей среде `convert`/`montage`
не установлены (`which convert` → ничего), а требуемые операции (кроп,
склейка «бок о бок») Pillow делает без внешнего бинаря. Результат тот же —
обрезка лишнего и компоновка, без перерисовки пикселей исходного скриншота.

Выход — два файла в `rendered/figures/`, НОВЫМИ именами (не переписывают
прежнюю программную схему `case2-n8n-splitter-scheme.png`, которая остаётся
на диске как запись устройства прежнего решения, но слайдами больше не
используется — см. `stend/README.md`):

  - `case2-n8n-canvas-real.png`   — холст целиком (копия, без обрезки:
    снято уже кадрировано зумом «по размеру», лишнего по краям нет)
  - `case2-n8n-code-panels-real.png` — два code-узла («Нарезка фиксированным
    размером» и «Нарезка по границам предложений») БОК О БОК, каждый обрезан
    по нижней оранжевой подсказке интерфейса («Type $ for a list…», она же
    UI-подсказка n8n, не содержание узла) — найдено по смене цвета фона
    (белый → `#FDF9F1` на y≈1258 в оригинале 1382px), обрезка на y=965 с
    запасом в 15px до начала 13-й строки кода, чтобы строка не резалась.

Запуск: `python3 compose_case2_real_screens.py` (из `rendered/`).
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

CROP_H = 965   # высота кропа каждой панели — см. докстринг модуля
GAP = 28       # белый зазор между панелями


def canvas():
    src = RAW / "case2-canvas.png"
    im = Image.open(src).convert("RGB")
    im.save(OUT / "case2-n8n-canvas-real.png")
    print("  case2-n8n-canvas-real.png", im.size)


def code_panels():
    fixed = Image.open(RAW / "case2-fixed-chunk-panel.png").convert("RGB").crop(
        (0, 0, 1286, CROP_H))
    struct = Image.open(RAW / "case2-structural-chunk-panel.png").convert("RGB").crop(
        (0, 0, 1286, CROP_H))
    w = fixed.width + GAP + struct.width
    h = CROP_H
    im = Image.new("RGB", (w, h), (255, 255, 255))
    im.paste(fixed, (0, 0))
    im.paste(struct, (fixed.width + GAP, 0))
    im.save(OUT / "case2-n8n-code-panels-real.png")
    print("  case2-n8n-code-panels-real.png", im.size)


if __name__ == "__main__":
    canvas()
    code_panels()
