# Лекция 6 «AI в инженерном проектировании и CAD/CAM» — Research-заметка: тенденции 2026

> Issue #101. Собрано 2026-05-17. Приоритет источникам 2025–2026.
> Курс «Отраслевое применение AI», 3-й курс ИУ6 МГТУ им. Баумана.
>
> **Сквозная мысль лекции — таксономия типов ИИ.** В CAD/CAM/CAE под зонтиком «AI» сосуществуют принципиально разные классы методов с разными гарантиями, разной зрелостью и разными провалами. Каждый раздел явно маркирует тип. Базовая таксономия:
>
> | Тип | Что это | Гарантии | Зрелость 2026 |
> |-----|---------|----------|----------------|
> | **Оптимизационный ML / численная оптимизация** (topology optimization: SIMP, level-set, density) | градиентная/эволюционная оптимизация под физические ограничения; ML лишь *ускоряет* решатель | физически валидно (FEM-в-петле), детерминированно | зрелое, в продакшене ~10 лет |
> | **ML-ускорение оптимизации** (CNN/U-Net/DBN-прокси для шагов SIMP) | нейросеть предсказывает промежуточные/финальные плотности | приближённо; требует FEM-доводки | research → ранний продакшен |
> | **Surrogate / ROM / operator-learning** (SimAI, PhysicsAI, neural operators) | нейросеть аппроксимирует решатель CFD/FEM по архиву симуляций | интерполяция в обучающем домене; экстраполяция ненадёжна | продакшен для дизайн-исследования, НЕ для сертификации |
> | **PINN** (physics-informed NN) | сеть минимизирует невязку PDE | силён на разреженных данных/обратных задачах; слаб на резких градиентах | в основном research, точечный продакшен |
> | **Генеративный AI** (diffusion/LLM/neural-CAD: Bernini, Text-to-CAD, CAD-Recode) | генерация геометрии/кода по тексту/картинке/облаку точек | НЕТ физических гарантий; галлюцинации; нужна верификация | концепт → ранний beta-продакшен |
> | **Computer Vision** (дефектоскопия AM, инспекция) | классификация/детекция по изображениям/сенсорам | статистическая точность 95–99% в контролируемых условиях | зрелое в инспекции |
> | **LLM-копайлоты** (Autodesk Assistant, NX/Solid Edge Copilot, Mastercam Copilot) | natural-language → команды/документация/скрипты | помощник, не источник истины; ошибается | быстрый рост 2025–2026 |
>
> Центральный педагогический тезис: **«генеративный дизайн» (topology optimization) ≠ «генеративный AI» (diffusion/LLM)** — это разные вещи под похожими названиями; их путают вендоры в маркетинге и студенты на собеседованиях.

---

## 1. Генеративный дизайн (generative design) — состояние 2026

**Тип ИИ:** в подавляющем большинстве это **оптимизационный ML / численная топологическая оптимизация + эволюционное исследование вариантов**, НЕ генеративный AI (diffusion). Маркетинг вендоров намеренно размывает границу — это материал для блока «провалы/ограничения».

### Autodesk Fusion (generative design)
- Generative design в Fusion работает по схеме: задаём сохраняемую/запрещённую геометрию, нагрузки, материалы, процессы изготовления → облако генерирует **сотни вариантов** под цели (минимизация массы при ограничении напряжений). Это **multi-objective оптимизация + физический решатель в петле**, не нейросеть-генератор.
- 2025–2026: фокус Autodesk сместился на **AI-копайлот поверх** generative design (см. раздел 4). На AU 2025 (16 сентября 2025) анонсированы **Neural CAD foundation models** — отдельный новый класс (раздел 4), не путать с классическим generative design.
- Apr 2026 Product Update Fusion — поток инкрементальных улучшений; конкретику по generative design в апдейте `[FACT-CHECK]` (не извлёк точный список из блога).

### Эталонные промышленные кейсы (с числами — пригодны для слайдов)

**General Motors — кронштейн сиденья (seat bracket), Autodesk, анонс май 2018, остаётся каноническим кейсом:**
- **8 деталей → 1** (консолидация), 3D-печать.
- Выбранный вариант на **40% легче** и **на 20% прочнее** прежнего кронштейна.
- Софт сгенерировал **более 150 альтернатив**.
- Тип ИИ: оптимизация + cloud-перебор, НЕ diffusion.

**Airbus A320 — «бионическая перегородка» (bionic partition), Autodesk + The Living, ~2015–2016:**
- Масса перегородки ~**35 кг** против ~**65 кг** стандартной → **−45% (≈−30 кг)**.
- Структура: кость/клеточный рост (lattice), материал **Scalmalloy** (Al-Mg-Sc сплав Airbus для лазерного спекания).
- **122 напечатанные детали + 40 титановых соединителей**.
- При установке на весь портфель заказов A320: экономия ~**465 000 т CO₂/год** `[FACT-CHECK: цифра CO₂ — из вторичных источников 2015–2016]`.

