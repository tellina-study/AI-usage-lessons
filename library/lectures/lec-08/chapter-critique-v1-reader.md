# Reader Text-Only Report — Лекция 8 — 2026-05-20

**VERDICT: APPROVE-WITH-POLISH**

**Mode:** text-only (методический контроль ДО создания слайдов)
**Target:** `/tmp/lec-08-wt/library/lectures/lec-08/chapter.md` (v1, ~13 200 слов)
**Reader profile:** студент 3 курса МГТУ ИУ6 (программная инженерия / системы); базовый ML; не дизайнер; не работал в creative-индустрии; не знает industry-context.

---

## Открывающее впечатление (сырая реакция студента)

Я сел читать в субботу после обеда. Раздел 0 пошёл нормально — три семейства моделей понятно, мне как ИУ-шнику архитектурный взгляд приятен. К §3 я уже выпил вторую кружку чая и понял: тут 12 кейсов подряд, каждый с американскими судами, юридическими формулировками — это к РК будет ад. Но прочитал. К §5 чек-лист — щёлкнул, осмысленно. Закрыл вкладку, и понял: я не помню разницу между Andersen и Getty. И кто такой Joe Russo, и почему «fucking sucks» — это весомое мнение.

Общая оценка: глава **читабельная и полезная**, но **тяжёлая** для self-study без преподавателя на ряде участков. P0 issues нет; есть **компактный набор P1 friction-точек**, которые при доработке делают главу самодостаточной.

---

## Проверка 1. Когнитивная нагрузка

### Где теряюсь

- **§0.1 «Три семейства моделей»** — плотный, но честно достаточный. Diffusion объяснён через «обращение процесса добавления шума» — для меня (есть базовый ML) понятно; для одногруппника без ML — на грани. Один абзац на семейство — лимит для первого знакомства, без визуализации в тексте; в режиме text-only это **OK для меня**, но станет крайне зависимым от слайдов потом.
- **§3.1 «Taxonomy 4 категорий исков»** — самый перегруженный момент. В одном абзаце вводятся: NYT v OpenAI, Andersen, Getty UK/US, RIAA v Suno/Udio, Thomson Reuters v Ross. **5 кейсов за 4 строки**, без того чтобы я ещё успел понять, чем каждый отличается. Это caption-style introduction перед deep-dive — задумка ясна, но **я как читатель ещё не различаю эти кейсы**, а от меня уже требуется держать в голове четыре категории.
- **§3.6 «Andy Warhol Foundation v Goldsmith факторы»** — упоминается без объяснения, что это за тест и какие 4 фактора. Я как студент это пропускаю и иду дальше, теряя нить аргумента.
- **§2.4 «Wage compression снизу»** — термин впервые появляется в bold без определения, я понимаю по контексту со второго абзаца, но первое чтение — пауза.

### Что НЕ объяснено достаточно при первом появлении

| Термин | Где впервые | Объяснён? |
|---|---|---|
| `[VFY-day-of]` | §1.1 Sora 2 | Пояснено в §Введение, но только если читать линейно. Студент, открывший с §1, не поймёт |
| MoE (Mixture-of-Experts) | §1.6 Kandinsky 6.0 | **НЕТ** — упоминается всуе |
| ELO benchmark | §1.1 Kling 3.0 | Минимум контекста — «открытый ELO benchmark», но как метрика работает — нет |
| TDM-exception | §1.6 RU законопроект | Объяснено через «обучение... не нарушает авторское право» — для меня OK, но «TDM» как акроним непонятно (text and data mining — нигде не расшифровано) |
| MTD (Motion to Dismiss) | §3.4 Andersen | Не расшифровано. «Class action выживает до discovery» — что значит discovery? |
| SDNY / Northern District of California / District of Delaware / District of Massachusetts | §3.2, 3.4, 3.5, 3.6 | Зачем мне знать в каком округе подан иск? Нигде не объяснено, почему юрисдикция важна |
| DMCA | §3.4 Andersen | Просто «DMCA violations» — что это, я не знаю |
| Summary Judgment | §3.2, 3.5 | Не объяснено. Я знаю что суд, но что такое SJ vs trial — нет |
| Section 107, fair-use 4 factor test | §3.6 + глоссарий | Глоссарий упоминает «4 factor test», но факторы не перечислены. Студент не может сам применить тест |
| GPAI | §Введение «EU AI Act для GPAI-моделей» | Не расшифровано |
| Mel-spectrogram | §0.1 | Брошено без объяснения, но это не критично для понимания |
| KDP (Amazon Kindle Direct Publishing) | §3.10 | Не расшифровано |
| ESG | §2.4 + §5.2 | Не расшифровано; я слышал, но что именно — нет |
| FMCG | §4 self-check | Не расшифровано |

