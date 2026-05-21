# 02 — Сегменты логистики и транспорта × AI-приложения

**Summary.** Лекция 13 разделяется на 4 сегмента, у которых **разная среда (по структурированности)**, разные ИИ-стэки, и разные failure modes. Для каждого сегмента: 4–6 верифицируемых кейсов 2024–2026, что считается «работает», где границы. Формат каждого кейса: задача → inputs/outputs → измеренный эффект → failure mode → источник. Используй для §1–§3 плана.

**Принцип сегментации (выбран после анализа альтернатив, см. файл 05):** ось «структурированность среды», от наиболее контролируемой к наиболее хаотичной:
1. **Склад + intralogistics** — контролируемое освещение, известные SKU, защищённые проходы, нет пешеходов.
2. **Магистральный транспорт** (highway robotruck + long-haul robotaxi маршруты) — частично структурированная: HD-карты, ограниченные направления, понятные правила.
3. **Городская подвижность** (robotaxi + city last-mile роботы/дроны) — слабо структурированная: пешеходы, погода, исключения.
4. **Морской / воздушный / port / rail** — особый случай: высоко контролируемая в портах, регулируемая на воде/в воздухе, AI как augmentation.

---

## Сегмент 1. Склад + intralogistics

### 1.1. Amazon — Sparrow / Sequoia / Proteus / Vulcan (2022–2026)

