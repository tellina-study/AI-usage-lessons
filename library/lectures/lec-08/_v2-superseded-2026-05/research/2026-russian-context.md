# Russian Creative AI Context — 2026-05-20

Сжатый research для Лекции 8 §4.5 «Russian context» (1 слайд). Tone: нейтральный. Все цифры — со ссылками; volatile / spec-detail помечены `[VFY-day-of]`.

---

## Изображения

### Sber Kandinsky

- **Актуальные версии (на 2026-05-20):**
  - **Kandinsky 6.0 Image** — flagship, анонс 28 апреля 2026. Архитектура Mixture-of-Experts (MoE); работает «до двух раз быстрее» предыдущих версий, новые функции: реставрация, нейрофотосессии, смена одежды и локаций, ретушь и макияж. Бесплатный доступ через ассистент GigaChat без лимита генераций. [`[VFY-day-of]`: точные бенчмарки vs MJ v7/v8] [SHADR](https://www.shadr.info/news/2026/04/29/36773-sber_predstavil_kandinsky_60_image_flagmanskuyu_model_dlya_/), [4PDA](https://4pda.to/2026/04/28/455813/).
  - **Kandinsky 5.0 Video** (релиз 18 ноября 2025) — открытые веса под Apache 2.0; Video Lite 2B и Video Pro 19B; до 10 секунд 24 fps; Video Lite декларирует #1 среди open-source моделей своего класса по «пониманию русских концептов». [GitHub kandinskylab](https://github.com/kandinskylab/kandinsky-5), [aifilms studio](https://studio.aifilms.ai/blog/kandinsky-5-video-generation).
- **Adoption:** в марте 2024 совокупная аудитория GigaChat + Kandinsky достигла 18 млн пользователей (Сбер). [`[VFY-day-of]`: цифры за 2026 не опубликованы публично]. Доступ через `fusionbrain.ai`, GigaChat, GigaChat API; FusionBrain — ~106k visits/мес в Q1 2026, 89% — RU-трафик. [`[VFY-day-of]`].
- **Capability gap:** объективные head-to-head c Midjourney v7+ / DALL-E 4 в открытых независимых бенчмарках отсутствуют — все сравнения исходят из релиз-материалов Sber. На 2026-05-20 это не подтверждено независимо.

### Yandex Шедеврум

- **Актуальная версия:** для изображений — YandexART 2.7 / гибрид 3.0 (beta, февраль 2026). Видео-генерация — 4 модели (v.1 / v.2 Beta / v.3 / Wan 2.2 от Alibaba); v.3 — самая детализированная, 4 секунды × 24 fps, форматы 16:9 / 9:16 / 1:1; гибрид 3.0 декларирует 5-секундные ролики с «физически корректным движением». [`[VFY-day-of]`]. [vc.ru обзор](https://vc.ru/aihub/2842605-shedrevum-ot-yandeks-vozmozhnosti-nevrosseti), [Yandex Support](https://yandex.ru/support/shedevrum/ru/video/create).
- **Доступ:** iOS + Android + web, бесплатно без VPN из РФ; с 3 марта 2026 — API через Yandex Cloud + AI Studio (стартовые гранты, промокоды, free-trial).
- **Adoption:** публичных метрик MAU/downloads за 2026 в открытом доступе не найдено на 2026-05-20.

---

## Музыка / звук

- **Sber SymFormer (Маэстро):** генератор музыки на базе архитектуры Performer, обучен на 160k композиций; результат — mp3 за <1 минуту, через ассистентов «Салют» и «Звук Студио». Sber выпустил с её помощью альбом «Thriving Machine» (15 треков) под open license. Уровень — entry-level vs Suno v5 / Udio v2 (длительность короче, вокал ограниченный). [Sber Developers](https://developers.sber.ru/portal/products/symformer), [Хабр Sber](https://habr.com/ru/companies/sberdevices/articles/826118/).
- **Прямого RU-конкурента Suno уровня v5 нет.** Российские «решения» — это **агрегаторы-прокси** (GPTunneL, Chad AI, GenAPI, Sonata-бот) с оплатой в рублях, обёрнутые поверх Suno API. [Хабр TOP-músic](https://habr.com/ru/companies/era2/articles/1037070/), [vc.ru](https://vc.ru/toprate/2680250-luchshie-analogi-suno-ai-dlya-sozdaniya-muzyki).
- **Голос (TTS/voice cloning):** **Sber SaluteSpeech** (YourVoice — клонирование от нескольких часов аудио; VoiceCloning — секунды; SSML, RU/KZ/EN) и **Yandex SpeechKit** — функциональные TTS, но эмоциональная выразительность и «character voices» уступают ElevenLabs v3. [Sber Developers SaluteSpeech](https://developers.sber.ru/portal/products/smartspeech-yourvoice).

---

## Видео

- **Отечественный production-ready text-to-video в РФ на 2026-05-20 — Kandinsky 5.0 Video (open-source, до 10 сек, 768×512)** и **Шедеврум видео v.3 / Hybrid 3.0 (до 4-5 сек)**. Прямой конкурент Sora 2 Pro / Veo 3 / Kling 2.6 по длительности (15-60 сек), разрешению (1080p+), физике и аудио-синху **не подтверждается** на 2026-05-20. Объяснение: фронтир-видео-модели требуют capex (десятки тысяч GPU-часов в кластере) и доступа к большим видео-датасетам — концентрация в US (OpenAI, Google DeepMind, Runway) и Китае (Kuaishou Kling, MiniMax Hailuo, Alibaba Wan). [Habr](https://habr.com/ru/companies/studyai/articles/1026652/), [Sostav Top-15](https://www.sostav.ru/blogs/287107/77059).

---

## Copyright / правовое поле

- **Минцифры законопроект 18 марта 2026** — «Об основах государственного регулирования сфер применения технологий ИИ». Общественное обсуждение до 15 апреля 2026; план вступления в силу — 1 сентября 2027. Ключевое для медиа: (1) **TDM-exception** — обучение моделей на правомерно полученных опубликованных произведениях не нарушение; (2) **обязательная маркировка** ИИ-сгенерированного фото/видео/аудио; (3) **авторство** на ИИ-результат — у пользователя промпта, внёсшего творческий вклад. [РИА Право](https://riapravo.ru/intellekt/avtorskoe-pravo-i-ii-v-2026-godu-revoljuciya-zakonodatelstva-i-novye-riski/), [CNews 12.03.2026](https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat), [vc.ru legal](https://vc.ru/legal/2847664-regulirovanie-ii-v-rossii-novyy-zakon-o-intellektualnoy-sobstvennosti).
- **Landmark RU-cases против Kandinsky / Шедеврум по training data**: на 2026-05-20 публично не подтверждено (англо- и русскоязычные источники не показывают аналога Getty-vs-Stability / NYT-vs-OpenAI). Иски возможны после 1 сентября 2027 — после введения чёткого правового режима.

---

## Урок для лекции (1-2 предложения)

**RU GenAI для медиа в 2026 — это «local convenience» (бесплатность, RU-промпты, без VPN, оплата в рублях, GigaChat-интеграция), но НЕ frontier-quality.** Где задача — быстрый masstige-контент или маркетинговый visual на русском с гарантированным юридическим контуром — Kandinsky 6.0 / Шедеврум конкурентоспособны; где нужны cinematic video, профессиональный вокал, character consistency — выбор остаётся за Midjourney / Sora 2 / Suno, и это сам по себе **honest takeaway**: концентрация фронтир-R&D в US/CN — структурное, не идеологическое.

---

## Sources

- [Sber пресс-релиз Kandinsky 6.0 Image — sbersbusiness.live](https://sberbusiness.live/news/sber-predstavil-kandinsky-60-image)
- [SHADR — Kandinsky 6.0 Image, 29.04.2026](https://www.shadr.info/news/2026/04/29/36773-sber_predstavil_kandinsky_60_image_flagmanskuyu_model_dlya_/)
- [4PDA — Kandinsky 6.0 Image, 28.04.2026](https://4pda.to/2026/04/28/455813/sber_provyol_masshtabnoe_obnovlenie_generatora_izobrazhenij_kandinsky_6_0_image/)
- [GitHub kandinskylab/kandinsky-5](https://github.com/kandinskylab/kandinsky-5)
- [aifilms.ai studio — Kandinsky 5.0 Video разбор](https://studio.aifilms.ai/blog/kandinsky-5-video-generation)
- [Sber Developers — SymFormer](https://developers.sber.ru/portal/products/symformer)
- [Sber Developers — SaluteSpeech YourVoice](https://developers.sber.ru/portal/products/smartspeech-yourvoice)
- [Yandex Support — создание видео в Шедевруме](https://yandex.ru/support/shedevrum/ru/video/create)
- [vc.ru — Шедеврум обзор 2026](https://vc.ru/aihub/2842605-shedrevum-ot-yandeks-vozmozhnosti-nevrosseti)
- [vc.ru — Шедеврум генерация видео 2026](https://vc.ru/aihub/2842848-shedrevum-generatsiya-video)
- [CNews 12.03.2026 — обучение ИИ на авторских материалах](https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat)
- [РИА Право — ИИ-контент и авторские права 2026](https://riapravo.ru/intellekt/avtorskoe-pravo-i-ii-v-2026-godu-revoljuciya-zakonodatelstva-i-novye-riski/)
- [vc.ru legal — проект федерального закона об ИИ 2026](https://vc.ru/legal/2847664-regulirovanie-ii-v-rossii-novyy-zakon-o-intellektualnoy-sobstvennosti)
- [Habr studyai — аналоги Sora 2 / доступ для РФ](https://habr.com/ru/companies/studyai/articles/1026652/)
- [Sostav — TOP-15 нейросетей для видео 2026](https://www.sostav.ru/blogs/287107/77059)
