# Дневник студента ИУ6 — Лекция 8 «AI в креативных индустриях и медиа» — 2026-05-20

**Кто я.** 3 курс ИУ6 (программная инженерия), сижу в большой аудитории, далеко от экрана. Слышал про ChatGPT, Midjourney, видел демо Suno. NYT v OpenAI, SAG-AFTRA, Lionsgate — это для меня «что-то слышал, но не уверен что именно». Диффузия — знаю по слухам; «latent transformer» — пугает.

Лекция длинная — 75 мин, 39 слайдов. Сегодня посмотрел PNG-снимки и попытался представить, что бы я почувствовал.

---

## Per-slide reactions (sample 15 слайдов)

### s01 — Ice-breaker «Сгенерируем прямо сейчас» (Suno + Firefly)

**Что понял:** сейчас сделаем трек на suno.com или картинку на firefly.adobe.com, и это «3 года назад = $500–2000, сегодня = $0».
**Реакция:** «О, прикольно, наконец-то живое демо!» Suno я не слышал — заинтриговало. Сравнение «$500–2000 → $0» зашло, эмоциональный hook сработал.
**Минус:** мелкая надпись внизу — *«Live demo (внимание: пара дополнительных минут на демо) · резервный PNG если интернет недоступен»* — это «лектору», зачем мне это видеть? Designer-extra. Убрал бы.
**Также:** QR-блок справа внизу — белая пустая коробка с надписью «QR». Это не QR, это плейсхолдер. Если на лекции будет реальный QR — хорошо. Если плейсхолдер — выглядит «недоделанным».
**Вердикт:** 8/10 как hook, но «pair of extra minutes on demo» — лишний шум.

### s02 — Cover «AI в креативных индустриях и медиа · 08»

**Что понял:** название лекции, номер 08 декоративно.
**Реакция:** OK, classic cover. Большая «08» — приятно.
**Минус:** жёлтый pill «≥ 30% — failure budget» — это **МЕТОДИЧЕСКИЙ маркер**, я как студент не должен видеть «failure budget». Это для методиста / preподавателя. Designer-extra. Убрал бы.
**Subtitle:** «Что AI добавил, изменил и сломал — и где сказать "нет".» — хорошо, это hook.
**Вердикт:** 7/10. Уберите «failure budget» pill.

### s03 — Central question

**Что понял:** «Что AI сделал с creative к 2026 — и где сказать "нет"?»
**Реакция:** OK, чёткий вопрос. Двойная подсветка («Что AI сделал» жёлтым + «здесь AI не нужен» teal) помогает.
**Минус:** внизу 2 chip-pill — «Разделы 1-3: что AI сделал» и «Разделы 4-5: где сказать "нет"». Это «навигационный маркер» (которого по нашим правилам не должно быть). Я не нуждаюсь в роадмапе на этом слайде — он будет на s04 lecture-map. Designer-extra. Убрал бы.
**Вердикт:** 7/10.

### s04 — Lecture map (6 разделов)

**Что понял:** 6 карточек: 0 keystone, 1 ДОБАВИЛ, 2 ИЗМЕНИЛ, 3 СЛОМАЛ, 4 «AI не нужен», 5 «что делать», + Q&A.
**Реакция:** хорошо, читается за 5 сек. Жёлтая 0 = «вы здесь», teal — следующие. Понятно куда идём.
**Минус:** в карточке 0 написано «keystone» прямо так — это **методический термин**, мне как студенту слово «keystone» ничего не говорит. Лучше «ось лекции» или «главная мысль». Designer/orchestrator extra.
**Вердикт:** 8/10. Замените «keystone» на русский эквивалент.

### s05 — Keystone «AI добавил → изменил → сломал»

**Что понял:** три времени одного процесса — capabilities → экономика → юр. долг. Каждая карточка имеет один-два примера (Sora 2, RIAA v Suno, NYT v OpenAI).
**Реакция:** «О, это интересный фрейм!» Не «топ инструментов», а «3 времени». Запомню.
**Минус:** **Названия примеров RIAA, Sony, NYT, ScarJo** — для меня просто аббревиатуры, не имеют контекста на этом слайде. Я узнаю в Разделе 3, но здесь ещё не знаю кто это. Поэтому первый раз читаю как «какие-то английские буквы».
**Вердикт:** 8/10. Сам frame отличный — но «teaser» примеров без объяснения = шум. Лучше 1 универсальная фраза на каждое время, без аббревиатур.

