---
id: s07
type: data_chart
duration_min: 2
assertion: "За 10 лет — от ~6 до 1 451 AI-устройств в FDA-list. Это инфраструктура, не футурология."
learning_goal: "Quantitative evidence — exponential growth FDA AI/ML adoption"
learning_outcomes: [LO1]
frame_mapping: ["Другой AI", "Безопасность"]
chapter_ref: "§1.2 — Масштаб: FDA-одобренные устройства и mosmed.ai"
references: [fda-aiml-list-2025, jama-network-open-2025, imaging-wire-2025]
visual:
  pattern: timeline
  primary: "Большой bar chart с timeline overlay 2015→2025 (рост к 1,451 cumulative); pivot 2022–2024 acceleration выделен gold; caption «76% — радиология»"
  illustration:
    type: data_chart
    sources:
      - "FDA AI/ML-Enabled Medical Devices List — https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices"
      - "The Imaging Wire (Dec 10, 2025) — https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/"
      - "JAMA Network Open systematic review (2025) — https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841066 (76% radiology)"
    caption: "FDA AI/ML-enabled Medical Devices list, end-2025 (1,451 cumulative)"
interaction: none
---

# За 10 лет — от 6 до 1 451 AI-устройств в FDA-list

## Assertion

За 10 лет — от ~6 до 1 451 AI-устройств в FDA-list. Это инфраструктура, не футурология.

## Visual

Большой bar chart занимает ~70% ширины слайда в Ocean rounded box. Ось X — годы (2015, 2018, 2020, 2022, 2024, 2025). Столбики растут от ~6 (2015) до ~14 (2018) → ~64 (2020) → ~221 (2022 new) → 258 new в 2024 (cumulative 1 193) → 295 new в 2025 (cumulative 1 451). Маркеры cumulative 1 193 и 1 451 — большие gold-dots. Pivot-зона 2022–2024 (exponential acceleration) выделена светло-Surface полосой. Под графиком caption (12pt italic): «76% — радиология; остальное — кардиология, неврология, прочее». Справа в узкой колонке — assertion 24pt bold deep.

## Speaker notes

Десятилетняя динамика FDA-одобрений AI и ML-медицинских устройств — это самая прозрачная картина зрелости поля, доступная инженеру в открытых данных. В 2015 году в списке FDA было примерно шесть AI/ML-устройств за год. Между 1995 и 2015 годами кумулятивно — около тридцати трёх устройств, то есть около трёх процентов от текущего объёма. К 2020 году годовой приток вырос до шестидесяти четырёх устройств. Перелом приходится на 2022–2024 годы: в 2023 одобрено около двухсот двадцати одного нового устройства, в 2024 — двести пятьдесят восемь, в 2025 — двести девяносто пять. Кумулятивно к концу 2025 года в списке тысяча четыреста пятьдесят одно AI/ML-устройство.

Два контекстных факта. Первое: около семидесяти шести процентов этих устройств относятся к радиологии — это computer vision для рентгена, КТ, МРТ, маммографии, ультразвука. Следующие по объёму специальности — кардиология и неврология; LLM-based устройства составляют единицы и пока редкость в FDA-списке. Второе: список FDA — публичный и обновляется примерно поквартально. Любой инженер может проверить статус конкретного устройства по идентификатору 510(k) или De Novo.

«Тысяча четыреста пятьдесят один» — это не «AI в каждой клинике» и не «AI заменил рентгенологов». Это означает, что AI-диагностика перешла из стадии лабораторного эксперимента в стадию производственной инфраструктуры — и именно поэтому методические и регуляторные практики, о которых пойдёт речь в следующих разделах, становятся профессионально обязательными.
