# Reader Simulation — text-only mode — Plan-v1 — Лекция 4

**Date:** 2026-05-13
**Reader:** студент 3 курса инженерного факультета, без медицинского/фарм бэкграунда, базовая ML-подготовка, умеет считать sens/spec, видел Лекцию 1
**File reviewed:** `notes/lecture-4-review/plan-v1.md`
**Mode:** text-only (markdown plan, no slide renders)
**Reading time:** примерно 45-55 минут, чтобы вдумчиво прочитать; ещё минут 20, чтобы понять секцию drug discovery (s14-18) — там я застревал.

---

## Overall verdict

**APPROVE-WITH-POLISH**

Если бы мне это дали как handout перед лекцией, я бы пошёл на лекцию с уверенностью, что я готов. План структурный, центральный вопрос держится через всю лекцию, есть конкретные numbers и cases (не «AI спасёт всё»). НО: есть три места, где я как студент 3 курса застревал — секция drug discovery (s15-18) грузит меня терминологией pharma, которую я не знаю; s24 (responsibility quadrant) описан так, что я понимаю concept, но не уверен, могу ли я объяснить его одногруппнику; и s19 micro-exercise (что мне делать за 8 минут) звучит чуть размыто. Это polish, не reject — основной нарратив работает.

---

## Reading-flow blockers (P0)

### P0-1 — Slide s18 (FDA AI/ML framework, PCCP)

**My experience:** Я прочитал этот слайд два раза. На второй раз понял, что PCCP — это «пред-объявленный план изменений модели», но не понял, *почему* это innovation. Я инженер, я знаю что модели continuous-deploy с CI/CD. Зачем для медицины это innovation?

**Specific obstacle:** Plan говорит «**Это innovation 2023-2024.**» но не объясняет, что было ДО PCCP. Я не знаю, что традиционный FDA approval требует new submission per update — это не очевидно для не-медика. «Predetermined change control plan» — само словосочетание длинное и непрозрачное.

**Fix recommendation:** Добавить одно предложение «До PCCP: каждое обновление модели требовало новой full submission в FDA (~12-18 мес). С PCCP: vendor pre-declares допустимые updates → может обновлять без re-submission». Без этого контраста я не понимаю, что это упрощение.

### P0-2 — Slide s17 (DSP-1181 timeline + Exscientia CEO firing + Recursion merger)

**My experience:** Этот слайд — самый перегруженный в лекции. На первое чтение я понял: DSP-1181 — первый AI-designed drug, discontinued. На второе чтение я заметил: «Exscientia CEO Hopkins fired 2025; merger talks с Recursion 2024». На третье чтение я подумал: «А зачем мне знать про CEO firing? И что такое Recursion?»

**Specific obstacle:** Слайд хочет рассказать ДВЕ истории одновременно: (1) DSP-1181 efficacy reality check + (2) Exscientia корпоративная turbulence. Для центрального вопроса нужна только (1). История про CEO firing и Recursion merger мне как студенту НЕ помогает понять «обещания vs реальность» — она просто говорит «всё ещё хуже». Я не вижу, какой инженерный урок я должен из этого извлечь.

**Fix recommendation:** Убрать всё про Exscientia 2025 (CEO firing, Recursion merger) — это P1 polish, который перегружает P0 narrative. Оставить timeline до 2022 discontinuation + insight «AI ускорил design, эффективность — отдельная задача». Если хочется upd 2025 — speaker notes, не visible content.

---

## Confusion / friction points (P1)

### P1-1 — Slide s15 (Drug discovery pipeline, 5 stages)

**My experience:** Я понял pipeline в общем (target → hit → lead → preclinical → clinical), но specific термины — «target identification», «hit discovery», «lead optimization», «ADMET» (упомянуто в speaker notes s16) — это не очевидные для инженера слова. Я угадал из контекста, но угадывание = friction.

**Specific obstacle:** Эти 5 stages — pharma jargon. Plan ожидает, что я знаю разницу между «hit» и «lead» в drug discovery. Я не знаю. Лекция 4 для инженеров — нужно explain эти 2 слова в одном предложении.

**Fix recommendation:** В speaker notes s15 добавить: «Hit = молекула, у которой есть начальный signal активности vs target. Lead = hit, доведённый до состояния, готового для preclinical (улучшенная affinity, selectivity, stability). Между ними — лет лабораторной работы.» На слайде сами labels могут оставаться короткими.

### P1-2 — Slide s10 (sensitivity / specificity matrix)

