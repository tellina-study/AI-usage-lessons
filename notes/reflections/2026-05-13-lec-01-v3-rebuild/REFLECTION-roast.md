# Reflection Roast — Lecture 1 v3.2 — 2026-05-13

**Reviewer:** methodology-critic agent (roast mode).
**Target:** `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION.md` (~6750 слов, 12 секций).
**Verdict short:** Reflection покрывает structural failure modes хорошо, но **критически слаб на visual/build/coordination операционке**. User лично указал ровно на это (последняя реплика session: «помимо прочего мы много правили визуал, но я не вижу этого в рефлексии»). Если внедрить только то, что в reflection — Лекция 2 пройдёт похожий путь с 2-3 раундами user feedback по ровно тем же причинам, что и Л1.

---

## Verdict on reflection itself

### Strong points (что покрыто хорошо)
- Failure-mode каталог (5 главных) — concise и точный.
- Анализ critic blind spots в §4.1 — 10 строк checklist'а реально actionable.
- Categorisation 3 раундов user feedback (§2.1-2.3) и подсчёт «62 user-driven changes» — solid evidence base.
- Open questions §11 (9 штук) — правильные вопросы, реально нужны user input.
- TL;DR concise, top-3 правильно расставлены приоритеты.

### Gaps (что пропущено или поверхностно)
1. **Визуальный production почти полностью отсутствует** (хотя 14 visual loop iter — половина wall-clock времени) — это ключевая жалоба user.
2. **WPM violations s07/s09/s17 (102-107 wpm) в финальной speech v3.2** — explicitly прошли «8 of 10 ≤97» как acceptable, но WPM ≤95 был P0 в REQUIREMENTS.md DoD. Это методическая регрессия, не отмечена.
3. **s14 deletion (Fix-17) — designer удалил слайд без user request** — упомянуто только в общей куче «designer extras», но это **самостоятельный structural change**, который должен иметь отдельный severity. Designer удалил методически legal divider потому что «paraphrased s10».
4. **Orchestrator failure modes** — Категория F «Coordination» назвается, но это per-pipeline, а не per-orchestrator. Нет анализа моих собственных решений (выбор tools для s09 v3 — я выбрал MCP+Llama-3, user отверг как «не прорывы»).
5. **Build approach — python-pptx-direct vs MCP** упомянуто в §6.1 как «New observation», но не как структурное решение. Текущие 7 build scripts + 6 iter-logs = legacy от итераций. Нет policy.
6. **Snapshot bloat (562 PNG, 71MB) → P2** — это P0 для масштабирования на 17 лекций (1.2GB). Reflection даёт правильный масштаб, но недооценивает severity.
7. **«Приложение-робот» → «Приложение в режиме автоматизации»** — terminology прошла **3 stages** (drift): chapter v3 «Приложение-робот» → consistency-check «3 формы» → speech v3.1 «Приложение в режиме автоматизации». Reflection упомянул как 1 случай, но это паттерн «critic-driven terminology rename», который сам создаёт drift.
8. **Hooks / automation absence** — нет упоминания о возможных pre-commit hooks для grep-валидаций (англицизмы, term consistency, footer-tax). Сейчас всё ad-hoc.
9. **Critic-driven s14 deletion разница от designer-driven** — s14 удалён designer, но Pearl/ARC-AGI были добавлены critics ранее. Нет отдельной категории «critic-driven additions/deletions» — это разные failure modes.
10. **Output-format errors самих critics** (fact-checker не сохранил отчёт как файл, consistency-checker аналогично) — упомянуты, но не как root cause: **subagent инструкции не enforce save**. Reflection предлагает «add to prompt», но не указывает, что это **systemic** — затронет все будущие critic runs если не зафиксировать сейчас.
11. **3 раунда user feedback пришли через ~5 часов каждый раз. Wall clock 14 hours** — significant cost. Reflection не оценивает «во сколько обходится 1 user revision round» (token cost + wall clock + frustration risk). Нет ROI calculation для preventive measures.
12. **Reflection sсам себя не позиционирует как living document** — нет link на Issue #70/EPIC #64.D follow-up, нет «next reflection date», нет feedback loop. Tag «Готово для review user'ом + переход к implementation» — хороший но недостаточный.

