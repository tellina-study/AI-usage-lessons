---
id: s24
type: assertion_visual
duration_min: 3
assertion: "BASF Geismar: –30% batch defects. Pfizer Vox: +20000 доз mRNA per batch — но «recommend», не autonomous."
learning_goal: "Мягкие сенсоры + AI-formulation; Pfizer Vox forward-link к §4"
learning_outcomes: [LO1a, LO7]
chapter_ref: "§3.1 мягкие сенсоры"
references: [basf-geismar-2024, pfizer-vox-2024, aws-bedrock-pfizer]
visual:
  pattern: two_cases_with_diagram
  primary: "BASF reactor photo + Pfizer pharma plant photo; центр — soft sensor schematic"
---

# Мягкие сенсоры: BASF + Pfizer Vox

## BASF Geismar (Louisiana, 2023–2024)

**Мягкие сенсоры** дают real-time оценку quality parameters без physical lab samples.

**–30% batch defects** без увеличения тестирования.

**R&D formulation 18 мес → 3 недели** для определённых классов соединений.

## Pfizer Vox (2024–2025)

GenAI на AWS Bedrock + SageMaker.

Identify «golden batch» parameters в mRNA-вакцинах; detect anomalies; **recommend actions to operators**.

**+20 000 vaccine doses per batch.**

**Ключевое:** «recommend», не autonomous. Consistent с FDA Part 11 — оператор подписывает release.

## Что такое мягкий сенсор

Программная модель, которая оценивает **труднo-измеряемые** параметры (вязкость продукта, концентрация активного компонента, плотность) по **легко-измеряемым** (температура, давление, расход, спектроскопические данные).

Это **input substitute** для дорогой / медленной лабораторной пробы — но не контроллер процесса.

## Forward-link к §4

Pfizer Vox станет worked example в §4 — мы проходим его через 5-step framework.

## Speaker notes

Процессное производство имеет свою фундаментальную концепцию — мягкий сенсор. Запомните: soft sensor — это программная модель, которая оценивает truдно-измеряемые параметры качества по легко-измеряемым входам. Вместо того, чтобы взять физическую пробу из реактора и отправить в лабораторию на 4 часа, мы используем модель на температуре, давлении, расходе, спектроскопических данных — и получаем оценку вязкости или концентрации в реальном времени.

BASF Geismar в Луизиане развернул мягкие сенсоры на реакторах в 2023-2024 году. Результат: 30 процентов снижение batch defects без увеличения тестирования. И параллельно — R&D formulation для определённых классов соединений: 18 месяцев → 3 недели. Это огромное ускорение в формулировании, и оно работает потому, что мягкий сенсор не пытается заменить контроллер, он заменяет лабораторную пробу.

Pfizer Vox — это, пожалуй, самый интересный кейс в процессном AI для нашей лекции. Запустили в 2024-2025 году на AWS Bedrock + SageMaker. Задачи: идентифицировать «golden batch» parameters для mRNA-вакцин; детектировать аномалии в текущем batch; и рекомендовать действия оператору. Результат: 20 тысяч дополнительных доз вакцины на batch.

Я хочу, чтобы вы заметили формулировку. Pfizer не говорит «AI управляет batch process». Pfizer говорит «AI recommends actions to operators». Это не риторика — это архитектура. Vox работает в режиме recommend, не autonomous. Оператор смотрит рекомендацию, оценивает, принимает решение, подписывает действие. Это consistent с FDA Part 11 — оператор подписывает release, не AI.

Если бы Pfizer развернул Vox как autonomous controller — без human-in-the-loop — FDA не выпустила бы продукт. Audit trail не работает для black-box ML, мы это разберём через два слайда на регуляторных блокерах.

Pfizer Vox мы возьмём в §4 как worked example: пройдём его через 5-step framework, и покажем, как именно эта рамка работает на реальном кейсе. Запомните этот forward-link.