**My experience:** Я могу считать sens/spec — я их видел на ML-курсе. Но plan хочет «mat-применение» и подразумевает, что я знаю Bayes. Я Bayes знаю по формуле P(A|B) = ..., но *intuition* для prior probability в medical screening (low prevalence → high false positive even with high specificity) — это второй порядок понимания. Plan не упоминает prevalence/PPV/NPV, хотя это критическая часть medical AI evaluation.

**Specific obstacle:** Если лекция говорит «AI имеет sens 0.94 и spec 0.89», я могу подумать «отлично, 94% точность!» — но в реальности, при prevalence 1% патологии, PPV будет ~8%. Это критическая интуиция для medical context, и plan её не вводит.

**Fix recommendation:** Либо явно добавить prevalence/PPV box в s10 (4-я метрика), либо отметить в speaker notes: «Sens/spec не зависят от prevalence; PPV (predictive value) — зависит. Это часто причина, почему "94% accuracy" звучит хорошо, но в screening даёт много false positives.» Это даёт мне «aha moment».

### P1-3 — Slide s6 (4-type matrix: scope × modality)

**My experience:** Я понимаю matrix как структуру, но axes — «scope: single patient ↔ population/pharma» и «modality: image/signal ↔ text/molecule» — это не self-evident axes. Почему именно эти 2 оси? Почему не «narrow ML / foundation model» vs «approved / experimental»? Plan не объясняет выбор axes.

**Specific obstacle:** Plan говорит «4 типа AI-применений по 2 осям», но axes ощущаются ad-hoc — придумали, чтобы получить 4 квадранта, а не органичная классификация. Personalized medicine «text/molecule + single patient» — а почему не «text/signal»? ЭКГ AI — signal + single patient, но он в «диагностике» квадрант.

**Fix recommendation:** Либо обосновать axes одной фразой в speaker notes («modality важна, потому что определяет, какой ML stack используется — CV vs NLP vs generative chemistry»; «scope важен, потому что определяет регуляторный pathway — single patient = device, population = analytics»). Либо упростить до linear list 4 types без matrix gimmick. Matrix должна service the content, не наоборот.

### P1-4 — Slide s19 (micro-exercise — что я должен сделать за 8 минут)

**My experience:** Plan говорит: 3 мин промпт + 3 мин read + 2 мин reveal. Я понимаю, что я должен сделать. НО: я не понимаю, что я должен *вынести* из упражнения. Plan говорит «LLM pattern + LLM anti-pattern», но это абстрактно. Какой output? Я должен написать что-то? Поднять руку? Заполнить чек-лист?

**Specific obstacle:** «Step 2: заметь (a) error/неточность (b) приводит ли AI конкретные числа (c) пример adequate?» — это 3 вопроса, я должен ответить на все три? Или выбрать один? Что я делаю с ответами — записываю в тетрадь, обсуждаю с соседом, никому ничего не показываю до reveal?

Кроме того: «обсуждение 2-3 ответов аудитории» — это ОЧЕНЬ зависит от того, поднимут ли студенты руки. Скорее всего, 2 минуты на это мало. Plan не имеет fallback на случай тишины.

**Fix recommendation:** Сделать concrete instruction: «Открой web-chat → задай вот этот промпт (готовый текст на слайде) → ответ AI скопируй → отметь карандашом на распечатке (или в notes app): 1 неточность ИЛИ 1 unverifiable claim ИЛИ 1 место, где объяснение слишком абстрактное. На reveal — лектор спросит "у кого нашёлся пример?" → 2-3 студента читают (1 минута каждый).» Без этого 8 минут расплываются.

### P1-5 — Slide s13 vs s21 (Bias — повтор?)

**My experience:** На s13 рассказывают «3 bias case-cards» — dermatology, pulse-oximeter, Obermeyer. На s21 — deep-dive Obermeyer 2019. Когда я дошёл до s21, я подумал «но это же уже было на s13?»

**Specific obstacle:** Plan признаёт это: «Note: bias уже коротко затронут на s13 — здесь deep-dive с одним paper.» Но для меня как студента-читателя это всё равно ощущается как повтор. На s13 я уже услышал «proxy spending вместо severity», на s21 — те же слова. Между s13 и s21 — 7 слайдов (s14-20), но я помню Obermeyer с s13.

**Fix recommendation:** Один из двух подходов:
- (A) На s13 — НЕ упоминать Obermeyer вообще; оставить только dermatology + pulse-oximeter. Obermeyer = exclusively s21.
- (B) На s21 — НЕ повторять mechanism (3 boxes goal/proxy/bias); вместо этого углубиться в «как это починили + что инженер должен извлечь» — actionable angle, который s13 не покрывает.

