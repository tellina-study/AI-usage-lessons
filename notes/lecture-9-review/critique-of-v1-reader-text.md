# reader-simulator (text-only) — критика plan-v1.md (Phase 1)

**Дата:** 2026-05-20
**Студент:** ИУ6 МГТУ Бауман, 3 курс (профильно — инф.системы, базовый ML, без авиакосмического бэкграунда)
**Источник:** `notes/lecture-9-review/plan-v1.md`
**Verdict:** **APPROVE-WITH-POLISH**

Объяснение verdict: план **читаемый** и **mental map** в голове после 5 минут — формируется. Keystone (OODA Sense→Decide→Act) у меня как у студента 3 курса понятен сразу, потому что разжёван 1-й строкой и явно повторён в каждом разделе. **БОЛЬШИНСТВО** failure-блоков понятны и переводимы на «инженерный язык». Но **есть конкретные glossary-провалы**, **terminology overload в Р3**, и пара мест где мне как студенту физически тяжело — это не отказ, это polish. Кладу в Recommendations.

---

## TL;DR (что я понял из плана за 5 минут)

> «Лекция про то, как AI вторгается в три звена военно-космической работы — наблюдать, решить, действовать. На каждом звене он работает по-разному: лучше всего на Sense (спутники, мониторинг двигателей), опаснее всего на Decide (LLM-помощники для targeting, IDF Lavender как канонический провал), и далеко не так автономен на Act, как обещает маркетинг (Lancet recall, Replicator не вытянул сроки). Финальная мысль — где регулирование обрезает Act, и какие у меня как у будущего инженера КБ критерии "здесь AI не нужен".»

Это я могу пересказать. Это хороший знак.

---

## Что я понял хорошо

1. **OODA-ось ясна с первого упоминания.** Строка 36-37 говорит мне в одной фразе что такое цепочка и зачем она. Не abstract — сразу: «каждая задача — цепочка из трёх звеньев, AI вторгается в каждое по-разному, провалы случаются на стыках». Это **готовое мне в голову**, не докапываться.
2. **Anti-hype секции в каждой таксономии (Sense / Decide / Act) — драгоценны.** Они мне говорят «бренд ≠ режим работы» (стр. 49), «accuracy 90% ≠ 90% правильных решений» (стр. 56), «hype far ahead of true autonomous engagement» (стр. 63). Я понимаю, что это и есть mental model «как читать вендора», и она будет повторяться весь курс.
3. **Failure cases переведены на инженерный язык.** F-35 ALIS (стр. 99): «(a) быстрый feedback loop, (b) ground truth, (c) FP-cost < FN-cost — ALIS нарушил все три». Это **в моей терминологии** — три простых условия. Я могу применить это сам к своему ВКР.
4. **Strict-in бюджет посчитан явно (стр. 170-176).** 48-56% strict-in по времени, по 38-44% по слайдам — это «больше 30% с запасом». Я как студент не должен это считать, но методичность плана меня успокаивает.
5. **Russian context честно отмаркирован caveat'ами.** ScanEx, Sputnix, GigaChat на ISS, Svod/Glaz/Groza — везде явно «единственный источник», «independently verified — нет» (стр. 103, 118). Это **не агитация**, это нормальное обращение с источниками.
6. **Hook A (BEFORE/AFTER спутник) — отличный выбор.** Я бы как студент сел и пять секунд просто смотрел разницу. Это сразу tangible — «вот ДО, вот ПОСЛЕ, AI это нашёл». Не политика, не этика, просто «вау».
7. **Карьерный угол в Р5 (стр. 158) — без агитации.** МГТУ ИУ + ВКА Можайского + dual-use (VisionLabs / Cognitive Pilot) + civilian (Роскосмос TerraTech). Несколько траекторий, не одна — мне не загоняют в ВПК.

---

## Что я понял с трудом