- **Задача.** Bin-picking (Sparrow), high-density storage (Sequoia), autonomous mobile robot для перевозки carts по floor (Proteus), tactile manipulation (Vulcan 2024–2025).
- **Inputs/outputs.** Vision (RGB + depth) + tactile (Vulcan) → распознавание SKU из миллионов → grasp planning → place в right bin.
- **Эффект.** Amazon развернула **>750 000 роботов** в fulfillment-сети к 2024 `[VFY-day-of]`. К 2024 — каждое 4-е заказе обрабатывается с участием робота на каком-то этапе.
- **Failure mode.** Прозрачные / зеркальные / текстильные SKU — слабые места pure-vision (Sparrow); Vulcan добавлен именно для этого. Distribution shift при сезонных catalogue changes (например, Halloween).
- **Дата.** Sparrow — 2022; Sequoia — 2023; Proteus — 2022; Vulcan — 2024–2025.
- **Источники:** [Amazon News — Sparrow](https://www.aboutamazon.com/news/operations/amazon-introduces-new-robotics-solutions); общественные пресс-релизы Amazon Robotics.

### 1.2. Symbotic + Walmart — 400 APD multi-year deployment

- **Задача.** Полная складская автоматизация — pallet handling, depalletization, picking, repalletization.
- **Inputs/outputs.** SKU master data + barcode + vision → robot control → APD (Accelerated Pickup and Delivery) сборка для in-store pickup.
- **Эффект.** Январь 2025 — Walmart обязалась **400 APD** на multi-year period; backlog Symbotic вырос на **>$5 миллиардов**. FY2025 Q4 revenue $618M [1].
- **Failure mode.** Капитальные расходы — десятки $M на APD; ROI требует объёмов; **малые ритейлеры не могут позволить**.
- **Источник:** [SEC — Symbotic 8-K FY2025](https://www.sec.gov/Archives/edgar/data/0001837240/000183724025000043/q1258-k_ex991.htm).

### 1.3. Locus Robotics — AMR co-bot picking

- **Задача.** Collaborative picking — AMR ездит к worker'у, worker кладёт товар на бот, бот едет к следующему месту.
- **Inputs/outputs.** WMS data → robot fleet manager → routing. Cloud-managed.
- **Эффект.** Locus **обработала >5 миллиардов pick'ов** к 2024 в 200+ deployments (FedEx, GXO, DHL партнёрства). Заявка — 2–3× productivity vs ручной picking.
- **Failure mode.** Не работает в densely-packed legacy warehouses без redesign; **не plug-and-play**.
- **Источник:** [Locus Robotics — 5B picks press](https://locusrobotics.com/).

### 1.4. GreyOrange Butler + Geek+ (goods-to-person)

- **Задача.** Перенос rack-полки к picker'у (вместо picker → rack).
- **Эффект.** Высокая throughput, но **рабочая нагрузка на одного picker'а вырастает в разы** — это привело к union-критике в Великобритании.
- **Источник:** [GreyOrange](https://www.greyorange.com/); [Geek+](https://www.geekplus.com/).

### 1.5. Tesla Optimus + Figure 02 — humanoid в складе (research stage)

- **Задача.** General-purpose humanoid для unstructured warehouse / picking tasks.
- **Состояние 2026.** **Production-stage = нет**; demos = да; **production deployments на масштаб >100 единиц = нет** для warehouse-роли. Figure 02 в BMW Spartanburg — pilot, ограниченная роль.
- **Pedagogical note.** Это **hype zone 2025–2026**, важно отделить от reality (см. файл 04).

### 1.6. Российский контекст

- **Wildberries.** Распределительные центры с роботизированной сортировкой; **public deployment metrics ограничены**.
- **Сберлогистика.** Distribution centers с AI-маршрутизацией; **specific metrics не disclosed**.

**Cross-segment Lesson.** Склад = **самая контролируемая среда** в transport/logistics, поэтому здесь AI достигает наибольших ROI. **Это не значит, что AI «лёгкий» — это значит, что среда упрощает задачу**. Foreshadow для keystone-оси.

---

## Сегмент 2. Магистральный транспорт (highway robotruck + interstate)

### 2.1. Aurora Innovation — first commercial driverless trucking (май 2025)

- **Задача.** L4 driverless heavy-duty trucking, маршрут Dallas–Houston (~390 миль).
- **Inputs/outputs.** Camera + LiDAR + Radar + HD-map + Aurora Driver stack → control.
- **Эффект.** Май 2025 — старт коммерческих cargo операций без safety driver. К концу 2025 — расширение до ~10 машин, добавлены Fort Worth–El Paso и Phoenix lanes [11].
- **Failure mode.** **Night driving + rain validation** — выкатывалась во второй половине 2025; **сложные weather conditions** (туман, ice) — за пределами текущего ODD (Operational Design Domain).
- **Источник:** [Aurora press release май 2025](https://ir.aurora.tech/news-events/press-releases/detail/119/aurora-begins-commercial-driverless-trucking-in-texas-ushering-in-a-new-era-of-freight).

### 2.2. КамАЗ — М-11 «Нева» / «Маяк-2.5»

- **Задача.** L3 ADAS магистральный тягач КамАЗ-54901, маршрут СПб–Москва.
- **Inputs/outputs.** Sensors → ADAS stack (Кognitive Pilot + собственный) → ограниченные ACC + lane keeping + emergency braking при магистральной скорости.
- **Эффект.** 67 единиц на М-11 (2024), **10 — в реальных коммерческих перевозках**. К 2025 — 100 единиц, расширение на М-12 + ЦКАД.
- **Failure mode.** L3, не L4 — **safety driver обязателен в кабине**; **очень ограниченный ODD** (одна магистраль, не city streets).
- **Источники:** [КамАЗ press](https://kamaz.ru/press/releases/kamaz_zapustit_kommercheskie_bespilotnye_perevozki/); [ComNews 100 grузовиков 2025](https://www.comnews.ru/content/238302/).

### 2.3. Plus.ai + Volvo / Daimler — supervised L2+/L3

- **Задача.** Driver-assist tier с возможной 1-driver-в-кабине вместо 2 (US team driving requirement).
- **Состояние.** **Supervised**, не driverless. Production deployments через OEM-каналы — медленнее, чем Aurora full driverless, но **более низкий риск и более стабильный business model**.

### 2.4. Kodiak Robotics — defense + commercial dual

- **Задача.** Двойной фокус — DoD контракты + commercial freight.
- **Pedagogical note.** Сigna что **commercial AV-trucking так и не дал coherent revenue model к 2026** — даже выжившие игроки берут defense money параллельно.

### 2.5. Wayve — end-to-end research → production transition

- **Задача.** Embodied AI driving — без HD-maps, end-to-end (camera-only).
- **Состояние.** **Pre-production**; partnerships с тремя OEM (февраль 2026 announcement). $1,2B Series D с NVIDIA, Uber.
- **Failure mode (если оправдается).** End-to-end без HD-map — **research-stage**, не **production-safe для L4** на 2026. Mobileye / Waymo доказывают, что **HD-map + remote ops + formal safety case** работает; pure end-to-end — ещё не доказан.

---

## Сегмент 3. Городская подвижность (robotaxi + city last-mile)

### 3.1. Waymo — лидер robotaxi (Phoenix→multi-city)

- **Задача.** L4 robotaxi в urban environments.
- **Inputs/outputs.** HD-map + multi-sensor (camera + LiDAR + radar) + remote ops backup + Waymo Driver stack → fully driverless paid rides.
- **Эффект.** 500K поездок/неделю март 2026; 3 067 машин 5-го поколения декабрь 2025; **14M поездок суммарно за 2025**. Самый сильный безопасность record на public roads (по compared crash rate per million miles данным NHTSA).
- **Failure mode.** **Phoenix-style (sun belt) сценарий** — лучший случай; **snow / heavy rain** — за пределами ODD (Phoenix, LA, Austin — мягкая погода). Регулярные **remote ops interventions** (telop через 4G/5G).
- **Источники:** [TechCrunch март 2026](https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/); [Waymo blog 2025 review](https://waymo.com/blog/2025/12/2025-year-in-review/).

### 3.2. Tesla Robotaxi Austin — отдельный case (см. файл 04 для critique)

- **Задача.** L4 robotaxi на Tesla Model Y, vision-only stack (без LiDAR), Austin pilot.
- **Состояние май 2026.** ~10 машин, 700K миль платных, 14 ДТП в Austin к февралю 2026, расширение в Houston + Dallas с unsupervised режимом.
- **Pedagogical note.** Tesla — **исключение** в индустрии: единственный major игрок, делающий robotaxi без LiDAR + без HD-map. Это **философская ставка** Маска. Sumary — пока **ещё не доказано** на масштабах Waymo (500K/неделю); 14 ДТП в Austin — **меньше**, чем у Waymo total (sample size меньше) [7].

### 3.3. Apollo Go / Pony.ai / WeRide — Китай

- **Задача.** L4 robotaxi в китайских tier-one + tier-two городах.
- **Эффект.** Apollo Go — 240M км глобально, 17M+ заказов, 22 города (октябрь 2025). Pony.ai — позитивный operating profit per machine в Shenzhen (февраль 2025). WeRide — +761% YoY revenue Q3 2025.
- **Failure mode (для лекции).** **Public crash data в Китае — ограничена**. Сравнение с US — методологически сложно.

### 3.4. Cruise (GM) — **анти-кейс**

- **Состояние.** **Полностью закрыт декабрь 2024** после октябрь-2023 инцидента с протягиванием пешехода 20 футов. **$10B operating losses за 8 лет**.
- **Pedagogical use.** Canonical failure-case (см. файл 04 подробнее).

### 3.5. City last-mile роботы (Coco / Starship / Serve / Avride)

- **Coco Robotics.** >1 000 роботов в LA, 500K+ доставок. Restaurant + grocery в Santa Monica/Koreatown.
- **Starship.** 9M+ доставок globally; 60+ университетских кампусов; 150+ локаций.
- **Avride (Yandex SDG спин-аут).** Тротуар-роботы в Seoul, Austin; food delivery partnerships.
- **Failure mode.** **Sidewalk regulation** — в каждом городе свои правила; **погода** (тротуар-роботы плохо в снеге). **Vandalism** (вандализм) — Berkeley задокументирован.

### 3.6. City дроны (Wing / Manna / Matternet)

- **Состояние 2026.** В suburban-зонах работает (Dallas–Fort Worth Wing, Dublin Manna), в densely-populated urban — **acoustic objections + ATC complexity** = блокировки.

---

## Сегмент 4. Морской / воздушный / port / rail

### 4.1. Port automation — ABB, Konecranes, ZPMC

- **Задача.** Auto STS-cranes (ship-to-shore), auto ASC (automated stacking cranes), AGV (automated guided vehicles) на терминале.
- **Maturity.** **Высокая**, particularly в Rotterdam (Maasvlakte II), Long Beach LBCT, Yangshan (Shanghai), Hamburg HHLA Burchardkai. Это **самая автономная среда** в transport.
- **Why it works.** Closed environment, без пешеходов, GPS+RTK работает, известная geometry контейнеров. **Структурированность ≈ максимальна**.
- **Failure mode.** **Capital-intensive** (миллиарды на новый автоматизированный терминал); **labor pushback** — port unions блокировали автоматизацию в US портах (ILA strikes 2024).

### 4.2. KONUX — rail predictive maintenance (Deutsche Bahn)

- **Задача.** Sensor + AI на switches/turnouts (стрелочные переводы) — самая частая причина железнодорожных задержек в Германии.
- **Эффект.** **Reduces unplanned maintenance** на switches; Deutsche Bahn — основной клиент. Производство в Munich.
- **Источник:** [KONUX rail PdM](https://www.konux.com/).

### 4.3. Hitachi Lumada, GE Digital — generic industrial PdM platforms

- **Состояние.** **Большинство в pilot-purgatory** (см. lec-11 file 04 — McKinsey 2025: 95% GenAI pilots fail; KPMG / Deloitte similar data).
- **Lesson.** **PdM как product category — зрелая**, но **adoption — медленная**, ROI часто overstated vendors. Это **переход к failure-bucket лекции**.

### 4.4. Air traffic — IATA / EUROCONTROL — AI assists, не контроль

- **Задача.** Slot management, gate assignment, baggage routing, fuel optimization (Skywise — Airbus, см. lec-09).
- **Что НЕ делает AI.** **Контроль воздушного движения** — запрещён ICAO/EASA/FAA для **полной автономии**. AI assist controllers, но **финальное решение — диспетчер-человек** [для уровня safety-critical].

### 4.5. Yandex Cargo + Деловые Линии + Wildberries — Россия

- **Yandex Cargo.** B2B доставка с AI-маршрутизацией.
- **Деловые Линии.** Cargo classification + route optimization; **AI применяется**, но specific production metrics частично public.

---

## Cross-cutting наблюдения для плана §2

1. **Среда определяет AI-стэк.** Контролируемая (склад, порт) → robotic + CV inspection; semi-controlled (highway) → L3-L4 ADAS; chaotic (urban) → robotaxi с huge HD-map + remote ops; **regulated waters/skies** → AI only as assist.

2. **Survivor bias.** Из 30+ AV/robotruck стартапов 2017–2022 — выжили **3-4**: Waymo, Aurora, Apollo Go, Pony.ai. Остальные — Cruise, Argo, Embark, TuSimple, Starsky, Waymo Via — закрыты. Это **>$50 миллиардов спущено**.

3. **«AV решит trucker shortage» — false framing.** ATA дефицит 78K водителей; Aurora имеет 10 машин. **AV скейлится медленнее, чем human-labor problems требуют.**

4. **Last-mile = огромные инвестиции, мало profit.** Coco / Starship — operating, но **profitability не доказана**; Nuro — pivot из B2C delivery в licensing. Drone delivery работает в **medical Africa**, не в urban US.

5. **Российский контекст:** **adopt, но не disclose** — паттерн повторяется (см. lec-11 file 03 для production). Это требует осторожности в metrics, не выдумывать. Лучше указать «public-verifiable metrics ограничены».

---

## Источники (inline)

Все ссылки в разделе 01-trends-2026.md воссозданы; здесь дополнительно:

- [Locus Robotics — 5B picks](https://locusrobotics.com/)
- [GreyOrange](https://www.greyorange.com/)
- [Geek+](https://www.geekplus.com/)
- [KONUX](https://www.konux.com/)
- [Aurora press release май 2025](https://ir.aurora.tech/news-events/press-releases/detail/119/aurora-begins-commercial-driverless-trucking-in-texas-ushering-in-a-new-era-of-freight)
