#!/usr/bin/env python3
"""Кейс 4 — сборка фигур слайда из НАСТОЯЩИХ скриншотов живого n8n, не из
программной схемы (issue #311, та же правка, что `compose_case1_n8n_shots.py`
и `compose_case2_real_screens.py` уже сделали для своих кейсов). Источник —
`stend/n8n-screenshots-raw/` (`stend/README.md`, раздел «Экран канваса n8n —
ИСПРАВЛЕНО 2026-11-01»): реальные снимки `case4-canvas.png` и
`case4-embed-image-panel.png`, сняты `stend/n8n_shots.py` на живом
`n8n.lessons.tellian.io`.

Инструмент — Pillow, не ImageMagick (`which convert` в этой рабочей среде
пусто, как и у двух предыдущих кейсов) — кроп и только кроп, без перерисовки
единого пикселя исходного скриншота.

Прежняя программная схема `case4-n8n-mm-scheme.png`
(`make_figures_sem10.py::case4_scheme`) НЕ удалена — остаётся на диске как
запись устройства прежнего (ошибочного, по признанию `stend/README.md`)
решения, но слайды на неё больше не ссылаются.

Выход — ДВА файла в `rendered/figures/`, новыми именами:

  - `case4-n8n-canvas-real.png` — холст целиком, с кропом справа: исходный
    кадр (1560×544) снят зумом «по размеру» и лишнего по краям почти нет,
    кроме висящего коннектора «+» ПОСЛЕ узла `Result screen` (тот же
    служебный «добавить следующий узел» значок интерфейса, который
    `compose_case1_n8n_shots.py` убрал по тому же месту холста Кейса 1) —
    обрезано до x=1500 из 1560, сам путь трёх узлов (`Скан бланка (data
    URL)` → `Embed image (amazon/titan-embed-image-v1)` → `Result screen`)
    кадр не задевает.

  - `case4-n8n-embed-panel-real.png` — узкий вертикальный кроп панели
    настройки узла `Embed image` (846×1846 целиком — обычная одноколоночная
    форма n8n, список полей сверху вниз). Показывать всю форму целиком как
    один кадр нельзя: 846×1846 в книжной ориентации почти не ложится в
    альбомный слайд (ширина/высота 0,46), фигура встаёт узкой колонкой с
    пустым полем по бокам (`deck_kit.figure`, предупреждение «СХЕМА ЗАЖАТА»).
    Поэтому выбран ОДИН содержательный кусок внизу формы — `Body Content
    Type: JSON` → `Specify Body: Using JSON` → `JSON: {{ $json.body }}`
    (y=1253…1621 из 1846, пропорция кадра 846×368 = 2,3, та же пропорция,
    которую держит кроп панели `Simple Vector Store` Кейса 1). Выбор этого
    куска, а не верхнего (`Method`/`URL`/`Authentication`/`Credential
    Type`/`OpenRouter account`): URL-эндпоинт и тип credential
    («OpenRouter») уже один раз показаны и названы текстом на панели
    Кейса 1 (`n11a`) — повторный разбор здесь добавил бы не новое, а то же
    самое (та же логика отбора, что `uzly_nastroyka()` Кейса 4 Семинара 8:
    «подтверждение тождества узла, не вторая лекция про то же самое»). Тело
    запроса — `{{ $json.body }}`, выражение, не литерал: сама картинка и имя
    модели подставляются ВЫШЕ по цепочке (в `Set`-узле, который готовит
    `data URL`), и это единственное место на панели, которое показывает
    именно это, а не повтор уже известного.

Запуск: `python3 compose_case4_real_screens.py` (из `rendered/`).
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)


def canvas():
    src = RAW / "case4-canvas.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 0, 1500, im.height))
    cropped.save(OUT / "case4-n8n-canvas-real.png")
    print("  case4-canvas.png", before, "-> case4-n8n-canvas-real.png", cropped.size)


def embed_panel():
    src = RAW / "case4-embed-image-panel.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 1253, 846, 1253 + 368))
    cropped.save(OUT / "case4-n8n-embed-panel-real.png")
    print("  case4-embed-image-panel.png", before,
          "-> case4-n8n-embed-panel-real.png", cropped.size)


if __name__ == "__main__":
    canvas()
    embed_panel()