1. **L1-L5 ladder в Р4 не привязан к конкретным реальным примерам в плане.** Строка 143: «MSS=L1; Saker Scout=L2; Fury supervised CCA=L3; Patriot/S-400=L4; LAWS=L5». Это **назначение**, но я как студент не понимаю **почему**. Что такое L2 vs L3 — где граница? Кто решил? Если это SAE-style лестница, то у SAE есть operational definitions. Тут — нет. Я бы wanted одно предложение под каждым уровнем «отличается от соседнего тем, что...».
2. **«Cost-asymmetry FP↔FN космическая» (стр. 56)** — формулировка крутая, но я как студент не уверен что **сам мог бы её посчитать** для конкретного случая. Я хочу один числовой пример, иначе это просто красивая фраза.
3. **Раздел 4 sub-section 4.5 «Maven walkout + Project Nimbus»** (стр. 147). Я знаю что Google и Project Maven были новостями, но **детали 2018** — 4000+ letter, 12 резигнировали, контракт не продлён, потом Anduril/Palantir/Scale подобрали — это для меня **новая история**. Урок «personal ethics ≠ industry regulation» сильный, но я бы хотел чуть больше контекста: почему именно Google? что было в письме? И самое главное — что мне как инженеру с этим делать? Опция «не работать на DoD» сейчас редкая (план это говорит). Что мне с этим делать?
4. **«Аnti-hype: "96-drone swarm / 1 планшет" = centralized многоканальное управление, не decentralized peer-to-peer» (стр. 63).** Я как студент 3 курса **не знаю что такое peer-to-peer swarm vs centralized swarm** в контексте drone autonomy. Это лежит вне моего ML-курса. Мне нужна одна фраза-определение.
5. **Раздел 4.6 «HITL как инженерный паттерн» — для меня очень сжат.** «Calibrated uncertainty + abstention; pairwise comparison не free-form; structured outputs с explicit "I don't know"; mandatory human gates для kinetic action». Это **5 разных техник в одной строке**, без определений. Calibrated uncertainty — что это? Abstention в LLM — это «модель отказывается отвечать»? Я ожидаю, что в chapter это раскроется, но в плане для меня это сейчас buzzword-зой.

---

## Что я НЕ понял

1. **«SAR ATR adversarial attacks — physical scatterer perturbations»** (стр. 100). Я **вообще не знаю**, что такое SAR (Synthetic Aperture Radar — я угадываю по контексту), ATR (Automatic Target Recognition — угадываю), и что такое «physical scatterer perturbations» в одной фразе. Это для меня **полностью чёрный ящик**. План мне не объясняет — там это идёт как failure case. **Это блокирует понимание раздела 1.**
2. **«SC2S/SIPR/JWICS» (стр. 56)** — три аббревиатуры подряд без контекста. Я предполагаю что это уровни секретности US-сетей, но я **впервые их вижу**. Если они не критичны для урока — убрать; если критичны — расшифровать.
3. **«FedRAMP HIGH», «IL4/IL6», «Claude IL6»** (стр. 54-56) — повторяющиеся аббревиатуры compliance-уровней. Для меня сейчас это шум. Что значит IL6 vs IL4? Зачем я как студент должен это знать?
4. **«Bayesian NN + ensemble»** как «альтернатива SAR ATR» (стр. 100). Я слышал про Bayesian methods на лекции 2-3 нашего курса, но **не уверен**, что я смогу объяснить, **почему именно Bayesian NN** помогает против adversarial. Это требует контекста, который план мне не даёт.
5. **«Helsing Altra + Centaur AI fighter pilot test на Saab Gripen E June 2025» (стр. 111).** Что такое Altra? Что такое Centaur? Это две системы или две версии? Они для разных целей? План их называет как «land combat fusion + AI fighter pilot test» — это две **разные** вещи в одном bullet, я путаюсь.
6. **«BPSA», «MSS»** (упомянуты в Topics + раскрыты позже)— я ОК с MSS (Mission Support System / Palantir Mission Software) после Р2, но BPSA — где он введён? Я не нашёл расшифровку.
7. **«Slingshot Agatha + TALOS» (стр. 47)** — что это такое? «Photometric fingerprinting спутников» (стр. 47) — звучит интригующе, но **что они делают в одной фразе с Maxar Sentry?** Это другая категория задач (SDA — space domain awareness vs ISR), но план их кладёт в одну Sense-корзину.