**P1.** **Юридический жаргон** (MTD, SJ, SDNY, DMCA, fair-use 4-factor) — самая большая когнитивная нагрузка для инженера-студента. Глава предполагает, что я понимаю американскую процедуру; я не понимаю. Это **не academic deficit**, это **gap для целевой аудитории** — лекция не для law-студентов.

---

## Проверка 2. Industry context

### Background — какие отсылки требуют знаний, которых у студента нет

- **NYT (New York Times)** — я знаю что это газета, но **не знаю**, что это считается «paper of record», эталоном американской журналистики. Без этого context «NYT судится с OpenAI» звучит как «одна компания судится с другой». Глава не объясняет, почему именно NYT — символический case.
- **SAG-AFTRA / WGA** — расшифровка ни разу не дана. Я погуглил: Screen Actors Guild – American Federation of Television and Radio Artists / Writers Guild of America. **P1: расшифровка нужна при первом появлении в §2.4.**
- **RIAA** — Recording Industry Association of America. Тоже не расшифровано.
- **UMG, Sony Music, Warner Music** — major labels, индустриальный контекст не объяснён. Я как ИУ-шник могу не знать, что «3 major labels» — это олигополия в музыкальной индустрии и что их claim особенно весомый.
- **Sports Illustrated** — я слышал название (видел в школьных учебниках английского), но не знаю, что это spez 70-летний журнал с миллиардным brand-equity. Глава **упоминает**, что это «журнал с 70-летней историей, brand equity около миллиарда долларов» (§3.10) — OK, **есть inline context, P2**.
- **Toys "R" Us** — я знаю что это магазин игрушек (был в детстве в моллах). Что это бренд с huge ностальгической ценностью в US — не знаю. Глава **не объясняет** brand-equity context для Toys R Us; просто «iconic seasonal creative».
- **Joe Russo** — упоминается с цитатой «fucking sucks», без объяснения кто это. В §3.11 в скобках есть «director Avengers: Endgame» — **OK, есть P2 fix**.
- **Coca-Cola «Holidays Are Coming»** — глава пытается объяснить через «культурную классику с грузовиком», но я как русский студент эту campaign не знаю (не транслировалась в РФ). Здесь критика «soulless» падает в пустоту, я не понимаю **что именно** soul'less, если оригинальной кампании я не видел.
- **Lionsgate** — упомянут через скобку «студия за "Голодными играми", "Saw", "John Wick"» — **OK, P2**.
- **Arup** — «британская engineering firm, известна по Sydney Opera House» — **OK**.
- **Cannes Lions** — фестиваль рекламы, не объяснено. Студент-инженер может не знать.
- **Bird & Bird, Mayer Brown, Davis Wright Tremaine, Reed Smith, Knowing Machines, Patent AI Lab** — юридические фирмы / специализированные блоги. Имена в источниках выглядят как авторитетные, но мне неизвестно, кто из них relevant authority.
- **Adobe MAX, Cannes Lions** — отраслевые события.

### Industry context — общее впечатление

Глава **очень US-центрична**. Я как русский студент чувствую: лекция написана с допущением, что NYT, SAG-AFTRA, Hollywood, FMCG-бренды — это common knowledge. Для меня — нет. §1.6 (Russian context) и упоминание Минцифры — единственные точки заземления в моём контексте.

