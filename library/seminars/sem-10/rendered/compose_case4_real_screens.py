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

Выход — ПЯТЬ файлов в `rendered/figures/`. Два первых режут ПРЕЖНИЙ,
titan-холст (ниже), три последних — холст переписанного 2026-11-12
сценария на рабочей модели: `case4-n8n-canvas-working.png`,
`case4-n8n-embed-working-panel.png`, `case4-n8n-cosine-panel.png` (их
разбор — в докстрингах `canvas_working()` / `embed_working_panel()` /
`cosine_panel()`). Прежние два НЕ переименованы и НЕ перерезаны: кейс
рассказывает и не удавшуюся попытку тоже.

Прежние два:

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


# --- Переписанный сценарий, рабочая модель (2026-11-12) ------------------------------
# Кейс переписан вокруг РАБОЧЕЙ модели `nvidia/nemotron-3.5-embed-1b:free`, и сценарий на
# стенде переписан вместе с ним (`stend/sborka.py::case4_multimodal_workflow`): вместо
# одного узла-вызова на холсте стоит вся механика — запрос-скан и индекс → сборка тела с
# именем модели → один вызов `/embeddings` → косинусное расстояние до индекса → ближайший.
# Функции НИЖЕ режут кадры этого, нового холста; функции ВЫШЕ (`canvas`, `embed_panel`)
# оставлены как есть и режут прежний, titan-холст — он кейсу ещё нужен как запись не
# удавшейся попытки, и его сырые кадры не перезаписывались (проверено по md5).
# Живой прогон этого сценария — execution 7839, протокол
# `stend/raw/case4_mm_working_execution.json`.


def canvas_working():
    """Холст переписанного сценария целиком.

    Источник: `stend/n8n-screenshots-raw/case4-canvas-working.png` (2584×544), снят
    `stend/n8n_shots.py --only case4` на живом `n8n.lessons.tellian.io`.
    Кроп: `(0, 0, 2500, 544)` → 2500×544.

    Почему именно этот кусок. Срезаны последние 84 пикселя справа — висящий значок «+»
    ПОСЛЕ узла `Result screen` (служебная кнопка интерфейса «добавить следующий узел», не
    часть сценария); ровно по тому же месту и по той же причине режут холст Кейса 1
    (`compose_case1_n8n_shots.py`) и прежний холст этого кейса (`canvas()` выше). Пять
    узлов пути кадр не задевает.

    Что видно на кадре: `Запрос-скан + индекс` → `Тело запроса: nemotron-3.5-embed-1b`
    → `Эмбеддинги сканов` (с подписью `POST: https://openrouter.ai/…`) →
    `Косинусное расстояние до индекса` → `Result screen`. Имя рабочей модели стоит в
    подписи узла ПОЛНОСТЬЮ, не срезанным многоточием — подписи узлов для этого
    укорочены (холст n8n даёт метке две строки примерно по 22 знака и режет длинный
    токен, а не переносит; см. комментарий в `sborka.py`).
    """
    src = RAW / "case4-canvas-working.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 0, 2500, im.height))
    cropped.save(OUT / "case4-n8n-canvas-working.png")
    print("  case4-canvas-working.png", before,
          "-> case4-n8n-canvas-working.png", cropped.size)


def embed_working_panel():
    """Панель узла, который собирает тело запроса — там, где названа модель.

    Источник: `stend/n8n-screenshots-raw/case4-embed-working-panel.png` (1286×1320),
    панель узла `Тело запроса: nemotron-3.5-embed-1b` в развёрнутом виде редактора.
    Кроп: `(0, 424, 1286, 1170)` → 1286×746 (пропорция 1,72 — альбомная, ложится в слайд;
    та же причина, по которой `embed_panel()` выше режет узкую колонку, а не берёт форму
    целиком).

    Почему именно этот кусок: взято поле `JavaScript` целиком, от верхней рамки редактора
    до последней строки кода (`}}];`), и отрезаны шапка формы (`Mode` / `Language` —
    служебные поля n8n, одинаковые у любого Code-узла и ничего про кейс не говорящие) и
    подсказка редактора внизу («Type $ for a list of special vars…» — подсказка
    интерфейса, не содержание узла).

    Что видно на кадре: полный идентификатор рабочей модели литералом —
    `const MODEL = 'nvidia/nemotron-3.5-embed-1b:free'` — вместе с комментарием, почему
    она рабочая и чем была предыдущая; и сборка тела запроса: `input` — это вектор
    запроса ПЛЮС векторы индекса одним вызовом (`[payload.query.image,
    ...payload.index.map(s => s.image)]`), то есть обе стороны сравнения считаются одной
    моделью за один раз. Подписи сканов (`labels`) идут мимо модели — в тело запроса
    уходят только пиксели.
    """
    src = RAW / "case4-embed-working-panel.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 424, 1286, 1170))
    cropped.save(OUT / "case4-n8n-embed-working-panel.png")
    print("  case4-embed-working-panel.png", before,
          "-> case4-n8n-embed-working-panel.png", cropped.size)


def cosine_panel():
    """Панель узла сравнения — там, где считается косинус. Это то, что кейс обязан показать.

    Источник: `stend/n8n-screenshots-raw/case4-cosine-panel.png` (1286×1382), панель узла
    `Косинусное расстояние до индекса` в развёрнутом виде редактора.
    Кроп: `(0, 424, 1286, 1215)` → 1286×791 (пропорция 1,63).

    Почему именно этот кусок: как и у панели выше, отрезаны шапка формы и подсказка
    редактора. Нижняя граница — 1215, а не рамка редактора (≈1231): на строке 16 поле
    кода обрывается посреди глифов (редактор n8n показывает ровно столько строк, сколько
    влезло в развёрнутую высоту), и обрезанная наполовину строка на слайде читается как
    дефект кадра. Кадр заканчивается последней ЦЕЛОЙ строкой — 15-й, на которой
    заканчивается сам расчёт: каждому проиндексированному скану сопоставлены `similarity`
    и `distance`.

    Что видно на кадре: функция `cos(a, b)` целиком (скалярное произведение, делённое на
    произведение длин) с комментарием «cos = 1 → векторы совпали по направлению;
    расстояние = 1 − cos»; `qvec = vectors[0]` — вектор запроса; `indexVectors =
    vectors.slice(1)` — векторы проиндексированных сканов; и строка, где косинус
    считается вектор-к-вектору. Сортировка, ближайший, отрыв от второго и текст экрана
    результата остаются ниже кадра — они следствие, а не механика.
    """
    src = RAW / "case4-cosine-panel.png"
    im = Image.open(src).convert("RGB")
    before = im.size
    cropped = im.crop((0, 424, 1286, 1215))
    cropped.save(OUT / "case4-n8n-cosine-panel.png")
    print("  case4-cosine-panel.png", before, "-> case4-n8n-cosine-panel.png", cropped.size)


if __name__ == "__main__":
    canvas()
    embed_panel()
    canvas_working()
    embed_working_panel()
    cosine_panel()