**Отраслевые ориентиры (2025, вторичные источники):**
- Autodesk заявляет: generative design снижает массу детали **до 40%** при сохранении прочности.
- NASA-исследования: компоненты generative design на **30–50% легче** традиционных при той же прочности `[FACT-CHECK: «NASA-backed studies» — формулировка вторичного источника CIMdata-подобного, точную ссылку не подтвердил]`.
- A380 landing-gear door bracket, jet-engine bracket — типовые academic-кейсы оптимизации под AM.

### Прочие платформы (2025–2026)

- **nTop (бывш. nTopology):** не топология-оптимизатор в классике, а **implicit / field-driven modelling engine** — геометрия задаётся математическими полями, не sketch/feature. nTop 3.0 — **GPU-ускорение** (мгновенный вьюпорт на моделях с миллионами элементов); nTop 4 — холистический DfAM (design/integration/scaling/adoption), **Implicit Interop** (обмен данными в мегабайтах вместо гигабайтов). v5.36.2 — стабилизационный релиз 2026 (Windows 11 24H2, NVIDIA GPU). Тип: процедурная/имплицитная геометрия + оптимизация полей, **не генеративный AI**.
- **Altair Inspire / OptiStruct:** Inspire — CAE-инструмент для дизайнера (geometry + generative design + manufacturing simulation). OptiStruct — «One Model, One Solver» (implicit↔explicit). **PhysicsAI** теперь доступен как расширение прямо в Inspire и может **заменять численный решатель** (см. раздел 3). HyperWorks 2026 (релиз **8 декабря 2025**): generative-алгоритмы автоматически исследуют геометрии, физ-AI до **1000× быстрее** решателя. **Siemens купил Altair (март 2025)** — консолидация в Xcelerator.
- **Siemens NX / Solid Edge:** объединены в экосистему **Designcenter** (общий ядро Parasolid). Декабрь 2025 (NX) / Solid Edge 2026: **Design Copilot** (genAI-ассистент: NL→действие), авто-генерация **до 80% видов 2D-чертежей** на основе анализа миллионов чертежей пользователей. Generative design усиливается через интеграцию с Altair после поглощения.
- **PTC Creo:** Generative Topology Optimization (**GTO**, локально) + cloud **Generative Design Extension (GDX)**. Creo 12: AI-generative с учётом **тепловой физики** (термо+механика+масса), generative-подсказки сборки по интерференции/ограничениям.
- **Dassault CATIA / SOLIDWORKS:** CATIA — performance-driven generation/topology, тысячи альтернатив на раннем этапе, governance через 3DEXPERIENCE digital thread. SOLIDWORKS — AI-подсказки, авто-эскизы и 2D-из-3D; ассистент **AURA AI** показан на 3DX World 2025, **но в beta / на roadmap** (не GA — материал для «хайп vs реальность»).

### Провал/ограничение раздела 1 (для ≥30%-бакета)
- **Терминологическая ловушка:** «generative design» в Fusion/Creo/CATIA — это **топологическая оптимизация + перебор**, а не генеративная нейросеть. Инженер, считающий, что «AI придумал деталь», не понимает, что результат детерминирован физикой и постановкой задачи. Урок: спрашивать «какой это тип ИИ?» до доверия.
- **Не «AI придумывает», а «оптимизатор решает поставленную задачу»:** мусор на входе (неверные нагрузки/ограничения) → красивый, но непригодный «органический» результат. GM-кронштейн потребовал DfAM-итераций и валидации, а не «одной кнопки».
- **Себестоимость AM:** большинство generative-форм требуют 3D-печати (Scalmalloy, титан) → дорого; для серийной механообработки результат часто непроизводим без ре-инжиниринга. Альтернатива: классическая параметрика + ручная оптимизация там, где деталь фрезеруется/льётся.

---

## 2. Topology optimization — современные методы и ускорение (2025–2026)

**Тип ИИ:** базовый метод — **детерминированная численная оптимизация** (НЕ ИИ в смысле нейросетей). ML здесь — *ускоритель*, отдельный слой.

### Классические методы (база лекции)
- **SIMP** (Solid Isotropic Material with Penalization) — density-based, штраф за промежуточные плотности; индустриальный стандарт (OptiStruct, Tosca, Fusion).
- **Level-set** — граница через нулевой уровень функции; точно описывает сложные топологические изменения и чёткую границу.
- **Density-based / ESO/BESO** — эволюционное удаление/добавление материала.

