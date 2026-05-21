---
id: s14
type: assertion_visual
duration_min: 2.5
assertion: "CV-инспекция работает в production: BMW GenAI4Q, TSMC 95% accuracy, Boeing fuselage 2025."
learning_goal: "Discrete production CV cases с эталонной разметкой как cornerstone"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§2.1 CV-инспекция"
references: [bmw-genai4q-2025, tsmc-defect-detection, boeing-cv-fuselage-2025]
visual:
  pattern: three_cases_grid
  primary: "3 карточки реальных кейсов с фото линий BMW / TSMC fab / Boeing 737"
---

# CV-инспекция в production — три рабочих кейса

## BMW GenAI4Q (Regensburg, 2025)

Bespoke inspection catalogue per vehicle — каждый автомобиль на сборке имеет свой набор checkpoints.

**«FACTORY OF THE YEAR 2024».** Развёрнуто на BMW Plant Regensburg.

Партнёр: Datagon AI.

## TSMC wafer defect detection

**95% accuracy** на классификации дефектов wafers.

**+10–15% yield improvement** — на high-volume fab это сотни миллионов долларов.

Применяется на 5nm и 3nm узлах.

## Boeing 737 fuselage (декабрь 2025)

CV-инспекция критических зон fuselage, photo-driven part validation на сборочных операциях.

Развёрнуто после кризиса door-plug января 2024 (s15).

## Что общее

Все три кейса требуют **эталонной разметки** — размеченные экспертами примеры дефектов / правильных конфигураций. Класс defect rate 1–2% означает class imbalance: модель надо тренировать на большом объёме нормальных примеров и сравнительно скудных дефектов.

## Speaker notes

Дискретное производство — это та область, где компьютерное зрение для контроля качества действительно работает в production уже сегодня. Три рабочих кейса.

BMW Plant Regensburg в 2024 году получил премию «Factory of the Year». В 2025 году они развернули GenAI4Q — bespoke inspection catalogue, где каждый автомобиль на сборочной линии имеет свой собственный набор checkpoints в зависимости от конфигурации. Если клиент заказал спортивный пакет — это другие точки контроля. Это уже не universal computer vision, это GenAI, который генерирует план инспекции под конкретный билд. Партнёр — Datagon AI.

TSMC, тайваньский производитель чипов, использует CV для wafer defect detection на 5nm и 3nm узлах. Accuracy — 95 процентов на классификации дефектов. Yield improvement — 10-15 процентов. На high-volume fab, который производит миллионы wafers в год, 10-15 процентов yield — это сотни миллионов долларов чистой прибыли. Это самый зрелый сегмент CV в производстве — wafer inspection полупроводников.

Boeing после кризиса январь 2024 — мы про него на следующем слайде — начал в декабре 2025 разворачивать CV-инспекцию критических зон fuselage 737. Photo-driven part validation: фотография части → AI сверяет с CAD-моделью → flag отклонений. Это не замена ручной инспекции, это дополнительный слой.

Что общее у всех трёх кейсов — эталонная разметка. Это та самая ground truth, размеченные экспертами примеры дефектов и правильных конфигураций, на которых учится модель. И вот здесь проблема: defect rate в normal production — 1-2 процента. Class imbalance: модель надо тренировать на десятках тысяч нормальных примеров и сравнительно скудных дефектах. Чем редкая аномалия, тем хуже модель её ловит. Это структурное ограничение, и на следующем слайде мы увидим, как оно проявилось в Boeing 737.
