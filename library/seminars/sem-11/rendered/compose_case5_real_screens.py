#!/usr/bin/env python3
"""Кейс 5 (CRAG) Семинара 11 — сборка фигур слайда из НАСТОЯЩИХ скриншотов живого n8n,
не из программной схемы (та же правка, что `sem-10/rendered/compose_case4_real_screens.py`
сделал для своего кейса, и тот же приём, предписанный заданием этой сессии).

Источник — `stend/n8n-screenshots-raw/` (`stend/n8n_shots_case5.py`, снято на живом
`n8n.lessons.tellian.io`, workflow `GQESX1lq9wlQPxpL`, webhook `s11-case5-crag`).

Инструмент — Pillow (`which convert` в этой среде пусто, как и в предыдущих кейсах) —
кроп и только кроп, без перерисовки единого пикселя исходного скриншота.

Выход — ТРИ файла в `rendered/figures/`:

  - `case5-n8n-canvas-real.png` — холст целиком (путь: Вопрос+источники А/Б → Поиск
    top-1 (keyword) → LLM Relevance Grader (gpt-4o-mini) → Разбор вердикта → два IF-узла
    → три конечных узла). Обрезан справа до x=3660 из 3800 — убраны висящие коннекторы
    «+» после трёх узлов `Result screen` (тот же служебный значок, что уже убирался у
    холста Кейса 4 Семинара 10), путь узлов кадр не задевает.

  - `case5-n8n-grader-panel-real.png` — нижняя часть панели параметров узла
    `LLM Relevance Grader (gpt-4o-mini)`: `Body Content Type: JSON` → `Specify Body:
    Using JSON` → JSON-тело, где видно `model: 'openai/gpt-4o-mini'`, `temperature: 0`
    и начало системного промпта грейдера (С5 — модель и её настройки названы прямо на
    кадре). Верхняя часть панели (Method/URL/Authentication/Credential Type/OpenRouter
    account) не взята — тот же тип узла, тот же credential, что уже показан текстом на
    панелях предыдущих занятий; повторный разбор добавил бы не новое, а то же самое.

  - `case5-n8n-if-correct-panel-real.png` — панель условия IF-узла `Вердикт = CORRECT?`:
    `{{ $json.grader_verdict }}` is equal to `CORRECT` — настоящее условие ветки, не
    пересказ. Обрезан низ (`Options`/`No properties`/`Add option`) — пустой хвост формы.

Запуск: `python3 compose_case5_real_screens.py` (из `rendered/`).
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)


def canvas():
    src = RAW / "case5-canvas.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 0, 3660, im.height))
    cropped.save(OUT / "case5-n8n-canvas-real.png")
    print("  case5-canvas.png", before, "-> case5-n8n-canvas-real.png", cropped.size)


def grader_panel():
    src = RAW / "case5-grader-panel.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 1280, 846, 1846))
    cropped.save(OUT / "case5-n8n-grader-panel-real.png")
    print("  case5-grader-panel.png", before,
          "-> case5-n8n-grader-panel-real.png", cropped.size)


def if_correct_panel():
    src = RAW / "case5-if-correct-panel.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 0, 1286, 420))
    cropped.save(OUT / "case5-n8n-if-correct-panel-real.png")
    print("  case5-if-correct-panel.png", before,
          "-> case5-n8n-if-correct-panel-real.png", cropped.size)


if __name__ == "__main__":
    canvas()
    grader_panel()
    if_correct_panel()
