---
id: s13
type: assertion_visual
duration_min: 2.5
assertion: "AI-диагностика хорошо работает в распределении обучения. Outside — может проваливаться unfairly. Bias = consequence design choices, не bug."
learning_goal: "2 bias case-cards (dermatology + pulse-ox); validation set должен покрывать deployment population"
learning_outcomes: [LO3]
frame_mapping: ["LLM anti-pattern", "Безопасность", "Человек vs AI"]
chapter_ref: "§2.5 — Где AI-диагностика проваливается: bias в CV"
references: [daneshjou-2022-science-advances, adamson-2018-jama-derm, sjoding-2020-nejm]
visual:
  pattern: matrix
  primary: "2 bias case-cards в Ocean rounded box (dermatology + pulse oximeter); каждая = title + mechanism + evidence + engineering implication"
  illustration:
    type: paper
    sources:
      - "Daneshjou et al. 2022 Science Advances — https://www.science.org/doi/10.1126/sciadv.abq6147 (paper figure)"
      - "Adamson & Smith 2018 JAMA Dermatology — https://jamanetwork.com/journals/jamadermatology/article-abstract/2688587"
      - "Sjoding et al. 2020 NEJM — pulse oximetry racial bias"
      - "FDA Safety Communication 2021 — pulse oximeter accuracy and skin pigmentation"
    caption: "Daneshjou 2022 Science Advances; Sjoding 2020 NEJM; FDA 2021"
interaction: none
---

# Bias = consequence design choices, не bug

## Assertion

AI-диагностика хорошо работает в распределении обучения. Outside — может проваливаться unfairly. Bias = consequence design choices, не bug.

## Visual

Две Ocean rounded box карточки большого размера слева и справа. Левая: заголовок «Dermatology skin tone bias» (20pt semi-bold), под заголовком 3 строки текста: «Mechanism: training datasets перепредставляют светлую кожу (ISIC archive)»; «Evidence: Daneshjou 2022 — sens падает на 20–30% на коже Фитцпатрика V–VI»; «Fix: fine-tuning на DDI-датасете закрыл gap». Правая: заголовок «Pulse oximeter racial bias», 3 строки: «Mechanism: optical sensor systematically overestimates SpO2 на dark skin»; «Evidence: Sjoding 2020 NEJM — гипоксия пропускается чаще у черных пациентов»; «AI implication: модели, использующие SpO2 как input feature, наследуют sensor bias». Сверху — ассертион; снизу — gold-strip: «Validation set должен покрывать deployment population».

## Speaker notes

AI-диагностика хорошо работает в распределении, на котором обучена. За пределами этого распределения она может проваливаться несимметрично — и эти провалы не bug, а consequence design choices в подборе тренировочных данных. Два классических кейса.

Первый — дерматология и тон кожи. Большинство публично доступных дерматологических AI-датасетов, включая ISIC challenge archive — основной открытый ресурс, — исторически перепредставляли пациентов со светлой кожей из США, Европы и Австралии. Daneshjou и соавторы в 2022 году (Science Advances) протестировали несколько ранее опубликованных дерматологических алгоритмов на разнообразной по тонам кожи выборке и обнаружили: на изображениях кожи с тёмными тонами Фитцпатрика V и VI чувствительность падала на двадцать–тридцать процентов по сравнению со светлыми тонами I–III. Важный нюанс: дерматологи-люди тоже работали хуже на тёмной коже, но fine-tuning на разнообразном датасете DDI закрыл этот разрыв для AI, и fine-tuned модели в итоге превзошли дерматологов в обнаружении злокачественных образований на тёмной коже. Source bias — не моральная категория, а технический следствие выбора датасета; и он решаем.

Второй — пульсоксиметры. Это случай, в котором bias проникает в AI через входной сенсор, а не через тренировочный датасет AI как такового. Пульсоксиметры систематически переоценивают SpO2 у пациентов с тёмной кожей — гипоксия пропускается чаще (Sjoding et al. 2020). FDA выпустило safety communication по этой проблеме в 2021 году. AI-системы, использующие SpO2 как input feature, наследуют этот сенсорный bias.

Инженерное следствие для обоих кейсов одинаковое: validation set должен покрывать deployment population. Это не academic point — это профессиональная ответственность.
