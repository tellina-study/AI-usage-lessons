# Consistency Checker Report — Лекция 3 — 2026-05-16 (deck v3)

**Mode:** chapter+slides (Phase 7, v3 cross-artifact alignment + ref-точность + deck-split целостность)
**Scope:** deck.yaml + deck-part2.yaml + slides/sNN-*.md против finalized chapter (chapter.md / chapter-part2.md / chapter-part3.md) + glossary.yaml LOCK + plan-v2-final.md §4.
**Speech:** не существует на этой фазе (Phase 9 ещё не запущена) — speech-alignment вне scope.
**Issue:** #87. **NOT git.**

---

## VERDICT: **APPROVE-CLEAN**

- **P0 (factual contradiction / book-first violation / missing coverage / orphan ref):** 0
- **P1 (significant drift):** 0
- **P2 (minor inconsistency):** 1 (косметика citation-chain в s13 notes — НЕ блокирует)

Все 7 case-refs, добавленные в speaker notes v3, **дословно совпадают** с finalized главой (book-first соблюдён). Deck-split целостен. Маркеры главы целы, глава не правилась. Терминология — 0 forbidden форм. 0 orphan-ссылок. Арка соответствует плану §2.2.

---

## 1. Deck-split целостность (фокус 1) — ✅ PASS

| Проверка | Результат |
|---|---|
| deck.yaml + deck-part2.yaml вместе = 36 слайдов | ✅ 15 (s01..s13a) + 21 (s13b..s31) = 36 |
| IDs уникальны (нет дублей) | ✅ 36 уникальных, `uniq -c` → 0 DUP |
| Нет пропусков (s01–s30 monotonic + 6 suffix) | ✅ s01–s30 + s04a/s13a/s13b/s23a/s25a/s31 все присутствуют |
| Порядок канонический (plan §2.2/§4) | ✅ s01..s04, **s04a**, s05..s09, s10..s13, **s13a**, **s13b**, s14..s18, s19..s23, **s23a**, s24, s25, **s25a**, s26..s30, **s31** — точное совпадение с plan §4 |
| Оба файла ≤600 строк | ✅ deck.yaml = 353, deck-part2.yaml = 425 |
| Кросс-ссылки между файлами | ✅ deck.yaml L13/35/101/349-351 → part2; deck-part2.yaml L5/11-12/423-424 → part1 (двусторонние) |
| `deck_parts: [deck.yaml, deck-part2.yaml]` объявлен | ✅ deck.yaml L35 |
| Loader build_v3.py читает обе части | ✅ build_v3.py L338-339 (`p1=deck.yaml`, `p2=deck-part2.yaml`), L367 `assert tot == 36` |
| deck↔slide-файл консистентность (все `file:` существуют) | ✅ 36/36 файлов существуют (0 MISS) |
| totals блок (PART 2) согласован | ✅ `slides: 36`, `suffix_slides: [s04a,s13a,s13b,s23a,s25a,s31]`, `base_slides_locked: s01–s30 НЕ перенумерованы` |

**Вывод:** split структурно целостен. s01–s30 НЕ перенумерованы (cascade-tracking lock соблюдён) — это критично для отсутствия orphan-ссылок.

---

## 2. Маркеры главы целы / глава не правилась (фокус 2) — ✅ PASS · book-first соблюдён

- `git diff --stat HEAD -- chapter*.md` → **пусто**. Глава не модифицирована с коммита `c2200a4` (GATE A finalized). **Diff главы не ожидался и не обнаружен — book-first подтверждён.**
- `[for-slide-sNN]` маркеры в главе: **s01–s30 все 30 присутствуют** (нет suffix-маркеров — корректно: suffix-слайды НЕ требовали правки главы).
- Маппинг новых suffix-слайдов на **существующие** § главы:

