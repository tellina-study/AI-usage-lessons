# Lec-17 case images — acquisition manifest (Phase 8c-img)

Real case images добыты через 6-tier acquisition (см. `tools/presentation-build/README.md` §5.7).
**НЕ mock, НЕ stylized card.** Educational fair use. Каждое изображение визуально проверено или подтверждено source-identifiable.

| slug | file | tier | source | license |
|---|---|---|---|---|
| zillow | zillow.jpg | Tier2 Commons | Russell Investments Center, Seattle — штаб-квартира Zillow | CC BY-SA |
| crowdstrike | crowdstrike.jpg | Tier2 Commons | BSOD на табло LaGuardia Airport (инцидент CrowdStrike 19.07.2024) | CC BY-SA 4.0 |
| waymo | waymo.jpg | Tier2 Commons | Waymo robotaxis, San Francisco (Dllu) | CC BY-SA 3.0 |
| see-and-spray | see-and-spray.jpg | Tier2 Commons | John Deere tractor and sprayer (Bill Kasman) | CC BY 2.0 |
| aidoc | aidoc.jpg | Tier2 Commons | Brain CT Scan for Stroke Diagnosis (кейс Aidoc радиология) | CC BY 4.0 |
| galactica | galactica.png | Tier5 Wayback | galactica.org snapshot 2022-11-18 — реальный интерфейс демо Meta | © Meta, fair use (archived) |
| arup-deepfake | arup-deepfake.jpg | Tier2 Commons | Многоэкранная видеоконференция, DoD (концепт; кейс Arup $25M deepfake) | CC BY 2.0 |
| tesla-2018 | tesla-2018.png | Tier2 Commons | Giga Press IDRA, Tesla Fremont — производственная линия | CC BY 3.0 |
| monarch | monarch.jpg | Tier3 Newsroom | monarchtractor.com — MK-V автономный электротрактор (blueberry demo) | © Monarch, fair use |
| plenty | plenty.jpg | Tier2 Commons | iFarm вертикальная ферма Finland (отрасль; кейс Plenty) | CC BY-SA 4.0 |
| cruise | cruise.jpg | Tier2 Commons | Autonomous car, Point Lobos Ave, San Francisco 2022 (Rabich) | CC BY-SA 4.0 |
| devin | devin.jpg | Tier3 Newsroom | cognition.ai opengraph — анонс Devin | © Cognition, fair use |
| ibm-watson | ibm-watson.jpg | Tier2 Commons | IBM Watson (система Jeopardy; кейс Watson for Oncology) | CC BY 3.0 |
| epic-sepsis | epic-sepsis.jpg | Tier2 Commons | Система мониторинга пациентов ICU, US Navy (кейс Epic Sepsis Model) | Public domain (US Navy) |
| klarna | klarna.jpg | Tier2 Commons | Стенд Klarna, Internet World Fair 2017 | CC0 |
| stripe-radar | stripe-radar.png | Tier3 Newsroom | stripe.com/radar — официальная страница (fraud detection) | © Stripe, fair use |
| github-copilot | github-copilot.png | Tier3 Newsroom | github.com/features/copilot — официальная страница | © GitHub, fair use |
| symbotic | symbotic.jpg | Tier2 Commons | Amazon fulfilment robot 2020 (отрасль складской робототехники) | CC BY-SA 4.0 |
| alphafold | alphafold.png | Tier2 Commons | AlphaFold prediction структуры белка (C4orf47) | CC BY-SA 4.0 |
| uber-tempe | uber-tempe.jpg | Tier2 Commons | Uber self-driving Volvo XC90 (Dllu) — модель из аварии Tempe 2018 | CC BY-SA 2.0 |
| f35-alis | f35-alis.jpg | Tier2 Commons | F-35A hot-pit refueling, USAF — наземное обслуживание (кейс ALIS/ODIN) | Public domain (USAF) |
| boeing-max9 | boeing-max9.jpg | Tier2 Commons | NTSB: door plug рейса Alaska 1282, 737 MAX 9 (05.01.2024) | Public domain (NTSB) |
| air-canada | air-canada.jpg | Tier2 Commons | Air Canada Boeing 777-333ER (кейс чат-бота Moffatt v. Air Canada 2024) | CC BY-SA 3.0 |
| getty-stability | getty-stability.jpg | Tier2 Commons | Stable Diffusion-генерация с искажённым Getty-watermark (кейс Getty v. Stability) | Public domain (AI-gen) |
| ups-orion | ups-orion.jpg | Tier2 Commons | Грузовик UPS, USDA (кейс ORION оптимизация маршрутов) | Public domain (USDA) |
| yokogawa-eneos | yokogawa-eneos.jpg | Tier2 Commons | Диспетчерская промышленного предприятия (кейс Yokogawa CENTUM / ENEOS) | CC BY 2.5 |

## Сводка

- **Добыто real images: 26 / 26** (target был 20-25 — превышен).
- **Failed 6/6 (mock-only): 0.** Mock НЕ создавался ни для одного кейса.
- **Tier breakdown:** Tier2 Commons = 21, Tier3 newsroom og:image = 4 (monarch, devin, stripe-radar, github-copilot), Tier5 Wayback = 1 (galactica).
- **Все ≥800px по широкой стороне** (мин: galactica 873px). Крупные файлы (f35, ups, ibm-watson) downscaled до ≤1600px.
- **Total folder size:** ~9.7 MB.

## Notes / substitutions (industry-proxy, честно помечены в caption)

Несколько кейсов не имеют свободного фото самого продукта/компании — использован релевантный отраслевой/концептуальный real-image (НЕ mock), с явной пометкой в attribution:
- **zillow** — штаб-квартира Zillow (Russell Investments Center), а не Zillow Offers houses (нет свободного фото iBuying-домов).
- **plenty** — вертикальная ферма iFarm как отрасль-прокси (нет свободного фото фермы Plenty).
- **symbotic** — Amazon fulfilment robot как прокси складской робототехники (нет свободного фото Symbotic).
- **arup-deepfake** — многоэкранная видеоконференция как концепт (deepfake-кадр самого инцидента не публичен).
- **epic-sepsis** — система мониторинга ICU (US Navy) как прокси клинической инфосистемы.
- **yokogawa-eneos** — диспетчерская промпредприятия как прокси DCS-контроля.
- **ibm-watson** — фото системы Watson (Jeopardy-эпоха); кейс лекции — Watson for Oncology.
- **getty-stability** — реальная Stable Diffusion-генерация с искажённым Getty-watermark (центральная улика иска).

Per-image source URL + tier + attribution + license — в соответствующих `<slug>.url` файлах.