### s05a — 3 семейства генеративных моделей

**Что понял:** diffusion / latent transformer / neural audio. Принцип, инструменты, «инженерное следствие».
**Реакция:** «О, это полезно — я хотел понять как работает.» Колонки structurally читаемые.
**Минус 1:** За 5 секунд я **НЕ ПОЙМУ что такое «autoregressive + diffusion»**, «latent space + temporal consistency» — это термины, которые мне как 3-куркеру нужны 5 минут на каждое объяснение. Один-два слова на «принцип» = недостаточно для меня (если лектор не расскажет более развёрнуто).
**Минус 2:** В §3.1 диффузия — этот термин я слышал, но «инженерное следствие "Commercial-safety зависит от training corpus, не от архитектуры"» — звучит академично. Я бы предпочёл «Firefly = безопасный, потому что Adobe платит за training data; Stable Diffusion = риск, потому что собран с интернета».
**Cognitive load:** очень высокий. 3 колонки × 4 строки × technical jargon = 30+ сек на чтение.
**Вердикт:** 6/10 — концепт правильный, но язык слишком академический для 3 курса. Перепишите «инженерное следствие» на более человеческий язык.

### s07 — Text-to-video 2026 (Sora 2 / Veo 3.1 / Kling 3.0)

**Что понял:** 3 модели + их характеристики. ELO #1 у Kling, Sora $0.10/сек, Veo $0.05/сек.
**Реакция:** «О, классно — конкретные цены и числа!» Хочу запомнить.
**Минус 1 (P0 — критично):** В subtitle жирно написано **«3 флагманские модели определяют состояние индустрии · [VFY-day-of для версий и цен в frontmatter]»** — последний кусок (`[VFY-day-of ...]`) — это **методический tag, который я НЕ должен видеть как студент**. Это «designer-extras leak». Очень бросается в глаза, отвлекает.
**Минус 2:** Sora 2 release reel block — пустая `[ FRAME ]` плейсхолдер. Если на лекции будет видео — отлично, если плейсхолдер — выглядит «не доделано».
**Минус 3 (низкий):** «60M creators» у Kling 3.0 — это маркетинговая цифра, не очень важна для меня.
**Урок для инженера:** хорошо, понятно — «25 сек не фильм, Lionsgate × Runway = augmentation».
**Вердикт:** 7/10 — концепт хороший, но VFY-tag leak и пустая плейсхолдер сильно бьют. P0 fix `[VFY-day-of]`.

### s08 — Character consistency

**Что понял:** Sora 2 cameos, MJ Omni Reference, Runway Director Mode — теперь character сохраняется через scene.
**Реакция:** OK, понятно. Числа (60% → 85%+) помогают.
**Минус 1 (P0 — критично):** **«Урок для инженера» yellow rounded box внизу ОБРЕЗАН** — я вижу только «УРОК ДЛЯ ИНЖЕНЕРА» заголовок и обрезанный текст: «Anti-hype: multi-scene drift после 5-10 scene'ов. Continuity supervisor — новая профессия creative-pipeline...» — текст уходит ниже видимой области слайда. **Это рендеринг-баг или text overflow.** Я не могу прочитать урок.
**Минус 2:** Grid demo справа — пустые frame 1, frame 2, frame 3, frame 4 (4 серых квадрата). Без реальных скриншотов это не «доказывает» character consistency, это просто гарантирует «вот тут будут картинки». Если на лекции будут реальные — ОК, если нет — слабо.
**Минус 3:** «$1B+ deal» — что за Disney $1B+ deal? Не объяснено на слайде; новость недавняя.
**Вердикт:** 5/10. P0: text overflow Урок-блок (нужен fix). P1: пустые frames.

### s09 — Voice cloning + multilingual dubbing

**Что понял:** ElevenLabs делает voice clone из 1 минуты в 32+ языков. $50-500 → <$1 / мин. Deutsche Telekom, Klarna используют.
**Реакция:** «О, я слышал про ElevenLabs!» Цена удивляет. Хочу запомнить.
**Минус 1:** voice library с 4 «Voice 1, Voice 2, Voice 3, Voice 4» — это плейсхолдер; на лекции будет действительно играть звук? Без аудио я не понимаю, насколько это «магия».
**Минус 2:** «Voice 4: ScarJo-like soundalike (s9 caveat)» — **«(s9 caveat)»** — это **cross-slide reference visible на слайде**, designer-extra. Что значит «s9 caveat»? Я как студент не знаю что есть «s9» (это сам слайд?). Уберите.
**Урок для инженера:** хорошо подан — ScarJo v OpenAI «Sky» = consent risk даже для soundalike.
**Вердикт:** 7/10. P1 fix: «(s9 caveat)» visible.

