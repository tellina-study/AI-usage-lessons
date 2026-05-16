# Reflection — Content (сессия #78/#82, 2026-05-15/16)

## Главное содержательное наследие

1. **Reusable research-таблицы документированных провалов ИИ по темам лекций.**
   Аудит сгенерировал проверенные (WebSearch) кейсы с источниками/датами:
   - `notes/reviews/2026-05-15-failure-content-audit/lec-01.md` — Air Canada chatbot 2024, Amazon hiring 2018, Zillow Offers 2021, Mata v. Avianca 2023, IBM Watson Oncology, Gemini images 2024, Tay 2016, McDonald's×IBM 2024 + 3 «когда ИИ не нужен».
   - `lec-02.md` — reversal curse (Berglund 2309.12288), lost-in-the-middle (Liu 2307.03172), sycophancy (Sharma 2310.13548), legal hallucinations (Dahl 2401.01301), prompt injection (Greshake 2302.12173), tokenization/counting (2412.18626, 2410.19730).
   - `lec-04.md` — Epic Sepsis Model (external AUC 0.63 vs vendor 0.76–0.83, 67% пропущено), Roberts COVID-232 (Nature MI 2021), Google Thailand DR field-study 2020, IBM Watson Oncology, FDA recalls, Obermeyer bias.
   → **Это seed-материал** для failure-контента будущих лекций. При production L3/L5–L17 — сначала смотреть сюда.

2. **Л4 — эталон правила (strict-in 62/53/53%, APPROVE-CLEAN).**
   Failure-нить распределена по всем 5 разделам с явными «Engineering lesson» / критериями / альтернативами (Obermeyer, парадокс PPV, DSP-1181, Change Healthcare, 4-actor framework).
   → **Reference-модель** структуры failure-контента для прикладных лекций L4–L17.

3. **Системная находка: slides — слабейший артефакт для failure-контента во всех лекциях.**
   Уроки проговариваются устно (speaker notes / речь), но не вынесены на видимый слой слайда. Самое дешёвое лечение — surfacing существующих устных уроков на visible layer 1–2 слайдов, без раздувания объёма.
   → **Production-guidance:** при дизайне слайдов проверять, что failure-урок виден на слайде, а не только в notes. Кандидат в presentation-designer/critic чек-лист (не внедрял — вне scope, REPORT-only).

4. **Качество bucket'а ≠ объём.**
   Где доля формально есть, но подана дисклеймером без явного *урока/критерия/альтернативы* — критик метил P1 (Л2 §4.2/s19 «стохастичность»). Правило теперь требует не только %, но и наличие суждения (в рубрике methodology-critic).

## Незакрытое (передано)
- Л4 4 P2-leads → issue #73 (текущий production), решение исполнителя.
- Л1/Л2 ориентир доработки сохранён в аудит-отчёте на случай отзыва owner-waiver (#82).
