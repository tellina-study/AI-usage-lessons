#!/usr/bin/env python3
"""Программные схемы «слой 2» для Кейсов 1 и 4 Семинара 10 — реальные имена узлов и
реальные значения параметров со стенда (execution 2112 / 2114, см. README.md).

Живой скрин канваса n8n в этом окружении недостижим (задача явно просит не тратить
время на повторную попытку — см. README.md «Открытый технический риск» / `n8n_canvas_kit.py`
docstring, `notes/mcp-limitations.md` [#233-8]), поэтому здесь — программная схема в духе
n8n (подход `sem-08/rendered/n8n_canvas_kit.py`), подписанная в frontmatter будущего слайда
как `backup:` не-скриншот. Это НЕ слайд (Фаза 4 этим не является) — заготовка для неё.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, N8N_DISCLAIMER  # noqa: E402

W_PX, H_PX = 1600, 620


def case1_vector_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 1 · «С10 · Кейс 1 — векторное хранилище (демо-экран)» — execution 2112", sz=30)

    y = 180
    node_n8n(d, 40, y, 300, 160, "Вопрос + корпус с векторами", "formTrigger · s10-case1-vector",
              kind="trigger", subtype=None)
    node_n8n(d, 390, y, 300, 160, "Embed query (OpenRouter)",
              ["httpRequest → /v1/embeddings", "model: text-embedding-3-small"], kind="external")
    node_n8n(d, 740, y, 320, 160, "Simple Vector Store (cosine top-1)",
              ["Code: cosine(qvec, doc.embedding)", "top-1 из 10 документов, score=0.590"], kind="code")
    node_n8n(d, 1110, y, 300, 160, "Answer (RAG)",
              ["chainLlm + lmChatOpenRouter", "model: gpt-4o-mini"], kind="model")
    for x1, x2 in [(340, 390), (690, 740), (1060, 1110)]:
        arrow_n8n(d, x1, x2, y + 80)

    callout(d, 40, y + 220, 1370, 140,
            "Результат execution 2112",
            [f"вопрос: «При каком давлении удалось получить кристаллы гелия?»",
             f"найден кусок: needle-1 (cosine=0.590) — «...применив давление выше 35 атм...»",
             f"ответ модели: «При давлении выше 35 атм.» — верно"],
            tone="ok")
    d.text((40, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case1-n8n-vector-scheme.png")


def case4_mm_scheme():
    im = Image.new("RGB", (W_PX, H_PX), W)
    d = ImageDraw.Draw(im)
    head(d, "Кейс 4 · «С10 · Кейс 4 — мультимодальный эмбеддинг (демо-экран)» — execution 2114", sz=30)

    y = 180
    node_n8n(d, 60, y, 320, 160, "Скан бланка (data URL)", "formTrigger · s10-case4-mm",
              kind="trigger")
    node_n8n(d, 420, y, 620, 160, "Embed image (amazon/titan-embed-image-v1)",
              ["httpRequest → /v1/embeddings", "model: amazon/titan-embed-image-v1"], kind="external")
    node_n8n(d, 1080, y, 300, 160, "Result screen", "form · completion", kind="code")
    arrow_n8n(d, 380, 420, y + 80)
    arrow_n8n(d, 1040, 1080, y + 80)

    callout(d, 140, y + 220, 1180, 160,
            "Критическая находка (не ожидание плана)",
            ["voyage-multimodal-3 не существует на OpenRouter этого стенда (проверено живым вызовом)",
             "amazon/titan-embed-image-v1 существует, НО на реальном разрешении скана (300×450) отдаёт",
             "БИТОВО одинаковый вектор для любых двух разных картинок — рабочий диапазон найден только",
             "у маленьких превью (~64×96); подробности и сырые вызовы — debug_mm1..6.py"],
            tone="warn")
    d.text((140, H_PX - 28), N8N_DISCLAIMER, font=f(14), fill=MUTE)
    save(im, "case4-n8n-mm-scheme.png")


if __name__ == "__main__":
    case1_vector_scheme()
    case4_mm_scheme()
    report()