**P1: Industry context для US institutions** требует minimal inline-explanations при первом появлении (≤10 слов).

---

## Проверка 3. Понятность кейсов

Sample-check 5 кейсов: могу ли я объяснить случившееся в 3 предложениях после чтения?

### NYT v OpenAI (§3.2)

Могу:
> NYT подал в суд на OpenAI и Microsoft за то, что ChatGPT обучался на их статьях без лицензии И способен воспроизвести эти статьи verbatim. Если NYT выигрывает — fair-use для AI training отвергнут, и AI-компании обязаны лицензировать корпус. Trial — конец 2026 / начало 2027.

**Понятно. Урок ясен:** реализуй output-similarity check.

### Andersen v Stability/Midjourney/DeviantArt (§3.4)

Полу-могу:
> Художники подали class action против Stability и Midjourney за обучение на их работах без consent. Если выиграют, prompts «in the style of [artist]» станут infringement. Trial — сентябрь 2026.

**Понятно с натяжкой.** Что такое class action, я понимаю; что такое DMCA — нет; «выживает до discovery» — нет понимания discovery. **Урок ясен:** не позволяй prompts «in the style of».

### RIAA v Suno/Udio (§3.5)

Могу:
> RIAA (три major labels) подал в суд на AI music generators. К маю 2026 года Udio settled с UMG и стал licensed-partner; Warner лицензировал Suno. Sony продолжает push. Outcome — licensing, не банкротство.

**Понятно. Урок ясен:** выбирай licensed-corpus провайдеров.

### Korea schoolgirl deepfake (§3.8)

Могу:
> В Корее обнаружили 230+ Telegram-чатов с deepfake-porn из selfies одноклассниц. 74% подозреваемых — подростки 10–19 лет. Enforcement rate ~2%.

**Понятно, эмоционально сильно.** Урок чёткий: NSFW + age verification до launch.

### SI fake authors (§3.10)

Полу-могу:
> Sports Illustrated публиковал статьи под fake author names с AI-generated profile photos. Когда вскрылось, бренд потерял доверие моментально.

**Понятно, но context "почему это разрушительно"** опирается на знание SI как 70-летнего флагмана. Глава дала это в скобке — норм.

### Итог проверки кейсов

**4 из 5 кейсов студент пересказывает осмысленно**, 1 (Andersen) с лёгким friction по юридическому жаргону. Это **хороший результат** для глубокой темы.

**Урок для инженера** в каждом case действительно сформулирован отдельным quote-block — это **сильное методическое решение**. Я их выделяю взглядом сразу.

---

## Проверка 4. Связность narrative

### Переходы между разделами

- **§0 → §1.** Жёсткая ось «добавил → изменил → сломал» введена в §0.2 и затем тянется как connective tissue. **Отлично работает.**
- **§1 → §2.** Гладко. «Capabilities появились → они меняют экономику» — естественная логика.
- **§2 → §3.** Чуть резковато. §2 закрывается «displacement — структурный shock», §3 открывается «taxonomy исков». Связь есть, но между last sentence §2.4 и first sentence §3.1 я бы хотел один связующий абзац: «теперь, когда мы видим экономические изменения, посмотрим на юридическую цену».
- **§3 → §4.** Сильный мост. §3 имеет 12 кейсов; §4 формулирует 4 критерия отказа inductively. §4.1 явно прописывает «выведены **inductively из кейсов §3**, не a priori» — это и есть payoff, я как студент это вижу.
- **§4 → §5.** Гладко. §4 — критерии, §5 — operational чек-лист с mapping на 12 кейсов.

### Keystone-ось «добавил → изменил → сломал»

**Работает как обещано.** Не теряется к Разделу 4, тянется до §5 («4 критерия выведены из 12 cases»). Это методически сильное решение, и студент-читатель чувствует, что лекция структурирована, а не свалена.

