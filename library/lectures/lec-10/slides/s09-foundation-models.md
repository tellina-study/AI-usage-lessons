---
id: s09
type: content
duration_min: 1.5
assertion: "Foundation models меняют порог входа: команда из 3 человек дообучает TerraMind на тысячах изображений вместо миллионов. Риск — vendor concentration: вся индустрия L1 строится на 2-3 моделях IBM / NASA / ESA."
learning_goal: "Foundation model + RAG-pattern + vendor concentration risk"
learning_outcomes: [LO1a]
chapter_ref: "§1.3 Часть 1 — Foundation models 2026"
references: [ibm-research-2025-terramind, nasa-earth-2025-prithvi, arxiv-2505-agrifm]
visual:
  pattern: 2col_diagram
  primary: "Слева — satellite imagery sample (Sentinel-2 multispectral) + diagram TerraMind multimodal transformer; справа — vendor concentration risk callout + Prithvi-EO 2.0 cite"
---

# Foundation models 2026 — TerraMind, Prithvi-EO 2.0

## Assertion

Foundation models меняют порог входа: команда из 3 человек дообучает TerraMind на тысячах изображений вместо миллионов. Риск — vendor concentration: вся индустрия L1 строится на 2-3 моделях IBM / NASA / ESA.

## Visual

Двухколоночный layout.

**Левая колонка (55%) — что такое TerraMind / Prithvi-EO 2.0:**
- Сверху — сэмпл спутникового снимка Sentinel-2 (~10-метровое разрешение, мультиспектральный) в Ocean rounded box. Подпись 12pt: «Sentinel-2 / ESA Copernicus · 10 м · 13 спектральных каналов».
- Под ним — diagram TerraMind: multimodal transformer (оптика + SAR + temporal + IoT + текст) → fine-tune для downstream-задачи. **1 триллион токенов pretrain** (gold accent).
- Прихvi-EO 2.0 как успешная специализированная модель: NASA + IBM, открыта через Hugging Face.

**Правая колонка (45%) — vendor concentration risk:**
- Callout Ocean rounded box: «**Риск vendor concentration.** Вся индустрия L1 на 2-3 foundation models от IBM / NASA / ESA. Закрытие модели = downstream-команды теряют capabilities одномоментно. Санкционная asymmetry: РФ-команды формально открытый доступ через HF, но GPU (NVIDIA H100/A100) под export controls».
- AgriFM disambig: «AgriFM = University of Hong Kong + Wuhan University (arXiv 2505.21357, май 2025) — **НЕ Carnegie Mellon**».

Footer 12pt italic: «Архитектура advisor 2026: foundation layer (TerraMind) + RAG к local regulator + LLM генерация + abstention. Источники: IBM Research blog 2025-04; NASA Earth Observatory 2025; arXiv 2505.21357».

## Speaker notes

Два события 2025 года изменили картину первой ступени на горизонте трёх-пяти лет, и инженер должен о них знать.

TerraMind — foundation model от IBM Research и Европейского космического агентства, выпущена в открытый доступ в 2025 году. Это первая «GPT-3-момента» модель для Earth observation: предобучена на одном триллионе токенов спутниковых данных, поддерживает несколько модальностей — оптические снимки, радар синтезированной апертуры, мультиспектральные изображения, временные ряды, метаданные IoT-сенсоров, агрономические отчёты в текстовой форме. Архитектура двойного scale — связывает локальный pixel-level и global region-level контекст. Применение в АПК: variable-rate prescriptions, прогноз урожайности на уровне поля, детекция стресса культуры за недели до видимых симптомов.

Prithvi-EO 2.0 — продолжение совместного проекта IBM и NASA, специализированная foundation model для агромониторинга. Главные улучшения от 1.0 к 2.0 — deeper metadata understanding и temporal capability: модель умеет работать с временными рядами одного и того же поля, не только snapshots.

Что это меняет для инженера? Раньше каждая команда стартапа в AgTech обучала свою свёрточную сеть с нуля на собственных размеченных датасетах — это требовало миллионы изображений, миллионы долларов, годы работы. Foundation model сдвигает баланс: команда из трёх человек может дообучить TerraMind на специализированной задаче на тысячах изображений вместо миллионов. Это понижает порог входа для команд из университетов и небольших стартапов.

Но одновременно создаёт системный риск. Если все AgTech-решения L1 построены на двух-трёх foundation models, надёжность всего слоя зависит от continuity этих моделей. Три класса риска. Первый — закрытие модели: Hugging Face аккаунт удалён или лицензия изменена. Второй — деградация поддержки: модель не обновляется, обучающие данные устаревают. Третий — геополитическая недоступность: санкционные ограничения, export controls на ML-модели. Российские команды формально имеют открытый доступ к Prithvi-EO через Hugging Face, но дообучение требует GPU-кластера на NVIDIA H100 или A100, которые сами по себе под санкционными ограничениями.

Маленькая, но важная техническая корректировка: AgriFM — это публикация исследовательских групп Гонконгского университета и Уханьского университета в мае 2025 года, а не Carnegie Mellon, как иногда указывается в обзорных материалах. Crop Wizard — это RAG-grounded advisory приложение, не отдельный foundation model «Crop-LLM». Это пример misattribution, против которого работают наши собственные навыки fact-check.

Архитектура advisor 2026 года — это паттерн, не модель. Foundation layer как perception плюс RAG к локальному регулятору плюс LLM поверх для генерации recommendation плюс явный отказ при low confidence плюс человек в цикле для критичных решений. К этому паттерну мы будем возвращаться в каждой следующей failure-истории.

## Источники

- IBM Research blog (2025-04) — TerraMind.
- NASA Earth Observatory (2025) — Prithvi-EO 2.0.
- arXiv 2505.21357 (май 2025) — AgriFM (University of Hong Kong + Wuhan).
