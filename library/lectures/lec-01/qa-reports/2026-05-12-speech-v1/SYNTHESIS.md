# SYNTHESIS — speech v1 Phase 10 — 2026-05-12

**Issue:** #69 (Phase 10 of EPIC #64).
**Артефакт:** `library/lectures/lec-01/speech.md` (5821 слов, 73.5 min заявлено).
**3 критика:** methodology-critic + fact-checker + consistency-checker (все Opus 4.7).

## Общий verdict

**⚠️ NEEDS REVISION перед USER GATE 3 final.** methodology REJECT (3 P0), fact+consistency APPROVE-WITH-MINOR. Главный блокер — **pacing рассинхрон** (66.5 vs 73.5 vs 75 mins) + 7 слайдов TOO-FAST WPM + 0 «мы с вами» — детали из methodology-critic.

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| methodology-critic | **3** | 6 | 4 | ❌ **REJECT** |
| fact-checker | 0 | 3 | 3 | ✅ APPROVE-WITH-MINOR |
| consistency-checker | 0 | 4 | 9 | ✅ APPROVE-WITH-MINOR |
| **После дедупликации** | **3** | **~10** | ~13 | NEEDS REVISION |

## 3 P0 (методология) — обязательно

### P0-M1 — Pacing рассинхрон
- Frontmatter `75 min` ≠ sum slides 66.5 ≠ task brief 73.5.
- 6541 слов при 60-80 wpm = **82-109 минут реальной доставки** = overrun 7-34 мин.
- **Fix (рекомендую b):** поднять allocation на 7 TOO-FAST слайдов = +5 мин до 71.5 мин активной + 3.5 буфера, и обновить frontmatter.

### P0-M2 — 7 слайдов > 120 wpm (непроговариваемо)
- s05b 125 / **s06 141** / s17 132 / **s19 134** / **s22 150** / **s24 137** / **s25 143**.
- Физически невозможно проговорить за declared time.
- **Fix:** либо поднять length_min, либо сократить слова per slide. См. methodology report детали.

### P0-M3 — «Мы с вами» — 0 раз (playbook violation)
- Playbook требует inclusive language. Speech — преимущественно «вы» — создаёт дистанцию, обвинительный тон в s19+.
- **Fix:** засеять минимум 8-10 экземпляров «мы с вами» в ключевых местах (s05b, s06, s11, s18, s22, s28).

## Конвергентные P1 (≥2 критика)

### КОНВЕРГЕНЦИЯ A — s10 MCP исчезает в speech
- **methodology** + **consistency** (D2): chapter §2.2 + slide s10 visible content включают MCP, speech не упоминает.
- **Fix:** добавить упоминание MCP в [s10] (1 предложение).

### КОНВЕРГЕНЦИЯ B — s24 речь дублирует slide
- **methodology** P1 (410 слов прямого пересказа таблицы).
- **Fix:** сократить до 280 слов, оставить 2 контрастных лидеров (Altman vs LeCun) развёрнуто.

## Уникальные P1

### От methodology
- s12 demo — нет fallback timing'а если >2 мин.
- s03 — нет backup для тишины (мало рук).
- Дидактически-обвинительный tone s19/s22.
- s01 «по всему зоопарку AI-инструментов» — magic-pill light.
- s24 предложение 27 слов про «Какое решение он бы хотел».

### От fact-checker
- **P1-F1 s07** — Vaswani 160K+ цитирований: добавить timestamp «на май 2026» (dynamic data, +5K/month).
- **P1-F2 s23** — ARC-AGI: pre-flight checklist «verify arcprize.org leaderboard за 1 день до лекции, обновить s23 numbers если изменились» (Gemini 3.1 Pro / GPT-5.5 уже past 54%/37.6%).
- **P1-F3 s09** — GitHub Copilot 46% / Java 61%: backup attribution готов.

### От consistency-checker
- **D1 s04** — DeepSeek teachable moment не звучит в речи (chapter §2.1 имеет ВЦИОМ 20% vs Microsoft telemetry 43%; speech даёт только обобщение «смотрите на методологию»).
- **D3 s25** — Pearl levels 2/3 worked examples не проговариваются (chapter §4.8 имеет $100/мес лимит, fine-tune; speech даёт сухие дефиниции).
- **D4 s15** — Role B content drift: chapter+slide «не-специалист, далёкий от технологий» vs speech «врач-практик объясняющий пожилому пациенту» — слушатель видит одно, слышит другое.

## P2 (на усмотрение)

- s10 marginal cost определение, s13 edge-устройство, s28↔s21↔LO7 мостик, mid-point recap §4.5↔§4.6, 7-тематическая раскладка раздела 4 в [s19].
- s22 Altman quote shortened, s09 AI market $244-390B source not named orally.
- Frontmatter обновить length_words и length_min после fix.

## Сильные стороны (НЕ менять)

✅ **Zero drift** (fact-checker): 38 critical statistics matches между chapter v2 и speech v1 (ВЦИОМ, Stack Overflow, DeepSeek timeline, Vectara HHEM, ARC-AGI, GPT-4o sycophancy, etc.).
✅ **Central question синхронно** (consistency): chapter «Где AI работает, где — нет?» = slide s05b = speech [s05b].
✅ **GPT-4o sycophancy 25/28/29 апр** — синхронно во всех 3.
✅ **Feng/McDonald/Zhang 5 levels** — корректная атрибуция везде.
✅ **0 mentions ИУ6** — universal tone выдержан.
✅ **Diagnostic tone** в s05b: «Это не рецепт успеха. Это диагностика».
✅ **Conversational, не дидактический** в большинстве мест.
✅ **30 pacing markers + 43 interactive moments + 10 backup phrases** — мощная фактическая структура.

## Топ-N правок для Phase 11 revision (приоритезированно)

### P0 (must fix)
1. **Pacing fix** — allocation +5 min на 7 TOO-FAST slides + frontmatter sync (66.5+5=71.5 + 3.5 buffer = 75).
2. **WPM fix** — sсократить s06/s17/s19/s22/s24/s25 ИЛИ увеличить allocation (см. #1).
3. **«Мы с вами»** — 8-10 экземпляров в s05b/s06/s11/s18/s22/s28.

### P1 convergent (2)
4. **s10 MCP** — добавить упоминание (1 предложение).
5. **s24** — сократить до 280 слов, контраст Altman vs LeCun развёрнуто.

### P1 unique (8)
6. **s12** fallback timing для demo > 2 мин.
7. **s03** backup для тишины.
8. **s19/s22** обвинительный tone → «наша инженерная работа».
9. **s01** «по всему зоопарку» → «по основным архетипам».
10. **s07** Vaswani citations timestamp «на май 2026».
11. **s23** pre-flight checklist для ARC-AGI numbers.
12. **s04** DeepSeek teachable moment в speech.
13. **s25** Pearl examples проговорить.
14. **s15** Role B content sync с chapter («не-специалист»).

### P2 (на усмотрение revision)
- s10 marginal cost определение.
- s13 edge-устройство определение.
- s28 LO7 мостик.
- Mid-point recap §4.5.
- s22 Altman quote.
- Frontmatter обновить.

## Recommendation orchestrator'у

**Phase 11 plan:**
1. Спавнить `speech-writer` (Opus) с 14 правками выше → speech v2.
2. Optional: 1 sanity-check methodology-critic на v2 (главный был REJECTовал).
3. После approval → USER GATE 3 final → multi-artifact lecture production complete.

**Estimated effort:** ~30-45 мин speech-writer на pacing fix + content revision.
