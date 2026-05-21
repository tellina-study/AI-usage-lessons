# Multi-artifact Lecture Production Pipeline

**Canonical doc** для сборки полной лекции (3 финальных артефакта). Любой агент, работающий над лекционным материалом, читает этот файл **первым**.

**Связан с** `tools/presentation-build/README.md` — он покрывает только slides-specific. Этот README — **полный пайплайн**, slides — одна из фаз.

---

## 1. Финальные артефакты (3 на каждую лекцию)

```
library/lectures/lec-NN/
  chapter.md              ← глава методички ≥30k слов для L4+ (academic)                  [PRIMARY = source of truth]
  chapter-part2.md        ← multi-part split при >600 строк (CLAUDE.md doc-size-limit)
  chapter-part3.md        ← при ≥30k обычно 3 части по 6 500–8 500 слов; >1200 строк суммарно — split продолжать
  rendered/lec-NN.pptx    ← презентация со speaker notes для студентов                    [DERIVED from chapter]
  speech.md               ← речь лектора ~4-6k слов (conversational)                       [DERIVED from chapter + slides]
```

**Source of truth:** `chapter.md`. Slides и speech derive из неё. При conflict — fix slides/speech, не chapter (если chapter сам не ошибается).

**L4+ chapter mandatory ≥30 000 слов** (target 30k ±5% = 28 500–31 500). Issue #128 + memory `feedback_chapter_depth`. См. CLAUDE.md § «Chapter Depth Baseline (ENFORCED)». L1–L3 introductory — 8–12k acceptable с owner waiver.

---

## 2. Промежуточные артефакты

```
library/lectures/lec-NN/
  deck.yaml               ← структура слайдов (см. tools/presentation-build/README.md)
  slides/
    sNN-*.md              ← per-slide content (assertion + visible + speaker notes)
  rendered/
    snapshots/sNN.png     ← визуальные снапшоты
    iteration-log.md      ← лог визуального цикла
    assets/               ← icons, charts, diagrams, illustrations
  qa-reports/
    {YYYY-MM-DD-vN}/
      methodology-critic.md
      fact-checker.md
      reader-text-only.md
      presentation-critic.md
      student-simulator.md
      reader-rendered.md
      consistency-checker.md
      SYNTHESIS.md
```