### s10 — World models — Genie 3

**Что понял:** Genie 3 = text → playable 3D world в реальном времени @ 24 fps.
**Реакция:** «О, это другое — не video, а интерактивная среда!» Интересно.
**Минус 1:** demo frame — плейсхолдер «medieval castle on mountain · light wind» (placeholder text!). Без реального скриншота это не убеждает. Жаль.
**Минус 2:** «720p · мин. consistency» — что значит «мин. consistency»? Минимальная? Несколько минут? Двусмысленно (минуты vs «минимальная»).
**Минус 3:** Урок-блок внизу обрезан (как на s08), не вижу полный текст.
**Вердикт:** 6/10. P0: плейсхолдер + обрезка.

### s10a (на PNG — это s-12) — Russian context

**Что понял:** Kandinsky 6.0, Yandex Шедеврум, SymFormer — RU аналоги. Не frontier на видео/музыке.
**Реакция:** «О, это про нас. Полезно!» Side-by-side Kandinsky vs Kling — хорошо.
**Минус 1 (P0 — палитра нарушена):** Status-pills используют **зелёный** («конкурентен») и **красный** («gap structural») цвета. Это нарушение Ocean palette (Ocean + Teal + Gold only). Anti-pattern #3 generic blue/red palettes.
**Минус 2:** «Минцифры 18.03.2026» — для меня это значит «государство хочет что-то с AI»; на лекции пояснят. На слайде кратко OK.
**Минус 3:** видеть «гэп structural» / «конкурентен» / «ниже ElevenLabs» / «в процессе» — слишком много status-меток, теряется. 4 области × 1 pill = 4 пилла, можно проще.
**Вердикт:** 7/10 как контент. Срочно: убрать красный + зелёный.

### s14 — Cost-collapse table

**Что понял:** таблица: 1 image $50-200 → $0-0.25 (200×–10000×); 50 product images $1k-25k → $0-1.50 (>1000×); 1 мин 720p video $1k-50k → $6 (150×–8000×); dub /мин $50-500 → <$1.
**Реакция:** «Ого, числа поражают.» Хочу сфоткать.
**Минус 1 (P0):** **«[VFY-day-of для версий и цен в frontmatter]»** в footer источника — снова visible designer-extra. Опять.
**Минус 2:** «MIDDLE-TIER ≠ FREE» жёлтая колонка с $400M (Adobe Firefly) — полезный counter-point, но я не сразу понимаю связь. Лектор пояснит.
**Вердикт:** 8/10 без VFY-tag. P0: убрать VFY.

### s15 — Скорость дни → секунды

**Что понял:** concept art дни → 5-60 сек; B-roll часы → 5-60 сек; dub недели → минуты; concept exploration полу-неделя → минуты·10×+.
**Реакция:** хорошо, понятно. Стрелки помогают.
**Минус 1 (P0 — палитра):** «ДО» колонки имеют **красную обводку** + красный текст. Это нарушение Ocean palette. Anti-pattern #3.
**Минус 2:** в последней строке «иерация плотнее» — **опечатка** (должно быть «итерация»). Бросается в глаза.
**Минус 3:** Урок для инженера — «Inжeнерный урок» — первая буква **латинская «I»** вместо кириллической «И». Опечатка / mixed scripts. Бросается.
**Вердикт:** 7/10. P0: уберите красный + 2 опечатки.

### s20 — «AI vs copyright» — 4 категории исков

**Что понял:** 4 категории: training scraping / output similarity / style mimicry / voice-likeness. Каждая со связанным case.
**Реакция:** хорошо, 2×2 матрица читается.
**Минус 1:** внизу «Конкретные landmark-cases каждой категории — **s21-s27**.» — это **cross-slide reference** «→ s21-s27», designer-extra. Уберите. Я не знаю что s21 и s27 значат.
**Минус 2:** имена case'ов (NYT, Andersen, ScarJo, SAG-AFTRA, Korea) — я их видел в Разделе 0, но всё ещё не знаю что это. Лектор должен пояснить устно.
**Урок для инженера:** хороший — «4 разных категории риска, смотри какая применима».
**Вердикт:** 7/10. P1: уберите «— s21-s27».