Текущее состояние = 2 слайда говорят одно и то же, и я не помню к концу лекции, какие 3 bias case я слышал.

### P1-6 — Slide s23 (Change Healthcare breach) — какое отношение это имеет к AI?

**My experience:** Слайд про ransomware. 190M affected, $2-3B recovery, HIPAA, GDPR, ФЗ-152. Я понимаю — медицинские данные важны для защиты. Но это про *security*, не про *AI*. Где AI в этом слайде?

**Specific obstacle:** Plan связывает это с medical AI через «training data — нужно деперсонализировать», но эта связь слабая. ransomware attack на Change Healthcare — не AI-инцидент. Я как студент думаю: «зачем это в AI-лекции?»

**Fix recommendation:** Если security слайд нужен — связь с AI должна быть explicit и в visible content, не только speaker notes. Например: «Medical AI training datasets — наследуют security risk medical data. mosmed.ai обрабатывает 12M+ images; что если кто-то ex-filtrate dataset?» Либо переместить s23 в seminar/material и в лекции иметь только 1 строчку «security — отдельный pillar; см. семинар». 3 минуты в 75-мин лекции — это много для слайда, где AI = marginal.

### P1-7 — Slide s25 (3-jurisdiction regulation comparison)

**My experience:** Я понимаю что US/EU/RU имеют разные подходы. Plan вводит 3 термина в одном слайде: SaMD, PCCP, MDR, CE-mark, Conformity Assessment, ГОСТ Р 59921. Это много новых аббревиатур на 2 минуты.

**Specific obstacle:** Я не запомню эти термины через 2 недели. И понимаю, что слайд хочет дать панораму, не заставить запоминать — но тогда зачем мне эти конкретные аббревиатуры? Что я должен вынести?

**Fix recommendation:** Сжать до «3 jurisdictions, все классифицируют medical AI как high-risk. Различия — в process (centralized FDA vs distributed EU notified bodies vs RU Росздравнадзор). Engineering takeaway: deploying medical AI = projecting в 3 different compliance pipelines.» Аббревиатуры — в speaker notes как reference, не как visible content.

---

## Polish / nice-to-have (P2)

### P2-1 — Slide s14 (mid-lecture callback) — нужен ли он?

Я понимаю, что это структурный «pause beat». Но 1 минута на «return to central question» в плотной 75-мин лекции — это luxury. Я как студент могу подумать «это filler». Альтернатива: 30 секунд устного callback на старте s15, без отдельного слайда.

### P2-2 — Slide s3 + s4 (poll + reveal) — длина

3.5 минуты на opening poll. Это много для лекции, где central content начинается на s5. Я как студент терпеливый, но если опрос затянется, теряется энергия. Можно сжать до 1 минуты «один вопрос — руки — reveal цифры».

### P2-3 — Слова «mat-применение», «mat-prerequisites» в плане

В плане s10 написано «mat-применение». Это разговорное сокращение. Я понимаю, что это для self, не для слайда — но если попадёт в slide content, выглядит непрофессионально.

### P2-4 — «Хосзу-роль» в glossary (item 24)

«Хосзу-роль (Hospital / clinic operator)» — я не понимаю это слово. Это опечатка? Транслит? Я нагуглил — не нашёл. Если это не общеупотребимый термин, в glossary его быть не должно.

### P2-5 — Russian context — local color, не интеграция

mosmed.ai (s12) — отлично интегрировано. Но другие RU отсылки — Sber AI Lab «параллельная история» (s17 notes), GigaChat/YandexGPT «add as options» (s19 notes), Cognitive Agro Pilot (s28 teaser) — ощущаются как «вставка для местного контента», а не органичная часть narrative. Я как студент RU аудитории это замечаю — не критично, но patchy.

---

## Section-by-section reading log

### Section 0 (slides 1-5)

Чтение приятное. Hook через live demo (mosmed.ai или AlphaFold) — это сильно, я бы реально проснулся. Poll на s3 + reveal на s4 — стандартная техника, работает. Central question на s5 — чёткий, я понимаю, что лекция отвечает на 2 связанных вопроса (что сбылось + кто отвечает). Roadmap присутствует. **Темп ощущается ОК, но 9 минут на opening — на грани. Я бы хотел content начался на минуте 6.**

### Section 1 (slides 6-8)

s6 — 4-type matrix с axes, которые я не сразу принял (см. P1-3). s7 — FDA growth bar chart, понятный. s8 — «зачем медицина для инженера» — этот слайд лично мне резонирует, я инженер, я хочу понять, что в этой лекции для меня. **3 reason cards хорошо работают.** Темп 7 минут — нормально.

