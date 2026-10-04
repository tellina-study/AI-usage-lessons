---
id: s19
type: alternatives_list
duration_min: 2
assertion: "Альтернатива Q3: Eclipse / INTERSECT / CMG (IMEX, STARS, GEM) / OpenFOAM. Senior геофизик + классическая интерпретация — остаётся essential. AI augmentation поверх, не replacement."
learning_goal: "LO3 alternative Q3 + frontier без analog criterion"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part2.md]
  sections: ["§2.7-§2.8 Eclipse alternatives + sparse data limit"]
visual:
  type: diagram
  description: "4 рамки альтернатив в 2×2 grid: Eclipse, INTERSECT, CMG, OpenFOAM с brief role; bottom — gold callout «PINN research-grade, не commercial»"
  acquisition_tier: self_render
visible_numbers: ["1983 Eclipse release", "$200-500k/год senior геофизик vs $5-20M foundation model"]
russification_check: "Eclipse, INTERSECT, CMG, IMEX, STARS, GEM, OpenFOAM, SLB, ECL, Computer Modelling Group — brand list; «пластовый симулятор», «improved oil recovery», «гидравлический фрекинг», «physics-informed neural network (PINN)», «дифференцируемые физические симуляторы» inline gloss."
speaker_notes_target_words: 230
---

# Альтернатива Q3: 4 physics simulators + senior геофизик

## Visible content

Заголовок: «Альтернатива Q3: physics-based simulators + senior expertise» (28pt deep ocean).
Sub: «AI augmentation поверх, не replacement. Через 5 лет Eclipse будет стандартом — не AI-замена.» (16pt italic)

**4 Ocean rounded cards в 2×2 grid:**

**Eclipse (SLB).** Industry-standard reservoir simulator с 1983. Coupled fluid + heat + chemistry equations на 3D-сетке. Mature reservoirs + regulatory submissions.

**INTERSECT (SLB).** Next-gen Eclipse. Высокое разрешение, лучше параллелизация. Новейшие месторождения.

**CMG (Computer Modelling Group, Калгари).** Три продукта: **IMEX** (black-oil), **STARS** (thermal EOR, паровые методы), **GEM** (compositional, газоконденсатные системы). Niche, stable.

**OpenFOAM.** Open-source CFD. CCS plume modelling, multi-phase flow, gas plume modelling.

**Bottom bar (gold tint) — Экономика senior expertise:**

- Senior геолог 25+ лет = **$200-500k/год**.
- Foundation model = **$5-20M/год** capex + opex (= 5-25 senior geologists за стоимость одной инсталляции).
- Окупается только если воспроизводит работу 5-25 геологов — что в 2026 году **не доказано** ни одним публичным бенчмарком.

**Когда AI augmentation работает поверх:** screening 10k сценариев → 10 best в Eclipse для валидации (hybrid); auto-tuning calibration параметров (50-80× ускорение); quick-look interpretation сейсмики (с senior QC).

## Speaker notes

Это ключевой раздел для Q3. Когда AI в разведка фронтиров буксует — что используют операторы вместо? Ответ — физически обоснованный simulators, разработанные за десятилетия и хорошо валидированные.

Eclipse — отраслевой стандарт симулятор пласта от SLB. Используется с восьмидесятых; сегодня — ключевой для большинства мейджоров. Решает coupled fluid плюс heat плюс уравнения химии на 3D-сетке пласта. Параметризируется через свойства породы, fluid PVT, kinetics. Скорость — десятки часов до дней на крупной модели; точность — well-characterized.

INTERSECT — next-generation Eclipse от SLB. Высокое разрешение, лучше параллелизация.

CMG — Computer Modelling Group, Калгари. Три продукта. IMEX — чёрная нефть симулятор пласта. STARS — thermal и advanced processes, для теплового методы увеличения нефтеотдачи (МУН), паровых методов в тяжёлой нефти. GEM — compositional simulator для газоконденсатных систем. Niche, но stable.

OpenFOAM — open-source CFD пакет. Не симулятор пласта per se, но используется для CFD-моделирования в CCS, в многофазный поток, в gas plume modelling.

Когда использовать физически обоснованный вместо ML. Mature коллектор плюс регуляторный отчёт: регулятор требует физически прослеживаемый submission. Complex методы увеличения нефтеотдачи (МУН) scenarios. Hydraulic fracturing modelling. CCS миграция шлейфа на 100-летнем горизонте. Frontier basin без analog — ML не на чем обучать.

PINN (нейросеть с встроенной физикой) — physics-informed neural networks — попытка построить мост: speed of ML плюс consistency of physics. Активно изучается academia с 2019 года. К 2026 году PINN (нейросеть с встроенной физикой) — не mainstream commercial product. Это потенциальный мост в будущее, но не сейчас.

Экономика. Senior геолог с двадцатью пятью годами опыта стоит компании двести-пятьсот тысяч долларов в год. Foundation model с обучением плюс интеграцией — пять-двадцать миллионов в год. Арифметика простая: пять-двадцать пять старших геологов за стоимость одной инсталляции базовая модель. Foundation model окупается только если воспроизводит работу пяти-двадцати пяти геологов — что в 2026 году не доказано ни одним публичным бенчмарком.