### Cross-references к Лекциям 1/3/5/7

- **К Лекции 1** (§Введение, §Закрытие) — упоминается framework «где AI работает / где нет». Я лекцию 1 помню, понимаю отсылку. Если бы не помнил — отсылка «Лекция 1 ставила general framework» достаточно self-contained.
- **К Лекции 3** (§1.4 Genie 3, §1.5 платформенный слой, §Закрытие) — отсылки к «архитектурам AI-систем», «композитным архитектурам». **Self-contained**, без знания лекции 3 урок понятен.
- **К Лекции 5** (§Закрытие) — параллель в legal-risk frame. Понятно, но **очень коротко** — для студента, кто Лекцию 5 пропустил, ссылка ничего не дополняет.
- **К Лекции 7** (§3.1, §Закрытие) — 4-actor responsibility framework. **Self-contained**, идея мэппинга «artist / creator / victim / IP holder» дана inline в §3.1.

**P2.** Cross-references к Лекциям 5/7 предполагают, что студент эти лекции прошёл. Если он на самоподготовке к РК после пропуска лекций — friction. Не критично.

---

## Проверка 5. LO achievability

После прочтения главы, могу ли я выполнить LO?

### LO1 — классифицировать AI-применения по 4 областям + назвать tool 2026

**ДА.** Cross-product матрица 3×4 (§0.3) — мощный инструмент навигации. Каждая клетка имеет конкретный инструмент с brand-named tool (Sora 2 / ElevenLabs / Midjourney / ChatGPT). **LO1 достигается уверенно.**

### LO2 — оценить cost/quality/legal trade-off для конкретной задачи

**Частично.** §0.1 даёт mental model 3 семейств (необходимо для архитектурного аргумента). §2.1 даёт cost-таблицу. §3 даёт legal risks. §5 даёт чек-лист. Все элементы есть, **но они в разных разделах**. Студент должен собрать оценку сам из 3 мест. Это OK для LO глубокого уровня, но **может быть полезен один summary-блок в §5 — «как применять trade-off** в комбинации».

### LO4 — проанализировать landmark case + урок

**ДА.** §3 имеет 12 кейсов, каждый с механизмом провала и quote-block «урок для инженера». Студент тренируется на 12 примерах. **LO4 достигается крайне уверенно.**

### LO5 — сформулировать критерии «здесь AI не нужен» + чек-лист

**ДА.** §4.1 даёт 4 критерия. §5.1 — 5-вопросный чек-лист. §5.2 — mapping на 12 кейсов. **LO5 достигается уверенно** — операционализуемый артефакт.

**Общий вердикт по LO:** все 4 цели достижимы. LO2 требует синтеза из разных разделов — это **не дефект**, это normal для интегрированных skills, но summary-блок в §5 был бы plus.

---

## Проверка 6. Engagement

### Где скучно

- **§2.3 «Новые профессии»** — список ролей с описаниями каждой строки. Information dense, но эмоционально нейтрально.
- **§3.6 «Thomson Reuters v Ross»** — самый юридически плотный кейс; non-generative AI; рассказ через 4-factor Warhol test и Section 107 — это академическая сухота. Студент-инженер пробегает глазами.
- **§3.12 «Displacement consolidated»** — третий раз про displacement (после §2.4 и §3 преамбулы). Повтор.

### Где emotionally engaged

- **§3.7 Arup $25.6M** — конкретный кейс, конкретная сумма, конкретный механизм. **Hook-grade engagement.**
- **§3.8 Korea schoolgirl deepfake** — морально шокирующий case, цифры «793 reported / 16 prosecuted = 2% enforcement» бьют. **Hook-grade engagement.**
- **§3.10 SI fake authors + Amazon Kindle (19 из 100 books — реальные)** — конкретно и contraintuitively плохо. **Engaged.**
- **§3.11 Toys R Us sentiment swing −9pp positive / +40pp negative** — конкретные measurable цифры. **Engaged.**
- **§1.3 ScarJo «Sky»** — Hollywood drama, конкретная цитата, recognized name. **Engaged.**

