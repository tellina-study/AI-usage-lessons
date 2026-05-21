# Reader-text-only critique — Лекция 11 plan v1

**Режим:** text-only (outline без рендера, без живого лектора).
**Reader:** студент-инженер 3 курса, прошёл lec-01..lec-10.
**Verdict:** **Mostly engaging, but slogs в двух местах** (§1.2 foundation models + §4 overload). Outline читается как «настоящая инженерная лекция, не PR-проповедь», но **середина выходит длинной и плотной**.

---

## 1. Overall reading verdict

**Mostly engaging.** Я читал 15 минут и **не заскучал в первые 7-8 минут** (hook + keystone + §1.1 + §1.3 hype-collapses). Но в §1.2 (foundation-модели) и в §4 (10+6+4+5 items) я начинаю **просматривать по диагонали** — слишком много item-listing без анкеров. К §2.5 (границы CV) я уже устал от Tesla и думаю «когда я смогу унести что-то *своё*?», а это критично — после §2 ещё §3 и §4. Финал спасает Q&A formula («3 вопроса к вендору»), но почти теряется в overload §4.

Плюс: **honestly я бы пошёл на эту лекцию.** Tesla retreat 2018+2024 + 10 критериев «когда AI не нужен» + российский контекст — это редкий набор, не «AI меняет мир» бубнёж.

Минус: outline не даёт мне **одну единственную thing-to-remember** — он даёт 5 thing-to-remember, и я подозреваю, что через неделю помню только Tesla.

---

## 2. Per-section reading take

### §0 (Hook + keystone) — **Engaging**
Tesla Giga Press underbody + Musk «humans are underrated» **цепляет**. «Если Tesla сожгла дважды + GE сожгла $4B + 95% не доходят» — это **central question**, на которую я хочу ответ. Keystone двух колонн читается чисто: «discrete: дискретные единицы → CV/коботы; process: непрерывный поток → soft sensors/MPC». **Но** «соединительный пояс: foundation-модели + agentic copilots + pilot purgatory» — я не понимаю, это всё **одна** связка или три разные? Звучит как cram-three-things-on-belt. После 30 сек я бы предпочёл просто «pilot purgatory» как общий пояс — foundation models я лучше вижу в §1.2.

### §1 (Что общее) — **Mixed: 1.1 engaging, 1.2 slog, 1.3 engaging**
- **1.1 Adoption landscape** — рыночные оценки 5×, 5.5% high performers, 2/3 в pilot purgatory. **Engaging.** «Vendors расходятся в 5×, читайте methodology» — это конкретный навык.
- **1.2 Industrial foundation models** — **slog.** Siemens 150 PB + Foxconn FoxBrain Llama 70B injection-molding параметры — звучит как два sponsored-namedrop. **Критическая граница** «augmentation, не controller» — это полезная идея, но я не понимаю **почему именно foundation модели не могут быть controller**? Это про latency? Hallucinations? Safety certification? Outline это не объясняет, а я по prerequisites должен помнить из lec-03 что-то. **Я залипаю здесь** — 4 минуты на два кейса с непонятной мне границей.
- **1.3 Hype-collapses (GE / IBM / Foxconn WI)** — **Engaging.** Три истории, три урока, чистая структура. «8-е чудо света от главы государства предсказывает провал» — это запомню.

### §2 (Discrete deep-dive) — **Engaging до 2.4, slog к 2.5**
- **2.1 CV-инспекция** — BMW + TSMC + Boeing **plus** anti-кейс Alaska 737 door plug — отличная пара. «CV — последняя линия защиты, не первая» — формула, унесу.
- **2.2 PdM** — короткий, чистый. «Vendor обещает -25-40%, McKinsey: большинство not capturing value» — это применимо.
- **2.3 Коботы + Jidoka 2.0** — Hyundai Spot + Toyota GAIA + Foxconn FoxBrain self-claim — нормально, но **3 разных кейса в 3 минуты — я не запомню кто что сделал**.
- **2.4 Tesla 2018** — **самый сильный кусок**. Конкретный причинный анализ (conveyor, fluffer, robotic battery module) + Bainbridge automation paradox + Toyota Jidoka как альтернатива + follow-up 2024 retreat. Это **готовая лекция в лекции**.
- **2.5 Границы CV** — **slog.** Я уже в 12-й минуте §2, мне дают ещё «physical signal amplification до ML, rules-based vision 60-70%». Это полезно, но **звучит как post-script к 2.1**, не отдельный sub-section. Утомительно.

