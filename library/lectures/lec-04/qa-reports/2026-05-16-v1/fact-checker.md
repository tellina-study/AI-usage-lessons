# Fact-Checker Report — Лекция 4 slides + charts (Phase 7) — 2026-05-16

VERDICT: APPROVE-CLEAN

**Артефакт:** `library/lectures/lec-04/slides/*.md` (32 слайда) + 5 charts (`rendered/assets/charts/c{06,08,12,13,17}*.png`) + visible/notes слой.
**База истины:** `chapter.md` + `chapter-part2.md` + `chapter-part3.md` v1.1 (status=finalized) + `notes/research/lecture-4/{failures-and-limitations,sources,trends-2026}.md`.
**Issue:** #99. **Дата проверки:** 2026-05-16. **Scope:** только данные/цифры/даты/citations на видимом слое + speaker notes + charts. Методику/визуал/педагогику — не проверял (другие критики).

## Severity counts
- **P0 (false fact / broken citation / direction inversion / curriculum hallucination / возврат старой citation-ошибки): 0**
- **P1 (missing source / suspicious number без caveat / freshness expired): 0**
- **P2 (cite format / minor formulation): 1** (не блокирующий)

## Главный результат

Все числа на слайдах и в charts **совпадают с верифицированной главой v1.1**. Ни одна из старых citation-ошибок, исправленных в chapter v1.1 changelog, **не вернулась** на слайды. Все 5 charts рендерят корректные значения. Все volatile-факты (SWE-bench, adoption) несут `[VFY-day-of]` метку на видимом слое **или** в notes и не поданы как незыблемые.

## Таблица проверки: число/факт | slide/chart | == глава? | verdict | fix

