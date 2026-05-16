---
id: s24
type: assertion_visual
duration_min: 3
assertion: "Врач ставит диагноз. AI подсказывает. Ответственность — на враче. Vendor + regulator + operator — обеспечивают системные условия."
learning_goal: "4-actor responsibility framework — ответ на central question"
learning_outcomes: [LO3, LO8]
frame_mapping: ["Человек vs AI", "Безопасность"]
chapter_ref: "§4.6 — Кто отвечает за AI-ошибку: 4-actor framework"
references: [price-2019-stanford, gerke-2020-elsevier, eu-ai-act-2024-1689]
visual:
  pattern: quadrant
  primary: "2×2 quadrant (technical control × legal liability) с 4 actor cards (Врач / Operator / Vendor / Regulator); 1-word role + 1-line responsibility per card; central line ниже"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2×2 quadrant через PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `stethoscope` (Врач), `building-2` (Operator), `code` (Vendor), `gavel` (Regulator), 32px badge size, recolored к Primary mid"
      - "Reference paper: Price 2019 (U Michigan Law School)"
      - "Reference paper: Gerke 2020 (Penn State Dickinson Law)"
    caption: "4-actor responsibility framework (Price 2019, Gerke 2020)"
interaction: none
---

# Врач решает. AI подсказывает. Final responsibility undivided.

## Assertion

Врач ставит диагноз. AI подсказывает. Ответственность — на враче. Vendor + regulator + operator — обеспечивают системные условия.

## Visual

В верхней половине — большой 2×2 quadrant с осями. Ось X (горизонтальная): «technical control: low ↔ high», стрелка-направление справа. Ось Y (вертикальная): «legal liability: low ↔ high», стрелка вверх. Четыре actor cards, по одной в каждой ячейке: ВЕРХ-ПРАВО — `Врач` (иконка `stethoscope`, **gold highlight**): «Final diagnostic decision; AI = подсказка». ЦЕНТР-ПРАВО — `Operator` (иконка `building-2`): «Vendor selection + training + monitoring». ВЕРХ-ЦЕНТР — `Vendor` (иконка `code`): «Model design + safety claims + PCCP updates». ВЕРХ-ЛЕВО — `Regulator` (иконка `gavel`): «Approves + audits + revokes». Под quadrant — central line в большом Ocean rounded box 24pt bold: «Врач ставит диагноз. AI подсказывает. Final clinical responsibility undivided».

## Speaker notes

Это центральная секция для центрального вопроса лекции. Мы прошли половину пути: AI-диагностика работает, mosmed.ai тому пример; drug discovery частично работает, Rentosertib и DSP-1181 — две стороны одной медали; bias и LLM анти-паттерны реальны. Теперь — кто отвечает, когда AI ошибается. Применяем 4-actor framework: Price 2019 (U Michigan Law School) и Gerke 2020 (Penn State Dickinson Law) — основа 4-actor framework. Ответственность распределяется между четырьмя акторами с разной комбинацией technical control × legal liability.

Врач — высокий control и высокая liability. Ставит финальный диагноз. AI — это input, не decision-maker. С юридической точки зрения врач остаётся primary responsible person; AI-suggestion — это «второе мнение», не decision. Это не punitive distribution: только врач имеет full context — анамнез, осмотр, лабораторные результаты, AI-output как один из inputs; никакой другой actor этого full context не имеет.

Healthcare operator — больница, клиника, ДЗМ. Средний control и средняя liability. Выбирает поставщика AI, обеспечивает training персонала, мониторит работу системы в production. Если operator деплоит AI без adequate тренинга врачей — несёт ответственность за foreseeable misuse.

AI-vendor — высокий control, низкая-средняя liability. Дизайнит модель, делает safety claims при FDA / EU / Росздравнадзор-регистрации, обеспечивает PCCP-updates. Если model design имеет defect — vendor несёт liability по product liability. При faithful disclosure ограничений и proper post-market surveillance liability ограничена.

Regulator — FDA, EU Notified Bodies, Росздравнадзор. Низкий control, высокий oversight. Approves системы, проводит post-market surveillance, может revoke authorization. Не несёт liability за individual cases, но несёт systemic responsibility за качество approval process. Central principle: финальная клиническая ответственность не делится между человеком и алгоритмом. Врач ставит диагноз. AI подсказывает. Это юридический консенсус во всех трёх крупных юрисдикциях. Если работаете в AI-vendor роли, ваша responsibility — design AI так, чтобы врач мог выполнить свою responsibility. Эти три инженерных принципа войдут в финальный takeaway на следующем слайде.
