# Real applications — AI в сельском хозяйстве 2026

Каталог named реальных применений AI в агросекторе с метриками, ограничениями и источниками. Все цифры — с inline URL. Маркер `[VFY-day-of]` означает, что факт нужно перепроверить непосредственно перед лекцией.

---

## 1. Precision farming / field crops

### 1.1 John Deere See & Spray Ultimate (Blue River Technology)

- **Vendor / scope:** John Deere (Blue River Technology acquired 2017 за $305M). See & Spray Select (fallow / pre-emergence, retrofit, 2021), Premium (factory-fit, 2023), Ultimate (in-crop, dual-tank, 2023). Цена в 2025: $1/acre fallow, $5/acre in-crop через Application Savings Guarantee subscription.
- **2025 metrics:**
  - Развёрнуто на **более 5 млн акров** за сезон 2025 (территория больше штата Нью-Джерси) — источник: <https://www.deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/>
  - Среднее сокращение non-residual гербицидов на **~50%**, экономия **~31 млн галлонов** смеси за сезон — источник: <https://www.agtechnavigator.com/Article/2025/11/10/john-deere-uses-ai-to-slash-farmers-input-costs/>
  - Прирост урожайности соевых: **+2.0 bu/A** (в среднем), в лучших случаях **+4.8 bu/A** благодаря reduced chemical injury — источник: <https://modernconstructionnews.com/news/john-deeres-see-spray-technology-covers-over-five-million-acres-in-2025-boosts-yields-by-up-to-4-8-bu-a/>
  - Hardware: **36 камер**, скан **2500 sq ft/sec** на 16 mph, классификация и actuation за миллисекунды; **>95% детекции Palmer amaranth в хлопке**, включая укрытые в canopy — источник: <https://growiwm.org/a-deep-dive-on-the-see-spray-ultimate-system-from-john-deere-blue-river/>
- **Ограничения:**
  - Работает только в системах John Deere ExactApply на R-серии прыскивателей; не retrofittable на чужие машины.
  - Эффективность зависит от чистоты междурядий — при сильном смешивании culture/weed canopy показатель падает.
  - $5/acre in-crop экономически оправдан только при высоких pesticide costs (broadacre row crops в США), для small farms < 500 ha — не окупится.
- **Sources:**
  - <https://www.deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/>
  - <https://www.agtechnavigator.com/Article/2025/11/10/john-deere-uses-ai-to-slash-farmers-input-costs/>
  - <https://hpj.com/2025/11/12/john-deere-customers-use-see-spray-technology-across-5-million-acres-in-2025-as-company-touts-results-for-producers/>
  - <https://www.oklahomafarmreport.com/okfr/2025/12/29/john-deeres-see-spray-cuts-herbicide-use-50/>

### 1.2 Climate FieldView (Bayer)

- **Vendor / scope:** Bayer (acquired The Climate Corporation от Monsanto deal 2018; Climate Corp основана 2006 в Сан-Франциско, $1.1B покупка Monsanto в 2013). Платформа farm data management + satellite imagery + variable-rate prescriptions.
- **2025 metrics:**
  - **>250 млн подписных акров** в **23 странах** — источник: <https://geo.sig.ai/brands/climate-fieldview>
  - В США подписные акры составляют **>50% всех площадей кукурузы, сои и хлопка**.
  - Farmers using FieldView seed scripts: **+5 bu/acre vs custom scripts**; ~15% input savings — источник: <https://climate.com/en-us.html>
  - Новая фича 2024: "Your Farm at a Glance" — summary overview с harvest progress, moisture, yield, top hybrids — источник: <https://www.agrinews-pubs.com/news/science/2025/01/08/bayers-recent-fieldview-release-turns-farm-information-into-answers/>
- **Ограничения:**
  - Vendor lock-in: рекомендации smart по Bayer/Pioneer hybrids; для независимых селекций — биас.
  - Покрытие культур узкое (corn / soy / cotton / wheat), для specialty crops почти не работает.
  - Точность рекомендаций деградирует за пределами Corn Belt (валидационные данные ориентированы на US Midwest).
- **Sources:**
  - <https://www.cropscience.bayer.us/brands/deltapine/climate-field-view>
  - <https://geo.sig.ai/brands/climate-fieldview>
  - <https://www.bayer.com/en/us/news-stories/fieldview-features>

### 1.3 xarvio FIELD MANAGER (BASF Digital Farming)

- **Vendor / scope:** BASF Digital Farming GmbH (часть BASF Agricultural Solutions). Crop modeling + satellite + AI рекомендации (Healthy Fields, Bioenergy, Fruits & Veggies, Grapes, AgBusiness варианты).
- **2025 metrics:**
  - **>130 000 farmers** и консультантов подписаны; **field area >20 млн гектаров** — источник: <https://www.basf.com/global/en/media/news-releases/2025/09/p-25-176>
  - Продукты SCOUTING / FIELD MANAGER / HEALTHY FIELDS используются в **>100 странах**.
  - 2025 launches: xarvio FIELD MANAGER For Fruits & Veggies (февраль), For AgBusiness (USA, Canada, then Argentina & Brazil late 2025), For Grapes (France, Italy, Spain, Türkiye, ноябрь 2025).
  - BASF Japan запустил **первую в Японии outcome-based rice yield guarantee** через xarvio HEALTHY FIELDS с AI-сервисом "Humus" — источник: <https://www.basf.com/global/en/media/news-releases/2025/10/p-25-191>
- **Ограничения:**
  - Recommendations часто tied to BASF chemistry (Revysol, Xemium); independent retailers недополучают value.
  - Free tier ограничен — расширенные рекомендации платные ($35-50/ha/year [VFY-day-of]).
  - Для русско-/центральноазиатского рынка не локализован.
- **Sources:**
  - <https://www.basf.com/global/en/media/news-releases/2025/02/p-25-016>
  - <https://www.basf.com/global/en/media/news-releases/2025/09/p-25-176>
  - <https://www.basf.com/global/en/media/news-releases/2025/11/p-25-227>
  - <https://www.basf.com/global/en/media/news-releases/2025/10/p-25-191>

### 1.4 Taranis (AI crop scanning)

- **Vendor / scope:** Taranis, израильский стартап (основан 2015, Tel Aviv). Самолёт/дрон + leaf-level 0.3 mm/pixel CV для weeds / insects / diseases / nutrient deficiencies. Total funding **$107.05M** (Series D + extensions).
- **2025 metrics:**
  - **Millions of acres** scanned в США, Бразилии, Европе — источник: <https://www.taranis.com/>
  - **>100 agribusiness customers** (ag retailers, crop protection companies).
  - Октябрь 2024: многолетнее партнёрство с **Syngenta Crop Protection** для US ag retailers — источник: <https://www.croplife.com/smart-tech/syngenta-crop-protection-and-taranis-partner-to-drive-ai-powered-agronomy-solutions-and-business-opportunities-for-ag-retailers/>
- **Ограничения:**
  - Требует cooperative pilots + ground crew; не self-serve farmer-facing.
  - Стоимость on-demand fly-over [VFY-day-of] — недоступна smallholders.
  - Cloud cover days = no scan (avian sensor не SAR).
- **Sources:**
  - <https://www.taranis.com/>
  - <https://finder.startupnationcentral.org/company_page/taranis>
  - <https://www.prnewswire.com/news-releases/syngenta-crop-protection-and-taranis-partner-to-drive-ai-powered-agronomy-solutions-and-business-opportunities-for-retailers-302275789.html>

### 1.5 Granular Insights (Corteva)

