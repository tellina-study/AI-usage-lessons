# 02 — Failures, Limits & Where AI Should NOT Be Used (Aerospace & Defense)

**Цель.** Каталог документированных провалов, фундаментальных границ и анти-кейсов для strict-in failure/judgment-блоков лекции (≥30% контента).

**Принцип отбора.** Каждый кейс содержит: (1) что произошло (документировано), (2) выученный урок, (3) правильная альтернатива / границы применимости.

**Структура.** 6 категорий: history (1960s–2010s), recent (2018–2026), fundamental limits, ethical/LAWS, supply-chain & dependency, hype-deflation.

---

## 1. Исторические провалы автоматизации в воздушных/морских системах

### 1.1 USS Vincennes / Iran Air 655 — Aegis automation, 1988
- **Что произошло.** USS Vincennes сбил Iran Air Flight 655 (A300, Tehran→Dubai) двумя SM-2 ракетами. 290 убито. Aegis-система **корректно** записала track как climbing — но операторы под стрессом доложили captain'у "descending into attack". 
- **Корневая причина.** Не баг алгоритма, а human-machine interface: автоматика правильно классифицировала, экипаж — нет. Manual correlation сбоит под стрессом + target fixation.
- **Урок.** «Человек over loop» — это не панацея; стресс ломает human judgment именно там, где он критичнее всего. Если система предполагает "people will catch the error" — нужно проектировать процесс под predicted human failure modes, не под expectation rationality.
- **Альтернатива.** Тестирование UI под combat stress, fully automatic mode для time-critical decisions с pre-authorised ROE (rules of engagement), либо более долгие decision windows.
- Источники: [Wikipedia — Iran Air 655](https://en.wikipedia.org/wiki/Iran_Air_Flight_655), [Stanford CSLI — Overwhelmed by Technology](https://xenon.stanford.edu/~lswartz/vincennes.pdf), [USNI Proceedings — Human-Machine Team Failed Vincennes](https://www.usni.org/magazines/proceedings/2018/july/human-machine-team-failed-vincennes).

### 1.2 Patriot friendly fire — IFF + automation, 2003
- **Что произошло.** RAF Tornado GR4 (22 March 2003, 2 крс KIA), US Navy F/A-18C Lt N. White (2 April 2003, KIA) сбиты собственными Patriot batteries во время Operation Iraqi Freedom.
- **Корневая причина.** Tornado misclassified как Iraqi anti-radiation missile; IFF system был interrogated, но **не ответил** (problem known — uncorrected). Аэропилоты воспринимали automated mode как «better than human», operators ослабили oversight.
- **Урок.** Когда automated system "лучше человека" по статистике — operators перестают активно мониторить. Это **automation bias**. Безответ IFF не означает враг, но в auto-engage режиме именно так интерпретировался.
- **Альтернатива.** После incidents: запрет fully-automatic launch mode; pilots — non-encrypted IFF (более надёжный, хоть и менее защищённый); periodic active interrogation теста.
- Источники: [Trenchart — F-16 vs Patriot](https://www.trenchart.us/p/in-2003-a-us-air-force-f-16-and-a), [The Register — Patriot friend or foe](https://www.theregister.com/2004/05/20/patriot_missile/), [Brookings — military AI errors](https://www.brookings.edu/articles/understanding-the-errors-introduced-by-military-ai-applications/), [SOFREP — 2003 Patriot F/A-18 incident](https://sofrep.com/military-history/aviation-history-the-2003-patriot-missile-friendly-fire-incident-that-downed-a-us-navy-f-a-18-in-iraq/).

### 1.3 Iran capture of US RQ-170 Sentinel, 2011
- **Что произошло.** Lockheed Martin RQ-170 «Beast of Kandahar» захвачен Ираном 5 Dec 2011. Iran заявил GPS-spoofing — feed false GPS data → drone приземлился на иранской базе, "думая" что вернулся в Афганистан.
- **Каверзы.** Atribution неоднозначно: некоторые эксперты (JAS Global Advisors) считают GPS-spoofing маловероятным для milspec drone — скорее EW jamming + autonomic landing logic. Но **независимо** от точного механизма, drone **захвачен**.
- **Урок.** GNSS-зависимые autonomous systems — fragile в contested EM environment. Single-source positioning = single point of failure.
- **Альтернатива.** Multi-sensor fusion (INS + terrain-matching + optical + GNSS); spoof-detection logic; "lose link" fallback не на homing, а на self-destruct или random-egress.
- Источники: [Wikipedia — Iran-US RQ-170 incident](https://en.wikipedia.org/wiki/Iran%E2%80%93U.S._RQ-170_incident), [SecurityWeek — RQ-170 GPS hijack](https://www.securityweek.com/reports-say-us-drone-was-hijacked-iran-through-gps-spoofing/), [JAS Advisors — skeptical view](https://www.jasadvisors.com/iran-hijacked-us-rq-170-sentinel-drone-with-gps-hack-not-likely/).

### 1.4 Boeing 737 MAX MCAS — single-AoA dependency, 2018–2019
- **Что произошло.** Lion Air 610 (29 Oct 2018, 189 убито) и Ethiopian 302 (10 Mar 2019, 157 убито). MCAS активировался от **одного** AoA-сенсора без redundancy; пилоты не были обучены и не могли пересилить repeated nose-down trim commands.
- **Контекст и AI-релевантность.** MCAS не AI в строгом смысле, но pedagogically важен как extreme case **automation-bias + opacity + single-point-of-failure**. Это анти-паттерн, применимый ко **всем** AI-системам в safety-critical контексте.
- **Уроки.**
  1. **Redundancy.** Никогда не делать safety-critical системы зависимыми от single sensor.
  2. **Transparency.** Если operator не знает что система делает — он не может override.
  3. **Single-point-of-failure analysis** — обязателен в FMEA / FTA до сертификации.
  4. **Software cannot solve hardware shortfalls.** MCAS добавили, чтобы скомпенсировать aerodynamic shift от больших двигателей. Software-patches для физических проблем — risky.
- Источники: [PMC — Boeing 737 MAX Engineering Ethics](https://pmc.ncbi.nlm.nih.gov/articles/PMC7351545/), [Fierce Sensors — Killer software lessons](https://www.fiercesensors.com/electronics/killer-software-4-lessons-from-deadly-737-max-crashes), [Medium/Ish — MCAS Design Failure](https://medium.com/@ish1442006/boeing-737-max-mcas-design-failure-and-fatal-crashes-2018-2020-af86eab7ff42), [ThinkReliability — Four Lessons from 737 MAX](https://blog.thinkreliability.com/four-lessons-from-the-boeing-737-max-8-crashes).

---

## 2. Современные провалы AI в обороне (2018–2026)

### 2.1 F-35 ALIS predictive maintenance fiasco (2010s–2024)
- **Что произошло.** ALIS (Autonomic Logistics Information System) — cloud-based maintenance + supply chain manager для F-35. К 2020-м: high false-positive rate, неточные данные, технически сложная, плохо usable. Operators bypassed её и делали manual inspections. Cost-per-flight-hour вырос до **$44 000** — выше F-22 Raptor.
- **GAO findings.** «Inaccurate and missing data have at times resulted in the system signalling that an F-35 should not be flown — even though aircraft had no issues». ALIS faced challenges deploying F-35, training personnel, accurate data resident in system.
- **Дорогостоящий exit.** ALIS не отменили — её **последнюю версию** выкатили June 2024 → потом постепенный переход на ODIN до конца 2025. ODIN-fielding к squadrons **задержан на 2025**. 29 ODIN hardware kits от Lockheed.
- **Урок.** Predictive maintenance работает там, где (a) feedback loop быстрый (drift детектируется ml-операторами в дни, не годы), (b) ground truth доступен, (c) false-positives дешевле чем false-negatives. F-35 ALIS нарушал все три условия + adversarial UI/UX design.
- **Альтернатива.** Меньше всеобъемлющий стек, отделение predictive analytics от flight-clearance authority. ODIN строится именно по этим принципам — government-owned, smaller scope, disconnected mode, явное human-in-the-loop для flight authorisation.
- Источники: [Air & Space Forces — F-35 dumps ALIS](https://www.airandspaceforces.com/f-35-program-dumps-alis-for-odin/), [GAO-20-316](https://www.gao.gov/assets/gao-20-316.pdf), [GAO-22-105943](https://www.gao.gov/assets/gao-22-105943.pdf), [Bolt Flight — F-35 Issues](https://boltflight.com/f-35-issues-an-in-depth-examination-of-a-troubled-program/), [Defense Daily — ODIN delay](https://www.defensedaily.com/start-of-f-35-odin-software-fielding-to-squadrons-delayed-until-2025/air-force/).

### 2.2 Russian Lancet — automated target recognition **rolled back** (2022–2024)
- **Что произошло.** Lancet-3 рекламировался как autonomous target ID & engagement; видео с "Target Locked" + bounding box в 2022–2023. Анализ показал: Russians **выключили AI-guidance**, последние video drops не имеют autonomous-locking UI.
- **Гипотеза.** Premature product rollout → product "recall". ATR работал в demo-conditions, но не на ротации цели / vibration / EW.
- **Урок.** **Demo ≠ production.** ML-перформанс в narrow training distribution не переносится на full battlefield variance: dust, smoke, EW, новые camo, повреждённое оборудование, weather. "Edge cases" — это **большинство** real combat.
- **Альтернатива.** Operator-in-the-loop с automated tracking-assist; не autonomous-engage до production hardening.
- Источники: [Breaking Defense — revolution that wasn't](https://breakingdefense.com/2024/02/the-revolution-that-wasnt-how-ai-drones-have-fizzled-in-ukraine-so-far/), [CSIS — Russia probably hasn't used AI weapons in Ukraine](https://www.csis.org/analysis/russia-probably-has-not-used-ai-enabled-weapons-ukraine-could-change), [CSIS — Russia drone ecosystem](https://www.csis.org/analysis/how-russia-building-sovereign-drone-ecosystem-ai-driven-autonomy).

### 2.3 IDF Lavender targeting system — Gaza 2023–2024
- **Что произошло.** Lavender — AI database, помечает Palestinian мужчин как suspected Hamas / PIJ на основании communications / travel / associations patterns. ~37 000 человек помечены.
- **Цифры от самой IDF.** **90% accuracy** — то есть 1 из 10 (≈3700 человек) — false positive по собственному признанию.
- **Process gap.** «Officers devoted almost no resources to double-checking targets, nor bystander locations». Авторизация автоматики до 15–20 civilian casualties per Hamas operative junior level.
- **Источник.** Yuval Abraham (+972 / Local Call), 6 IDF intelligence officers с first-hand experience. UN SG Guterres «глубоко обеспокоен». IDF официально отрицает («claims baseless»).
- **Урок.** AI снижает cost decision-making → масштабирует темпы → **снимает фрикцию**, обеспечивавшую качество human deliberation. 90% accuracy звучит хорошо до момента, когда 10% — это **тысячи людей**. «Accuracy %» — wrong metric для life-and-death; нужно false-positive consequence × population × frequency.
- **Альтернатива.** AI ассистирует ranking / triage, но financial authority остаётся human + adversarial review process. Минимум — calibrated uncertainty estimates + abstention механизмы ("system not confident, requires manual review").
- Источники: [+972 — Lavender investigation](https://www.972mag.com/lavender-ai-israeli-army-gaza/), [Wikipedia — AI-assisted targeting Gaza](https://en.wikipedia.org/wiki/AI-assisted_targeting_in_the_Gaza_Strip), [Lieber Institute — Gospel, Lavender, LOAC](https://lieber.westpoint.edu/gospel-lavender-law-armed-conflict/), [AOAV — Lavender precedent](https://aoav.org.uk/2025/the-lavender-precedent-automated-kill-lists-and-the-limits-of-international-humanitarian-law/), [Foreign Policy — When AI decides life/death](https://foreignpolicy.com/2024/05/02/israel-military-artificial-intelligence-targeting-hamas-gaza-deaths-lavender/), [RUSI — IDF use of AI in Gaza](https://www.rusi.org/explore-our-research/publications/commentary/israel-defense-forces-use-ai-gaza-case-misplaced-purpose), [Time — AI in Gaza/Ukraine](https://time.com/7202584/gaza-ukraine-ai-warfare/), [Democracy Now — Lavender + Where's Daddy](https://www.democracynow.org/2024/4/5/israel_ai), [Incident Database 672](https://incidentdatabase.ai/cite/672/).

### 2.4 Google Project Maven walkout — ethics provision failure (2018)
- **Что произошло.** Март 2018 leaked: Google AI помогает Pentagon анализировать drone surveillance footage (Maven). 4000+ employees подписали open letter; ~12 engineers резигнировали; staged walkouts. К June 2018 Google объявил, что не продлевает контракт.
- **Анти-кейс этики.** Anduril, Palantir, Scale AI **подобрали** контракт. Maven жив, Maven Smart System достиг $1.3B ceiling к 2029. Урок: одна компания может отказаться; индустрия адаптируется.
- **Урок-1.** Personal/employer ethics не блокируют адопцию military-AI на industry level — только legal regulation (например, treaty) может.
- **Урок-2.** Опция «не работать на DoD» теперь редкая роскошь — каждая AI-foundation-model компания обсуждает defense partnerships (OpenAI removed military ban Jan 2024, Anthropic — Palantir/AWS deal).
- Источники: [TechPolicy.Press — Google employees push back](https://www.techpolicy.press/google-employees-push-back-on-government-surveillance-contracts/), [Politics Today — Google AI contracts](https://politicstoday.org/google-controversial-artificial-intelligence-contracts/), [Turing Way — Google Workers + Maven](https://book.the-turing-way.org/ethical-research/activism/activism-case-study-google/), [Wikipedia — Project Maven](https://en.wikipedia.org/wiki/Project_Maven), [KQED — Project Nimbus protest](https://www.kqed.org/news/11971467/protesting-project-nimbus-what-rights-do-silicon-valley-employees-have).

### 2.5 DoD Replicator missed scale (2023–2025)
- **Что произошло.** Replicator-1 цель: thousands of autonomous attritable systems к August 2025. Реальность Sept 2025: «hundreds», не «thousands». Software для command/control multi-vendor swarms — самое слабое звено.
- **Урок.** Hardware scaling быстрее software integration. Multi-vendor autonomy stack — gigantic system engineering challenge (heterogeneous comms, conflicting safety models, vendor lock-ins).
- **Альтернатива.** DAWG (преемник Replicator, Dec 2025) — фокус на larger UAS, less on quantity. Замедление amid honest assessment лучше, чем premature scaling.
- Источники: [DefenseScoop — Replicator transition](https://defensescoop.com/2025/09/03/dod-replicator-drone-tech-transition-fielding-questions-linger/), [Responsible Statecraft — DoD swarms still waiting](https://responsiblestatecraft.org/replicator/), [Breaking Defense — DAWG successor](https://breakingdefense.com/2025/12/its-alive-biden-era-replicator-drone-initiative-lives-on-as-dawg-looking-at-bigger-uass/), [National Defense Magazine — Replicator counter-UAS](https://www.nationaldefensemagazine.org/articles/2024/12/16/pentagons-replicator-initiative-sets-sights-on-counteruas).

### 2.6 Ukrainian F-16 Patriot friendly fire (2024)
- **Что произошло.** Ukrainian F-16 (полёт на перехват крылатых ракет) сбит **дружественной** Patriot batterery. Обстоятельства not fully disclosed.
- **Связь с lec-09.** Совмещённые AI-системы (Patriot ML-based ATR / IFF) + lay coordination = sustained risk даже после lessons-learned 2003.
- **Урок.** Friendly-fire mitigation требует **системного** подхода (deconfliction protocols, IFF reliability, doctrinal training) — никакой single ML upgrade его не закрывает.
- Источники: [Medium — Wes O'Donnell, Friendly Fire Ukraine](https://wesodonnell.medium.com/friendly-fire-in-ukraine-how-can-a-patriot-shoot-down-an-f-16-47d0474868ed).

### 2.7 GPS spoofing of civil aviation in war zones (2023–2026)
- **Что происходит.** Latvia: **820** satellite signal interference cases в 2024 (vs 26 в 2022). Spoofing в Smolensk «aircraft spoofed in a circle»; Black Sea / Crimea spoofing. Affecting commercial flights в Eastern Europe / Middle East.
- **Атрибуция.** Russia EW (Krasukha-4, Borisoglebsk-2); Israel/Iran зона.
- **Урок.** Защита GNSS — collective good; degradation spillover ударяет по civilian aviation который **не участник** конфликта.
- **Альтернатива.** Multi-GNSS receivers, INS-fallback, eLORAN, multi-sensor cross-checks; в долгую — Quantum-INS (DARPA, ESA исследуют).
- Источники: [Foreign Policy — War-zone GPS spoofing civil aviation](https://foreignpolicy.com/2024/03/19/war-zone-gps-spoofing-threat-civil-aviation-russia-iran/), [PBS — Russia GPS jamming European plane](https://www.pbs.org/newshour/world/what-to-know-about-russias-gps-jamming-of-a-european-officials-plane), [Stanford SCPNT — Russia spoofing 2023-24](https://web.stanford.edu/group/scpnt/gpslab/pubs/papers/Lo_ION_ITM_2025_Russia_Spoofing.pdf).

---

## 3. Фундаментальные технические границы

### 3.1 Adversarial attacks on SAR ATR
- **Феномен.** ML-classifiers для SAR ATR vulnerable к adversarial perturbations: small carefully crafted scatterer placements → misclassification. Physical implementation feasibility — установка ложных corner reflectors / decoys реальна.
- **Урок.** DL-classifiers в adversarial domains требуют (a) Bayesian uncertainty estimates, (b) regular adversarial training, (c) abstention pathways. **Standard accuracy benchmark** обманчив — adversary defines test-time distribution.
- **Альтернатива.** Multi-sensor fusion (SAR + Electro-Optical + signals); Bayesian NN с calibrated uncertainty; ensemble methods; reliance на physical signatures, не учёных features.
- Источники: [arXiv — Realistic Scatterer SAR adversarial](https://arxiv.org/abs/2312.02912), [arXiv — Bayesian SAR ATR defense](https://arxiv.org/pdf/2403.18318), [arXiv — Scattering Model Guided SAR](https://arxiv.org/pdf/2209.04779).

### 3.2 LLM hallucinations в military decision support
- **Феномен.** «A human leader, under time pressure, swayed by a highly articulate, confident — yet catastrophically wrong — LLM-generated briefing». DoD AI Ethics guidelines подчёркивают hallucination risk.
- **DoD response.** Prompt discipline training (2 hours, mandatory); "open then closed" prompting; явные human override protocols. Air Force ShOC-N — AI for dynamic targeting **с** mandatory human gates.
- **Урок.** LLM в decision-support — НЕ replacement для analyst, а text-processing accelerator. Confidence от LLM ≠ correctness. Fluent BS = high-risk fluent BS в high-stakes.
- **Альтернатива.** RAG над verified document corpora (не open-web); retrieval citations mandatory; structured outputs с explicit "I don't know" pathways; pairwise comparison не free-form generation для critical questions.
- Источники: [Foreign Affairs — Why military can't trust AI](https://www.foreignaffairs.com/united-states/why-military-cant-trust-ai), [i10x — LLMs in military decision-making risks](https://i10x.ai/news/llms-in-military-decision-making-risks), [SWJ — AI-enabled wargaming](https://smallwarsjournal.com/2026/01/16/ai-enabled-wargaming-cgsc/), [arXiv — LLMs in National Security](https://arxiv.org/html/2407.03453v1), [JAPCC — LLMs transforming warfare](https://www.japcc.org/articles/how-large-language-models-are-transforming-modern-warfare/), [arXiv — Wargame simulations LLM behavior](https://arxiv.org/pdf/2403.03407).

### 3.3 Data-distribution shift в spaceborne ML
- **Феномен.** Models trained on dense data regions (urban, mid-latitudes) underperform на sparse regions (Arctic, ocean, equatorial cloud). Cross-sensor generalization (Maxar → BlackSky) — hard.
- **Урок.** Specify training distribution explicitly + monitor inference distribution; flag OOD samples for human review.

### 3.4 PINN / surrogate model accuracy bounds
- **Феномен.** PINNs для CFD — promising но stable training в high-Re regime сложен; gradient pathologies — общая проблема. Не replacement для full Navier-Stokes в certification-critical CFD.
- **Урок.** PINNs — для preliminary design loop и optimization-cycle acceleration. Final cert требует full-fidelity CFD + flight test.
- Источники: [arXiv — Investigations on PINNs aerodynamics](https://arxiv.org/pdf/2403.17470), [PhilArchive — PINNs in aerospace](https://philarchive.org/archive/TKAPNN).

### 3.5 Brittleness под EW / GPS-denial
- **Феномен.** Lancet «Target Locked» turned off под real EW; Russian Geran-2 потребовала Iranian-made anti-jamming + thermal modules; Ukrainian drones — переход на fibre-optic tethered control (immune to EW).
- **Урок.** Autonomy под EW требует self-contained navigation (INS + visual SLAM + terrain reference); ML-perception на onboard hardware (а не cloud); fail-safe behaviours (return-to-base, loiter, self-destruct), не aggressive completion.
- Источники: [Modern War Institute — autonomous arms race Ukraine](https://mwi.westpoint.edu/battlefield-drones-and-the-accelerating-autonomous-arms-race-in-ukraine/), [Kyiv Post — fiber-optic drones turrets](https://www.kyivpost.com/post/75772), [TechRxiv — GPS spoofing drones Russia-Ukraine](https://www.techrxiv.org/doi/full/10.36227/techrxiv.175203757.71749390/v1).

---

## 4. Этика / LAWS — где AI **не должен** применяться

### 4.1 UN GGE on LAWS + UNGA resolutions (2024–2026)
- **Hard data.**
  - **5 Nov 2024.** UNGA First Committee resolution: **161** for / **3** against / **13** abstain.
  - **2 Dec 2024.** Resolution 79/62 plenary: **166** for / **3** against / **15** abstain.
  - **6 Nov 2025.** First Committee 3rd consecutive resolution: **156** for / **5** against / **8** abstain.
  - **Sept 2025 GGE.** 42 states joint statement — rolling text — sufficient basis для negotiation.
- **States against** (2024): Belarus, North Korea, Russia.
- **States abstaining** (notable): China, India, Iran, Israel, Latvia, Lithuania, Poland, Ukraine.
- **120+ states** support treaty negotiation.
- Источники: [Stop Killer Robots — 161 states UNGA](https://www.stopkillerrobots.org/news/161-states-vote-against-the-machine-at-the-un-general-assembly/), [Stop Killer Robots — 156 states UNGA 2025](https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/), [HRW — UN treaty talks 2025](https://www.hrw.org/news/2025/05/21/un-start-talks-treaty-ban-killer-robots), [Stop Killer Robots — Sept 2025 GGE](https://www.stopkillerrobots.org/news/september-2025-gge-joint-statement/), [HRW — treaty by 2026](https://www.hrw.org/news/2024/08/26/killer-robots-new-un-report-urges-treaty-2026), [Arms Control Association — UN expands LAWS talks](https://www.armscontrol.org/act/2024-12/news/un-moves-expand-autonomous-weapons-discussions).

### 4.2 ICRC position (2024–2025)
- **Recommendations.** New legally binding rules: **prohibit** (a) unpredictable autonomous weapons, (b) AWS designed/used to apply force against persons; **restrict** all others.
- **Ethical core.** «Ethically, ceding life-and-death decisions to machine sensors and software is a dehumanizing process».
- **Procedural core.** «It is not the weapon system that must comply with IHL, but the humans using it».
- Источники: [ICRC — Autonomous Weapons hub](https://www.icrc.org/en/law-and-policy/autonomous-weapons), [ICRC position paper](https://www.icrc.org/sites/default/files/2026-03/4896_002_Autonomous_Weapons_Systems_-_IHL-ICRC.pdf), [ICRC Vienna Conference 2024](https://www.icrc.org/en/document/statement-icrc-president-mirjana-spoljaric-vienna-conference-autonomous-weapon-systems-2024), [ICRC — preserving human control](https://www.icrc.org/en/statement/preserving-human-control-over-use-force-call-regulate-lethal-autonomous-weapon-systems).

### 4.3 Stop Killer Robots — 270 NGOs / 70 countries
- **30 countries** explicitly support a **full ban** на fully autonomous weapons (Algeria, Argentina, Austria, Bolivia, Brazil, Chile, China, Colombia, Costa Rica, Cuba, Djibouti, Ecuador, Egypt, El Salvador, Ghana, Guatemala, Holy See, Iraq, Jordan, Mexico, Morocco, Namibia, Nicaragua, Pakistan, Panama, Peru, Palestine, Uganda, Venezuela, Zimbabwe).
- Источники: [HRW — country positions on fully autonomous weapons](https://www.hrw.org/report/2020/08/10/stopping-killer-robots/country-positions-banning-fully-autonomous-weapons-and), [Stop Killer Robots policy brief](https://www.stopkillerrobots.org/wp-content/uploads/2025/05/Autonomous-Weapons-Systems_Key-issues-and-path-to-a-treaty_Policy-Brief_Stop-Killer-Robots.pdf).

### 4.4 Future of Life Institute / CNAS позиции
- **FLI.** Banned autonomous weapons: те что (a) target humans, (b) highly unpredictable, (c) function beyond meaningful human control. Slaughterbots — immoral + threat to global security.
- **CNAS.** «Today it would be very challenging for autonomous weapons to comply with the laws of war except under narrow circumstances».
- **Paul Scharre / Mike Horowitz.** Authoritative analysts; раскрывают AI-nuclear-weapons risks (особенно ranking suggestions to commanders в crisis).
- Источники: [FLI — Autonomous Weapons project](https://futureoflife.org/project/autonomous-weapons-systems/), [CNAS — Autonomous Weapons program](https://www.cnas.org/research/technology-and-national-security/defense-technology/autonomous-weapons), [CNAS — Army of None commentary](https://www.cnas.org/publications/commentary/army-of-none-autonomous-weapons-and-the-future-of-war).

### 4.5 Project Nimbus — Google/Amazon Israel 2021 → walkouts 2024
- **Что.** $1.2B контракт на cloud + AI + ML для Israeli government & military, sign 2021.
- **2024.** Под No Tech for Apartheid — sit-ins / protests в Sunnyvale, NY, Seattle; 9 arrested, 28 fired (потом ~20 more).
- **Урок.** AI-services поставляются на cloud-уровне; provider не контролирует downstream use. «Acceptable use policy» — слабая защита.
- Источники: [Al Jazeera — Project Nimbus protests](https://www.aljazeera.com/news/2024/4/23/what-is-project-nimbus-and-why-are-google-workers-protesting-israel-deal), [KQED — Protesting Project Nimbus](https://www.kqed.org/news/11971467/protesting-project-nimbus-what-rights-do-silicon-valley-employees-have).

---

## 5. Supply Chain & Dependency Failures

### 5.1 Russian AI-hardware dependency на западные чипы
- **2025 evidence.** Ukrainian wreckage analysis: **NVIDIA Jetson** computers в Geran-2; Intel/AMD chips в Lancet; thermal-vision modules. Russia официально под sanctions.
- **Evasion pathways.** Indian firm Shreya Life Sciences — 1111 Dell PowerEdge XE9680 servers shipped to Russia (Apr–Aug 2024). Smuggling через third countries — задокументировано.
- **Урок.** Sanctions slow but don't stop. Russian AI defense ecosystem **критически** зависим от западного hardware → AI strategy strict-sanctions-vulnerable. Это и **возможность для adversary**, и **риск для US/EU** (свои чипы окажутся в чужих weapons).
- Источники: [Tom's Hardware — Indian firms funneled GPUs Russia](https://www.tomshardware.com/tech-industry/artificial-intelligence/indian-firms-secretly-funneled-amd-nvidia-ai-gpus-to-russia-sanctions-reportedly-skirted-on-hundreds-of-millions-of-dollars-of-hardware), [Fortune — Nvidia smuggling China/Russia/Iran](https://fortune.com/2026/05/13/nvidia-chip-smuggling-china-russia-iran-export-controls-supermicro/), [Sourceability — NVIDIA export controls](https://sourceability.com/post/export-controls-and-geopolitical-risks-test-ai-chip-supply), [Autonomy Global — Geran-2 AI mass production](https://www.autonomyglobal.co/what-the-other-guys-are-doing-russia-mass-producing-ai-enabled-geran-2-drones/).

### 5.2 SDA Tracking Layer schedule risk
- **Что.** Tranche 2 — критическая задержка; Tranche 3 launches FY2029. Hypersonic threat timeline opposing → window для adversary.
- **Урок.** "Build it fast" rhetoric vs reality: 72 satellites + 4 prime contractors + classified payloads = inevitable delays.

### 5.3 ALIS cost-per-flight-hour ($44 000)
- **Метрика.** Inefficiency раскрывает hidden cost AI-fail: $44k/h F-35 vs F-22's lower, in part из-за бесполезных false positives → manual inspections.

---

## 6. Hype Deflation: где AI **не нужен** в aerospace/defense

### 6.1 GenAI для CAD drawings — overhyped
- См. lec-06: generative design ≠ AI generative model в смысле GPT. Для aerospace components используется RL / topology-opt, не diffusion. Diffusion-CAD — research stage.

### 6.2 LLMs как mission planner replacement
- Hallucination + opacity делает LLM unsuitable для **autonomous** mission planning. LLM как **summarizer + draft generator** для analyst — OK; LLM как commander — нет.

### 6.3 Foundation models для real-time control
- Latency, hallucination, hardware footprint делает GPT-class models **непригодными** для tight control loops (sub-second). Лучше использовать smaller distilled / specialized policy models на onboard hardware.

### 6.4 Hype loop drone-swarm "magic"
- **Реальность Ukraine.** Большая часть drone successes — **operator-in-the-loop FPV** или **semi-auto terminal guidance**, не fully-autonomous swarms. Real swarms (decentralized communication, peer-to-peer task allocation) — research demo stage. CETC Atlas — single tablet operator, не truly decentralized.
- **Урок.** Hype vs measurable adoption: количество AI-enabled drones в инвентаре vs количество actually-autonomous strikes. Большой gap.
- Источники: [Lawfare — AI-Enabled drones Ukrainian battlefields](https://www.lawfaremedia.org/article/the-rush-for-ai-enabled-drones-on-ukrainian-battlefields), [Breaking Defense — Russia autonomous drone swarms](https://breakingdefense.com/2025/01/inside-russias-plan-to-build-autonomous-drone-swarms/), [IEEE Spectrum — Autonomous drone warfare](https://spectrum.ieee.org/autonomous-drone-warfare).

### 6.5 «AI заменит pilots» — overhyped
- **Реальность.** X-62A AI-dogfight + Lockheed AI battle mgmt — demonstrations в narrow scripted scenarios. Beyond-visual-range, fuel management, fight management, ROE judgment — далеко от full autonomy. CCA (Fury, YFQ-42) — **collaborative**, supervised pilots overhead.

---

## Top-20 failures table (для plan / slides)

| # | Кейс | Год | Тип failure | Урок |
|---|------|-----|-------------|------|
| 1 | USS Vincennes / Iran Air 655 | 1988 | Human-machine interface under stress | UI testing under combat stress essential |
| 2 | Patriot friendly fire Tornado/F-18 | 2003 | Automation bias + IFF failure | Auto-mode disengage after lessons |
| 3 | Iran captures RQ-170 | 2011 | GNSS spoofing / EW | Multi-sensor positioning |
| 4 | Boeing 737 MAX MCAS | 2018–19 | Single-sensor + opacity | Redundancy + transparency mandatory |
| 5 | Google Project Maven walkout | 2018 | Ethics adoption failure | Personal ethics ≠ industry regulation |
| 6 | F-35 ALIS predictive maintenance | 2010s–24 | False positives + UX failure | Ground truth + small scope |
| 7 | IDF Lavender Gaza targeting | 2023–24 | 90% acc × 37k pop = 3700 FP | "Accuracy" wrong metric for life/death |
| 8 | Russian Lancet ATR rollback | 2022–24 | Demo ≠ production | Operator-in-loop, no autonomous engage |
| 9 | DoD Replicator missed scale | 2023–25 | Software integration lag | Slower honest scale > premature scaling |
| 10 | Ukrainian F-16 Patriot friendly fire | 2024 | IFF + ROE coordination | System-level deconfliction needed |
| 11 | GPS spoofing civil aviation | 2023–26 | EW spillover to non-combatants | Multi-GNSS + INS fallback |
| 12 | SAR ATR adversarial attacks | research | DL classifier brittleness | Bayesian uncertainty + ensemble |
| 13 | LLM hallucinations decision support | research+practice | Confident BS in high-stakes | RAG + structured outputs |
| 14 | PINN training pathologies high-Re | research | Surrogate accuracy limits | PINN for preliminary, not cert |
| 15 | EW degrades autonomous drones | combat | GNSS-only fragile | INS+SLAM+terrain backup |
| 16 | UN GGE 161-3-13 vote | 2024 | LAWS unregulated | Treaty negotiation in progress |
| 17 | ICRC ethical prohibition | 2024 | Dehumanization risk | Strict restrictions on AWS vs humans |
| 18 | Project Nimbus walkout | 2024 | Cloud-AI dual-use ambiguity | Provider can't gatekeep downstream |
| 19 | Russian dependency on NVIDIA chips | 2025 | Sanctions evasion | Hardware supply-chain = strategic risk |
| 20 | Hype: drone swarm "magic" | ongoing | Demo ≠ production scale | Operator-in-loop is current reality |

---

## Volatile-цифры для re-verify (`[VFY-day-of]`)
- IDF Lavender — официальные публикации vs IDF rebuttal status (ongoing).
- Replicator delivered count (changes monthly).
- UN GGE — latest vote outcome.
- Russian chip-evasion enforcement — sanctions update.