---

## Glossary gap (acronyms я не понимаю)

Помеченные **(D)** — требуется **explicit definition** на слайде или в первой строке параграфа.
Помеченные **(C)** — могу угадать из контекста, желательно gloss, но не блокирует.
Помеченные **(R)** — резать как шум, не учебная цель.

| Аббревиатура | Раскрытие нужно? | Где впервые в плане |
|---|---|---|
| **OODA** | **(D)** | стр. 8, 36 |
| **SAR** | **(D)** — Synthetic Aperture Radar | стр. 47 (косвенно «EO/SAR/AIS») |
| **ATR** | **(D)** — Automatic Target Recognition | стр. 100 |
| **ISR** | **(D)** — Intelligence/Surveillance/Recon | стр. 12 (topics) |
| **EW** | **(D)** — Electronic Warfare | стр. 12 |
| **LAWS** | **(D)** — Lethal Autonomous Weapon Systems | стр. 12 |
| **ALIS / ODIN** | **(C)** | стр. 80, 99 |
| **MSS** | **(C)** | стр. 54 |
| **CCA** | **(C)** — Collaborative Combat Aircraft | стр. 12, 63 |
| **AMRAAM** | **(C)** | стр. 126 |
| **VISTA** | **(C)** — DARPA X-62A test platform | стр. 61 |
| **V-BAT / RPAS / eVTOL** | **(C)** | стр. 61, 126 |
| **MCAS** | **(C)** | стр. 129 |
| **IFF** | **(C)** — Identification Friend or Foe | стр. 130 |
| **SDA** | **(C)** — Space Domain Awareness | стр. 50 |
| **PWSA** | **(C)** — Proliferated Warfighter Space Architecture | стр. 12 |
| **BPSA** | **(D)** — нигде не раскрыто! Что это? | стр. 12 |
| **GGE** | **(C)** — Government Group of Experts | стр. 20 |
| **ICRC** | **(C)** — Int. Committee of the Red Cross | стр. 20 |
| **HITL** | **(D)** — Human-in-the-Loop | стр. 16 |
| **IL4 / IL6 / FedRAMP HIGH / SC2S / SIPR / JWICS** | **(R)** | стр. 54-56 |
| **DO-178C / ARP4754A** | **(C)** — упоминается как safety-cert | стр. 23, 68 |
| **NIST AI RMF** | **(R)** | стр. 22 |
| **HALE** | **(D)** — High Altitude Long Endurance | стр. 126 |
| **GPS / GNSS / INS / eLORAN** | **(C)** | стр. 101 |
| **Bayesian NN** | **(D)** или callback к lec-02 | стр. 100 |

**Подсчёт.** ~10 терминов помечены **(D)** — это **критическая масса** для одного слайда определений. Я бы как студент **очень хотел glossary-слайд в Р0** перед началом Р1. Если его нет — терминология блокирует Р1-Р2 первые 10 минут.

---

## Hook impact (моё мнение)