- **Vendor / scope:** Corteva Agriscience. Granular acquired DuPont в 2017; Corteva в 2022 продала Granular Business в Traction AG, оставила Granular Insights (поле-уровневые prescriptions + 3-m satellite + variable-rate).
- **2025 metrics:**
  - Pioneer seed-aligned рекомендации, integrate с Corteva Strategic Plans.
  - Variable-rate prescriptions с weather/soil topography/irrigation inputs.
  - Точные числовые метрики 2025 не disclosed Corteva publicly.
- **Ограничения:**
  - Жёсткий vendor lock-in (только для Corteva seed/chemistry клиентов).
  - Bench-test показывает, что free 3-m imagery даёт rough resolution для micro-zones — не заменяет sub-meter Planet/Maxar.
- **Sources:**
  - <https://www.corteva.com/us/products-and-solutions/digital-solutions/granular-insights.html>
  - <https://www.corteva.com/us/press-releases/granular-provides-new-digital-nitrogen-management-options-to-farmers.html>

### 1.6 Yara Atfarm + N-Sensor

- **Vendor / scope:** Yara International ASA (Норвегия). N-Sensor — tractor-mounted reflectance device для variable-rate N (с 1990-х). Atfarm — free satellite-based remote crop monitoring app, использует proprietary N-Sensor Index (улучшенный NDVI, работает в late-season dense canopy).
- **2025 metrics:**
  - Algorithm основан на **>25 лет research + 250+ field trials** — источник: <https://www.yara.us/crop-nutrition/tools-and-services/atfarm/>
  - Атfarm бесплатен для базового мониторинга, премиум — variable-rate maps + N-Tester BT integration.
- **Ограничения:**
  - В первую очередь оптимизирован под cereals (wheat, barley); для маржинальных культур и тропиков биас.
  - Effective только когда farmer применяет Yara fertilizer (рекомендации — в формате Yara products).
- **Sources:**
  - <https://www.yara.us/crop-nutrition/tools-and-services/atfarm/>
  - <https://www.yara.com/digital-farming/our-digital-farming-solutions/>

### 1.7 Syngenta Cropwise

- **Vendor / scope:** Syngenta (запущен 2020). Cropwise Operations, Seed Selector, Spray Assist, Protector. AI + agronomic data для recommendations.
- **2025 metrics:**
  - **>70 млн гектаров** под управлением в **>30 странах** — источник: <https://www.syngenta.com/media/media-releases/2025/syngenta-opens-cropwise-digital-platform-developers-co-innovate-and>
  - Партнёрство с Al Dahra (Romania, Serbia, Egypt, Morocco): **>220 000 acres** охвачено digital farm management — источник: <https://www.agtechnavigator.com/Article/2025/10/08/tech-insight-exploring-syngentas-cropwise-platform/>
  - Ноябрь 2025: **Cropwise Open Platform** для third-party developers — попытка экосистемы.
  - Партнёрство с Planet Labs (renewed 2025) для near-daily imagery.
- **Ограничения:**
  - Syngenta-IPSOS исследование показало: **digital divide расширяется** — крупные фермы adopt быстрее, smallholders отстают.
  - Trust, data control, proof of local results — главные барьеры adoption.
- **Sources:**
  - <https://www.syngenta.com/media/media-releases/2025/syngenta-opens-cropwise-digital-platform-developers-co-innovate-and>
  - <https://www.agtechnavigator.com/Article/2025/10/08/tech-insight-exploring-syngentas-cropwise-platform/>
  - <https://www.syngenta.com/media/media-releases/2025/new-level-precision-agriculture-thanks-renewed-partnership-between>

### 1.8 Planet Labs + ICEYE (satellite imagery for ag)

- **Vendor / scope:** Planet Labs PBC — Dove constellation, daily revisit, 3-5m resolution. ICEYE — SAR (Synthetic Aperture Radar), through-cloud imaging.
- **2025 metrics:**
  - Глобальный satellite-imaging-for-agriculture рынок: **$588M в 2024**, прогноз $1.36B к 2034 (CAGR 8.9%) — источник: <https://www.insightaceanalytic.com/report/satellite-imaging-for-agriculture-market/1851>
  - Syngenta-Planet partnership: near-daily imagery для глобальных фермеров (renewed 2025).
  - ICEYE — единственный SAR-provider с daily revisit; критичен для tropics + monsoon regions, где cloud cover >60% days.
- **Ограничения:**
  - 3m resolution Planet Dove не показывает single-plant signals (Taranis-уровень — 0.3 mm нужен hi-res aerial).
  - SAR проигрывает в spectral signature: не различает chlorophyll-states как multispectral.
- **Sources:**
  - <https://www.planet.com/industries/agriculture/>
  - <https://www.syngenta.com/media/media-releases/2025/new-level-precision-agriculture-thanks-renewed-partnership-between>
  - <https://www.insightaceanalytic.com/report/satellite-imaging-for-agriculture-market/1851>

---

## 2. Autonomous machinery

### 2.1 Monarch Tractor MK-V

- **Vendor / scope:** Monarch Tractor, Inc. (Livermore, CA). Полностью электрический, driver-optional smart tractor. 70 hp peak / 40 hp continuous, swappable battery pack, V2X charging.
- **2025 metrics:**
  - Founder Series production launched декабрь 2022.
  - **First customer: Constellation Brands** (крупнейший US импортёр пива, премиум-вино) — 6 Founder Series MK-V для Wente Vineyards — источник: <https://www.monarchtractor.com/news/mk-v-first-commercially-available-electric-driver-optional-smart-tractor>
  - May–July 2025: autonomy usage hours в dairies **nearly tripled** — источник: <https://www.monarchtractor.com/blog/self-driving-tractor-usage-growing>
  - Calif CORE 2025 subsidy: vouchers расходятся быстрее availability (открытие 19 августа 2025).
  - Расширение в Europe + MonarchOne platform для off-highway vehicles.
- **Ограничения:**
  - **Autonomy feature commercially available только для одной задачи — dairy cattle feed pushing**; другие autonomy modes — limited release.
  - Battery range ~10 рабочих часов под нагрузкой — для broadacre фермы (24/7 sprayers) недостаточно.
  - Цена ~$70 000+ [VFY-day-of] — без CORE subsidy неконкурентна с дизельным эквивалентом.
- **Sources:**
  - <https://www.monarchtractor.com/news/mk-v-first-commercially-available-electric-driver-optional-smart-tractor>
  - <https://www.monarchtractor.com/news/core-subsidy-2025>
  - <https://www.monarchtractor.com/blog/self-driving-tractor-usage-growing>
  - <https://www.farm-equipment.com/articles/22294-monarch-tractor-expansion-across-the-us-and-europe>

### 2.2 Bear Flag Robotics → John Deere Autonomous

- **Vendor / scope:** Bear Flag Robotics (Silicon Valley startup, founded 2017). Acquired by John Deere August 2021 за **$250M**. Develop autonomous driving stack для retrofit в existing tractors.
- **2025 metrics:**
  - Stack интегрирован в Deere Autonomous Tractor portfolio (8R Autonomous launched CES 2022, expanded для tillage 2023; Autonomy 2.0 announced CES 2025 для articulated dump trucks, orchard tractors, sprayers, mowers).
  - Скорость / hourly performance — vendor-claimed, не publicly disclosed acreage 2025.
- **Ограничения:**
  - Autonomous tractor требует GPS+inertial+computer vision stack; cellular dead zones в US Plains реально ломают operation.
  - High-end pricing (8R Autonomous ~$700K+ base [VFY-day-of]); ROI требует >2000 acres + labour shortage.
- **Sources:**
  - <https://www.oemoffhighway.com/electronics/smart-systems/automated-systems/press-release/21591189/deere-company-john-deere-acquires-robotics-startup-to-accelerate-autonomous-farm-equipment>