| Факт | Slide / Chart | Глава (источник истины) | == глава? | Verdict |
|---|---|---|---|---|
| METR: прогноз −24% / вера −20% / факт **+19% времени** | s01, s17, **c17** | §0.1, §3.5, part2 §3.5/3.6 | да | VERIFIED |
| c17 sign-flip: «Прогноз до»≈−24, «Вера после»≈−20, «Измеренный факт»≈+19 (gold) | **c17-metr-gap.png** | §3.5 (вера −20% ускорение vs факт +19% замедление) | да — знак корректен | VERIFIED |
| METR n=16, 246 задач, своих репо 22k+, Cursor Pro + Claude 3.5/3.7, RCT 1H-2025 | s01, s17 | part2 §3.5 ст.84/111 | да | VERIFIED |
| METR framing: illustrative/early-2025 RCT, late-2025 «разворот»/selection-bias в главе, НЕ на слайд | s01 (verify_day_of:false), s17 footer | part2 §3.5 ст.113 | да — НЕ «AI ускоряет»; reversal off-slide | VERIFIED |
| SWE-bench Verified ~88,7% vs Pro ~64,3%, разрыв ~24 п.п. | s12, **c12** | §2.2 ст.266 (88,7% / 64,3% / ~24 п.п.) | да | VERIFIED |
| c12: Verified bar≈88,7, Pro bar≈64,3 (gold) | **c12-swe-bench.png** | §2.2 | да | VERIFIED |
| SWE-bench `[VFY-day-of]` (Л1 ARC-AGI устарел за 2 дня) | s12 footer + speaker notes; s27, s31 | §2.2 `[VFY-day-of]`; sources.md #47-49 weekly | да — на видимом И в notes | VERIFIED |
| «Почти правильный» код — топ-фрустрация **66%**; отладка 45,2% | s08, **c08** | §1.4 ст.186 (66% / 45,2%) | да | VERIFIED |
| c08 donut: 66 / 34 | **c08-almost-right.png** | §1.4 (66%) | да (34 = дополнение до 100) | VERIFIED |
| GitClear: клоны 8,3→**12,3%**, рефакторинг 24,1→**9,5%**, churn 5,5→**7,9%**, 211M строк | s13, **c13** | §2.3 ст.277 | да — направление клоны↑/рефакт↓/churn↑ корректно | VERIFIED |
| c13 grouped bars: Клоны 8,3/12,3 · Рефакторинг 24,1/9,5 · Churn 5,5/7,9 | **c13-gitclear.png** | §2.3 | да | VERIFIED |
| Автодоп: ~+56% лаб (точно 55,8%) / +7–22% поле / −19% легаси | s06, **c06** | §1.2 ст.167 («примерно на 56%, точно 55,8%»; +12,9–21,8% / +7,5–8,7%; −19%) | да — НЕ «+55%»-старое | VERIFIED |
| c06 bars: Лаборатория≈+56 · Поле≈+14 · Знакомое легаси≈−19 | **c06-context-effect.png** | §1.2 (поле в диапазоне +7–22) | да | VERIFIED |
| Replit: реальные данные, code-freeze, удалил prod-БД, солгал, **95/100**, rollback работал; Kiro 13ч; PocketOS 9 сек | s16 | part2 §3.4 ст.67-69, §3.3 ст.60 | да | VERIFIED |
| «более 1200 руководителей / 1190 компаний» | s16 (на видимом — «реальные данные», число опущено) | part2 §3.4 ст.67 | да — число не искажено (опущено корректно) | VERIFIED |
| slopsquatting: ~20% / 43% / **58%** воспроизводимо; **576 000** сэмплов | s22 | part2 §4.6 ст.215 (576 000 / ~20% / 43% / 58%) | да — НЕ «756 000» | VERIFIED |
| Seth Larson (PSF), апрель 2025 — термин slopsquatting | s22 | part2 §4.6 ст.213 | да | VERIFIED |
| NYU: ~**40%** в 89 security-сценариях; Schreiber 7703 файла **12,1% CWE**; Python ~16–18% | s21 | part2 §4.4 ст.185/254 | да | VERIFIED |
| NYU «Asleep at the Keyboard?» 2022 (citation 2108.09293, НЕ 2310.02059) | s21 footer («NYU, 2022») | part2 §4.4; sources.md #36; changelog P1-4 | да — старый ID 2310.02059 НЕ на слайдах | VERIFIED |
| Stanford: вносят больше уязвимостей И увереннее | s21 | part2 §4.4 ст.185/254 (dl.acm.org/10.1145/3716848) | да | VERIFIED |
| Brooks accidental/essential; «deciding precisely what to build» | s26 | part3 §5.2 ст.54 | да | VERIFIED |
| DORA 2025 n~5000, adoption ~90%, negative stability 2-й год, «amplifies what's already there» | s26, s27 | part3 §5.2 ст.57 | да | VERIFIED |
| CamoLeak: prompt-injection в Copilot Chat, confused-deputy; CVE — только в главе | s23 | part2 §4.7; CVE-2025-59145 в главе/sources #27 | да — CVE off-slide (нет риска неверного CVE) | VERIFIED |
| Anthropic «How AI Impacts Skill Formation» 2026, n=52, **−17%**, >60% делегировали / ≥65% концепции | s30, s32 | part3 §6.3 ст.188/190; sources.md #39; changelog P1-6 | да — корректное название статьи | VERIFIED |
| Meta TestGen: 32% vs 5,3% классов; 2,4% vs 15% мутантов; 100% coverage / ~4% mutation | s19 | part2 §4.1 ст.157/160 | да | VERIFIED |
| Code-review: Greptile 82%/11FP, CodeRabbit 44%/2FP, Graphite 6%, 50 багов | s20 | part2 §4.2 ст.165 | да | VERIFIED |
| SDD 3–10× first-pass — vendor-claim; AGENTS.md 20k→40k+ | s28 | part3 §6.4 ст.44/75/77 | да — помечено vendor/`[VFY]` | VERIFIED |
| s31 worked example: Pro ~64%; s27 ландшафт «направление, не доли» | s31, s27 | part3 §6 ст.208/213; §5.3 ст.68 | да — volatile не как факт | VERIFIED |
| Recap-маппинг: Л4 = первая отраслевая, аппарат Л3 (Модуль 1) | s03 | §0.2; chapter frontmatter (Module 1) | да — нет curriculum-галлюцинации | VERIFIED |

## DISPUTED / FALSE facts

Нет. 0 P0.

## Возврат старых citation-ошибок (целевая проверка брифа)

Grep по всем 32 слайдам — **все старые ошибки отсутствуют**:

| Старая ошибка (исправлена в chapter v1.1) | На слайдах? | Статус |
|---|---|---|
| «756 000» сэмплов (транспозиция, верно 576 000) | НЕТ | ✓ чисто |
| arXiv `2310.02059` (чужая статья Fu et al., верно 2108.09293) | НЕТ | ✓ чисто |
| `arXiv:2603.17973` / «GraphRAG+TDD −72%/−81% peer-review» (misattribution) | НЕТ | ✓ чисто |
| Старое название статьи Anthropic (верно «How AI Impacts Skill Formation») | НЕТ — везде корректное название | ✓ чисто |
| «+55%»/«на 55%» как первичный показатель автодопа (верно ~56% / 55,8%) | НЕТ — слайды используют «~+56%»/«пятьдесят шесть процентов» | ✓ чисто |

## NEEDS-CITATION (статистика без источника)

Нет. Все числа на видимом слое либо имеют source-footer, либо source в speaker notes, либо помечены vendor/`[VFY]`.

## UNVERIFIABLE