### s21–s25 — Lawsuit cases (NYT, Getty, Andersen, RIAA, Reuters)

**Что понял для каждого:** дата + ключевая цифра + урок. Хронология справа.
**Общая реакция:** «5 слайдов подряд с одинаковым layout — становится скучновато.» Anti-pattern #6 (repeating identical layouts).
**Минус 1 (P0 — критично, повторяется на 5 слайдах):** ВСЕ 5 case-слайдов имеют **`[ news screenshot ]` плейсхолдер** в центре главного box'а — серый квадрат с текстом «[ news screenshot ]». Это очевидно «не доделано». Без реальных Bloomberg / Bird & Bird / docket / RIAA / Reed Smith скриншотов — это просто пустые boxes. Если на лекции будут реальные — ОК; если нет — слабо.
**Минус 2 (P0 — палитра нарушена):** s22 (Getty) использует **зелёный pill** «04 ноя 2025 UK Stability won». s25 (Reuters) использует **красный** «⚠ Caveat» pill. Палитра нарушена на нескольких слайдах подряд.
**Минус 3 (P1 — опечатка):** s22 хронология — **«Suprior»** (должно быть «Superior»). Бросается в глаза.
**Минус 4 (P1):** «20M ChatGPT logs» (s21) — это про OpenAI должна выдать 20 миллионов логов суда? Контекст недостаточен без устного.
**Cognitive load:** на 5 слайдов подряд с похожим layout — устаю к 3-му слайду, отвлекаюсь к 5-му.
**Вердикт:** 5/10 средняя. Уроки для инженера — это сильно. Но 5× плейсхолдер + 2 палитры breach + опечатка = плохое впечатление. P0 fix: real screenshots / альтернативный layout (icon вместо placeholder).

### s26 — Arup CFO deepfake $25.6M

**Что понял:** finance worker заплатил $25.6M после deepfake video-call с CFO + colleagues.
**Реакция:** «Ого, страшно!» Это меня зацепит. Сценарий атаки (5 шагов) — отлично визуально.
**Минус 1 (P0 — палитра):** шаг 5 «$25.6M gone» — **красный box**. Палитра нарушена.
**Минус 2:** CNN screenshot — текст-only headline в Ocean box, OK.
**Урок для инженера:** «Видеозвонок ≠ identity proof, нужна out-of-band verification» — отлично, **запомню**.
**Cognitive load:** 5-шагов сценарий хорошо разбит на blocks.
**Вердикт:** 8/10 как кейс. P0: уберите красный.

### s27 — Korea schoolgirl deepfake

**Что понял:** >230 Telegram-чатов, 6500 takedown, 74% подозреваемых 10-19 лет, 793 reported / 16 prosecuted.
**Реакция:** «Это серьёзно.» Числа shock-эффект. Хорошо, что **без визуалов** (sensitive case).
**Минус 1:** «Только text headline — без визуалов (sensitive case)» — это **методический комментарий лектору**, видимый студенту. Должен быть в speaker notes, не на слайде. Designer-extra. Уберите.
**Минус 2:** «text only» в metadata вверху — то же самое, методический маркер.
**Урок для инженера:** «Safety layer (NSFW detection + age verification + reporting pipeline) ДО launch» — actionable. Запомню.
**Вердикт:** 7/10. Уберите методические комментарии.

### s28 — Slop / model collapse

**Что понял:** Google AI Overview «put glue on pizza», «eat one rock per day»; Shumailov 2024 — recursive training деградирует модель.
**Реакция:** Анекдот про glue+pizza — смешно и shocking. Запомню.
**Минус 1:** «source: Reddit joke 11 years ago» / «source: Onion satire» — **красный текст** (палитра нарушена).
**Минус 2:** «AI Overview: "add ⅛ cup of non-toxic glue to the sauce"» / «AI Overview: "at least one small rock per day"» — тоже красным выделено. Подсвечено как «плохое», но **красный = нарушение Ocean**.
**Вердикт:** 8/10 как story. P0: красный → Ocean accent.

### s30 — Marketing backlash (Toys R Us + Coca-Cola)

