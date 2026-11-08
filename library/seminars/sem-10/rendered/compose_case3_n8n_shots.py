#!/usr/bin/env python3
"""Кроп настоящих скринов живого стенда для Кейса 3 (issue #311) — заменяет
программную схему `case3-n8n-hybrid-rerank-scheme.png` (`make_figures_sem10.py::
case3_scheme`) тремя кадрами слоя 2, той же техникой, что
`compose_case1_n8n_shots.py` уже применил для Кейса 1 (три отдельных кадра —
холст + панель + панель — не склейка бок о бок, как у Кейса 2/4): это НЕ
пересъёмка и не стилизация (канон §3 проектирования — системные id/служебные
детали на экран не выносятся, но настоящий скрин заменять рисованной
карточкой нельзя), а дообрезка уже снятых пикселей живого стенда
(`stend/n8n_shots.py`, `stend/n8n-screenshots-raw/`) — ImageMagick в этом
окружении недоступен (`which convert` пусто), поэтому кроп сделан тем же
инструментом, что и сам тулкит схем (`Pillow`/`PIL`), один в один с эффектом
`convert -crop`.

Источники (не трогаются, остаются как документация прогона):
  stend/n8n-screenshots-raw/case3-canvas.png            3912×522
  stend/n8n-screenshots-raw/case3-rrf-panel.png         1286×1204
  stend/n8n-screenshots-raw/case3-reranker-panel.png     846×1846

Границы кропа найдены тем же способом, что в `compose_case1_n8n_shots.py`:
профиль нечисто-белых строк/столбцов самого кадра, без выдумывания числа:

  - холст (`case3-canvas.png` → `case3-n8n-canvas-real.png`): справа убран
    висящий «+»-коннектор ПОСЛЕ узла Result screen (тот же служебный
    значок интерфейса, что Кейс 1/Кейс 4 убрали по тому же месту) — кадр
    обрезан до x=3860 из 3912, сама цепочка из восьми узлов («Вопрос +
    корпус с эмбеддингами» → «Keyword overlap» → «Embed query (OpenRouter)»
    → «Cosine ranking (vector)» → «RRF fusion (hybrid)» → «LLM-реранкер
    (gpt-4o-mini)» → «Разбор ответа реранкера + итог» → «Result screen»)
    кадр не задевает.

  - панель слияния (`case3-rrf-panel.png` → `case3-n8n-rrf-panel-real.png`):
    сверху убраны вкладки Parameters/Settings и поля Mode/Language
    (служебная часть интерфейса, не код узла) — кроп начинается на y=390,
    прямо над заголовком «JavaScript»; снизу — подсказка «Type $ for a
    list...» (кремовый фон начинается на y=1084, профиль найден тем же
    способом, что у Кейса 1) — кроп заканчивается на y=1070, с запасом
    перед подсказкой. Остаётся заголовок «JavaScript» + все 13 строк кода
    RRF (`function rrf(rankA, rankB, k=60) {...}`) целиком, без обрезки
    последней строки.

  - панель реранкера (`case3-reranker-panel.png` →
    `case3-n8n-reranker-panel-real.png`): ПОЛЕ «Method»/«URL»/
    «Authentication»/«Credential Type» (y=0…1230) НЕ взято в кадр — тот же
    узел HTTP Request к тому же OpenRouter credential уже один раз показан
    и назван текстом на панели Кейса 1 (`n11`/`n11a`/`n11b`), повторный
    разбор добавил бы не новое, а то же самое (та же логика отбора, что
    `compose_case4_real_screens.py::embed_panel` уже применил к Кейсу 4).
    Взят единственный содержательный кусок внизу формы — заголовок «Specify
    Body: Using JSON» → «JSON» → тело запроса, где ВИДНО ИМЯ МОДЕЛИ
    (`openai/gpt-4o-mini`) и начало системного промта реранкера НА РУССКОМ
    («Ты — переранжировщик результатов поиска. Тебе дан вопрос и ' +
    $json.top_ids.length + ' кандидатов-отрывков...») — y=1398…1816 (846×418,
    пропорция 2,02 — того же порядка, что кроп панели Кейса 1/Кейс 4, не
    уходит в книжную ориентацию). Нижняя граница (y=1816) — перед тёмной
    служебной полосой редактора в самом низу кадра (y=1816…1846, профиль
    846 нечисто-белых пикселей на строку — сплошная полоса, не содержание).

Запуск: `python3 compose_case3_n8n_shots.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image

RAW = Path(__file__).resolve().parents[1] / "stend" / "n8n-screenshots-raw"
OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

CROPS = (
    ("case3-canvas.png", (0, 0, 3860, 522), "case3-n8n-canvas-real.png"),
    ("case3-rrf-panel.png", (0, 390, 1286, 1070), "case3-n8n-rrf-panel-real.png"),
    ("case3-reranker-panel.png", (0, 1398, 846, 1816), "case3-n8n-reranker-panel-real.png"),
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
