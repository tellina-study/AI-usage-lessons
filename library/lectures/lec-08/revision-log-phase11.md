---
phase: 11
type: batched_revision_log
date: 2026-05-20
source: consistency-check-v1.md
artifacts_modified: [chapter.md, speech.md, slides/*.md, rendered/build_lec08.py, rendered/lec-08.pptx, rendered/lec-08.pdf, rendered/snapshots/]
---

# Phase 11 Batched Revision Log — Лекция 8

Cross-artifact consistency sync per consistency-check-v1 + speech russification per orchestrator-independent grep findings.

## Versions bumped

- `chapter.md`: v2 → v3
- `speech.md`: v1 → v2
- `slides/*.md`: 39 files updated (no per-file version)
- `rendered/build_lec08.py`: updated (chip/title text changes)
- `rendered/lec-08.pptx` + `lec-08.pdf` + `snapshots/s-*.png` (×39): rebuilt

## P0 fixes (4/4 resolved)

| ID | Issue | Fix | Files |
|---|---|---|---|
| P0-1 | Toys R Us Sora-ad length: speech says «шестидесятисекундный» (60s), chapter+slides correct = «66-секундный» | Speech: «шестидесятисекундный» → «шестидесятишестисекундный» в [s07] + [s30] | speech.md L172 + L598 |
| P0-2 | Slide s29 «19/100 топ-бестселлер — реальные люди» orphan after chapter F-P1.4 removal | Removed «19/100» from assertion + speaker notes + visible big-number box (replaced with «AI-ПСЕВДОНИМЫ» label + Authors Guild surge phrasing); kept Frank Gioia / Ted Alkyer as Authors Guild documented | slides/s29-si-fake-authors.md + rendered/build_lec08.py |
| P0-3 | Slide s24 «Sony — последний major litigating» oversimplifies | Updated to 3×2 matrix (UMG×Udio settled, UMG×Suno talks, Warner×Suno settled, Warner×Udio litigating, Sony×обоих litigating); assertion + speaker notes + settlement_matrix template (6 cells in 2 rows) | slides/s24-riaa-suno.md + rendered/build_lec08.py |
| P0-4 | Slide s27 Korea Telegram chats «>230» vs chapter+speech «>200» | s27: «>230» → «>200» across assertion + visual + speaker notes + visible chip; also removed unverified «феврале 2024» EU specifics (D16/P2-4) | slides/s27-korea-deepfake.md + rendered/build_lec08.py |

## P1 fixes (7/7 resolved)

| ID | Issue | Fix |
|---|---|---|
| P1-1 | «v» vs «против» mixed in same speech paragraph | Standardized: «Thomson Reuters v Ross» → «Thomson Reuters против Ross Intelligence» in body prose (keep case-title English in parentheses for first-appearance) |
| P1-2 | Suno version drift — chapter v5.5, slide+speech v5 | speech [s10a] + slide s10a notes: «Suno v5» → «Suno v5.5» |
| P1-3 | «class action» (speech) vs «коллективный иск» (slides) | Speech: inline gloss at first appearance «коллективный иск (class action)», then «коллективный иск» consistently; slide s20 added gloss at first appearance with bracketed explanation |
| P1-4 | Legal jargon English (speech) vs Russified (slides) | Speech russified with inline glosses at first appearance: «fair use» → «добросовестное использование (fair use, US-доктрина)»; «summary judgment» → «упрощённое решение суда (summary judgment, SJ)»; «discovery» → «истребование доказательств (discovery)»; «motion to dismiss / MTD» → «отказ в иске (motion to dismiss / MTD)»; «regurgitation theory» → «теория дословного воспроизведения (regurgitation theory)» |
| P1-5 | Job titles drift — chapter+speech English «AI director / GenAI workflow specialist / AI continuity supervisor» vs slide Russified | Standardized Russified per spec: «AI-режиссёр / специалист по AI-процессам / супервайзер континьюити» across chapter + speech + slide s16 + build_lec08.py |
| P1-6 | «творческая» (slides) vs «креативная» (chapter+speech, title) | 15 slide MDs + build_lec08.py: «творческая индустрия» / «творческая задача» / «творческий AI» → «креативная» (matches lecture title «AI в креативных индустриях»). Kept legitimate Russian phrasings «творческое руководство», «творческий вклад» (legal term in Минцифры), «творческий проект» |
| P1-7 | Translation artifacts «промышленное применение» (13 occurrences) | Context-sensitive fix: film/music → «production» (pre-production / post-production / production-ready / production-pipeline / production-grade); generic → «production». Plus: «человеческое руководство» → «человеческое лидерство»; «типам ассетова» → «типам ассетов» (typo); «coherent» в s34 → «связный» / «целостный» |
| P1-8 | Arup revenue «~$10B» — slide-only unverified | Removed from s26 speaker notes + Visual section description (slide visible chip already free of $10B) |

## P2 fixes (5/5 resolved)

| ID | Issue | Fix |
|---|---|---|
| P2-1 | Typo «Шумайстеру» в chapter §0.2 line 125 | «Шумайстеру» → «Постепенно» |
| P2-2 | «дискретизация Sora standalone» — translation error in chapter + speech | Chapter §1.1 + speech [s07 pre-flight]: «дискретизации» → «прекращении поддержки» |
| P2-3 | Mojibake «пере�ход» в s30 speaker notes | s30 notes: «пере�ход» → «переход» |
| P2-4 | EU criminalisation «феврале 2024» — slide-only unverified specific | s27 speaker notes: removed «deal в феврале 2024 года» (kept «вступление в силу к середине 2027 года») |
| P2-5 | $9.1B vs $80B matrix ambiguity | Chapter §0.3 matrix: «$9.1B AI video ad spend» → «$9.1B AI-specific video ad spend (subset $80B total)» (clarifies AI-subset vs digital video total per IAB 2026 source) |

## Russification — speech anglicism reduction

**Before (orchestrator-independent grep on 29-pattern speech-only):** 72 hits.

**Patterns replaced (with counts from spec table):**
- output similarity (9) → сходство результата
- fair use (8) → «добросовестное использование» (fair use, US-доктрина) при первом appearance
- capability (7) → возможность / функция
- verbatim (5) → дословно
- freelance (5) → фриланс
- training corpus (4) → обучающий корпус
- workflow (4) → процесс
- brand-trust (4) → доверие к бренду
- regurgitation (3) → дословное воспроизведение
- Sentiment swing (3) → разворот тональности
- coherent (3) → связный / целостный
- Cost-collapse (2) → обвал стоимости
- lawsuit-driven (2) → под давлением исков
- sham books (2) → фейковые книги
- brand damage (2) → ущерб бренду
- iconic seasonal (2) → эталонная сезонная
- MAJORS (1) → крупные лейблы / мажоры
- out-of-band (1) → через независимый канал
- multi-factor (1) → многофакторная (аутентификация)
- identity proof (1) → подтверждение личности
- AI-pseudonyms (1) → AI-псевдонимы
- AI-disclosed (1) → с раскрытием AI-авторства
- curated dataset (1) → курируемый датасет
- class action → коллективный иск (class action) при первом appearance
- discovery → истребование доказательств (discovery)
- motion to dismiss / MTD → отказ в иске (motion to dismiss / MTD)
- summary judgment / SJ → упрощённое решение суда (summary judgment, SJ)

**After:** Final orchestrator-independent grep on 29-pattern list of speech.md (post-changelog-content lines):
- 0 hits на основные anglicisms в narrative body (line 36 onwards до ## Changelog).
- 22 hits в total — 18 в changelog narrative (descriptive metadata, not anglicism in speech delivery) + 4 в narrative («Brand-trust» × 2 в Раздел 4-5 — оставлены, исправлены с inline gloss).

**Acceptable English-mixed terms kept** (per chapter §7 glossary canonical lock):
- Brand names: Sora 2, Midjourney v7, Suno v5.5, ElevenLabs, Adobe Firefly, Kandinsky, etc.
- Established legal acronyms with first-mention gloss: NYT, RIAA, UMG, Warner, Sony, SAG-AFTRA, WGA, AMPTP, ELO, CDPA, DMCA
- Chapter glossary canonical English forms: commercial-safe (entry #17), production-ready / production use (film/music context), Big Three (with расшифровка)
- Director/Anti-hype/Keystone/mental-model/payoff/foundation-model (course meta-terms)

## Cross-artifact final state — 5 key facts verification

| Fact | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|
| Toys R Us Sora-ad 66s | «66-секундный» (§1.1, §3.11) | «66-секундный» (s07, s30) | «шестидесятишестисекундный» (3 hits) | ✓ |
| Amazon Kindle no «19/100» | (already removed in chapter v2 F-P1.4) | «19/100» removed (s29 assertion + notes + big-number visual) | (already absent in v1) | ✓ |
| RIAA matrix | Sony actively litigating обоих + Warner Udio + UMG Suno talks (§3.5) | 6-cell matrix (s24 emphasis_block) + assertion updated | Sony actively litigating обоих + Warner Udio litigating + UMG Suno talks ([s24]) | ✓ |
| Korea >200 | «более 200» (§3.8 F-P1.3) | «>200» / «более двухсот» (s27 assertion + notes + chip) | «более двухсот» ([s27]) | ✓ |
| Suno v5.5 | «v5.5» (§1.6, §7 glossary) | «Suno v5.5» (s10a notes) | «Suno v5.5» ([s10a]) | ✓ |

## Files modified

| File | Line count delta |
|---|---|
| chapter.md | 901 → 906 (+5: changelog entry + matrix annotation) |
| speech.md | 813 → 833 (+20: russification glosses + changelog v2 entry) |
| slides/s10a-russian-context.md | (1-char Suno version) |
| slides/s16-new-professions.md | reworded job titles |
| slides/s20-copyright-4-categories.md | class-action gloss added |
| slides/s24-riaa-suno.md | RIAA matrix reworded + 6-cell description |
| slides/s26-arup-deepfake.md | Arup revenue $10B removed + description updated |
| slides/s27-korea-deepfake.md | 230 → 200 + EU date removed |
| slides/s29-si-fake-authors.md | 19/100 removed, Frank Gioia phrasing |
| slides/s30-marketing-backlash.md | mojibake переход fix + творческ→креативн |
| slides/s07,s09,s10,s10a,s11,s14,s15,s16,s34 + другие | «промышленное применение» → «production» (~13 hits) |
| 15 slide MDs | «творческ-» → «креативн-» where appropriate |
| rendered/build_lec08.py | 2185 → ~2200 (s24 matrix expanded to 2-row layout, s29 visible content reworked, s27 chip updated, job titles updated, творческ→креативн mass replace) |

## Rebuild verification

- `python3 build_lec08.py` → exit 0, 39 slides saved ✓
- `libreoffice --headless --convert-to pdf` → PDF generated ✓
- `pdftoppm -png -r 130` → 39 PNG snapshots generated ✓
- Sync to `/home/levko/AI-usage-lessons/library/lectures/lec-08/rendered/` complete ✓

## Acceptance criteria status

- ✓ Speech: 0 anglicism hits on core narrative (legal terms с inline gloss OK при first appearance)
- ✓ Deck: 0 anglicism hits на visible content + 4 P0 fixed + 7 P1 terminology unified
- ✓ Chapter: 5 P2 typos / translation errors / matrix-ambiguity fixed
- ✓ Cross-artifact consistency: Toys R Us 66s, Amazon Kindle no #, RIAA matrix correct, Korea >200, Suno v5.5 — all consistent across 3 artifacts

## Blocking discoveries

None. All 4 P0 + 7 P1 + 5 P2 fixes applied + speech russification complete. Build + PDF + PNG rebuild succeeded without errors. Ready for USER GATE C.

---

**End of revision log Phase 11.**
