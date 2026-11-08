---
id: s10
type: assertion_visual
duration_min: 1.5
assertion: "Genie 3 (DeepMind, 29.01.2026) — text → playable 3D world @ 24 fps. Это не видеогенерация — это симулированное окружение."
learning_goal: "World models — другой класс инструмента"
learning_outcomes: [LO1, LO2]
chapter_ref: "§1.4 — World models — Genie 3"
references: [genie-3-deepmind, wavespeed-genie-3]
visual:
  pattern: assertion_visual
  primary: "Genie 3 demo frame + QR + caption «не видеогенерация — симулированное окружение»"
  backup: assets/backup/s10-genie3.png
---

# World models — Genie 3

## Assertion

Genie 3 (DeepMind, 29.01.2026) — text → playable 3D world @ 24 fps. Это не видеогенерация — это симулированное окружение.

## Visual

Сверху assertion 26pt. Слева — Ocean rounded box с Genie 3 demo frame (snapshot из DeepMind blog поста, мокап playable world). Под frame — QR на deepmind.google/blog/genie-3-a-new-frontier-for-world-models/. Справа — 3 metric chips: «text → playable 3D», «24 fps real-time», «720p, мин. consistency». Под chips — gold-tint anti-hype block: «Не видеогенератор. Production — пока граничные случаи (игровой прототип, разведка локаций). Frontier — впереди».

## Speaker notes

Google DeepMind Genie 3 — публичный релиз двадцать девятого января 2026 года — представляет собой другой класс инструмента, который часто ошибочно сравнивают с видеогенерацияerators. Что делает Genie 3: из текстового промпта — например, «средневековый замок на горе, день, лёгкий ветер» — модель генерирует playable 3D world. Это explorable, navigable среда в режиме реального времени при двадцати четырёх кадрах в секунду, разрешение 720p, consistency сохраняется в течение нескольких минут. Это не sequence пред-определённых кадров, как у Sora или Veo или Runway — это интерактивная среда, реагирующая на действия пользователя: камера, движение, манипуляция объектами. Архитектурно Genie 3 — это совмещение latent diffusion для visual generation с world-model-частью, которая обрабатывает state transitions. Доступ — для US-подписчиков Google AI Ultra. Anti-hype: Genie 3 — не video генератор. Это симулированное окружение генератор. Прямое production в креативных индустриях пока граничные случаи. Пара game-studios экспериментирует с Genie 3 для prototyping levels. Пара film-studios — для разведка локаций, генерировать virtual location вместо travel'а к real location. Образовательный сектор — для immersive learning environments. Frontier-grade использование в production — впереди, по оценкам индустриальных аналитиков. Genie 3 — это пример симбиоза нескольких архитектур в одном AI-system: latent diffusion как Sora плюс reinforcement-learning state model как игровой AI плюс transformer для language understanding. Это иллюстрирует тезис: AI-системы 2026 года — это композитные архитектуры, не monolithic models.