И **в репо вне library/**:
- `notes/lecture-N-review/final/new-plan-vN-final.md` — narrative план (input для chapter).
- `notes/research/lecture-N/*.md` — research notes (источники, факты).

---

## 3. Workflow (11 фаз + 3 USER GATEs A/B/C)

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1 — Plan critique                                         │
│ Agents: methodology-critic + reader-text-only (на v4 plan)      │
│ Output: notes/lecture-N-review/{date}/critique-of-vN.md         │
├─────────────────────────────────────────────────────────────────┤
│ Phase 2 — Chapter draft                                         │
│ Agent: book-editor                                              │
│ Output: library/lectures/lec-NN/chapter.md (status=draft)       │
├─────────────────────────────────────────────────────────────────┤
│ Phase 3 — Chapter critique                                      │
│ Agents (parallel): methodology-critic + fact-checker +          │
│                    reader-simulator mode=text-only              │
│ Output: 3 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4 — Chapter revision (book-editor) → finalize             │
│ Status: draft → reviewed → finalized                            │
│ ENFORCED: full citation sweep на revised chapter (не subset).   │
│   Subset reruns acceptable только для P0 verification ПОСЛЕ     │
│   full sweep — иначе inherited fact drift в slides (Лекция 9    │
│   lesson: Du→Ye + CENTCOM→EUCOM пропущены subset rerun).        │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=chapter)                            │
│ Steps: read chapter as student, find P0/P1 NOT caught by critics│
│ Outcome: fix P0/P1 BEFORE presenting GATE A                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE A — chapter approved                                │
│ Criteria: pre-gate walkthrough INCLUDED reading test            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 5 — Slides update from chapter                            │
│ Agent: presentation-designer (refine deck.yaml + slides/*.md)   │
│ Update assertions / learning_goals из chapter                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 6 — Slides design + visual loop                           │
│ Agent: presentation-designer (visual-loop min 3 / max 7 iter    │
│   per slide, escalate at iter 7)                                │
│ See: tools/presentation-build/README.md §5, §5.5, §5.6          │
├─────────────────────────────────────────────────────────────────┤
│ Phase 7 — Slides QA                                             │
│ Agents (parallel): presentation-critic + student-simulator +    │
│                    reader-simulator mode=rendered +             │
│                    consistency-checker (chapter ↔ slides) +     │
│                    fact-checker (если данные на slides)         │
│ Output: 5 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 8 — Slides revision → finalize                            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 8.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=slides)                             │
│ Steps: visual sweep all PNGs + read 5-7 random speaker notes +  │
│   designer-extras grep + checklist (schemas, terminology, etc.) │
│ Outcome: fix P0/P1 BEFORE presenting GATE B                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE B — slides approved                                 │
│ Criteria: pre-gate walkthrough INCLUDED visual sweep            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 9 — Speech draft                                          │
│ Agent: speech-writer (из finalized chapter + slides)            │
│ Output: library/lectures/lec-NN/speech.md (status=draft)        │
├─────────────────────────────────────────────────────────────────┤
│ Phase 10 — Speech critique + consistency check                  │
│ Agents (parallel): methodology-critic (speech-specific) +       │
│                    fact-checker (на speech) +                   │
│                    consistency-checker (chapter ↔ slides ↔ speech)│
│ Output: 3 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 11 — Speech revision → finalize                           │
├─────────────────────────────────────────────────────────────────┤
│ Phase 11.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=final)                              │
│ Steps: cross-artifact consistency grep + pre-flight checklist   │
│   actionability + cornerstone concepts alignment                │
│ Outcome: fix P0/P1 BEFORE presenting GATE C                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE C — final approval (всё 3 артефакта)                │
│ Criteria: pre-gate walkthrough INCLUDED cross-artifact grep     │
└─────────────────────────────────────────────────────────────────┘
```

**Каждый USER GATE — explicit approval.** Не двигаться к следующей фазе без него.

### USER GATE criteria (явно)

| Gate | Что approve | Pre-gate walkthrough mode | Что обязательно сделано |
|---|---|---|---|
| **GATE A** | chapter.md (status=reviewed) | `/pre-user-gate mode=chapter` | Reading test: orchestrator прочитал главу как студент, найдены P0/P1 (relevance, terminology, factual, reading flow), исправлены ДО presenting user. |
| **GATE B** | slides (deck.yaml + slides/*.md + rendered/lec-NN.pptx + snapshots) | `/pre-user-gate mode=slides` | Visual sweep: открыты все PNG, проверена schema readability + designer-extras grep («Лектору», «Вы здесь», тайминг, subtitle) + speaker notes sample read + checklist (palette, gold ≥1×, footer-tax 0, англицизмы 0). |
| **GATE C** | final 3 artifacts (chapter + slides + speech) | `/pre-user-gate mode=final` | Cross-artifact consistency grep: cornerstone концепты aligned (central question, ключевые термины, числа, attributions, roadmap), terminology unified, pre-flight в speech actionable + 0 orphan refs к удалённым slides. |

**Принцип pre-gate walkthrough:** «critics проходят там, где user отклоняет» (Лекция 1 v3 had 3 user feedback rounds после critic-approve). Pre-gate walkthrough — orchestrator-level self-review, который дублирует user-perspective и ловит P0/P1 ДО formal gate'а. См. `.claude/skills/pre-user-gate/SKILL.md`.

---

## 3.5 Cascade-of-changes tracking (ENFORCED)

Когда меняется content одного artifact, downstream artifacts могут разъехаться. Orchestrator **обязан** трекать cascade и автоматически проверять impact.

### Триггеры cascade-check

| Изменение | Что грепать downstream |
|---|---|
| **Slide rename** (sNN-old-id → sNN-new-id) | speech.md, chapter.md, other slides/*.md, qa-reports — на старый ID |
| **Term renaming** (например, «Приложение-робот» → «AI-приложение») | grep по всем 3 artifacts; consistency-checker пересчитать |
| **Roadmap shift** (модули программы курса reshuffle) | chapter §intro, slides «карта курса», speech «карта курса», `catalog/manifests/lectures.yaml` |
| **Slide deletion** | speech pre-flight checklist (orphan refs!), other slides «callbacks к sNN», chapter §«ссылки на материал» |
| **Chapter section restructure** | slides assertions (если sourced from chapter §X), speech pacing (если глава была reference для timing) |

### Workflow cascade-check

1. **Detect change** — orchestrator замечает diff в одном из 3 artifacts.
2. **Auto-grep** — orchestrator (или pre-user-gate skill) grepает downstream на старые references.
3. **Report cascade list** — список найденных «orphan / stale» references → revision agent (book-editor / presentation-designer / speech-writer) фиксит.
4. **Re-run consistency-checker** — после revision sync verifies.

**Якорь правила:** speech v3 в Лекции 1 имел orphan reference на удалённый s26 (ARC-AGI слайд) — consistency-checker поймал как P0 на финальной фазе. Если бы cascade-check работал на этапе deletion — поймали бы сразу.

---

## 3.6 AI-Failure & Judgment Content Check (ENFORCED ≥30%)

**Источник правила:** `CLAUDE.md` § «AI-Failure & Judgment Content Rule» (single source of truth — здесь только enforcement-механика, текст правила не дублировать).

Каждая лекция: **strict-in ≥30%** содержания — провалы ИИ + выученные уроки, фундаментальные ограничения/риски, явные критерии «здесь ИИ не нужен», или сравнение с более правильным альтернативным инструментом. Измерение **холистическое + strict-in**: доля ≥30% видна **в каждом из 3 артефактов** (chapter / slides / speech) отдельно. Засчитывается только **полностью** in-bucket контент — частично-bucket блоки и общие оговорки идут как out (решение #78, 2026-05-15: strict-in, не weighted).

| Где проверяется | Кто | Триггер провала |
|---|---|---|
| Phase 1 — plan | `methodology-critic` + orchestrator | план не выделяет ≥30% бюджета на failure/judgment → REVISE плана |
| Phase 3 — chapter | `methodology-critic` | <30% слов chapter в bucket'е → REVISE |
| Phase 7 — slides | `methodology-critic` | <30% слайдов/минут в bucket'е → REVISE |
| Phase 10 — speech | `methodology-critic` | <30% речи в bucket'е, либо доля только в chapter → REVISE |
| GATE A/B/C | orchestrator (`/pre-user-gate`) | failure-share check не пройден → NOT present GATE |

**Не засчитывается:** общие дисклеймеры, однострочные оговорки без урока/критерия/альтернативы, «магическая пилюля + будьте осторожны». Counter-check: <30% или single-artifact concentration = структурный gap (REVISE), не polish.

### Owner waiver — реестр (только L1–L3, решение #82)

Для вводных лекций **L1–L3** владелец может явным решением снять ≥30%. Waiver действует **только если записан в таблице ниже** со ссылкой на issue. `methodology-critic` для L1–L3 с записанным waiver: strict-in <30% → informational note «WAIVED», НЕ P0/REVISE. **L4–L17 — waiver недоступен.**

| Лекция | Класс | Waiver | Issue | Дата |
|---|---|---|---|---|
| Лекция 1 | introductory (L1–L3) | ✅ granted (owner) | #82 (закрыл #80) | 2026-05-15 |
| Лекция 2 | introductory (L1–L3) | ✅ granted (owner) | #82 (закрыл #81) | 2026-05-15 |

---

## 3.7a Anonymization mandate (ENFORCED — Лекция 9 lesson 2026-05-21)

**Источник:** рефлексия Лекции 9 (#118), user explicit feedback «убери конкретные ссылки на специальности и кафедры».

Все 3 артефакта (chapter / slides / speech) обезличены:
- Frontmatter `audience`: «студенты-инженеры 3 курса (универсальная)» — НЕ ИУ6 / МГТУ / Бауман
- Career section в родовой форме: «профильные технические университеты + военно-космические академии»
- 0 named institutions: МГТУ / Бауман / ИУ-N / Кафедра «...» / ВКА им. Можайского / МАИ / СПбГУ / bauman.ru / vka.mil
- Эталон pattern: lec-03 / lec-05 / lec-07 — 0 named institutions; lec-06 — единственная generic «профильные кафедры»

**Cost-of-omission:** Lec-09 v2 потребовала 1 revision cycle (v2→v3) anonymization. Lec-10+ — apply by default, не require user-intervention.

## 3.7b Russification (anti-anglicism) mandate (ENFORCED — memory rule `feedback_russification`)

Все 3 артефакта visible body Russified. Whitelisted: brand names + tech acronyms с RU расшифровкой при первом упоминании.

**Producer agents** имеют embedded mandate в `.claude/agents/book-editor.md`, `speech-writer.md`, `presentation-designer.md` — orchestrator не обязан повторять в каждом spawn brief.

**Pre-submission self-grep** обязателен для speech-writer (см. `.claude/agents/speech-writer.md` § ENFORCED Anti-anglicism mandatory pre-submission self-grep).

**Pre-GATE deep latin-token scan** (broad regex + brand allowlist) — обязательный orchestrator-INDEPENDENT check перед GATE B/C; pattern-narrow grep маскирует depth (см. `tools/presentation-build/README.md` §5.8).

**Cost-of-omission lec-08+09:** speech v1 self-report «0 hits» при 107-186 реальных → caught Phase 10 critic → speech revision 2-3ч × 3 passes.

## 3.7c Plan-level mandates carry-forward (ENFORCED — Лекция 8 lesson)

**Phase 1 plan-checklist** обязан содержать (carry-forward instructions для downstream chapter / slides / speech):

- [ ] **Hero images plan для s01 + s39** — какие real images планируются (entity + источник + 6-tier acquisition strategy). См. [[hero-images-required]] + `tools/presentation-build/README.md` §5.9.
- [ ] **Russification mandate в plan v1 sam** — никаких anglicisms в plan itself; carry-forward instruction для chapter / slides / speech ([[russification]] + `tools/presentation-build/README.md` §5.8).
- [ ] **6-tier real image acquisition strategy** sketched per case-study slide — minimum 12-15 real images на типичный deck из 32-35 слайдов ([[no-mock-fallbacks]] + `tools/presentation-build/README.md` §5.7).
- [ ] **Anonymization carry-forward** — generic «студенты-инженеры 3 курса», без named institutions (см. §3.7a).
- [ ] **Anti-anglicism таблица** ссылается на canonical replacements (см. §3.7b).

## 3.7d Phase 5 (Deck design) acceptance additions (ENFORCED — Лекция 8 lesson)

**Deck spec acceptance criteria additions:**

- [ ] ≥80% media coverage requires **REAL images** (no mocks) per [[no-mock-fallbacks]]. Self-report «X% coverage» НЕ trustworthy без per-image source URL.
- [ ] **Hero s01 + s39 mandatory** per [[hero-images-required]] — ≥40% area, real image via 6-tier, attribution.
- [ ] **Russification mandate** в visible body + speaker notes per [[russification]] — pre-submission deep latin-token scan.
- [ ] **Per-slide media kind explicit** в `deck.yaml` (см. `templates/slide-outline.md` `media:` block) — acquisition_tier + source_url + attribution_label.

## 3.7e Phase 7.5 (Critic pass) additions (ENFORCED — Лекция 8 lesson)

**Critic checklists augmented:**

- **presentation-critic:**
  - [ ] «Mock vs real» check per slide claiming external screenshot — identifiable real source URL?
  - [ ] Russification deep scan на rendered PPTX visible body — 0 critical anglicism hits.
  - [ ] Hero check: s01 + s39 ≥40% area, real image, attribution visible.
- **student-simulator:**
  - [ ] Comprehension check assuming real images present (если slide claims «вот скриншот от NYT» — студент должен видеть actual NYT page, не abstract case name).
- **reader-simulator (mode=rendered):**
  - [ ] Deep latin-token scan на speaker notes + visible body — sample 5 random slides.
- **methodology-critic:**
  - [ ] Real-image-check (см. presentation-critic Check 12) на bucket-контенте (cases, failures) — abstract case names без real visual = pedagogical gap.

## 3.7f Pre-USER-GATE B walkthrough additions (ENFORCED — Лекция 8 lesson)

Explicit checklist (расширяет existing Pre-USER-GATE Walkthrough Rule в CLAUDE.md):

- [ ] **Deep latin-token scan на rendered pptx visible body** (broad regex + brand allowlist; не только narrow Russification таблица patterns) — `unique - whitelist = ∅` для narrative content.
- [ ] **6-tier image acquisition log per image** (no blanket mocks; если Tier 6/6 failed — ≥6 documented attempts).
- [ ] **Hero on s01** (≥40% area, real image via 6-tier, attribution visible).
- [ ] **Hero on s39** (≥40% area, real image via 6-tier, attribution visible).
- [ ] **Visual sweep: каждый «screenshot» claim — actual real source identifiable?** Sample 5 slides → identifiable real source URL? matches what source would show?
- [ ] **Stylized Ocean-palette card с verbatim headline ≠ real image** — это mock, FAIL.

**Если P0/P1 found — NOT present GATE.** Spawn revision, re-run pre-gate, потом present.

## 3.7 Self-reported метрики — critic re-verify (ENFORCED)

**Источник:** рефлексия Лекции 5 (#100), issue #111.

Producer-агенты (book-editor / presentation-designer / speech-writer) часто прилагают self-проверку метрики (WPM, strict-in %, word-count, pacing-sum, coverage-count) со скриптом. **Self-report НЕ является gate-сигналом.**

- Якорь: speech-writer Phase 9 Л5 заявил «все ≤95 WPM, PROVEN PASS» — фактически s28=100.3 (non-greedy баг скрипта producer'а); methodology-critic Phase 10 поймал → REVISE.
- Producer в отчёте помечает self-reported метрику как **«требует critic-ре-верификации»**, НЕ «PROVEN / zero-tolerance соблюдён».
- Если метрика погнала **REVISE** и revision-agent заявил fix → авторитетная ре-верификация = **focused re-spawn профильного critic'а** (узкий scope, методика Phase N), НЕ ad-hoc orchestrator-grep (тоже ненадёжен — Л5 Phase 11.5 orchestrator-WPM-скрипт дал s32=794). Механика — `.claude/skills/pre-user-gate/SKILL.md` Step 0.

---

## 4. Роли всех агентов (8 total)

### Производители (writers / builders)
| Agent | Что производит | Capabilities (NEW from Лекции 1 v3) | Phase |
|---|---|---|---|
| `book-editor` | `chapter.md` | Mark unverified specifics `[FACT-CHECK]`; cross-reference course structure (Drive doc) для footnotes; speaker-notes section markers `[for-slide-sNN]` | 2, 4 (revisions) |
| `presentation-designer` | slides/*.md adjustments + rendered PPTX + snapshots | **Schema Readability Checklist** per schema slide; **No-extra-content rule** (do nothing not in brief); **Speaker notes contract** (150-300 words readable text, NO layout descriptions); per-designer file ownership при parallel spawn; visual-loop max 7 iter с escalation | 5, 6, 8 |
| `speech-writer` | `speech.md` | Pre-flight sync с deck.yaml (auto-regenerate при slide deletions); англицизм cleanup pass; reference user-provided Drive docs | 9, 11 (revisions) |

### Критики (reviewers, read-only)
| Agent | Что проверяет | Capabilities (NEW) | Phase |
|---|---|---|---|
| `methodology-critic` | Pedagogical depth, LO coverage, sequence, assertion-evidence | **Curriculum Relevance check** («зачем в лекции N — introductory/intermediate/advanced?»); **Term canonical-validity** (insider phrasing detection); англицизмы в tone-analysis; designer-added content audit | 1, 3, 7, 10 |
| `fact-checker` | Цифры, даты, attribution, citations | **Freshness verification** (date of source + refresh cadence + verify-on-day-of-lecture для < 1 month); user-provided source documents (Drive); mandatory file save | 3, 7, 10 |
| `presentation-critic` | Визуал deck'а (overlap, contrast, hierarchy, anti-patterns) | **Schema Readability check** (mirror designer's checklist); cross-slide redundancy grep; **5-second teach test** для diagrams; updated verdict scale (REJECT / REVISE / APPROVE-WITH-POLISH / APPROVE-CLEAN) | 7 |
| `student-simulator` | Студент в зале (PNG + speaker notes) | **Explicit slides-to-delete recommendation** (P1-DELETE category) | 7 |
| `reader-simulator` | 2 mode'а: `text-only` (md без рендера) + `rendered` (PNG + notes через 2 нед) | **Structural blocker assessment** (mode=rendered: notes-fix vs structural cut) | 1, 3, 7 |
| `consistency-checker` | Chapter ↔ slides ↔ speech alignment | **Terminology Drift sub-mode** (`terminology-only`): grep по watched terms перед каждым USER GATE; runs Phase 4.5, 8.5, 11.5 (не только 10) | 4.5, 7, 10, 11.5 |

### Pre-USER-GATE walkthrough (orchestrator skill)

`/pre-user-gate` — orchestrator self-review skill, запускается перед каждым USER GATE (A/B/C). Дублирует user-perspective, ловит P0/P1 что critics miss. См. `.claude/skills/pre-user-gate/SKILL.md`.

---

## 5. Источники по теме

### Chapter authoring
- Russell & Norvig **AIMA** 4th ed — образец академического текста.
- Mayer's **Multimedia Learning Principles** — application для chapter ↔ slides split.
- **Bloom's taxonomy** — для калибровки LO levels.
- **Retrieval practice** — для self-check вопросов.

### Speech writing
- TED-talks transcripts (NPR-style) — для conversational pacing.
- Карнеги «Как выступать публично» — основы.
- Anthropic **pptx skill** § «assume there are problems» — applies to speech tooltipи.

---

## 6. Размер artifacts

| Артефакт | Длина | Pacing |
|---|---|---|
| `chapter.md` (L4+) | **≥30 000 слов** (target 28 500–31 500), multi-part 3-5 файлов по 6 500–8 500 слов; ~100-130 страниц A4 | Textbook chapter depth + Q&A backup + self-study reference; ~2-3 ч глубокого чтения; на лекции проходится 30-40%, остальное Q&A backup + self-study deep-dive |
| `chapter.md` (L1–L3 introductory) | 8–12k слов acceptable с owner waiver | Self-study, ~30-60 мин чтения |
| `slides/*.md` | ~150-300 слов на slide × 25-30 slides ≈ 5-8k слов суммарно | Visible content + speaker notes |
| `speech.md` | 4-6k слов (≈70-80 wpm × 75 мин) | Сliceful pacing, паузы, переходы |

**Chapter Depth Baseline (ENFORCED — см. `CLAUDE.md` § «Chapter Depth Baseline»):**
- L4–L17: **≥30 000 слов** mandatory, waiver недоступен; <28 500 слов → P0 BLOCKING REVISE (структурный gap, не polish; issue #128).
- L1–L3: 8-12k acceptable; ≥30k если owner explicit instruction.
- **Multi-part split mandatory при >600 строк per file** (CLAUDE.md «Document Size Limit»): `chapter.md` + `chapter-part2.md` + `chapter-part3.md`, cross-link через TOC.

**Что НЕ засчитывается в 30k:** frontmatter YAML, heading-only sections, TOC, Источники / bibliography (это отдельно).

**Старый red-flag «>15k» НЕ применять для L4+** — обновлено 2026-05-21 (issue #128).

---

## 7. Anti-patterns (cross-artifact)

1. ❌ **Chapter повторяет slides дословно** — chapter должен быть deeper / wider.
2. ❌ **Speech читает chapter** — speech conversational, не learning.
3. ❌ **Slides не покрывают LO chapter'а** — coverage gap.
4. ❌ **Drift между artifacts** — цифры не сходятся, tone разный, ссылки разные.
5. ❌ **«Магическая пилюля» tone** в любом из 3 — нарушение D5.
6. ❌ **Local audience binding** («инженер ИУ6») в chapter — она универсальная для переиспользования.
7. ❌ **Skip USER GATE** — каждый gate explicit.
8. ❌ **Single-pass без critic'а** — каждый артефакт должен пройти ≥1 critic перед финализацией.
9. ❌ **Lec-N-1 pattern divergence без explicit approval** (R2-R5 L2 production all stem from this).
10. ❌ **Hook outdated empirical test** (strawberry-type when 2026 models pass) — use 2026-evergreen.
11. ❌ **Missing fundamental concepts** (attention matrix, embedding space, end-to-end flow) — Missing-Fundamentals check.
12. ❌ **Artifacts only in temp worktree at GATE** — sync to main repo before opening.
13. ❌ **Branch contention from parallel session** — worktree isolation для multi-lecture parallel.
14. ❌ **Per-artifact spawns для polish** (separate designer + writer per phase) — use single batched revision agent.

---

## 8. Multi-Lecture Parallel Production Policy (ENFORCED после L2 lessons)

When starting Lec-N production while parallel session (Lec-N-1 или Lec-N+k) активна:

### Pre-conditions
- Identify parallel sessions: `git worktree list` shows other lectures in production
- Decide: same-session sequential ИЛИ separate worktree

### Worktree isolation (RECOMMENDED для parallel)

```bash
git worktree add --detach /tmp/lec-NN-wt <base-commit>
cd /tmp/lec-NN-wt && git checkout -b phase-X-Y
```

**All subsequent agent spawns:** include explicit `cd /tmp/lec-NN-wt FIRST` в prompt. Agent должен verify `git branch --show-current` returns `phase-X-Y`. If branch changes mid-session → STOP, report (don't recover).

### Branch ref management

After phase commits в worktree → `git update-ref refs/heads/issue-NN-lec-NN <commit-sha>` from main repo. This propagates branch HEAD без requiring main worktree checkout (avoids contention с parallel session).

### Pre-USER-GATE artifacts sync (MANDATORY — hardened)

**Silent-failure mode (Лекция 5 #100):** `cd /tmp/lec-NN-wt && … && cp src dst` оставляет cwd в worktree → `cp` получает **src==dst** («are the same file»), sync в main-repo **молча НЕ происходит**. Поймано только inode-check'ом перед GATE. Поэтому процедура ниже — ENFORCED, с обязательным пост-верификатором.

**Правила (нарушение = sync считается невыполненным):**
- **Абсолютные src И dst** в каждой `cp`. НИКОГДА `cd`-в-worktree в том же compound, где `cp` (cwd-relative dst разрешится в worktree → src==dst).
- Запускать sync **из main-repo cwd** (или вообще без `cd`), оба пути абсолютные.
- **Обязательный пост-верификатор** (inode-diff ИЛИ `rsync --checksum`) — без него sync НЕ считается выполненным.

```bash
SRC=/tmp/lec-NN-wt/library/lectures/lec-NN
DST=/home/levko/AI-usage-lessons/library/lectures/lec-NN
mkdir -p "$DST/slides" "$DST/rendered/snapshots"
cp "$SRC"/chapter*.md "$SRC"/speech.md "$SRC"/glossary.yaml "$SRC"/deck*.yaml "$DST/"
cp "$SRC"/slides/*.md "$DST/slides/"
cp "$SRC"/rendered/lec-NN.{pptx,pdf} "$SRC"/rendered/iteration-log.md "$DST/rendered/" 2>/dev/null
cp "$SRC"/rendered/snapshots/*.png "$DST/rendered/snapshots/" 2>/dev/null
```

**Verify before GATE opens (ОБА обязательны):**
```bash
ls -la "$DST"/rendered/lec-NN.{pptx,pdf}                              # существование
stat -c '%i' "$SRC"/chapter.md "$DST"/chapter.md                      # inodes ДОЛЖНЫ различаться = реальная копия
```
- `ls` отсутствует ИЛИ inodes совпадают (src==dst — sync не произошёл) → **STOP, do NOT open GATE**, пере-выполнить sync абсолютными путями.

(Memory rule: `feedback_pre_gate_render_artifacts.md`. Якорь hardening: рефлексия Л5, issue #112.)

### Final merge

After USER GATE C approval:
```bash
git push origin refs/heads/issue-NN-lec-NN:refs/heads/issue-NN-lec-NN
gh pr create --base main --head issue-NN-lec-NN --title ...
gh pr merge <PR#> --merge --delete-branch
```

### Worktree cleanup

```bash
git worktree remove /tmp/lec-NN-wt --force
```

---

## 9. Polish Round Pattern (после Phase 7 OR post-GATE feedback)

**Anti-pattern:** spawning separate designer/writer per-artifact для каждого feedback round (Lec-2 Phase 8.5 / 8.6 / 8.7 / 8.8 / 8.9 — 5 sub-iterations).

**Recommended pattern (proven Phase 11 efficient):** single batched revision agent doing 3-artifact touches:

- **book-editor** для chapter-heavy revisions (text content + chapter cross-refs)
- **presentation-designer** для slide-heavy revisions (visual + structural + deck.yaml)
- **speech-writer** для cross-artifact polish (speech + minor chapter/slide touches)

Brief должен включать:
- All critic reports (paths)
- Synthesis с prioritized fixes
- 3-artifact touch list
- Single commit message

**Phase 11 demonstrated:** 1 spawn × 40 min closed 6/6 P1 + 9/16 P2 across chapter + slides + speech. Estimated 5-10× more efficient than per-artifact spawns.

### Parallel revision spawn — cross-artifact alignment mandate (ENFORCED — Лекция 11 lesson)

При parallel spawn'ах **двух или более** producer agents (например, `speech-writer` + `presentation-designer` одновременно для closure cross-artifact P0s), orchestrator brief **MUST** включать:

1. **Explicit cross-artifact alignment requirements per agent.** Каждый агент должен явно перепроверить, что его fix **matches sibling artifact's fix** через цитирование canonical source.
2. **Canonical anchor** (обычно chapter) — все cross-artifact numbers, формулировки, ordering anchor на canonical, не на parallel artifact.
3. **Cross-reference list** — orchestrator brief lists конкретные slides/sections где аналогичная content есть в parallel artifact (например, «brewery numbers в s34c slide ОБЯЗАН match chapter §4.3c canonical 30K bph / 700K/day / 3.5K defects / 30 days»).

**Anchor:** Лекция 11 Phase 11 — speech-writer fixed brewery в speech к canonical 30K bph, presentation-designer parallel scope не touched s34c, slide остался с 60K bph drift. Independent pre-USER-GATE C walkthrough caught — +15 мин quick-fix spawn. Без explicit cross-reference brief — parallel spawns создают scope gaps.

---

## 10. Phase 4b — Chapter expansion (ad-hoc OR owner-mandated)

После Phase 4 (chapter v2 finalized), owner может explicit запросить chapter expansion к глубине L8/L9-style или 30k-baseline. В этом случае:

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 4b — Chapter expansion (conditional)                      │
│ Trigger: owner explicit instruction («сделай как в L8/L9»,      │
│   «30к target», «глубже») OR pre-USER-GATE A walkthrough flag   │
│   chapter < ≥30k baseline (per CLAUDE.md Chapter Depth)         │
│ Agent: book-editor с expansion mandate                          │
│ Output: chapter.md v3 status=reviewed (expansion preserves      │
│   structure, не reorders)                                       │
│ ENFORCED: full citation sweep на expanded chapter; Russification│
│   regression risk — deep latin scan mandatory post-expansion    │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4c — Focused critique post-expansion                      │
│ Critics: methodology + fact-checker (focused на new content,    │
│   reader-text-only skipped если структура не менялась)          │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4d — Chapter expansion revision → finalize v4             │
└─────────────────────────────────────────────────────────────────┘
```

**Anchor:** Лекция 11 Phase 4b — owner explicit «30k цель твоя», chapter 13.4k → 29.8k (+122%). Phase 4c focused critique (methodology + fact-checker) caught 2 P0 + 12 P1 (mostly Russification regression на new content + minor fact-corrections). Phase 4d closed all P0/P1 → v4 finalize 30 499 слов.

## 11. Phase 4e — Chapter multi-part split (ENFORCED при >600 строк)

Per `CLAUDE.md` § «Document Size Limit» + § «Chapter Depth Baseline» — chapter >600 строк per file требует multi-part split:

```
chapter.md         (Part 1 — frontmatter + intro + early sections, ≤600 lines)
chapter-part2.md   (Part 2 — middle sections, ≤600 lines)
chapter-part3.md   (Part 3 — late sections + Q&A + Источники, ≤600 lines)
```

Frontmatter chapter.md: `parts: 3`, `parts_files: ["chapter.md", "chapter-part2.md", "chapter-part3.md"]`.
Frontmatter chapter-partN.md: `part: N`, `of: 3`, `parent: "chapter.md"`.

**Cross-references update:** при split, intra-file refs unchanged; cross-part refs получают path hints (например, «см. §1.1 (chapter.md)» в Part 2/3).

**Navigation block** mandatory: nav header в каждом part (prev / current / next), nav footer в конце.

**Anchor:** Лекция 11 Phase 4e — chapter v4 single-file 1438 строк → split в 3 parts (409/510/592 строк), все ≤600. Zero content loss (+431 слов от navigation blocks). Owner explicit decision «Split на 3 parts → потом slides».

---

## 8. Связь с slides-specific pipeline

`tools/presentation-build/README.md` — фокусируется на slides:
- Palette (Ocean Gradient + Teal + Gold).
- Visual motif (Ocean rounded box).
- Slide-types library (8 типов).
- Visual-loop (min 3 iter).
- 3 QA-агента для slides (presentation-critic / student-simulator / reader-rendered).

Этот файл — **расширение**, добавляющее chapter + speech + новых критиков (`methodology-critic`, `fact-checker`, `consistency-checker`).

---

## 9. Текущий статус (#64 EPIC)

- ✅ **#65 (этот sub-issue)** — 5 агентов созданы, README написан, CLAUDE.md обновлён.
- 🟡 **#64.B** — Phase 1 пилота (re-review v4 plan Лекции 1).
- ⬜ **#64.C** — Phase 2-3 (chapter draft + critique).
- ⬜ **#64.D** — Phase 5-7 (slides update + design + QA).
- ⬜ **#64.E** — Phase 9-10 (speech draft + critique).
- ⬜ **#64.F** — Phase 11 (final approval).
- ⬜ **#64.G** — Methodology stabilization.

После #64.G — отдельный EPIC «Factory: scale to L2-L17».

---

## 10. References

- `notes/decisions.md` § «2026-05-12 — Presentation pipeline» — anti-patterns каталог + iteration journey.
- `notes/mcp-limitations.md` — gotchas tools.
- `tools/presentation-build/README.md` — slides-specific.
- Anthropic **pptx skill** (knowledge source): `github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md`.
- Penn State **assertion-evidence**: `writing.engr.psu.edu/ae_comprehension.pdf`.
- McGill **Design slides to support learning**: `teachingkb.mcgill.ca`.