### §3 (Process deep-dive) — **Engaging но плотно**
- **3.1 Soft sensors + Pfizer Vox** — engaging, «recommend not autonomous» — чёткая формула.
- **3.2 MPC/RL гибрид (Yokogawa-JSR + CIRL)** — engaging но **я не понимаю CIRL без подробностей**. «PID в RL архитектуре» — это PID inside RL, RL inside PID, или они работают параллельно? Outline загадывает.
- **3.3 PdM на edge + F-35 ALIS callback** — POSCO 180 nodes + Holcim. Callback к lec-09 хорош, но **F-35 в процессной лекции — точно ли это нужно?** Я уже знаю про ALIS из lec-09. Outline кладёт callback в раздел, где он немного не на своём месте (defense ≠ process manufacturing).
- **3.4 Regulatory (FDA + ATEX)** — engaging. «Audit trail + HITL + Zone 0 запрет non-certified hardware» — это конкретные правила.
- **3.5 Russian context** — **engaging методически** («public-disclosure скудна — анти-pattern в reporting»), но **тонкий слой** (3 минуты, 4 компании без metrics). Я понимаю аргумент, но не унесу ни одного российского кейса с цифрами — только «они там что-то делают».

### §4 (Decision framework) — **Conceptually engaging, structurally slog**
- **10 критериев** — **payoff** который я ждал. Но **10 пунктов за 4 минуты = 24 сек на пункт.** Это нечитаемо вслух, я **сдамся на 5-м критерии**. И я подозреваю, что некоторые критерии overlap (criterion 1 «MTBF >1 year» и criterion 7 «pilot без go-criteria» — это разные вещи?).
- **6 альтернатив** — SPC/DOE/MPC/RCM/CFD/rules-vision. Норм, но **читается как глоссарий**, не как сравнение.
- **Hybrid patterns** — PINN/CIRL/ML over SPC/POSCO PLC+ML. Опять 4 нерасшифрованных acronym'а за 3 минуты. **Я залипну.**
- **5-step framework** — **самое полезное**, его хочу как чек-лист. Но он спрятан в конце §4 (2 мин), когда я уже устал от list-overload.

### §5 (Замыкание) — **Engaging**
Recap + «задайте 3 вопроса вендору» + Bridge к lec-12 (digital twins) — чисто. Closing hero BMW Werk digital-twin — захочу увидеть.

---

## 3. Top 5 confusions (out of outline)

