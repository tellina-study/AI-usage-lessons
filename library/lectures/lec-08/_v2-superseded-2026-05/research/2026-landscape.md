# Lec-08 Research Dossier: 2026 Creative AI Landscape
**Дата:** 2026-05-20
**Audience:** студенты-инженеры 3 курса МГТУ ИУ6 (универсальная, не дизайнеры)
**Лекция:** «AI в креативных индустриях и медиа» (75 мин)
**Keystone axis:** «Что AI ДОБАВИЛ → что AI ИЗМЕНИЛ → что AI СЛОМАЛ»

> **Соглашения:**
> - `[VFY-day-of]` — verify в день лекции (цены, версии, статусы исков, бенчмарки)
> - Stable facts (исторические инциденты, поданные дела) — без пометки
> - «to verify» — факт встречался в исследовании, но не подтвердился из надёжного источника

---

## A. Landscape по 4 областям

### A.1 Кино / видео / VFX

**Ключевые модели 2026:**

| Модель | Релиз | Длина | Разрешение | Цена API | Особенности |
|---|---|---|---|---|---|
| **OpenAI Sora 2** | сент 2026 | до 25 сек | 1080p, синх. аудио | $0.10/сек 720p; Pro $0.30–0.50/сек | character cameos, лицензия Disney; **standalone discontinued** март 2026 (по PCMag/RedShark) [VFY-day-of] |
| **Google Veo 3.1 / Lite** | 2026 | 4/6/8 сек | 720p/1080p, native audio | $0.05–0.40/видео | text-to-video + image-to-video, 16:9 и 9:16; Google AI Ultra $249.99/мес [VFY-day-of] |
| **Runway Gen-4 / Gen-4.5** | 2026 | до 60 сек | до 4K, temporal consistency | подписка | Motion Brush, Camera Control, Lip Sync, Director Mode; **Aleph in-video editor + Act-Two mocap** |
| **Kling 3.0 (Kuaishou)** | 4 фев 2026 | 15 сек | native 4K, 60 fps | подписка | **#1 ELO benchmark 1243** (выше Veo 3.1, Gen-4.5, Pika 2.2); 60M+ creators, 600M+ видео |
| Pika 2.2, Luma | 2026 | varies | varies | varies | партнёрские модели в Adobe Firefly |

**Adoption в production:**
- **Lionsgate × Runway**, сент 2024 — первый Hollywood-studio AI deal; custom-модель на корпусе студии, использование в **previsualization, storyboarding, post-prod backgrounds, VFX** уже подтверждено earnings call ноябрь 2024. Burns (Vice Chairman): экономия "millions and millions of dollars" на pre-/post-production.
- **Adobe Firefly** интегрировал 12 third-party моделей (Veo, Luma, Runway, Topaz) — выбор пользователя, мульти-модельный подход.
- **Sora 2 + Disney $1B partnership** — licensed character generation.
- **86% buyers** используют или планируют generative AI для video creative; **40% всех видеообъявлений 2026** — AI-сгенерированные (IAB 2026); **AI video ad spend $9.1B** глобально 2026.

