# Orchestrator-roast plan-v1 — Лекция 15

**Author:** orchestrator (Claude Opus 4.7 1M).
**Date:** 2026-05-27.
**Scope:** self-review plan-v1.md ДО merge critic-findings; находки добавятся к methodology + reader + fact-checker.

---

## R-O1 — Worked examples ≠ case studies (terminology drift)

Plan заявляет «6 worked examples» (AlphaFold, AlphaProof, GNoME+A-Lab, Galactica, Frontiers, NeurIPS, Sakana). Это **case studies / illustrative cases**, не worked examples в смысле lec-13/14 («walk-the-student-through-decision-making»). Реальный worked example в plan v1 = только **s34 «catalyst pipeline»** (один). Lec-13/14 имели 2-4 *applied* worked examples (e.g., «выбрать AV-уровень для городского курьера»).

**Impact:** LO8 («Применять и создавать») риск под-обеспечен. Студент не получит достаточно тренировки в decision framework.

**P:** P1 (should-fix). **Action**: либо добавить 1-2 worked examples в plan (e.g., §3 «классификация спектральных сигналов» уже скетчем, но не развёрнут как 5-step framework; §4 «коллаборатор даёт LLM bibliography — что делаете?» — это decision exercise, добавить в plan); либо явно переименовать «6 worked examples» → «6 case studies (success/failure)» + «2 applied worked examples».

## R-O2 — Hero «две стороны медали» pattern (single-attention dilution risk)

Side-by-side hero (Nobel + Galactica) — novel pattern, plan признаёт R1. Hero обычно «фокусирует внимание на ОДНОЙ entity». Split half/half может dilute hook impact, особенно для 75-минутной лекции, где первые 30 секунд хука критичны.

**Альтернативный pattern (safer):** Single hero AlphaFold Nobel ceremony (Hassabis/Jumper/Baker на сцене) — позитивный momentum; на s02 (lecture-map slide или s03 keystone) — Galactica failure callback. Tension создаётся через slide-transition, не через split.

**P:** P1 (defer-to-owner). **Action:** flagged в plan-approval gate к user.

## R-O3 — §2 failure-share 23% (under-30% concern)

Plan: §2 (Experiment, 15 мин) — 23% strict-in failure. Holistic average 47.3%, но **самый длинный single section** (15 мин = 20% всей лекции) под-30% bucket. Plan utility: «компенсируется в §4/§5».

**Concern:** CLAUDE.md AI-Failure Rule говорит «доля strict-in ≥30% должна быть видна **в каждом из 3 артефактов** (chapter/slides/speech) отдельно, не сконцентрирована в одном». В рамках одного артефакта (slides) под-30% в одном section допустимо, **если общий артефакт-уровень ≥30%**. **Holistic — да, в порядке.** Но pedagogically: §2 — самый длинный + 23% failure → студент может получить «Nobel-keynote» feel в первые 22 мин лекции, до §4 failure peak.

**Mitigation в plan:** s17 (Palgrave A-Lab critique) + s14 (AlphaFold open-source debate) + s23 (IDP limits, но это уже в §3). Это **2 failure deep-dive слайда из 8 в §2**. Можно усилить — добавить «AlphaFold не работает на membrane proteins» или «Aurora overconfident on extreme weather events» как 3-й failure slide.

**P:** P2 (nice-to-fix). **Action:** book-editor Phase 2 brief — explicit «в §2 chapter увеличить failure callbacks до ~30%».

## R-O4 — Co-Scientist Nature May 2026 (volatile, very recent)

Plan ссылается на DeepMind Co-Scientist Nature May 2026 paper как primary case s07. **Это 9 дней до plan-creation (2026-05-27)** — paper может быть в press, retracted, или corrected; community reactions ещё не сформированы.

**Risk:** book-editor может зашить depth-mention, а к моменту лекции paper изменён.

**Mitigation:** Co-Scientist — **secondary mention** в plan body; primary case для Hypothesis уровня keystone = **Sakana** (более established failure pattern). Co-Scientist — 1 слайд с `[VFY-day-of]`.

**P:** P1 (action-fixable). **Action:** plan revision — Co-Scientist downgraded к secondary; primary Hypothesis-level case = Sakana failures.

## R-O5 — «Closed-world / open-world» термин (Variant B risk)

Plan Variant B keystone использует «closed-world / open-world». Plan сам в Variant B risks (b) предупреждает confusion с established CWA (Closed-World Assumption в Prolog/logic AI).

**Concern:** Если выберем Variant B, нужно либо переименовать («хорошо определённые задачи vs ambiguous задачи»; «verifiable vs unverifiable domains»; «structured vs unstructured science») либо явно ввести термин с RU-расшифровкой («в логике есть Closed-World Assumption, мы используем другое значение — здесь это значит "верифицируемо/неверифицируемо"»).