### 2.3 PTx Trimble (AGCO + Trimble JV)

- **Vendor / scope:** PTx Trimble — JV созданный 1 апреля 2024 года: Trimble продал свою Ag-бизнес-линию в AGCO за **$1.9 млрд cash + equity stake**. Объединили Trimble precision ag + AGCO JCA Technologies.
- **2025 metrics:**
  - Mixed-fleet precision ag (factory-fit + retrofit) — single biggest non-OEM precision player после consolidation.
  - Конкретные acreage/revenue metrics только в SEC filings — источник: <https://www.sec.gov/Archives/edgar/data/0000864749/000086474925000243/a2025q2-8kex991.htm>
- **Ограничения:**
  - Integration риск (Trimble vs JCA tech stacks); первый full year revenue показал mixed results [VFY-day-of].
- **Sources:**
  - <https://www.sec.gov/Archives/edgar/data/0000864749/000086474925000023/a2024q4-8kex991.htm>
  - <https://www.sec.gov/Archives/edgar/data/0000864749/000086474925000243/a2025q2-8kex991.htm>

### 2.4 Naïo Technologies (Oz / Dino / Orio)

- **Vendor / scope:** Naïo Technologies (Toulouse, France). Manufactured in France. Robots для weeding/seeding/transplanting: **Oz** (small, vegetable beds), **Dino** (mid-size, field-scale vegetables), **Orio** (новейший, 2025, sown crops, young trees).
- **2025 metrics:**
  - **40 certified partners** в **>20 странах**, manufactured с European components.
  - Orio operates with Augmented Autonomy, **multiple hectares/day** без supervisor.
  - World FIRA 2025 + SIVAL 2025 — major launches Orio.
- **Ограничения:**
  - Низкая мощность (Oz < 2 hp eq.); не для broadacre.
  - Цена Orio €100K+ [VFY-day-of]; ROI realistic только для специализированных vegetable растениеводств с labour shortage.
- **Sources:**
  - <https://www.naio-technologies.com/en/news/naio-technologies-unveils-2025-innovations-at-sival/>
  - <https://www.naio-technologies.com/en/orio-robot/>
  - <https://www.agricultural-robotics.com/news/naio-technologies-unveils-new-advances-in-agricultural-robotics-at-world-fira-2025>

### 2.5 AgXeed AgBot T2

- **Vendor / scope:** AgXeed BV (Netherlands). Diesel-electric autonomous tractor platform. Software co-developed with Nobleo Technology.
- **2025 metrics:**
  - Launched **AgBot T2 7-Series**: 230 hp diesel-electric, 8+ tonnes, tracked, на Agritechnica 2025 (Ноябрь 9-15, Hanover).
  - Starting price **€295 000 gross** — источник: <https://www.agxeed.com/agxeed-unveils-the-new-agbot-t2-7-series-230-hp-of-autonomous-power-forsmarter-soil-friendly-farming/>
  - Декабрь 2025 field trial: **80 ha за 20 часов** на 2 полях в Uckermark, северо-восточная Germany, в challenging terrain (hills, landscape elements).
  - Commercial deployment в NL, UK, DE, Czech Republic, и др.
- **Ограничения:**
  - Diesel-electric — не пользовательно для zero-emission climate targets; ESG-mark mixed.
  - Высокая цена входа; service network концентрирован в Western/Central Europe.
- **Sources:**
  - <https://www.agxeed.com/agxeed-unveils-the-new-agbot-t2-7-series-230-hp-of-autonomous-power-forsmarter-soil-friendly-farming/>
  - <https://www.futurefarming.com/smart-farming/agxeed-launches-new-agbot-t2/>
  - <https://soilessentials.com/agbot/>

### 2.6 Solinftec Solix

- **Vendor / scope:** Solinftec (HQ São Paulo, Brazil; US HQ West Lafayette, IN). Solar-powered autonomous scouting + sprayer robot. ALICE AI agronomic engine.
- **2025 metrics:**
  - **243% YoY US footprint expansion** — источник: <https://www.solinftec.com/en-us/blog/solinftec-expands-u-s-footprint-243-deploys-100-autonomous-robots-as-it-showcases-next-generation-solix-system-at-commodity-classic-2026/>
  - **>100 Solix robots deployed** в Indiana, Illinois, Kansas, Iowa, Wisconsin, Texas.
  - 2024 baseline: 50 robots monitored **>65M plants** в Indiana/Illinois.
  - North America COO: **~35M acres** monitored ALICE solutions.
  - Self-refilling sprayer для 24/7 autonomy — источник: <https://agfundernews.com/solinftecs-self-refilling-spray-robots-close-the-loop-on-247-autonomy-on-the-farm>
- **Ограничения:**
  - Solar-powered означает: low sun = downtime (winter wheat поля в высоких широтах — нерабочие зимой).
  - Scout-первоначально, sprayer — second-gen; ROI vs full-tractor sprayer для broadacre не доказана.
- **Sources:**
  - <https://www.solinftec.com/en-us/blog/solinftec-expands-u-s-footprint-243-deploys-100-autonomous-robots-as-it-showcases-next-generation-solix-system-at-commodity-classic-2026/>
  - <https://agfundernews.com/solinftecs-self-refilling-spray-robots-close-the-loop-on-247-autonomy-on-the-farm>
  - <https://www.globalagtechinitiative.com/in-field-technologies/robotics-automation/solinftec-to-showcase-solix-robotics-advancements-and-u-s-expansion-at-farm-progress-2025/>

### 2.7 CNH Industrial (Raven + Augmenta + ONE SMART SPRAY)

- **Vendor / scope:** CNH Industrial (бренды Case IH, New Holland Agriculture, Steyr). Raven Industries (acquired 2021 за $2.1B), Augmenta (Athens, Greece, acquired март 2023).
- **2025 metrics:**
  - Smart Sprayer system (camera-based, deep learning) deployed на **40 000-acre** US farming operation — first commercial fleet.
  - Augmenta camera unit: **138-foot field of view**, scaling от smallest booms до largest.
  - Integration с ONE SMART SPRAY (Bosch+BASF JV) commercial via Case IH + New Holland brands.
- **Ограничения:**
  - Несколько overlapping spray-AI offerings (Augmenta + ONE SMART SPRAY + Raven) — confusion для customers.
  - Smart Spray pricing + ROI claims тонут в маркетинге; independent validation 2025 limited.
- **Sources:**
  - <https://www.stocktitan.net/news/CNHI/cnh-s-latest-ai-sprayer-precision-tech-goes-beyond-the-uepmgonz82t2.html>
  - <https://media.cnh.com/north-america/cnh/cnh-industrial-adds-new-automation-and-autonomy-solutions--to-ag-tech-portfolio/s/3865e629-4df5-4d46-90eb-b7d79865c87c>
  - <https://www.precisionfarmingdealer.com/articles/5487-cnh-industrial-announces-collaboration-with-one-smart-spray>

### 2.8 EcoRobotix ARA

- **Vendor / scope:** Ecorobotix SA (Yverdon-les-Bains, Switzerland). Tractor-mounted ultra-high precision (UHP) sprayer; AI + camera identifies каждое растение, прицельный спрей в зону 6 × 6 cm.
- **2025 metrics:**
  - **1000 ARA sprayers sold** за последние 5 лет — источник: <https://press.ecorobotix.com/449695-ecorobotix-1-000-pulverisateurs-ara-ultra-haute-precision-vendus-et-utilises-par-des-agriculteurs-en-europe-et-dans-le-monde>
  - Agromačaj A.S. (one of largest EU onion producers, 12 000 ha): **3 ARA sprayers**, экономия от 200 л/га до 28.2 л/га = **~86% reduction** в первом году.
  - UK VCS: **до 96%** chemical savings на 1000 ha; Netherlands Doorgrond: **до 95%** на 15 000 ha.
  - Скорость: **4 га/час**.
