# Content — Lec-2 production observations

## Methodology gaps that critics missed

### Gap 1: Hook quality not checked

**What happened:** s01 hook = strawberry test («сколько r в strawberry → 2 vs 3»). Plan v1 + chapter + first slide render все cited strawberry as central hook. Fact-checker DID flag freshness (P1 в Phase 3 + 7) but framed как «verify-day-of»: assumption that strawberry still fails in 2026.

User в R4: «strawberry test устарел ведущие ллм его проходят». Top GPT-4o / Claude 4.7 / GPT-5 reliably answer «3» now. Hook FAILS methodologically.

**No critic agent had «is hook engaging vs just educationally correct?» в checklist.**

**Action:** methodology-critic ADD «Hook Engagement Quality Check» (см. improvements.md P0-2).

### Gap 2: Attention as matrix concept missing

**What happened:** Plan + chapter описывали attention как «distribution на токены, сумма=1» (s14). Cosine + bar chart visualization. Никогда не mentioned **matrix nature** of attention (N×N for sequence length N).

User в R4: «механизм же не линейный а матричный! добавь слайд и скорректируй где надо остальные».

**Methodology-critic at chapter stage** checked LO coverage + assertion-evidence + sequence — но did not ask «is fundamental N×N matrix nature shown?». **Missing-Fundamentals check needed.**

**Action:** methodology-critic ADD «Missing-Fundamentals Check» (см. improvements.md P0-3).

### Gap 3: End-to-end flow schema missing

**What happened:** Chapter + slides covered tokenization → embedding → attention → sampling as separate stages. NO synthesizing slide showing **words → tokens → vectors → LLM → vectors → tokens → words** end-to-end.

User в R4: «перед токенами не хватает схемки, что слова в векторы, уже они в LLM, оттуда тоже вектора и они в слова».

**Phase 8.8 created s04b «Поток данных в LLM — туда и обратно»** showing 7-box flow. This should have been in initial plan.

**Action:** Missing-Fundamentals check explicit per-section (см. improvements.md P0-3): «End-to-end flow shown somewhere?».

### Gap 4: Vector space introduced before similarity

**What happened:** s10 used cosine similarity heatmap + 2D scatter projection — но без preceding slide explaining «what IS embedding space, what are dimensions, how are vectors learned».

User в R4: «может даже отдельный слайд до этого про пространство в котором вектора появляются, что там за измерения и как они проставляются у векторов».

**Phase 8.8 created s09a «Пространство эмбеддингов — где живут векторы»** with clusters illustration + Размерность / Обучение / Проекция cards. This should have been in initial plan.

**Action:** Missing-Fundamentals check для embedding section: «vector space before similarity?».

### Gap 5: Methodology-critic curriculum-relevance check missed «too forward-looking»

**What happened:** s11 «3 применения эмбеддингов: similarity / clustering / search — основу RAG» listed RAG application. User в R4: «защити это на следующей лекции, фокусируйся на основном материале».

**Methodology-critic** has Curriculum Relevance Check (Bloom × lecture-level matrix) — it categorized s11 as «Understand» level (KEEP per matrix). But missed «this content belongs in Lec-3, not Lec-2» dimension.

**Lesson:** Curriculum Relevance check should also ask «does this content belong in current lecture OR is it forward-pointing to future lecture?». Defer-or-keep call.

**Action:** methodology-critic Curriculum Relevance Check EXTEND with «temporal placement» дополнительный criterion.

### Gap 6: Designer-added extras despite explicit rule

**Already documented в Phase 7 critique:** `[VERIFY-DAY-OF]` markers leaked to visible body на s16 + s27. LO codes (LO4, LO7) visible. § cross-refs visible.

**Lesson:** «No Extra Content Rule» в CLAUDE.md exists but ENFORCEMENT in pre-USER-GATE walkthrough wasn't aggressive enough. Need grep-based STOP-if-hits enforcement.

**Action:** pre-user-gate skill ADD mandatory grep checks (см. improvements.md P1-2).

---

## What worked well content-wise

1. **3 cross-cutting frames placement** (s22 local/cloud, s25 ML vs LLM, s26 Human vs AI). All 3 callbacks to Lec-1 sections (§4.2, §1.4, §4.8) intact.

2. **3 «почему» Лекции 1 §5.3 payoff** mechanistically закрыт в s24. All 3 answers tied к specific внутренний mechanism:
   - Role в prompt → attention weights
   - AI can't count letters → BPE token-level
   - Different answers → sampling stochasticity at T>0

3. **Glossary lock 17 canonical terms** preserved through all 12 phases. Zero forbidden term hits в final body.

4. **Pearl callback в s26** softened from Phase 3 «3 уровня causality» (overshoot for introductory) to Phase 8 «корреляции в данных, не каузальный граф» (correct level).

5. **Cross-references Lec-1** (9 sections cited) all consistent through chapter + slides + speech.

---

## Action

→ improvements.md P0-2 (hook quality), P0-3 (missing-fundamentals), P1-4 (curriculum temporal placement).