### Overall completeness score
**6.5/10.** Покрывает 60-70% реальных failure modes. Структурные правильно. **Visual + WPM + orchestrator самокритика + automation gap — ~30% объёма должно быть, ~5% есть.**

---

## Missed failure modes (15 specific items)

1. **WPM regression в speech v3.2 не помечена как P0.**
   - REQUIREMENTS.md DoD прямо требует «Все speech fragments WPM ≤ 95».
   - Speech v3.2 final имеет s07/s09/s17 на 102-107 WPM (8 из 10 changed slides ≤97).
   - Reflection §3.2 (speech-writer failures) не упоминает WPM regression.
   - **Severity:** P0 — methodology DoD violated в final artefact, никто не поднял.
   - **Why missed:** Reflection focused на content failures; numerical pacing thresholds не отмечались как reflection scope.

2. **s14 deletion designer-driven, не user-driven — не отделено как failure mode.**
   - Fix-17 (Unified nav slides) → designer решил, что s14 «paraphrased s10» → удалил.
   - User не просил удалять s14 (REQUIREMENTS.md в §1 не упоминает).
   - Reflection упоминает как «designer extras», но удаление — обратный знак относительно «extras».
   - **Severity:** P1 — structural change без user approval.
   - **Why missed:** Reflection поленился разделить «added by designer» vs «removed by designer».

3. **5 параллельных designers — coordination issues упомянуты, но нет дополнения «file ownership map».**
   - Reflection §3.1 Failure 3 упомянет «PPTX file lock conflicts» и «build script monolithic».
   - Реальная проблема — все правят `build_lec01_v31.py`. Нет git branch per designer, нет slide-id ownership.
   - Reflection P1-5 («Per-designer file ownership») — без deliverable: «explicit list slide-IDs» — но не описано как enforce (skill hook? CLAUDE.md rule?).
   - **Severity:** P1 — повторится для Л2 если designer'ы спавнятся parallel.