### «Ага-моменты»

- **§0.1 «Firefly safe не от архитектуры, а от training corpus»** — это аха. Я думал, разница архитектурная; на самом деле — data-licensing. Меняет мою mental model.
- **§0.1 «Voice cloning из 1 минуты, потому что foundation модель делает 99% работы»** — аха.
- **§2.4 «Photographers перестают быть customer'ом, они становятся data source»** — мощная фраза. Структурный shift в одной строке.
- **§3.5 «Outcome RIAA — не AI music banned, а AI music licensed»** — counterintuitively. Я думал, что lawsuits закроют Suno; реальность — превратили его в licensed product. Аха.

**Engagement gradient:** Раздел 0 — нейтрально-engaging (architectural insights), §1 — moderately engaging (tool tour), §2 — neutral, §3 — **HIGH engaging** (cases), §4-§5 — moderate-utility engaging (chek-list).

---

## Проверка 7. Q&A backup полнота

### «Как именно работает diffusion?»

§0.1 даёт абзац: noise add → reverse denoising → text-conditioning. Для не-ML студента — достаточно для intuitive понимания. Для ML-студента — отсылка к Ho et al. (2020) / Rombach et al. (2022) для глубины. **OK.**

### «А в РФ что?»

§1.6 — отдельный subsection с Kandinsky 6.0 / Шедеврум / SymFormer / SaluteSpeech + Минцифры законопроект + frontier-gap объяснение. **Полно.** Конкретные даты, конкретные models, конкретный legal landscape, **honest takeaway про gap**.

### «Что делать если мой проект подпадает под Andersen case?»

§3.4 quote-block: «не допускать prompts типа "в стиле Эджа"»; §5.1 чек-лист пункт 1 (training-data license); §5.2 mapping. **Actionable.**

### «А как реализовать output-similarity check?»

§3.2 quote-block: «Bloom-filter на known protected content, либо вероятностная проверка через embedding similarity». §5.1 — повтор. Для студента-инженера — **достаточно для starting point**, не developer-grade инструкция, но направление ясно.

### «Что такое 4-factor fair-use test?»

**Gap.** Глоссарий упоминает «4 factor test, расширенный Andy Warhol Foundation v Goldsmith», но факторы не перечислены. Если на лекции задают вопрос — лектор должен помнить факторы сам. Я как студент по chapter ответить не могу.

### «Чем slop отличается от обычных AI-ошибок?»

§3.9 — Shumailov model collapse + Google AI Overviews + glue-on-pizza. **OK для intuitive понимания.** Глоссарий даёт чёткое определение через Bender/Marcus.

### «Что такое EU AI Act, конкретно?»

Упомянут в §Введение и §1.6, но без детального изложения. Если на лекции спросят — лектор должен помнить. **Gap для chapter.**

**Итог:** Q&A backup **отличный для специфических кейсов**; **с пробелами на legal frameworks** (fair-use факторы, EU AI Act detail).

---

## Проверка 8. Style

### Tone

**Academic-но-читаемый.** В целом сильно. Местами скатывается в:

- **Канцелярит:** «дериваты конкретных судебных дел», «реалистическое распределение capex», «структурно негативно». Это читается, но усилием.
- **Англоязычные кальки:** «sustained "soulless" backlash», «accept liability», «trans-parency for GPAI», «slight-modified», «не дублируется AI», «дисontonant с brand expectation». Калька + опечатка — глаз цепляется.
- **Опечатки/typos:** «дentрализированный finance worker» (§3.7), «фронтир-видео-модели» (склейка), «масстиже-контент» (latinized), «деntrализированный», «дисontonant», «spas'ает», «commodific'ация» (с апострофами вместо «-ация»), «нагрузка commercial-safe генерация», «отнсения», «трансcript».
- **Иногда стилистический скачок:** в §3.11 цитата «fucking sucks» — окей, аутентичная цитата, но возле академического тона немного резко без warning'а.

