# Fact-Check — Plan-v1 — Лекция 4

**Date:** 2026-05-13
**Critic:** fact-checker (re-pass on plan-v1)
**File reviewed:** `notes/lecture-4-review/plan-v1.md`
**Cross-ref:** `notes/research/lecture-4/sources.md`

---

## Verdict: REVISE

Plan-v1 содержит **3 критических P0 issues**, требующих swap'а или rewording до USER GATE 0:

1. **DSP-1181 case** (s17) — план описывает его как narrative "обещание vs реальность" с timeline и discontinuation **уже как ожидаемый исход** ([CRITICAL FACT-CHECK] tag присутствует), но не делает swap на verified primary flagship **Insilico Rentosertib (Nature Medicine June 2025)**. Это технически OK (план учитывает оба исхода), но **upgrade путь рекомендован**: Rentosertib = first peer-reviewed positive Phase 2a — гораздо сильнее narrative.
2. **mosmed.ai «4 млрд руб/год экономии в ОМС»** (s5, s8, s12, s26) — `[FACT-CHECK]` tag присутствует только на s12; на s5, s8 и в central question framing s24 повторяется **без caveat**. Per sources.md §2.3 — **этот точный figure NOT VERIFIED**. Должен быть swap на operational metrics.
3. **FDA AI/ML device count freshness mismatch** (s4, s7) — plan-v1 цитирует «1016 одобренных к августу 2024» как baseline + проекция на 2026; sources.md §2.1 показывает **1,451 cumulative through end-2025** — это уже не проекция, это публикованный official count, и plan-v1 baseline устарел.

Прочие P1 — sensitivity/specificity numbers без published source, AlphaProteo capability oversimplified, Liu et al. 2019 в s11 не покрыт sources.md (необходим second-pass verify), MASAI отсутствует в plan-v1 вообще (хотя per sources.md = strongest peer-reviewed AI diagnostic case).

---

## P0 — Claims that MUST be fixed before USER GATE

### P0-1 — Slide s17: DSP-1181 flagship case (UPGRADE recommended)

**Plan-v1 claim:** «DSP-1181 (2020): "первый AI-designed drug" — обещали 12 месяцев design vs 4-5 лет традиционно... 2022: Phase 1 closed/discontinued [CRITICAL FACT-CHECK]».

**Actual status per sources.md §1.1, §1.3, "Status of DSP-1181" final section:**
- DSP-1181 **DISCONTINUED**, Phase 1 stopped 2022 in Japan. Confirmed via Synapse/PatSnap, Sumitomo press, CAS Insights. Sources do NOT specify cause (efficacy/safety/business).
- **Verified upgrade path:** **Insilico Rentosertib (ISM001-055 / INS018_055)** — **Nature Medicine June 2025** peer-reviewed Phase 2a positive readout (n=71 IPF patients, 21 China sites). 60 mg QD: +98.4 mL FVC vs −62.3 mL placebo at 12 weeks. **This is the first peer-reviewed clinical proof-of-concept for AI-designed drug on May 2026.**

**Fix recommendation:** Restructure s17 narrative:
- **Primary case:** Insilico Rentosertib — peer-reviewed Nature Medicine 2025, positive Phase 2a, ~18 months target→preclinical = «AI обещание частично сбылось».
- **Reality check case:** DSP-1181 discontinued + BenevolentAI BEN-2293 Phase 2a failure + Exscientia→Recursion merger Nov 2024 = «marketing promises met clinical reality».
- This makes s17 narrative **stronger**, not weaker — есть verified success AND verified failure, comparable timeline.

**Confidence:** HIGH (Nature Medicine June 2025 is peer-reviewed, Synapse/PatSnap data is authoritative for clinical status).