### GPU-ускорение и ML-ускоренная топология (свежее)
- **PeTTO** (arXiv 2509.06971, сент. 2025): pseudo-transient методы + GPU; пример — **200 000 итераций: 176 с на GPU против 8774 с на CPU ≈ ~50× ускорение**.
- **Deep belief networks (DBN) + SIMP:** предсказывают почти-оптимальную плотность из промежуточных шагов, далее доводка SIMP → **>10× сокращение числа итераций**, эффект растёт на больших задачах.
- **U-Net / Res-U-Net / ConvLSTM-autoencoder:** обучаются на траектории оптимизации, предсказывают финальную топологию; **суммарная экономия времени до ~98%** на отдельных задачах `[FACT-CHECK: «до 98%» — обзорная агрегированная цифра, разброс по постановкам велик]`.
- **Reinforcement learning** для генеративных лёгких структур (PMC 2025, статья по RL-based topology optimization для lattice) — research-фронтир.

### Ключевой нюанс для лекции (тип ИИ)
- Чистый SIMP/level-set — это **оптимизация, а не машинное обучение**. Когда вендор пишет «AI-powered generative design», физика всё ещё считается FEM; «AI» — это либо (а) ML-прокси, ускоряющий итерации, либо (б) маркетинг поверх классики.
- ML-прокси даёт *приближение*, требует **FEM-верификации** результата → нельзя сертифицировать деталь по одному предсказанию U-Net.

### Провал/ограничение раздела 2
- **ML-ускоренная топология ≠ доверенный результат:** нейросеть-прокси экстраполирует плохо вне обучающего распределения (новые нагрузки/домены/разрешения сетки) → требуется FEM-доводка; «98% экономии» в обзорах не воспроизводится в продакшене на нестандартных задачах.
- Альтернатива при риске: классический SIMP с полным FEM (медленнее, но детерминирован и сертифицируем) — пример «здесь нейросеть не нужна».

---

## 3. AI-симуляция / surrogate-модели (2025–2026)

**Тип ИИ:** **surrogate / reduced-order models / operator learning** — отдельный класс. Не diffusion, не «AI придумывает физику»; это **аппроксимация решателя по архиву прошлых симуляций**.

### Ansys SimAI (2026 R1 — крупный релиз)
- 2026 R1: реструктуризация на два tier:
  - **SimAI Pro** (новое) — десктоп, локальное обучение/предсказание на воркстейшн-GPU, на уровне компонента; работает с/без GPU (GPU настоятельно рекомендован).
  - **SimAI Premium** — облако/VPC, полное 3D-поле, SaaS, без кода, из архива доверенных симуляций.
- Технология: **AI-ROM (reduced-order surrogate)** — интерполяция между ранее посчитанными результатами. Заявленное ускорение **10–100×** на счётно-тяжёлых задачах по фазам проектирования `[FACT-CHECK: «10–100×» и «boosts 10-100X across all design phases» — из вторичного агрегатора, не из первичной страницы Ansys (timeout при fetch)]`.
- 2026 R1 также: **Ansys GeomAI** — отдельный AI-софт для геометрии (деформация/морфинг геометрии под ML), дополняет SimAI `[FACT-CHECK: детали GeomAI — fetch первичной страницы Ansys дважды дал timeout; описание из заголовков/сниппета]`.

### Altair PhysicsAI (HyperWorks 2026)
- **PhysicsAI** — обучается на историческом архиве симуляций, предсказывает физические исходы; теперь **разворачивается как «решатель»**, заменяя/дополняя численный.
- HyperWorks 2026 (релиз 8 дек 2025): geometric deep learning + GPU-ускоренный ROM → near-real-time; **до 1000× быстрее** традиционного решателя, доступно в защищённой браузерной среде.
- Кейс: **JetZero** (blended-wing) использует FlightStream — ранние точные оценки без массивного HPC.

### SimScale + NVIDIA
- Март 2025: SimScale + **NVIDIA PhysicsNeMo** — «первая в мире foundation-модель» для турбомашин/центробежных насосов; тысячи дизайн-точек в реальном времени, **ускорение ~2700×** через AI-surrogate `[FACT-CHECK: «world's first foundation model» — маркетинговое заявление SimScale; «~2700×» — заявление вендора]`.
- Март 2026: SimScale + AI Engineering GmbH — интеграция SPH-решателя **PAMICS** (meshless CFD в облаке).
- Стратегия 2025: «Physics AI» (предсказание) + «Engineering AI» (агентный co-pilot, валидирует постановку, гоняет оптимизационные петли).

