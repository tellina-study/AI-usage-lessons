VERDICT: REVISE

# Fact-Checker Report — Глава 4 «AI в разработке ПО» (chapter.md + chapter-part2.md + chapter-part3.md + glossary.yaml) — 2026-08-10

Context: this is a from-scratch verification of a book-editor recreation after a git-revert accident. Verified against current file content (not memory of a prior pass) and live web sources as of 2026-08-10.

## Severity counts
- P0 (false fact / broken citation / stale-to-wrong benchmark number presented as current): 1
- P1 (missing caveat / imprecise methodology description / minor date slip): 3
- P2 (cite format / rounding / terminology nuance): 2

## Summary verdict rationale
One P0: the chapter's SWE-bench Pro numbers for "August 2026" (~69% independent SEAL / ~79–80% vendor, gap narrowed to ~15–17pp) do not match the live primary source (Scale AI SEAL public leaderboard) at time of fact-check, which tops out at ~59–61% with different leading models, and does not show the Claude Opus 5/Fable 5/Mythos 5 entries the chapter attributes scores to on that benchmark. Everything else checked (curl timeline, DORA citations, METR deep-dive, both new arXiv citations, glossary) is accurate or only needs light polish. Per the 4-level scale, one P0 forces REVISE regardless of how clean the rest is.

---

## 1. Four freshness fixes

### C1 — SWE-bench Verified/Pro numbers (§2.2, chapter.md)

**Verified-side: APPROVE-WITH-CAVEAT (not a P0, but flag).**
- Claude Opus 5, Claude Fable 5, Claude Mythos 5 are real, currently-shipping Anthropic models (Fable 5/Mythos 5 launched 2026-06-09; Opus 5 launched 2026-07-24) — not fabricated placeholder names. VERIFIED.
- SWE-bench Verified ~95–96% for these models is directionally plausible against current leaderboard aggregators.
- **Missing, material context (P1):** OpenAI publicly announced on 2026-02-23 that it is retiring SWE-bench Verified as a frontier-capability metric, after auditing the 500-task set and finding a majority of a contamination-flagged subsample had serious test defects; OpenAI's own comparison showed models at ~80% on Verified fell to ~23% on (an earlier cut of) Pro under stricter evaluation. The chapter's Deep-dive box 2 already makes a structurally similar point (contamination inflates Verified) but does not cite this specific, dated, high-profile vendor announcement, which would strengthen — not contradict — the chapter's existing argument. Recommend adding one sentence + source. Source: openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (2026-02-23).