### Section 2 (slides 9-13)

Это **сильная секция**. s9 — CV pipeline, понятная. s10 — sens/spec, я могу применить мат-знания (с caveat про prevalence — P1-2). s11 — AI vs радиолог — очень крутой слайд, потому что разрушает «AI лучше человека» миф цифрами. s12 — mosmed.ai concrete case с Russian context, evidence для central question. s13 — bias studies, важный, но overlap с s21 (см. P1-5).

**14 минут — насыщенно. Я бы вышел из этой секции с ощущением, что AI-диагностика — это реально, измеримо, но имеет известные failure modes.** Это работает.

### Section 3 (slides 14-18)

Это **самая трудная для меня секция** как для не-медика. s14 — pause beat (P2-1). s15 — drug discovery pipeline; я понял в общем, но термины «hit», «lead» требуют explain (P1-1). s16 — AlphaFold + AlphaProteo; впечатляет (200M структур, Нобель), но я как инженер задаю вопрос «и что? как это превращается в drug?» Plan отвечает на s17, но связь между s16 и s17 не очень explicit.

s17 — overloaded (P0-2). s18 — FDA framework, blocker (P0-1).

**14 минут на эту секцию — мало для не-медика.** Я бы вышел с пониманием «AlphaFold = крутой, DSP-1181 = маркетинг ≠ реальность», но без ясной mental модели «почему drug discovery 12 мес vs 4-5 лет — это разные claims».

### Section 4 (slide 19)

Micro-exercise (P1-4). Я понимаю задачу в общем, но не уверен в output. Бы прошёл, но без сильного «aha moment». **8 минут — может быть мало, если discussion расплывётся.**

### Section 5 (slides 20-25)

s20 — transition, ОК. s21 — Obermeyer deep, повтор с s13 (P1-5). s22 — NEDA Tessa, **это сильный слайд** (concrete harm, конкретный таймлайн «3 дня от launch до suspension»). s23 — Change Healthcare, слабая связь с AI (P1-6). s24 — responsibility quadrant, **core слайд лекции, отвечает на central question**. s25 — 3-jurisdiction comparison, перегружен аббревиатурами (P1-7).

**14 минут — сообразно. Я бы вышел с ощущением, что есть framework ответственности (s24), но не уверен, могу ли я его объяснить одногруппнику без слайда.**

### Section 6 (slides 26-29)

s26 — 3 takeaways, чёткие, mapping к LO явный. s27 — closing line «Врач решает. AI подсказывает. Инженер обеспечивает» — **это сильно**, эмоциональный payoff, я бы запомнил эту фразу. s28 — тизер Лекции 5 + homework, ОК. s29 — Q&A с провокациями, хорошие backup-prompts.

**6 минут на заключение — правильно.**

---

## Top 3 «aha moments»

1. **s11 — «AI + радиолог > каждого alone».** Я ожидал бинарность «AI vs человек». Реальный фрейм — complementarity, с цифрами из meta-analysis. Это изменило моё мышление о medical AI.

2. **s17 narrative — DSP-1181 discontinued.** Я не знал, что «первый AI-designed drug» провалился в Phase 1. Это reality check, который ломает наивный hype. Один из главных messages лекции.

3. **s24 — «Final responsibility = врача. Инженер делает так, чтобы это было технически выполнимо.»** Этот фрейм reframes мою роль как инженера: не «строить AI который решает», а «строить AI который позволяет человеку решать». Это connects с LO8 explicit.

---

## Top 3 «wait, what?» moments

1. **s18 (PCCP) — почему это innovation?** Без контраста «до PCCP» я не понимаю значимость. См. P0-1.

2. **s17 — зачем мне знать про CEO firing Exscientia в 2025?** Перегружает narrative, не служит main message. См. P0-2.

3. **s15 — что такое «hit» vs «lead» в drug discovery?** Pharma jargon, не explain. См. P1-1.

---

## Дополнительные observations (per user spec)

### Frame mapping (6 frames) — logical или искусственная классификация?

В целом — **logical, не искусственно**. LO + LLM pattern/anti-pattern + Другой AI + Безопасность + Человек vs AI — это органичные angles, я не чувствую, что их притянули за уши. CORE концентрации в s11/s24/s27 — sensible.

НО: LLM pattern frame появляется только на s19 (single CORE) — это feels thin для одного из 6 frames. Если у меня 29 слайдов и frame появляется как CORE только один раз — это скорее «один важный слайд», чем «frame, который organizes лекцию».

### Russian context — органично или patchy?