### NVIDIA Modulus → PhysicsNeMo + PINN
- 2025: NVIDIA переименовал **Modulus → PhysicsNeMo**, **open-source** Python-фреймворк для physics-AI в масштабе.
- Спектр методов: чистый PINN → data-driven (neural operators, GNN) → diffusion-генеративные. Multi-GPU/multi-node масштабирование.
- Кейсы (заявления вендора): Kinetic Vision — оптимизация air-knife, PINN ↔ SolidWorks в реальном времени; **Shell — 100 млн× ускорение** инференса для multiscale химреакторов `[FACT-CHECK: «100 million times faster» — маркетинговое заявление NVIDIA/Shell, узкий частный случай]`.

### PINN в инженерии — реальность vs хайп (центральный «провал»-блок)
Из рецензируемых обзоров 2025 (ScienceDirect «Fundamental flaws of PINNs…», MDPI Mathematics 13/3289, Medium/обзоры):
- **Ill-conditioned обучение:** несбалансированные градиенты между PDE-/BC-/data-невязками → vanishing/exploding, экстремальная чувствительность к весам loss и learning rate.
- **Спектральный bias:** PINN тяготеет к пере-сглаженным решениям, плохо ловит резкие фронты, multi-scale и высокочастотные структуры (типичны для реальной механики/CFD).
- **Не бьёт зрелые численные методы** на стандартных прямых задачах; часто **медленнее**, чем решить ту же задачу классическим солвером.
- **Не обобщает:** валиден только в сценариях обучения; новый случай → переобучение.
- **Непрозрачность:** при сбое нельзя атрибутировать ошибку (физика / шум данных / ёмкость сети).
- **Где реально полезен:** разреженные данные, **обратные задачи**, сложная геометрия, ассимиляция данных — НЕ замена FEM/CFD для forward-задач.

### Провал/ограничение раздела 3
- **Surrogate валиден только в обучающем домене:** SimAI/PhysicsAI интерполируют по архиву; экстраполяция (новый режим, материал, геометрия вне распределения) ненадёжна — нельзя использовать для **сертификации**, только для дизайн-исследования/скрининга.
- **Громкие «×1000 / ×2700 / ×100 млн»** — узкие частные случаи и маркетинг; в среднем по парку задач выигрыш скромнее, плюс стоимость генерации обучающего архива (тысячи дорогих FEM/CFD-прогонов) часто игнорируется в ROI.
- Альтернатива/критерий: для однократной задачи без архива и без многих вариантов — **прямой FEM/CFD дешевле и доверенней**, чем строить surrogate.

---

## 4. AI-копайлоты в CAD и text-to-CAD (2025–2026)

**Тип ИИ:** **генеративный AI (LLM + diffusion/neural-CAD)** — принципиально иной класс, без физических гарантий, подвержен галлюцинациям.

### LLM-копайлоты в коммерческих CAD
- **Autodesk Assistant (Fusion):** текстовый промпт → действия. Возможности 2025–2026: **Text-to-Command** (NL → команды Fusion: «split this body…», «extrude this face by 1 inch»), авто-констрейнты эскизов, авто-toolpath, генерация рендер-визуалов (интеграция Microsoft Azure OpenAI / GPT-image-1), **Script Execute** (генерирует и исполняет код через Fusion API).
- **Siemens Designcenter NX / Solid Edge 2026:** **Design Copilot** (genAI-ассистент NL→действие, на знаниях Siemens) + продуктовый чат-бот поддержки; авто-генерация **до 80% видов 2D-чертежей**.
- **Mastercam 2026:** **Mastercam Copilot** (early-adopter) — NL-помощь по программированию CAM + Command-функция-гид.
- **SOLIDWORKS AURA AI** — beta/roadmap (показан 3DX World 2025, не GA).

### Text-to-CAD / foundation-модели для геометрии
- **Zoo.dev (бывш. KittyCAD):** open-source **Text-to-CAD** (текст → 3D, экспорт STEP/STL/OBJ/GLTF…), **ML-ephant** API (design-intent → CAD через KittyCAD Design API), **Zookeeper** — разговорный CAD-агент (анонс май 2025), **Zoo Design Studio v1** — новый стек механического CAD.
- **Autodesk Project Bernini** (research, анонс **8 мая 2024**): генеративная 3D-модель из текста/2D-картинок/эскизов/вокселей/облаков точек. Обучена на **10 млн 3D-форм**, **>3 млрд параметров** (publicly available data + CAD + органика). Раздельная генерация формы и текстуры (кувшин получается полым). **Строго экспериментальный, не для публичного использования**; на AU 2025 — обсуждение переноса в manufacturing cloud.
- **Autodesk Neural CAD** (AU 2025, 16 сент 2025): два foundation-семейства — **Neural CAD for Buildings** (AEC) и **Neural CAD for Geometry** (CAD из текста); цель — **редактируемая B-rep геометрия из одного промпта**, дообучение на проприетарных данных заказчика. Commercial availability — «upcoming», без точной даты.
- **Академический фронтир 2025–2026:** парадигмы — (а) параметрическая (последовательность операций), (б) **B-rep-синтез** (diffusion: **BrepGen**, **VQ-CAD**, **Diffusion-CAD**); **CAD-Recode** (ICCV 2025) — LLM предсказывает CAD-**Python-код** из облака точек (reverse engineering); **FutureCAD** — LLM + BRepGround-трансформер; генерация STEP из NL (arXiv 2601.12641).

