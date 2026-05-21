---
id: s38
type: qa
duration_min: 1
assertion: "Q&A — 10 минут. Backup-вопросы про термодинамику vertical farming, agentic AI scope, ИТЭЛМА vs Cognitive Pilot, foundation models к 2030."
learning_goal: "Dedicated Q&A slide с 3 backup-prompts"
learning_outcomes: []
chapter_ref: "Q&A backup + §9 Часть 3"
references: []
visual:
  pattern: cover_distinct_qa
  primary: "Огромное Q&A typography + Lucide message-circle-question icon + 3 backup-prompts мелким снизу"
---

# Q&A

## Assertion

Q&A.

## Visual

Главная композиция — огромный заголовок «Q&A?» по центру 120pt bold Primary deep, под ним — иконка `message-circle-question` Lucide 96px Primary mid.

Под этим — 3 backup-prompts в горизонтальную строку Ocean rounded box (мелким шрифтом 14pt italic Primary light, как подсказки для лектора и студента):

1. **«Vertical farming — Oishii выжила и привлекла $150M в 2026. Это исключение или поворот?»** (B7 главы)
2. **«ИТЭЛМА vs Cognitive Pilot — это правда замена или они решают разные задачи?»** (B6 главы)
3. **«Foundation models — насколько они доступны smallholders к 2030?»** (B14 главы)

Внизу — small course-contact card (~10pt italic Primary light) с курсом контакта.

## Speaker notes

Открываем Q&A. У меня в запасе три типичных вопроса, которые могут возникнуть — на случай, если зал молчит.

Первый — про vertical farming. «Oishii выжила и привлекла Series C на сто пятьдесят миллионов в мае 2026 года. Это исключение или поворот для категории?» Ответ короткий. Oishii — это исключение, подтверждающее правило, не reversal коллапса категории. Oishii продаёт премиум-клубнику по десять плюс долларов за упаковку в Whole Foods Нью-Йорка. Их unit-economics работают именно потому, что они не пытаются конкурировать с открытым полем по leafy greens. Tortuga AgTech, приобретённая Oishii в марте 2025-го, показала техническую успешность — пятьдесят процентов reduction в harvest expenses — но внутри коллапсировавшей категории. Это business-model lesson, не technical robotics lesson. Premium-сегмент в vertical farming может выживать; commodity leafy greens — нет, из-за термодинамики LED против free sunlight.

Второй — про Cognitive Pilot и ИТЭЛМА. «Это правда замена одного другим или они решают разные задачи?» Они решают разные задачи. Cognitive Pilot — это CV-стек, отвечающий на вопрос «что я вижу» — распознавание визуальных признаков в поле: кромка нескошенного, препятствия. ИТЭЛМА Квадро — это sensor-fusion-AI на multi-GNSS, отвечающий на вопрос «где я нахожусь» — точная навигация с точностью два-пять сантиметров. Правильное решение современного автономного комбайна — комбинация обоих: GNSS-навигация как primary плюс CV как secondary для нестандартных ситуаций. Сравнение «один лучше другого» — методически неверное. Это пример AP-два-а — архитектурный выбор внутри AI-домена.

Третий — про foundation models. «Насколько TerraMind и Prithvi-EO 2.0 доступны smallholders к 2030 году?» Ответ зависит от трёх факторов. Первый — compute. Дообучение foundation model требует значимого GPU-кластера. Для smallholders в Африке или Азии прямой доступ к H100 / A100 — нет. Альтернатива — fine-tune-as-a-service от крупных провайдеров. Второй — local data. Foundation model для агро неравномерно покрывает географии — США, ЕС, Бразилия перегружены данными; Африка южнее Сахары, Россия за пределами южных регионов — недопредставлены. Это означает, что дообучение требует local data collection — что для smallholders сложно без external partner. Третий — interface. Smallholder не работает с Hugging Face API; ему нужно мобильное приложение в национальном языке. Это значит, что между foundation model и фермером должен быть слой UX, который пока не создан. К 2030 году я ожидаю: foundation models станут доступны крупным AgTech-стартапам, обслуживающим smallholders через UX-слои (типа Plantix, но с RAG-grounded архитектурой); прямой доступ smallholders к моделям — нет.

Открыт для ваших вопросов.

## Источники

- Chapter v3.1 §9 Часть 3 — Q&A-бэкап.