- **Ограничения:**
  - Лучше всего для row-crop vegetables (sugar beet, onions, carrots); для broadacre cereals overkill.
  - Tractor-mounted, не autonomous — operator всё ещё нужен.
- **Sources:**
  - <https://ecorobotix.com/12000-hectares-3-ara-sprayers-1-vision-precision-farming-at-agromacaj-a-s/>
  - <https://ecorobotix.com/en-us/savings-phytosanitary-products/>
  - <https://press.ecorobotix.com/449695-ecorobotix-1-000-pulverisateurs-ara-ultra-haute-precision-vendus-et-utilises-par-des-agriculteurs-en-europe-et-dans-le-monde>

### 2.9 Greeneye Technology

- **Vendor / scope:** Greeneye Technology (Tel Aviv, Israel, основан 2017). Retrofit AI selective-spray kit на existing sprayers. Funding **$45M total** (с $20M Series 2024).
- **2025 metrics:**
  - Target: **200M acres** US broadacre — большая часть машин 2025 sea son уже distributed — источник: <https://agfundernews.com/israels-greeneye-technology-raises-20m-to-expand-precision-spray-tech-across-the-us>
  - Trials: **65-92%** herbicide reduction.
  - Cotton-farmer commercial sales для 2025 season.
- **Ограничения:**
  - Конкуренция с See & Spray (John Deere) на bigger machines; positioning — для non-Deere fleets.
  - Retrofit ROI зависит от existing sprayer condition; old sprayers — barrier.
- **Sources:**
  - <https://agfundernews.com/israels-greeneye-technology-raises-20m-to-expand-precision-spray-tech-across-the-us>
  - <https://greeneye.ag/press/>

### 2.10 Carbon Robotics LaserWeeder

- **Vendor / scope:** Carbon Robotics (Seattle, WA). LaserWeeder + Autonomous Tractor Kit (ATK). Использует CV + 30 high-power CO2 lasers для убийства weeds без химии. Funding $20M (Series 2025).
- **2025 metrics:**
  - **>150 машин** в **>100 фермерских хозяйствах** в **14 странах**.
  - **>250 000 acres** обработано, **>15 млрд weeds eliminated** — источник: <https://carbonrobotics.com/>
  - LaserWeeder G2 launched февраль 2025: modular от 6.6 до 60 feet boom; faster, lighter.
  - Sales roughly doubled YoY since debut.
  - Ноябрь 2025: targeting organic corn/soybean acres.
- **Ограничения:**
  - Стоимость капитальная: ~$1.2M на машину [VFY-day-of]. ROI чувствителен к organic premium.
  - Лазеры эффективны при small weeds (cotyledon-stage); поздние weeds — incomplete kill.
  - Глубокие или укрытые сорняки — недоступны.
- **Sources:**
  - <https://carbonrobotics.com/>
  - <https://www.businesswire.com/news/home/20250210556114/en/Carbon-Robotics-Introduces-Faster-Lighter-and-Modular-LaserWeeder-G2-Product-Line>
  - <https://www.geekwire.com/2025/carbon-robotics-raises-20m-as-laserweeder-maker-plans-secretive-new-ai-robot-for-farms/>
  - <https://www.realagriculture.com/2025/11/carbon-robotics-laser-weeder-targets-organic-corn-and-soybean-acres/>

### 2.11 Bonsai Robotics + farm-ng (Amiga platform)

- **Vendor / scope:** Bonsai Robotics (acquired farm-ng июль 2025). Amiga platform для specialty crops — orchards, vineyards, bedded crops. Funding ~$15M Series A.
- **2025 metrics:**
  - October 2025 FIRA USA: launched **Amiga Flex** (vision-based autonomy), Amiga Trax, Amiga Max — источник: <https://www.agtechnavigator.com/Article/2025/10/21/ag-robotics-company-releases-amiga-flex-following-acquisition/>
  - Commercial deployments в almond, citrus, pistachio в California + Australia (spray, disk, move, shake, sweep).
  - Integration с OMC + Flory Industries для orchard equipment.
- **Ограничения:**
  - Vision-first autonomy чувствителен к освещению (overcast, dust) — orchard floor может ломать perception.
- **Sources:**
  - <https://bonsairobotics.ai/>
  - <https://bonsairobotics.ai/bonsai-robotics-acquires-farm-ng-to-lead-the-future-of-autonomous-farming/>
  - <https://www.agtechnavigator.com/Article/2025/10/21/ag-robotics-company-releases-amiga-flex-following-acquisition/>
  - <https://agfundernews.com/with-a-fresh-15m-bonsai-robotics-stresses-the-need-for-an-ai-first-approach-to-on-farm-autonomy>

---

## 3. Livestock / dairy

### 3.1 Allflex / SenseHub (MSD Animal Health / Merck)

- **Vendor / scope:** Allflex Livestock Intelligence (часть MSD Animal Health после 2019 acquisition Antelliq у BC Partners за **$3.85B**). eSense Flex ear tags, cSense Flex neck tags, SenseHub Cloud platform.
- **2025 metrics:**
  - **2 млн коров mounted** на SenseHub (milestone 2025) — источник: <https://www.merck-animal-health-usa.com/newsroom/2-million-cows-monitored-with-sensehub/>
  - Reproductive, health, nutritional, wellbeing monitoring + SenseHub Cow Calf (beef breeding) + SenseHub Feedlot (backgrounding/stocker).
  - Partnership с Nestlé farms для wellbeing tracking.
- **Ограничения:**
  - Subscription + tag costs накапливаются (~$30/cow/year [VFY-day-of]) — для small dairies (<50 cows) — overkill.
  - Algorithms tuned для Holstein / dairy breeds; для местных пород калибровка слабая.
- **Sources:**
  - <https://www.merck-animal-health-usa.com/newsroom/2-million-cows-monitored-with-sensehub/>
  - <https://www.allflex.global/our-legacy/>
  - <https://cowsmo.com/news/antelliqs-allflex-partners-with-nestle-farms-to-monitor-dairy-cows-wellbeing/>

### 3.2 Connecterra IDA

- **Vendor / scope:** Connecterra B.V. (Amsterdam, NL). IDA ("Intelligent Dairy Assistant") — neck-collar sensor + AI behaviour analysis. Funding Series B €7.8M.
- **2025 metrics:**
  - Available в Canada, USA, Western Europe.
  - Customers: **Danone, Bayer, Kersia**, multiple thousand dairy subscribers (точное число 2025 не public).
- **Ограничения:**
  - Конкуренция жёсткая с Allflex / DeLaval / SmartBow / GEA.
  - Algorithm требует ~2 weeks baseline для каждой коровы; для часто-обновляемых стад biased outputs.
- **Sources:**
  - <https://www.connecterra.ai/>
  - <https://siliconcanals.com/dairy-tech-europe-ai-connected-cows-conterra/>
  - <https://cordis.europa.eu/project/id/812312>

### 3.3 Cainthus (Cargill partnership)

- **Vendor / scope:** Cainthus (Dublin, Ireland). Camera-based CV для dairy: monitors feeding, drinking, lying, social behaviour. Cargill exclusive partnership.
- **2025 metrics:**
  - Цель: optimize milk production + animal welfare через cloud-based computer vision.
  - Конкретные acreage / cow numbers 2025 — не public.
- **Ограничения:**
  - Computer vision требует чистых barns + good lighting; tie-stall barns с обилием silhouettes — challenging.
- **Sources:**
  - <https://www.digi.com/resources/customer-stories/cainthus-dairy-farm-ai-monitoring-technology>
  - <https://www.dairyherd.com/news/dairy-production/rise-ai-powered-smart-cameras-dairy-farming>