- **A. BEFORE/AFTER object detection (спутник).** Сильнее всего для меня. Visual immediate, не требует bridge'а, evergreen. Я **сразу понимаю**, **что AI делает** — и оно полезно. Любой инженер кивнёт.
- **B. F-35 ALIS → ODIN failure-first.** Концептуально мощно, прямо служит миссии курса «AI ≠ магия». Но как hook первой минуты — я бы скорее заскучал. Заголовок «вот провал на миллиарды» — нужно prefacing «вот что обещали → вот что получили», а это 2-3 минуты ввода прежде, чем hook сработает.
- **C. X-62A AI dogfight.** Wow factor реально high, но я как студент сразу подумаю «это AI vs пилот, я уже знаю кто выиграл». Hype-vibes. Отклонить.
- **D. Drone footage с AI-аннотированием.** Не отвратит политически, **отвратит этически** — я сразу подумаю «это видео, где AI решает кого убить, и нам это показывают как cool tech». Я хочу **уйти из аудитории**. Отклонить однозначно.

**My pick: A.** Подтверждаю выбор плана.

---

## Pacing self-test

Прохожу план «студент-в-голове-таймером»:

- **Р0 (5 мин).** Свеж, готов. Hook A работает, ось OODA схвачена, roadmap есть. **OK.**
- **Р1 Sense (12 мин).** 4-5 working cases + 3 failures + Russian context — **плотно**. Особенно если ALIS перенесён сюда (а не в Act). Я к концу Р1 уже немного «выгружен» на термины. **Граница комфорта**.
- **Р2 Decide (14 мин).** **Это самый плотный для меня раздел.** Palantir MSS + Scale Donovan + Defense Llama + Thunderforge + Helsing Altra + Centaur + Anthropic-Palantir-AWS + NASA FDL FOXES + Russian Svod/Glaz/Groza/ZOV — это **9+ vendor-программ за 14 минут**. Я устал. Failure-блоки (Lavender, Vincennes, Lancet) сильные, но плотности vendor-tools слишком много. **REQUEST: сократить кейсы до 3-4 working + 3 failure.**
- **Р3 Act (14 мин).** Тоже плотно, но мне теперь интереснее (физические системы — Fury, Saker, X-62A, Geran-2). Я **просыпаюсь**. Failure-блоки (737 MAX, Patriot, Replicator) — для меня **более конкретны**. **OK с лёгкой перегрузкой по vendor-tools.**
- **Р4 Граница (15 мин, целиком strict-in).** **Это требует от меня собранности.** 7 sub-sections × 2 мин: L1-L5 ladder → UN GGE timeline → ICRC → Stop Killer Robots → Maven walkout → HITL pattern → Russia votes. Это много **новых концепций без подкрепления визуалом за 15 минут**. Я могу **выпасть**. **REQUEST: либо резать 4.4 (Stop Killer Robots — short embed в 4.3 ICRC), либо expand до 18 мин с явным «расслабьтесь, мы тут думаем не быстро».**
- **Р5 Q&A + payoff (10 мин).** Хорошо как закрытие, 7 критериев — у меня в голове остаётся ровно эти 7 как takeaway. Career-angle честный. **OK.**

**Cumulative usage:** к концу Р3 я уже на 45 мин лекции **выгружен на vendor-tools** + готов к глубоким идеям. Р4 идёт в неподходящий момент — я в самой плотной части. Структурно правильно (Sense→Decide→Act→Граница→Закрытие), но **15-минутный strict-in блок в конце требует pacing-tricks** (визуал, короткие sub-sections, явные паузы).

---

## Failure-block readiness

**Могу ли я после плана сформулировать критерии «когда не AI»?**

Да, частично. План явно даёт мне 7 критериев в Р5.1 (стр. 157). Из них **5 я понимаю прямо сейчас**:
- FP-cost >> FN-cost → AI ассистент (понимаю)
- Adversarial domain → multi-sensor + abstention (понимаю частично — нужно объяснение abstention)
- Single-point-of-failure — никогда (понимаю)
- Combat stress UI — testing under predicted failure modes (понимаю)
- Demo vs production (понимаю)

