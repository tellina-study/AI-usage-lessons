---
id: s10a
type: assertion_visual
duration_min: 2
assertion: "российский GenAI — локальное удобство (бесплатно, RU-промпты, без VPN, рубли), но НЕ frontier-уровень в видео и музыке. Концентрация R&D в US/CN — структурное, не идеологическое."
learning_goal: "Russian context: Kandinsky 6.0, Шедеврум, SymFormer, SaluteSpeech, Минцифры законопроект"
learning_outcomes: [LO1, LO2, LO5]
chapter_ref: "§1.6 — Russian context"
references: [kandinsky-6-sber, sheddev-yandex, symformer-sber, cnews-mincifry]
visual:
  pattern: matrix
  primary: "Side-by-side: Kandinsky 5.0 Video sample frame vs Kling 3.0 sample frame + 4-card RU landscape (image/video/audio/legal)"
  backup: assets/backup/s10a-russian-vs-frontier.png
---

# Российский контекст: локальное удобство vs frontier

## Assertion

российский GenAI — локальное удобство (бесплатно, RU-промпты, без VPN, рубли), но НЕ frontier-уровень в видео и музыке. Концентрация R&D в US/CN — структурное, не идеологическое.

## Visual

Сверху assertion 22pt (более узкий формат). Слева — side-by-side comparison: Kandinsky 5.0 Video sample frame (768×512, 10 сек) и Kling 3.0 sample frame (4K, 60 fps) с visible quality gap. Справа — 4 Ocean rounded boxes по 4 областям: Изображения (Kandinsky 6.0 Image MoE, бесплатно через GigaChat + YandexART 2.7 / Шедеврум hybrid 3.0); Видео (Kandinsky 5.0 Video Apache 2.0 — frontier gap); Аудио (Sber SymFormer, SaluteSpeech VoiceCloning, Yandex SpeechKit); Legal (Минцифры законопроект 18.03.2026 — TDM-exception, маркировка, авторство у промпт-пользователя, в силу с 01.09.2027). Внизу gold-tint anchor: «Структурное (capex GPU, видео-датасеты), не идеологическое».

## Speaker notes

Российский ландшафт generative AI к 2026 году функционален, но не frontier по большинству областей. По изображениям. Sber Kandinsky 6.0 Image анонсирован двадцать восьмого апреля 2026 года. Архитектурно — Mixture-of-Experts. Работает по заявлению Сбера до двух раз быстрее предыдущих версий. Бесплатный доступ через ассистент GigaChat без лимита генераций. Kandinsky 5.0 Video — релиз ноября 2025, открытые веса под Apache 2.0, до десяти секунд при 24 fps, разрешение 768 на 512. Yandex Шедеврум — YandexART 2.7 и гибрид 3.0 beta февраля 2026, бесплатно из РФ без VPN. По видео — frontier gap. Прямого конкурента Sora 2 Pro, Veo 3.1, Kling 3.0 по длительности, разрешению, физике и audio-синху в РФ к моменту лекции не подтверждается. Объяснение структурное, не идеологическое: фронтир-видео-модели требуют capex — десятки тысяч GPU-часов в кластере — и доступа к большим лицензированным видео-датасетам. Концентрация R&D — в США и Китае. Это объективное распределение capex и data access на 2026 год. По музыке и звуку. Sber SymFormer — entry-level vs Suno v5.5; российские «решения» — это агрегаторы-прокси типа GPTunneL, Chad AI, GenAPI, обёрнутые поверх Suno API. То есть RU-аудитория всё равно потребляет западный frontier через локальные wrapper'ы. Sber SaluteSpeech YourVoice — клонирование голоса от нескольких часов аудио, в отличие от ElevenLabs с одной минутой. По legal — Минцифры законопроект восемнадцатого марта 2026 года: TDM-exception для обучения, обязательная маркировка AI-контента, авторство у промпт-пользователя при творческом вкладе, план вступления в силу — первое сентября 2027. Урок для инженера: российский GenAI для медиа в 2026 — это локальное удобство: бесплатность, RU-промпты, доступ без VPN, оплата в рублях. Но не frontier-уровень в видео и музыке. Где задача — быстрый масс-маркет премиум-контент на русском с гарантированным правовым контуром — Kandinsky и Шедеврум конкурентоспособны; где нужны cinematic video, профессиональный вокал — выбор остаётся за Sora и Suno.
