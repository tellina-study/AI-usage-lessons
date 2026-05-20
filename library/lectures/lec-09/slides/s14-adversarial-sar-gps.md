---
id: s14
type: assertion_visual
duration_min: 2
assertion: "Adversarial-атаки на SAR ATR + GPS-spoofing — accuracy benchmark обманчив, single-source decision хрупка. 820 случаев GPS-интерференции в Латвии 2024 vs 26 в 2022."
learning_goal: "2-в-1 failure: adversarial SAR + GPS spoofing → urok про single-source"
learning_outcomes: [LO1b, LO3]
chapter_ref: "§1.7 — Adversarial-атаки и GPS-spoofing"
references: [du-2024-arxiv, stanford-scpnt-2025, foreign-policy-2024]
visual:
  pattern: matrix
  primary: "2 case cards + Bayesian + multi-GNSS защита"
---

# Adversarial SAR + GPS-spoofing — accuracy обманчив, single-source хрупок

## Assertion

Adversarial-атаки на SAR ATR + GPS-spoofing — accuracy benchmark обманчив, single-source decision хрупка. 820 случаев GPS-интерференции в Латвии 2024 vs 26 в 2022.

## Visual

Под assertion — 2 равные колонки.

**Слева — Adversarial SAR ATR** (Ocean rounded box):
- Schematic illustration: танк с corner reflectors → SAR classifier → misclassification
- Иконка `triangle-alert` Primary mid 32px
- Текст: «Дешёвые металлические рассеиватели в специальной геометрии обманывают classifier»
- Source: Du et al. 2024 arXiv:2312.02912
- Защита (3 пункта):
  - Bayesian uncertainty estimates
  - Adversarial training
  - Abstention pathway → human

**Справа — GPS-spoofing civil aviation** (Ocean rounded box):
- QuickChart mini bar: 2022 — 26 cases; 2024 — 820 cases (~32×, gold)
- Иконка `radio-tower` Primary mid 32px
- Текст: «Российские средства РЭБ (Krasukha-4, Borisoglebsk-2) — Чёрное море, Восточная Европа»
- Source: Stanford SCPNT 2025
- Защита (3 пункта):
  - Multi-GNSS (GPS+GLONASS+Galileo+BeiDou)
  - INS-fallback (инерциальная)
  - eLORAN наземная навигация

Внизу — bridge callout 14pt italic в Teal-tint боксе: «Spillover: военный РЭБ-эффект распространяется на не-комбатантов. Защита GNSS — это collective good».

## Speaker notes

Второй провальный кейс Sense — adversarial-атаки на SAR ATR. Идея проста. Classifier обучен распознавать танки и пусковые установки по SAR-снимкам; противник размещает на местности или на технике дешёвые металлические рассеиватели — corner reflectors — в специальной геометрии, и classifier начинает неправильно классифицировать объекты. Опубликованные исследования показывают физическую реализуемость таких атак — Du et al., 2024. Это не лабораторный edge case, это знание, доступное любой противоборствующей стороне.

Урок. Стандартный benchmark accuracy обманчив для adversarial-доменов: противник определяет distribution на test-time. Защита требует трёх вещей одновременно. Bayesian uncertainty estimates — модель должна уметь сказать «я не уверена», а не выдать confident wrong answer. Adversarial training — обучение на adversarial-примерах, дополняющее обычный датасет. И pathway абстракции, abstention: когда uncertainty высокая, модель эскалирует к человеку, а не молча выбирает «наиболее вероятный» класс.

Третий провальный кейс Sense — GPS-spoofing гражданской авиации. AI как таковой ни при чём — но кейс демонстрирует фундаментальную хрупкость GNSS-зависимых автономных систем, на которых строится много AI-применений: drone navigation, авиадиспетчеризация, точные посадки. По данным Латвии, в 2024 году зарегистрировано 820 случаев интерференции спутникового сигнала против 26 в 2022 году. Это тридцатидвухкратный рост. Большая часть — атрибуция к российским средствам РЭБ — Krasukha-4, Borisoglebsk-2; зона спугнутого сигнала включает Чёрное море и Восточную Европу.

Урок. GNSS-only — это single point of failure. Защита системы — это multi-GNSS, одновременная работа с GPS плюс GLONASS плюс Galileo плюс BeiDou; INS-fallback — инерциальная навигация без внешних сигналов; eLORAN — наземная радионавигация; долгосрочно — quantum INS, исследуется DARPA и ESA.

И главное — spillover-проблема. Военный РЭБ-эффект распространяется на не-комбатантов: гражданские самолёты в Восточной Европе и на Ближнем Востоке регулярно попадают в зоны искажённого GPS. Защита GNSS — это collective good, и инженер, работающий хоть с одной из сторон, обязан понимать масштаб spillover.