Нет недоступных источников для слайд-слоя — все числа сверены с finalized chapter v1.1 (та сама прошла Phase 3 fact-check + Phase 4 revision; research sources.md синхронизирован changelog'ом). Live WebSearch не потребовался: задача — сверка slide↔verified-chapter, не повторная верификация первоисточников.

## P2 (minor, не блокирует)

- **P2-1 (s01 формулировка знака).** Visible body: «Прогноз до эксперимента: AI ускорит на **−24%**» / «Вера после… ускорил примерно на **−20%**». Подпись «ускорит на −24%» формально-некорректна на чтение (ускорение со знаком минус — оксюморон вне контекста знаковой конвенции главы). Содержательно верно (совпадает с §3.5 и c17, где negative = ожидаемое ускорение, +19% = факт-замедление), и gold-callout + speaker notes («ускорит примерно на двадцать четыре процента / заняли на девятнадцать процентов больше времени») снимают двусмысленность. Это formulation-clarity, не factual error → P2, на усмотрение presentation-critic/book-editor; **не P0/P1, не блокирует показ**.

## Freshness — verify-on-day-of список (для pre-flight лектора)

Weekly cadence (sources.md #47-49) — ОБЯЗАТЕЛЬНО переверить в день лекции (Л1-урок: ARC-AGI устарел за 2 дня на 30+ пп):

| Факт | Slide | Cadence | Метка на слайде? | Действие в день лекции |
|---|---|---|---|---|
| SWE-bench Verified ~88,7% (GPT-5.5, рел. 2026-04-23) | s12 + c12 | **weekly** | да (footer + notes `[VFY-day-of]`) | переверить swebench.com / marc0.dev/leaderboard; лидер/число могли сместиться на 10+ пп |
| SWE-bench Pro ~64,3% (Claude Opus 4.7, апр 2026) | s12 + c12 | **weekly** | да (footer) | переверить Scale SWE-Bench Pro leaderboard |
| Доля Pro ~64% в worked-example | s31 | weekly (производное от выше) | косвенно | синхронизировать с обновлённым s12, если число изменилось |
| Adoption-доли инструментов (Copilot стагнирует / Claude Code, Cursor растут) | s27 | quarterly | да (footer `[VFY-day-of]`, «направление, не доли») | проверить JetBrains/Pragmatic, если дата лекции > середины 2026 |
| AGENTS.md 20k→40k+ репо | s28 | monthly | да (footer `[VFY-day-of]`) | проверить agents.md/infoq, если дата лекции далеко от 2026-05 |
| METR late-2025 «разворот» статус «unreliable signal» | s17 (в главе, не на слайде) | quarterly | главой покрыто | проверить, вышел ли methodology re-run METR (на слайд не выносится — корректно) |

Стабильные (yearly+, day-of-проверка НЕ требуется): METR early-2025 perception-gap, SO-2025 66%/45,2%, GitClear 8,3→12,3 / 24,1→9,5 / 5,5→7,9, Anthropic −17%, NYU ~40%, Brooks essential/accidental, DORA «amplifies», Replit/Kiro/PocketOS/CamoLeak/slopsquatting (исторические факты с датой).

## Charts — итог (целевая проверка брифа)

| Chart | Числа корректны? | Направление/знак | Соответствие главе |
|---|---|---|---|
| **c06-context-effect** | да (≈+56 / ≈+14 / ≈−19) | корректно (лаб > поле > 0 > легаси) | §1.2 — НЕ «+55%»-старое |
| **c08-almost-right** | да (66 / 34) | корректно | §1.4 (66% фрустрация) |
| **c12-swe-bench** | да (≈88,7 / ≈64,3) | корректно (Verified > Pro) | §2.2 |
| **c13-gitclear** | да (8,3/12,3 · 24,1/9,5 · 5,5/7,9) | корректно (клоны↑, рефакт↓, churn↑) | §2.3 |
| **c17-metr-gap** | да (≈−24 / ≈−20 / ≈+19) | **sign-flip корректен** (прогноз/вера отрицательны = ожид. ускорение; факт +19 = замедление, gold) | §3.5 |

Ошибок на charts **нет**.

## Топ-правок до публикации

Блокирующих правок **нет** (0 P0, 0 P1). Опционально (P2, на усмотрение book-editor/presentation-critic, не блокирует GATE B):
1. **P2-1:** рассмотреть формулировку s01 visible «AI ускорит на −24%» → напр. «прогноз: AI ускорит (−24% времени)» или дать явную подпись знаковой конвенции рядом с тремя числами, чтобы visible-слой читался так же однозначно, как gold-callout и notes.

---
**Вывод:** Слайды и charts Лекции 4 фактологически чисты относительно verified chapter v1.1. 0 P0 / 0 P1 / 1 P2 (non-blocking). Старые citation-ошибки не вернулись. Freshness-метки на месте. **APPROVE-CLEAN.** Единственное обязательное действие — лектор переверяет 5 weekly/monthly/quarterly пунктов из freshness-таблицы в день лекции (особенно SWE-bench s12/c12).