### Провал/ограничение раздела 4 (мощный «провал»-блок)
- **Галлюцинации и отсутствие физ-гарантий:** LLM/diffusion CAD генерирует геометрию, которая *выглядит* правдоподобно, но может быть **не-manifold, непроизводимой, не несущей нагрузку**. Бенчмарки 2025 (Mu-SHROOM, CCHall, OpenAI Sept-2025 «models reward confident guessing») показывают: модели уверенно «блефуют»; **domain-knowledge deficiency** в узких инженерных доменах усиливает фактические ошибки. Прямой studied-метрики точности именно text-to-CAD в общих обзорах галлюцинаций нет — `[FACT-CHECK: количественная точность Text-to-CAD/Zoo не подтверждена первичным бенчмарком]`.
- **Bernini сам помечен Autodesk как «strictly experimental, not for public use»** — честный сигнал зрелости; контраст с маркетинговым «AI проектирует за вас».
- **Редактируемость vs mesh-блоб:** ранние генеративные модели выдавали неструктурированный mesh, непригодный для инженерного редактирования; «editable B-rep» (Neural CAD) — заявленная, но ещё не GA цель.
- Альтернатива/критерий: для ответственной несущей детали — параметрический CAD + FEM + ручной инженерный контроль; text-to-CAD уместен на этапе **идеации/концепта**, не финальной документации. Это прямой пример «когда ИИ не применим».

---

## 5. Manufacturing / DfAM: AM, AI-CAM, инспекция (2025–2026)

**Тип ИИ:** смесь — **CV (инспекция дефектов)**, **ML-планирование (toolpath/build sequencing)**, **LLM-копайлот (Mastercam)**. Маркировать раздельно.

### AI для аддитивного производства (DfAM) + AI-CAM
- Тренд 2025–2026: CAD и CAM в 3D-печати/фрезеровке планируются совместно (toolpath, build-sequencing, stock recognition) как единый непрерывный процесс.
- **Mastercam 2026:** Mastercam Copilot (early-adopter) — NL-гид по программированию CAM (тип: **LLM-копайлот**).
- **BMW:** AI-driven AM — оптимизация геометрии, экономия материала, >**100 промышленных 3D-принтеров** под AI-управляемыми workflow `[FACT-CHECK: «100+ принтеров под AI» — вторичный источник]`.
- DfAM с lattice: алгоритмы зашивают производственные ограничения 3D-печати в геометрию (чтобы каждая форма была печатаема без ре-инжиниринга).

### CV-инспекция и дефектоскопия AM (тип: Computer Vision, зрелое)
- Дефекты AM: пористость, делмаинация слоёв, коробление, остаточные напряжения.
- Метрики (research/вендоры 2025–2026): **ResNet50 / EfficientNetV2B0 >99%** точность классификации дефектов; **YOLOv5 > Faster-RCNN** в детекции/локализации; робото-зрение в инспекции **>95%**, в контролируемых условиях **98–100%**.
- Сравнение: AI-зрение **95–99%** стабильно во все смены против **70–80%** у человека-инспектора в реальных условиях `[FACT-CHECK: «70–80% человек» — заявление вендора (ifactoryapp), не независимый бенчмарк]`.

### Провал/ограничение раздела 5
- **Generalization gap:** CV-модели дефектов плохо переносятся между AM-платформами/материалами; редкие дефекты — мало размеченных данных → high-dimensional multimodal сенсорика тяжела. «99%» в контролируемой среде ≠ продакшен на новой машине/порошке.
- **AI-CAM (toolpath) — ассистент, не автопилот:** ошибка в toolpath = сломанный инструмент/деталь; Mastercam Copilot позиционируется как помощь по программированию, окончательная верификация — за инженером. Критерий «AI не заменяет»: безопасность-критичная траектория проверяется симуляцией/человеком.

---

## 6. Аналитика рынка / прогнозы (с источником и датой)

> **Внимание (для лекции, материал про провалы измерения):** оценки рынка «generative design» расходятся на **порядок** между агентствами — пример того, как «AI-рынок $X млрд» нужно читать критически.

