#!/usr/bin/env python3
"""Программные схемы «слой 2» для всех четырёх кейсов Семинара 10.

Живой скрин канваса n8n в этой рабочей среде недостижим (задача прямо просила
не тратить время на повторную попытку — `notes/mcp-limitations.md` [#233-8]),
поэтому здесь — программная схема в духе n8n (тот же инструмент, что
Семинар 8/10-Фаза-2: `n8n_canvas_kit.py`, лежит рядом в этой же папке),
реальными именами узлов и реальными значениями параметров со стенда Фазы 2
(`stend/README.md`, `stend/raw/*.json`). Каждый слайд, который использует эти
схемы, обязан нести `backup:` в frontmatter, что это не скриншот (канон §8.4,
`proektirovanie-keysa-i-voprosa.md` §3).

Кейс 1 и Кейс 4 повторяют те же числа, что уже нарисовал стенд Фазы 2
(`stend/make_figures_case1_case4.py`) — перерисованы здесь заново, чтобы все
четыре схемы деки жили в одном месте (`rendered/`, канон
`tools/seminar-build/README.md`: «Своё у занятия — rendered/make_figures_*.py»)
и одним инструментом. Кейс 2 и Кейс 3 — НОВЫЕ схемы, такого слоя не было до
Фазы 4.

    python3 make_figures_sem10.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, N8N_DISCLAIMER  # noqa: E402

W_PX, H_PX = 1600, 680


# ── Схема сцены Кейса 1 — «case1-shema-postanovka.png» (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2) ───────────────────
# Сплошное — поток, который уже работает с прошлого занятия (С9): вопрос
# приходит формой, весь текст справочника уходит в промт целиком, модель
# отвечает, видя базу полностью. Пунктирная стрелка и золотой контур —
# то, что СТРОИТ этот кейс: отдельное хранилище и поиск нужного куска,
# которые встанут ВМЕСТО узла «весь справочник целиком».
SCENE_W_PX = 1700


def case1_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 420), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в потоке ответа встанет поиск нужного куска", sz=28)
    d.text((40, 56),
            "форма и вызов модели уже работают — вопрос в том, что займёт место узла "
            "«весь справочник целиком», когда база вырастет",
            font=f(19), fill=LIGHT)

    y1, h1 = 120, 120
    nodes = [
        ("Вопрос обратившегося", "форма, как на прошлом занятии"),
        ("Весь справочник целиком", "текст базы — в промт целиком"),
        ("Модель отвечает", "gpt-4o-mini, вся база в промте"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (SCENE_W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=20,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 290, 110
    goal_w = node_w + 60
    goal_x = xs[1] + node_w / 2 - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Строим сегодня:", "хранилище + поиск куска"],
        W, tc=DEEP, sz=20, outline=GOLD, where="сцена-цель")
    arrow(d, goal_x + goal_w / 2, y2, xs[1] + node_w / 2, y1 + h1,
          col=GOLD, wd=4, dash=True)

    save(im, "case1-shema-postanovka.png")


# ── Схема сцены Кейса 2 — «case2-shema-postanovka.png» (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2) ───────────────────
# Сплошной контур — узлы, уже работающие с прошлого занятия (эмбеддинг
# и хранилище, решённые Кейсом 1). Подпись узла эмбеддинга — «в Кейсе 1 —
# по документу»: там эмбеддинг считался ПО ДОКУМЕНТУ ЦЕЛИКОМ
# (`stend/measure/embed_corpus.py` эмбеддит `d["text"]`, нарезки там нет),
# и прежняя подпись «эмбеддинг куска уже работает, Кейс 1» обещала
# механизм, которого Кейс 1 не строил (issue #311).
# Пунктирный золотой контур — узел, который СТРОИТ этот кейс: разбиение
# документа на куски, встающее ПЕРЕД эмбеддингом.
# Имён инструмента внутри узлов нет умышленно — слой 1 - устройство решения,
# не экран n8n (экран — отдельно, n28/n29).
def case2_shema_postanovka():
    im = Image.new("RGB", (1600, 360), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в пути документа встаёт разбиение на куски", sz=30)
    d.text((40, 58), "эмбеддинг и хранилище уже работают с прошлого занятия — "
            "вопрос в том, что происходит до них", font=f(20), fill=LIGHT)

    y, h = 140, 170
    gap = 40
    n = 4
    node_w = (1600 - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    nodes = (
        ("Документ", "база знаний, Кейс 1", False),
        ("Разбиение на куски", "строим в этом кейсе", True),
        ("Эмбеддинг куска", "в Кейсе 1 — по документу", False),
        ("Хранилище", "уже работает, Кейс 1", False),
    )
    cy = y + h / 2
    for i, (title, sub, is_new) in enumerate(nodes):
        x = xs[i]
        if is_new:
            dashbox(d, x, y, node_w, h, GOLD, dash=16, gap=11, width=4, r=14)
        else:
            d.rounded_rectangle([x, y, x + node_w, y + h], radius=14,
                                 outline=TEAL, width=4)
        clabel(d, x + node_w / 2, y + 46, title, 24, DEEP, b=True,
               where=f"узел {i + 1} · заголовок", limit=node_w - 30)
        clabel(d, x + node_w / 2, y + 92, sub, 18, MUTE,
               where=f"узел {i + 1} · подпись", limit=node_w - 30)
        if i:
            arrow(d, xs[i - 1] + node_w, cy, x, cy, col=TEAL, wd=4)
    save(im, "case2-shema-postanovka.png")


def case1_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 1 · хранение базы знаний", sz=28)

    y = 170
    node_n8n(d, 40, y, 300, 160, "Вопрос + корпус с векторами", "formTrigger",
              kind="trigger")
    node_n8n(d, 390, y, 300, 160, "Embed query",
              ["httpRequest → OpenRouter /v1/embeddings", "model: text-embedding-3-small"],
              kind="external")
    node_n8n(d, 740, y, 320, 160, "Simple Vector Store (поиск)",
              ["cosine(qvec, doc.embedding)", "top-1 из N документов, score=0,590"], kind="code")
    node_n8n(d, 1110, y, 300, 160, "Answer (RAG)",
              ["httpRequest → chat/completions", "model: gpt-4o-mini"], kind="model")
    for x1, x2 in [(340, 390), (690, 740), (1060, 1110)]:
        arrow_n8n(d, x1, x2, y + 80)

    callout(d, 40, y + 220, 1370, 180,
            "Чего нет на этом холсте — узла «эмбеддинг через OpenRouter» в каталоге n8n 2.42.7",
            ["и шаг эмбеддинга, и финальный вызов модели собраны обычным узлом HTTP Request",
             "с предустановленным типом учётных данных (predefinedCredentialType: openRouterApi)",
             "вопрос «При каком давлении удалось получить кристаллы гелия?» → найден кусок",
             "needle-1 (score 0,590, «…применив давление выше 35 атм…») → ответ верный"],
            tone="ok")
    d.text((40, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case1-n8n-vector-scheme.png")


def case2_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 2 · разбиение документа на части — Text Splitter перед эмбеддингом", sz=28)

    y = 170
    node_n8n(d, 40, y, 300, 160, "Документ базы знаний",
              "Set · текст регламента/FAQ", kind="trigger")
    node_n8n(d, 390, y, 420, 160, "Text Splitter",
              ["v1: Character Text Splitter, chunkSize=180, separator=\"\" (посимвольно)",
               "v2: Recursive Splitter, separator=\"по предложению\", chunkSize=180"],
              kind="code")
    node_n8n(d, 860, y, 300, 160, "Embed chunk",
              ["httpRequest → /v1/embeddings", "model: text-embedding-3-small"], kind="external")
    node_n8n(d, 1210, y, 300, 160, "Simple Vector Store (запись)",
              "insert(chunk, embedding)", kind="code")
    for x1, x2 in [(340, 390), (810, 860), (1160, 1210)]:
        arrow_n8n(d, x1, x2, y + 80)

    callout(d, 40, y + 220, 1470, 200,
            "Разница версии 1 и версии 2 — один параметр узла, не новая цепочка",
            ["v1 (separator «посимвольно», chunk_size=180): доля разорванных ответов 12,5% (9 из 72)",
             "v2 (separator «по предложению», тот же chunk_size=180): доля разорванных ответов 1,4% (1 из 72)",
             "остальная цепочка (эмбеддинг, запись в хранилище) не меняется ни одним узлом",
             "60 документов SberQuAD (≥500 символов), 72 вопроса — stend/raw/case2-results.json"],
            tone="ok")
    d.text((40, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case2-n8n-splitter-scheme.png")


# ── Схема сцены Кейса 3 — «case3-shema-postanovka.png» (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2) ───────────────────
# Сплошное — то, что уже работает после Кейса 2: вопрос приходит формой,
# куски базы уже нарезаны по смыслу, модель отвечает по тому куску, который
# ей передали. Пунктирная стрелка и золотой контур — то, что СТРОИТ этот
# кейс: сам шаг поиска, который решает, какой из сотен кусков модель увидит.
def case3_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в потоке ответа встаёт поиск нужного куска", sz=30)
    d.text((40, 64),
            "вопрос и ответ уже работают, база уже нарезана по смыслу (Кейс 2) — "
            "вопрос в том, какой кусок из сотен увидит модель",
            font=f(21), fill=LIGHT)

    y1, h1 = 150, 150
    nodes = [
        ("Вопрос обратившегося", "форма, как и раньше"),
        ("База нарезана по смыслу", "готово с прошлого кейса"),
        ("Ответ по найденному куску", "модель видит только переданное"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (SCENE_W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=21,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    y2, h2 = 370, 150
    gap_cx = xs[1] + node_w + gap / 2   # граница между узлом 2 (база) и узлом 3 (ответ)
    goal_w = node_w + gap * 2 + 90
    goal_x = gap_cx - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Строим сегодня: найти самый нужный кусок из сотен",
         "до того, как положить его в промт"],
        W, tc=DEEP, sz=21, outline=GOLD, where="сцена-цель")
    arrow(d, gap_cx, y2, gap_cx, y1 + h1, col=GOLD, wd=4, dash=True)

    save(im, "case3-shema-postanovka.png")


def case3_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 3 · чем искать нужный кусок — гибрид + необязательный LLM-реранкер", sz=27)

    y = 150
    node_n8n(d, 40, y, 260, 150, "Вопрос", "formTrigger", kind="trigger")
    node_n8n(d, 350, y, 300, 150, "Simple Vector Store (поиск)",
              ["cosine(qvec, doc.embedding)", "top-10 по смыслу"], kind="code")
    node_n8n(d, 350, y + 200, 300, 150, "Keyword-фильтр",
              ["Code: пересечение токенов", "top-10 по словам"], kind="code")
    node_n8n(d, 700, y + 100, 300, 150, "Слияние (RRF, k=60)",
              "Code: Reciprocal Rank Fusion", kind="code")
    node_n8n(d, 1050, y + 100, 300, 150, "LLM-реранкер (необязательно)",
              ["httpRequest → chat/completions", "gpt-4o-mini, top-10 в промте"], kind="model")
    node_n8n(d, 1400, y + 100, 160, 150, "Answer", "top-1 → промт", kind="external")

    arrow_n8n(d, 300, 350, y + 75)
    arrow_n8n(d, 300, 350, y + 275)
    arrow_n8n(d, 650, 700, y + 175)
    arrow_n8n(d, 650, 700, y + 175)
    arrow_n8n(d, 1000, 1050, y + 175)
    arrow_n8n(d, 1350, 1400, y + 175)

    callout(d, 40, y + 320, 1520, 200,
            "Реранкер — дополнительный узел после слияния, тот же credential, новой инфраструктуры нет",
            ["recall@1: keyword 0,74 → vector 0,86 → hybrid(RRF) 0,84 → hybrid+реранкер 0,96",
             "у OpenRouter нет отдельного rerank-эндпоинта — это обычный chat-completions, которому",
             "передают top-10 кандидатов и просят вернуть порядок по релевантности вопросу",
             "цена шага реранка: ~$0,00033 на вопрос, +1,6–1,9с — больше, чем весь пайплайн Кейса 1"],
            tone="ok")
    d.text((40, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case3-n8n-hybrid-rerank-scheme.png")


# ── Схема «би-энкодер vs кросс-энкодер» — «case3-biencoder-vs-crossencoder.png»
# (n41a, правка владельца issue #311: «добавь схему и описание особенностей
# работы реранкера как он работает и почему точнее») ────────────────────────
# Левая колонка (LIGHT, основной синий) — обычный векторный поиск: запрос и
# документ кодируются ПО ОТДЕЛЬНОСТИ, их векторы встречаются только на самом
# последнем шаге, в сравнении готовых чисел. Правая колонка (TEAL, вторичный
# акцент палитры — семантически «альтернативный механизм») — реранкер
# (кросс-энкодер): запрос и документ сливаются в ОДИН вход на шаг РАНЬШЕ, чем
# у би-энкодера происходит сравнение, — поэтому колонка короче на один уровень
# параллельности. Эта асимметрия (где именно сходятся две ветки) и есть сама
# схема, не декоративная разница цветов.
BCE_W, BCE_H = 1200, 238


def case3_biencoder_vs_crossencoder():
    """Схема устройства реранкера: раздельное кодирование против совместного.

    ПРАВКА issue #311 (обобщение замечаний владельца на Кейс 3). Прежняя
    версия холста была 1700×720 с поясняющим блоком «Почему совместное чтение
    точнее» внутри рисунка, набранным 15 px. Замер: при таком соотношении
    сторон (2,36 : 1) схема на слайде упиралась в высоту и рисовалась на 7,97″
    из отведённых 12,23″, то есть 1700 px приходились на 7,97″ — 213 px на
    дюйм, и 15 px давали 5,1 pt. Пол кегля деки — 15,0 pt (`deck_kit.SCALE`,
    `type_scale: true` у Семинара 10). С проектора такой текст не читается.

    Арифметика, из которой выведен новый холст: кегль на слайде в пунктах =
    px · 72 · (ширина отрисовки в дюймах) / (ширина холста в px). Чтобы 21 px
    давали ≥15 pt при полной ширине 12,23″, холст обязан быть не шире
    ~1230 px; чтобы схема НЕ упёрлась в высоту (и потому рисовалась во всю
    ширину), её соотношение сторон обязано быть не выше, чем отведённая ей
    высота к 12,23″. Отсюда 1200×238: соотношение 5,04 : 1 даёт на слайде
    12,23″ × 2,43″ — ровно столько высоты кадру и остаётся после двух
    плашек, так что схема НЕ сжимается вовсе и идёт во всю ширину. 98 px
    на дюйм, и самый мелкий кегль схемы — 21 px — выходит 15,4 pt, над
    полом. Замерено по собранному .pptx, а не на глаз: прежняя версия
    ставила картинку шириной 7,97″, промежуточные 1200×300 — 10,09″ и 1200×250 — 11,87″,
    эта — 12,23″.

    Чем за это заплачено, явно: с холста сняты собственный заголовок схемы и
    подзаголовок (они повторяли заголовок самого кадра) и блок «Почему
    совместное чтение точнее» — его текст дословно жил и в блоке-цитате
    слайда, который верстается китом по полу кегля. То есть пояснение не
    потеряно, оно переехало туда, где читается. Правило — §8 требований к
    форме: если схема нарисована, текст о том же на том же кадре удваивает
    и съедает место.
    """
    im = Image.new("RGB", (BCE_W, BCE_H), W)
    d = ImageDraw.Draw(im)

    SZ, SZH = 21, 22                      # пол схемы: 21 px = 15,4 pt на слайде
    half = 570
    x0, x1 = 10, 620
    inner, igap = 275, 20

    clabel(d, x0 + half / 2, 2, "Би-энкодер (векторный поиск)", SZH, MID, b=True,
           where="заголовок би-энкодера", limit=half)
    clabel(d, x1 + half / 2, 2, "Кросс-энкодер (реранкер)", SZH, TEAL, b=True,
           where="заголовок кросс-энкодера", limit=half)

    y1, y2, y3 = 28, 79, 150
    h1, h23 = 38, 58

    # ── Левая колонка: вход → раздельное кодирование → сравнение чисел ─────
    box(d, x0, y1, inner, h1, ["Запрос"], SURF, tc=DEEP, sz=SZ, outline=LIGHT,
        pad=10, where="би-энкодер · запрос")
    box(d, x0 + inner + igap, y1, inner, h1, ["Документ"], SURF, tc=DEEP, sz=SZ,
        outline=LIGHT, pad=10, where="би-энкодер · документ")
    box(d, x0, y2, inner, h23, ["Кодировщик", "вектор запроса"], SURF, tc=DEEP,
        sz=SZ, outline=LIGHT, pad=10, where="би-энкодер · кодировщик запроса")
    box(d, x0 + inner + igap, y2, inner, h23, ["Кодировщик", "вектор документа"],
        SURF, tc=DEEP, sz=SZ, outline=LIGHT, pad=10,
        where="би-энкодер · кодировщик документа")
    box(d, x0, y3, half, h23,
        ["Сравнение векторов", "косинусное сходство двух готовых чисел"],
        W, tc=DEEP, sz=SZ, outline=GOLD, pad=10, where="би-энкодер · сравнение")

    cL1, cL2 = x0 + inner / 2, x0 + inner + igap + inner / 2
    arrow(d, cL1, y1 + h1, cL1, y2, col=LIGHT, wd=3, head=9)
    arrow(d, cL2, y1 + h1, cL2, y2, col=LIGHT, wd=3, head=9)
    arrow(d, cL1, y2 + h23, cL1, y3, col=LIGHT, wd=3, head=9)
    arrow(d, cL2, y2 + h23, cL2, y3, col=LIGHT, wd=3, head=9)

    clabel(d, x0 + half / 2, y3 + h23 + 6, "кодируются ПОРОЗНЬ, документ — заранее",
           SZ, LIGHT, b=True, where="подпись би-энкодера", limit=half)

    # ── Правая колонка: вход → единый вход на шаг раньше → оценка ──────────
    box(d, x1, y1, inner, h1, ["Запрос"], SURF, tc=DEEP, sz=SZ, outline=TEAL,
        pad=10, where="кросс-энкодер · запрос")
    box(d, x1 + inner + igap, y1, inner, h1, ["Документ"], SURF, tc=DEEP, sz=SZ,
        outline=TEAL, pad=10, where="кросс-энкодер · документ")
    box(d, x1, y2, half, h23, ["Единый вход", "один текст вместо двух векторов"],
        W, tc=DEEP, sz=SZ, outline=GOLD, pad=10, where="кросс-энкодер · единый вход")
    box(d, x1, y3, half, h23,
        ["Модель оценивает релевантность", "один проход, отдельных векторов нет"],
        SURF, tc=DEEP, sz=SZ, outline=TEAL, pad=10, where="кросс-энкодер · оценка")

    cR1, cR2 = x1 + inner / 2, x1 + inner + igap + inner / 2
    arrow(d, cR1, y1 + h1, cR1, y2, col=TEAL, wd=3, head=9)
    arrow(d, cR2, y1 + h1, cR2, y2, col=TEAL, wd=3, head=9)
    arrow(d, x1 + half / 2, y2 + h23, x1 + half / 2, y3, col=TEAL, wd=3, head=9)

    clabel(d, x1 + half / 2, y3 + h23 + 6, "читаются ВМЕСТЕ, одним вызовом модели",
           SZ, TEAL, b=True, where="подпись кросс-энкодера", limit=half)

    save(im, "case3-biencoder-vs-crossencoder.png")


def case4_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 4 · поиск по изображениям", sz=28)

    y = 170
    node_n8n(d, 60, y, 320, 160, "Скан бланка (data URL)", "formTrigger",
              kind="trigger")
    node_n8n(d, 420, y, 620, 160, "Embed image",
              ["httpRequest → /v1/embeddings", "model: amazon/titan-embed-image-v1"], kind="external")
    node_n8n(d, 1080, y, 300, 160, "Result screen", "form · completion", kind="code")
    arrow_n8n(d, 380, 420, y + 80)
    arrow_n8n(d, 1040, 1080, y + 80)

    callout(d, 140, y + 220, 1300, 200,
            "Находка, не ожидание плана: ответ приходит без ошибки и всё равно не работает",
            ["voyage-multimodal-3 не найден на OpenRouter этого стенда ни под одним написанием id",
             "amazon/titan-embed-image-v1 существует, вектор приходит — НО на реальном разрешении",
             "скана (300×450) он битово ОДИНАКОВЫЙ для любых двух разных картинок (cosine=1,0)",
             "«отвечает без ошибки» ≠ «использует вход» — проверено подачей двух разных входов"],
            tone="warn")
    d.text((140, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case4-n8n-mm-scheme.png")


# ── Схема сцены Кейса 4 — «case4-shema-postanovka.png» (правило С1, канон
# `tools/seminar-production/forma-keysa-s-zamerom.md` §2) ───────────────────
# ПЕРЕРИСОВАНА 2026-11-12 вместе с переписыванием кейса (issue #311).
#
# Что было и почему перестало быть верным. Прежняя схема вела сплошной ряд
# «скан → подпись (OCR) превращает картинку в текст → текстовый поиск», а
# пунктирная стрелка указывала на узел подписи: кейс строился вокруг версии
# «подписать картинку словами», и обойти он пытался именно этот шаг. Кейс
# переписан — разбирается ПРЯМОЕ сравнение картинок, а подпись осталась
# упоминанием, одной из трёх версий, а не несущим узлом потока. Схема, на
# которой подпись стоит сплошным узлом, после этого обещает залу не то,
# что кейс делает.
#
# Что стало. Сплошной ряд — ровно то, что уже СОБРАНО этим занятием и чего
# зал не вспоминает, а видел сегодня: скан приходит в заявке → хранилище
# (Кейс 1) → поиск находит похожее (Кейсы 1–3). Пунктирная золотая цель —
# ровно тот шаг, который кейсу предстоит сделать: сравнение самих
# изображений в их числовом представлении, минуя текстовый пересказ.
# Стрелка указывает в СТЫК между «скан приходит» и «хранилище» — это и есть
# место, где шаг встанет: вопрос кейса не в том, как искать, а в том, что
# класть в хранилище, когда документ не текст, а картинка.
def case4_shema_postanovka():
    # Холст НАРОЧНО плоский (1700×440, ширина к высоте 3,9). Замер: при
    # прежних 1700×560 сборщик на n60 ужимал схему до 57% отведённой ширины
    # («СХЕМА ЗАЖАТА»), потому что высоты слайд даёт всего 2,28″; при 440 та
    # же схема встаёт в 72% и читается крупнее. Та же плоская пропорция у
    # принятой схемы сцены Кейса 1 (1700×420), где предупреждения нет.
    im = Image.new("RGB", (SCENE_W_PX, 440), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в потоке поиска встанет сравнение самих изображений", sz=26, y=14)
    d.text((40, 54),
           "хранилище и поиск уже собраны сегодня — вопрос в том, что класть в хранилище,",
           font=f(19), fill=LIGHT)
    d.text((40, 78),
           "когда документ пришёл картинкой",
           font=f(19), fill=LIGHT)

    y1, h1 = 118, 118
    nodes = [
        ("Скан приходит в заявке", "бланк или чек у Ольги"),
        ("Хранилище", "собрано Кейсом 1 этого занятия"),
        ("Поиск находит похожее", "Кейсы 1–3 этого занятия"),
    ]
    gap = 50
    n = len(nodes)
    node_w = (SCENE_W_PX - 80 - gap * (n - 1)) // n
    xs = [40 + i * (node_w + gap) for i in range(n)]
    cy1 = y1 + h1 / 2
    for i, (title, sub) in enumerate(nodes):
        box(d, xs[i], y1, node_w, h1, [title, sub], SURF, tc=DEEP, sz=19,
            outline=LIGHT, where=f"сцена-узел {i + 1}")
        if i:
            arrow(d, xs[i - 1] + node_w, cy1, xs[i], cy1, col=LIGHT, wd=4)

    # Стык «скан приходит» → «хранилище»: туда и встаёт шаг, который делает кейс.
    # Золотая метка ставится прямо на соединитель — чтобы место было названо
    # точкой на потоке, а не только направлением пунктирной стрелки.
    joint_x = (xs[0] + node_w + xs[1]) / 2
    d.ellipse([joint_x - 10, cy1 - 10, joint_x + 10, cy1 + 10], fill=GOLD)

    y2, h2 = 300, 124
    goal_w = 980
    goal_x = SCENE_W_PX / 2 - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Делаем сегодня:",
         "сравнивать сами изображения в их числовом представлении",
         "— минуя пересказ картинки словами"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, goal_x + goal_w * 0.22, y2, joint_x, cy1 + 22,
          col=GOLD, wd=4, dash=True)

    save(im, "case4-shema-postanovka.png")


# ── «case4-edinoe-prostranstvo.png» — чем вообще сравнивают картинку с
# картинкой (issue #311). Схема отвечает на один вопрос, который кейс
# обязан закрыть до первого замера: почему два ЧИСЛОВЫХ ряда вообще можно
# сравнить между собой, если один получен из пикселей, а другой из слов.
# Ответ — в том, что считает их ОДНА И ТА ЖЕ модель и кладёт в ОДНО
# пространство; оттуда и берётся право сравнивать их напрямую.
# Числа: длина вектора рабочей модели — 2048 (`stend/raw/
# case4_quality_limits.json`, `engines.api.embedding_dim`); косинус и
# расстояние — как их считает сам сценарий на стенде (узел «Косинусное
# расстояние до индекса», кадр `case4-n8n-cosine-panel.png`).
def case4_edinoe_prostranstvo():
    im = Image.new("RGB", (SCENE_W_PX, 690), W)
    d = ImageDraw.Draw(im)
    head(d, "Одна модель, одно числовое пространство, одно сравнение", sz=28)
    d.text((40, 64),
           "картинку и подпись к ней считает одна и та же модель — поэтому их числовые",
           font=f(20), fill=LIGHT)
    d.text((40, 90),
           "ряды лежат в одном пространстве и сравнимы между собой напрямую",
           font=f(20), fill=LIGHT)

    widths = [330, 400, 345, 345]
    gap = (SCENE_W_PX - 80 - sum(widths)) / (len(widths) - 1)
    xs, x = [], 40
    for wd_ in widths:
        xs.append(x)
        x += wd_ + gap
    y_top, y_bot, h = 150, 330, 130
    cy_top, cy_bot = y_top + h / 2, y_bot + h / 2
    y_mid, h_mid = 215, 200
    cy_mid = y_mid + h_mid / 2

    # 1 — два разных входа
    box(d, xs[0], y_top, widths[0], h, ["Скан чека", "пиксели"], SURF, tc=DEEP, sz=19,
        outline=LIGHT, where="вход · картинка")
    box(d, xs[0], y_bot, widths[0], h, ["Подпись к чеку", "слова"], SURF, tc=DEEP, sz=19,
        outline=LIGHT, where="вход · текст")

    # 2 — одна модель на оба входа
    box(d, xs[1], y_mid, widths[1], h_mid,
        ["Одна модель", "nvidia/nemotron-3.5-embed-1b"], SURF, tc=DEEP, sz=19,
        outline=TEAL, where="модель")

    # 3 — два вектора в одном пространстве
    box(d, xs[2], y_top, widths[2], h, ["Вектор картинки"], W, tc=DEEP, sz=19,
        outline=TEAL, where="вектор · картинка")
    box(d, xs[2], y_bot, widths[2], h, ["Вектор подписи"], W, tc=DEEP, sz=19,
        outline=TEAL, where="вектор · текст")
    fr_x, fr_w = xs[2] - 22, widths[2] + 44
    fr_y, fr_h = y_top - 24, (y_bot + h + 24) - (y_top - 24)
    dashbox(d, fr_x, fr_y, fr_w, fr_h, TEAL)
    clabel(d, xs[2] + widths[2] / 2, fr_y + fr_h + 10, "одно числовое пространство", 18,
           TEAL, b=True, where="подпись пространства", limit=fr_w)

    # 4 — сравнение
    box(d, xs[3], y_mid, widths[3], h_mid,
        ["Косинус", "двух векторов", "— одно число"], W, tc=DEEP, sz=19,
        outline=GOLD, where="сравнение")

    arrow(d, xs[0] + widths[0], cy_top, xs[1], cy_mid - 40, col=LIGHT, wd=4)
    arrow(d, xs[0] + widths[0], cy_bot, xs[1], cy_mid + 40, col=LIGHT, wd=4)
    arrow(d, xs[1] + widths[1], cy_mid - 40, fr_x, cy_top, col=TEAL, wd=4)
    arrow(d, xs[1] + widths[1], cy_mid + 40, fr_x, cy_bot, col=TEAL, wd=4)
    arrow(d, xs[2] + widths[2], cy_top, xs[3], cy_mid - 40, col=GOLD, wd=4)
    arrow(d, xs[2] + widths[2], cy_bot, xs[3], cy_mid + 40, col=GOLD, wd=4)

    # Числа — плашками, не внутри абзаца (канон «Форма подачи слайда»).
    yp, hp, gp = 548, 102, 30
    pw = (SCENE_W_PX - 80 - gp * 2) / 3
    plashki = [
        (["Длина вектора", "2048 чисел"], TEAL),
        (["Косинус 1", "направления совпали"], GOLD),
        (["Расстояние", "1 − косинус"], LIGHT),
    ]
    for i, (lines, col) in enumerate(plashki):
        box(d, 40 + i * (pw + gp), yp, pw, hp, lines, SURF, tc=DEEP, sz=20,
            outline=col, where=f"плашка {i + 1}")

    save(im, "case4-edinoe-prostranstvo.png")


# ── Иллюстрация метрики n28 — «case2-razryv-metriki.png» (issue #311,
# правка владельца 2026-11-04: «слайд не читается, что это — доля успешных
# ответов или что?? надо описать что делаем и что замеряем»). Нарочно
# абстрактная (не документ про кибернетику из n27/n29) — реальный пример и
# его разрез показывает n29 отдельным тактом, дублировать его здесь нельзя
# (канон С11, и это испортило бы reveal n29).
def case2_razryv_metriki():
    """Компактная версия (issue #311): заголовок «Что считаем «разорван»»
    уже стоит жирным в тексте плашки над схемой — дублировать его здесь
    значило бы тратить вертикальный бюджет на повтор. Низкое соотношение
    высота/ширина (120/1600) держит отведённую фигуре долю композиции
    маленькой, чтобы таблица 5×4 под ней не переполнялась (замерено:
    230 px высотой даёт ПЕРЕПОЛНЕНИЕ/НЕ ПОМЕСТИЛОСЬ на n28 — см.
    iteration-log.md)."""
    im = Image.new("RGB", (1600, 90), W)
    d = ImageDraw.Draw(im)

    y, h = 6, 56
    w1, w2, gap = 700, 700, 20
    x1 = 60
    x2 = x1 + w1 + gap
    box(d, x1, y, w1, h, ["кусок N", "«…часть ответа»"], SURF, tc=DEEP, sz=15,
        outline=TEAL, where="кусок N")
    box(d, x2, y, w2, h, ["кусок N+1", "«ответа…»"], SURF, tc=DEEP, sz=15,
        outline=GOLD, where="кусок N+1")

    cut_x = x1 + w1 + gap / 2
    yy = y - 5
    while yy < y + h + 5:
        d.line([cut_x, yy, cut_x, min(yy + 6, y + h + 5)], fill=RED, width=3)
        yy += 12
    clabel(d, cut_x, y + h + 6, "разрез куска", 11, RED, where="подпись разреза")
    save(im, "case2-razryv-metriki.png")


if __name__ == "__main__":
    case1_shema_postanovka()
    case1_scheme()
    case2_shema_postanovka()
    case2_scheme()
    case2_razryv_metriki()
    case3_shema_postanovka()
    case3_scheme()
    case3_biencoder_vs_crossencoder()
    case4_scheme()
    case4_shema_postanovka()
    case4_edinoe_prostranstvo()
    report()