**2 не очень понимаю:**
- «Human ON the loop с pre-authorised ROE OK, OUT оспаривает treaty» — ROE = Rules of Engagement, я угадываю. «ON the loop vs OUT» — нужен явный visual. Сейчас это для меня bullet, не картинка.
- «Industry ethics — личный opt-out не масштабируется, legal regulation — рычаг». Это для меня **философское утверждение**, не критерий. Я как студент 3 курса не могу применить его в проектной работе.

**Урок Lancet rollback применим к моей будущей работе в КБ?** **Да.** Я **легко** представляю — буду в КБ, маркетинг скажет «у нас autonomous», менеджер захочет рекламировать, мне как ML-инженеру нужно сказать «demo ≠ production, distribution shift на полигоне». Это **directly transferable**.

**Урок LAWS-блока применим к моему ВКР?** **Частично.** Я **не строю** оружие. Но критерий «pre-authorised ROE боком» — пересекается с «pre-authorised limits» для любой автономной системы (пром.робот, авто). LAWS — частный случай. **Plan должен это явно сказать в Р4 — иначе LAWS-блок звучит как "не для меня".**

---

## Russian context — релевантность

**Отождествляю ли я себя с примерами?**

- **TerraTech / ScanEx / Sputnix.** Да. Это **гражданская траектория**, я могу туда пойти после диплома. Полезно.
- **Geran-2 / Lancet.** **Это для меня странно.** Я как студент Бауман с одной стороны понимаю, что это **актуальная техника** и эти системы реально работают; с другой — план показывает мне **failure-урок** на одном из них (Lancet rollback), что делает разбор инженерным, не политическим. **Это работает, если ТОЛЬКО как инженерный кейс, БЕЗ агитации.** План это держит — caveat «по сообщениям CSIS», «videos без Target Locked UI». Я **OK** с таким уровнем нейтральности.
- **Svod / Glaz / Groza / ZOV Maps.** Я **никогда о них не слышал**. Это **новые названия для меня**. План честно говорит «single-source caveat». OK, но я бы не делал на них акцент.
- **МГТУ ИУ + ВКА Можайского career angle.** Это **личная связь** — я **студент ИУ**. Это попадает в меня прямо. **Если упомянуть мою кафедру — будет работать**. Если общими словами «выпускник МГТУ может пойти в…» — **уменьшит engagement**.

**Russian context overall:** 22-25% объёма (стр. 201) — **для меня OK**, не перебор. Открытый question 4 («22-25% — принять или резать?») — **принять**, я не чувствую перекоса.

**Что НЕ работает.** Sber GigaChat на ISS (стр. 103). Это **single-source unverified claim**. Если упоминать — то **explicitly как пример "вот так бывает с открытыми данными"**, а не как working case. План это держит — но в speech нужно подчеркнуть.

---

## What's missing / what I expected

**Fundamentals я ожидал, но их нет (или они в подразумеваемом chapter).**

1. **Что такое sensor fusion в принципе.** План говорит «multi-sensor tipping EO/SAR/AIS» (стр. 96) — но я **не знаю**, как это работает математически. Один параграф или один слайд «вот как два сенсора объединяются» — был бы спасением. Иначе любой fusion-кейс — buzzword для меня.
2. **Что такое edge ML / on-orbit inference.** План говорит «remote-upgradable on-orbit models» (стр. 96) — но **не объясняет**, почему это challenging (latency, power budget, radiation hardening). Я как студент 3 курса слышал «edge», но **не знаю**, что специфично для космоса.
3. **OODA-loop сам.** План вводит ось, но **не объясняет**, откуда она пришла (J. Boyd, USAF 1976, изначально для air combat). Один слайд «эта рамка не наша — она 50-летняя инженерная модель» — даст мне **доверие к подходу**.
4. **HITL как concept.** План говорит про HITL патн (стр. 148), но я **не уверен**, что я понимаю **разницу** между HITL / HOOL (human-on-the-loop) / HOTL (human-out-of-the-loop). Это **критически важно** для LAWS-блока. Это **должно быть на слайде в Р4.6 как ladder**, не bullet.