4. **Orchestrator-инициатива в s09 v3 (выбор Llama-3 + MCP) — не критикуется.**
   - User в round 3 #8: «убрать Llama-3 + MCP, добавить OpenClaw + Kimi K2.5».
   - Llama-3 + MCP попали в s09 v3 потому что **я (orchestrator) посчитал их «прорывами»** в Phase 12.3.
   - User: «Llama-3 — Meta уже большая лаба, MCP — infra protocol, weak narrative» — fundamentally orchestrator picked wrong examples.
   - **Severity:** P1 — orchestrator self-critique missing.
   - **Why missed:** reflection боится назвать orchestrator-failure как orchestrator-failure (атрибутирует designer'у).

5. **Proactive freshness check от orchestrator не делал.**
   - User вручную делал web search → сказал про OpenClaw / Kimi K2.5.
   - Я (orchestrator) мог сделать `WebSearch "AI breakthroughs 2025-2026 open source"` ДО designer spawn, и сразу получить свежие примеры.
   - **Severity:** P0 — root cause «outdated examples» = orchestrator не проактивен.
   - **Why missed:** reflection переложил на fact-checker (P1-3), но реальная роль — orchestrator's pre-spawn research.

6. **«Приложение-робот» → «-автоматизация» → «в режиме автоматизации» — рассматривается как 1 drift, но это pattern «critic-driven rename».**
   - Iteration: chapter v3 «Приложение-робот» (book-editor) → consistency-checker П1 P1: «3 формы» → speech v3.1 unified «в режиме автоматизации» (speech-writer applied critic-suggested form, не original).
   - Каждый critic round может tweak terminology — без freeze это идёт навечно.
   - **Severity:** P1 — нет «term lock» protocol после chapter approval.
   - **Why missed:** reflection видит drift как 1 проблему, не как pattern «critics могут предлагать relabeling без полного понимания».

7. **562 PNG snapshots в repo — bloat scaling math не сделана, severity занижена.**
   - 71MB × 17 лекций × 1-3 ребилда = 1.2-3.6 GB только snapshots.
   - Plus каждая лекция получит дополнительные iterations при правках.
   - GitHub max repo рекомендация ≤1GB, soft.
   - **Severity:** P0 для масштабирования; reflection дал P2.
   - **Why missed:** focus на «сейчас работает», not «через 6 лекций будет проблема».

8. **Build script proliferation — 7 scripts, 6 iter-logs.**
   - `build_lec01_full.py`, `_v2.py`, `_v3.py`, `_v31.py`, `_full_v4.py`, `_full.py`, `build_v36.py`.
   - Reflection говорит «consolidate», но не объясняет **policy для будущих лекций**: 1 script + git branches? 1 script + version variables?
   - Risk: Л2 начнёт с copy-paste `build_lec01_v31.py` → `build_lec02_v3.py` → snowball.
   - **Severity:** P1 для Л2.

9. **Snapshots stored in `library/lectures/lec-01/rendered/snapshots/` (in repo) vs build artefacts policy.**
   - Аналогично #7. PowerPoint MCP build = ephemeral. Snapshots = build artefact, должны быть в `.gitignore` целиком (включая финальные `sNN.png` если они тоже могут быть rebuilt).
   - Reflection P2-1 говорит «снапшоты в gitignore (iter*.png only)» — а финальные `sNN.png` остаются. Это compromise но без обоснования.

10. **Pre-USER-GATE walkthrough — ROI и feasibility не оценены.**
    - Reflection P0-2 предлагает orchestrator делать «30-минутный visual sweep + read-aloud».
    - 30 минут × 3 USER GATEs × 17 лекций = 25.5 hours per course of pre-gate review.
    - Может быть стоит автоматизировать через automated check skill вместо manual?
    - Reflection «Открытые вопросы #1» правильно поднял вопрос, но без альтернатив (e.g. «sub-orchestrator agent — pre-gate-reviewer»).

11. **Methodology-critic не имел «freshness» check для AI tools/benchmarks.**
    - Reflection §3.4 Failure 1 упомянет «curriculum relevance» — но не «temporal relevance».
    - Любая лекция о AI имеет данные, которые устаревают за дни/недели. Это **systemic** для курса.
    - **Severity:** P0 — без freshness check каждая лекция начнёт сесcession с user замечанием «эти примеры устарели».
    - **Why missed:** reflection выделил как «P1 freshness в fact-checker», но это должно быть в methodology-critic тоже (relevance = currency).

12. **Reader-simulator (rendered) не сделал «не self-contained» = «недопустимо» severity.**
    - Reflection §3.9 Failure 1 говорит «28/34 self-contained — number грew, OK».
    - Но 6 не-self-contained слайдов означают, что 18% deck'а **не работает для самоподготовки**.
    - Для лекции которая показывается раз в семестр и потом студенты пересматривают — это P0.
    - **Severity:** P0 — reflection дал «structural improvement assessment missing».
    - **Why missed:** reflection воспринимает rising number как progress без absolute threshold.

13. **TaskCreate / TaskUpdate / TaskList не использованы proactively.**
    - Reflection §7.3 упомянет «не systematically обновлял in_progress / completed».
    - На самом деле **TaskList tool вообще не использовался** — это видно из transcript: orchestrator делал inline plans.
    - User не видел progress tracking → каждый user message включал «что мы делаем сейчас?» вопрос.
    - **Severity:** P1 — UX failure для user.

14. **«Speaker notes контракт» — DoD только через reader-simulator.**
    - Reflection P0-1 даёт DoD «reader-simulator (mode=rendered) ≥ 26/N self-contained».
    - Но reader-simulator уже не дал поднять «28/34 не достаточно». Self-loop.
    - Нужен **independent DoD** — например word count + grep на «Assertion слева, donut справа» pattern + sample 3 слайдов проверка человеком.
    - **Severity:** P1 — DoD не enforceable если только через критик, который сам blind to threshold.

15. **«Iteration log» format не стандартизован.**
    - 6 iter-logs (v2, v3, v31, v32, v34, v4, no-suffix). Каждый разный.
    - Reflection §8.3 «merge to one rolling log» — без template для будущих лекций.
    - Risk: каждый designer создаёт own log → cross-lecture comparison не возможна.
    - **Severity:** P2 для Л1, P1 для course audit trail.

---

## Unactionable items → concretize

| # | Reflection language | Problem | Concrete action |
|---|---|---|---|
| 1 | «Pre-USER-GATE walkthrough by orchestrator» (P0-2) | «делает 30-минутный visual sweep» — без чек-листа | New skill `/pre-gate-review {phase}` который spawn'ит pre-gate-reviewer subagent с pinned checklist (PNG scan + notes read + speech read + N=10 issues output) |
| 2 | «Schema readability checklist в presentation-designer.md» (P0-3) | Per-schema bullets есть, но нет definition «5-second test» как процедуры | Designer DoD: «attach screenshot + answer in chat: did you understand main message in 5 sec? If no — redo». Critic verification: same question, same threshold. |
| 3 | «Curriculum relevance check в methodology-critic.md» (P0-4) | Question есть, но нет threshold «когда удалять» | Add severity matrix: «if Bloom ≥ Synthesis & lecture = introductory → RECOMMEND DELETE. Если Apply & introductory → REVIEW. Если Understand-Apply & introductory → KEEP». |
| 4 | «Designer no-extra-content rule» (P0-5) | «do nothing not in task brief» — abstract | Concrete enforcement: critic-presentation runs grep на designer output vs task brief deliverables list, любое addition flagged P1. |
| 5 | «Terminology drift sub-check» (P1-1) | «list watched terms» — но кто составляет? | Each lecture chapter v1 done → orchestrator generates `watched-terms.yaml` с топ-20 неологизмами; consistency-checker запускается per artifact с этим файлом. |
| 6 | «Verdict scale recalibration» (P1-2) | «If 5+ P1 — verdict = REVISE» — но critics уже сейчас не ставят правильно | Add to each critic agent prompt: «Output line 1 MUST be: VERDICT: REJECT / REVISE / APPROVE-WITH-POLISH / APPROVE-CLEAN. Counter check: if you wrote ≥5 P1 issues but said APPROVE — STOP, change to REVISE». |
| 7 | «Per-designer file ownership» (P1-5) | «каждый получает explicit list slide-IDs» — но кто проверяет что не пересекаются? | New skill `/spawn-designers {slide-id-map}` — orchestrator выдаёт map, skill validates non-overlap, spawns parallel agents с individual prompts containing «НЕ трогать s07-s11». |
| 8 | «Pre-flight checklist sync со deck» (P1-6) | «auto-generated на основе deck.yaml» — но нет реализации | Skill `/regenerate-pre-flight {lec-id}` → reads deck.yaml, regenerates speech.md preflight section. Add как post-deck-edit hook. |
| 9 | «consistency-checker запускается до каждого USER GATE» (P1-7) | Когда — в Phase 4, 7, 10? | Move к gate logic: USER GATE A (chapter) → consistency-checker mode=chapter-only; GATE B (slides) → chapter+slides; GATE C (final) → all 3. Document в lecture-production/README.md как Phase Gate Protocol. |
| 10 | «Session-end save mandate для всех critic agents» (P1-8) | «Before completing, MUST save report as file» — но если save fails? | Добавить retry logic в prompt: «Save → if Permission denied → call Bash to verify path exists → retry Write → if still fails STOP and request orchestrator». |
| 11 | «PowerPoint MCP fork» (P2-5) | «invest 2-3 часа» — нет ROI оценки | Estimate: list_shapes + update_shape_position сэкономит ~3-5 min per visual iter × 14 iter × 17 lectures = 12-20 hours. Fork = 3 hours one-time → 4× ROI. Decision: do it now. |
| 12 | «Snapshots в .gitignore» (P2-1) | Какие snapshots — все, или только iter? | Policy: gitignore `**/snapshots/iter*.png` AND `**/snapshots/fix*.png`. Keep `**/snapshots/sNN.png` финальные. Or — gitignore все, derive from PPTX on demand. **Recommend latter** — финальные тоже могут быть rebuilt. |

---

## Risk Лекции 2 (если внедрить только то что в reflection)

### Risk 1 (P0): WPM violations повторятся
- Speech v3.2 final имел s07/s09/s17 102-107 WPM, прошли как «8 из 10 OK».
- В reflection нет mention этой violation → speech-writer для Л2 повторит pattern.
- **Mitigation:** Add hard rule в speech-writer.md: «WPM > 95 на любом fragment = P0, не submit. Trim content или split slide».

### Risk 2 (P0): Visual iteration explosion
- Л2 Phase 12.4 будет 14+ iter если каждый visual issue ловить только в visual-loop.
- Reflection P0-3 (schema checklist) — частично, но не предотвращает «schema redesign 3 раза» (s11/s13/s16/s21 in Л1).
- **Mitigation:** Pre-design wireframe phase — designer **рисует sketch ASCII/draw.io** перед PPTX render, orchestrator approve.

### Risk 3 (P0): Designer-added содержимое
- «Лектору» секция, «Вы здесь» маркеры, subtitle, s14-deletion — все designer initiative.
- Reflection P0-5 правильно идентифицирует, но enforcement — только в prompt («do nothing extra»).
- Designer-Opus-4.7 может игнорировать, если задача формулируется «улучши слайд».
- **Mitigation:** Make designer brief = strict checklist «modify these N items, leave others untouched». No general «улучшать».

### Risk 4 (P0): User pre-gate review гонит цикл
- 3 user feedback rounds = ~3 hours user wall time.
- Reflection P0-2 предлагает orchestrator pre-gate review, но не оценивает feasibility.
- Если orchestrator не дисциплинирован — снова 3 rounds.
- **Mitigation:** Hard rule в CLAUDE.md: «NEVER present USER GATE без explicit orchestrator pre-review report. Format: «Я просмотрел N слайдов, нашёл K issues, фиксанул M, остался L»».

### Risk 5 (P1): Tools/benchmarks freshness регрессия
- Л2 «Как работают современные большие модели» — критически зависит от свежих ARC-AGI / MMLU / HumanEval / agentic benchmarks.
- Reflection §6.2 / P1-3 даёт fact-checker «freshness verification» — но это **post-fact**.
- К моменту user review — уже выкатили draft с устаревшими цифрами.
- **Mitigation:** Pre-design phase: orchestrator делает `WebSearch "{benchmark} 2026 latest"` ДО chapter draft. Required для AI-domain контента.

### Risk 6 (P1): Terminology rename циклы
- Л2 будет иметь много новых терминов (токен, эмбеддинг, attention, temperature).
- Без term lock после chapter approval — каждая critic round может suggest rename → speech-writer apply → designer apply → drift.
- **Mitigation:** Phase 4.5 — orchestrator freezes glossary `lec-NN/glossary.yaml` после chapter approve. Все downstream artefacts MUST use exact terms из glossary. Critics MAY flag inconsistency, MAY NOT suggest rename.

### Risk 7 (P1): Build script proliferation
- Л2 начнёт `build_lec02.py` копирование из v31. Через 5 итераций — `build_lec02_v3.py` + 5 iter-logs.
- **Mitigation:** Template policy — `tools/lecture-production/lecture-template/` директория с canonical `build.py` + iteration-log.md template + .gitignore. Each new lecture copy template, NOT old lecture.

### Risk 8 (P2): Repo bloat (snapshots × 17 lectures)
- Без gitignore = 1.2-3.6 GB repo за курс.
- **Mitigation:** gitignore policy сейчас, до Л2.

---

## Дополнительные рекомендации (не в reflection)

1. **Orchestrator self-evaluation block в reflection.** Каждая reflection MUST include section «Orchestrator decisions retrospective»: list 3-5 orchestrator-level decisions (subagent spawning, timing, tool selection) + assess each. Текущий reflection трактует orchestrator как невидимого.

2. **Pre-design wireframe для нетривиальных слайдов.** Любой слайд с custom schema (matrix, quadrant, cycle, layered, pipeline) — designer **сначала рисует ASCII или mermaid wireframe**, orchestrator approves, **потом** PowerPoint MCP render. Это снимет 50%+ visual iterations.

3. **Glossary lock после chapter approve.** Phase 4.5 — orchestrator generates `lec-NN/glossary.yaml` из chapter, freezes. Downstream agents MUST use exact terms. Критики MAY flag inconsistency, MAY NOT propose rename без USER approval.

4. **Tool/benchmark freshness pre-check skill.** New skill `/freshness-check {lec-NN}` runs WebSearch на список benchmarks из chapter; outputs «outdated entries report». Mandatory ДО Phase 12.4 (designer spawn).

5. **Iteration cap с automatic escalation.** Visual loop > 7 iter на 1 слайд = STOP, escalate to user с PNG + «we tried X approaches, none worked, what to do?» Сейчас designer бесконечно tries.

6. **Designer brief strict format.** Brief MUST be explicit YAML:
   ```yaml
   modify:
     - s07: change timeline events from 12 to 9
     - s09: replace Llama-3 with OpenClaw
   leave_untouched: [s01-s06, s08, s10-s28, s30-s33]
   forbidden_additions: [subtitle, navigation marker, лектору section]
   ```
   Designer любое отклонение от modify-list = P1.

7. **Pre-USER-GATE skill вместо manual orchestrator review.**
   ```
   /pre-gate-review {phase}
   ```
   Skill spawns pre-gate-reviewer subagent с automated PNG scan + grep validations + word count + reads.
   Output: «Found 12 issues. Fixed 8 quick. Remaining 4 — need user judgement: [list]».
   Это даёт ROI (auto vs 30 min manual) + reproducibility.

8. **Snapshots policy: gitignore ALL, derive on demand.** Финальные `sNN.png` тоже rebuilt из PPTX через libreoffice. Не commit → repo size flat.

9. **Build script consolidation: lecture-template directory.** `tools/lecture-production/lecture-template/build.py` — canonical builder. Each lecture copies, not old lecture. Avoids snowball.

10. **Reflection-on-reflection automation.** Skill `/roast-reflection {file}` — спавнит methodology-critic с roast prompt. Каждая reflection должна пройти roast перед implementation. (Эта задача — proof-of-concept.)

---

## Финальная implementation priority

### P0 (must-have перед Л2 — risk блокирует quality result)

1. **WPM hard rule в speech-writer.md** — refuse output если любой fragment > 95 WPM.
2. **Designer brief strict YAML format** — modify/leave_untouched/forbidden_additions.
3. **Pre-design wireframe для schema slides** — ASCII/mermaid sketch ДО PowerPoint render.
4. **Tool freshness pre-check skill** — orchestrator runs ДО Phase 12.4 для AI-domain content.
5. **Pre-USER-GATE skill** (auto, не manual) — replaces manual 30-min sweep.
6. **Glossary lock после chapter approve** — Phase 4.5, freeze terms.
7. **Speaker notes contract** в playbook + DoD = independent (не reader-simulator-only).
8. **Snapshot gitignore policy** — gitignore all, build on demand.
9. **Verdict scale enforcement в critic agents** — output line 1 = VERDICT, counter check.
10. **Critic save-report mandate с retry** — explicit Write + Bash verify в prompt.

### P1 (should-have — снизит revision rounds на ~40%)

1. **Orchestrator self-evaluation block** в reflection template.
2. **Per-designer file ownership skill** (`/spawn-designers`).
3. **Curriculum relevance threshold matrix** в methodology-critic.
4. **Term-rename freeze** после chapter approval (critics flag, не suggest rename).
5. **Build script template** в `tools/lecture-production/lecture-template/`.
6. **Iteration cap (7 iter → escalate)** в visual loop.
7. **Reader-simulator absolute threshold** (e.g. ≥30/33 self-contained, не «better than v2»).
8. **TaskList proactive use** — orchestrator MUST update todo per phase.
9. **Schema wireframe library** в `tools/presentation-build/wireframes/` (canonical ASCII for matrix/quadrant/timeline/cycle/layered/pipeline).

### P2 (nice-to-have — quality of life)

1. **Iteration log template** standardization.
2. **QA-reports directory schema** unification.
3. **Reflection-on-reflection automation** (`/roast-reflection`).
4. **PowerPoint MCP fork** (list_shapes + update_shape_position) — high ROI but one-time engineering work.
5. **Build script consolidation** for Л1 (cleanup, не блокирует Л2).
6. **workspace-mcp OAuth → production status** (admin task).

---

## Финальный verdict

Reflection — **good first draft, not implementable as-is**. Имплементировать только P0/P1 из reflection даст ~40% улучшения. Чтобы дойти до 80% («Л2 проходит за 1 user feedback round»), нужно покрыть **15 missed failure modes** + **8 unactionable → concretize** + **9 дополнительных рекомендаций** этого roast'а.

**Самая главная gap которую отметил сам user:** «много правили визуал, но не вижу в рефлексии». Это not metaphorical — буквально 14 visual loop iterations + 5 параллельных designer batches за 1 wall-day производства не отражены в самокритике. Reflection видит структурные failures (LO coverage, terminology), но **слепа к visual production process** — а это ровно то, на что user тратил больше всего времени критики.

**Recommendation для следующего шага:** orchestrator должен взять этот roast как input, обновить REFLECTION.md (или создать v2), и **тогда** идти в implementation. Иначе implementation будет fixить только то, что reflection видел.