### Length per section

| Раздел | Слова (прибл) | Feels |
|---|---|---|
| §Введение | 600 | Balanced |
| §0 (mental model) | 1500 | **Чуть тяжеловат**, plотный для самого начала |
| §1 (capabilities) | 2500 | Balanced; §1.6 RU — особенно хорошо |
| §2 (economics) | 2000 | Balanced |
| §3 (failures) | 4000 | **Marathon** — 12 кейсов подряд утомляют |
| §4 (negative criteria) | 1200 | Good — payoff |
| §5 (checklist) | 800 | Чуть кратко для finale |
| §6 (closing) | 600 | Good |

**P2.** §3 — 12 кейсов подряд — это marathon. Между кейсами полезны были бы breath-marks: одна строка типа «До сих пор мы видели copyright cases — теперь переход к deepfake harms». **Структурные подзаголовки уже есть** (§3.1 taxonomy → §3.2-3.6 cases → §3.7-3.8 deepfakes → §3.9-3.10 trust erosion → §3.11 brand backlash → §3.12 displacement), но именно **transitional sentences** между группами отсутствуют.

### «Урок для инженера» blocks

**Сильно помогают flow.** Quote-block формат → визуально отделён → я возвращаюсь к нему при review. Это **методическое золото** главы. Сохранить как есть.

---

## Top 5 P0 issues (студент НЕ понимает критичное → LO не достижим)

**Ни одного P0.** Все LO достижимы; критические кейсы понятны. Глава работает для self-study уверенно. Это значит — **chapter ready for slide derivation**.

---

## Top 5 P1 issues (студент понимает с усилием, friction)

### P1-1. Юридический жаргон без расшифровки

**MTD, SJ, SDNY, NDCA, DMCA, fair-use 4-factor test, discovery, class action, motion to dismiss** — все используются без inline-расшифровки при первом появлении. Студент-инженер не law-student.

**Fix:** Добавить glossary-блок в начале §3 «Юридическая лексика этой главы (для не-юристов)» с 8-10 терминами на пол-строки каждый.

### P1-2. SAG-AFTRA / WGA / RIAA / UMG / Sony Music — расшифровка только в глоссарии (если вообще)

При первом появлении в основном тексте — только акронимы. Студент не знает, что это.

**Fix:** При первом появлении — расшифровка в скобках («SAG-AFTRA — Screen Actors Guild, профсоюз американских актёров»). 4-5 точечных вставок.

### P1-3. §3.1 taxonomy перегружен — 5 кейсов в одном абзаце до того, как студент их различает

Caption-style introduction до deep dive — методически OK, но **перегружает** на первом чтении.

**Fix:** Переписать §3.1 как **матрицу 4×3** (категория × case-name × theory-of-harm) — визуально легче парсить, чем сплошной абзац.

### P1-4. §3 marathon — 4000 слов / 12 кейсов без structural breathing marks

Студент устаёт между §3.6 и §3.7, теряет concentration.

**Fix:** Добавить ~3 transitional абзаца на 2 строки между группами кейсов: copyright cases (3.2-3.6) → deepfake harms (3.7-3.8) → trust erosion (3.9-3.10) → brand backlash (3.11) → displacement (3.12).

### P1-5. US-центричность без inline industry context

NYT, Toys R Us, Coca-Cola «Holidays Are Coming», Cannes Lions, Joe Russo, Lionsgate — для русского студента-инженера не common knowledge. Часть имеет context-скобки (Lionsgate, Arup, Joe Russo, SI), часть — нет (Toys R Us, Coca-Cola campaign, NYT как paper of record).

**Fix:** 5-7 точечных context-скобок на ≤10 слов каждая.

---

## Top 5 P2 polish suggestions

### P2-1. Опечатки/typo cleanup

«дentрализированный», «дисontonant», «spas'ает», «commodific'ация», «масстиже-контент», «трансcript», «нагрузка commercial-safe генерация», «фронтир-видео-модели», «отнсения», «трансcrip», «slight-modified», «not just ethical», «(нон-fair-use)». Pass typo-сweepers.