mosmed.ai (s12) — органично, central case. Остальное (Sber AI Lab, GigaChat/YandexGPT, Cognitive Agro teaser, ГОСТ Р 59921) — patchy, ощущается как «местная вставка». Не критично, но если усилить, лекция почувствовала бы себя более «о российской AI-медицине», не «international with RU footnotes».

### Drug discovery «12 мес vs 4-5 лет» — я понимаю, что AI не решил всё?

После s17 — да, понимаю. Discontinued. AI ускорил design, не efficacy. Это **key reality check**, который план хорошо доносит. Это работает.

Но если бы s17 был overloaded (CEO firing + Recursion merger), main message мог бы потеряться. Поэтому P0-2 важен.

### Этическая секция (s20-25) — логика или морализаторство?

**Логика, не морализаторство.** Plan последовательно: bias (s21 evidence) → LLM-specific harm (s22 NEDA Tessa) → data security (s23 — слабее связь) → responsibility framework (s24) → regulation (s25). Я слышу «вот случаи, вот frameworks», не «инженер должен быть хорошим». Это сильно.

### Conclusion (s26-29) — 3 discrete и actionable вывода?

s26 takeaways:
1. AI-диагностика работает (LO1, LO2).
2. Drug discovery частично (LO2, LO3).
3. Ответственность — на враче, инженер обеспечивает выполнимость (LO3, LO8).

**Эти 3 discrete? — Да.** **Actionable? — (1) и (2) — informational; (3) — actionable, потому что говорит инженеру, что строить.** Я бы предпочёл, чтобы все 3 были actionable («инженер делает X, Y, Z»), но 1-из-3 actionable — приемлемо для obzor-лекции.

s27 closing line — strong.

### «Зачем мне это знать?» — personal relevance

Slides где personal relevance явная: s8 («Если научиться оценивать AI здесь — научишься оценивать везде»), s10 (мат-применение), s11 (concrete cifры), s19 (я сам делаю упражнение), s24 (моя инженерная роль), s27 (closing line).

Slides где personal relevance слабая: s7 (FDA stats — informational), s23 (Change Healthcare — security-focused, не AI-инженер-focused), s25 (regulation comparison — informational).

Лекция в целом — **personally relevant** для инженера. Но secondary слайды (s7, s23, s25) можно усилить connection «зачем именно МНЕ это знать».

---

## Would I recommend this lecture to a classmate?

**Yes, conditionally.**

Я бы сказал одногруппнику: «Лекция стоит того. Я узнал, что medical AI — production-инфраструктура (mosmed.ai, FDA 1000+), что AI+врач > каждого alone, что AlphaFold = Нобель но drug discovery — не «12 мес чудо», и что есть конкретный framework ответственности. Это новая mental модель для меня.»

НО: «Будь готов, что drug discovery секция (s15-18) грузит pharma jargon, который без подготовки парсится медленно. И responsibility quadrant (s24) — главный takeaway, читай его внимательно.»

Условие — это P0/P1 фиксы. С плохими частями (s17 overloaded, s18 без контраста, s19 размытый output) — я бы рекомендовал с большей осторожностью. С фиксами — рекомендовал бы безусловно.

---

## Summary count

| Priority | Count | Issues |
|----------|-------|--------|
| **P0 (blocker)** | 2 | s18 PCCP без контраста; s17 overloaded narrative |
| **P1 (friction)** | 7 | s15 pharma jargon; s10 prevalence/PPV; s6 axes ad-hoc; s19 size of output unclear; s13/s21 bias повтор; s23 weak AI connection; s25 аббревиатуры перегруз |
| **P2 (polish)** | 5 | s14 необходимость pause beat; s3+s4 длина poll; «mat-применение» как термин; «Хосзу-роль» неясно; RU context patchy |
| **Total** | **14** | |

**Top 5 fixes до chapter draft (Phase 2):**

1. **s18:** добавить one-line контраст «до PCCP vs с PCCP» — без этого PCCP innovation не parse-ится.
2. **s17:** убрать Exscientia 2025 (CEO firing, Recursion merger) из visible content; оставить только DSP-1181 timeline до 2022.
3. **s15:** в speaker notes — определение «hit» vs «lead» одной фразой.
4. **s10:** добавить prevalence/PPV intuition box или footnote — без этого студент думает «94% accuracy = хорошо», что в screening misleading.
5. **s19:** concrete instruction для micro-exercise output — что студент *выносит* за 8 минут (1 неточность ИЛИ 1 unverifiable claim ИЛИ 1 место abstract).

*Конец reader-text-only critique.*
