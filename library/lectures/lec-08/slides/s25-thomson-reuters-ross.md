---
id: s25
type: assertion_visual
duration_min: 2
assertion: "Thomson Reuters против Ross (Feb 2025): first US ruling REJECTING «добросовестное использование» в AI training. 2200/3000 headnotes infringed. Caveat: Ross — non-generative."
learning_goal: "Case 5: «добросовестное использование» rejected (с caveat)"
learning_outcomes: [LO4, LO5]
chapter_ref: "§3.6 — Thomson Reuters против Ross"
references: [reed-smith-tr-ross, judge-bibas-feb-2025]
visual:
  pattern: assertion_visual
  primary: "Reed Smith analysis screenshot + Warhol против Goldsmith 4-factor chip + «Урок: «добросовестное использование» не дефолт»"
  backup: assets/backup/s25-thomson-ross.png
---

# Thomson Reuters против Ross — first US отказ в «добросовестном использовании» (Case 5)

## Assertion

Thomson Reuters против Ross (Feb 2025): first US ruling REJECTING «добросовестное использование» в AI training. 2200/3000 headnotes infringed. Caveat: Ross — non-generative.

## Visual

Сверху assertion 22pt. Слева — Reed Smith analysis article screenshot мокап в Ocean rounded box. Справа — крупный fact-card: «Judge Bibas, Feb 2025 · 2200/3000 headnotes infringed · 4-factor «добросовестное использование» rejected». Под fact-card — Warhol против Goldsmith chip (4-factor reference). Под этим — крупный amber caveat box: «⚠ Caveat: Ross — non-generative AI (legal search). LLM/diffusion test cases pending (NYT, Andersen, Getty US)». Внизу — gold «УРОК ДЛЯ ИНЖЕНЕРА»: ««Добросовестное использование» — не дефолт. LLM/diffusion test cases впереди. Не строй продуктовый дорожная карта на предположении «добросовестное использование» как защита».

## Speaker notes

Пятый кейс — Thomson Reuters против Ross Intelligence. Это первое в США судебное решение, которое отвергло «добросовестное использование» как защита для AI training. Решение вынесено судьёй Bibas в феврале 2025 года. Конкретика. Ross Intelligence — компания, разрабатывавшая legal search engine на AI-основе. Для обучения модели Ross использовала Westlaw headnotes — короткие summary-аннотации судебных решений, являющиеся охраняемый авторским правом контент Thomson Reuters. Из трёх тысяч использованных headnotes, две тысячи двести были признаны infringed. Судья применил Warhol против Goldsmith four-factor test для «добросовестное использование» и пришёл к выводу, что Ross не проходит этот тест. Важный caveat. Ross — non-generative AI. Это legal search engine, который использовал headnotes для индексации и matching, не для generation нового контента. Применимость этого решения к LLM и diffusion моделям — открытый вопрос. Test cases в эту сторону — NYT против OpenAI, Andersen, Getty US — ещё впереди. Reed Smith опубликовал детальный analysis ruling, который мы цитируем в материалах лекции. Что эта решение уже изменило для индустрии. До февраля 2025 года значительная часть AI-индустрии действовала на предположении, что training на охраняемый авторским правом контент — это transformative «добросовестное использование», и поэтому defensible. Решение Bibas сигнализирует, что эта предположение — не self-evident. Конкретный исход для generative AI ещё не определён, но baseline сдвинулся: «добросовестное использование» надо доказывать, не предполагать. Урок для инженера: «добросовестное использование» — не дефолт. LLM и diffusion test cases впереди — NYT, Andersen, Getty US. Не строй продуктовый дорожная карта на предположении «добросовестное использование» как защита. Если твой business model завязан на use охраняемый авторским правом контент без licensing — это business model на legally unstable foundation. Альтернатива — лицензированный корпус model, как Adobe Firefly: training data — это core business asset, не free externality. Это сейчас выглядит как структурный сдвиг индустрии 2025-2026 годов: licensed data становится дороже, и эта стоимость переходит в product pricing.
