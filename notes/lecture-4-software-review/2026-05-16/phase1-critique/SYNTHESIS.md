# Phase 1 SYNTHESIS — plan v1 Лекции 4 «AI в разработке ПО»

**Дата:** 2026-05-16 · **Issue:** #99

## Сводный вердикт: **REVISE** (methodology governs) → plan-v2-final обязателен до USER GATE 0

| Критик | Verdict | P0 | P1 | Ядро |
|---|---|---|---|---|
| methodology-critic | **REVISE** | 1 | 6 | strict-in chapter/speech постулат не расчёт (P0-1); 42%→честно ~35.5% (11 solid + s24/s25 пограничные); s16/Раздел-4 hotspots; LO4 слабый Apply; course-конструкты без атрибуции; pacing 85≠75 |
| reader-text-only | APPROVE-WITH-POLISH | 0 | — | каркас сильный; s16 «как измерять» нет; Раздел 4 перегруз; SWE-bench не определён s12; мост s03 Л3→A→D тонок; perception-gap в s01 за 15 слайдов до раскрытия |
| orchestrator roast | — | — | — | pacing-математика §4 (Σ=80+5≠75); нумерация §2.2↔§4; L4 waiver НЕдоступен → chapter (22k таксономия) разжижает strict-in — инженерить осознанно; hook→s01 gloss + s04 disclaimer (урок Л3) |

## Обязательное в plan-v2 (P0/P1 + roast)

1. **[P0-1] strict-in операционализировать per-artifact, не постулировать.** §5/§12: chapter ≥40% и speech ≥35% — дать механику (именованные блоки + квантификация: «критерий "человек обязателен" ≥N слов × 6 разделов» + 5 детальных кейсов). Honest recompute slides: **11 solid/31 ≈ 35.5%** (s24/s25 пограничные → усилить failure/judgment-якорь, путь до ~42%). L4 ∉ L1–L3 → **waiver НЕдоступен** (Решение #82), реестр §3.6 только Л1/Л2. Несущая ось A→D НЕ failure сама по себе (в отличие от Л3-LO7) → failure-плотность главы проектировать намеренно (не «растечётся таксономией»).
2. **[P1 meth-2/4 + reader S-1] Раздел 4 реструктур + retrieval.** s17→s30 = 28 мин без retrieval; 3 security-слайда подряд. Разнести: тест+review один beat; безопасность — с retrieval-моментом; ≤2 security подряд. Добавить retrieval в Р4 и Р5.
3. **[P1 meth-2 + reader N-4] s16 METR: добавить КАК измерять.** «Измеряй, не верь ощущению» без метода = тревога без выхода (несущая рамка, эхо hook s01). Дать actionable: A/B на своих задачах, фиксировать реальное время, селективное применение. late-2025 «unreliable signal» reversal → chapter/notes (зеркало Л3 multi-agent/CVE→chapter).
4. **[reader S-3/N-* ] A/B-граница + s03 mapping + s01 gloss.** Артикулировать границу уровня A vs B (s05/s06) явным паттерном «что делает AI / кто решает / где человек обязателен» единым для A→D. s03 — явная таблица-мэппинг «6 ступеней лестницы Л3 → 4 уровня A–D» (иначе подрывает §1.1 тезис). s01 — 1-строчный inline-gloss perception-gap + s04 disclaimer «лестница = карта лекции» (урок Л3 fine-tuning/s13b).
5. **[P1 meth-1] LO4 — зафиксировать как entry-Apply.** §3: осознанное решение «s30 = entry-Apply (worked + think-pair-share mini-apply), full mastery = Семинар 4»; success-критерий привязать к осям матрицы s28.
6. **[P1 meth-5/6] Course-конструкты + Л3-пререквизит.** «лестница A–D», «70/80%-проблема», «perception-gap», «vibe-coding» — пометить course-scaffold + атрибуция (s04 disclaimer). §1.2 + §7 inline-safety-net: prompt-injection, лестница сложности, plan→act→check→iterate — мини-определение при 1-м упоминании (Л3 chapter — канон-пререквизит, но не дублировать визуально). §10 — pre-Phase-2 sanity vs finalized Л3 chapter (§ ссылки валидны).
7. **[roast P2→P1] pacing-математика честная.** §4 Σ бюджетов = 80 + 5 буфер = 85 ≠ 75. Пересчитать как Л3 plan §2.2 (slide-times ~55 + retrieval ~8 + переходы ~7 = 70 + 5 = 75) с явной сноской; нумерация разделов §2.2 ↔ §4 синхронна.
8. **[P2] SWE-bench inline-define s12; CWE inline s21 + ≤2 источника видимо; s27 не совмещать 2 owner-темы за 2.5 мин (дать 2 слайда либо +время).**

## Положительное (подтверждено)
Несущая ось A→D как продолжение лестницы Л3 — методически верна; honest partial→out уже в v1 (лучше Л3-v1); anti-hype, 0 anti-pattern-grep; owner-бриф покрыт; s17 Replit — эталонный failure-слайд (урок+4 альт+accountability); §1.2 пререквизит без дыр.

**После v2 (8 пунктов) → APPROVE-WITH-POLISH достижим → pre-gate → USER GATE 0.**