### P2-2. §1.6 — добавить inline-context для не-российских читателей курса

Если глава потенциально транслируется в другие языки или будет читать иностранец — context Сбера / Яндекса / Минцифры нужен. **Для целевой аудитории МГТУ — P3.**

### P2-3. Cross-product матрица 3×4 (§0.3) — повторно отображать в §3 как mental anchor

После 12 кейсов §3 — повторить ту же матрицу с заполненными клетками (где-какой-case в какой клетке). Это **mnemonic для retention**.

### P2-4. §2.3 + §2.4 — список ролей info-dense. Иллюстративная mini-story помогла бы

«Иван — graphic designer на Upwork в 2022 года заработал $4k/мес; к 2026 — $1.5k и переход в AI-prompt-engineer specialty» — даёт human-scale grounding для wage compression цифр.

### P2-5. §3.6 fair-use 4-factor test — перечислить факторы прямо

Один абзац с factor list (purpose / nature / amount / market effect) + как Warhol-suit их modified. Без этого студент не может применить test самостоятельно, что снижает Q&A backup.

---

## Reader-rating (1-10)

**Как студент я бы оценил эту главу 8/10**, потому что:

**+ Сильные стороны:**
- Keystone-ось «добавил → изменил → сломал» работает как обещано — связность есть.
- Cross-product матрица 3×4 — мощный mental model.
- 12 landmark кейсов с quote-блоком «урок для инженера» — методическое золото.
- 4-критерия + 5-вопросный чек-лист + mapping — payoff на operational уровне, не abstract.
- §1.6 Russian context — honest и detailed, без cherry-pick.
- Failure-share визуально доминирует (§3 + §4 + §5 ≈ 50%) — это уважительная подача темы.

**− Friction:**
- Юридический жаргон без расшифровки — самый большой барьер для инженера.
- §3 marathon — 12 кейсов подряд утомляют.
- US-центричность без context-скобок.
- Опечатки/typos местами.

**Если P1 fixes применены — оценка вырастет до 9/10.** P0 нет — глава готова идти на slide derivation, но **с P1-фиксами вперёд**, чтобы slides не унаследовали ту же legal-жаргон friction.

---

## Сводка

- **Mode:** text-only (методический pre-render контроль).
- **Слайдов с P0 issues:** 0 (LO достижимы, критические кейсы понятны).
- **P1 issues:** 5 (юридический жаргон, акронимы, §3.1 перегрузка, §3 marathon, US-context).
- **P2 polish suggestions:** 5 (typos, RU-context, матрица recap, mini-story для §2.3-2.4, fair-use факторы).
- **LO achievability:** LO1/LO4/LO5 уверенно; LO2 частично (синтез нескольких разделов).
- **Vocabulary issues:** ~10 терминов без inline definition (MTD, SJ, SDNY, DMCA, MoE, ELO, TDM, KDP, ESG, FMCG).
- **Industry-context gaps:** SAG-AFTRA / WGA / RIAA расшифровки, NYT / Toys R Us / Coca-Cola campaign brand-equity context.

**Self-study verdict:** глава **читается за 60-80 минут** (~13 200 слов), **достигает 4 LO** с лёгкой нагрузкой на LO2, **engaged in §3** (cases), **academic-readable** style с typo-cleanup pending. **Готова к slide derivation** при условии применения P1-фиксов до Phase 5.

**Top-3 правки до slide derivation:**
1. Inline-расшифровка юридических акронимов (P1-1) — иначе slides унаследуют этот gap.
2. Glossary-блок «легальная лексика для не-юристов» в начале §3 (P1-1).
3. Расшифровка industry-акронимов (SAG-AFTRA, WGA, RIAA) при первом появлении (P1-2).

---

*Конец отчёта Reader Text-Only. Версия v1. Готов к слиянию с другими критиками Phase 3.*