**Что понял:** Toys R Us Cannes 2024 — positive sentiment +12.2% → +3.4%, negative 13.5% → 53.4%. «−8.8 pp» / «+39.9 pp».
**Реакция:** числа shockingly bad. Joe Russo цитата «AI ad fucking sucks» — запомню (хотя на лекции лектор может смягчить).
**Минус 1 (P0 — палитра):** **«ПОСЛЕ» = красный**, текст «−8.8 pp» = красный. Палитра нарушена.
**Минус 2:** «+12.2%» в маленьком жёлтом квадрате выглядит обрезанным («+12.2 / %» с переносом строки). Layout issue.
**Урок для инженера:** «Brand-trust риск = sentiment swing, не CTR» — actionable.
**Вердикт:** 7/10. P0: уберите красный.

### s33 — 4 критерия отказа

**Что понял:** 4 критерия: training data license / output similarity / voice-likeness consent / brand-trust риск.
**Реакция:** OK, это main deliverable §4. Понятно.
**Минус 1 (P0 — layout):** под заголовком «Firefly = да · Stable Diffusion = риски» **есть обрезанный текст в виде** «х сравнения...» **под пиллом** — какой-то OVERLAP. Текст в пилле перекрывает второй уровень текста. Render glitch.
**Минус 2:** «Технический контроль обязателен» — что это значит? Слишком общо. Я как студент не понимаю «технический контроль» — какие именно проверки.
**Вердикт:** 6/10. P0: overlap fix.

### s35 — YouTube AI thumbnails — 47.3% creators dropped

**Что понял:** 47.3% дропнули AI thumbnails; -22% CTR, -19% CTR, -61.8% first-15-sec drop-off.
**Реакция:** «Цифры shocking. Хорошо, что end-user rejection — это реальный signal.»
**Минус 1 (P0):** subtitle — **«Social Blade Creator Survey · Dec 2025 [VFY-day-of]»** — visible VFY-tag. Снова. **Третий слайд с VFY leak.**
**Минус 2 (P0 — палитра):** в нижнем блоке «ПРИЧИНЫ DROP-OFF» три числа: «-22%», «-19%», «-61.8%» — **выглядят красным/coral**. Палитра нарушена.
**Минус 3:** Урок для инженера обрезан (как s08, s10).
**Вердикт:** 5/10. P0: VFY leak + красный + обрезка.

### s38 — Q&A

**Что понял:** Q&A слайд, central question recap + 3 backup-prompts.
**Реакция:** OK, стандарт. Большой жёлтый «Q&A?» левый — приятно визуально.
**Минус:** «BACKUP PROMPTS» — методический термин («backup» для лектора). Я как студент могу не понять что это «варианты тем для обсуждения». Можно «вопросы для дискуссии».
**Вердикт:** 7/10.

### s39 — Closing

**Что понял:** Спасибо за внимание + анонс Лекции 9 (авиакосмос).
**Реакция:** OK, classy closing.
**Вердикт:** 8/10. **Хороший** — лекция явно закрывается.

---

## Overall ratings (по 10-балльной шкале)

| Metric | Score | Комментарий |
|---|---|---|
| **Engagement** | **6/10** | Hook сильный (s01, cost-collapse, deepfake $25.6M, glue+pizza, Korea numbers). НО 5 case-слайдов подряд (s21-s25) с одинаковым layout + плейсхолдеры = drift. |
| **Comprehension** | **5/10** | Без подготовки: «3 семейства моделей» (s05a) слишком академично. Case-имена (NYT, Andersen, RIAA) не объяснены contextually на keystone (s05) и copyright matrix (s20). Жаргон («latent space + temporal consistency», «autoregressive + diffusion») — нужно перевести. |
| **Memorability** | **6/10** | Через 2 нед запомню: cost-collapse table (s14), Arup $25.6M (s26), Korea numbers (s27), glue+pizza (s28), keystone «добавил → изменил → сломал». Не запомню: ELO scores, отдельные lawsuit names (NYT vs Andersen vs Getty размылются). |
| **LO achievability** | **6/10** | LO1 (классификация по 4 областям) — ✓ achievable. LO2 (применимость через mental model) — risk: 3 семейства слишком кратко. LO4 (анализ landmark кейса) — ✓ если лектор устно вытянет. LO5 (критерии отказа) — ✓ s33 + s37 хорошо подведены. |
| **Visual quality** | **5/10** | Множественные palette violations (red/green pills на 7+ слайдах), плейсхолдеры на 5 case slides, VFY-tag leak на 3+ слайдах, text overflow на 3+ слайдах, опечатки. Без визуальной полировки — выглядит как black draft. |

