# SYNTHESIS — v4 Plan Лекции 1 — 2026-05-12

**Issue:** #67 (Phase 1 of EPIC #64).
**Источники:** 3 параллельных критика.
- `methodology-critic.md` — 6 P0 / 9 P1 / 7 P2.
- `reader-text-only.md` — 3 P0 / 9 P1 / 5 P2.
- `fact-checker.md` — 6 P0 / 8 P1 / 5 P2.

## Общий вердикт

**v4 plan не proceed-to-chapter as-is.** План хороший как brief для лектора, но **15+ P0/P1 issues** воспроизведутся в chapter (~10k слов) и slides+speech. Methodology-critic явно говорит: «chapter (10k слов) воспроизведёт системные проблемы → переписывание в 5-10× дороже, чем поправить план сейчас».

**Рекомендация: создать v5 plan с фиксами ДО старта Phase 2 (chapter draft).** USER GATE 0 = approve v5 plan.

## Convergent findings (≥2 критика согласны)

### КОНВЕРГЕНЦИЯ 1 — Central question «попасть в 10%» = magic-pill anti-pattern
- **methodology-critic** (P0): magic-pill anti-pattern #10 из catalog. Reformulate в диагностический tone.
- **(implicit) reader**: «90% звучит как fearmongering» (s5).
- **(implicit) fact-checker**: «90%» из CNews/Vedomosti, не АНО ЦЭ — attribution слаб.
- **NB:** v3.6 пилот **уже сделал** этот фикс на уровне slides («Где AI работает, где — нет, и как это понять?»). План v4 не обновлён под это решение. Нужно sync план с slides.

### КОНВЕРГЕНЦИЯ 2 — «Инженер ИУ6» depersonalize
- **methodology-critic** (P0): local binding anti-pattern #8. В плане 6+ мест (s05×3, s14, s18×2, s27, s29).
- **NB:** v3.6 пилот уже убрал из slides. План v4 не обновлён.

### КОНВЕРГЕНЦИЯ 3 — s5 «90% AI-пилотов откатываются»
- **methodology-critic** (P1): сильное утверждение без обоснования.
- **reader** (P0): без методологии звучит как «магическая цифра» / fearmongering. Стержень лекции висит без обоснования.
- **fact-checker** (P1): цифра подтверждается, но attribution **не АНО ЦЭ**, а CNews / Vedomosti / Intellectual Analytics (март 2026).
- **Fix:** заменить attribution + добавить методологию («что считается откатом», stages).

### КОНВЕРГЕНЦИЯ 4 — s4 + s14 «Доли LLM-рынка РФ» factual error
- **reader** (P1): сумма ≠ 100% (115%), что мерили?
- **fact-checker** (P0): сумма 108%, DeepSeek 43% = глобальные downloads (Microsoft 2026), НЕ market share РФ. ВЦИОМ multi-select: DeepSeek **20%**, не 43%.
- **Fix:** заменить на верифицированную метрику + явный multi-select disclaimer.

### КОНВЕРГЕНЦИЯ 5 — s18 чек-лист (кульминация раздела 3) — без worked example
- **reader** (P0): студент не сможет применить чек-лист без worked example.
- **methodology-critic** (implicit): LO6 и LO7 покрыты только на remember-уровне, нет apply.
- **Fix:** worked example в chapter (взять кейс с конвейера → прогнать 4 вопроса → ответ «модель»).

### КОНВЕРГЕНЦИЯ 6 — s22 overloaded (5-6 концептов за 2 минуты)
- **methodology-critic** (P0): 6 концептов + 4 термина-сироты (RLHF, data poisoning, prompt injection, guardrails).
- **reader** (P0): студент через 2 недели не вспомнит ничего.
- **Fix:** сжать до 3 связных концептов (bias + sycophancy + distribution shift).

### КОНВЕРГЕНЦИЯ 7 — Раздел 4 (17 мин) перегружен + 0 retrieval moments
- **methodology-critic** (P0): 0 retrieval-moment'ов между s18 и s23 (24 мин passive).
- **reader** (P1): материал на 2-3 лекции спрессован.
- **Fix:** добавить 2 retrieval moments (think-pair-share, poll).

### КОНВЕРГЕНЦИЯ 8 — Layered mental model model/chat/agent/app
- **reader** (P1): студент не схватывает различие; разное смешано в s12-s17.
- **methodology-critic** (implicit): концептуальная последовательность нарушена.
- **Fix:** в chapter explicit «chat = model + UI + memory; agent = chat + tools + planning».

## Уникальные находки (одного критика, но важные)

### От methodology-critic (P0/P1 only)
- **LO7 ошибочно мапится на s01** — камера-демо показывает «AI работает» (LO1), а LO7 = «критическая проверка». Снять с s01.
- **LO6/LO7 только remember-level**, нет apply/evaluate moment.
- **Cognitive load hotspots:** s07 (15 фактов / 4 мин), s08 (16 терминов / 2 мин), s12 (split-attention triple-channel), s24 (politicization без bias-разбора).

