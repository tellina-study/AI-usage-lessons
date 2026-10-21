---
id: s04
type: poll_reveal
duration_min: 2
assertion: "AI в медицине — уже не «будущее», а production-инфраструктура: 1 451 FDA-устройств и 14 млн исследований mosmed.ai."
learning_goal: "Раскрыть FDA cumulative + mosmed operational metrics"
learning_outcomes: [LO1]
frame_mapping: ["Другой AI", "Безопасность"]
chapter_ref: "§0.2 — Опрос и оценка читателя; §1.2 — Масштаб"
references: [fda-aiml-list-2025, imaging-wire-2025, mos-ru-2025, remedium-2025]
visual:
  pattern: chart
  primary: "Bar chart FDA AI/ML devices 2015→2025 (рост к 1,451 cumulative) слева в Ocean rounded box + info-card mosmed.ai operational metrics справа"
  illustration:
    type: data_chart
    sources:
      - "FDA AI/ML-Enabled Medical Devices List — https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices (verified 1,451 end-2025)"
      - "The Imaging Wire (Dec 2025) — https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/"
      - "Remedium (2025) — https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/ (mosmed 14M+ исследований)"
      - "mos.ru AI Leaders Award — https://www.mos.ru/en/news/item/147773073/ (74 региона, federal launch май 2024)"
    caption: "FDA list end-2025 + mosmed.ai 5-year operational stats"
interaction: none
paired_with: s03
---

# AI в медицине — уже не «будущее», а production-инфраструктура

## Assertion

AI в медицине — уже не «будущее», а production-инфраструктура: 1 451 FDA-устройств и 14 млн исследований mosmed.ai.

## Visual

Слева — bar chart роста FDA AI/ML-устройств с 2015 по 2025 год: столбики растут с ~6 в 2015 до 1 451 cumulative в конце 2025. Pivot-точки 2022–2024 (exponential acceleration) выделены gold-маркером на 2024 (1 193) и 2025 (1 451). Под графиком caption: «76% — радиология (CV-based)». Справа — info-card в Ocean rounded box: «mosmed.ai — 5 лет работы»; внутри 6 чисел крупно — `14M+ исследований`, `74 региона`, `2 000+ медорганизаций`, `18M+ изображений`, `70 AI-сервисов`, `11 нац. стандартов». Над всем слайдом — assertion в `#21295C`.

## Speaker notes

Ответы на первый вопрос. К концу 2025 года FDA авторизовало одну тысячу четыреста пятьдесят одно AI и ML-enabled medical device кумулятивно: двести пятьдесят восемь новых одобрений в 2024 году плюс двести девяносто пять новых в 2025. Примерно 76 процентов этих устройств относятся к радиологии — компьютерное зрение для рентгена, КТ, МРТ, маммографии, дерматологии. LLM в FDA-списке на 2026 год — единицы. Это и есть ответ на вопрос «что именно работает»: преимущественно computer vision для медицинских изображений.

В России операционный масштаб AI-диагностики тоже значителен. Платформа mosmed.ai, изначально запущенная как Московский эксперимент в ноябре 2019 года, за пять лет работы обработала более четырнадцати миллионов исследований; в мае 2024 года она получила федеральный запуск под названием MosMedAI и теперь покрывает семьдесят четыре региона России. К платформе подключено более двух тысяч медицинских организаций; на ней развёрнуто около семидесяти AI-сервисов на сорока трёх клинических областях, обработано более восемнадцати миллионов изображений, разработаны одиннадцать национальных стандартов.

Этот двойной сигнал — массовое внедрение в США и в России одновременно — показывает: AI в медицине перешёл из стадии лабораторного эксперимента в стадию производственной инфраструктуры. Но как мы увидим дальше, «production» не означает «решены все проблемы»; именно потому, что это масштаб, ошибки и злоупотребления тоже становятся массовыми.
