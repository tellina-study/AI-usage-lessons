# Lec-08 Research: Freshness-проверка на октябрь 2026

**Дата проверки:** 2026-10-21
**Метод:** WebSearch/WebFetch, прямое чтение источников (не суммаризация без проверки — см.
`notes/mcp-limitations.md` [#225-1] и memory `feedback_webfetch_unreliable_on_large_json`).
**Канон:** каждое число ниже несёт базу/counterfactual (CLAUDE.md § Baseline/Counterfactual
Mandate) и форму «цена ошибки → классический режим в той же цене → модель против режима»
(`stroenie-i-povestvovanie.md` §4), где применимо.
**Не редактировать файлы лекции из этого файла** — только фиксация находок для Phase 2.

---

## Задача 1 — Cost-collapse по классам творческих активов (Раздел 1 architecture.md)

### 1.1 Изображение: freelance-дизайнер вручную

**Старая цифра (`architecture.md`):** $50-200 вручную, 1-3 дня.

**Проверено на октябрь 2026:**
- Upwork — общий диапазон фрилансера $15-35/час (начинающий), $25-60/час (средний),
  $60-120+/час (эксперт). Adobe проанализировал 1000 профилей Upwork-дизайнеров: средняя
  ставка **$49.65/час** против среднерыночной Upwork ~$25/час
  ([designshifu.com](https://www.designshifu.com/blog/graphic-designer-cost),
  [gigradar.io](https://gigradar.io/blog/upwork-hourly-rate)).
- Fiverr — логотип/иллюстрация: базовый пакет $5-50, стандартный $30-150, премиум $80-500+,
  Fiverr Pro $300-5000 ([websiteplanet.com](https://www.websiteplanet.com/logo-design-services/fiverr-logo-design/),
  [inkbotdesign.com](https://inkbotdesign.com/logo-design-cost/)). Указанный источник честно
  отмечает: «при $5-30 вы получаете шаблонный логотип», то есть нижняя граница — не
  сопоставимый по качеству продукт.

**Вывод: старый диапазон $50-200 подтверждается**, но заслуживает уточнения на две полосы —
$50-150 (среднее/разовое задание фрилансера, 1-3 дня, то, что и описывал план) и отдельно
«Fiverr Pro / brand identity» $300-5000 (для иного по объёму заказа, не для одной
иллюстрации). Для одной иллюстрации/асcета — **база: $50-200 остаётся корректной, актуальный
диапазон 2026 — $50-150 за типовое задание фрилансера среднего уровня.**

**Источники:** [Upwork Hourly Rate Calculator 2026](https://gigradar.io/blog/upwork-hourly-rate) ·
[How Much Does a Graphic Designer Cost in 2026 — DesignShifu](https://www.designshifu.com/blog/graphic-designer-cost) ·
[Logo Design Cost In 2026 — Inkbot](https://inkbotdesign.com/logo-design-cost/) ·
[Fiverr Logo Design pricing — WebsitePlanet](https://www.websiteplanet.com/logo-design-services/fiverr-logo-design/)
(все проверены 2026-10-21, статьи датированы 2026).

### 1.2 Студийный трек на заказ

**Старая цифра:** $500-2000/неделя.

**Проверено:** реальность 2026 расслаивается сильнее одного диапазона —
- work-for-hire композитор: **$200-1500 за минуту** готовой музыки;
- прямой контракт с композитором (direct-from-composer): **$1000 за инди-проект до $500 000**
  за major-brand кампанию или полнометражный score;
- национальная ТВ-реклама с оригинальной композицией: **$5000-25000**;
- для сравнения — стоковая лицензия (не custom): standard/commercial $20-100/трек,
  extended/premium (broadcast/film/реклама) $100-500+/трек
  ([foximusic.com](https://www.foximusic.com/blog/how-much-does-it-cost-to-license-music-for-a-commercial/),
  [audiosocket.com](https://blog.audiosocket.com/entertainment-media/how-much-does-music-licensing-cost/)).

**Вывод: старая цифра $500-2000/неделя устарела по форме** (платят не за неделю работы
композитора, а помесячно/по минуте готового материала или по проекту). **Замена:**
«custom score для рекламного ролика — $5000-25000 за трек (нацреклама) или $200-1500/минута
(work-for-hire композитор)» против стоковой лицензии $20-100/трек (не custom) — это и есть
нужная пара база/counterfactual: custom vs stock, не custom vs AI напрямую без промежуточного
шага.

**Источники:** [Commercial Music Licensing Cost 2026 — Foxi](https://www.foximusic.com/blog/commercial-music-licensing-cost-ranges-by-use/) ·
[How Much Does Music Licensing Cost — Audiosocket 2026](https://blog.audiosocket.com/entertainment-media/how-much-does-music-licensing-cost/).

### 1.3 Озвучка диктором

**Старая цифра:** $Х/минута (не заполнено в плане).

**Проверено, диапазон по сегментам (2026):**
- non-broadcast narration: $350-450 (1-2 мин) до $1750-2350 (40-60 мин) за готовую минуту;
- e-learning/corporate: $15-55/минуту, минимум $350-450 за модуль независимо от длины;
- audiobook: $150-250/час (начинающий) до $500-1000+/час (топ-уровень);
- entry-level диктор: $50-150/минуту; mid-level (2-7 лет): $150-350/минуту;
  senior (7+ лет): $350-1000+/минуту
  ([voicecrafters.com](https://www.voicecrafters.com/industry-standard-voice-over-rates/),
  [biztoolkit.co](https://www.biztoolkit.co/post/voiceover-artist-rates-in-2026-per-word-per-minute-per-project)).

**База для главы:** $50-450/минуту готовой озвучки (зависит от опыта и типа контента) —
разброс нужно явно привязывать к сегменту (e-learning дешевле, рекламный/медицинский
дороже), иначе читатель не поймёт, почему «от $50 до $1000» выглядит как один разброс без
структуры.

**Источники:** [Voice Over Rates 2026 — Voicecrafters](https://www.voicecrafters.com/industry-standard-voice-over-rates/) ·
[Voiceover Rates 2026 — BizToolkit](https://www.biztoolkit.co/post/voiceover-artist-rates-in-2026-per-word-per-minute-per-project).

### 1.4 Актуальная цена генерации — флагманы октября 2026

| Класс актива | Инструмент (актуальный на 2026-10) | Цена |
|---|---|---|
| Изображение | **Midjourney V8.1/V8.2** (релиз V8 Alpha 17 марта 2026, V8.1 — 30 апреля, V8.2 — дефолт с 24 июля) | Basic $10/мес ≈200 fast-изображений ≈ **$0.05/img**; Pro ≈ $0.03/img fast, unlimited relax ([wavespeed.ai](https://wavespeed.ai/blog/posts/what-is-midjourney-v8-features-pricing-how-to-use-2026/)) |
| Изображение | **Adobe Firefly** (Image Model 5) | Standard $9.99/мес = 2000 кредитов, Image 5 = 10 кредитов/img → **≈$0.05/img** 2K; на платных планах «стандартные» генерации безлимитны/0 кредитов ([toolcolumn.com](https://www.toolcolumn.com/pricing/adobe-firefly-pricing)) |
| Музыка (трек) | **Suno** (V6-поколение моделей, тарифы Free/Pro $10/Premier $30) | Pro: ~2500 кредитов/мес ≈ 500 песен/мес ≈ **$0.02/песня**; Premier: ~2000 песен/$30 ≈ **$0.015/песня**; отдельно — скачивание $0.40/трек на Pro (ограничение 20/мес) ([costbench.com](https://costbench.com/software/ai-music-generators/suno/)) |
| Озвучка/минута | **ElevenLabs** | API Flash v2.5 ≈ $0.04/мин, Multilingual v2 ≈ $0.09/мин; на подписке ≈$0.17-0.20/минуту сгенерированной речи ([felloai.com](https://felloai.com/elevenlabs-pricing/), [oakgen.ai](https://oakgen.ai/blog/elevenlabs-pricing-limits-cost)) |

**Freshness-замечание (уже отмечено в architecture.md, подтверждено):** Sora API закрыт
24 сентября 2026 после провала партнёрства с Disney ($1B) — **не брать Sora как текущий
флагман** для видео-класса; если раздел 1 вообще разбирает видео, актуальная замена —
Veo 3.1 / Kling 3.0, не Sora.

**Итоговая база/counterfactual для разбора (разряд «три-четыре порядка»):**
- изображение: $50-150 вручную → $0.03-0.05 генерацией = **разрыв ×1000-3000** (три-четыре
  порядка подтверждается);
- трек (custom score): $5000-25000 (нацреклама) или $200-1500/мин вручную → $0.015-0.02/песня
  Suno = **разрыв на 5-6 порядков**, если сравнивать custom-score с AI-треком напрямую — это
  **честно должно быть помечено как разные по характеру продукты** (studio score для бренда ≠
  сгенерированный трек без вокалиста/студии), иначе сравнение «от нуля», что канон запрещает;
  корректнее сравнивать AI-трек со **стоковой лицензией** $20-100/трек → разрыв ×1000-5000,
  того же порядка, что и у изображений;
- озвучка: $50-450/минуту вручную → $0.04-0.20/минуту ElevenLabs = **разрыв ×250-1000**, тот
  же порядок.

**Правка для architecture.md (сообщить, не применять):** сравнение custom-studio-score
напрямую с ценой Suno-трека physически некорректно (разные продукты — см. выше); для
«трёх-четырёх порядков» как сквозного рефрена лучше опорная пара — **стоковая лицензия vs
AI-генерация**, не custom-composer vs AI-генерация.

---

## Задача 2 — Coca-Cola/Toys "R" Us, sentiment backlash (Раздел 3)

### Источник чисел — найден и подтверждён

Старые цифры (positive +12.2%→+3.4%, negative 13.5%→53.4%) **подтверждены дословно** прямым
чтением первоисточника:

> «12.2% positive, 13.5% negative and 74.3% neutral» → «3.4% positive, 53.4% negative and
> 43.2% neutral» — **Marketing-Interactive, 28 июня 2024**, со ссылкой на измерение
> **CARMA** (media intelligence firm).

**Кто измерял:** CARMA — PR/коммуникационная мониторинг-компания, 40 лет на рынке,
3500+ брендов-клиентов. Методология — «AI Sentiment Analysis» (AI-классификация тона +
human review), собственная «objectives-led» рамка, не просто vanity-метрики
([carma.com/ai](https://carma.com/ai/)).

**Какая платформа/выборка:** **не раскрыта** ни в оригинальной статье Marketing-Interactive,
ни в последующих цитированиях (Hollywood Reporter и др.) — CARMA не публикует, какая
соцсеть(и) легли в основу процента, и не называет размер выборки упоминаний. Это honest
gap, не придуманное число: **числа реальны и атрибутированы к конкретной компании
(CARMA), но методология измерения (платформа, N) не раскрыта публично** — для слайда это
нужно либо явно пометить («данные CARMA, методология не раскрыта»), либо не предъявлять как
точную науку, а как медиа-измерение с ограничением.

**Третья цифра (neutral), не упомянутая в architecture.md:** 74.3%→43.2% — полезно добавить
на слайд для полноты (positive+negative+neutral=100%, проверяемая арифметика).

### Что стало с кампаниями дальше

- **Coca-Cola повторила AI-рекламу в 2025** (второй год подряд) — снова AI-генерация
  (Silverside AI, 70 000 сгенерированных клипов на один ролик), снова backlash («soulless and
  creepy dystopian nightmare» — TechRadar, Forbes, нояб. 2025). Coca-Cola **не отступила** от
  AI-пути несмотря на повторную критику.
- **Контринтуитивная деталь, которой не было в старом research:** независимая ad-testing
  панель **System1 (Test Your Ad)** дала повторному ролику 2025 года **5.9 звёзд — максимум
  возможного по их шкале**, что системно расходится с soc-media негативным sentiment по
  CARMA. **Это и есть вторая пара данных для баланса** — панель предрелизного/контролируемого
  тестирования (классический режим, упомянутый в architecture.md как «pre-release фокус-группы»)
  **разошлась** с измеренной реакцией открытой аудитории. Формулировка для главы: «контролируемый
  тест (System1) оценил ролик максимально высоко — открытая аудитория (CARMA) отреагировала
  резко негативно» — само по себе иллюстрация тезиса раздела 3 («классика pre-release
  тестирования» vs «измеренная реакция на AI-контент»), причём ярче, чем предполагал
  architecture.md, потому что расхождение, а не совпадение.
- **Toys "R" Us** не повторяла AI-рекламу в заметном объёме в 2025-2026 (поиск не нашёл
  публичного продолжения кампании) — "The Origin of Toys 'R' Us" остаётся единичным
  инцидентом на 2026-10-21, в отличие от Coca-Cola.

**Вывод: цифры подтверждены дословно, источник найден (CARMA), платформа/выборка —
честно не раскрыты публично (gap). Добавление: System1 panel score 5.9/5.9 (2025 reprise)
даёт контраст классика-vs-открытая-аудитория, которого в архитектуре ещё нет — рекомендация
Phase 2 включить.**

**Источники:** [Toys R Us sentiments plummet — Marketing-Interactive, 28.06.2024](https://www.marketing-interactive.com/toys-r-us-sora-ai-sentiments-plummet) ·
[CARMA AI methodology](https://carma.com/ai/) ·
[Coca-Cola doubles down — MarketingDive](https://www.marketingdive.com/news/coca-cola-doubles-down-ai-new-holiday-campaign/804303/) ·
[AI or No AI, Coke Gets the Christmas Love — System1](https://system1group.com/ad-of-the-week/ai-or-no-ai-coke-gets-the-christmas-love) ·
[Coca-Cola Sparks Backlash Again — Forbes, 04.11.2025](https://www.forbes.com/sites/danidiplacido/2025/11/04/coca-cola-sparks-backlash-with-ai-generated-christmas-ad-again/).

---

## Задача 3 — YouTube AI-thumbnails, CTR drop (Раздел 3)

### Первоисточник — НЕ найден, цепочка выглядит как самоцитирующийся SEO-контент

Прямая проверка (WebFetch на `blog.bananathumbnail.com`, откуда и разошлись все три цифры
−22%/−19%/−61.8%, плюс 47.3%):

- Статья **сама не даёт ссылок, методологии или размера выборки** для «Social Blade Creator
  Survey, декабрь 2025» и для чисел −22%/−19%.
- Единственная цифра со ссылкой — 61.8% (атрибутирована статьёй к Wistia). **Прямая проверка
  Wistia State of Video Report 2026 не нашла цифры 61.8%** — найдены другие, несовпадающие
  числа того же явления («мismatch thumbnail/title» → ~30% drop в первые 10 секунд, 33% drop
  в первые 30 секунд). **61.8% как атрибуция Wistia не подтверждается.**
- Прямой поиск «Social Blade Creator Survey» на `socialblade.com` (включая `site:socialblade.com`)
  **не находит такого исследования** — официальный блог Social Blade (`/blog/youtube-auto-generated-thumbnails-experiment/`,
  недоступен для WebFetch, HTTP 403, но виден в поисковой выдаче) посвящён другой теме —
  **YouTube собственному эксперименту с auto-generated thumbnails** (платформенная функция,
  не creator-survey про отказ от AI-миниатюр).
- Независимые вторичные блоги (`kavel.ai` и др.) повторяют те же три числа **без собственной
  проверки**, то есть это одна исходная (неподтверждённая) цифра, растиражированная по
  SEO-контенту — классический признак «источника не существует», который канон требует
  проверять прямым чтением, а не доверием к цитате (`notes/mcp-limitations.md` [#225-1]).

**Контрастные легитимные данные, найденные вместо этого (2026):**
- YouTube: **>1 млн каналов** ежедневно использовали встроенные AI-инструменты создания
  (включая, предположительно, генерацию миниатюр/скриптов) в декабре 2025.
- Kit (ConvertKit) 2026 Creator Economy Survey (апрель 2026, N=550 creators): 57.3%
  используют AI-инструменты ежедневно, 89.2% всегда проверяют/правят AI-вывод вручную —
  **это прямо противоречит нарративу «почти половина creators отказалась от AI»** — реальный
  тренд на 2026 выглядит как рост принятия с обязательной human-правкой, не массовый откат.

**Вывод: старые цифры (47.3%, −22%, −19%, −61.8%) НЕ подтверждаются первоисточником —
первоисточник физически не найден при прямой проверке, атрибуция к Social Blade и Wistia
не выдерживает проверки. Рекомендация: СНЯТЬ все четыре числа из главы.** Баланс/база для них
отсутствует не потому, что не искали, а потому, что число само по себе похоже на
выдуманное/непроверяемое — ровно случай, который канон запрещает «допускать выигрыш от нуля»
по аналогии: здесь это «провал без измеренной базы», то есть тот же дефект с другим знаком.

**Что можно использовать вместо (с реальной базой):**
- Kit 2026 Creator Economy Survey, N=550, апрель 2026, 57.3% daily AI use / 89.2% always
  edit — реальная, атрибутированная, с размером выборки цифра о принятии AI в творческом
  процессе creators (не специфично про thumbnails, но про редакционный контроль над AI-выводом —
  неплохо встаёт в раздел 2 «кто это проверил», не раздел 3).
- YouTube официальная политика (2026): AI-миниатюры **разрешены без disclosure** (категория
  «production assistance»), единственное ограничение — миниатюра не должна вводить в
  заблуждение относительно контента видео. Это полезный «классический режим / актуальное
  правило» факт для раздела 3, даже без цифр CTR.

**Источники (включая опровержение):** [AI YouTube Thumbnails Fail — BananaThumbnail (источник исходных чисел, без верифицируемых ссылок)](https://blog.bananathumbnail.com/ai-youtube-thumbnails-2/) ·
[Social Blade auto-generated thumbnails experiment (другая тема, не creator survey)](https://socialblade.com/blog/youtube-auto-generated-thumbnails-experiment/) ·
[Wistia State of Video 2026](https://wistia.com/blog/video-marketing-statistics) ·
[Kit 2026 AI Creator Economy Report](https://kit.com/resources/blog/ai-creator-economy-report) ·
[YouTube AI thumbnail policy 2026 — AIMetadataCleaner](https://aimetadatacleaner.com/blog/youtube-ai-content-identification-policies-2026).

---

## Задача 4 — Displacement (Upwork) и Getty+Shutterstock merger (Раздел 5)

### 4.1 Upwork/Fiverr creative-категории — 2026 данные

**Официальный источник:** Upwork «In-Demand Skills 2026» (опубликован февраль 2026, данные
US-маркетплейса за 2025 год) + Upwork investor PDF.

- **Рост AI-навыков:** AI-related freelance skills в целом **+109% YoY**; внутри этого —
  **AI video generation/editing +329% YoY** (самая быстрорастущая категория), **AI image
  generation/editing +95% YoY**, AI data annotation +154%, AI integration +178%
  ([selfemployed.com](https://www.selfemployed.com/news/upwork-ai-freelance-skills-demand-2026/),
  investor PDF).
- **Fiverr:** AI video/animation +278%, «Canva designers» +403% (отдельная категория
  курирования AI-инструментов, не ручного дизайна).
- **Традиционные (non-AI) creative категории — качественно, без точной цифры:** официальный
  отчёт говорит лишь, что «спрос остаётся сильным» (без численного YoY). **Это важный
  честный gap** — architecture.md корректно отметил, что displacement-данные «требуют
  проверки причинности», и проверка это подтверждает: **рост AI-категорий измерен точно,
  падение/рост традиционных категорий на 2026 год — НЕ измерено тем же источником**, то есть
  нельзя посчитать net displacement как «выросло X% / упало Y%» одной парой чисел.
- **Платформенный контекст (не часть architecture.md, но важный baseline):** Upwork сам как
  платформа сжимается — активная клиентская база −6% в 2025, новые постинги −19% YoY
  (2026) — часть эффекта «меньше заказов» может быть платформенным спадом Upwork, не
  AI-вытеснением конкретно creative-специалистов. Это ровно тот case, когда «два числа
  разошлись — проверь базу» (memory `feedback-two-numbers-check-the-base.md`): падение
  постингов на Upwork ≠ падение спроса на creative-работу в экономике в целом.
- **Старая цифра из `2026-landscape.md` («−17.01% graphic design jobs на Upwork после релиза
  GenAI image tools»)** — **не переподтверждена свежим поиском**; более свежий (июль 2026)
  срез показывает Graphic/Editorial/Presentation Design как 6.8% всех категорий (10889
  вакансий) без явного сравнения год-к-году в том же источнике. Occupational Outlook (BLS,
  США в целом, не Upwork) — графический дизайн как профессия **−2% за 2025-2035** (10-летний
  прогноз, не Upwork-специфичный срез).

**Вывод: подтверждения причинности по-прежнему нет.** Рост AI-категорий — измерено и
атрибутировано (Upwork official report). Снижение традиционных категорий — качественно
правдоподобно (Upwork-платформа сжимается, «дешёвая массовая работа» уходит к
Canva/AI-инструментам), но **без единого числа, сопоставимого по методологии с ростом
AI-категорий**. Для главы: **не предъявлять «AI vs традиция» как одну пару процентов** —
предъявлять раздельно (рост AI-категорий +109-329% YoY, упадок традиционных — качественно,
со ссылкой на BLS −2%/10 лет как единственную количественную, но не Upwork-специфичную базу).

**Источники:** [Upwork: AI Freelance Skills Demand More Than Doubles — Selfemployed.com](https://www.selfemployed.com/news/upwork-ai-freelance-skills-demand-2026/) ·
[Upwork Investor PDF, In-Demand Skills 2026](https://investors.upwork.com/node/12681/pdf) ·
[Upwork Job Market July 2026 — TryVibeWorker](https://tryvibeworker.com/blog/upwork-job-market-report-july-2026) ·
[Graphic Designer Hiring Market 2026 — AIGA](https://designcareers.aiga.org/career-resources/hire-designers-11/graphic-designer-hiring-market-demand-and-supply-2026-156) ·
[BLS Occupational Outlook — Graphic Designers](https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm).

### 4.2 Getty + Shutterstock merger — КРИТИЧЕСКОЕ ОБНОВЛЕНИЕ, старые данные полностью устарели

**Старая цифра (`2026-landscape.md`):** «merger объявлен январь 2025, $3.7B, ожидаемый
$150-200M cost savings (3 года)» — подана как состоявшийся/продолжающийся defensive-ход.

**Реальный статус на 2026-10-21 — слияние НЕ состоялось, Getty проходит банкротство:**

1. **7 июля 2026** — Getty Images официально **расторгла** merger agreement после того, как
   UK CMA (антимонопольный регулятор) 15 мая 2026 поставил условием одобрения **продажу всего
   редакционного бизнеса Shutterstock** — совет директоров Getty 30 июня 2026 единогласно
   отказался на это пойти.
2. **29 сентября 2026** — NYSE приостановила торги акциями Getty Images после падения цены до
   нескольких центов.
3. **12-13 октября 2026** — Getty Images подала **prepackaged Chapter 11 bankruptcy** (Delaware),
   инициировала делистинг с NYSE.
4. **21 октября 2026 (сегодняшняя дата проверки)** — Getty объявила реструктуризацию:
   семья Getty + Koch Equity Development вносят до **$533M** нового капитала; кредиторы
   списывают **$270M** необеспеченных облигаций; компания возвращается в частную собственность.
5. **Причины, названные самой компанией** (лендер-презентация, октябрь 2026): долговая
   нагрузка **≈$2.1B**, издержки несостоявшегося слияния, судебные издержки (включая
   litigation со Stability AI — тот самый Getty v Stability UK кейс из раздела 4
   architecture.md), **и «растущее давление AI-генерируемых изображений»** — названо прямо
   как один из факторов.
6. **Бизнес-показатели:** выручка упала на 2.5% (до $229.1M за отчётный период), число
   активных годовых подписчиков упало до **240 000** с **321 000** годом ранее — это и есть
   нужная пара база/counterfactual: **−25% подписчиков за год**, прямое измерение эффекта,
   которое старый research не имел вообще.

**Это не «форма переезда бизнес-модели», как предполагал architecture.md («Getty+Shutterstock
merger как форма переезда»), а провал защитной стратегии: слияние задумывалось как ответ
на AI-disruption, регулятор его заблокировал, а сама компания-инициатор обанкротилась в
процессе.** Для раздела 5 это даёт значительно более сильный (и структурно иной) разбор, чем
«консолидация в ответ на AI»: **попытка защититься слиянием не состоялась, и именно AI-
давление в числе названных причин банкротства.**

**Baseline/counterfactual для главы:** было 321 000 подписчиков (год назад) → стало 240 000
(октябрь 2026) = **−25% за год**, на фоне долга $2.1B и выручки −2.5% — это сопоставимые,
атрибутированные к одному источнику (lender presentation + Getty Q2 2026 financials) числа,
готовые к использованию без доп. проверки.

**Источники:** [Getty Images Ends Shutterstock Merger — TipRanks](https://www.tipranks.com/news/company-announcements/getty-images-ends-shutterstock-merger-redeems-secured-notes) ·
[Getty Scraps $3.7B Merger — US News, 30.06.2026](https://money.usnews.com/investing/news/articles/2026-06-30/getty-images-scraps-shutterstock-merger) ·
[NYSE halts Getty Images trading — PPC Land](https://ppc.land/nyse-halts-getty-images-trading-after-shares-fall-to-12-cents/) ·
[Getty Files for Bankruptcy, going private with Koch — Bloomberg, 21.10.2026](https://www.bloomberg.com/news/articles/2026-10-21/getty-files-for-bankruptcy-in-process-that-will-take-it-private) ·
[Getty Images Heads Into Bankruptcy, subscribers fall to 240,000 — DesignRush](https://news.designrush.com/getty-images-chapter-11-prepackaged-bankruptcy-go-private-koch-equity) ·
[How Getty's Bankruptcy Affects Photographers — PetaPixel, 12.10.2026](https://petapixel.com/2026/10/12/how-gettys-bankruptcy-affects-photographers-payments-contracts-and-next-steps/) ·
[Getty Images Advances Financial Restructuring — GlobeNewswire, 21.10.2026](https://globenewswire.com/news-release/2026/10/21/3385104/0/en/getty-images-advances-financial-restructuring-to-strengthen-balance-sheet-and-support-future-growth.html).

---

## Резюме по всем 4 задачам (для Phase 2 брифа)

| № | Группа чисел | Статус | Действие |
|---|---|---|---|
| 1 | Cost-collapse по классам активов | Подтверждено с уточнением | Изображение $50-150→$0.03-0.05 (MJ V8/Firefly) ОК; трек — заменить custom-studio-vs-AI на stock-license-vs-AI ($20-100→$0.015-0.02) для честного «того же порядка» сравнения; озвучка $50-450/мин→$0.04-0.20/мин (ElevenLabs) ОК, но разбить по сегментам |
| 2 | Coca-Cola/Toys R Us sentiment | Подтверждено дословно + источник найден (CARMA) | Числа верны; добавить System1 panel 5.9★ (2025) как контраст классика/аудитория; явно пометить «платформа/выборка CARMA не раскрыта публично» |
| 3 | YouTube AI-thumbnails CTR | НЕ подтверждено — первоисточник не существует | СНЯТЬ 47.3%/−22%/−19%/−61.8% целиком; заменить на Kit 2026 Creator Survey (N=550, атрибутировано) + YouTube official no-disclosure policy |
| 4 | Upwork displacement + Getty/Shutterstock | Upwork: рост AI-категорий подтверждён, падение традиционных — не подтверждено тем же источником (gap честный). Getty/Shutterstock: **устарело полностью** — merger расторгнут июль 2026, Getty в Chapter 11 с 12-13 октября 2026 | Переписать раздел 5: merger не «консолидация», а проваленная защита + банкротство; подписчики 321k→240k (−25%/год) как новая опорная пара |

**Самое важное изменение против майских (2026-05) данных:** Getty Images, которую план ещё
называл примером «отрасль консолидируется в ответ на AI», **подала на банкротство 9 дней
назад** (12-13 октября vs дата проверки 21 октября), а само слияние с Shutterstock
**провалилось** в июле — это меняет тезис раздела 5 с «бизнес-модель переезжает» на
«попытка защититься не сработала, и AI-давление — одна из названных причин краха». Второе по
значимости — цепочка цифр про YouTube-миниатюры физически не имеет первоисточника и должна
быть снята, а не исправлена мелкой правкой.