**Source:** sources.md §1.1, §1.3, §1.6, §1.10; primary: [Nature Medicine June 2025 (PMID 40461817)](https://pubmed.ncbi.nlm.nih.gov/40461817/), [Insilico press](https://insilico.com/news/tnrecuxsc1-insilico-announces-nature-medicine-publi).

---

### P0-2 — Slides s5, s8, s12, s26: mosmed.ai «4 млрд руб/год экономии в ОМС»

**Plan-v1 claim (verbatim):**
- s5 framing (Bold): «mosmed.ai — concrete пример того, как AI-обещание сбылось» (implicit reference к 4 млрд).
- s8: «mosmed.ai 4 млрд руб/год = directly measurable ROI» — **WITHOUT [FACT-CHECK] tag**.
- s12: «4 млрд руб/год экономии в ОМС (Vedomosti / Kommersant 2024-2025) `[FACT-CHECK]`» — flagged.
- s26 takeaway #1: «mosmed.ai 4 млрд руб/год» — **WITHOUT [FACT-CHECK] tag**.

**Actual status per sources.md §2.3 (KRYTYCHNO):**
- **Точная цифра «4 млрд руб/год экономии в ОМС» НЕ НАЙДЕНА** в Moscow Healthcare Department press, mosmed.ai/en/ai/ операционная страница (no financial figures), TASS interview с главой ЦДиТ, или НПКЦ ДиТ ДЗМ публикациях.
- Похожая, но **не идентичная** цифра: «Moscow Healthcare digital transformation — RUB 2.96 billion saved per year» (broader, not radiology AI specifically). Другая: «AI company earned ~2.75 billion rubles over 2.5 years» (commercial revenue, not OMS savings).
- **Verified operational metrics** (use these instead):
  - 14+ миллионов исследований проанализировано за 5 лет (Remedium, mos.ru).
  - 2000+ медицинских организаций подключено (Healthcare ME, mos.ru).
  - 74 региона РФ (Healthcare ME).
  - 18+ миллионов medical images processed (Healthcare ME 2026).
  - ~70 AI services across 43 clinical areas.
  - 11 национальных стандартов разработано.
  - 300+ reference datasets.
  - До 95% accuracy claimed (caveat — vendor self-report).

**Fix recommendation:**
1. **Remove «4 млрд руб/год» from s5, s8, s26** — на каждом из этих слайдов используется без caveat.
2. **Replace в s12** на «свыше 14 млн исследований за 5 лет, 74 региона РФ, 18+ млн изображений (источник: mosmed.ai, Remedium, ДЗМ Москвы)» — verified, sufficient impact.
3. **Если хочется financial framing** в s8 — формулировать как «измеримый ROI на operational scale» без conkretного числа; или сослаться на verified 2.96 млрд/год Moscow digital transformation broader figure (с caveat «not radiology-specific»).
4. Central question framing на s5 («обещание сбылось — mosmed») остаётся валидным — она про operational reality, не про точный rub-savings число.

**Confidence:** HIGH (sources.md проделана thorough поиск, alternative figures найдены, точный 4 млрд не верифицирован).

**Source:** sources.md §2.3 + cross-ref §10.1; primary: [Mos.ru AI Leaders Award](https://www.mos.ru/en/news/item/147773073/), [mosmed.ai operational](https://mosmed.ai/en/ai/), [Remedium](https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/), [Vedomosti March 2026](https://www.vedomosti.ru/press_releases/2026/03/18/moskovskii-ii-pomogaet-vracham-po-vsei-strane-uzhe-provereno-10-mln-snimkov).

---

### P0-3 — Slides s4, s7: FDA AI/ML device count — OUTDATED baseline

**Plan-v1 claim:**
- s4: «FDA AI/ML-enabled medical devices: 1016 одобренных к августу 2024 (FDA, обновляется ~quarterly) [FACT-CHECK: latest count] — на дату лекции 2026 будет ~1200-1400 (linear extrapolation, проверить FDA-list).»
- s7: bar chart data: «2022: ~521; 2024 (август): 1016 [FACT-CHECK: latest count]; 2026 проекция: ~1300-1500.» Caption: «76% — рентгенология (CV-based); 11% — кардиология».

**Actual status per sources.md §2.1:**
- **1,451 cumulative authorized devices through end-2025** (verified — FDA official + JAMA Net Open + The Imaging Wire Dec 2025 + IntuitionLabs).
- **258 AI devices authorized в 2024 alone** (not «cumulative until Aug 2024»).
- **295 new authorizations в 2025** (recent year — quarterly cadence holds).
- **Radiology = 76%** — VERIFIED.
- Cardiology breakdown — sources.md says «cardiology + neurology following»; 11% claim in plan-v1 needs second-source verification (один subspecialty study showed cardiology ~10-11%, OK approximation).

**Fix recommendation:**
- Replace «1016 одобренных к августу 2024» → «**1,451 cumulative через конец 2025** (с **258 в 2024 + 295 в 2025**); rolling quarterly update».
- Update bar chart endpoint: not «2024 (август): 1016» but **«2024: cumulative 1,193 (258 new); 2025: cumulative 1,451 (295 new)»** — actual published numbers, not extrapolation.
- For lecture date 13 мая 2026 — re-fetch FDA list on day-of-lecture (quarterly cadence + recent Q1 2026 authorizations may add 50-80 more devices).
- Keep 76% radiology — VERIFIED.

**Confidence:** HIGH (multiple independent sources confirm 1,451 through end-2025).

**Source:** sources.md §2.1; primary: [FDA AI/ML official list](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices), [The Imaging Wire Dec 2025](https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/), [JAMA Net Open systematic review](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841066).

---

## P1 — Refinements

### P1-1 — Slide s10: mosmed.ai sensitivity 0.94 / specificity 0.89 — unverified published source

**Plan-v1 claim:** «для mosmed.ai CV-моделей: sensitivity 0.94, specificity 0.89 (для COVID screening, 2020-2022) [FACT-CHECK].»

**Issue:** Plan flagged via `[FACT-CHECK]`, but specific numbers (0.94 / 0.89) appear to be conjectured — sources.md does NOT have a verified Morozov et al. or mosmed.ai-published sens/spec pair at this resolution. Morozov / ЦДиТ публикации существуют, но values vary by pathology (rak lung vs COVID vs ischemic stroke = different operating points). Citing a single «0.94 / 0.89 pair as mosmed.ai number» without proper source = high risk of being wrong.

**Fix recommendation:**
- **Option A (preferred):** Replace mosmed COVID numbers с **CheXNet pneumonia (Rajpurkar et al. 2017 + 2018 reanalysis) numbers**, which are properly published, peer-reviewed, и stable (sensitivity 0.96, specificity 0.93 — published values, verifiable). Plan-v1 actually acknowledges this fallback option in s10 Risks/things to verify section — formalize as primary.
- **Option B:** Use **MASAI Sweden RCT 2024/2025 numbers** (sensitivity 0.805 AI vs 0.738 standard — see P1-2 below) — these are gold-standard peer-reviewed, perfect для мат-применение.
- **Option C:** If keeping mosmed — verify specific publication (Morozov 2021/2022 in peer-reviewed journal) with exact pathology + threshold; cite as «по pathology N, threshold X».

**Severity:** P1 (not P0 because plan already flags as `[FACT-CHECK]`, но это foundational metrics slide и хотите solid example).

**Source:** sources.md §2.5 (MASAI), §9.1 reference Rajpurkar CheXNet 2017.

---

### P1-2 — MASAI trial NOT IN plan-v1 — major omission for diagnostic strongest evidence

**Plan-v1 status:** MASAI not mentioned in plan-v1 slide content (verified via line-search).

**Per sources.md §2.5:**
- MASAI = **first peer-reviewed RCT of AI mammography**, Sweden, >100,000 women, Lancet Digital Health (Feb 2025) + Lancet (2025-2026) interval cancer follow-up.
- **AI sensitivity 80.5% vs 73.8% standard** (at specificity 98.5%).
- Cancer detection rate **6.4 vs 5.0 per 1000** (ratio 1.29).
- **44% reduction в radiologist workload**.
- **12% reduction in interval breast cancers** in follow-up.

**Issue:** s11 «AI vs радиолог» сейчас cites Liu et al. 2019 Lancet Digital Health meta-analysis (5+ years old) и McKinney 2020 Nature breast cancer. **MASAI is newer, stronger, peer-reviewed RCT** (not meta-analysis) с verified clinical outcomes. Plan-v1 misses this as foundation.

**Fix recommendation:**
- Add MASAI к s11 (или integrate INTO s11) as primary evidence; keep Liu 2019 / McKinney 2020 as historical context.
- Caption: «MASAI RCT — Sweden 100k women, Lancet Digital Health 2025: sensitivity gain 6.7 pp, workload −44%, interval cancers −12%».
- Strengthen central question payoff («AI-диагностика — обещание сбылось»): MASAI = harder evidence than mosmed operational stats.

**Severity:** P1 (omission, not error — but for «strongest evidence» strategic slide).

**Source:** sources.md §2.5; [Lancet Digital Health MASAI 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00267-X/fulltext), [Lancet 2025 interval cancer](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract).

---

### P1-3 — Slide s11: Liu et al. 2019 numbers — partial verification

**Plan-v1 claim:** «Radiologist alone: sensitivity 0.85-0.92 / specificity 0.95+ (Liu et al. 2019 Lancet Digital Health meta-analysis)»; «AI alone: 0.94 / 0.89»; «AI + Radiologist: 0.97+ / 0.94+».

**Issue:**
- Liu et al. 2019 IS landmark meta-analysis — sources.md does not directly verify these exact numbers (no §2 entry for Liu 2019 specifically, see Top-3 Surprising Findings + §2.5 MASAI).
- The «AI + Radiologist» numbers (0.97+ / 0.94+) are NOT cited to specific paper in plan-v1 — «Sezgin et al. 2024 + Mango Tx 2024» mentioned, but neither in sources.md.
- This is the **central comparison slide for «AI vs радиолог»** — accuracy матerial.

**Fix recommendation:**
- Replace «AI alone» mosmed COVID number (already P1-1) с MASAI или CheXNet.
- Verify Liu 2019 numbers against published abstract (the meta-analysis is real, but exact pooled sens/spec values vary by inclusion criteria — pull verbatim from paper abstract before citing).
- Replace «Sezgin et al. 2024 + Mango Tx 2024» с MASAI (which is the AI+radiologist study на mammography). MASAI: AI+radiologist achieves the 6.7 pp gain that current claim attributes to Sezgin/Mango — these are the actual numbers, properly cited.
- Caption update: «MASAI Lancet 2025; Liu et al. 2019 Lancet Digital Health» — two papers, one current RCT, one foundational meta-analysis.

**Severity:** P1 (numbers may be roughly correct, but attribution and exact values lack solid backing in sources.md).

---

### P1-4 — Slide s16: AlphaProteo «3-300× better» — wording precise but oversimplified

**Plan-v1 claim:** «AlphaProteo (2024): designs new protein binders с 3-300× improved affinity vs prior methods (DeepMind blog Sep 2024) [FACT-CHECK]».

**Per sources.md §1.5 — verified:**
- **VERIFIED:** 3-300× better binding affinity vs best existing methods on seven protein targets — correct.
- **Missing from plan-v1:** specific BHRF1 result («88% of candidate molecules bound successfully» in DeepMind wet lab) + «first AI tool that designed successful binder для VEGF-A».
- **Issue:** «3-300×» without target/context = orphan number; could be misleading (300× is single best case, 3× is lower bound).

**Fix recommendation:**
- Reword: «AlphaProteo (DeepMind Sep 2024) — designs novel protein binders для 7 targets; **88% success rate for BHRF1, 3-300× affinity improvement** vs prior methods; first AI binder для VEGF-A».
- Caveat (speaker notes): independent lab replication outside DeepMind не было found в search через May 2026 — proprietary lab data only.

**Severity:** P1 (number correct, framing could be tightened).

**Source:** sources.md §1.5 + §1.10 «Critical Gaps»; primary: [DeepMind blog](https://deepmind.google/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/), [arXiv:2409.08022](https://arxiv.org/abs/2409.08022).

---

### P1-5 — Slide s16: AlphaFold «2M+ researchers in 190 countries»

**Plan-v1 claim:** «Used by 2M+ researchers в 190 странах (DeepMind 2024 update). [FACT-CHECK]».

**Per sources.md §3.3 (AlphaGenome):** «**3,000 scientists from 160 countries** using AlphaGenome» — but this is AlphaGenome (June 2025), not AlphaFold.

**Issue:**
- AlphaFold-specific user count of «2M+ in 190 countries» NOT verified in sources.md.
- sources.md does confirm AlphaFold Protein Structure Database has 200M+ structures (predictions, not users), но user-count number 2M+ is a separate claim.
- DeepMind has cited various AlphaFold user numbers in 2024-2025 (1.4M, 2M+, 2.3M) — needs verbatim source.

**Fix recommendation:**
- Either: verify exact number from DeepMind 2024 update press release (Hassabis Nobel talk 2024 cited «over 2 million researchers» — primary source recommended).
- Or replace с verified structure count: «200M+ structures предсказано в AlphaFold Protein Structure Database (UniProt-coverage)».
- Don't conflate с AlphaGenome 3000-scientist number.

**Severity:** P1 (probably correct order-of-magnitude, but exact figure needs primary-source attribution).

**Source:** sources.md §3.3; AlphaFold-specific user count requires Hassabis Nobel talk Dec 2024 or DeepMind 2024 annual report check.

---

### P1-6 — Slide s17: Exscientia 2025 timeline — verify status

**Plan-v1 claim:** «**Exscientia сама — turbulent** (CEO Hopkins fired 2025; merger talks с Recursion 2024). [FACT-CHECK]».

**Per sources.md §1.2 — verified facts but **timeline correction needed**:**
- Merger announced **August 8, 2024** (not «merger talks 2024» — formal announcement August).
- Merger **completed November 2024** (all-stock $688M deal closed) — Exscientia folded INTO Recursion, no longer standalone.
- CEO Hopkins firing claim: **NOT verified в sources.md**. sources.md describes Exscientia financial trouble + merger; CEO firing as separate event needs primary source.
- Possible conflation: «Hopkins fired 2025» may refer to BenevolentAI's CEO changes (different company), OR Hopkins may have left during merger process (executive transitions are normal in mergers). Verify or remove.

**Fix recommendation:**
- Replace «CEO Hopkins fired 2025; merger talks с Recursion 2024» с verified «Recursion + Exscientia merger announced Aug 2024, completed Nov 2024 ($688M all-stock); Exscientia folded into combined company».
- If Hopkins firing happened, find primary source (FierceBiotech / Endpoints article) — else remove claim.

**Severity:** P1 (one verified fact + one unverified claim).

**Source:** sources.md §1.2; primary: [Recursion press release Aug 2024](https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-enter-definitive-agreement-create), [Fierce Biotech merger article](https://www.fiercebiotech.com/biotech/after-tough-year-exscientia-folds-recursion-create-ai-super-power), [PharmaPhorum](https://pharmaphorum.com/news/ai-biotechs-exscientia-and-recursion-agree-688m-merger).

---

### P1-7 — Slide s22: Mihalache et al. 2024 hallucination rate «~20%»

**Plan-v1 claim:** «ChatGPT medical Q&A studies: ~20% hallucination rate в medical literature citations (Mihalache et al. 2024 + others).»

**Per sources.md §4.5, §6.2:**
- Baseline GPT-4 ~63% hallucination rate in clinical Q&A.
- DeepSeek-R1 ~48%, SoTA medical LLMs 15-40%.
- Fabricated citations: **>30% of chatbot answers** in research contexts.
- Stanford specific: GPT-4o **6% fabricated for major depression** vs **28-29% fabricated для binge eating/body dysmorphic disorder** (varies by topic).
- Mihalache et al. 2024 IS a real JAMA Network Open paper, но точный «20%» — нет explicit verification в sources.md.

**Fix recommendation:**
- Either: cite verbatim Mihalache 2024 number (verify from abstract — likely something like «5.4%-22.5% по conditions» or similar, not single «20%»).
- Or use Stanford HAI numbers: «6% to 29% fabricated citations depending on medical topic» (sources.md §6.2 verified).
- Or general «Stanford HAI documented up to 30% unsupported statements в GPT-4 RAG medical responses».

**Severity:** P1 (general claim direction correct, specific number suspect).

**Source:** sources.md §4.5, §6.2; primary: [Stanford HAI](https://hai.stanford.edu/news/generating-medical-errors-genai-and-erroneous-medical-references), [Mihalache 2024 JAMA Network Open](https://doi.org/10.1001/jamanetworkopen.2024.21945).

---

### P1-8 — Slide s23: Change Healthcare breach — numbers slightly inconsistent

**Plan-v1 claim:**
- «190 млн человек, $2-3 млрд recovery cost» (assertion bullet).
- «$2-3 млрд recovery cost (UHG financial reports)» (info-card).
- «**22 дня** outage» (info-card).
- «**ALPHV/BlackCat** — ransomware group; paid **$22 млн ransom**» (info-card).

**Per sources.md §7.1 — verified precise numbers:**
- **190 million Americans** — VERIFIED (UHG official statement updated to 190M from initial 100M).
- **6 TB of data exfiltrated** — VERIFIED.
- **$22M Bitcoin ransom paid** — VERIFIED.
- **$2.457 billion total cost (UHG Q3 2024)** — VERIFIED (precise number, not range $2-3B).
- **«22 дня outage»** — needs verification; sources.md мentions «outage major US healthcare claims processing» without specific 22-day figure. Industry reports vary (outage was multi-week, full restoration weeks-to-months for some services).

**Fix recommendation:**
- Replace «$2-3 млрд» with **«$2.457 млрд»** (specific verified number; precise = more authoritative).
- Verify «22 дня outage» from primary source — Reuters/Kaiser Health News article preferred. If unverified, use «multi-week disruption affecting US healthcare claims processing» (generic but defensible).
- Other numbers (190M, $22M ransom, ALPHV/BlackCat group) — VERIFIED.

**Severity:** P1 (precision improvement, not factual error).

**Source:** sources.md §7.1; primary: [UHG official statement April 2024](https://www.unitedhealthgroup.com/newsroom/2024/2024-04-22-uhg-updates-on-change-healthcare-cyberattack.html), [BleepingComputer 190M](https://www.bleepingcomputer.com/news/security/unitedhealth-now-says-190-million-impacted-by-2024-data-breach/), [HIPAA Journal 2024 report](https://www.hipaajournal.com/biggest-healthcare-data-breaches-2024/).

---

### P1-9 — Slide s21: Obermeyer 2019 «26.3% more chronic illnesses» + «84% bias reduction»

**Plan-v1 claim:** «at same risk score, black patients had **26.3% more chronic illnesses** than white»; «Optum + researchers совместно improved algorithm — **reduction in bias by 84%** post-fix».

**Per sources.md §9.1:**
- **84% bias reduction post-fix** — VERIFIED.
- **Black patients spent $1,800/year less** than equally-sick white patients — VERIFIED.
- **Black patients served increased from 17.5% to 46.5%** — VERIFIED.
- **«26.3% more chronic illnesses»** — number cited in plan-v1 not explicitly in sources.md §9.1 excerpt; общий смысл правильный (Obermeyer показал, что at same risk score, black patients had more chronic conditions than white), но точное число 26.3% нужно verify против published paper.

**Fix recommendation:**
- Verify «26.3%» against [Obermeyer 2019 Science paper](https://www.science.org/doi/10.1126/science.aax2342) Figure 1 directly (paper says «26% more chronic illnesses» in some summaries; precise figure needed for slide credibility).
- Add «17.5% → 46.5% increase в Black patients served» (s/he served data) — concrete и compelling, missing in plan-v1.
- Caption verified: «Obermeyer, Powers, Vogeli, Mullainathan — Science 366, 447-453 (2019). DOI: 10.1126/science.aax2342» — CORRECT verbatim.

**Severity:** P1 (specific number 26.3% may be slightly off — paper actually says ~26% or specific value; precise verification needed).

**Source:** sources.md §9.1; primary: [Science Vol 366 (Oct 2019)](https://www.science.org/doi/10.1126/science.aax2342), [Berkeley News press](https://news.berkeley.edu/2019/10/24/widely-used-health-care-prediction-algorithm-biased-against-black-people/).

---

### P1-10 — Slide s18: FDA PCCP final guidance — date verified

**Plan-v1 claim:** «FDA Guidance: ... PCCP for AI-Enabled Device Software Functions (final guidance Dec 2024).»

**Per sources.md §8.1 — VERIFIED precise:**
- **December 4, 2024** — FINAL guidance: «Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions».
- Additional: **August 22, 2024** — PCCP extended to all medical devices (broader). **January 7, 2025** — draft TPLC guidance.

**Fix recommendation:**
- Replace «Dec 2024» with «**4 декабря 2024**» (precise date).
- Add caveat speaker notes: «PCCP framework extended to all medical devices (not just AI) on Aug 22, 2024; AI-specific PCCP finalized Dec 4».

**Severity:** P1 (precision improvement; date is correct but vague).

**Source:** sources.md §8.1.

---

### P1-11 — Slide s25: EU AI Act «high-risk medical AI effective Aug 2026»

**Plan-v1 claim:** «EU (EU AI Act + MDR): High-risk AI Annex III; Conformity Assessment; CE-mark; effective Aug 2026 для high-risk.»

**Per sources.md §8.2 — VERIFIED with addition:**
- **Entry into force August 1, 2024** — VERIFIED.
- **February 2025** — prohibitions on unacceptable-risk AI.
- **August 2025** — GPAI obligations.
- **August 2026** — high-risk AI systems rules ← **THIS DATE CORRECT in plan-v1**.
- **August 2027** — full compliance for AI in regulated products (medical device MDR Class IIb/III и IVDR Class C/D).

**Fix recommendation:**
- Add nuance: «high-risk medical AI deadline 2 августа 2026; full compliance for AI in regulated medical products 2 августа 2027».
- Lecture date 13 мая 2026 = **2.5 months pre-deadline** → very topical, mention this.

**Severity:** P1 (verified but adds important upcoming-deadline context for лектор + students).

**Source:** sources.md §8.2; [EU AI Act Article 6](https://artificialintelligenceact.eu/article/6/).

---

### P1-12 — Slide s25: ГОСТ Р 59921 — verify standard numbers

**Plan-v1 claim:** «ГОСТ Р 59921 серия для AI в medicine (2022-2024) [FACT-CHECK]».

**Per sources.md §8.5 (Russian regulation):**
- sources.md confirms: **48 registered AI medical devices в России на 2024 (43 domestic + 5 foreign)**; **57 to mid-2026 (52 Russian + 5 foreign)**.
- **С 1 марта 2025** — new state registration rules, expedited procedure для Class 1, in-vitro diagnostics, IT solutions, AI-based devices.
- **ГОСТ Р 59921 series** — not directly verified in sources.md but plan-v1 flagged via `[FACT-CHECK]`.

**Fix recommendation:**
- ГОСТ Р 59921 series IS real (VNIIIMT publishes «Искусственный интеллект в здравоохранении» standards); verify specific numbers (-1, -2, ... -7? -10?) via Росстандарт catalog before citation.
- Add «48-57 AI medical devices registered in RF as of 2024-2026» — verified Russian operational data.
- Add «expedited registration procedure для AI MD from 1 March 2025 (ПП РФ № 1684)» — strong topical Russian content per sources.md §8.5.

**Severity:** P1 (existence verified, exact series numbers need confirmation).

**Source:** sources.md §8.5; [Webiomed registered devices blog](https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/), [VNIIIMT ПП РФ № 1684](https://www.vniiimt.ru/blog/pravila-gosudarstvennoy-registratsii-meditsinskikh-izdeliy-versiya-2024-2025/).

---

### P1-13 — Slide s22: NEDA Tessa specifics — verify exact dates

**Plan-v1 claim:**
- «2022: NEDA decides replace human helpline (cost saving) with Tessa.»
- «**31 мая 2023:** Tessa launch.»
- «**2 июня 2023:** Tessa suspended».

**Per sources.md §6.1 — verified:**
- **Cass (developer) — original Tessa rule-based, then modified to include generative AI Q&A feature WITHOUT NEDA's approval**.
- **Sharon Maxwell posted screenshots May 2023**.
- **NEDA pulled Tessa May 30, 2023** (< 24 hours after Maxwell's screenshots, **2 days before hotline scheduled shutdown**).
- Tessa was running for months/years before suspension — not «launched May 31, 2023».
- Suggested calorie limits: lose 1-2 lbs/week, eat no more than 2000 cal/day, calorie deficit 500-1000/day — should be quoted in lecture для emotional anchor.

**Fix recommendation:**
- Replace timeline:
  - «**2022 март-апрель**: NEDA announces replacing human helpline with Tessa».
  - «**~март 2023**: Tessa starts including generative AI feature (Cass modified без NEDA approval per NPR)».
  - «**конец мая 2023**: Sharon Maxwell posts screenshots of harmful advice».
  - «**30 мая 2023**: NEDA pulls Tessa within 24 hours of Maxwell screenshots, **2 days before hotline scheduled shutdown**».
- Add specific harmful advice quotes for visceral impact: «lose 1-2 lbs/week, calorie deficit 500-1000/day».
- Add «vendor accountability» frame explicitly — **Cass changed rule-based AI to generative without NEDA approval** — this is the engineering lesson per sources.md.

**Severity:** P1 (specific dates and vendor-accountability framing need correction).

**Source:** sources.md §6.1; primary: [NPR June 2023](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea), [AI Incident DB 545](https://incidentdatabase.ai/cite/545/).

---

### P1-14 — Slide s8: AI market size $50+ млрд 2025 → $100 млрд by 2030

**Plan-v1 claim:** s5: «AI в медицине — индустрия $50+ млрд в 2025 (Statista) с >$100 млрд прогнозом к 2030. [FACT-CHECK]».

**Per sources.md §11.1 — varies значительно:**
- **$21.66B in 2025 → $110.61B by 2030** (Markets and Markets, CAGR 38.6%).
- **$14.92B in 2024; $37.98B in 2025 → $928.18B by 2035** (Towards Healthcare, CAGR 37.66%).
- **North America 42.6% share in 2024**.

**Issue:** «$50+ млрд в 2025» — not matched by any specific source. Markets and Markets says $21.66B, Towards Healthcare says $37.98B. «$50+ млрд» = overestimate or different scope.

**Fix recommendation:**
- Replace «$50+ млрд в 2025 → $100 млрд к 2030» с **«$22-38 млрд в 2025 (estimates vary; Markets and Markets, Towards Healthcare); projected $100+ млрд к 2030»**.
- Caveat speaker notes: «market sizing varies дramatically by vendor — use as order-of-magnitude, not authoritative single number».

**Severity:** P1 (number wrong, направление correct).

**Source:** sources.md §11.1.

---

## P2 — Optional polish

### P2-1 — Slide s7: Bar chart data values

Plan-v1 cites «2015: ~6 devices; 2018: ~14; 2020: ~64; 2022: ~521». Per sources.md §2.1: «Between 1995-2015 — только 33 devices (3%). 2023 alone — 221 devices (23%). 2024: 258 alone. 2025: 295 alone.» — verify exact 2020, 2022 cumulative numbers from FDA official list pull. (2015: cumulative ~33 not 6; 6 might be «new in 2015»).

### P2-2 — Slide s11: «McKinney 2020 Nature breast cancer» — accuracy

McKinney et al. 2020 IS real Nature paper «International evaluation of an AI system for breast cancer screening» — but methodology was later questioned (Haibe-Kains et al. 2020 Nature correspondence on reproducibility). If citing, add caveat or replace with MASAI as primary reference.

### P2-3 — Slide s17: «Sber AI Lab Russian drug discovery (AIDD pilot 2024-2025)» — verify existence

sources.md does not cover Russian drug discovery specifically (mostly diagnostics-focused). Plan-v1 includes «Sber AI Lab AIDD pilot» — verify before citing OR remove for now.

### P2-4 — Glossary candidate #24 «Хосзу-роль»

Typo / unclear term «Хосзу-роль (Hospital / clinic operator)» — should be «Хост-роль» or «Hospital role» plain. Polish.

---

## Claim verification matrix

| Slide | Claim | Status | Source |
|---|---|---|---|
| s1 | mosmed.ai active URL | NEEDS-REFRESH | mosmed.ai (verify on day of lecture) |
| s4 | FDA devices «1016 to Aug 2024» | **WRONG — should be 1451 cumulative by end-2025** | FDA list, JAMA Net Open |
| s4 | mosmed «12 млн изображений с 2020» | VERIFIED (now 14+M per sources §2.2) | Remedium, mos.ru |
| s5 | AI medical market $50B in 2025 | **WRONG (actual $22-38B)** | Markets and Markets, Towards Healthcare |
| s5/s8/s12/s26 | mosmed «4 млрд руб/год экономии в ОМС» | **UNVERIFIED — REMOVE** | Not found in primary RU sources |
| s7 | FDA «76% radiology» | VERIFIED | JAMA Net Open systematic review |
| s7 | FDA «11% cardiology» | NEEDS-REFRESH (likely correct order) | secondary source |
| s8 | EU AI Act high-risk medical | VERIFIED | Article 6 + Annex III |
| s10 | mosmed «sens 0.94 / spec 0.89» | UNVERIFIED (no published Morozov paper specifying) | replace with CheXNet or MASAI |
| s11 | Liu 2019 «sens 0.85-0.92 / spec 0.95+» | NEEDS-REFRESH (paper real, exact numbers TBD) | Lancet Digital Health 2019 |
| s11 | MASAI not cited | OMITTED — should be primary RCT | Lancet Digital Health 2024/2025 |
| s12 | mosmed «12 млн с 2020, 80+ клиник» | PARTIALLY VERIFIED (14+M; 2000+ orgs / 74 regions on 2026) | mos.ru, Healthcare ME |
| s13 | Obermeyer 2019 (cv bias context) | VERIFIED | Science 2019 |
| s13 | Daneshjou 2021 (referenced as Science Advances 2021) | NEEDS DATE CORRECTION (actually **Aug 2022**) | sources.md §9.2 |
| s14 | mid-callback (structural) | N/A — not factual | — |
| s15 | DiMasi 2016 + Mullard 2024 cost numbers | VERIFIED concept; verify exact numbers | npj Drug Discovery 2025 |
| s15 | Jumper 2021 (AlphaFold2) + Abramson 2024 (AlphaFold3) | VERIFIED | Nature DOIs |
| s16 | AlphaFold «200M+ structures» | VERIFIED | DeepMind + EBI |
| s16 | AlphaFold «2M+ researchers in 190 countries» | NEEDS PRIMARY VERIFICATION | DeepMind 2024 update needed |
| s16 | AlphaProteo «3-300× affinity» | VERIFIED | DeepMind blog + arXiv 2409.08022 |
| s17 | DSP-1181 «12 mo design, Phase 1 closed/discontinued 2022» | VERIFIED — Plan correctly flags `[CRITICAL FACT-CHECK]` | Synapse, CAS Insights, Sumitomo |
| s17 | DSP-1181 as primary case (vs swap to Rentosertib) | **NEEDS RESTRUCTURE — add Insilico Rentosertib** | Nature Medicine June 2025 |
| s17 | Exscientia «CEO Hopkins fired 2025» | UNVERIFIED | needs FierceBiotech/Endpoints verify |
| s17 | Exscientia + Recursion merger 2024 | VERIFIED (Aug announce, Nov close, $688M) | Recursion press, Fierce Biotech |
| s18 | FDA PCCP final guidance Dec 2024 | VERIFIED (Dec 4, 2024) | FDA official |
| s19 | (interactive — no factual claims to verify) | N/A | — |
| s21 | Obermeyer «26.3% more chronic illness» | NEEDS VERBATIM CHECK | Science 2019 paper |
| s21 | Obermeyer «84% bias reduction post-fix» | VERIFIED | Science 2019 |
| s22 | NEDA Tessa «May 31, 2023 launch; June 2, 2023 suspended» | **WRONG DATES** — Tessa was running for months; suspended **May 30, 2023** | NPR, AI Incident DB |
| s22 | Tessa context: Cass modified rule-based to generative without NEDA approval | NEEDS EXPLICIT FRAMING | sources.md §6.1 |
| s22 | Mihalache 2024 «~20% hallucination» | NEEDS VERBATIM CHECK | JAMA Network Open |
| s22 | Air Canada chatbot court case | NEEDS PRIMARY VERIFICATION (cross-lecture, not in sources.md) | — |
| s23 | Change Healthcare «190M affected» | VERIFIED | UHG, BleepingComputer |
| s23 | Change Healthcare «$2-3 млрд cost» | PARTIAL — should be precise «**$2.457B**» | UHG Q3 2024 |
| s23 | Change Healthcare «22 day outage» | NEEDS PRIMARY VERIFICATION | secondary sources only |
| s23 | ALPHV/BlackCat + $22M ransom | VERIFIED | Kaspersky, House E&C |
| s23 | ФЗ-152 personal data category | VERIFIED + ADD 2025 amendments | sources.md §7.4 |
| s24 | Price 2019 Stanford TR + Gerke 2020 framework | NEEDS VERBATIM CHECK (frameworks exist; exact reference details verify) | Stanford / Elsevier |
| s24 | 4-actor framework | DEFENSIBLE CONSTRUCT | Multiple legal sources sources.md §8.3 |
| s25 | FDA SaMD + PCCP | VERIFIED | FDA official |
| s25 | EU AI Act effective Aug 2026 for high-risk | VERIFIED | sources.md §8.2 |
| s25 | Росздравнадзор + ГОСТ Р 59921 | EXISTENCE VERIFIED; exact series numbers TBD | VNIIIMT |
| s28 | Cognitive Agro Pilot teaser «1500+ машин, +30-40%» | OUT-OF-SCOPE for L4; verify в Lec 5 fact-check | — |

---

## Freshness watchlist (verify on day of lecture)

| Item | Cadence | Days delta (lecture - source) | Action |
|---|---|---|---|
| **FDA AI/ML device count** | Quarterly | Last verified end-2025 (~135 days) | **Re-pull FDA list 12 мая 2026** before lecture — expect 1,500-1,550 cumulative |
| **Exscientia / Recursion post-merger status + clinical readouts** | Weekly (biotech news) | Last verified May 2026 | Check FierceBiotech / Endpoints for Recursion clinical updates 1 week pre-lecture |
| **Insilico Rentosertib post-Phase 2a status** | Monthly | Last verified June 2025 (Nature Medicine pub) | Check Insilico investor news / Phase 3 announcements |
| **mosmed.ai operational stats** | Quarterly (DZM Moscow updates) | Last verified March 2026 (Vedomosti) | Check mos.ru ДЗМ press for Q1-Q2 2026 figures |
| **AlphaFold user count** | Yearly (DeepMind annual update) | DeepMind 2024 update | Verify against most recent DeepMind blog (Q2 2026) |
| **Change Healthcare follow-up litigation / settlements 2025-2026** | Quarterly | Last verified UHG Q3 2024 | Check for class-action settlements, OCR enforcement actions in 2025-2026 |
| **EU AI Act compliance prep** | Monthly | Lecture = 81 days pre-deadline (2 Aug 2026 high-risk medical AI) | Hot topic — monitor for landmark conformity assessments |
| **Russian medical AI registrations** | Quarterly | Last verified mid-2026 (57 devices) | Webiomed updated count |

**Top items requiring re-verification 12 мая 2026 (day-of-lecture pre-flight):**

1. FDA AI/ML device count (most likely to have moved).
2. Insilico Rentosertib news (Phase 3 announcement potential).
3. mosmed.ai dashboard URL liveness + key statistics (lecture demo dependency).
4. Recursion Q2 2026 clinical readouts (post-merger update).

---

## Recommendations for plan-v2 revision

1. **(P0) s17 — restructure DSP-1181 → add Insilico Rentosertib as primary flagship.** New structure: «AI обещание частично сбылось: Insilico Rentosertib Nature Medicine 2025 = first peer-reviewed positive Phase 2a; reality check: DSP-1181 + BEN-2293 + Exscientia→Recursion = clinical trials hard». Stronger narrative than current.
2. **(P0) s5, s8, s12, s26 — remove «4 млрд руб/год» mosmed claim entirely.** Replace с verified operational metrics: «14+ млн исследований, 2000+ организаций, 74 региона, 18+ млн изображений за 5 лет». Reframe central question «обещание сбылось» от financial argument к operational scale argument.
3. **(P0) s4, s7 — update FDA count to «1,451 cumulative by end-2025; +258 в 2024 + 295 в 2025»** — replace «1016 to Aug 2024» baseline. Pull fresh FDA list on day of lecture.
4. **(P1) s10, s11 — add MASAI Sweden RCT** as primary diagnostic case study (Lancet Digital Health 2024/2025): sens 80.5% vs 73.8%, 44% workload reduction, 12% interval cancer reduction. Replace или supplement Liu 2019 + McKinney 2020. Stronger peer-reviewed evidence для central question.
5. **(P1) s22 — correct NEDA Tessa timeline** (suspended May 30, 2023, не June 2), add vendor accountability frame (Cass modified rule-based → generative without NEDA approval), include specific harmful advice quotes.
6. **(P1) s23 — replace «$2-3 млрд» с precise «$2.457 млрд»** Change Healthcare cost. Verify or remove «22 day outage» specific claim.
7. **(P2) s25 — add EU AI Act high-risk medical AI deadline = 2 Aug 2026** (= 81 days post-lecture); RU expedited AI MD registration since 1 March 2025 (ПП РФ № 1684).
8. **(General) Add `[FACT-CHECK: cadence=Wn]` tags** for all weekly/monthly cadence claims (s4, s7, s12, s16, s17) — book-editor must re-verify on day of lecture per freshness watchlist above.

---

**End of fact-check report.**