| Suffix | deck chapter_ref | Реальная § главы | Валиден? |
|---|---|---|---|
| s04a (divider Р1) | §1 `[for-slide-s05]` | §1 (intro раздела, маркер s05 существует) | ✅ divider → intro секции |
| s13a (divider Р3) | §3 `[for-slide-s14]` | §3 intro (маркер s14 существует) | ✅ divider → intro секции |
| **s13b (определение FT)** | **§3.1 `[for-slide-s14]`** | **chapter-part2.md §3.1 L38: «**Fine-tuning (дообучение)** — это дополнительное обучение... при котором изменяются веса»** | ✅ определение УЖЕ было в §3.1, slide лишь поднимает его на видимый слой; маркер s14 переиспользован (документировано) |
| s23a (sub-div Безопасность) | §4.6, §4.7 `[for-slide-s24]` | §4.6/§4.7 (маркер s24 существует) | ✅ sub-divider → intro блока |
| s25a (divider Р5) | §5 `[for-slide-s26]` | §5 intro (маркер s26 существует) | ✅ divider → intro секции |
| s31 (Q&A) | §5.5 `[for-slide-s30]` | §5.5 (маркер s30 существует) | ✅ Q&A → конец раздела |

**Вывод:** все 6 suffix-слайдов маппятся на СУЩЕСТВУЮЩИЕ § главы без правки маркеров. s13b определение FT **не введено слайдом** — оно дословно присутствовало в §3.1 (book-first: slide подаёт уже-существующий материал). Маркеры s01–s30 целы.

---

## 3. Case-refs точность (фокус 3, КРИТИЧНО U-4) — ✅ PASS · 0 ref не из главы

Таблица сверки добавленных в speaker notes v3 атрибуций против finalized главы (§ Источники chapter-part3.md L317-358 + inline):