- **CAE-рынок (Grand View Research):** $**12,90 млрд** (2025) → $**32,87 млрд** (2033), **CAGR 12,8%** (2026–2033); драйвер — интеграция AI/ML в CAE. US-сегмент CAGR 11,4%.
- **Generative design market — расхождение оценок:**
  - Coherent Market Insights: **$4,68 млрд** (2025), CAGR 16,5% (2025–2032).
  - Mordor Intelligence: **$4,30 млрд** (2025) → **$8,58 млрд** (2030), CAGR 14,82%.
  - Research and Markets: **$4,51 млрд** (2025) → ~$9 млрд (2029), CAGR 18,9%.
  - Grand View Research: **$377,8 млн** (2025) → $451,8 млн (2026), CAGR 19,6% — **на порядок меньше** прочих (разная дефиниция рынка). `[FACT-CHECK: расхождение реально, причина — несовпадающие границы «generative design» у агентств; не ошибка извлечения]`
- **Gartner (макро-контекст AI, не CAD-специфично):** AI-расходы ~**$1,5 трлн** в 2026 (Gartner, цитируется Network World); >80% предприятий используют GenAI API/приложения к 2026 (Gartner press 2023-10-11). Эти цифры — общеотраслевые, не CAD.
- **CIMdata** конкретные цифры по AI-CAD/CAE **не подтверждены** — в выдаче не найдено первичного отчёта CIMdata с числами (см. «Не удалось подтвердить»).

### Провал/ограничение раздела 6
- Расхождение оценок рынка на порядок (×12) → «размер AI-рынка» как аргумент в инженерном решении ненадёжен; зависит от дефиниции и интересов агентства. Урок для студента: проверять методологию и границы рынка, а не цитировать цифру.

---

## Сводка «тип ИИ → раздел» (для слайда-таксономии)

| Раздел | Доминирующий тип ИИ | Зрелость | Главный риск |
|--------|---------------------|----------|--------------|
| 1 Generative design (Fusion/Creo/CATIA) | Численная оптимизация + перебор (НЕ diffusion) | Зрелое | Терминологическая подмена; непроизводимость |
| 2 Topology optimization | Детерм. оптимизация; ML-ускоритель сверху | Зрелое / research | ML-прокси не сертифицируем |
| 3 Surrogate / PINN | Operator learning / ROM / PINN | Продакшен (скрининг) / research (PINN) | Валиден только в домене обучения |
| 4 Text-to-CAD / neural-CAD | Генеративный AI (LLM/diffusion) | Концепт / beta | Галлюцинации, нет физ-гарантий |
| 5 AI-CAM / CV-инспекция | CV (зрелое) + LLM-копайлот | Зрелое (CV) / early (copilot) | Generalization gap; не автопилот |
| 6 Рынок | — | — | Оценки расходятся ×12 |

---

## Источники

