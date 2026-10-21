---
id: s21
type: assertion_visual
duration_min: 3
assertion: "Obermeyer 2019 (Science): commercial AI для 200M Americans systematically underestimated severity для black patients. Proxy «стоимость лечения» вместо «тяжесть болезни»."
learning_goal: "Deep-dive bias case с actionable engineer lesson"
learning_outcomes: [LO3, LO8]
frame_mapping: ["Безопасность", "Человек vs AI", "LLM anti-pattern"]
chapter_ref: "§4.3 — Obermeyer 2019: как выбор метрики стал выбором политики"
references: [obermeyer-2019-science, berkeley-news-2019, stat-news-2019]
visual:
  pattern: pipeline
  primary: "3-box mechanism (Goal → Proxy used → Bias source) + result chart 26% more chronic illness + fix arrow «17.7% → 46.5% Black served»"
  illustration:
    type: paper
    sources:
      - "Obermeyer et al. 2019 Science — https://www.science.org/doi/10.1126/science.aax2342 (Figure 1: gap chart)"
      - "Berkeley News 2019 — https://news.berkeley.edu/2019/10/24/widely-used-health-care-prediction-algorithm-biased-against-black-people/"
      - "STAT News 2019 — https://www.statnews.com/2019/10/24/algorithm-racial-bias-care-black-patients/"
    caption: "Obermeyer et al., Science 2019. DOI: 10.1126/science.aax2342"
interaction: none
---

# Obermeyer 2019 — выбор прокси стал выбором политики

## Assertion

Obermeyer 2019 (Science): commercial AI для 200M Americans systematically underestimated severity для black patients. Proxy «стоимость лечения» вместо «тяжесть болезни».

## Visual

Верхняя половина слайда — 3-box mechanism pipeline в Ocean rounded box: Box 1 «Goal: identify patients needing additional care» → Box 2 «Proxy used: spending on previous care» → Box 3 «Bias source: black patients spent $1 800/year less historically (access disparities) → AI thinks less sick». Соединено MSO_SHAPE.RIGHT_ARROW. Нижняя половина — слева result-chart: на одинаковом risk score у чернокожих — `+26% more chronic illnesses` крупно gold. Справа — fix-arrow: «17.7% → 46.5% Black patients served» + «84% bias reduction». Сверху ассертион 20pt; снизу caption «Obermeyer, Powers, Vogeli, Mullainathan — Science 366, 447 (2019)».

## Speaker notes

Obermeyer, Powers, Vogeli и Mullainathan, Science, страницы 447–453, 2019 года. Это золотой стандарт case study по bias в medical AI; цитируется более трёх тысяч раз; обязательное чтение для любого AI-инженера, работающего в healthcare.

Контекст. В США существует коммерческий алгоритм Impact Pro, разработанный компанией Optum, дочкой UnitedHealth, и применяемый ежегодно для примерно двухсот миллионов американцев — для идентификации пациентов с высоким риском, нуждающихся в дополнительной координированной помощи. Алгоритм даёт risk score; пациенты с высоким score попадают в high-risk care management programs.

Что нашли исследователи. На одном и том же risk score чернокожие пациенты были существенно болезненнее, чем белые: у них было на двадцать шесть процентов больше хронических заболеваний. То есть алгоритм систематически недооценивал тяжесть болезни у черных пациентов.

Почему. Алгоритм был обучен предсказывать healthcare cost — расходы на лечение — как прокси для healthcare need, медицинской потребности. Эти две переменные коррелируют — больные тратят больше — но они не идентичны. Чернокожие пациенты исторически тратили на здравоохранение примерно на тысячу восемьсот долларов в год меньше, чем равно-больные белые, из-за access disparities: меньше страхового покрытия, географические барьеры, недоверие к системе, дискриминация. Алгоритм видел: у этих пациентов низкие расходы, значит, они «менее больны». На самом деле они были такими же больными, но получали меньше помощи.

Исправление. Когда исследователи переобучили алгоритм на гибридный proxy (cost + chronic conditions), bias уменьшился на восемьдесят четыре процента. Доля чернокожих пациентов в high-risk care management programs выросла с семнадцати и семи десятых процента до сорока шести и пяти десятых. Это не теоретическое улучшение — это конкретные пациенты, получившие доступ к дополнительной помощи. Инженерный урок: когда выбираете прокси, спрашивайте — какие демографические группы могут иметь систематически разный доступ к этой прокси? Выбор метрики — это выбор политики, даже когда никто о политике не думает.
