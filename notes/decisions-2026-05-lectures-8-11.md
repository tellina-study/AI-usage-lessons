# Решения: 21 мая 2026 (лекции 8–11, рефлексии)

Часть журнала решений. Указатель и текущие записи — в [decisions.md](decisions.md).

## 2026-05-21 — Рефлексия Лекции 8: 3 ENFORCED-правила в инфраструктуру (#122)

Рефлексия: `notes/reflections/2026-05-21-lec-08/`. Production Л8 завершён (PR #121 merged, #119 closed), 3 owner-интервенции на GATE B (~3 дополнительных revision rounds, ~83 минуты wasted). Все 3 предотвратимы постоянной инфраструктурой.

- **IMP-1 No-mock-fallbacks (стоимость ~1.5h cycle wasted).** Designer Phase 6+7 столкнулся с paywall/JS на BBC/Futurism/NYT/Reuters/etc. → blanket-fallback: 16 stylized Ocean-palette PNG mocks с verbatim headlines. Self-report 87.2% media coverage прошёл orchestrator visual sweep (mocks выглядели похоже на cards). Owner: «что за херня, где картинки? ты просто забил! ... все переделать». → Memory rule [[no-mock-fallbacks]] + 6-tier acquisition (og:image / Wikipedia / press release / YouTube thumb / Wayback / Google Images) с per-image attempt log. Validation: 16/16 real images, 87.5% Tier 1 success. → propagated в `tools/presentation-build/README.md` + `presentation-designer.md` + `presentation-critic.md` + Pre-USER-GATE skill + CLAUDE.md anti-patterns.
- **IMP-2 Russification (стоимость ~3h, 3 revision passes).** Producer agents (designer + speech-writer) свободно использовали английскую tech-лексику в visible body для RU-аудитории МГТУ ИУ6. Pattern-narrow grep (32 patterns) показал 0-72 hits; deep latin-token scan (любое English слово вне brand allowlist) показал 224 unique в PPTX и 919 unique в speech. Owner: «обилие англицизмов в презе! это просто трындец! провал». → Memory rule [[russification]] + таблица 45+ replacements + explicit keep-list (brand names, established acronyms с inline gloss, mode names) + deep latin-token scan в pre-GATE. → propagated в `tools/presentation-build/README.md` + `presentation-designer.md` + `speech-writer.md` + `book-editor.md` + `presentation-critic.md` + Pre-USER-GATE skill + CLAUDE.md.
- **IMP-3 Hero-images на s01 + s39 (стоимость 6 min — простое улучшение).** Owner explicit запрос: «не хватает броской иллюстрации на самом первом слайде и на завершающем, сделай и запиши себе как общее требования ко всем презам». → Memory rule [[hero-images-required]] ≥40% area + 6-tier acquisition + Russian captions + Ocean palette. → propagated в `tools/presentation-build/README.md` + `presentation-designer.md` + `presentation-critic.md` + Pre-USER-GATE skill + CLAUDE.md.
- **IMP-4 Pattern-narrow grep маскирует depth of problem.** Мой initial Russification verification (32-pattern) вернул 0-4 hits → подумал deck clean. Deep latin-token scan показал 919 в speech. → новый mandatory check «deep latin-token scan» для RU-language deck перед каждым USER GATE (не только pattern check).
- **IMP-5 Critics в Phase 7.5 не отличали mock от real image.** 3 critics (presentation/student/reader) flag-нули placeholder issues, но не различали «stylized mock с verbatim headline в Ocean palette» от actual screenshot. → `presentation-critic.md` checklist: «if slide claims to show screenshot from external source — can you identify source page URL? matches what source would show?»
- **IMP-6 Single batched revision agent (Phase 11) сработал отлично.** Per CLAUDE.md anti-pattern, one book-editor agent смог touch chapter + slide MD + speech одним проходом для consistency fixes (4 P0 + 7 P1 + 5 P2). Подтверждено как preferred pattern для multi-artifact polish.

**Сработало (усилить):** Worktree-изоляция параллельно с Лекцией 9 (0 контеншена); 6-tier image acquisition после re-spawn (87.5% Tier 1); 12 case-слайдов с «Урок для инженера» в Ocean gold rounded box format; Kelly McKernan plaintiff portrait + Drew Ortiz CNN screenshot — real images dramatically сильнее abstract case names; X-62 VISTA DARPA bridge к Лекции 9 — strongest pedagogical bookend.

**Метрика успеха:** следующая лекция (Л10+) — 0 owner-интервенций классов (а) mock-вместо-real, (б) anglicism leaks, (в) missing hero s01/s39. Pre-GATE B walkthrough catches все 3 automatically через updated infra.

## 2026-05-21 — Лекция 9 production (рефлексия, #118; reflection-folder `notes/reflections/2026-05-21-lec-09/`)

Production Л9 завершён (PR #120 merged 2026-05-21), 1-day cycle, 12 commits, 17 critic-spawns. Lessons learned:

- **Анонимизация = default, не per-lecture intervention.** Л9 v2 chapter содержал «МГТУ им. Баумана, Факультет ИУ, Кафедра... ВКА им. Можайского, МАИ, СПбГУ» в §5.2 + frontmatter audience «ИУ6 МГТУ Бауман». User explicit correction → 1 revision cycle (v2→v3). **Fix:** embedded mandate в `.claude/agents/book-editor.md` + `tools/lecture-production/README.md §3.7a` + `templates/lecture-outline.md`. Эталон: lec-03/lec-05/lec-07 — 0 named institutions.

- **Speech-writer self-report «0 anglicism hits» был массивно ложным (реальность 107 patterns).** Memory rule `feedback_russification` существовала, но не embedded в agent default. **Fix:** mandatory pre-submission anti-anglicism self-grep в `.claude/agents/speech-writer.md` § ENFORCED Anti-anglicism (top-30 regex blacklist, report ACTUAL count не narrative «0»). Lec-09 cost-of-omission: 2-3ч revision pass.

- **Designer self-report «72% media-rich» был misleading.** Counted icons-in-boxes + primitive shapes как media. **Fix:** strict media-rich definition в `.claude/agents/presentation-designer.md` § ENFORCED Media-rich definition: real photo OR generated diagram OR chart OR UI screenshot OR BEFORE/AFTER case. НЕ icons, НЕ primitives. Pre-render counter с specific media kind per slide. Lec-09: v1 0 real photos → v2 17 photos (113% target after 6-tier Tier 2 Wikimedia acquisition).

- **Inherited fact drift из chapter в slides — subset rerun недостаточен.** Phase 4.5 fact-checker subset rerun (UN LAWS only) пропустил §1.7 (Du→Ye) + §2.2 (CENTCOM→EUCOM). Found только Phase 7 slides QA fact-checker. **Fix:** ENFORCED full citation sweep на каждой chapter revision в `tools/lecture-production/README.md` Phase 4 line. Subset reruns acceptable только для P0 verification ПОСЛЕ full sweep.

- **API 529 overload pattern: defer retry 30+ мин, не immediate.** Lec-09 consistency-checker Phase 7 dropped 2× immediate retries, 3-я попытка через ~30 min recovery succeeded. Reusable для transient infra issues.

- **GATE-C definition-of-done honored.** Manifest lectures.yaml lec-09 → produced включён в финализирующий PR #120 (не отдельный manifest-PR). Лекция 4 lesson applied successfully — repeatable pattern.

- **Memory rules не embedded в agent defaults — структурный gap.** До Л9 правила (anonymization, Russification, no_mock_fallbacks, hero_images) существовали только в memory files; subagent prompts требовали orchestrator manual injection. **Fix:** Memory rules с ENFORCED статусом embedded в `.claude/agents/*.md` defaults — agent видит mandate каждый spawn без orchestrator повторения. Survival rate rules в production цикле = высокий.

**Метрика успеха для Л10+:** 0 owner-интервенций классов (а) named institutions в chapter, (б) anglicism self-report inflation, (в) primitive-only media, (г) inherited fact drift. Updated infra catches все 4 automatically.

## 2026-05-21 — Лекция 11 production (рефлексия, #131; reflection-folder `notes/reflections/2026-05-21-lec-11-production/`)

Production Л11 «AI в дискретном и процессном производстве» завершён (PR #130 merged 2026-05-21), single-day cycle, 38 commits, ~22 agent-spawns. Финал: chapter v5 multi-part (30 930 слов, 3 файла ≤600 строк) + slides v2.2 (41 слайд, 56% media, hero ≥40% s01+s39) + speech v2 (5 289 spoken words, 0/41 фрагмент >95 WPM).

- **Chapter Depth Baseline ENFORCED — новое фундаментальное правило (PR #129).** Owner explicit «30k цель твоя» override на ad-hoc Лекция 10 target 20-26k → **минимум 30 000 слов для всех L4+ chapter'ов**. Записано в CLAUDE.md новой ENFORCED секцией «Chapter Depth Baseline» + tools/lecture-production/README.md §6 + memory `feedback_chapter_depth`. Multi-part split mandatory при >600 строк per file (chapter.md + chapter-part2.md + chapter-part3.md). L1-L3 owner waiver доступен, L4-L17 mandatory. Counter-check: <28.5k для L4+ → REVISE структурный gap.

- **Лекция 4 «designer self-report FALSE» паттерн повторился ДВАЖДЫ в L11.** (а) Phase 8.5: presentation-designer заявил «designer-extras 17→0» — orchestrator-INDEPENDENT regex на rendered PPTX visible body нашёл 10 timing markers «N мин» на 6 slides (s03 lecture-map + 5 dividers). (б) Phase 11.5: parallel revision designer заявил «4 slide fixes complete» — orchestrator-INDEPENDENT cross-artifact verify нашёл slide s34c brewery numbers drift (60K bph vs chapter+speech 30K canonical, parallel scope не touched s34c). Оба caught via independent python-pptx text extract + grep, не self-report. **Fix carry-forward:** centralized `tools/presentation-build/deep_designer_extras_scan.py` script + `cross_artifact_numbers_check.py` для auto-detection drift между artifacts. Pre-USER-GATE skill вызывает scripts automatically. (См. improvements.md I-1, I-2.)

- **Parallel revision agent scope gaps cost +15 мин quick-fix.** Phase 11 spawned speech-writer + presentation-designer параллельно с different briefs — speech-writer fixed brewery в speech, designer fixed unrelated 4 slides. Brewery slide s34c не в scope ни одного. **Fix:** при parallel revision спавнах — orchestrator brief MUST include EXPLICIT cross-artifact alignment requirements per agent, не assume sibling artifact consistency. Carry-forward в `tools/lecture-production/README.md` § Polish Round Pattern.

- **Hero size designer self-report unreliable.** Phase 8 designer заявил «s01 42.5% / s39 43.2% area». Visual sweep showed s01 31% / s39 32.5% (P0 — below ≥40% mandate). **Fix:** independent hero size measurement script `tools/presentation-build/hero_size_check.py` (PPTX shape coordinates × slide dimensions) — orchestrator не trust self-report, measure independently. (См. improvements.md I-4.)

- **Russification regression на новом контенте при каждой revision.** Chapter v3 expansion (Phase 4b) добавил 16k новых слов — 101 anglicism leak hits (regression от v2 closed-P1). Slides v1 design имел 620 unique non-whitelist latin tokens. Phase 5+6 designer initial render имел Tier 1-4 English subheaders, рекурсивные parens. **Fix:** deep latin-token scan **после каждой revision** mandatory, не только финальный pre-GATE. Producer agents всё ещё drift при новом content generation.

- **Owner mandate M1/M2/M3 labeling pattern works well.** Phase 8 owner brief contained 3 explicit mandates («убери методические + временные», «убери англицизмы», «переведи цитаты»). Orchestrator labeled M1/M2/M3 в spawn brief — каждый стал independent acceptance criterion. **Fix:** formalize pattern в CLAUDE.md methodology или anti-patterns section — when user gives multi-part mandate, label M1/M2/M3 + propagate в agent prompts с explicit verify per M.

- **Quote translation mandate — extension of Russification.** Owner explicit «переведи цитаты!» extended Russification rule beyond narrative — to direct quotes. 5 quotes translated to RU primary на slides + speech (Musk April 2018 / Bainbridge 4 ironies / Foxconn Liu Computex 2025 / Trump «8th wonder» / Toyota GAIA). English original optional в speaker notes parenthetical italic gloss. **Fix:** update memory rule `feedback_russification` + producer agent prompts с quote translation mandate.

- **Snapshot PNG numbering shift при slide insertion.** Phase 8 added s34b + s34c (worked examples for §4.3) → original s35-s39 shifted to s37-s41 in render position. PNG snapshot names `s-XX.png` follow render position, не source slide ID. Caused orchestrator confusion at GATE C walkthrough (s-39.png ≠ slide s39). **Fix:** auto-generated sidecar `library/lectures/lec-NN/rendered/slide-index.yaml` mapping PNG-position → source-slide-ID. (См. improvements.md I-7.)

- **Pre-USER-GATE walkthrough как separate phase окупается.** L11 имел 0 user feedback rounds AFTER each GATE — все P0/P1 caught в walkthrough ДО presenting. Это паттерн который sustainably eliminates Лекция 1-стиль rounds (3 user feedback rounds post-critic-approve). Walkthrough is mandatory phase, not optional polish.

- **Manifest update в том же finalizing PR — соблюдено** (GATE-C definition-of-done ENFORCED). lectures.yaml lec-11 status planned → produced в commit на той же branch. Carry-forward pattern.

**Метрика успеха для L10/L12+:** 0 owner-интервенций классов (а) designer self-report FALSE (extras / hero / Russification), (б) cross-artifact numbers drift в worked examples, (в) parallel revision scope gaps, (г) quote translation missed для RU аудитории. Updated infra (PR #129 + I-1/I-2/I-3/I-4) catches все 4 automatically.

**Production efficiency baseline для отраслевых лекций (L_N+):**
- Phases: 11 standard + 4.5/8.5/11.5 pre-USER-GATE = 14 distinct steps
- Agent spawns: ~20-25 (research + plan + chapter draft+revise+expand + slides design+visual+revise + speech draft+revise + 8 critic runs)
- USER GATE feedback rounds: target 0 (pre-USER-GATE walkthrough catches P0)
- Wall-clock: single-day cycle achievable с parallel critics
- Artifacts: chapter ≥30k multi-part / slides 35-41 / speech ~5k / manifest update / reflection

---

## 2026-05-21 — Лекция 10 production findings (issue #137 reflection)

- **2 NEW ENFORCED rules introduced mid-flight по explicit user feedback.** Both bundled в PR #136 с lec-10 production (precedent: Лекция 9 #123, Лекция 11 #129):
  - **«No Timing / No Methodology in Slides»** — user signal «в каждой лекции правлю» indicates rule violated systematically across L1-L9+10. Existing No Extra Content Rule был too abstract; новая section provides explicit forbidden pattern list (timing regex `\b[0-9]+\s*мин(ут)?\b` + methodology regex `(методическ|педагогическ)\s*\w+|На этом этапе студент|Зачем это в Лекции`). Pre-USER-GATE Walkthrough Rule §5 расширен 3 groups grep (scaffold + timing + methodology). Anti-Patterns table +2 rows.
  - **«Baseline / Counterfactual Mandate for Measurable Claims»** — user signal «во многих оценках эффектов/потерь не хватает базы. а сколько на человека или без робота? а сколько было?» exposes pedagogical gap. Pre-USER-GATE точка 12 added (baseline coverage check sample 5-7 measurable). Anti-Patterns +1 row. Все measurable claims (acres / cows / $$ / % / kg / hours) ОБЯЗАНЫ inline base / counterfactual / denominator.

- **Batched revision pattern окупается на P0+P1 combined fixes.** Phase 8 v2 (lec-10): single presentation-designer agent applied 8 P0 + 32 P1 batched, regenerated PPTX + PNG snapshots. Phase 11 v2: single book-editor agent applied 3 P0 + 12 P1 across 3 artifacts atomically (speech v1→v2 + chapter v3.2→v3.3 + slides s05/s10/s37s re-render). **vs per-artifact serial fixing** — batched eliminates inter-phase drift и снижает agent invocations.

- **Self-report inflation × 2 verified в этой сессии.** Phase 6 designer self-report 66 anglicism candidates → independent presentation-critic scan 84 (~27% inflation). Phase 9 speech-writer self-report 2 critical → methodology-critic broad regex 43. **Pattern stable across lectures:** subagent self-grep систематически underestimates. **Mitigation already in CLAUDE.md (Pre-USER-GATE Walkthrough Rule §5 ENFORCED orchestrator-INDEPENDENT)** — это works когда applied.

- **Usage limit handled correctly per memory rule `feedback_subagent_usage_limit`.** 2 hits в этой сессии (Phase 4b chapter expansion + Phase 11 batched revise). Memory rule explicit: **«limit ≠ failure»**, wait for reset + re-spawn same brief. Orchestrator НЕ self-implement как workaround. **Verified pattern.**

- **AP2a/AP2b split — strongest pedagogical insight отраслевых лекций.** Cognitive Pilot (CV) vs ИТЭЛМА (sensor-fusion на multi-GNSS) framed как «architecture choice within AI domain», not «AI vs не-AI». **Это concept-cracker** для студентов после L7 (closed-loop medicine) + L9 (OODA dual-use). Применимо к будущим отраслевым лекциям где есть multiple AI architectures для same task.

- **Лестница 5 уровней (L1→L5) как keystone-axis для отраслевых лекций.** Reader-simulator verified «через 2 недели восстанавливается по памяти» — sticky mnemonic. Pattern: для industry-applied lecture, taxonomic ladder с growing controllability + falling biological/environmental noise + measurable ROI — образцовый scaffold. Compare к L9 OODA-keystone (conceptual axis) — both work, но ladder лучше для multi-segment industries.

- **Plenty Compton failure-first hook + closing callback arc.** Pattern: open lecture с dramatic recent failure ($940M / 19 мес / –99% valuation) + close с causal explanation («не из-за плохого AI, из-за термодинамики LED»). Hook → keystone → 5 анти-AI критериев → close = narrative arc complete. **Align с course mission «учить говорить нет»**, не «AI revolution». Применимо ко всем отраслевым лекциям.

- **Multi-lecture parallel production проверен (4 worktrees one-time).** lec-10 (`/tmp/lec-10-wt`) + lec-12 + lec-13 + lec-14 worktrees coexist; main repo на main; branch ref sync через `git update-ref` без contention. Лекция 10 finalization (PR #136) clean-merged несмотря на parallel Лекция 11 (#129) infrastructure changes. **Pattern works for ≥4 parallel lectures.**

- **Cross-artifact cascade fix pattern (chapter ↔ slides ↔ speech) в одном batched book-editor agent.** Phase 11 v2 lec-10 demonstrated: agent касается 3 артефактов atomically + re-renders affected slides + updates frontmatters. **Превосходит per-artifact serial cascade** (avoid drift between fixes). Recommended для все cross-artifact P0 cascade fixes в future lectures.

**Metric для L10:** 0 user feedback rounds AFTER each critic-APPROVE (vs Лекция 1 v3 = 3 rounds; Лекция 8 = 3 rounds wasted ~83 min). 2 user mid-flight interventions handled как infrastructure improvements, не one-off fixes. **Pre-USER-GATE Walkthrough Rule patterns (3 versions: A/B/C) sustainably eliminate post-critic owner intervention.**