### 3.4 CattleEye (acquired by GEA 2024)

- **Vendor / scope:** CattleEye (Belfast, UK). Low-cost CCTV + cloud AI для **lameness detection** при выходе из milking parlour. **GEA Group AG (DE) acquired 2024**.
- **2025 metrics:**
  - **60 dairy farms, 11 000 cows** monitored (per Fortune June 2025) — источник: <https://fortune.com/2025/06/26/ai-farming-cows-cattleeye-health-environment/>
  - Trusted by farms managing **>250 000 cows worldwide** (через GEA channel).
- **Ограничения:**
  - Single-task (lameness); не full SenseHub-style multi-modal.
  - Camera placement требует physical install (entry/exit of parlour) — tie-stall barns не подходят.
- **Sources:**
  - <https://fortune.com/2025/06/26/ai-farming-cows-cattleeye-health-environment/>
  - <https://cattleeye.com/home/>
  - <https://agfundernews.com/cattleeye-comes-out-of-stealth-with-computer-vision-based-livestock-management-platform>

### 3.5 DeLaval VMS V300 / V310 (robotic milking)

- **Vendor / scope:** DeLaval (Tetra Laval). VMS — Voluntary Milking System. V300 (2018), V310 (2019, добавлен progesterone monitoring), VMS Batch Milking (2024).
- **2025 metrics:**
  - VMS V300 boasts **99.8% attachment rate**, **50% faster attachment** vs предыдущая модель, до **7500 lbs milk/day** на робот (70+ cows).
  - VMS V310: + individual cow fertility (progesterone).
  - **15% увеличение North American installations** за последний год — источник: <https://www.thebullvine.com/news/robotic-milking-revolution-15-surge-in-delaval-systems-as-labor-crisis-deepens/>
  - VMS Batch Milking: **20 ферм в 13 странах**; expected double каждый год.
  - Flow-Responsive Milking standard на новых V300 с июня 2025.
- **Ограничения:**
  - Capital cost ~**$200K на robot box** [VFY-day-of]; ROI чувствителен к labour cost.
  - Robotic milking требует free-stall design + cow training; tie-stall barns переоборудовать дорого.
  - Когда cow injury / отказ от robot box → ручная intervention.
- **Sources:**
  - <https://corporate.delaval.com/2025/02/vms-batch-milking-is-reshaping-dairy-operations-worldwide/>
  - <https://corporate.delaval.com/2025/04/delaval-unveils-faster-smarter-bigger-milking-robot-model/>
  - <https://www.thebullvine.com/news/robotic-milking-revolution-15-surge-in-delaval-systems-as-labor-crisis-deepens/>

### 3.6 Cargill Birdoo

- **Vendor / scope:** Cargill + Knex (digital technology enablement). CV + AI для broiler weight estimation без человеческой калибровки. **Cargill — exclusive provider для Americas**.
- **2025 metrics:**
  - **>95% accuracy** на weight estimation, без labour для clean/calibrate.
  - Improves feed conversion ratio; saves **10-30g feed на bird**, reduces variability + downgrades.
  - Real-time tracking via cloud platform.
- **Ограничения:**
  - Только Americas (Cargill exclusive distribution).
  - Camera install требует properly-built broiler houses; old open-side houses — challenging.
  - Конкретные 2025 deployment numbers не public.
- **Sources:**
  - <https://www.feedandadditive.com/cargill-supports-poultry-producers-with-artificial-intelligence/>
  - <https://www.cargill.com/2022/cargill-expands-portfolio-innovations-for-poultry-producers>
  - <https://www.cargill.com/story/artificial-intelligence-in-animal-farming>

---

## 4. Robotics — harvesting / sorting

### 4.1 Octinion Rubion (strawberry picker)

- **Vendor / scope:** Octinion (Leuven, Belgium; now part of «Picking Technology»). Autonomous strawberry-picking robot для tabletop strawberry cultivation. Photonic sensor + RGB camera для ripeness detection.
- **2025 metrics:**
  - Picks **70% всех ripe strawberries** damage-free.
  - Cycle: **strawberry каждые 5 секунд**.
  - Capacity: **180-360 kg/day** на robot.
- **Ограничения:**
  - Tabletop-only — для field strawberry не работает.
  - 70% pick rate означает 30% ягод остаются for manual second-pass.
  - 2025 commercial scale-deployment не публично заявлен (small/pilot).
- **Sources:**
  - <http://octinion.com/products/agricultural-robotics/rubion>
  - <https://www.hortidaily.com/article/9071455/the-robot-currently-picks-a-strawberry-every-five-seconds/>
  - <http://octinion.com/news/press-release-octinion-presents-world%E2%80%99s-first-strawberry-picking-robot>

### 4.2 Tortuga AgTech (acquired by Oishii March 2025)

- **Vendor / scope:** Tortuga AgTech (Denver). Dual-arm AI-driven F (strawberry) + G (table grape) models. **Acquired by Oishii март 2025** (IP, assets, engineering team).
- **2025 metrics:**
  - **50 robots** в Oishii vertical farms.
  - Цель: surpass human picker — **98% accuracy 24/7, 365** к концу 2025.
  - **50% reduction in harvest expenses** vs human labour.
  - TIME Best Inventions 2025 Special Mention.
