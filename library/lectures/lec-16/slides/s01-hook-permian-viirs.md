---
id: s01
type: hero_cover
duration_min: 2
assertion: "YOLOv8 видит каждый резервуар на промысле автоматически. Computer vision — это уже не демо, а production-grade infrastructure для нефтегаза."
learning_goal: "Эмоциональный hook + AI-explicit (Phase 8.6 Item 1): real bbox detection на oil tanks → foreshadow Q1 mainstream AI + Q2 monitoring"
failure_bucket: partial
chapter_ref:
  parts: [chapter.md]
  sections: ["Введение (§ Почему нефтегаз — особый случай для AI)"]
visual:
  type: image
  description: "YOLOv8-OBB object detection с rotated bounding boxes на oil storage tanks — реальный AI-вывод на инфраструктуре нефтегаза. Замена Phase 8.6 Item 1: AI-explicit vs prior VIIRS ESG/scale image."
  source_url: "https://www.ultralytics.com/blog/ai-in-oil-and-gas-refining-innovation"
  acquisition_tier: 3
  hero: true
  area_pct: 60
visible_numbers: ["AI видит каждый резервуар", "0,41% выручки Aramco от AI", "Сотни резервуаров — секунды inference"]
russification_check: "YOLOv8, Ultralytics, Aramco — brand allowlist; «резервуар», «нефтегазоносный», «промысел» — RU."
speaker_notes_target_words: 220
---

# YOLOv8 видит каждый резервуар. AI в нефтегазе — это уже не демо.

## Visible content

Hero ≥60% площади слайда: реальный output computer-vision модели **YOLOv8-OBB** (Oriented Bounding Boxes) на снимке нефтепромысла — каждый резервуар-хранилище автоматически обведён повёрнутым прямоугольником с confidence score. Под фото — атрибуция: «Ultralytics · YOLOv8-OBB · промышленный демо, 2024».

Справа — текстовый блок:

- **Сотни резервуаров** на промысле детектируются за секунды inference.
- Это **не демо** — это production-grade infrastructure (asset inventory, оптимизация обхода, anomaly detection).
- **Aramco METABRAIN** — крупнейшая отраслевая foundation model, **0,41% выручки** в 2024 году.
- AI в нефтегазе работает там, где **есть данные и определены процессы** (мы вернёмся к этой матрице на s04).

Внизу — gold-tint полоса с центральным тезисом:

«AI в нефтегазе нужен не как улучшалка на 5%, а как способ закрыть конкретные провалы. И сегодня — он либо закрывает их, либо проваливается громко и публично.»

## Speaker notes

Это не stock illustration и не художественный рендер. Это реальный output computer-vision модели YOLOv8-OBB — Ultralytics, версия с поворачиваемыми bounding boxes — на снимке нефтепромысла с резервуарами-хранилищами. Каждый резервуар автоматически обведён повёрнутым прямоугольником, и для каждого — confidence score модели в правом верхнем углу.

То, что вы видите на этом кадре — это не демо для конференций. Это уже production-grade computer-vision infrastructure, развёрнутая на сотнях промыслов по всему миру. Asset inventory без выезда инспектора. Оптимизация маршрута обхода. Anomaly detection — если резервуар внезапно поменял геометрию или цветовую сигнатуру, alert уходит оператору. Это узкая, верифицируемая, скучная задача — и в этом её сила.

Зачем именно это на первом слайде. Потому что многие думают, что AI в нефтегазе — это про красивые demo с большими языковыми моделями типа Aramco METABRAIN на 250 миллиардов параметров. METABRAIN существует, и в 2024 году принёс компании 1,8 миллиарда долларов реализованной стоимости — но это 0,41 процента от 436-миллиардной выручки Aramco. Большая, видимая часть AI в нефтегазе — это узкие, верифицируемые, скучные computer-vision и time-series ML задачи на конкретных промыслах. Резервуары. Скважины. Метановые шлейфы со спутника.

И в этом главный вопрос лекции, который мы вынесем на keystone-слайд: когда у нас есть данные и определены процессы — AI работает. Когда нет — он либо необходим как единственная альтернатива, либо, наоборот, опасен. На этой матрице построена вся лекция.
