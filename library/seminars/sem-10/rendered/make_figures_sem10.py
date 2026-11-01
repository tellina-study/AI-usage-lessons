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
# Сплошной контур — узлы, уже работающие с прошлого занятия (эмбеддинг куска
# и хранилище, решённые Кейсом 1). Пунктирный золотой контур — узел, который
# СТРОИТ этот кейс: разбиение документа на куски, встающее ПЕРЕД эмбеддингом.
# Имён инструмента внутри узлов нет умышленно — слой 1 - устройство решения,
# не экран n8n (экран — отдельно, n26/n27).
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
        ("Эмбеддинг куска", "уже работает, Кейс 1", False),
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
# Сплошной ряд — то, что уже построено этим занятием: скан приходит в
# заявке, подпись (OCR) превращает его в текст, и ТЕКСТОВЫЙ поиск (тот же
# механизм, что Кейсы 1-3) находит похожий документ. Пунктирная золотая цель
# — то, что Кейс 4 пробует: сравнивать саму картинку в её числовом
# представлении, пропустив шаг «превратить в текст» — стрелка поэтому
# указывает на узел подписи/OCR, не на вход и не на весь поток целиком: это
# единственный шаг, который кейс пытается обойти.
def case4_shema_postanovka():
    im = Image.new("RGB", (SCENE_W_PX, 560), W)
    d = ImageDraw.Draw(im)
    head(d, "Где в потоке поиска встанет сравнение самой картинки", sz=28)
    d.text((40, 64),
           "подпись и текстовый поиск уже работают — вопрос в том, можно ли пропустить",
           font=f(20), fill=LIGHT)
    d.text((40, 90),
           "шаг «превратить картинку в текст» и сравнивать саму картинку",
           font=f(20), fill=LIGHT)

    y1, h1 = 160, 150
    nodes = [
        ("Скан бланка или чека", "в заявке Ольге"),
        ("Подпись: OCR → текст", "картинка пересказана словами"),
        ("Текстовый поиск находит похожий", "Кейсы 1–3 этого занятия"),
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

    y2, h2 = 380, 150
    goal_w = 820
    goal_x = xs[1] + node_w / 2 - goal_w / 2
    box(d, goal_x, y2, goal_w, h2,
        ["Пробуем сегодня:",
         "сравнивать саму картинку в её числовом представлении",
         "— без шага «превратить в текст»"],
        W, tc=DEEP, sz=19, outline=GOLD, where="сцена-цель")
    arrow(d, goal_x + goal_w / 2, y2, xs[1] + node_w / 2, y1 + h1,
          col=GOLD, wd=4, dash=True)

    save(im, "case4-shema-postanovka.png")


if __name__ == "__main__":
    case1_shema_postanovka()
    case1_scheme()
    case2_shema_postanovka()
    case2_scheme()
    case3_shema_postanovka()
    case3_scheme()
    case4_scheme()
    case4_shema_postanovka()
    report()