1. **§1.2: почему foundation-модели «не могут быть autonomous controller»?** Outline говорит «критическая граница» — но не объясняет. Latency? Hallucinations? Сертификация SIL? Я как студент думаю «ну дайте foundation model PID-цикл — что мешает?»
2. **§3.2 CIRL:** что такое «PID в deep RL» структурно? Outline пишет «гибрид, не RL вместо PID» — это **два контура** или **PID внутри loss function RL** или **RL подсказывает setpoint PID-у**? Без диаграммы я угадываю.
3. **§4.1 critеrions overlap:** «MTBF >1 year — insufficient data» (#1), «pilot без go-criteria» (#7), «demo-hype без 6-mo track record» (#10) — это **разные критерии или один в трёх формулировках**?
4. **Keystone belt confusion:** «соединительный пояс — foundation-модели + agentic copilots + pilot purgatory» — три разные вещи в одном поясе? Pilot purgatory — это **failure mode**, foundation models — **technology layer**, copilots — **interaction pattern**. Они логически не одинаковы.
5. **§3.5 Russian context:** outline говорит «public-disclosure скудна = анти-pattern в reporting, не absence adoption». Это **методическая защита** или **реальный факт**? Я как студент хочу увидеть **доказательство, что adoption есть** — может быть закрытые отраслевые отчёты, госконтракты, патенты. Outline даёт только тезис.

---

## 4. Top 5 «hooks worked» (хочется развернуть)

1. **Musk «Humans are underrated» 2018.** Это не «AI плох» а «инженер недооценил variability». Хочу детальный разбор conveyor + fluffer + battery module — где именно automation paradox сработал.
2. **«CV — последняя линия защиты, не первая» (Boeing 737 door plug).** Применимая мне формула — как инженер я могу её повторить начальнику.
3. **3 вопроса к вендору (baseline / окно / intervention list).** Готовый артефакт, я унесу.
4. **«Pilot purgatory 95% (MIT Sloan 2025) + только 5.5% high performers (McKinsey)».** Цифры, которые ломают «AI всех меняет» — я хочу источник под рукой для собственных дискуссий.
5. **Yokogawa-JSR FKDPP 35 days autonomous distillation control (2022).** Это **первый production-precedent RL** — конкретное достижение, не demo. Хочу понять, что именно RL умел такого, что PID не умел.

---

## 5. Failure-bucket experience (49%)

**49% — не давяще, потому что:**
- Failure встроен **рядом с кейсом**, а не в отдельный «раздел провалов». Это работает: TSMC 95% accuracy + Boeing door plug — **одна минута**, я не отдельно «слушаю успех», отдельно «слушаю провал».
- §4 (100% failure) **payoff**, не наказание. «Вот критерии, вот альтернативы, вот рамка» — это **полезное знание**, а не «AI не работает».
- Tesla 2018 + GE Predix + Foxconn WI — **истории, не цифры**. Запоминаются.

**Но есть риск:** **§4 (13 мин = 17% времени с 100% failure)** — если outline сохранит 10+6+4+5 items dump, я уйду с ощущением «много негатива списком». **Подача §4 решает всё.** Список вслух — провал; визуальная карта + 3 категории + 5-step framework как hero-визуал — победа.

**Как должно подаваться:** мне нужны **2-3 anchor cases на §4**, не 25 abstract items. Например: «вот завод X, вот вендор хочет AI, применяем 5-step framework вживую» — это лучше, чем «10 критериев списком».

---

## 6. Keystone test

**Могу ли я после outline сформулировать одной фразой ось лекции?**

**Да, с натяжкой:** «Эта лекция учит меня **различать дискретное и процессное производство** через ось **«разная физика → разный AI-стек → разные failure modes»**, и даёт **рамку решения, где AI не нужен**.»

Но в outline keystone **слишком много задач делает одновременно:**
- (a) объяснить две модели производства,
- (b) показать failure modes под обеими,
- (c) обозначить общий пояс (foundation/copilots/pilot purgatory),
- (d) подвести к LO8.

Я **унесу discrete vs process** как axis. **Но «соединительный пояс» с 3 элементами я не запомню.** Keystone был бы сильнее, если бы пояс — **один концепт** (например, только pilot purgatory как universal failure), а foundation models / copilots — это содержание §1.

---

## 7. What's missing for me as future engineer

1. **Один реальный production-ready чек-лист** (не 10 критериев абстрактно). Например: «10 вопросов на собеседовании с вендором AI for manufacturing» — print-on-A4.
2. **Бенчмарк зарплат / ролей в industrial AI** (см. lec-06/07 паттерн). Outline это не упоминает — мне любопытно «какие roles на рынке сейчас? MLE-в-manufacturing? data engineer на MES? PLC + ML coprocessor?»
3. **Сравнение open-source vs vendor** (Foxconn FoxBrain Llama 70B — кто ещё делает open-source industrial foundation models? Есть ли Hugging Face dump?).
4. **«Покажите мне data pipeline, на котором сидит soft sensor».** Outline говорит «soft sensors дают real-time estimate без lab samples» — но не показывает **что физически на входе** (датчик температуры? давления? и сколько данных за час?).
5. **Hands-on artifact:** маленький toy dataset / Jupyter notebook на CV-defect (Kaggle steel defects?) — чтобы я мог пощупать. Outline только теория.

(Понимаю, что это outline лекции, не лабораторной — но **mention о seminar/lab companion** ожидал бы.)

---

## 8. Recommendations для plan v2

1. **§1.2 foundation models — добавить ОДНУ строку «почему augmentation, не controller»** (latency? hallucinations? regulatory? всё три?). Иначе sub-section читается как marketing.
2. **§4.1 — урезать с 10 критериев до 6-7 крупных категорий** или **сгруппировать**: (A) data/MTBF: criteria 1,5,9; (B) cost asymmetry: 2,4; (C) regulatory: 3,8; (D) human factors: 6,7,10. **Группировка делает payoff читаемым.**
3. **§4 weight cut — 13 мин → 11 мин**, освободить 2 мин для **одного worked example «применяем 5-step framework на реальном кейсе»** (например, «нас просят внедрить AI на упаковочной линии, поехали по 5 шагам»). Worked example >>> 10 abstract criteria.
4. **Keystone belt — упростить до одного концепта.** Pilot purgatory универсален → его в пояс. Foundation models / copilots / agentic — это уже **содержание §1**, не keystone.
5. **§3.3 F-35 ALIS callback — сократить до 1 строки** или **переместить в §1.3 hype-collapses trio** (Predix + Watson + ALIS = три hype-collapses defense+industrial+health → cleaner). Defense callback внутри process-deep-dive отвлекает.
6. **Добавить §4 cheat-sheet artifact** — «3 вопроса к вендору» + 5-step framework на одной странице, downloadable. Студенты унесут.
7. **§3.5 Russia — либо расширить с одним конкретным public case (Норникель flotation с цифрами если найдутся) либо явно сократить до 2 мин,** чтобы не выглядело token-gesture.
8. **§1.2 + §3.2 — мини-диаграммы обязательны** (foundation model layer vs PLC stack; CIRL как PID inside RL loss). Без них словесно не объяснимо.
9. **2-3 sub-section nameplates сделать read-out-loud формулами** (стиль «CV — последняя линия защиты, не первая»). Это запоминается лучше любых статистик.
10. **Hook A примечание:** «Musk humans are underrated 2018» — 8 лет назад. Сегодня я (студент 2026) подумаю «опять Маск восьмилетней давности». **Сделать сильнее**: связать с retreat 2024 в одной фразе («Tesla обожглась в 2018, обожглась снова в 2024 — компании не учатся один раз»). Outline это делает, но в hook кладёт акцент на 2018 — лучше поставить **2024 первым, 2018 как «и в первый раз тоже»**.