**Cases I expected but missing.**

- **Wisk Aero / Joby / eVTOL.** Plan explicitly excludes (стр. 202). **OK** — я согласен, ёмко.
- **Russian Cognitive Pilot (КАМАЗ автономия).** Упомянут в Р5 (стр. 158) как **career-target**, но не как **case**. Если бы я как dual-use civilian-leaning студент сидел в зале — Cognitive Pilot был бы **bridge** между «коммерческое» и «военное». **Минимум: один параграф в Р3 с пометкой "civilian-side analogue Geran-2 autonomy"** — выровнял бы dual-use balance.
- **Anduril Sentry Tower (border / counter-UAS gateway).** План упоминает Anduril Lattice + Fury + Roadrunner + Barracuda (стр. 61), но **не Sentry Tower** — это **gateway-product** Anduril и хорошо иллюстрирует «AI на земле, не в воздухе». **Не критично**, но был бы dual-use kicker.
- **NASA Mars Perseverance autonomous navigation.** В Topics нет, но **гражданский «autonomous on-orbit/on-surface» кейс**, который **не вызывает этических вопросов**. Может балансировать defense-heavy кейсы. **Опционально**.

**Visual cues я ожидаю на слайдах.**

- Glossary-слайд **до Р1** (см. Glossary gap выше).
- L1-L5 ladder **с примерами на каждом уровне** в Р4.1.
- OODA-keystone **с stable repeat в Р5 как closing callback** — план это держит (стр. 162 слайд 27). **OK.**

---

## What's overload

1. **Р2 Decide — 9+ vendor-programs.** Я насчитал в Р2: Palantir MSS, Scale Donovan, Defense Llama, Thunderforge, Helsing Altra, Helsing Centaur, Anthropic-Palantir-AWS, NASA FDL FOXES, DAGGER++, Svod, Glaz, Groza, ZOV Maps. Это **13 vendor / program names** за 14 минут. Я не **запомню** даже 5 из них. **REQUEST: жёстко резать до 5-6 working + 3 failure.** Helsing вторая система (Centaur) — лишняя в этом срезе. Anthropic-Palantir-AWS — bullet, не отдельный case. NASA FDL FOXES / DAGGER++ — можно вынести одной строкой или вообще убрать (civilian-space, отвлекает от Decide-фокуса).
2. **Acronyms density в стр. 54-56.** «Palantir MSS… Scale Donovan / Defense Llama / Thunderforge (FedRAMP HIGH)… Anthropic-Palantir-AWS (Claude IL6); Anduril Lattice (mesh OS)…» — **6 vendor-program names + 3 compliance acronyms за 3 строки**. Это **слайд = 1 fact**, не **слайд = 9 facts**. План этого ещё не разрешит — это про слайды (Phase 5), но **уже сейчас в плане видно**, что для одного раздела слишком плотно.
3. **Р4 — 7 sub-sections × 2 мин.** Слишком coarse — sub-section на 2 минуты не usable для меня. **REQUEST: consolidate. 4.3 ICRC + 4.4 Stop Killer Robots → один блок «non-state actors положения». 4.6 HITL — отдельный slide-level explanation, нельзя 2 минуты.**
4. **Russian-political-context — некомфортно?** Не для меня лично. План правильно держит open-source-only и инженерный фокус. Если бы был **митингующий тон** — я бы попросил выйти. Сейчас — нейтрально, OK.

---

## Pre-submit checklist

- Я как студент **могу пересказать главное** лекции после плана: **YES** ✅
- Я **отождествляю** себя с примерами: **YES (частично)** — civilian path в Р5 + Бауман-mention need + dual-use balance need
- Я **понимаю критерии «когда не AI»**: **YES (5/7 прямо сейчас, 2 требуют объяснения)** ⚠️
- Я **не перегружен** acronyms / failure overload: **NO** — Р2 vendor density + ~10 critical acronyms без glossary блокируют Р1-Р2 первые минуты ❌