| Ref на слайде (speaker notes) | Slide | == глава §? | Verdict |
|---|---|---|---|
| Air Canada: «*Moffatt v. Air Canada*, BC CRT (Канада), 14.02.2024; McCarthy Tétrault 2024; ABA 2024» | s01 | ✅ chapter.md L89/L314 (14 февраля 2024, BC трибунал, McCarthy Tétrault 2024, ABA 2024) + Источники L321-322 | **OK** |
| CoT faithfulness: «Anthropic апрель 2025; Claude 3.7 ~25%; DeepSeek R1 ~39%» | s07 | ✅ chapter Источники L324 (Anthropic 2025-04, Claude 3.7 ~25%, DeepSeek R1 ~39%) + §1.3 | **OK** |
| Barnett: «Barnett et al. (arXiv:2401.05856, 2024) — семь точек отказа RAG» | s13 | ✅ chapter.md L298 + Источники L335/L370 (arXiv:2401.05856, семь точек отказа) | **OK** (P2 цитата-chain — см. ниже) |
| Air Canada callback: «*Moffatt v. Air Canada*, BC CRT, 14.02.2024» | s13 | ✅ chapter §2.5 L314/L320 (14.02.2024, BC трибунал) | **OK** |
| Luo: «Luo et al., arXiv:2308.08747, 2023 — catastrophic forgetting при continual fine-tuning» | s16 | ✅ chapter-part2.md L82 + Источники L339 (Luo Y. et al. 2023, arXiv:2308.08747) | **OK** |
| $4,200: «постмортем Sattyam Jain, 2026-04; single-author; числа округлены; иллюстративный» | s23 | ✅ chapter-part3.md L46/L350 (Sattyam Jain 2026-04, single-author, числа округлены, illustrative) | **OK** |
| reliability compounding: «MindStudio, 2025–2026» | s23 | ✅ chapter-part3.md Источники L351 (MindStudio 2025–2026) | **OK** |
| NYT v. OpenAI: «федеральный суд в мае 2025; Bloomberg Law 2025; National Law Review 2025; `[VFY day-of]`» | s24 | ✅ chapter-part3.md L65 (федеральный суд **в мае 2025**) + Источники L346 (Bloomberg Law; National Law Review 2025-11 — publication date, не event date; согласовано) | **OK** |
| ZDR Anthropic: «live-документ Anthropic об удержании данных, 2026, `[VFY quarterly]`» | s24 | ✅ chapter-part3.md Источники L345 (Anthropic 2026, live doc, *API and Data Retention*) | **OK** |
| GitHub MCP heist: «май 2025; Docker «MCP Horror Stories» 2025; AuthZed 2025–2026; Simon Willison 2025-04-09» | s25 | ✅ chapter-part3.md §4.7 L79 + Источники L348-349 (Docker 2025; AuthZed 2025–2026; Simon Willison 2025-04-09; GitHub MCP heist май 2025) | **OK** |
| tool poisoning/rug-pull: «инструмент меняет определение после установки» | s25 | ✅ chapter-part3.md L80 (tool poisoning / rug pull, кейс #8) | **OK** |
| MindStudio (s29 NANDA — не в v3-добавке) | s29 | ✅ chapter-part3.md Источники L353 (MIT NANDA, ~95%, методология) — не изменялся в v3 | **OK** |

**КРИТИЧЕСКИЙ ВЫВОД:** **Ни одна ref на слайдах НЕ введена сверх главы.** Все атрибуции, цифры (~25%/~39%, $4,200/63ч, ~95%), даты (14.02.2024, май 2025, 2026-04), arXiv-ID (2401.05856, 2308.08747) — **дословно совпадают** с finalized главой. **0 P0 нарушений book-first.**

**P2-1 (косметика, НЕ блокирует):** s13 speaker notes цитируют Barnett напрямую («Barnett et al. (arXiv:2401.05856, 2024)»), тогда как глава §2.4 (L298) даёт цепочку «Kore.ai со ссылкой на Barnett et al., arXiv:2401.05856» и Источники L335 — «Kore.ai (2024–2025) (со ссылкой на Barnett et al.)». arXiv-ID и авторство верны, deck `notes_case_refs_v3` для s13 сам пишет «Barnett et al. arXiv:2401.05856 (2024)» — slide упростил citation-chain до первоисточника. Факт корректен, источник тот же. Рекомендация (опционально, Phase 8): для строгого book-first можно добавить «(систематизировано Kore.ai)» в s13 notes — но это polish, не drift.

---

## 4. Drift: новые слайды vs глава (фокус 4) — ✅ PASS

| Проверка | Результат |
|---|---|
| s13b определение FT vs chapter §3.1 | ✅ s13b assertion «FT меняет САМИ ВЕСА... отличается от промпта/RAG (меняют контекст)» == chapter §3.1 L38 «RAG и промпт кладут знание в контекст... веса не трогают; fine-tuning меняет саму модель». Концептуально дословно. Speaker notes s13b — связный студенческий текст, derived из §3.1, без новых фактов. |
| s13b vs s14 (не противоречат?) | ✅ Комплементарны: s13b = что такое FT (механика весов); s14 = FT сузился до поведения. Обе grounded в §3.1 (L38 определение + L7-26 «сузился»). |
| s14 не дублирует inline-define FT | ✅ Видимый слой s14 НЕ переопределяет FT (gap корректно закрыт в s13b; deck L49 «inline-define больше НЕ дублируется здесь») |
| s30 новый title vs chapter §5.5 | ✅ Title «AI-архитектура — несущая ось отраслевых лекций» (контентный тезис, не function-as-title) согласован с §5.5 L259-265 («рамка — база для всех последующих лекций»; «какая архитектура и почему именно она, и при каком условии ответ был бы другим»; Семинар 3). U-6 ретайтл документирован в deck `retitled_v3`. |
| s30 Q&A удалён → s31 | ✅ s30 visible: «Q&A УБРАН (теперь s31)»; s31 — отдельный qa_minimal. Нет дублирования Q&A. |
| Дивайдеры s04a/s13a/s23a/s25a narrative-bridge vs глава | ✅ Мосты соответствуют intro соответствующих § (s13a «проблема не в знании, а в поведении» == §3 intro; s25a «соберём в инструмент выбора» == §5 intro) |
| Central question consistency | ✅ deck.yaml `central_question` == plan §2.1 == s04 == chapter.md L22/L41 — verbatim («У меня есть задача и доступ к LLM. Какую архитектуру выбрать — и когда правильный ответ "не ИИ"?») |
| Цифры/числа на новых слайдах | ✅ s13b — нет новых цифр (определение). Дивайдеры — нет цифр. s31 — нет цифр. |

**Вывод:** 0 drift. Новые слайды не противоречат главе; s13b/s14 grounded в одной §3.1; s30 retitle aligned с §5.5.

---

## 5. Терминология (glossary LOCK) — ✅ PASS · 0 forbidden

| Проверка | Результат |
|---|---|
| Forbidden anglicisms в slides (пайплайн/фоллбэк/эдж-кейс/инсайт) | ✅ 0 в slides (включая speaker notes) |
| Forbidden term-forms (раг/файнтюнинг/фью-шот/воркфлоу/тулюз/ретривал/эм-си-пи) | ✅ 0 в slides |
| s13b «fine-tuning / дообучение» — canonical | ✅ `fine-tuning` ×50 + `дообучение`/`дообученные` (canonical alias glossary L48-49) consistent; **0 `файнтюнинг`/`файн-тюнинг`** (forbidden L50) |
| Новые divider'ы — canonical формы | ✅ s04a «Промпт», s13a «Fine-tune vs промпт vs RAG», s23a «кто видит данные в цепочке», s25a «фреймворк решения» — все canonical, 0 forbidden |
| Drift глава↔слайды по новым слайдам | ✅ s13b термин «fine-tuning (дообучение)» идентичен chapter §3.1 + glossary canonical L48 |

**Вывод:** glossary LOCK соблюдён по всем новым слайдам. Critic не предлагает rename (за пределами полномочий — только REPORT). Канон оптимален, PROPOSED GLOSSARY UPDATE не требуется.

---

## 6. Арка / точки возврата ЦВ / orphan-ссылки (фокус 6) — ✅ PASS

| Проверка | Результат |
|---|---|
| Порядок 36 == plan §2.2/§4 | ✅ Точное совпадение (см. §1 выше) |
| Раздел-бюджеты vs plan §2.2 | ✅ deck-part2 totals note: Р0=8, div s04a 0.3, Р1=9, div s09, Р2=12, div s13a 0.3, s13b 1.5, Р3=9, div s18, Р4=13, sub-div s23a 0.3, Р4-sec=6, div s25a 0.3, Р5=11, s30 1.5, Q&A s31 ≤5 — совпадает с plan §2.2 таблицей |
| Air Canada through-line не разорван | ✅ s01 (hook) → §2.5 → s13 (revisited as grounding). Дивайдеры между ними (s04a/s09/s13a) — структурные, не разрывают нарратив (narrative-bridge явно мостит) |
| ЦВ точки возврата (s04/s08/s12/s17/s22 + payoff s26-s28) | ✅ Все слайды существуют; central_question идентичен; «когда НЕ» в каждом разделе сохранён (s08/s12/s17/s22) |
| callback s07 (в s21/s29) | ✅ s07 существует; deck s21 L159 «callback s07», s29 L335 «callback s07» — цель существует |
| callback s28 (в s30) | ✅ s28 существует; mini-apply задача B → s30 разминка |
| Все slide-id refs в slides → existing | ✅ 36/36 refs resolve (0 ORPHAN); s01–s30 НЕ перенумерованы → callbacks целы после suffix-вставок |
| ai_failure_judgment bucket целостность | ✅ 12 strict-in [s07,s08,s12,s13,s16,s17,s22,s23,s24,s25,s27,s28] все существуют; partial_out корректно включает 6 структурных suffix + s01/s14/s26/s29; share ≈33% слайдов / ≈43% минут (≥30% удержан) |
| Designer-extras в новых suffix (Лектору/Вы здесь/тайминг) | ✅ 0 в s04a/s13a/s13b/s23a/s25a/s31 |

**Вывод:** 0 orphan-ссылок. Cascade-tracking lock (s01–s30 не перенумерованы) сработал — suffix-вставки не создали ни одной битой ссылки. Арка и точки возврата ЦВ целы.

---

## DISCREPANCIES

### D1 — Citation-chain упрощение в s13 (Barnett)
**Severity:** P2 (minor, НЕ блокирует APPROVE-CLEAN)
**Where:** slides/s13-rag-fails-air-canada.md speaker notes vs chapter §2.4 (chapter.md L298) + Источники (chapter-part3.md L335)
**Issue:** s13 notes: «известный паттерн... семь точек отказа систематизированы у Barnett et al. (arXiv:2401.05856, 2024)». Глава даёт цепочку: «Kore.ai со ссылкой на Barnett et al., arXiv:2401.05856». arXiv-ID, авторство, год, факт («семь точек отказа») — верны и совпадают; slide процитировал первоисточник напрямую, опустив посредника Kore.ai. deck `notes_case_refs_v3` для s13 сам формулирует как «Barnett et al. arXiv:2401.05856 (2024)» — slide следует deck-спецификации.
**Recommendation:** Опционально на Phase 8 — добавить в s13 notes «(семь точек отказа систематизированы Kore.ai со ссылкой на Barnett et al., arXiv:2401.05856)» для строгого зеркала citation-chain главы. Это polish, не drift: факт и первоисточник корректны, book-first по существу соблюдён (slide не ввёл непроверенную ref — ref есть в главе).

---

## Coverage gaps
- **Нет.** Все LO chapter (LO7/LO4) покрыты; s13b закрыл пререквизит-gap определения FT на видимом слое (раньше только inline в s14 — теперь явный слайд, grounded в §3.1). Plan §4 36-слайдная спека покрыта полностью.

---

## Cross-artifact matrix (ключевые концепты v3)

| Концепт / число / ref | Chapter | Slides (v3) | Aligned? |
|---|---|---|---|
| ЦВ «какую архитектуру / когда не ИИ» | chapter.md §0 L22/L41 | deck central_question · s04 · s04a-s25a дивайдеры | ✅ verbatim |
| Air Canada 14.02.2024 BC CRT | §0 L89, §2.5 L314-320 | s01 notes · s13 notes (callback) | ✅ |
| CoT faithfulness Claude 3.7 ~25% / DeepSeek R1 ~39% | §1.3 / Источники L324 | s07 notes | ✅ |
| Barnett arXiv:2401.05856 (7 точек RAG) | §2.4 L298 / L335 | s13 notes | ✅ (P2 chain) |
| FT определение «меняет веса ≠ контекст» | §3.1 L38 | **s13b (NEW)** assertion+notes | ✅ grounded §3.1 |
| FT сузился → поведение/стиль/формат | §3.1 L7-26 | s14 | ✅ |
| Luo arXiv:2308.08747 (2023) cat. forgetting | §3.3 / part2 L82 / L339 | s16 notes | ✅ |
| $4,200/63ч Jain 2026-04 single-author | §4.5 part3 L46 / L350 | s23 notes | ✅ |
| NYT v. OpenAI фед.суд май 2025 | §4.6 part3 L65 / L346 | s24 notes | ✅ |
| ZDR Anthropic live-doc 2026 | §4.6 / L345 | s24 notes | ✅ |
| GitHub MCP heist май 2025 | §4.7 part3 L79 / L348-349 | s25 notes | ✅ |
| s30 «несущая ось отраслевых» + Семинар 3 | §5.5 part3 L259-265 | s30 (retitled U-6) | ✅ |
| Q&A отдельный финальный слайд | §5.5 (мост) | s31 (NEW, qa_minimal) | ✅ |

---

## Топ-фиксов (per artifact)
- **Chapter:** нет правок — book-first соблюдён, глава finalized, 0 P0 главы.
- **Slides:** 0 обязательных фиксов. Опционально Phase 8 (polish, не блокирует GATE B): D1 — добавить «(систематизировано Kore.ai)» в s13 notes для строгого citation-chain mirror.
- **Speech:** не существует (Phase 9 не запущена) — вне scope.

---

## Подтверждения (явно, по запросу task)

1. **«Глава не правилась»:** ✅ `git diff --stat HEAD -- chapter*.md` пусто; глава на коммите GATE-A finalized. Diff не ожидался, не обнаружен. **Book-first соблюдён.**
2. **«Маркеры целы»:** ✅ Все `[for-slide-s01..s30]` присутствуют в главе; suffix-слайды НЕ потребовали правки маркеров — маппятся на существующие §.
3. **«Любые ref не из главы»:** ✅ **0.** Все 11 проверенных case-ref атрибуций (Air Canada, CoT %, Barnett, Luo, $4,200 Jain, NYT, ZDR, GitHub MCP, MindStudio, tool poisoning, NANDA) — присутствуют в finalized главе с теми же датами/цифрами/ID. Ни один слайд не ввёл непроверенную ref.
4. **Deck-split целостен:** ✅ 36 уникальных IDs, канонический порядок, оба файла ≤600 строк, loader читает обе части + assert tot==36, 0 orphan-ссылок.

---

## ИТОГ

**VERDICT: APPROVE-CLEAN**

- **P0: 0** · **P1: 0** · **P2: 1** (D1 — citation-chain polish в s13, опционально, НЕ блокирует).
- **Ref не из главы: 0** (книга = source of truth соблюдён без исключений).
- Deck-split целостен; глава не правилась; маркеры целы; терминология 0 forbidden; 0 orphan; арка == plan §2.2.

v3 cross-artifact alignment **чистый**. Готов к Pre-USER-GATE walkthrough (Phase 8.5) → USER GATE B. D1 — на усмотрение оркестратора/Phase-8 как опциональный polish, gate не блокирует.