**Pro-side: P0.**
- Chapter claims (§2.2, chapter.md and Deep-dive box 2): "Scale AI SEAL, June 2026" gives the leader ~69% (conservative independent), newer vendor leaderboards ~79–80%, gap narrowed from ~24pp (May 2026, ~88%/~64%) to ~15–17pp (August 2026).
- Live fetch of the primary source (labs.scale.com/leaderboard/swe_bench_pro_public) today shows the top of the leaderboard at **~59–61%** (Muse Spark 1.1 — Meta, ~61.5%; GPT-5.4 xHigh ~59.1%), with **no Claude Opus 5 / Fable 5 / Mythos 5 entries appearing at all**, and no score anywhere close to 69% or 79–80%.
- Secondary aggregator/SEO sites (codingfleet.com, benchlm.ai, morphllm.com) do show numbers matching the chapter's 79–80% for Claude Fable 5/Mythos 5/Opus 5 — but these disagree with Scale's own primary leaderboard and with each other, and read as programmatic content rather than primary sourcing. No source could be found anywhere for the specific "~69%, Scale AI SEAL, June 2026" figure or for the "24pp→15-17pp" gap-narrowing framing.
- **Recommendation:** re-source this paragraph directly against labs.scale.com/leaderboard/swe_bench_pro_public with a fetch-date stamp, replace ~69%/~79-80% with whatever the primary leaderboard actually shows at time of final revision, and either drop the "24pp→15-17pp narrowing" claim or replace it with an honestly-computed comparison (current data suggests the Verified/Pro gap is if anything **wider** than 24pp, not narrower — e.g., ~96% vs ~60% ≈ 36pp on a naive top-line comparison, though note these aren't the same models on both boards so a clean matched-model gap needs recomputation). This is the one finding serious enough to block APPROVE.
- Note: this does not undermine the chapter's *qualitative* teaching point (agent trust should scale inversely with code unfamiliarity/criticality, calibrate to Pro not Verified) — if anything the real data makes that point more strongly. It's specifically the cited numbers that need correction.

### C2 — curl case (§4.5, chapter-part2.md)

**VERIFIED — all four sub-claims confirmed against primary sources.**
- Valid-rate decline: baseline >15% → <5% by 2025 — VERIFIED (Stenberg, "Death by a Thousand Slops," 2025-07-14: confirmed rate ~5%, corroborated historical baseline ~15% via secondary sources).
- Volume ×8 (July 2025) — VERIFIED, directly sourced from the same post.
- Bug-bounty sunset: **announced 2026-01-26**, **effective 2026-01-31** — VERIFIED, exact match to Stenberg's "The end of the curl bug-bounty" (2026-01-26) and the HackerOne cutover date. Announce/effective dates are correctly distinguished, not conflated, per the task's requirement.
- Full moratorium on **all** vulnerability reports **2026-07-01 to 2026-08-03** — VERIFIED, exact match. This is a real, separate, later escalation from the January bug-bounty closure, correctly framed in the chapter as "postdates the original analysis, new information." Source: Stenberg, "curl summer of bliss" (2026-06-15): "Summer of bliss starts: July 1, 2026, 00:00 CEST" / "Submissions resume: August 3, 2026, 09:00 CEST."
- No unresolved `[FACT-CHECK: curl valid-rate...]` placeholder remains in the text — confirmed via grep, the only remaining curl-related tags are appropriately-scoped `[VFY-day-of]` (for the exact moratorium dates, reasonable to re-confirm on lecture day) and a source-list `[FACT-CHECK recent — corroborate]` tag on the Kiro/PocketOS incidents (different case, not curl).
- **Post-moratorium update (informational, not requiring a chapter edit):** the moratorium ended on schedule 2026-08-03 as planned. Stenberg's follow-up post that same day ("What the bliss taught us") reports it as a success: zero official vulnerability reports received during the full 5-week pause, no security incidents, backlog returned to normal, and the team is open to repeating "bliss" periods if needed in the future. No renewed AI-slop flood or second moratorium has been reported as of 2026-08-10. This is good color the lecturer could mention live but does not change the chapter's factual claims, which stop appropriately at the moratorium's existence and dates.

### C3 — DORA citation (§5.2, chapter-part3.md)

**VERIFIED, with one minor P2 date nuance.**
- The chapter contains **two distinct DORA-attributed phrases** that must not be conflated, and it correctly does not conflate them:
  1. `«AI doesn't fix a team; it amplifies what's already there»` — presented as a **direct verbatim quote from DORA** (chapter-part3.md lines 57 and 101, "формулировка DORA"). **VERIFIED as accurate**: this is genuine, literal text from Google Cloud's own official 2025 DORA Report announcement blog post (Nathen Harvey, DORA Lead, 2025-09-23): *"The report reveals a key insight: AI doesn't fix a team; it amplifies what's already there."* This is correctly treated as a real DORA-sourced quote, not InfoQ paraphrase — no issue here.
  2. `«AI не чинит сломанные инженерные системы»` ("AI does not fix broken engineering systems") — the chapter explicitly attributes this to **InfoQ's interpretive coverage** of the May 2026 DORA follow-up, not as a verbatim DORA quote (chapter-part3.md line 60, and Sources line 350). **VERIFIED as correctly hedged**: direct fetch of the InfoQ article (infoq.com/news/2026/03/ai-dora-report/) confirms the phrase "Artificial intelligence will not fix broken engineering systems" is InfoQ author Craig Risi's own concluding synthesis/paraphrase, not a blockquoted excerpt from the DORA report itself. **This is the specific item the task flagged as critical to check — it is correctly resolved. No P1 here; the prior fact-check finding has been properly incorporated.**
- The May 2026 "ROI of AI-assisted Software Development" follow-up report is real (dora.dev/ai/roi/report/), and both cited findings check out:
  - "Instability tax": change failure rate rising 5%→6% ≈ −$344,000 modeled impact — VERIFIED via InfoQ's coverage of the report's sample ROI calculator.
  - J-curve model (temporary stability dip before gains, contingent on continued investment) — VERIFIED, matches the report's "J-Curve of value realisation" framing.
- **P2 (minor):** the DORA ROI report landing page itself shows "last updated April 22, 2026," while InfoQ's coverage of it is dated 2026-05-11. The chapter says "в мае 2026 вышло... продолжение" (the follow-up came out in May 2026). This is a soft date slip — the report may have been live in some form before May, with InfoQ covering it in May. Recommend either citing "InfoQ's May 2026 coverage of the report" explicitly, or confirming the report's actual first-publish date, to avoid ambiguity. Not blocking.

### C4 — METR Deep-dive box (Deep-dive box 3, chapter-part2.md)

**VERIFIED — full match against the primary source.**
- The post metr.org/blog/2026-02-24-uplift-update/ ("We are Changing our Developer Productivity Experiment Design") is real; title, date, URL match exactly.
- Late-2025 signal shift to order-of-magnitude −18%/−4% in different cuts — VERIFIED against the actual post (returnee cohort ~−18% [95% CI −38%, +9%], new-developer cohort ~−4% [95% CI −15%, +9%]).
- **Both independent confounds are correctly represented, not merged into one:**
  - Selection bias (developers refusing to do tasks without AI) — VERIFIED, matches METR's own post (30–50% self-reported refusal).
  - Separate pay-rate confound ($150/hr → $50/hr) — VERIFIED, explicitly named by METR itself as a distinct, independently-contributing factor. The chapter's insistence that these are "two independent sources, not one" is accurate to the source.
- Qualitative belief that true uplift is "likely positive," explicitly hedged as interview-based impression and NOT a new RCT remeasurement — VERIFIED, matches METR's own careful hedging language almost exactly.
- Full experiment-design overhaul announced — VERIFIED (METR describes six alternative redesign approaches in the same post).
- No unresolved `[FACT-CHECK: METR late-2025 reversal...]` placeholder remains in the text (confirmed via grep — the only METR-adjacent tags are the appropriately-scoped `[VFY-day-of quarterly]` on the sources line, which is correct practice, not an unresolved placeholder).

---

## 2. New claims in §2.4–§2.8

### Gloaguen et al., arXiv:2602.11988 ("presence paradox")

**VERIFIED with one methodological imprecision (P1).**
- The arXiv ID resolves to a real paper: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" by Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev (submitted 2026-02-12, v2 2026-06-23). Authors match the chapter's citation exactly.
- Core finding matches the chapter's description directionally: context files generally do not improve task success rate, while increasing inference cost (>20% average) — this is the "presence paradox" as the chapter frames it. VERIFIED.
- **P1 — methodology description imprecision:** the chapter describes this as "a controlled RCT with three arms (NONE / LLM-generated / developer-written)" implying one unified three-arm randomized trial. The actual paper design is **two complementary settings**: (1) SWE-bench tasks compared with LLM-generated context files vs. none, and (2) a separate collection of real-repo issues compared with developer-committed context files vs. none. It is not literally a single three-arm RCT as the "NONE / LLM-generated / developer-written" phrasing implies, though the paper does test all three conditions across its two study designs. Recommend softening "RCT с тремя плечами" to something like "controlled comparison across three conditions (two study designs)" to avoid overstating methodological unity. Minor — does not affect the substantive claim (presence alone doesn't help, cost rises), which is accurate.
- Note for awareness (not requiring a chapter change, but worth knowing): at least two other closely related but distinct 2026 papers exist on the same topic with different or opposite directional findings — arXiv:2601.20404 ("On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents," found *reduced* runtime/tokens with AGENTS.md present) and arXiv:2607.27250 (a later ablation study). The chapter cites only Gloaguen et al., which is fine, but if a reader encounters the other papers they may look contradictory — this is a landscape note, not a chapter defect.

### Dixit, Kamal, Oates, arXiv:2605.29463 ("Honest Lying")

**VERIFIED, with a minor framing nuance (P2).**
- The arXiv ID resolves to a real paper: "Honest Lying: Understanding Memory Confabulation in Reflexive Agents" by Prakhar Dixit, Sadia Kamal, Tim Oates (submitted 2026-05-28, v2 2026-05-31). Authors match. Accepted to an ICML 2026 workshop on failure modes in agentic AI.
- Core finding matches the chapter's claim closely: reflexion-style agents that write self-authored memory/reflections store confidently wrong self-diagnoses and continue acting on them across trials, even when the environment resets correctly — i.e., self-authored notes entrench rather than correct errors. VERIFIED.
- **P2 — minor framing breadth:** the paper's own scope is in-session "reflexive memory" in RL-style agent-loop benchmarks (ALFWorld, HumanEval), termed "memory confabulation," not literally file-based AGENTS.md/CLAUDE.md-style persistent steering files across coding sessions. The chapter's application of this finding to self-authored steering-file edits (§2.7) is a reasonable and defensible extrapolation of the mechanism, but is broader than the paper's literal tested scope. Not a misrepresentation — the underlying mechanism (self-authored belief-reinforcement without re-verification) transfers logically — but worth being aware this is an analogical application, not a direct empirical finding about steering files specifically.
- Both arXiv IDs are correctly formed per arXiv's YYMM.NNNNN scheme (2602 = Feb 2026, 2605 = May 2026) and both resolve to real, indexed papers as of today. Neither is fabricated.

### Anthropic Agent Skills format (§2.5)

**VERIFIED.**
- The described format (a skill = directory with required `SKILL.md`, YAML frontmatter with name/description driving when-to-use, optional `scripts/` and `references/` subdirectories) matches Anthropic's actual published documentation and the public `anthropics/skills` GitHub repo.
- The project-level vs. personal distinction is plausible and commonly described in third-party writeups, but was not independently confirmed against Anthropic's primary docs in this pass — mark this specific sub-claim as **UNVERIFIABLE** (not disproven, just not directly confirmed against a primary source in this check). Low risk given the rest of the format description is accurate.

### MCP server category claims (§2.6)

No specific numeric or dated claims present in this subsection — it is a descriptive taxonomy (repo/issue-tracker, filesystem, CI/CD, database, docs/search categories) without benchmark numbers or citations requiring external verification. No issues found.

### Claude Code / tooling adoption stats (§0.4, §1.2, §1.3, §2.2, §5.4, Deep-dive box 5)

**Largely VERIFIED**, sourced to a JetBrains-anchored 2026 developer survey (~10,000 developers, data through January 2026) as reported by danilchenko.dev and ideaplan.io.
- Claude Code ~6× growth over ~9 months: VERIFIED (sources show 3%→18% usage, described as "8 months"/"under a year" — the chapter's "~9 months" is a close, reasonable rounding, not a fabrication).
- Highest CSAT (91%)/NPS (54)/"most-loved" (46% vs Cursor 19%, Copilot 9%): VERIFIED.
- GitHub Copilot ~29% usage / ~76% awareness: VERIFIED, exact match.
- Copilot 4.7M paid subscriptions, +75% YoY, awareness/adoption "stalled": VERIFIED (4.7M and +75% YoY both confirmed; "stalled" supported by the same source noting awareness/adoption barely moved Sep 2025–Jan 2026).
- Cursor 18% usage, $2B ARR: VERIFIED.
- ChatGPT-as-coding-chat 28%: VERIFIED.
- Codex 3%/27%: the 3% figure (work adoption) is VERIFIED; the paired "27%" figure could not be matched to any specific metric in the two sources checked (possibly an awareness figure analogous to Copilot's 76%, but unconfirmed) — mark as **UNVERIFIABLE**, low severity given it's already tagged `[VFY-day-of]` in the chapter and the volatility framing is appropriate either way.

---

## 3. glossary.yaml — 28 new lines

**VERIFIED — no fabricated or incorrect definitions found.**

All seven new terms (skill/навык агента, субагент, agentic IDE, CLI-агент, steering-файл, presence paradox, Honest Lying) were cross-checked against their usage in chapter.md §2.4–§2.8:
- `skill (навык агента)` — note correctly points to Л3 §4.8 for the general definition and §2.5 (issue #162) for the SWE-specific format concretization; matches actual chapter content and the real Anthropic Agent Skills format.
- `субагент (subagent)` — note correctly distinguishes general definition (Л3 §4.4/§4.8) from SWE-specific application (§2.4); forbidden variants ("саб-агент", "sub-agent (в тексте)") are sensible anti-anglicism entries consistent with the project's Russification mandate.
- `agentic IDE` / `CLI-агент` — both correctly flagged as new §2.4 terms, categories orthogonal to the A→D autonomy ladder; matches chapter's explicit framing ("это отдельная ось от лестницы автономности").
- `steering-файл` — note explicitly says it does NOT replace the canonical "AGENTS.md / CLAUDE.md" term already in the glossary, but names its role as a versioned engineering artifact — this is accurate; the chapter (§2.7) uses "steering-файл" as a working name for the same file class, consistent with the glossary note.
- `presence paradox` / `Honest Lying` — both correctly marked as introduced in Lecture 3 §4.7 with a callback in this chapter's §2.7, and both carry an explicit "НЕ переопределять" (do not redefine) instruction — accurate, since the chapter's §2.7 does reference rather than redefine these concepts, per my reading of the actual text.

No glossary entry contradicts real-world usage of these terms or misstates what the cited arXiv papers found.

---

## Top-N правок до публикации

1. **[P0 — BLOCKING]** Re-verify and correct the SWE-bench Pro numbers in §2.2 (chapter.md) and Deep-dive box 2 against the live primary source (labs.scale.com/leaderboard/swe_bench_pro_public) — current chapter figures (~69% SEAL, ~79-80% vendor, gap narrowed to 15-17pp) do not match what the primary leaderboard shows today (~59-61% top score, different leading models, no Claude Opus 5/Fable 5/Mythos 5 entries visible). Either update numbers with a fresh fetch-date stamp, or reframe the paragraph to acknowledge leaderboard volatility more strongly and cite the primary source URL directly rather than secondary aggregators.
2. **[P1]** Add one sentence to §2.2 or Deep-dive box 2 noting OpenAI's 2026-02-23 announcement retiring SWE-bench Verified due to contamination findings (audited subsample, ~59% flawed; ~80%→~23% Verified-to-Pro drop under stricter evaluation) — this strengthens, not undermines, the chapter's existing contamination argument and is a citable, dated, high-profile fact currently missing.
3. **[P1]** Soften the Gloaguen et al. methodology description from "RCT с тремя плечами (NONE/LLM-generated/developer-written)" to reflect the paper's actual two-study-design structure, to avoid overstating methodological unity.
4. **[P2]** Clarify the DORA ROI report's actual publish/update date (landing page says "last updated April 22, 2026") vs. InfoQ's coverage date (2026-05-11) — either cite "InfoQ's May 2026 coverage" explicitly or confirm the report's true first-publish date.
5. **[P2 / informational, optional]** Consider a brief lecturer's-note (not necessarily a chapter edit) that the curl moratorium ended on schedule 2026-08-03 with zero vulnerability reports received during the pause and no incidents — good live color, doesn't change any existing chapter claim.
6. **[Informational]** The Codex "27%" figure in the tools-adoption data (§2.2/Deep-dive box 5) could not be matched to a specific metric in available sources — already appropriately `[VFY-day-of]`-tagged; no urgent action needed but flag for day-of-lecture recheck.

## Verified facts (sample) — full list of 4 freshness fixes + new-content spot-checks above
- curl bug-bounty timeline (announce/effective/moratorium, all four dates) — VERIFIED against primary source (Stenberg's own blog).
- METR 2026-02-24 post, both confounds, hedged belief, methodology overhaul — VERIFIED against primary source (metr.org).
- DORA "amplifies what's already there" as genuine verbatim DORA quote — VERIFIED against Google Cloud's own blog.
- "AI does not fix broken engineering systems" correctly attributed to InfoQ's paraphrase, not DORA verbatim — VERIFIED, this is the specific item flagged as critical and it is resolved correctly.
- DORA ROI report (instability tax $344k, J-curve) — VERIFIED.
- arXiv:2602.11988 (Gloaguen et al., presence paradox) and arXiv:2605.29463 (Dixit/Kamal/Oates, Honest Lying) — both real, both resolve, both substantively match chapter's description (with the P1/P2 nuances above).
- Anthropic Agent Skills format (SKILL.md + frontmatter + scripts/references) — VERIFIED.
- glossary.yaml 28 new lines — VERIFIED, no fabrications.
- Chapter word count: chapter.md 13,901 + chapter-part2.md 8,884 + chapter-part3.md 9,036 ≈ 31,821 words total, consistent with frontmatter's `length_words: ~31350` and comfortably above the ≥28,500 P0-blocking floor for L4+ under the Chapter Depth Baseline rule.

## NEEDS-CITATION
- None beyond what's already tagged `[FACT-CHECK]`/`[VFY-day-of]` in the source text — the chapter's existing tagging discipline is good and was checked; no untagged bare statistic was found lacking a source in the sections reviewed.

## UNVERIFIABLE
- Anthropic Agent Skills "project-level vs. personal" distinction — plausible, third-party-corroborated, not confirmed against Anthropic's primary docs in this pass.
- Codex "27%" figure in tools-adoption data — could not match to a specific metric; low severity, already `[VFY-day-of]`-tagged.