1. https://adsknews.autodesk.com/en/news/upcoming-3d-generative-ai-foundation-models/ (accessed 2026-05-17) — первичный, Autodesk AU 2025 (16 сен 2025), Neural CAD foundation models; свежий, авторитетный.
2. https://www.autodesk.com/products/fusion-360/blog/autodesk-assistant-ai/ (accessed 2026-05-17) — первичный, Autodesk Assistant features; свежий (2025–2026).
3. https://www.research.autodesk.com/projects/project-bernini/ (accessed 2026-05-17) — первичный, Project Bernini (анонс 2024-05-08); датирован, авторитетный, но research-only.
4. https://adsknews.autodesk.com/en/news/research-project-bernini/ (accessed 2026-05-17) — первичный, детали обучения Bernini (10M форм, 3B параметров); 2024, релевантен как контекст.
5. https://www.ntop.com/resources/blog/implicit-modeling-for-mechanical-design/ (accessed 2026-05-17) — первичный nTop, implicit modeling; актуально 2025–2026.
6. https://www.digitalengineering247.com/article/ntopology-3.0-powered-by-gpu-acceleration-on-the-market — вторичный, nTop 3.0 GPU; релевантен, дата требует уточнения.
7. https://www.additivemanufacturing.media/products/updated-ntop-platform-advances-am-design-simulations (accessed 2026-05-17) — вторичный, nTop 4 DfAM; свежий.
8. https://www.ansys.com/blog/introducing-ansys-geomai-software (accessed 2026-05-17) — первичный Ansys, 2026 R1 GeomAI/SimAI portfolio; свежий (страница не прогрузилась полностью — частично из сниппета). `[FACT-CHECK]`
9. https://www.ansys.com/products/ai/simai (accessed 2026-05-17) — первичный Ansys SimAI; FETCH TIMEOUT ×2, данные из поисковых сниппетов. `[FACT-CHECK]`
10. https://altair.com/hyperworks-2026 + https://www.prnewswire.com/news-releases/altair-hyperworks-2026-delivers-design-and-simulation-at-scale-with-ai-302634806.html (accessed 2026-05-17) — первичный/PR, HyperWorks 2026 (релиз 2025-12-08), PhysicsAI 1000×; свежий, авторитетный.
11. https://www.trueinsight.io/blog/altair-inspire-2025 (accessed 2026-05-17) — вторичный, Inspire 2025; релевантно.
12. https://www.digitalengineering247.com/article/siemens-altair-the-next-chapter-in-design-and-simulation (accessed 2026-05-17) — вторичный, Siemens-Altair (поглощение март 2025); свежий.
13. https://blogs.sw.siemens.com/nx-design/ai-enabled-design-whats-new-in-designcenter-nx-december-2025-release/ (accessed 2026-05-17) — первичный Siemens, NX Dec 2025 Design Copilot; очень свежий.
14. https://blogs.sw.siemens.com/solidedge/designcenter-solid-edge-2026-artificial-intelligence/ (accessed 2026-05-17) — первичный Siemens, Solid Edge 2026 AI (80% чертежей); свежий.
15. https://www.ptc.com/en/technologies/cad/generative-design (accessed 2026-05-17) — первичный PTC Creo GTO/GDX; актуально.
16. https://www.getleo.ai/blog/solidworks-vs-catia-vs-creo-ai-2026 (accessed 2026-05-17) — вторичный, сравнение CAD-AI 2026 (AURA beta); полезно как обзор, вендор-нейтральность ограничена.
17. https://ohmycad.com/en/ai-cad-what-solidworks-and-catia-will-change-for-designers-and-industrial-startups/ (accessed 2026-05-17) — вторичный, SOLIDWORKS/CATIA 2026; обзорный.
18. https://www.autodesk.com/customer-stories/general-motors-generative-design (accessed 2026-05-17) — первичный, GM seat bracket (40% легче, 20% прочнее, 8→1, 150+ вариантов); кейс 2018, остаётся каноном.
19. https://www.additivemanufacturing.media/news/gm-seat-bracket-made-with-autodesk-generative-design-software (accessed 2026-05-17) — вторичный, подтверждает GM-числа.
20. https://www.research.autodesk.com/projects/bionic-partition/ (accessed 2026-05-17) — первичный, Airbus bionic partition (−45%, ~35 vs 65 кг, Scalmalloy); кейс 2015–2016.
21. https://www.imeche.org/news/news-article/airbus-saves-weight-with-'bionic-partition' (accessed 2026-05-17) — вторичный (IMechE), подтверждает Airbus-числа; авторитетный.
22. https://arxiv.org/html/2509.06971 (accessed 2026-05-17) — первичный, PeTTO GPU topology opt (176с vs 8774с); препринт сент 2025, очень свежий.
23. https://academic.oup.com/jcde/article/10/4/1736/7223974 (accessed 2026-05-17) — рецензируемый обзор «Topology optimization via ML/DL»; авторитетный, но не 2025.
24. https://arxiv.org/pdf/2210.10782 (accessed 2026-05-17) — обзор ML/DL topology opt; 2022, фундамент.
25. https://www.sciencedirect.com/science/article/pii/S0360835225008502 (accessed 2026-05-17) — рецензируемая «Fundamental flaws of PINNs…»; 2025, ключевой для блока провалов.
26. https://www.mdpi.com/2227-7390/13/20/3289 (accessed 2026-05-17) — рецензируемый обзор PINN challenges; 2025, свежий.
27. https://developer.nvidia.com/physicsnemo (accessed 2026-05-17) — первичный NVIDIA, PhysicsNeMo; актуально 2025–2026.
28. https://developer.nvidia.com/blog/physics-ml-platform-physicsnemo-is-now-open-source/ (accessed 2026-05-17) — первичный, Modulus→PhysicsNeMo open-source (2025); свежий.
29. https://www.simscale.com/press/simscale-unveils-worlds-first-foundation-ai-model-centrifugal-pump-simulation-built-nvidia-physicsnemo/ (accessed 2026-05-17) — первичный SimScale PR (март 2025, ~2700×); вендор-заявление. `[FACT-CHECK]`
30. https://www.simscale.com/blog/agentic-ai-in-engineering/ (accessed 2026-05-17) — первичный SimScale, agentic AI workflows; свежий.
31. https://cdfam.com/simscale-bcn/ (accessed 2026-05-17) — вторичный (CDFAM), agentic engineering; 2025–2026.
32. https://www.research.autodesk.com/projects/project-bernini/ — (см. п.3).
33. https://arxiv.org/html/2603.11831v1 (accessed 2026-05-17) — препринт FutureCAD (LLM+B-rep grounding); 2026, фронтир. `[FACT-CHECK: arXiv-id вида 2603.* — необычная нумерация, перепроверить]`
34. https://openaccess.thecvf.com/content/ICCV2025/papers/Rukhovich_CAD-Recode_..._ICCV_2025_paper.pdf (accessed 2026-05-17) — рецензируемый ICCV 2025, CAD-Recode (point cloud→CAD-код); авторитетный, свежий.
35. https://www.computer.org/csdl/journal/tg/2025/12/10857640/23VCfOwtkWc (accessed 2026-05-17) — рецензируемый, Diffusion-CAD; 2025, свежий.
36. https://arxiv.org/pdf/2601.12641 (accessed 2026-05-17) — препринт STEP-из-NL; 2026. `[FACT-CHECK: arXiv-id]`
37. https://encycam.com/articles/top-trends-in-cad-cam-development-for-2025-2026/ (accessed 2026-05-17) — вторичный, CAD/CAM тренды 2025–2026; обзорный.
38. https://www.digitalengineering247.com/article/mastercam-2026-features-ai-enabled-cam-intelligence (accessed 2026-05-17) — вторичный, Mastercam 2026 Copilot; свежий.
39. https://www.mdpi.com/1424-8220/26/3/788 (accessed 2026-05-17) — рецензируемый обзор ML-vision robotic inspection; 2026, свежий.
40. https://accscience.com/journal/MSAM/4/3/10.36922/MSAM025150022 (accessed 2026-05-17) — рецензируемый, CNN дефекты metal 3D printing; 2025.
41. https://ifactoryapp.com/article/ai-vision-inspection-manufacturing-defect-detection (accessed 2026-05-17) — вторичный/вендор, метрики CV-инспекции; цифры «70–80% человек» — вендор. `[FACT-CHECK]`
42. https://www.grandviewresearch.com/industry-analysis/computer-aided-engineering-cae-market (accessed 2026-05-17) — вторичный, CAE-рынок $12,9→32,87 млрд; агентство.
43. https://www.mordorintelligence.com/industry-reports/generative-design-market (accessed 2026-05-17) — вторичный, GD-рынок $4,30→8,58 млрд; агентство.
44. https://www.coherentmarketinsights.com/market-insight/generative-design-market-5141 (accessed 2026-05-17) — вторичный, GD $4,68 млрд; агентство.
45. https://www.grandviewresearch.com/industry-analysis/generative-design-market-report (accessed 2026-05-17) — вторичный, GD $377,8 млн (расходится ×12); агентство.
46. https://www.networkworld.com/article/4058786/gartner-ai-spending-to-reach-1-5-trillion-dollars-this-year.html (accessed 2026-05-17) — вторичный (цитирует Gartner), AI-расходы $1,5 трлн 2026; макро-контекст.
47. https://www.gartner.com/en/newsroom/press-releases/2023-10-11-gartner-says-more-than-80-percent-of-enterprises-... (accessed 2026-05-17) — первичный Gartner press; 2023, общеотраслевой.

