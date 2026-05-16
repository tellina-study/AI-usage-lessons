---
id: s10
type: assertion_visual
duration_min: 3
assertion: "Для медицинского AI «accuracy» недостаточна. Нужны 4 метрики: sensitivity, specificity, prevalence, PPV. Sens/spec не зависят от prevalence; PPV — зависит."
learning_goal: "Apply Bayes intuition к medical AI оценке"
learning_outcomes: [LO1, LO2]
frame_mapping: ["Другой AI", "Человек vs AI"]
chapter_ref: "§2.2 — Sensitivity, specificity, prevalence, PPV"
references: [rajpurkar-2017-chexnet]
visual:
  pattern: matrix
  primary: "2×2 confusion matrix (TP/FN/FP/TN с цветовыми маркерами) слева + 4-metric table с формулами справа + CheXNet sens 0.96 / spec 0.93 пример"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2×2 matrix + 4-metric table через PowerPoint shapes"
      - "CheXNet paper — Rajpurkar et al. 2017 arXiv:1711.05225 (verified sens 0.96, spec 0.93 для pneumonia subset, AUC 0.96)"
      - "Bayes formula reference — стандартная educational diagram"
    caption: "2×2 confusion matrix + 4 metrics; CheXNet (Rajpurkar 2017)"
interaction: none
---

# Для медицинского AI нужны 4 метрики, не одна

## Assertion

Для медицинского AI «accuracy» недостаточна. Нужны 4 метрики: sensitivity, specificity, prevalence, PPV. Sens/spec не зависят от prevalence; PPV — зависит.

## Visual

Слева в Ocean rounded box — 2×2 confusion matrix. Строки: «Truth: sick / healthy», столбцы: «AI prediction: positive / negative». Четыре ячейки: TP (зелёный), FN (red bold — опасная ошибка), FP (yellow), TN (зелёный). Справа — 4-row table в собственном Ocean rounded box: каждая строка содержит метрику + формулу + одно-фразное объяснение. `Sensitivity = TP/(TP+FN)` — «доля больных, которых поймал AI». `Specificity = TN/(TN+FP)` — «доля здоровых, которых не напугал». `Prevalence = (TP+FN)/Total` — «как часто болезнь в популяции». `PPV = TP/(TP+FP)` — «если AI сказал болен, какова вероятность». Внизу gold-info-card: «CheXNet pneumonia: sens 0.96, spec 0.93 → PPV ~8% при prev 1%, ~78% при prev 30%».

## Speaker notes

Для медицинского AI обычная accuracy — недостаточная метрика. Нужно различать четыре связанных понятия, и понимание разницы — minimal due diligence для оценки любой медицинской CV-модели.

Sensitivity, или чувствительность, — это доля больных людей, которых AI правильно поймал: TP делённое на TP плюс FN. Чувствительность критична для скрининга, где пропустить больного — катастрофа: рак на ранней стадии, инсульт, инфаркт. Specificity, или специфичность, — это доля здоровых, которых AI правильно не напугал: TN на TN плюс FP. Специфичность критична для confirmation-задач, где ложноположительный диагноз сам по себе наносит вред: биопсия, химиотерапия, паника пациента.

Prevalence — распространённость болезни в популяции. Это не свойство модели, а свойство популяции, на которой модель применяется. PPV, или positive predictive value, — это вероятность реальной болезни при положительном AI-ответе: TP на TP плюс FP. Через формулу Байеса PPV выражается через sens, spec и prev напрямую.

Главный нюанс. Sensitivity и specificity не зависят от prevalence — это свойства модели. PPV — зависит. Возьмём пример. CheXNet (Rajpurkar 2017) на pneumonia detection даёт примерно sens 0.94–0.96 и spec 0.89–0.93. В больничной выборке с prevalence 30 процентов PPV получается около семидесяти восьми процентов — клинически приемлемо. Если ту же модель применить как screening в общей популяции с prevalence один процент — PPV падает до примерно восьми процентов. Та же модель, та же accuracy — но восемь из ста положительных результатов действительно больны, остальные девяносто два — false positives. «94% accuracy» в маркетинге и «8% PPV в screening» — два очень разных восприятия одной модели.