**Mitigation:** Plan рекомендует Variant A (Лестница цикла); Variant B как fallback. Если owner выбирает A — issue dissolves. Если B — book-editor Phase 2 brief должен explicitly handle terminology.

**P:** P2 (conditional-on-keystone-choice). **Action:** в plan-approval gate к user, flag «если выберешь B, нужно переименование».

## R-O6 — s33 «5 альтернатив matrix» (depth vs breadth)

s33: 5 альтернатив AI в науке (BO+GP, DFT/MD, classical statistical, OR-Tools, human peer review). List of 5 на одном слайде → каждая 1-line. Plan §5 — 12 мин, **5 alternatives × ~2 мин каждая = 10 мин = весь section** (s32+s33+s34+s35+s36).

**Concern:** list of 5 risks как «stuffing». Lec-13 «7 criteria decision framework» работало потому что: (1) 7 criteria — не tools, а questions; (2) каждый criterion имел concrete sub-prompts. Тут 5 tools — разные категории. Может outshow «catalogue mode» вместо deep understanding.

**Альтернатива:** 3 alternatives deep (BO+GP, DFT, classical peer review) + 2 short mentions (OR-Tools, classical signal processing) — keeps breadth но depth concentrated в applicable cases.

**P:** P2. **Action:** book-editor Phase 2 brief — «§5 alternatives: 3 deep + 2 short».

## R-O7 — A-Lab numbers discrepancy (36 of 57 vs 41 of 58)

Plan claims «**36 of 57** target compounds in 17 days». Original Nature paper Szymanski et al. Nov 2023 — я **не уверен** в этих цифрах. Public commentary often cites «41 of 58» or «36 of 41» as variations.

**Action:** fact-checker должен resolve (запускается параллельно).

## R-O8 — arxiv 2602.05930 hallucination suspicion

«arxiv 2602.05930» — arxiv ID format YYMM.NNNNN, 2602 = 2026 February, ID number 05930. Если research agent был в 2026-05-27 и paper якобы за 2026-02 — feasible (date format OK). Но title «NeurIPS 2025 analysis» — research analysis paper за 2 месяца до агента — может быть hallucination, либо может быть real.

**Action:** fact-checker должен verify (запускается параллельно).

## R-O9 — Russification table 22 anglicisms (под-coverage)

Plan имеет 22 anglicisms. Lec-11/13/14 reflection — после full draft обнаружили **40-50+ unique anglicisms** в speech body. Plan-stage таблица всегда optimistic.

**Concern:** «foundation model», «training distribution», «embedding», «replication» — это первые-низшие плоды. Высшие плоды: «alignment», «agentic», «in-context learning», «fine-tuning», «pretraining», «inverse problem», «benchmark», «leaderboard», «hyperparameter», «activation», «inference», «pipeline» — все вылезут в chapter.

**P:** P2. **Action:** book-editor Phase 2 brief — explicit «при первой draft chapter — run deep latin scan; добавить все NEW anglicisms к Russification таблице PER REVISION».

## R-O10 — Numbers convention lock (18 — какие забыты?)

Plan: 18 canonical numbers. Возможно забыты:
- AlphaFold 2 CASP14 GDT_TS (median ~92, baseline ~60)
- AlphaFold DB protein count (200M+)
- Insilico Medicine ISM001-055 trial size / Phase IIa enrollment numbers
- Aurora 1.3B parameters
- GNoME GNN architecture details (если discussed)
- Coscientist tool-call counts / synthesis steps

**P:** P2. **Action:** Phase 2 book-editor добавит при first draft.

---

## Summary roast

- **P0:** 0 — plan структурно sound.
- **P1:** 3 (R-O1 worked-examples-terminology, R-O2 hero side-by-side risk, R-O4 Co-Scientist volatile).
- **P2:** 6 (R-O3 §2 under-30, R-O5 Variant B termin, R-O6 s33 list-of-5, R-O7+8 fact-check pending, R-O9 anglicism scope, R-O10 numbers gaps).

**Verdict:** **APPROVE-WITH-POLISH** для plan-stage; revisions всё в Phase 2 book-editor brief (carry-forward), kроме R-O2 (defer-to-owner) и R-O7+8 (await fact-checker).

**Recommend к user (plan-approval gate):** plan-v1 решает principal questions; нужны 2 decisions от owner:

1. **Keystone choice** (Variant A / B / C) — рекомендую A.
2. **Hero pattern** s01 — «две стороны медали» side-by-side (novel, риск split-attention) ИЛИ single hero AlphaFold Nobel + Galactica callback на s02.

Остальные правки book-editor применит автоматически при Phase 2 chapter draft.