### От fact-checker (P0)
- **s9 «92% разработчиков США»** — реально Stack Overflow 2025: 84% globally / 51% daily. Цифра неверна.
- **s16 Chan et al.** — wrong attribution. Реально Feng/McDonald/Zhang arXiv:2506.12469, 5 ролей пользователя (не L0-L4 autonomy levels).
- **s22 sycophancy rollback март 2025** → апрель 2025.
- **s10 $5.6M DeepSeek** = V3, не R1; marginal cost, full infra $1.3-1.6B.
- **s5 Gartner 80%** — конкретный отчёт не найден; заменить на верифицированную «80% workforce upskill by 2027» или «40% enterprise apps with AI agents by 2026».

### От reader-text-only
- **s7 UDIO/Sakana** имена без контекста (P2).
- **s15 PARTS vs Роль+Задача+Контекст** несостыковка (P2).
- **s17 Copilot — приложение или агент?** ambiguity (P2).
- **s20 «100K запросов/день»** откуда (P1)?

## Топ-N правок до v5 plan (приоритизированно)

### P0 (обязательно перед chapter draft)
1. **Central question + ИУ6** — sync план v4 с v3.6 slides. Заменить «Как инженеру ИУ6 попасть в оставшиеся 10%?» на «Где AI работает, где — нет, и как это понять?» в s5, s14, s27 (и других местах). Убрать все «инженер ИУ6» (6 мест).
2. **s4 + s14 LLM доли** — заменить на верифицированную ВЦИОМ-метрику (multi-select, n=1600, методология). Убрать DeepSeek 43% market share / вынести как «43% global downloads».
3. **s5 attribution «90%»** — заменить АНО ЦЭ на CNews / Vedomosti / Intellectual Analytics. Добавить методологию «что считается откатом».
4. **s5 Gartner 80%** — заменить на верифицированную формулировку.
5. **s9 «92% разработчиков США»** — заменить на 84%/51% Stack Overflow 2025.
6. **s10 DeepSeek $5.6M** — уточнить V3 vs R1, marginal vs full infra.
7. **s16 Chan et al.** — фикс attribution на Feng/McDonald/Zhang + content (5 ролей пользователя).
8. **s22 sycophancy** — март → апрель 2025.
9. **s22 overload** — сжать до 3 концептов.
10. **s18 worked example** — добавить в план note для chapter author.
11. **s01 LO7 mapping** — снять.
12. **Раздел 4 retrieval moments** — добавить 2 (после s21 think-pair-share, после s22 poll).

### P1 (сильно желательно)
13. **ВЦИОМ 51% методология** — uточнить (интернет-пользователи 18+).
14. **Layered model/chat/agent/app** — добавить в план note для chapter.
15. **s08 классификации** — note «expand в chapter по одной оси на абзац».
16. **s21 hallucination range** — обновить с Vectara HHEM современного leaderboard.
17. **s21 CybSafe** — 34.8% → 38%.
18. **s23 ARC-AGI-2** — обновить «пустые LLM 0%» (устарело).
19. **s17 Google Translate** — обновить 2016 → 2026.
20. **s27 сломанные refs** на s14/18/27 — пометить «полная версия» если pilot only.

### P2 (не блокеры)
21. **s7 UDIO** — убрать (не от автора Attention).
22. **s7 цитирования** — динамическая цифра.
23. **s15 PARTS vs RTC** — выровнять.
24. **s20 EU AI Act fines** — полная структура.
25. **s25 Pearl 3 уровня** — расписать.

## Что предлагаю дальше

### Создать v5 plan (notes/lecture-1-review/final/new-plan-v5-final.md)

Делегирую `book-editor` (но не в роли writer chapter — а как **plan editor**):
- Вход: v4 plan + 3 critic reports + SYNTHESIS.
- Output: v5 plan с применёнными P0 + P1 фиксами.
- Размер: останется ~29 слайдов, изменения локальные.

После v5 — повторный read через 1-2 критика (sanity check) ИЛИ сразу USER GATE.

### Альтернатива

Если P0 фиксы кажутся слишком many — можно:
- (a) Применить только P0 (12 правок) в v5, остальное оставить chapter author'у как note.
- (b) Сразу применить P0 + P1 (20 правок) в v5, чтобы chapter author работал с чистым input.

Я склоняюсь к **(b)** — отложить P1 в chapter повышает риск drift.

## От тебя — USER GATE 0

1. **Согласен с findings?** Конвергенция 1-8 + уникальные?
2. **Подход к v5:**
   - (a) Только P0 (минимально).
   - (b) P0 + P1 (полнее, моя рекомендация).
3. **Кто пишет v5 plan:**
   - (a) book-editor (он умеет редактировать).
   - (b) general-purpose subagent с конкретным prompt.
4. **После v5 — sanity check или сразу к chapter?**

После твоих ответов — спавню v5 plan, потом USER GATE на v5, потом Phase 2 (chapter draft).