---

## Что НЕ удалось подтвердить / нуждается в fact-check

- **Ansys SimAI первичные цифры** (10–100× ускорение, SimAI Pro/Premium детали, GeomAI): страница `ansys.com/products/ai/simai` и `.../introducing-ansys-geomai-software` дважды дали timeout при WebFetch — данные из поисковых сниппетов, не из первичного текста. Помечено `[FACT-CHECK]`.
- **«NASA-backed studies: 30–50% легче»** — формулировка вторичного агрегатора; первичную NASA-ссылку не нашёл.
- **Airbus «465 000 т CO₂/год»** — из вторичных источников 2015–2016, не из первичного Airbus-релиза.
- **SimScale «~2700×» и «world's first foundation model»**, NVIDIA/Shell «100 млн×» — маркетинговые заявления вендоров, узкие частные случаи; не независимая верификация.
- **CV-инспекция «70–80% у человека»** — заявление вендора (ifactoryapp), не независимый бенчмарк.
- **CIMdata конкретные цифры по AI-CAD/CAE** — не найдено первичного отчёта с числами в выдаче (только упоминания CIMdata как лидера-аналитика без данных).
- **arXiv-идентификаторы вида 2603.* / 2601.*** (FutureCAD, STEP-из-NL) — необычная нумерация для мая 2026; названия/контент правдоподобны, но id перепроверить перед цитированием в лекции.
- **Расхождение оценок рынка generative design на порядок (×12)** — подтверждено как факт расхождения (разные дефиниции рынка), но конкретное «правильное» число назвать нельзя — это само по себе материал для лекции про критичность к рыночным цифрам.
- **Точная количественная метрика accuracy для Text-to-CAD / Zoo.dev** — не подтверждена первичным бенчмарком; общие обзоры галлюцинаций LLM не покрывают именно CAD-домен численно.