**Бенчмарки:**
- Kling 3.0 — ELO 1243 (Video Arena #1, февраль 2026).
- Veo 3.1 Lite — 50% дешевле Veo 3.1 Fast при той же скорости.
- 22% video ad creative в 2024 → **39% в 2026** использовали GenAI; **75% маркетинговых видео** AI-generated или AI-assisted (2026).

### A.2 Музыка / звук

**Ключевые модели 2026:**

| Модель | Особенности | Статус |
|---|---|---|
| **Suno** (v5/современная) | Text-to-song, vocals + instrumental + lyrics | **Иск RIAA**, fair-use defence; summary judgment hearing **июль 2026** [VFY-day-of] |
| **Udio (Uncharted Labs)** | Аналог Suno, SDNY | **UMG settled окт 2025** (compensatory + licensing для joint AI music platform 2026); Warner license late 2025; **Sony — единственный major, продолжающий litigation** [VFY-day-of] |
| **Stable Audio 2** | Stability AI, open-weights возможны | стабильно |
| **ElevenLabs** (v3, Studio) | Voice cloning **из 1 минуты аудио**, 32+ языков, multilingual dubbing 29 языков | Deutsche Telekom, Klarna — enterprise агенты |

**Adoption:**
- **Universal × Udio** — joint AI music platform launching 2026 после settlement.
- ElevenLabs Dubbing Studio — production-ready локализация long-form video между любыми из 29 языков, сохраняя голос, тон, стиль оригинала.

**Бенчмарки/тесты качества:** не выявлены публичные head-to-head (Suno vs Udio) бенчмарки на уровне FID/MS-SSIM; качество оценивается через blind tests среди musicologists (to verify).

### A.3 Изображения / иллюстрация / дизайн

**Ключевые модели 2026:**

| Модель | Цена/image | Сильная сторона | Заметки |
|---|---|---|---|
| **Midjourney v7** + **v8** | $10–120/мес | Aesthetic quality, character consistency (Omni Reference), web interface | "King of AI art" по аналитикам; v7 видео-генерация |
| **DALL-E 4 / GPT Image 1.5** | $0.04–0.25/img | Text rendering ≥90% accuracy | в ChatGPT |
| **Imagen 4** (Google, апр 2026) | API tier | S-tier photorealism, **product photography** (стекло/металл/жидкости) | fastest |
| **Flux Pro 1.1 / Flux 2** | $0.03/img | Photorealism + text + anatomy, fine control | developer-friendly |
| **Adobe Firefly** (image/video/audio/vector unified) | в подписке | **Commercially safe**, обучен на Adobe Stock + licensed | **22B+ assets generated** к 2026; $400M direct revenue 2024–25 |
| **Stable Diffusion 3.5 / 4** | $0.003–0.008/img | Open-weights, on-prem | base для multiple downstream tools |

**Adoption metrics:**
- Firefly: **22 миллиарда** ассетов за <2 года; **3x QoQ growth** generation в Q4 FY2025.
- Enterprise users: Deloitte, Tapestry, Paramount+, Pepsi, dentsu, PepsiCo/Gatorade, Stagwell — production-ready video.
- Adobe Firefly Foundry (MAX 2025, Oct) — proprietary on-brand models на корпусе IP клиента.

### A.4 Текст / журналистика / геймдев / реклама

**Текст:**
- ChatGPT, Claude, Gemini — стандартный writer toolkit.
- **87% маркетологов** используют generative AI хотя бы в одном workflow (Salesforce State of Marketing 2026, рост с 51% в 2024).
- **78% маркетинговых команд** используют AI-video в ≥1 кампании/квартал.

**Реклама/маркетинг:**
- US digital video ad spend проектируется **>$80B в 2026** (+11% YoY, в 2× быстрее total ad market) — впервые **>60% всего TV/video ad spend**.
- **86% ad buyers** используют или планируют generative AI для creative.
- **40% всей видеорекламы 2026** — GenAI-creative (прогноз IAB).
- Глобальный AI video generator market: $716.8M в 2025 → $847M в 2026.

**Геймдев:**
- Concept art / textures / NPC dialogue — pervasive. См. Wizards of the Coast cases ниже как failure.

**Журналистика:**
- См. Sports Illustrated AI-fake-authors scandal (раздел D.3).

---

## B. «AI ДОБАВИЛ» — новые возможности (новое, чего раньше не было)

### B.1 Real-time / интерактивная генерация
- **Google DeepMind Genie 3** (публичный релиз 29 янв 2026) — **world model**: text prompt → playable 3D world, navigable real-time @24 fps, 720p, consistency несколько минут. Не video generator — это **simulated environment**. Доступ для Google AI Ultra US-subscribers.
- В отличие от Sora/Runway (pre-determined sequences) — Genie 3 строит explorable среду в ответ на действия пользователя.

### B.2 Character consistency (multi-shot persistence)
- **Midjourney Omni Reference** (v7) — стабильные character proportions через генерации.
- **Sora 2 cameos** — character появляется в нескольких scene'ах.
- **Runway Gen-4 Director Mode** — multi-scene scripts с consistent characters.

### B.3 Voice cloning + multilingual dubbing
- **ElevenLabs**: voice clone из 1 минуты аудио → говорит на 32+ языках сохраняя характеристики голоса.
- **Dubbing Studio**: 29 языков, между любой парой, сохраняет тон/delivery/voice. Long-form видео локализуется за минуты, не недели.
- Use case: глобальный support agent, voice-cloned на 30+ языков.

### B.4 Personalisation at scale
- Каждый клиент получает свой ролик/трек/изображение (e-commerce + ad targeting). См. IAB report: agentic AI для video campaigns — 21% live, 20% testing, 25% planning.

### B.5 Voice/style cloning из minimal sample
- Drake/Weeknd "Heart on My Sleeve" (Ghostwriter977, апр 2023) — **9M+ views за дни**, voice mimicry impeccable. Демонстрация: трек уровня commercial release не требует ни студии, ни артистов (см. также D.4).

### B.6 Workflow примеры (production today)
- **Concept art / pre-viz**: Lionsgate uses Runway для storyboards и pre-production designs.
- **Dubbing**: одна training video → офисы Tokyo/Berlin/Mumbai mинуты (ElevenLabs).
- **B-roll**: Veo 3 / Sora 2 для филлерных кадров вместо stock footage.
- **Product photography**: Imagen 4 для пакшотов (стекло/жидкости) — generation < $0.25/img vs $50–500 stock + $1k–5k freelance designer.

---

## C. «AI ИЗМЕНИЛ» — pipeline и экономика

### C.1 Удешевление: cost-per-asset before vs after

| Asset | До (human/stock) | AI |
|---|---|---|
| **Иллюстрация (1 image)** | $50–$200+ (freelance designer), $50–500 stock | **$0–$0.25** (AI generation) |
| **50 product lifestyle images** | $1k–$5k freelance / $5k–$25k photography / $50–$500 stock | **$0–$1.50** |
| **Минута 720p видео** | ($1k–$50k+ shoot + post) | **$6** (Sora 2 standard, 60s × $0.10) [VFY-day-of] |
| **Минута 4K видео** | (большой бюджет) | Kling 3.0 / Veo Ultra (subscription) [VFY-day-of] |
| **Dub минуты видео на 1 язык** | $50–$500 (voice actor + studio) | <$1 (ElevenLabs subscription) |

**Множитель:** AI generation **100×–10,000× дешевле** традиционных альтернатив (ZSky AI calc для типовых product images).

### C.2 Скорость
- Concept art draft: дни → секунды.
- B-roll кадр: часы съёмки → 5–60 сек prompt-to-pixel.
- Dub long-form видео: недели студии → минуты (ElevenLabs Dubbing Studio).

### C.3 Новые профессии
- **Prompt engineer / AI artist** — Fiverr/Upwork category существует.
- **AI director / AI music producer** — supervises model output, доводит до production-ready.
- **GenAI workflow specialist** — интегрирует AI tools в существующие pipelines студий.
- 5.6M independent workers US >$100k/yr в 2025 (vs 3M в 2020) — рост связан с AI-augmented specialists.
- **70% YoY рост** AI/ML subcategory на Upwork; **52% gross services volume growth** — AI-related.

### C.4 Старые профессии под удар
- **Graphic designers**: **−17.01%** jobs на Upwork после релиза GenAI image tools.
- **Stock photographers**: Shutterstock contributors с hundreds/мес → single digits/мес (microstock forums). Getty Creative segment −5% YoY 2024.
- **Voice actors**: SAG-AFTRA strike 2023 + ElevenLabs adoption → Korea/global voice actor displacement.
- **Junior designers / commodity freelancers**: AI detected в 40% работ writers $10–19/час vs <10% $60+/час — wage compression снизу.
- **B-roll camera operators**: stock footage market disrupted.
- **Concept artists**: indirect signal — Wizards of the Coast вынуждены публично запрещать AI у вендоров (январь 2024).

### C.5 Industry consolidation / responses
- **Getty + Shutterstock merger** объявлен январь 2025, $3.7B, ожидаемый $150–200M cost savings (3 года) — defensive против AI disruption.
- Shutterstock licensing к AI companies: **$104M в 2023 → $138M в 2024 → ~$250M прогноз 2027** — пивот с photographers на data licensing.
- Adobe Firefly Foundry — bespoke models на корпусе IP клиента (Adobe MAX 2025).

### C.6 Конкретные кейсы маркетинг-провалов AI-adoption
- **Coca-Cola "Holidays Are Coming"** (Christmas 2024) — три AI-студии (Secret Level, Silverside AI, Wild Card), 4 модели, **"soulless" backlash**. Coca-Cola **повторила** AI-ad в 2025 несмотря на критику.
- **Toys "R" Us Sora ad** (Cannes Lions 2024) — sentiment с **+12.2% positive → +3.4%; negative с 13.5% → 53.4%**. Joe Russo (Avengers: Endgame): "fucking sucks". Toys "R" Us: "successful test".
- **Late Show / Colbert finale**: 21 мая 2026 — не показал systematic generative AI segments в production [VFY-day-of].

---

## D. «AI СЛОМАЛ» — провалы, риски, юридические кейсы (≥30% контента!)

### D.1 Авторское право — landmark cases

#### NYT v OpenAI & Microsoft (filed Dec 2023, SDNY)
- Center: **"Regurgitation"** — модели memorize и воспроизводят NYT content.
- **20 миллионов ChatGPT logs** OpenAI обязан выдать (Bloomberg Law affirms).
- **Summary Judgment deadline: 2 апреля 2026** [VFY-day-of].
- Plaintiffs' expert reports due 14 ноября 2025. Discovery + expert phase.
- Trial — TBD; **самое consequential дело для будущего GenAI** (formulation Patent AI Lab).

#### Getty Images v Stability AI
- **UK High Court ruling 4 ноября 2025**: Stability **выиграл** primary copyright claims. Court: AI model weights **NOT a "copy"** of images по CDPA. "Extremely limited" trademark infringement на early Stable Diffusion versions.
- **US case** (Getty Images (US) v Stability AI Ltd, 3:25-cv-06891) — **Motion to Dismiss 10 февраля 2026**, San Francisco, Judge Trina L Thompson [VFY-day-of].
- UK findings → used в US case.

#### Andersen et al v Stability/Midjourney/DeviantArt (NDCal)
- Class action artists: training данные без consent + DMCA + публичные права.
- Motion to dismiss **DENIED** Aug 12 (Judge Orrick) → discovery.
- **Третий amended complaint 27 фев 2026**; answers 13 марта 2026.
- **Trial set for 8 сентября 2026** [VFY-day-of].

#### RIAA v Suno / Udio (filed 24 июня 2024)
- Universal/Sony/Warner через RIAA.
- **Suno** (D Mass): fair-use defence; **summary judgment hearing июль 2026** [VFY-day-of].
- **Udio** (SDNY): **UMG settled 29 окт 2025** (payment + licensing для joint AI platform 2026); **Warner license late 2025**; **Sony — last major actively litigating** [VFY-day-of].

#### Thomson Reuters Enterprise Centre v Ross Intelligence (D Del)
- Westlaw headnotes → Ross's competing AI legal-research tool.
- **Февраль 2025**: Judge Bibas — **partial SJ for Thomson Reuters**, ruled "NOT fair use".
- **2,200+ из 3,000 headnotes** directly infringed.
- Применены Andy Warhol Foundation v Goldsmith факторы: "commercial" + no "further purpose or different character" → direct competition с Westlaw.
- **Первое американское ruling**, rejecting fair-use defense в AI-training контексте.
- ⚠ Caveat: Ross — non-generative AI. Применимость к LLM/diffusion — будет тестироваться в NYT/Andersen/Getty.

#### Японский подход (Article 30-4 Copyright Act)
- Non-expressive uses (training) **без авторизации**, commercial use разрешён.
- May 2024 — Agency for Cultural Affairs published "General Understanding on AI and Copyright in Japan".
- Fine-tuning / LoRA на стилистических corpora → exemption **не применяется**.
- Декабрь 2024 — Japan Newspaper Publishers Association formal request пересмотра.

#### EU AI Act (transparency в августе 2026)
- Article 50 II: dual transparency — **human-understandable labels + machine-readable** для outputs.
- Deepfakes + публичные тексты — clearly labelled.
- Provider GPAI: technical doc для AI Office, training data summaries.
- Copyright Directive opt-outs должны быть **respected explicitly**.
- Systemic-risk presumption: >10^25 FLOPs training.

### D.2 Deepfakes — landmark incidents

| Инцидент | Дата | Что произошло |
|---|---|---|
| **Scarlett Johansson v OpenAI "Sky"** | май 2024 | OpenAI продемонстрировал Sky-голос eerily similar to ScarJo (отказалась озвучивать ChatGPT в сент 2023). **No lawsuit filed**; OpenAI убрал voice within week. De-facto win for likeness rights. |
| **Drake "Heart on My Sleeve"** | апр 2023 | Ghostwriter977 + AI voice mimicry → 9M+ views, removed by UMG copyright claim. Submitted **for Grammys** (отозвано). |
| **Slovakia election deepfake** | окт 2023 | Fake audio liberal candidate "rigging election" + alcohol prices → vircal перед выборами. |
| **Biden robocall (New Hampshire primary)** | янв 2024 | AI-voice Biden говорил воздержаться от голосования. |
| **Taylor Swift deepfake images** | 27–29 янв 2024 | Sexually explicit AI images на 4chan + X; **one post 47M+ views**. X блокировал searches "Taylor Swift" 2 дня. Породило **No AI FRAUD Act** bill (Durbin/Graham/Klobuchar/Hawley) + EU criminalisation bill Feb 2024 (in force by mid-2027). |
| **South Korea schools epidemic** | август 2024 | **>230 Telegram-чатов** с deepfake-порно из selfies одноклассниц/учительниц. **6,500 takedown requests Jan–July 2024 (4× over 2023)**. 74% подозреваемых — 10–19 лет. **Между 2021–июль 2024: 793 reported, only 16 prosecuted.** |
| **Arup Hong Kong CFO scam** | январь 2024 | Finance worker invited на видеозвонок с deepfake-CFO + colleagues → **$25.6M (HK$200M) за 15 транзакций**. Engineering firm Sydney Opera House. Финансовый ущерб от deepfakes уровня корпоративного. |

### D.3 Slop & model collapse

#### Шумаилов и др., Nature 2024 (vol 631, p 755–759)
- **"AI models collapse when trained on recursively generated data"** — recursive training на синтетике даёт **прогрессирующую деградацию качества + сужение diversity**.
- Также называется **Model Autophagy Disorder (MAD)**.
- Контекст: проекция — supply высококачественных human-данных закончится к ~2026 → fallback на synthetic outputs → системный риск quality decline.

#### Конкретные инциденты slop
- **Google AI Overviews** (May 2024 rollout): рекомендации "**put glue on pizza**" (⅛ cup non-toxic glue, source = Reddit joke), "**eat at least one rock per day**" (source = The Onion satire, "Geologists recommend"), "Obama is a Muslim president" (false), "Andrew Johnson got degrees 1947–2012" (умер в 1875).
- **Sports Illustrated** (ноябрь 2023, Futurism exposé): articles published под **fake author names + AI-generated profile photos** (продавались на digital marketplaces). Arena Group blamed third-party AdVon Commerce. SI Union: "horrified". Articles deleted.
- **Amazon Kindle AI sham books** (2023–24): только **19 из 100 top-bestselling books** в одной секции — actual human writers; остальные 81 — absurd AI-generated. Scammers выпускают AI-knockoffs известных авторов под slight-modified названиями и pseudonyms ("Frank Gioia", "Ted Alkyer" — fakes реальных jazz figures). Amazon ограничил KDP до 3 books/day/author, требует disclosure (но не показывает её consumer'у).
- **Wizards of the Coast / Magic: The Gathering** (4 янв 2024): promotional image Ravnica Remastered с AI artefacts → отрицание ("created by humans") → **признание + правила vendor'ам прохибит AI** (мay 2024 contributor policy). Также — Glory of the Giants август 2023 (AI-"polished" art) + Player's Handbook 2024 accusations.

### D.4 Displacement & worker harm

#### Hollywood strikes 2023 (WGA + SAG-AFTRA)
- WGA strike 2 мая 2023 – 9 нояб 2023; SAG-AFTRA 14 июля – 9 нояб 2023.
- Завоёванные AI-clauses:
  - **Digital Replicas** (likeness): требуется informed consent + compensation.
  - **Synthetic Performers**: характеры созданные digitally, не identifiable как specific people — regulated.
- **2026 negotiations**: SAG-AFTRA + WGA подписали **4-year extension** with AMPTP — гарантирует no-repeat strike 2026/2027/2028. WGA push for expanded AI protections.

#### Freelance market data
- Upwork: **−17.01% graphic design** jobs после GenAI image release.
- Income compression: AI-detected в **40%** работ writers $10–19/час, **<10%** $60+/час.
- Korean voice actors — крупная displacement waveb (источники не подтверждены конкретными цифрами — to verify).

---

## E. Авторское право — taxonomy исков

### Категория 1: Training data scraping без лицензии (input side)
- **NYT v OpenAI/Microsoft** — текстовый flagship.
- **Andersen v Stability/Midjourney/DeviantArt** — визуальный flagship.
- **Getty Images v Stability AI** — UK lost (Nov 2025); US pending (Feb 2026 MTD).
- **RIAA v Suno/Udio** — музыкальный flagship.
- **Thomson Reuters v Ross Intelligence** — first US ruling **rejecting fair-use** (Feb 2025).
- Японский Article 30-4 — opt-in to scraping legalized; EU AI Act — обязательное disclosure источников.

### Категория 2: Output similarity / memorization (output side)
- NYT v OpenAI — "regurgitation" theory: output воспроизводит plaintiff's article verbatim.
- Suno/Udio — RIAA evidence: outputs "substantially similar" to копирайтнутым recordings (specific vocal styles, melodic patterns).

### Категория 3: Style mimicry
- Andersen: "in the style of" — выгенерированы works in style of named artists.
- Lensa controversy: signatures Kim Jung Gi visible в AI outputs.
- Wizards of the Coast: вендоры использовали AI-art в style Hasbro IP.
- **Open question 2026**: «style» не охраняется copyright традиционно, но Andersen ruling может его расширить.

### Категория 4: Voice / likeness rights (right of publicity)
- Scarlett Johansson v OpenAI — soundalike voice → de-facto resolution.
- SAG-AFTRA Digital Replicas clause — contract-based protection.
- Drake/Weeknd "Heart on My Sleeve" — UMG removed via copyright claim, not likeness suit (still open avenue).
- No AI FRAUD Act — federal bill для likeness protection.
- EU criminalisation of deepfake porn — Feb 2024 deal, by mid-2027.

---

## F. «AI здесь не нужен» — критерии негативного выбора

### F.1 Когда лучше human
- **High-stakes journalism / investigative reporting** — Sports Illustrated AI-fakes scandal показал: legacy trust = key asset, AI-pseudonyms разрушают brand value моментально. NYT, WaPo, Reuters — guidelines прохибит AI для original reporting.
- **Original creative direction** — Coca-Cola, Toys "R" Us cases: AI execution **может** работать как brand element, но Christmas/иконический ads без human creative leadership получают public backlash → measurable brand damage (sentiment swing −10pp для Toys "R" Us).
- **Long-form musical narrative / coherent album** — Suno/Udio пока генерируют tracks, не coherent 50-min album'ы с motif development (claim, to verify через MusicTechnology benchmarks).

### F.2 Где AI создаёт юридический долг компании
- Training data scrape без licence → судебный риск (Thomson Reuters case установил precedent для non-generative; NYT/Andersen/Getty US test для generative).
- Visa/Mastercard payment processors могут отказать (Stability AI Visa-restrictions 2023 — to verify) при NSFW capabilities.
- **EU AI Act август 2026**: missing training-data disclosure → enforcement (10^25+ FLOP models = systemic risk).
- Style cloning без consent (Wizards reverted vendor AI-policy после публичной outcry — reputational cost > savings).

### F.3 Where user research показал rejection
- **AI YouTube thumbnails**: 47.3% creators **stopped using** AI thumbnails (Social Blade Creator Survey, Dec 2025). Reasons:
  - "Creepy smooth skin / weird lighting" → **−22% CTR vs human-edited**.
  - Mobile text readability fails в 39.6% случаев → **−19% CTR**.
  - Mismatched promise/content → **−61.8% first-15-sec drop-off**.
- **Coca-Cola/Toys "R" Us AI ads**: measurable negative sentiment swing (см. C.6).
- **Lensa avatars**: вирусный peak 2022, последующая критика artist community + opt-out demands.
- **Wacom Christmas dragon controversy** (Dec 2023): brand published AI art в social → community backlash → public apology (to verify конкретного исхода).

### F.4 Где AI просто фейлит
- **Complex character continuity** в multi-scene narrative (Toys "R" Us ad: clothes/features inconsistency criticised).
- **Hand anatomy, text rendering** (Midjourney/SD3 — до GPT Image 1.5 при 90% accuracy).
- **Sustained classical music / long-form narrative** (Suno tracks ≤4 min, coherent album-level structure).
- **Fact-checked / factual reporting** — Google AI Overviews показал: модели pull jokes из Reddit/Onion как facts.
- **Original visual style** — модели **средневзвешивают** training data, не invent (это критика всё ещё стоит — см. style mimicry разделы).

---

## G. Media для embed в слайды

### G.1 Видео (YouTube / direct)

| Тема | Тип | URL (то, что валидно как public reference) |
|---|---|---|
| Sora 2 official release reel | официальный | https://openai.com/index/sora-2/ (embed Sora page) |
| Veo 3 examples | Google AI Studio | https://aistudio.google.com/models/veo-3 |
| Genie 3 demo (DeepMind) | официальный | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ |
| Toys R Us Sora ad full | YouTube | search "Toys R Us Sora AI Cannes 2024" |
| Coca-Cola "Holidays Are Coming" 2024 AI | YouTube | search "Coca-Cola AI Christmas 2024" |
| Heart on My Sleeve (Drake/Weeknd AI) | YouTube re-uploads (original taken down) | search "Ghostwriter977 Heart on My Sleeve" — original removed by UMG |
| Runway Gen-4 showcase | Runway site | https://runwayml.com (latest gallery) |
| Kling 3.0 release reel | Kuaishou | search "Kling 3.0 February 2026 launch" |

### G.2 Изображения (для слайдов)

- **Wizards of the Coast Ravnica Remastered controversial image** — публикация была удалена, но скриншоты в журналистских репортажах (PCGamer, GeekWire).
- **Sports Illustrated AI authors** — Futurism article screenshots реальных profile photos: https://futurism.com/sports-illustrated-ai-generated-writers
- **Sora 2 sample frames** — OpenAI release page.
- **Midjourney v7 community showcases** — https://www.midjourney.com/showcase
- **Adobe Firefly examples** — https://www.adobe.com/products/firefly.html
- **Imagen 4 product photography** — Google Cloud blog samples.
- **Genie 3 generated 3D scenes** — DeepMind blog.
- **Taylor Swift deepfake response Wikipedia** — нет direct media рекомендуется (sensitive); use #ProtectTaylorSwift hashtag screenshot или Variety article header.

### G.3 Аудио

- **Suno create UI public demos** — https://suno.com (intro page часто содержит samples).
- **ElevenLabs voice library demos** — https://elevenlabs.io/voice-library (sample voices, public, no auth).
- **Drake/Weeknd "Heart on My Sleeve" excerpt** — оригинал taken down; news reports содержат clips (NPR, Variety).
- **Stable Audio 2 examples** — https://www.stableaudio.com.

### G.4 Interactive demos (можно показать на лекции)

- **Adobe Firefly playground** — https://firefly.adobe.com (логин-only, но имеет public showcase).
- **Hugging Face Spaces** — https://huggingface.co/spaces (множество image/audio gen демонстраций).
- **Suno create** — https://suno.com (free tier).
- **ElevenLabs free TTS** — https://elevenlabs.io/text-to-speech.
- **Midjourney web** — https://www.midjourney.com (paid).
- **Runway** — https://runwayml.com (free trial).

---

## Источники

### Models & Tools

- [OpenAI Sora 2 Complete Guide 2026](https://wavespeed.ai/blog/posts/openai-sora-2-complete-guide-2026/)
- [Sora 2 is here | OpenAI](https://openai.com/index/sora-2/)
- [Sora 2 API Pricing & Quotas 2026](https://www.aifreeapi.com/en/posts/sora-2-api-pricing-quotas)
- [Sora 2 Pricing Calculator (May 2026)](https://costgoat.com/pricing/sora)
- [Veo 3 Pricing 2026](https://www.veo3ai.io/blog/veo-3-pricing-2026)
- [Build with Veo 3.1 Lite, Google Blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/)
- [Google AI Studio — Veo 3](https://aistudio.google.com/models/veo-3)
- [Runway Gen-4 Turbo (MindStudio)](https://www.mindstudio.ai/blog/what-is-runway-gen-4-turbo-video)
- [Runway Review 2026: Gen-4.5 #1 Video Arena](https://aitoolanalysis.com/runway-review/)
- [Kling AI Complete 2026 Guide](https://similevault.com/kling-ai/)
- [Kling 3.0 Tutorial 2026](https://medium.com/@cliprise/kling-3-0-tutorial-the-complete-guide-to-4k-ai-video-generation-in-2026-0e8cfed0e042)
- [Midjourney Review 2026 — Revoyant](https://www.revoyant.com/blog/midjourney-review)
- [Midjourney V7 Review 2026](https://ai-coding-flow.com/blog/midjourney-review-2026/)
- [AI Image Generation APIs in 2026 (NovaKit)](https://www.novakit.ai/blog/ai-image-generation-apis-2026-compared)
- [The Complete Guide to AI Image Generation 2026 (Cliprise)](https://medium.com/@cliprise/ai-image-generation-in-2026-midjourney-flux-2-imagen-4-and-beyond-7934a9228e98)
- [How Much Does AI Image Generation Cost in 2026 — ImagineArt](https://www.imagine.art/blogs/ai-image-generation-cost)
- [AI Art Cost: $0 Per Image Possible — ZSky AI](https://zsky.ai/blog/how-much-does-ai-art-cost)
- [Genie 3 — Google DeepMind](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
- [Genie 3 World Model (WaveSpeedAI)](https://wavespeed.ai/blog/posts/google-deepmind-genie-3-world-model-2026/)
- [ElevenLabs Dubbing Studio](https://elevenlabs.io/dubbing-studio)
- [ElevenLabs Voice Cloning](https://elevenlabs.io/voice-cloning)
- [ElevenLabs Review 2026 (Coval)](https://www.coval.dev/blog/elevenlabs-review-2026-voice-cloning-and-synthesis-capabilities-explained)
- [Adobe Firefly: Next Evolution (Adobe Blog April 2025)](https://blog.adobe.com/en/publish/2025/04/24/adobe-firefly-next-evolution-creative-ai-is-here)
- [Adobe MAX 2025 — Futurum](https://futurumgroup.com/insights/adobe-max-2025-will-adobes-platform-approach-resonate-with-enterprises/)
- [Adobe Q4 FY 2025 Revenue (Futurum)](https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/)
- [Adobe Firefly partner models](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-non-adobe-models.html)

### Lawsuits — Copyright

- [NYT v OpenAI Lawsuit Update 2026 — Patent AI Lab](https://medium.com/@patentailab/nyt-vs-openai-lawsuit-update-2026-did-regurgitation-kill-the-fair-use-defense-d63ff021b805)
- [OpenAI Must Turn Over 20 Million ChatGPT Logs (Bloomberg Law)](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms)
- [NYT v Microsoft case docket — CourtListener](https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/)
- [Getty v Stability AI UK ruling (Bird & Bird)](https://www.twobirds.com/en/insights/2025/uk/stability-ai-defeats-getty-images-copyright-claims-in-first-of-its-kind-dispute-before-the-high-cour)
- [Getty v Stability — Mayer Brown analysis](https://www.mayerbrown.com/en/insights/publications/2025/11/getty-images-v-stability-ai-what-the-high-courts-decision-means-for-rights-holders-and-ai-developers)
- [Andersen v Stability AI — Knowing Machines](https://knowingmachines.org/knowing-legal-machines/legal-explainer/cases/andersen-v-stability-ai)
- [Andersen v Stability AI — Mesh IP Law tracker](https://www.meshiplaw.com/litigation-tracker/andersen-v-stability-ai)
- [Thomson Reuters v Ross — Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2025/02/reuters-ross-court-ruling-ai-copyright-fair-use)
- [Thomson Reuters v Ross — Reed Smith](https://www.reedsmith.com/en/perspectives/2025/03/court-ai-fair-use-thomson-reuters-enterprise-gmbh-ross-intelligence)
- [RIAA sues Suno and Udio (RIAA)](https://www.riaa.com/record-companies-bring-landmark-cases-for-responsible-ai-againstsuno-and-udio-in-boston-and-new-york-federal-courts-respectively/)
- [Music Industry AI Lawsuits Tracker 2026 — Chartlex](https://www.chartlex.com/blog/business/music-industry-ai-lawsuits-tracker-2026)
- [Suno AI Lawsuit Update Feb 2026 — Patent AI Lab](https://patentailab.com/riaa-vs-suno-lawsuit-update-2026/)
- [EU AI Act transparency obligations (HSF)](https://www.hsfkramer.com/notes/ip/2026-03/transparency-obligations-for-ai-generated-content-under-the-eu-ai-act-from-principle-to-practice)
- [EU AI Act 2026 Compliance — Secure Privacy](https://secureprivacy.ai/blog/eu-ai-act-2026-compliance)
- [Japan AI Copyright — Privacy World](https://www.privacyworld.blog/2024/03/japans-new-draft-guidelines-on-ai-and-copyright-is-it-really-ok-to-train-ai-using-pirated-materials/)
- [Japan Approves Bill to Drop Consent Requirement — Tech Jacks](https://techjacksolutions.com/ai-brief/japan-approves-bill-to-drop-consent-requirement-for-ai-train/)

### Deepfakes & Likeness

- [Scarlett Johansson responds — Variety](https://variety.com/2024/digital/news/scarlett-johansson-responds-shocked-angered-openai-chatgpt-her-1236011135/)
- [ScarJo / OpenAI — Northeastern](https://news.northeastern.edu/2024/05/23/scarlett-johansson-open-ai/)
- [Drake AI Heart on My Sleeve — NPR](https://www.npr.org/2023/04/21/1171032649/ai-music-heart-on-my-sleeve-drake-the-weeknd)
- [Drake AI submitted for Grammys — Variety](https://variety.com/2023/music/news/ai-generated-drake-the-weeknd-song-submitted-for-grammys-1235714805/)
- [Taylor Swift deepfake controversy — Wikipedia](https://en.wikipedia.org/wiki/Taylor_Swift_deepfake_pornography_controversy)
- [Taylor Swift X block — TIME](https://time.com/6589487/taylor-swift-searches-blocked-x-twitter-deepfakes-response/)
- [Slovakia deepfake & 2024 election fakes — Ash Center Harvard](https://ash.harvard.edu/articles/the-apocalypse-that-wasnt-ai-was-everywhere-in-2024s-elections-but-deepfakes-and-misinformation-were-only-part-of-the-picture/)
- [Biden robocall NPR](https://www.npr.org/2024/02/08/1229641751/ai-deepfakes-election-risks-lawmakers-tech-companies-artificial-intelligence)
- [South Korea Telegram deepfakes — NPR](https://www.npr.org/2024/09/06/nx-s1-5101891/south-korea-deepfake)
- [Korea deepfake porn schools — Daily Star](https://www.thedailystar.net/news/world/news/deepfake-porn-crisis-batters-south-korea-schools-3698986)
- [Arup deepfake CFO scam — CNN](https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk)
- [Arup deepfake — Fortune](https://fortune.com/europe/2024/05/17/arup-deepfake-fraud-scam-victim-hong-kong-25-million-cfo/)

### Slop & Model Collapse

- [Shumailov Nature 2024 — model collapse note (arXiv)](https://arxiv.org/abs/2410.12954)
- [Nature Machine Intelligence on AI Autophagy](https://www.nature.com/articles/s42256-025-00984-1)
- [Google AI Overviews pizza/rock — ACS](https://ia.acs.org.au/article/2024/google-goes-viral-after-ai-says-to-put-glue-on-pizza-eat-rocks.html)
- [Why Google AI Overviews fails — MIT Tech Review](https://www.technologyreview.com/2024/05/31/1093019/why-are-googles-ai-overviews-results-so-bad/)
- [Sports Illustrated AI fake authors — CNN](https://www.cnn.com/2023/11/27/media/sports-illustrated-deletes-articles-fake-author-names-ai-profile-photos/index.html)
- [Sports Illustrated scandal — Poynter](https://www.poynter.org/commentary/2023/sports-illustrated-artificial-intelligence-writers-futurism/)
- [Amazon AI sham books — NPR / Authors Guild](https://www.npr.org/2024/03/13/1237888126/growing-number-ai-scam-books-amazon)
- [Authors Guild: AI Sham Books surge](https://authorsguild.org/news/ai-driving-new-surge-of-sham-books-on-amazon/)
- [Wizards of the Coast AI controversy — GeekWire](https://www.geekwire.com/2024/wizards-of-the-coast-will-adjust-generative-ai-policy-for-magic-following-controversy/)
- [WotC reverses course — PC Gamer](https://www.pcgamer.com/wizards-of-the-coast-reverses-course-admits-to-using-ai-in-promotional-image-well-we-made-a-mistake-earlier/)

### Marketing & Ad Backlash

- [Coca-Cola Holidays Are Coming AI backlash — NBC News](https://www.nbcnews.com/tech/innovation/coca-cola-causes-controversy-ai-made-ad-rcna180665)
- [Coca-Cola 2024 ad doubles down — Marketing AI Institute](https://www.marketingaiinstitute.com/blog/criticism-ai-coke-holiday-ad)
- [Toys R Us Sora ad backlash — Hollywood Reporter](https://www.hollywoodreporter.com/business/digital/toys-r-us-ad-sora-openai-video-tool-reaction-1235932993/)
- [Toys R Us sentiment plummet — Marketing-Interactive](https://www.marketing-interactive.com/toys-r-us-sora-ai-sentiments-plummet)
- [Lensa AI controversy — TechCrunch](https://techcrunch.com/2022/12/05/lensa-ai-app-store-magic-avatars-artists/)
- [Lensa AI signatures — ARTnews](https://www.artnews.com/art-news/news/signatures-lensa-ai-portraits-1234649633/)

### Industry Adoption / Displacement

- [Lionsgate × Runway partnership — Variety VIP](https://variety.com/vip/what-lionsgates-partnership-deal-runway-means-1236151418/)
- [Lionsgate × Runway — Lionsgate Investor Relations](https://investors.lionsgate.com/news-events/news/news-details/2024/Runway-Partners-with-Lionsgate-in-First-of-its-Kind-AI-Collaboration/default.aspx)
- [IAB U.S. Digital Video Ad Spend 2026](https://www.iab.com/news/u-s-digital-video-ad-spend-to-surpass-80b-in-2026/)
- [IAB 2026 Video Ad Spend Report](https://www.iab.com/insights/video-ad-spend-report-2026/)
- [AI Marketing Statistics 2026 — Digital Applied](https://www.digitalapplied.com/blog/ai-marketing-statistics-2026-adoption-data-points)
- [75 AI Video Statistics 2026 — Vivideo](https://vivideo.ai/blog/ai-video-statistics-2026)
- [Stock photography decline — Kaptur](https://kaptur.co/the-silent-collapse-generative-ais-erosion-of-photo-licensing-revenue/)
- [Stock photography dying — Tidewater Teddy](https://tidewaterteddy.com/2025/01/10/stock-photography-is-dying/)
- [Getty + Shutterstock merger — Kaptur](https://kaptur.co/the-authenticity-cartel-why-the-getty-shutterstock-merger-is-really-about-who-controls-real/)
- [Upwork AI displacement — Jobbers Displacement Index](https://www.jobbers.io/ai-job-displacement-index-which-freelance-skills-are-at-risk/)
- [Will AI Replace Graphic Designers — Upwork](https://www.upwork.com/resources/will-ai-replace-graphic-designers)
- [SAG-AFTRA AI bargaining timeline](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence/sag-aftra-ai-bargaining-and)
- [WGA/SAG-AFTRA 2023 AI contracts — Perkins Coie](https://perkinscoie.com/insights/blog/generative-ai-movies-and-tv-how-2023-sag-aftra-and-wga-contracts-address-generative)
- [2026 WGA & SAG-AFTRA Negotiations — No Film School](https://nofilmschool.com/2026-wga-contract-negotiations)
- [YouTube AI Thumbnails fail — Banana Thumbnail](https://blog.bananathumbnail.com/ai-youtube-thumbnails-2/)
- [YouTube CTR 2026 AI Thumbnails — Miraflow](https://miraflow.ai/blog/youtube-ctr-2026-good-click-through-rate-ai-thumbnails)