- **Ограничения:**
  - Acquisition означает: продукт уходит из open market к Oishii-only deployment.
  - Field-strawberry (Driscoll's-style outdoor) — НЕ цель Tortuga; только controlled environment.
- **Sources:**
  - <https://www.futurefarming.com/tech-in-focus/field-robots/oishii-acquires-tortuga-agtech-to-scale-robotic-strawberry-harvesting/>
  - <https://time.com/collections/best-inventions-special-mentions/7320803/tortuga-agtech-f-and-g-models/>
  - <https://agfundernews.com/oishii-acquires-tortuga-agtechs-ip-assets-and-engineering-team-to-supercharge-its-vertical-farms>

### 4.3 Tevel Aerobotics (Flying Autonomous Robots)

- **Vendor / scope:** Tevel Aerobotics Technologies (Israel). Flying Autonomous Robots (FAR) — tethered quadcopter drones, 4 per wheeled base vehicle (FAR-Wheeled). Picks apples, peaches, nectarines, pears, plums, citrus, avocado.
- **2025 metrics:**
  - Fruit weight range: **50g (apricot) до 700g (apple)**.
  - Trials в Washington state orchards (US apples).
  - Demonstrated at Interpoma (Italy) и Yakima (WA).
- **Ограничения:**
  - Tethered drones — limited reach radius.
  - Throughput per FAR-Wheeled ниже traditional crew для commodity apples.
  - Heavy fruit (apples ~250g+) — wear на drones.
- **Sources:**
  - <https://www.tevel-tech.com/>
  - <https://www.futurefarming.com/tech-in-focus/fruit-picking-drones-by-tevel-aerobotics-technologies/>
  - <https://www.goodfruit.com/flying-harvest-robot-demo-drew-a-crowd-at-interpoma-video/>

### 4.4 Saga Robotics Thorvald (UV-C mildew control)

- **Vendor / scope:** Saga Robotics (Oslo, Norway / UK / California). Thorvald — modular autonomous platform с UV-C light для disrupting fungal DNA (powdery mildew control без химии). Funding ~$11.2M + €9.5M expansions.
- **2025 metrics:**
  - **150+ robots** оперировали с **97% uptime**, **>200 000 autonomous km** (3x previous season).
  - UK: deployed в **20% tabletop strawberry sector** (sector-wide market share); 13 leading growers.
  - California: **>1300 acres of vineyards**.
  - Castoro Cellars (Paso Robles): UV-C bots across **600 organic acres**.
- **Ограничения:**
  - UV-C только для powdery mildew; downy mildew / Botrytis — другие методы.
  - Night-only operations (UV-C harmful, need dark).
  - Тяжёлый robot для steep vineyards — нужен новый vineyard model.
- **Sources:**
  - <https://www.agtechnavigator.com/Article/2025/10/29/saga-robotics-logs-record-season-across-us-and-uk-farms/>
  - <https://www.fruitnet.com/fresh-produce-journal/saga-robotics-continues-to-expand-after-successful-season-of-mildew-control/263695.article>
  - <https://agfundernews.com/castoro-cellars-deploys-saga-robotics-uv-c-bots-across-600-organic-acres>

### 4.5 FFRobotics (apple picker)

- **Vendor / scope:** FFRobotics (Israel, founded 2014). Multi-arm (12 robotic arms, 6 per side) tractor-mounted apple harvester. Service model (not unit sale).
- **2025 metrics:**
  - **22 000th robotic arm** deployed в commercial orchards (April 2024).
  - Trial farm в Washington (Stemilt Growers) — Fuji / WA 38 / Gala 2022, expanded since.
- **Ограничения:**
  - Apple-specific (some adaptation для citrus).
  - Service model → no farmer-ownership; vendor risk если company сворачивается.
  - Throughput improvement vs human crew не has converged к economically dominant; CES 2026 next-gen targets 80% pick rate — источник: <https://www.freshfruitportal.com/news/2026/01/23/next-gen-apple-robot/>
- **Sources:**
  - <https://www.ffrobotics.com/>
  - <https://www.thepacker.com/news/packer-tech/robot-apple-picker-close-commercialization>
  - <https://goodfruit.com/lots-of-bots-video/>
  - <https://www.freshfruitportal.com/news/2026/01/23/next-gen-apple-robot/>

---

## 5. Indoor / vertical farming (выжившие + проигравшие)

### 5.1 Oishii (premium vertical strawberry)

- **Vendor / scope:** Oishii (Jersey City, NJ; founded 2017). Premium Koyo + Omakase strawberries. Vertical Smart Farm + robotics + AI. Funding: **$150M Series C (May 2026)**.
- **2025 metrics:**
  - Acquired Tortuga AgTech (March 2025) — 50 robots в smart farms.
  - MISUMI Group partnership для automation deployment в US + Japan.
  - **60+ млрд data points/year** capture для environmental optimization — источник: <https://www.agtechnavigator.com/Article/2026/05/14/oishii-secures-150m-series-c-as-premium-strategy-sets-it-apart-from-vertical-farming-failures/>
  - Premium pricing strategy ($20 за 8 strawberries в Whole Foods) — disertinguish от commodity vertical farm failures.
- **Ограничения:**
  - Только premium-niche, не commodity volume; growth ceiling lower.
  - CapEx massive — Tokyo-trained robotics + Japanese cultivars license.
- **Sources:**
  - <https://www.agtechnavigator.com/Article/2026/05/14/oishii-secures-150m-series-c-as-premium-strategy-sets-it-apart-from-vertical-farming-failures/>
  - <https://www.prnewswire.com/news-releases/oishii-announces-first-closing-of-150m-in-series-c-financing-as-it-scales-its-indoor-smart-farm-model-302770199.html>
  - <https://www.therobotreport.com/oishii-raises-150m-robotic-vertical-farming-system/>

### 5.2 80 Acres Farms (Soli Organic merger 2025)

- **Vendor / scope:** 80 Acres Farms (Cincinnati, OH). Infinite Acres GroLoop platform (engineering + biology + tech). **Merged with Soli Organic август 2025** = one of largest indoor farming networks. AWS + International Research Centre on AI partnership.
- **2025 metrics:**
  - Projected first-year revenue **~$200M**.
  - **7 nationally distributed vertical farms**, **15-20 млн lbs annual produce**.
  - AWS + IRCAI partnership: AI models forecast crop performance in CEA.
  - Siemens R&D leveraging ML для irregularity detection.
- **Ограничения:**
  - Все indoor farms требует high power costs; survival зависит от cheap electricity (US Midwest).
  - Сравнительные unit economics vs greenhouses — questionable; pivot к leafy greens (lower CapEx ROI).
- **Sources:**
  - <https://www.80acresfarms.com/2025/08/18/indoor-farming-leaders-unite-to-build-a-national-powerhouse/>
  - <https://www.siemens.com/us/en/company/sustainability/80-acres-vertical-farming.html>
  - <https://triplepundit.com/2025/vertical-farming-new-ventures/>

### 5.3 Plenty (Chapter 11, vышел 2025)

- **Vendor / scope:** Plenty Unlimited (South San Francisco). Backed by Jeff Bezos / SoftBank / Eric Schmidt. **Filed Chapter 11 24 марта 2025; emerged 29 мая 2025**, operates Richmond, VA strawberry farm.
- **2025 metrics:**
  - Raised **>$900M** до bankruptcy.
  - Post-bankruptcy: focused only on Richmond VA strawberry farm (partnership с Driscoll's).
- **Ограничения:**
  - Failure caused by: high opex, stalled projects (Compton, Wyoming), investor cooling — источник: <https://techcrunch.com/2025/03/24/vertical-farming-company-plenty-files-for-bankruptcy-after-raising-nearly-1b/>
  - AI/ML capabilities не спасли unit economics commodity leafy-greens (overestimated demand premium).
- **Sources:**
  - <https://techcrunch.com/2025/03/24/vertical-farming-company-plenty-files-for-bankruptcy-after-raising-nearly-1b/>
  - <https://startupwired.com/2025/03/25/plenty-files-for-bankruptcy-amid-capital-crunch/>
  - <https://www.igrowmarketplace.com/post/lessons-learned-overview-plenty-s-bankruptcy-and-implications-for-vertical-farming>

### 5.4 Bowery Farming (collapse Nov 2024)

- **Vendor / scope:** Bowery Farming (New York). FarmOS AI platform для CEA. **Ceased operations November 2024** после raising **>$700M** + $2B valuation peak 2021.
- **2025 metrics (post-collapse):**
  - **$70M Georgia farm** sent to liquidation Nov 2025.
  - Nationwide sell-offs of assets.
- **Ограничения / failure modes:**
  - Plant disease pressure (yield disruptions).
  - Weak demand для premium-priced leafy greens.
  - Burn rate за scale: bigger growing rooms не нашли соответствия unit economics.
- **Sources:**
  - <https://www.fertilizerdaily.com/20251114-bowery-farmings-70m-georgia-vertical-farm-heads-to-liquidation-as-startups-collapse-triggers-nationwide-sell-offs/>
  - <https://agroreview.com/en/newsen/crops/bankruptcy-green-producers-predictions-for/>
  - <https://foodlore.blog/why-vertical-farms-go-bankrupt/>

### 5.5 Infarm → InFarm Technologies Limited

- **Vendor / scope:** Infarm (Berlin). Modular in-store growing units (originally in supermarkets — Edeka, Marks & Spencer). **Declared insolvency 2023**, resumed как InFarm Technologies Limited (UK-based).
- **2025 metrics:**
  - Cut staff, exited multiple markets; survive в select EU locations с favourable produce-price economics.
- **Ограничения:**
  - In-store модель не работает unit-wise (cost per gram > supermarket alternative).
- **Sources:**
  - <https://foodlore.blog/why-vertical-farms-go-bankrupt/>
  - <https://agroreview.com/en/newsen/crops/bankruptcy-green-producers-predictions-for/>

### 5.6 Kalera (Chapter 11 + Lactuca Holdings)

- **Vendor / scope:** Kalera (Orlando, FL). **Filed Chapter 11 April 4, 2023**; assets acquired Lactuca Holdings (Sandton Capital). Continues operating в Atlanta, Denver, Houston facilities.
- **2025 metrics:**
  - Nasdaq delisted.
  - Brand survives but radically downsized.
- **Sources:**
  - <https://www.thepacker.com/news/packer-tech/vertical-farmer-kalera-files-chapter-11-bankruptcy>
  - <https://igrownews.com/kalera-latest-news/>

### 5.7 AppHarvest (Chapter 11 2023, dissolved)

- **Vendor / scope:** AppHarvest (Morehead, KY). Greenhouse-based, NOT vertical (часто групируется с CEA collapse). **Chapter 11 July 23, 2023**; lost >$166M в 2021 alone. All 4 KY facilities (Morehead, Richmond, Somerset, Berea) sold orderly.
- **Sources:**
  - <https://www.agriculturedive.com/news/appharvest-bankruptcy-indoor-farming-martha-stewart-jd-vance/689039/>
  - <https://www.producebluebook.com/2023/07/24/appharvest-files-chapter-11-bankruptcy/>

### 5.8 Iron Ox (ceased June 2024)

- **Vendor / scope:** Iron Ox (Bay Area). Robotic greenhouse pivot. **Ceased operations June 30, 2024**. Spin-off успешник продолжает с LaserWeeder + ATK через Carbon Robotics-style implements (separately).
- **Sources:**
  - <https://forgeglobal.com/iron-ox_stock/>
  - <https://www.cbinsights.com/company/iron-ox>

### 5.9 14 vertical farms bankruptcy 2025

- В 2025 году **14 indoor / CEA companies filed bankruptcy** с combined **historical funding >$1.37 млрд** — источник: <https://foodlore.blog/why-vertical-farms-go-bankrupt/>

---

## 6. Supply chain & retail (agentic AI, demand forecasting, blockchain)

### 6.1 Cargill (CMAX + CarVe + 2026 BIG AI Award)

- **Vendor / scope:** Cargill Inc. >150 stran, 1000+ facilities, 70 стран.
- **2025 metrics:**
  - **CMAX**: predictive port + shipping logistics; optimizes grain flows.
  - **CarVe**: computer vision для protein supply chain yield, waste reduction.
  - **Brazil grain logistics**: AI-driven grain mixing в country elevators.
  - Won **2026 BIG AI Excellence Award** (января 2026) — источник: <https://www.cargill.com/2026/cargill-wins-2026-big-artificial-intelligence-excellence-award>
- **Ограничения:**
  - Most "AI" deployment остаётся в supply-chain optimization, не fully agentic end-to-end yet.
  - Кэгилл — non-public; metrics в большинстве случаев self-reported.
- **Sources:**
  - <https://www.cargill.com/story/reinventing-operations-resilient-food-system>
  - <https://www.cargill.com/2026/cargill-wins-2026-big-artificial-intelligence-excellence-award>
  - <https://www.cargill.com/about/artificial-intelligence>

### 6.2 Olam Agri (Mindsprint / Procuresprint / Tradesprint)

- **Vendor / scope:** Olam Group (Singapore). Major divestments + capital raises 2025; Saudi-state announced **80% stake purchase** Olam Agri early 2025.
- **2025 metrics:**
  - **Mindsprint** (Wipro deployment 2026 — one of largest strategic transformation engagements): Farmsprint® (plantation management), **Procuresprint®** (agentic AI procurement), Tradesprint® (commodity trading + risk).
- **Ограничения:**
  - Mindsprint products — relatively new; benchmarks vs Cargill / Bunge не public.
- **Sources:**
  - <https://www.wipro.com/newsroom/press-releases/2026/wipro-wins-one-of-its-largest-strategic-transformation-engagements-from-food-and-agri-business-leader-olam-group/>
  - <https://www.cbinsights.com/company/olam-agri>

### 6.3 Bunge (blockchain soy + AI)

- **Vendor / scope:** Bunge Global (HQ St. Louis, switched HQ Geneva to Chesterfield 2024). 2025 — merger с Viterra completed July 2025.
- **2025 metrics:**
  - **Bunge + Bangkok Produce Merchandising blockchain partnership** — deforestation-free soy traceability для Charoen Pokphand Foods (Thailand + SE Asia).
- **Ограничения:**
  - Blockchain ≠ AI; integration AI-side всё ещё в pilot phase.
- **Sources:**
  - <https://bunge.com/Press-Releases/Bunge-and-Bangkok-Produce-Merchandising-Expand-Partnership-for-Blockchain-Traced>

### 6.4 Walmart × Cropin (fresh produce supply chain)

- **Vendor / scope:** Walmart Inc. partnership с Cropin AI.
- **2025 metrics:**
  - **20% food waste reduction** в Walmart global ops (2020 baseline).
  - Eden ML algorithm (in-house, 2017) — produce quality scanning.
  - Cropin partnership: yield forecasting, crop health monitoring, seasonal transition prediction для fresh produce.
- **Ограничения:**
  - Cropin coverage outside US (PepsiCo India deployment) — different SLA для Walmart US.
- **Sources:**
  - <https://www.grocerydive.com/news/walmart-adds-partner-produce-crop-monitoring-artificial-intelligence/743919/>
  - <https://d3.harvard.edu/platform-digit/submission/walmart-using-machine-learning-to-reduce-food-waste/>

### 6.5 Tesco (AI demand forecasting)

- **Vendor / scope:** Tesco PLC (UK). AI demand forecasting для produce + bakery; expiring items markdown / donation.
- **2025 metrics:**
  - **30% reduction in food waste** since 2017 baseline.
  - **30% of all food wastage** comes from produce (target category).
- **Ограничения:**
  - UK-focused; not deployed в Asia / Tesco-licensed markets.
- **Sources:**
  - <https://www.ordergrid.com/case-studies/from-stockouts-to-success-a-grocery-chain-cuts-waste-and-grows-sales-with-ai>

### 6.6 Cropin Cloud (India + global)

- **Vendor / scope:** Cropin Technology (Bangalore, India, founded 2010). Cropin Cloud + Sage GenAI agri-intelligence platform.
- **2025 metrics:**
  - **>30 млн acres** digitized globally; **>7 млн farmers** impacted.
  - India: **35 000 ha** через 10 000+ farmer partners (170 villages) для Indian conglomerate (spices) — case study.
  - PepsiCo India partnership.
  - Walmart partnership (см. 6.4).
- **Ограничения:**
  - GenAI продукт «Sage» — новый, limited 2025 deployment data.
  - Cropin scaled через enterprise sales, не direct-to-farmer; smallholder reach indirect.
- **Sources:**
  - <https://www.cropin.com/>
  - <https://agrospectrumindia.com/2024/07/17/cropin-launches-first-real-time-gen-ai-powered-agri-intelligence-platform-sage.html>
  - <https://www.agtechnavigator.com/Article/2024/07/17/India-s-Cropin-Technology-says-GenAI-can-predict-the-future-of-crop-yields/>

### 6.7 AgriDigital (blockchain grain Australia)

- **Vendor / scope:** AgriDigital (Sydney, AU, founded 2015). Blockchain + grain management platform.
- **2025 metrics:**
  - Australia: leading grain management software.
  - Zambia + Zimbabwe deployment: **payment delays for smallholders reduced from 90 to 2 days**.
- **Ограничения:**
  - Blockchain hype часто overhyped; underlying value — payment automation, not crypto.
- **Sources:**
  - <https://www.agridigital.io/>
  - <https://qaltivate.com/blog/blockchain-technology-in-agriculture/>

### 6.8 Aclima (mobile air monitoring, ag-adjacent)

- **Vendor / scope:** Aclima Inc. (San Francisco). Sensor-equipped vehicles + Google Cloud + ML для block-level air quality (включая ag-pollution proxies, methane, ammonia).
- **2025 metrics:**
  - **California SMMI (June 2025)**: 64 communities, **950 000 miles**, **5.2 млн residents**, **50-100x more data per dollar** — источник: <https://www.gov.ca.gov/2025/06/03/in-first-of-its-kind-initiative-california-deploys-mobile-air-monitoring-to-protect-underserved-communities-from-pollution/>
  - $27M funded via Calif Climate Investments (Cap-and-Trade).
- **Ограничения:**
  - Air quality, не farm productivity tool; ag-relevant indirectly (downwind pesticide drift, methane livestock).
- **Sources:**
  - <https://aclima.earth/>
  - <https://www.prnewswire.com/news-releases/aclimas-sensor-equipped-vehicles-hit-the-road-for-block-by-block-air-pollution-mapping-in-64-underserved-california-communities-302494812.html>

---

## 7. Plant disease / pest / agronomy decision support

### 7.1 Plantix (PEAT GmbH → Helm AG)

- **Vendor / scope:** Plantix (Berlin, founded 2015 by Rob + Simone Strey as PEAT GmbH). **PEAT acquired Salesbee April 2020**; **sold to Helm AG 2023**.
- **2025 metrics:**
  - **>10 млн downloads global**, 19 languages.
  - **>7 млн users в India** (1M monthly active).
  - **800 symptoms** across **60 crop types**.
  - **>120 млн images** в дата-базе.
  - **~20 000 images uploaded daily**.
  - **>90% accuracy** vs **60-70% human expert** baseline (per Rob Strey).
- **Ограничения:**
  - Recommendations часто включают pesticide products — критики говорят про over-prescription.
  - Hardest crops + new pests — biased recall.
- **Sources:**
  - <https://plantix.net/en/>
  - <https://en.wikipedia.org/wiki/Plantix>
  - <https://plantix.net/en/blog/plantix-networked-india/>
  - <https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/blog/detecting-and-managing-crop-pests-and-diseases-with-ai-insights-from-plantix/>

### 7.2 Pl@ntNet (CIRAD / INRA / INRIA citizen science)

- **Vendor / scope:** Pl@ntNet (CIRAD + INRA + INRIA + IRD France). Citizen-science plant identification.
- **2025 metrics:**
  - **>70 000 species** identifiable (world flora).
  - **>1 млрд photographs** processed.
  - **Несколько миллионов users** в **>200 странах**.
  - 23 languages, 2025 identification model release + offline genus/family explorer.
- **Ограничения:**
  - Not specialized для crop disease (general plant ID).
  - Лучше всего для wild species; cultivated crops + diseases — гораздо ниже точность.
- **Sources:**
  - <https://plantnet.org/en/>
  - <https://en.wikipedia.org/wiki/Pl@ntNet>
  - <https://identify.plantnet.org/>

### 7.3 Climate Corporation (Bayer-owned)

- **Vendor / scope:** The Climate Corporation. Founded 2006 SF; Monsanto acquired 2013 за $1.1B; Bayer acquired Monsanto 2018 → теперь Bayer Crop Science Digital.
- **2025 metrics:**
  - Climate Basic mobile app maps soil + weather к **10m × 10m resolution** для **30 млн agriculture fields в America**.
  - Hyper-local weather forecast + agronomic recommendations.
  - Core technology теперь под FieldView umbrella.
- **Ограничения:**
  - Coverage extremely US-centric; international expansion через FieldView slower.
- **Sources:**
  - <https://en.wikipedia.org/wiki/The_Climate_Corporation>
  - <https://www.agri-pulse.com/articles/3287-monsanto-acquires-weather-data-company-climate-corporation>
  - <https://spectrum.ieee.org/monsanto-brings-big-data-to-the-farm>

### 7.4 Indigo Ag (GeoInnovation yield prediction + Carbon)

- **Vendor / scope:** Indigo Ag (Boston, MA). GeoInnovation satellite + ML acquired (2020s). Microbial seed treatments + Carbon by Indigo program.
- **2025 metrics:**
  - Indigo yield prediction historically **outperformed USDA** (2017 record corn forecast example).
  - **Microsoft 12-year agreement: 2.85M Carbon by Indigo credits** + prior 40K (2024) + 60K (2025) tonne purchases.
  - November 2024: **GROWMARK partnership** для FS cooperatives access.
- **Ограничения:**
  - Carbon credits market volatility; Indigo's carbon protocol critized для additionality + permanence.
  - Microbial seed treatments — incremental yield gains, not transformative.
- **Sources:**
  - <https://www.indigoag.com/pages/news>
  - <https://www.indigoag.com/pages/news/indigo-shares-january-corn-and-soy-yield-forecasts-for-americas-to-help-farmers-during-government-shutdown>

### 7.5 Lindsay FieldNET + CropX (irrigation AI)

- **Vendor / scope:** Lindsay Corporation (FieldNET) + Reinke-CropX integration. FieldNET — variable-rate irrigation + satellite crop health, CropX — soil sensor + IoT VWC + ML scheduling.
- **2025 metrics:**
  - FieldNET expanded к **1.2 млн hectares** satellite-based crop health coverage.
  - CropX charges **~$10/ha/year** для scheduling algorithms.
  - Reinke-CropX 2024 partnership: **18% average water usage reduction**; variable rates каждые 10 meters.
- **Ограничения:**
  - Irrigation-only — не full agronomic platform.
  - Sensor install требует upfront CapEx ($300-500/ha [VFY-day-of]).
- **Sources:**
  - <https://www.lindsay.com/apac/en/irrigation/fieldnet>
  - <https://link.springer.com/chapter/10.1007/978-3-032-02138-0_27>
  - <https://www.dtnpf.com/agriculture/web/ag/crops/article/2022/03/03/irrigation-technology-evolves-beyond>

### 7.6 Trace Genomics → Miraterra (soil microbiome AI)

- **Vendor / scope:** Trace Genomics (Bay Area, founded 2015). DNA-sequencing-based soil microbiome analysis + ML pathogen detection. **Acquired by Miraterra July 7 2025**.
- **2025 metrics:**
  - **70 crops + 225+ pathogens** в platform.
  - Combined Trace DNA + Miraterra Raman spectroscopy → biological + chemical + structural soil dimensions.
  - Miraterra raised **$16M** дополнительно — источник: <https://igrownews.com/miraterra-latest-news/>
- **Ограничения:**
  - DNA-based testing — high CapEx per sample ($75-150 [VFY-day-of]); not field-side instant.
  - Microbiome → yield correlation остаётся active research; recommendations probabilistic.
- **Sources:**
  - <https://www.prnewswire.com/news-releases/miraterra-acquires-trace-genomics-technology-and-products-to-unlock-measurement-and-insights-across-soil-plants-and-food-302498364.html>
  - <https://www.agtechnavigator.com/Article/2025/07/09/soil-measurement-company-miraterra-bolts-on-trace-genomics/>
  - <https://www.miraterrasoil.com/trace>

---

## Summary

- **Categories covered:** 7 (precision farming, autonomous machinery, livestock, harvesting robotics, indoor/vertical, supply chain, plant disease).
- **Total named cases:** 37 (см. table-of-contents выше).
- **Geographic spread:** US (15+), EU (10+), Israel (4), Brazil (2), India (2), Australia (2), Norway/UK/CH каждой 1+, Japan/Singapore 1+.

Этот файл — applications-only; failures (Section 5 — bankruptcies — кратко включены ради контекста, но deeper-dive остаётся в 02-failures.md), trends (03), Russia (04) — в других файлах.
