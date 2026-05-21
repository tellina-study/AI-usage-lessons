---
id: s12
type: assertion_visual
duration_min: 2
assertion: "Predictive maintenance: Rolls-Royce IntelligentEngine + Airbus Skywise. ~11 600 ВС подключены к Skywise; ~400 предотвращённых событий в год у Rolls-Royce."
learning_goal: "Predictive maintenance — массовая гражданская AI-инфраструктура"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§1.4 — Predictive maintenance"
references: [airbus-2024-skywise, klover-2024-rr, cio-2024-rr]
visual:
  pattern: data_chart
  primary: "QuickChart bar + 2 sidebar metrics + Skywise context"
---

# Predictive maintenance — массовая гражданская AI-инфраструктура

## Assertion

Predictive maintenance: Rolls-Royce IntelligentEngine + Airbus Skywise. ~11 600 ВС подключены к Skywise; ~400 предотвращённых событий в год у Rolls-Royce.

## Visual

Под assertion — 2 колонки.

Слева (55%): QuickChart horizontal bar chart в Ocean rounded box. Категории: «Skywise (Airbus, конец 2024)» — 11 600 (gold); «Skywise SFP+ (расширенная подписка)» — 1 500. Axis label: «Воздушных судов подключено». Caption под графиком: «easyJet: 8,1 тонны топлива/ВС/год сэкономлено; 44 предотвращённые отмены — июль 2024».

Справа (45%): 2 stacked info-card:

**Rolls-Royce IntelligentEngine**
- Работает с 2018
- Digital twin каждого летающего двигателя
- Azure → Databricks → ML pipelines
- ~400 непланированных событий предотвращены / год (gold)

**Стек публичный**
- Microsoft Azure data lake
- Databricks lakehouse
- ML pipelines

Внизу — caption 12pt italic: «В обороне аналог — F-35 ALIS → ODIN. Об этом — следующий слайд».

## Speaker notes

Помимо разведки, AI в Sense массово работает на собственных аппаратах. Predictive maintenance — это семейство задач: по телеметрии двигателей, систем, бортового оборудования предсказать отказ компонента до того, как он случится, и заменить его на плановом обслуживании, а не на аварийной посадке.

Rolls-Royce IntelligentEngine плюс TotalCare работает с 2018 года и сейчас представляет собой digital twin каждого летающего двигателя плюс ML-конвейеры на телеметрии. Стек публичный: Microsoft Azure data lake, поверх него Databricks lakehouse, далее ML pipelines. Главная метрика — около 400 непланированных событий обслуживания предотвращаются в год на флоте, что транслируется в миллионы евро экономии.

Airbus Skywise — более широкая платформа: ML-сервисы для авиакомпаний, прогнозирующие отказы компонентов на разных типах воздушных судов. К концу 2024 года к платформе подключены около 11 600 самолётов; около 40 авиакомпаний на расширенной подписке SFP+, что покрывает около 1 500 ВС. easyJet с использованием Skywise сообщил об экономии топлива около 8,1 тонны на воздушное судно в год и о 44 предотвращённых отменах рейсов в июле 2024 года.

Что важно для нашего инженерного слуха: это не пилот, это не лаборатория, это рабочая инфраструктура, которая обслуживает каждый день тысячи коммерческих самолётов. Predictive maintenance — это самый массовый успех AI в Sense, и он работает там, где выполнены три условия: быстрый feedback loop, доступная ground truth, FP-цена терпимая.

В оборонном секторе аналог — F-35 ALIS, Autonomic Logistics Information System, и его преемник ODIN. О том, почему ALIS не сработал как задумывалось — отдельный разговор на следующем слайде. Скажу заранее: ALIS нарушил все три условия predictive maintenance, и это поучительный contrast к Skywise.