---

## Recommendations (как студент)

В порядке приоритета **для меня как студента-читателя**:

1. **[P0] Glossary-слайд в Р0 после keystone, до Р1.** 10 acronyms (D) на одном слайде: SAR, ATR, ISR, EW, LAWS, OODA, HITL, BPSA (если используется), HALE, Bayesian NN (callback к lec-02). Без этого Р1 первые 5 минут — wall of acronyms. **Это структурный fix, дешёвый.**
2. **[P0] Р2 Decide — резать vendor-density.** С 9+ программ до 5-6 working: Palantir MSS, Scale (Donovan/Llama/Thunderforge — одной строкой), Helsing Altra, Anduril Lattice. Все остальные — bullets / one-line. **Иначе я выпаду к Р3.**
3. **[P1] L1-L5 ladder (Р4.1) — operational definitions на каждом уровне.** Одно предложение «L1 отличается от L2 тем, что…». Иначе «MSS=L1, Saker Scout=L2» — magic assignment.
4. **[P1] HITL / HOOL / HOTL — отдельный visual в Р4.6.** Это **не bullet**, это **центральная mental model** Р4. Я хочу одну картинку «вот человек ВНУТРИ цикла, вот НАД, вот ВНЕ».
5. **[P1] Bridge Russian-context: один цивильно-российский case (Cognitive Pilot, КАМАЗ autonomy) в Р3 как dual-use balance.** Иначе все российские примеры — defense (Geran-2, Lancet, Svod) → читается как «российский AI = только военный». Cognitive Pilot балансирует.
6. **[P2] Explicit «как Р4 LAWS применим к не-LAWS работе студента»** — одна строка в Р4 или Р5 «эти же критерии — pre-authorized limits / human gates — работают для любой автономной системы, не только оружия».
7. **[P2] OODA-loop sourcing.** Один слайд / параграф «эта рамка из 1976, J. Boyd, USAF» — даёт мне **доверие**, что ось не выдумана для лекции.
8. **[P2] Sber GigaChat на ISS — рассмотреть полное удаление.** Single-source unverified — даже с caveat, ИИ-восторженный читатель может не услышать caveat. План **уже** относит этот к Russian context секции с caveat — это OK, но для speech: либо **усилить** caveat ("единственный анонс одной стороны, независимо не подтверждено, упоминаем как пример с какими данными мы работаем"), либо удалить.

---

## Что я бы НЕ менял (явно)

- **Hook выбор A.** Подтверждаю.
- **OODA как ось.** Подтверждаю, **сильнее Б (autonomy ladder)** и **сильнее В (dual-use border)** для моего понимания.
- **Strict-in бюджет 48-56%.** Подтверждаю, comfortable margin.
- **22-25% Russian context.** Подтверждаю, не перебор.
- **Closing callback в Р5.4.** Это **сильное** возвращение к keystone, я **запомню** «Цепь Sense → Decide → Act — каждое звено имеет свои AI-инструменты, границы и failure modes. Инженер держит её в голове целиком». Это **тот takeaway, который я унесу из лекции**.
- **Р4 целиком strict-in.** Это **правильно** — даже если pacing-tight, это **миссия курса**. Не вырезать.

---

## Closing impressions

План **работает** для меня как студента. После 5 минут чтения я **могу пересказать** главное, **понимаю** keystone-ось, и **знаю** какие 7 критериев из него вытекают. Это **APPROVE-WITH-POLISH**, не REVISE — структурно всё на месте.

Polish — в **terminology layer**: glossary-слайд, операциональные L-определения, HITL-visual, Russian-context-balance с одним civilian-side кейсом, Р2 vendor-cleanup. Это **не структурный overhaul**, это **2-3 фикс-таргета** перед Phase 2 chapter draft.

Если эти 5 рекомендаций включены — план готов к chapter.