---

## Top P0 issues (БЛОКИРУЮТ GATE B — обязательно fix)

1. **P0 — Designer-extras visible на ≥5 слайдах:**
   - `[VFY-day-of для версий и цен в frontmatter]` visible body на **s07, s14**
   - `[VFY-day-of]` visible на **s35**
   - «(s9 caveat)» visible на **s09**
   - «— s21-s27» visible на **s20**
   - «keystone» (jargon) на **s04**
   - «failure budget» pill на **s02 cover**
   - «Только text headline — без визуалов (sensitive case)» на **s27** (методический комментарий)
   - «text only» metadata на **s27**
   - «Live demo (внимание: пара дополнительных минут на демо)» footer **s01**

2. **P0 — Ocean palette нарушена на ≥7 слайдах** (Anti-pattern #3):
   - **Зелёные** chips/pills: s12 (Russian context «конкурентен»), s22 (Getty UK win), s24 (RIAA settlements 2×)
   - **Красные** elements: s12 (Russian context «gap structural»), s15 (ДО boxes border + текст), s25 (Caveat pill), s26 (шаг 5 «$25.6M gone»), s28 (source labels + Overview quotes), s29 (Drew Ortiz pill), s30 (ПОСЛЕ + −8.8 pp), s35 (drop-off percentages)
   - Эти цвета — нарушения visual identity курса. Должны быть Ocean / Teal / Gold accent.

3. **P0 — Text overflow / обрезка «Урок для инженера» внизу на ≥3 слайдах:**
   - **s08** Character consistency — текст урока обрезан, не виден
   - **s10** Genie 3 — текст урока частично обрезан
   - **s35** YouTube thumbnails — текст урока частично обрезан
   - Yellow Ocean rounded box должен быть полностью видим внутри slide bounds.

4. **P0 — Плейсхолдеры на 5 case-слайдах (s21–s25):**
   - Каждый имеет `[ news screenshot ]` серый блок — без реального screenshot выглядит «недоделано». Plan §7 требует Bloomberg Law, Bird & Bird, docket, RIAA press, Reed Smith screenshots. Если они не доступны — **redesign layout** (например, замените на icon-схему с key quotes + timeline).
   - 5 слайдов подряд с одинаковым layout (Anti-pattern #6 «repeating identical layouts») — добавьте variation хотя бы на 1-2 cases.

5. **P0 — Опечатки visible:**
   - **s15** «иерация плотнее» → «итерация плотнее»
   - **s15** «Inжeнерный урок» (mixed Latin/Cyrillic «I») → «Инженерный урок»
   - **s22** «Suprior» → «Superior»

## Top P1 issues (сильно желательно fix)

1. **P1 — Layout glitch s33** — пилл «Firefly = да · Stable Diffusion = риски» overlap с предыдущей строкой (хвост подписи виден под пиллом).
2. **P1 — s05a 3 семейства слишком академично** для 3 курса. «Latent space + temporal consistency» / «autoregressive + diffusion» — нужен перевод на инженерный язык 1 строкой.
3. **P1 — s12 Russian context — слишком плотно** (4 области + 4 pills + legal block + Урок-блок). Cognitive load высокий за 2 мин.
4. **P1 — s10 Genie 3 «720p · мин. consistency»** — двусмысленно (минуты vs минимальная).
5. **P1 — s05 keystone teaser имён без объяснения** (RIAA, Sony, NYT, ScarJo на первом появлении) — лучше generic фразы или 1-словные категории.

## Top P2 issues (polish)

1. **P2 — Slides s21-s25 с одинаковым layout** — Anti-pattern #6. Вариативность поможет attention.
2. **P2 — «Backup prompts»** на s38 → «Вопросы для дискуссии».
3. **P2 — `[ FRAME ]` плейсхолдер s07** Sora 2 release reel — либо real screenshot, либо stylized icon.
4. **P2 — s17 Урок-блок может быть обрезан** (видна верхняя строка). Проверить.

---

## Designer-Added Extras (что бы убрал как студент)

- **s02 cover:** «≥ 30% — failure budget» pill — методический маркер, видимый студенту. УБРАТЬ.
- **s03 central question:** chips «Разделы 1-3 / Разделы 4-5» внизу — навигационные маркеры. УБРАТЬ.
- **s04 lecture map:** «keystone» в карточке 0 — жаргон, заменить на «ось лекции».
- **s07:** `[VFY-day-of для версий и цен в frontmatter]` в subtitle. УБРАТЬ.
- **s08:** Урок-блок обрезан — fix layout.
- **s09:** «(s9 caveat)» — cross-slide reference. УБРАТЬ.
- **s14:** `[VFY-day-of для версий и цен в frontmatter]` в footer. УБРАТЬ.
- **s20:** «— s21-s27» в footer caption. УБРАТЬ.
- **s27:** «Только text headline — без визуалов (sensitive case)» + «text only» metadata. ОБА — методические маркеры. УБРАТЬ.
- **s35:** `[VFY-day-of]` в subtitle. УБРАТЬ.
- **s01:** «Live demo (внимание: пара дополнительных минут на демо)» footer — info для лектора. УБРАТЬ.

---

## Кандидаты на удаление / merge (как студент)

- **s21 + s22 + s23 — рассмотреть merge** в «Copyright cases overview» с 3 mini-timelines + 1 общий screenshot, если real screenshots не будут доступны. Сейчас 3 слайда подряд с пустыми «[news screenshot]» = repetition.
- **s24 (RIAA) — оставить отдельно** (это story success «2 of 3 settled»).
- **s25 (Reuters) — оставить отдельно** (важный first US fair-use rejection).
- **s35 (YouTube thumbnails)** — мог бы быть merged в §3 как case 12 «end-user rejection», но сейчас он в §4 как мост к чек-листу. Owner-decision.

---

## Pacing perception

- Раздел 0 (s01-s05a, ~9.5 мин) — **OK pacing**. Live demo задаёт энергию.
- Раздел 1 (s06-s11, ~12 мин) — **OK**, разнообразие capabilities.
- Раздел 2 (s13-s17, ~10.5 мин) — **OK** до s17, который имеет text-heavy displacement data + потенциальную обрезку Урок-блока.
- Раздел 3 (s19-s31, ~24 мин) — **здесь problem**. 12 case-слайдов подряд = energy drop. Минута 45-65 = «отвлёкся бы, полез в телефон» (особенно s21-s25 с одинаковым layout). Plan правильный (failure budget concentrate в одной секции), но visual variety нужна — иначе fatigue.
- Раздел 4 (s32-s35, ~7.5 мин) — **OK**, возвращает в актionable mode.
- Раздел 5-6 (s36-s39, ~7 мин) — **OK closing**.

**Studied attention curve:** energy ~100% при s01 → ~75% к s11 → fatigue к s25 → recovery в s33 → energy ~60% к s39.

---

## 4-level verdict

**REVISE**

Причины:
1. **≥5 P0 issues** требуют fix перед GATE B. Counter-check policy: ≥5 P0 = автоматический REVISE.
2. Palette violations на 7+ слайдах = systemic, не one-off polish.
3. Designer-extras leaks на ≥9 слайдах = systemic.
4. Text overflow / обрезка Урок-блока на ≥3 слайдах = render quality.
5. 5 case-слайдов с плейсхолдерами `[news screenshot]` = «недоделано» feeling.

**ApprovE-WITH-POLISH невозможен**: проблемы visual+content+layout systemic, не косметические.

**REJECT не нужен**: контент сильный (keystone, ось 3 времён, чёткие уроки для инженера, конкретные cases с механизмами). После цикла fix визуала + palette + designer-extras — APPROVE-WITH-POLISH достижим.

---

**Конкретный recommended fix-cycle:**
1. Global grep по PNG-видимому слою + slides/*.md на designer-extras (VFY tags, s-references, «keystone» жаргон, «failure budget») — 0 hits после fix.
2. Palette violation sweep — все красные/зелёные → Ocean palette accents (teal для positive, Ocean для standard, gold для emphasis).
3. Text overflow fix на s08, s10, s35 — увеличить slide bottom margin или сократить текст Урок-блока.
4. Case slides s21-s25 — реальные screenshots ИЛИ alternative layout (icon-схема + key quote + timeline, без плейсхолдера).
5. Опечатки s15 (×2) + s22.

После — re-snapshot + re-review.

---

*End of student-simulator report v1.*
