---
id: s09
type: process
duration_min: 2
assertion: "AI-диагностика — это computer vision-классификация: image → label, с confidence score. Это не LLM."
learning_goal: "Как технически работает CV-диагностика"
learning_outcomes: [LO1]
frame_mapping: ["Другой AI"]
chapter_ref: "§2.1 — Как технически работает AI-диагностика"
references: [rajpurkar-2017-chexnet, selvaraju-2017-gradcam]
visual:
  pattern: pipeline
  primary: "4-stage pipeline (Input → Model → Output → Workflow) с MSO_SHAPE.RIGHT_ARROW + sample X-ray с heatmap справа"
  illustration:
    type: schematic
    sources:
      - "Self-generated pipeline через PowerPoint shapes (Ocean palette, RIGHT_ARROW)"
      - "CheXNet paper figure — Rajpurkar et al. 2017 arXiv:1711.05225 (Stanford ML Group, heatmap example)"
      - "Wikimedia Commons CC-BY https://commons.wikimedia.org/wiki/Category:Chest_X-rays (sample chest X-ray, anonymized)"
    caption: "CheXNet pipeline (Rajpurkar et al. 2017, Stanford ML)"
interaction: none
---

# AI-диагностика — это computer vision, не LLM

## Assertion

AI-диагностика — это computer vision-классификация: image → label, с confidence score. Это не LLM.

## Visual

Горизонтальный pipeline на всю ширину слайда. Четыре прямоугольника-стадии, соединённые MSO_SHAPE.RIGHT_ARROW в Ocean palette. Стадия 1 «Input» (синий `#1C7293`): медицинское изображение (X-ray / CT / MRI / дермато-скан); препроцессинг. Стадия 2 «Model» (mid `#065A82`): CNN (ResNet, EfficientNet) или Vision Transformer; pre-trained ImageNet + fine-tuned на медицинском dataset. Стадия 3 «Output» (deep `#21295C`): probability (0–1) + bounding box / heatmap. Стадия 4 «Workflow» (gold `#F0AB00`): врач видит heatmap + probability и принимает решение. Над pipeline — assertion. Под — sample chest X-ray с overlay heatmap (CheXNet figure) в Ocean rounded box. Caption: «Это не LLM. CV-pipeline уровня 2017–2024 с medical fine-tuning».

## Speaker notes

AI-диагностика — это в первую очередь computer vision-классификация: на вход подаётся медицинское изображение, на выход — вероятностное распределение по классам патологий и тепловая карта или bounding box, показывающие, где модель «увидела» признак. Этот pipeline укладывается в четыре стадии.

Первая стадия — input. Сырое медицинское изображение: DICOM-файл с КТ-аппарата, JPEG-фото дермато-скана, PNG-маммограмма. Изображение проходит препроцессинг — ресайз, нормализация интенсивности, иногда деперсонализация (удаление PHI-меток с пиксельного уровня).

Вторая стадия — модель. Исторически CNN: ResNet, EfficientNet. С 2024 года всё чаще Vision Transformer и специализированные foundation models — MedCLIP, BiomedCLIP, RoentGen. Обычная схема — pre-trained на ImageNet, затем fine-tuned на медицинском датасете.

Третья стадия — output. Probability score от нуля до единицы для каждого класса патологий и тепловая карта, чаще всего сгенерированная техникой Grad-CAM (Selvaraju et al. 2017), показывающая, какие пиксели вносили наибольший вклад в предсказание. Это попытка дать врачу explainability — неполную, но лучше, чем чёрный ящик.

Четвёртая стадия — workflow. Врач видит изображение, heatmap и probability score и принимает диагностическое решение. AI здесь — decision support, не decision maker.

Историческая референсная модель — CheXNet (Rajpurkar et al. 2017), 121-слойная DenseNet, обученная классифицировать четырнадцать патологий грудной клетки. CheXNet был одним из первых широко известных результатов «AI выходит на уровень специалиста». Современные модели — Vision Transformers и multimodal foundation models — превосходят CheXNet по точности и универсальности, но методологическая основа осталась той же.
