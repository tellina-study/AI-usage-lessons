#!/usr/bin/env python3
"""Кроп настоящих скринов живого стенда для Кейса 1 Семинара 11 (issue #345) —
workflow `CfRWQAELoIAbDPRm` («С11 · Кейс 1 — HyDE перед поиском (демо-экран)»,
`stend/sborka_case1_hyde.py`). Та же техника, что `sem-10/rendered/
compose_case1_n8n_shots.py`: это НЕ пересъёмка и не стилизация — дообрезка уже
снятых пикселей живого стенда (`stend/n8n_shots_case1.py`,
`stend/n8n-screenshots-raw/`), ImageMagick в этой среде недоступен, кроп через
Pillow, один в один с эффектом `convert -crop`.

Источники (не трогаются, остаются документацией прогона):
  stend/n8n-screenshots-raw/case1-hyde-canvas.png         3800×544
  stend/n8n-screenshots-raw/case1-hyde-vector-panel.png   1286×1204
  stend/n8n-screenshots-raw/case1-hyde-gen-panel.png       846×1846

Границы кропа найдены тем же способом (профиль нечисто-белых строк/столбцов
самого кадра, проверено просмотром):
  - холст: справа убран висящий «+»-коннектор после узла Result screen
    (виден на x≈3700-3790) — кадр обрезан до x=3680, семь узлов цепочки
    («Вопрос + корпус с векторами» → «Сочинить гипотетический ответ
    (gpt-4o-mini)» → «Разбор HyDE-документа» → «Embed HyDE-документ
    (text-embedding-3-small)» → «Simple Vector Store (cosine top-1 по HyDE)»
    → «Answer (RAG) по найденному куску (gpt-4o-mini)» → «Result screen»)
    не задеты.
  - панель Simple Vector Store: сверху убраны вкладки Parameters/Settings +
    поля Mode/Language (служебная часть интерфейса) — кроп начинается на
    y=385, прямо над заголовком «JavaScript»; снизу — подсказка тулкита
    «Type $ for a list...» убрана, кроп заканчивается на y=1040, сразу под
    тринадцатой (последней) строкой кода.
  - панель генерации HyDE-документа (HTTP Request): поля Method/URL/
    Authentication/Credential Type/Send Query Params/Send Headers/Body
    Content Type/Specify Body НЕ взяты в кадр — тот же узел HTTP Request к
    тому же OpenRouter credential уже показан и назван текстом на панели
    Simple Vector Store выше; взят единственный содержательный кусок внизу
    формы, где видно имя модели (`openai/gpt-4o-mini`) и начало промта
    (y=1540…1846, 846×306 — тот же порядок пропорции, что у аналогичных
    крупов Семинара 10, не уходит в книжную ориентацию).

Запуск: `python3 compose_case1_hyde_shots.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image

RAW = Path(__file__).resolve().parents[1] / "stend" / "n8n-screenshots-raw"
OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

CROPS = (
    ("case1-hyde-canvas.png", (0, 0, 3680, 544), "case1-hyde-n8n-canvas-real.png"),
    ("case1-hyde-vector-panel.png", (0, 385, 1286, 1040), "case1-hyde-n8n-vector-panel-real.png"),
    ("case1-hyde-gen-panel.png", (0, 1540, 846, 1846), "case1-hyde-n8n-gen-panel-real.png"),
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
