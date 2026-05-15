# Lecture 4 — Medicine & Pharma — Source Research

**Date:** 2026-05-13
**Researcher:** fact-checker subagent (deep-research pass)
**Purpose:** грунт для plan-v1 + chapter (Лекция 4 — AI в медицине и фармацевтике)
**LO coverage:** LO1, LO2, LO3, LO8 (ответственное использование)
**Audience:** студенты-инженеры (универсальная аудитория, не врачи)

---

## Index by section

| § | Тема | Sources |
|---|---|---|
| 1 | Drug discovery (DSP-1181, Insilico, AlphaFold 3, AlphaProteo, Recursion-Exscientia) | 12 |
| 2 | AI-диагностика (FDA list, mosmed.ai, IDx-DR, MASAI, Epic Sepsis, Aidoc/Tempus/PathAI) | 14 |
| 3 | Foundation models for biology (AlphaFold 3, ESM3, Evo 2, AlphaGenome) | 6 |
| 4 | Generative AI clinical reasoning (Med-PaLM 2, Med-Gemini, Goh, Kanjee) | 8 |
| 5 | LLM pattern «AI как объяснение для студента» | 4 |
| 6 | LLM anti-pattern (NEDA Tessa, hallucinations, adversarial) | 6 |
| 7 | Security (Change Healthcare, HIPAA, ФЗ-152, re-identification) | 8 |
| 8 | Responsibility (FDA PCCP, EU AI Act, malpractice, Росздравнадзор) | 8 |
| 9 | Ethics & bias (Obermeyer, Daneshjou, Adamson) | 4 |
| 10 | Russian context (mosmed.ai, Botkin.AI, Webiomed, СберМедИИ) | 7 |
| 11 | Indicator numbers 2024-2026 (market, adoption) | 5 |

**Total: ~82 source citations across 11 sections.** HIGH confidence: ~52, MEDIUM: ~22, LOW: ~8.

---

## Раздел 1 — Drug discovery

### 1.1 DSP-1181 — статус на май 2026 (КРИТИЧЕСКИЙ FACT)
**Claim:** DSP-1181, первый AI-designed препарат, попавший в clinical trials (Exscientia × Sumitomo Dainippon, январь 2020, обсессивно-компульсивное расстройство), **был discontinued после Phase 1** в 2022 году. Текущий R&D статус — Discontinued.
**Source:** [Synapse Drug Profile DSP-1181](https://synapse.patsnap.com/drug/a785db59b5d54d209ddfe8619dfcc2b0); [Sumitomo press 2020-01-30](https://www.sumitomo-pharma.com/news/20200130.html); [CAS Insights — AI drug discovery: first AI-designed drugs](https://www.cas.org/resources/cas-insights/ai-drug-discovery-assessing-the-first-ai-designed-drug-candidates-to-go-into-human-clinical-trials)
**Confidence:** HIGH
**Note:** Это **критическая поправка для лекции** — нельзя цитировать «12 мес vs 4-5 лет» как success story без оговорки «Phase 1 discontinued, drug never reached patients».

### 1.2 Exscientia × Recursion merger (август 2024 → ноябрь 2024)
**Claim:** Recursion + Exscientia объявили о слиянии 8 августа 2024 (all-stock $688M deal). Завершение — ноябрь 2024. Объединённая компания: Recursion HQ Salt Lake City, ~$850M cash, ~10 clinical readouts в 18 месяцев, 7 candidates от Recursion + 3 от Exscientia. Synergies ~$100M/год.
**Source:** [Recursion press release 2024-08-08](https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-enter-definitive-agreement-create); [Fierce Biotech — After tough year, Exscientia folds into Recursion](https://www.fiercebiotech.com/biotech/after-tough-year-exscientia-folds-recursion-create-ai-super-power); [PharmaPhorum $688M merger article](https://pharmaphorum.com/news/ai-biotechs-exscientia-and-recursion-agree-688m-merger)
**Confidence:** HIGH
**Note:** Merger сам по себе — сигнал, что AI drug discovery as standalone business is hard (Exscientia struggled financially despite Microsoft backing).

### 1.3 Insilico Medicine — ISM001-055 / INS018_055 / Rentosertib — IPF Phase 2a
**Claim:** Первое peer-reviewed proof-of-concept AI-driven drug discovery clinical validation. Phase IIa (NCT05938920) randomized double-blind placebo-controlled, n=71 patients across 21 China sites. Доза 60 mg QD (n=24) дала **+98.4 mL FVC (95% CI: 10.9–185.9) vs −20.3 mL placebo (95% CI: −116.1–75.6)** за 12 weeks; treatment effect ~118 mL. Most common AEs в 60 mg QD arm: diarrhea 14.8%, abnormal liver function 14.8%; TEAE rate 83.3% (60 mg QD) vs 70.6% (placebo). **Verified per Nature Medicine table (PubMed 40461817 abstract, WebFetch 2026-05-13).** Note: ранее в этой записи фигурировало placebo «−62.3 mL» — это была ошибка, исправлена в Phase 4 revision chapter v2 (2026-05-13).
**Publication:** **Nature Medicine, June 2025.**
**Source:** [Insilico press release: Nature Medicine publication June 2025](https://insilico.com/news/tnrecuxsc1-insilico-announces-nature-medicine-publi); [PubMed: A generative AI-discovered TNIK inhibitor for IPF: Phase 2a trial](https://pubmed.ncbi.nlm.nih.gov/40461817/); [Insilico Topline October 2024 PRNewswire](https://www.prnewswire.com/news-releases/insilico-medicine-announces-positive-topline-results-of-ism001-055-for-the-treatment-of-idiopathic-pulmonary-fibrosis-ipf-developed-using-generative-ai-302302583.html)
**Confidence:** HIGH
**Note:** Reframe для лекции: **«первый AI-designed drug с positive Phase IIa readout, опубликованным в peer-reviewed Nature Medicine»** — это replaces DSP-1181 как примарный success case на май 2026.

### 1.4 AlphaFold 3 — Nature May 2024
**Claim:** Опубликован 8 мая 2024 в Nature. Diffusion-based архитектура; теперь предсказывает structures of protein-DNA, protein-RNA, protein-ligand, ion complexes. **50% accuracy improvement vs best classical methods** на PoseBusters benchmark для protein-ligand. Первая AI system, surpassing physics-based docking tools.
**Source:** [Nature paper](https://www.nature.com/articles/s41586-024-07487-w); [Isomorphic Labs blog](https://www.isomorphiclabs.com/articles/alphafold-3-predicts-the-structure-and-interactions-of-all-of-lifes-molecules); [Nature commentary "AlphaFold 3.0: AI protein predictor gets upgrade"](https://www.nature.com/articles/d41586-024-01385-x)
**Confidence:** HIGH
**Note:** AlphaFold 2 (2021) → AlphaFold 3 (2024) shift = от proteins-only к full biomolecular complexes — это key narrative для «foundation models для биологии».

### 1.5 AlphaProteo — DeepMind September 2024
**Claim:** DeepMind announced 5 сентября 2024. Family of ML models для de novo protein binder design. **3-300× better binding affinity** vs best existing methods на семи protein targets. Для BHRF1 (viral protein): **88% of candidate molecules bound successfully** in DeepMind wet lab. First AI tool that designed successful binder for VEGF-A.
**Source:** [DeepMind blog AlphaProteo](https://deepmind.google/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/); [arXiv:2409.08022](https://arxiv.org/abs/2409.08022); [DeepMind PDF paper](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/AlphaProteo2024.pdf)
**Confidence:** HIGH

### 1.6 BenevolentAI — clinical setback
**Claim:** BEN-2293 (lead AI-derived candidate, eczema) failed Phase IIa efficacy → first high-profile AI-drug failure. После этого: layoffs 30%, US site closure, reverse merger with Osaka Holdings в начале 2025. Continues с BEN-8744 (PDE10 inhibitor, ulcerative colitis) и BEN-28010 (glioblastoma).
**Source:** [Leading AI-driven drug discovery platforms: 2025 landscape (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0031699725075118)
**Confidence:** MEDIUM
**Note:** Pair с DSP-1181 — два high-profile AI failures = healthy reality check для лекции (counters «AI drug timeline crushing»).

### 1.7 Generate Biomedicines — pipeline 2024-2025
**Claim:** GB-0895 (anti-TSLP monoclonal antibody) — Phase 1 results presented at European Respiratory Society International Congress (Amsterdam, 28 сентября 2025). Initiating global **Phase 3** studies for severe asthma в 2025. GB-7624 (anti-IL-13, atopic dermatitis) — Phase 1 в начале 2025.
**Source:** [Generate Biomedicines pipeline page](https://generatebiomedicines.com/pipeline); [GB Phase 1 results announcement](https://generatebiomedicines.com/media-center/generatebiomedicines-to-present-phase-1-results)
**Confidence:** HIGH

### 1.8 Atomwise — pipeline 2024
**Claim:** AtomNet platform — 250+ org partnerships, 600+ disease projects. Immunology — 4 proprietary assets в optimization. Plan submit IND H2 2024.
**Source:** [Atomwise official site](https://www.atomwise.com/); [GEN — Atomwise sets sights on inflammatory disease](https://www.genengnews.com/topics/artificial-intelligence/ai-based-drug-discovery-company-atomwise-sets-its-sights-on-inflammatory-disease-market/)
**Confidence:** MEDIUM

### 1.9 «12 months vs 4-5 years» — критический разбор
**Claim:** Традиционный preclinical drug discovery timeline: 12-15 years end-to-end, discovery + preclinical ~6 лет, lead identification до preclinical candidate ~4-5 лет. Insilico ISM001-055: target ID → preclinical candidate в **<18 месяцев** (что подтверждено их PR + verified в peer-reviewed Nature Medicine 2025 publication). НО: AI does not change ~90% clinical attrition rate. Phase 1 candidate в 2024 — ~6.7% chance to reach patients (down from ~10% decade ago).
**Source:** [The AI drug revolution needs a revolution — npj Drug Discovery 2025](https://www.nature.com/articles/s44386-025-00013-6); [Nature 2023 commentary — AI drug discovery needs reality check](https://www.nature.com/articles/d41586-023-03172-6); [Leading AI-driven drug discovery — Sci 2025](https://www.sciencedirect.com/science/article/abs/pii/S0031699725075118)
**Confidence:** HIGH
**Note:** Для лекции: AI ускоряет **discovery/preclinical** (один пайплайн-этап), а не clinical (3 пайплайн-этапа, ~80% timeline). Не overclaim «12 vs 60 месяцев на drug в целом» — corectно «discovery + preclinical timeline shortened, clinical attrition unchanged».

### 1.10 AI drug discovery 2025 landscape — общая картина
**Claim:** AI-discovered drugs are not yet a clinically validated revolution. Companies report acceleration of discovery, но clinical performance still bound by ~90% attrition. **2025 — Insilico's Nature Medicine paper = first peer-reviewed proof-of-concept**; everything else — company press releases.
**Source:** [npj Drug Discovery — The AI drug revolution needs a revolution](https://www.nature.com/articles/s44386-025-00013-6); [Drug Target Review — AI in drug discovery: 2025 in review](https://www.drugtargetreview.com/article/192951/ai-in-drug-discovery-2025-in-review/)
**Confidence:** HIGH

---

## Раздел 2 — AI-диагностика

### 2.1 FDA AI/ML medical device list — статистика на конец 2025
**Claim:** **1,451 cumulative authorized devices через конец 2025**; **258 AI devices authorized в 2024**; **295 new authorizations в 2025** (recent year). Radiology = **76%** всех authorizations (1,104 devices). Cardiology + neurology — следующие специальности. Between 1995-2015 — только 33 devices (3%). 2023 alone — 221 devices (23%).
**Source:** [FDA AI/ML enabled medical devices list (official)](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices); [JAMA Network Open — FDA Approval of AI/ML Devices in Radiology systematic review](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841066); [The Imaging Wire — FDA AI Approvals Surge Past 1k Dec 2025](https://theimagingwire.com/2025/12/10/ai-enabled-medical-devices-granted-fda-marketing-authorization/); [IntuitionLabs — FDA AI Medical Device List Stats](https://intuitionlabs.ai/articles/fda-ai-medical-device-tracker)
**Confidence:** HIGH

### 2.2 mosmed.ai — Moscow radiology AI Experiment
**Claim:** Эксперимент начат в ноябре 2019 как Moscow City project. **Over 5 years, ИИ проанализировал >14 миллионов radiology studies в Москве.** В мае 2024 — federal launch как «MosMedAI» nationwide service. На 2026: **2000+ медицинских организаций**, **74 региона РФ** подключены, **18+ миллионов** medical images processed, ~70 AI services across 43 clinical areas, **до 95% accuracy**, 11 национальных стандартов разработано, 300+ reference datasets.
**Source:** [mosmed.ai official](https://mosmed.ai/en/); [mos.ru news — MosMedAI wins AI Leaders Award](https://www.mos.ru/en/news/item/147773073/); [Healthcare ME — Moscow deploys AI 60+ diagnostic services](https://www.healthcaremea.com/2026/03/18/moscow-deploys-ai-across-the-healthcare-system-with-over-60-diagnostic-services/); [Remedium — За 5 лет ИИ проанализировал 14 млн исследований](https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/); [Webiomed corporate blog — РФ AI medical devices](https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/)
**Confidence:** HIGH (for studies count + service count + regions)

### 2.3 mosmed.ai «~4 миллиарда руб/год экономии в ОМС» — НЕ ПОДТВЕРЖДЕНО
**Claim:** Утверждение «~4 млрд руб/год экономии в ОМС от mosmed.ai».
**Verification:** Original source not found in official Moscow Healthcare Department press, в mosmed.ai/en/ai/ страница (operational metrics only — no financial figures), в TASS interview с главой Центра диагностики и телемедицины, или в публикациях НПКЦ ДиТ ДЗМ.
**Найденная похожая цифра:** «Moscow Healthcare digital transformation» (общая, не специфическая для mosmed.ai) — RUB 2.96 billion saved per year (но это broader healthcare digital, not radiology AI specifically). Также: один AI company earned ~2.75 billion rubles over 2.5 years (commercial, not OMS savings).
**Verdict:** [UNCERTAIN] — нужен оригинальный источник цифры «4 млрд/год». Возможные оригиналы: Moscow Department of Healthcare annual report, НПКЦ ДиТ ДЗМ публичный отчёт.
**Recommendation for lecture:** **Не цитировать «4 млрд руб/год экономии в ОМС»** без верифицированного источника. Использовать **операционные метрики** (14 млн studies, 74 региона, 70 сервисов, 11 нацстандартов) — они подтверждены и эффектные.
**Source:** [Mos.ru AI Leaders Award](https://www.mos.ru/en/news/item/147773073/); [mosmed.ai operational page](https://mosmed.ai/en/ai/); [TASS interview Center for Diagnostics and Telemedicine](https://tass.ru/interviews/19814421); [Vedomosti — Moscow AI helps doctors nationwide March 2026](https://www.vedomosti.ru/press_releases/2026/03/18/moskovskii-ii-pomogaet-vracham-po-vsei-strane-uzhe-provereno-10-mln-snimkov)
**Confidence:** LOW (4 млрд figure not verified)

### 2.4 IDx-DR (LumineticsCore) — diabetic retinopathy AI
**Claim:** FDA De Novo authorization April 2018 — first autonomous AI medical device, first AI for diabetic retinopathy. **Pooled sensitivity 93-95% / pooled specificity 91-93%** (hierarchical meta-analysis 2025). Real-world challenges: **adoption <5%** of US diabetic patients receive AI ophthalmic screening; **26.1% of images unanalyzable** by IDx-DR (factors: pupil size, age, visual acuity). 3 FDA-cleared autonomous DR AI products: IDx-DR (Digital Diagnostics), EyeArt (EyeNuk), AEYE Health.
**Source:** [American Journal of Ophthalmology — IDx-DR diagnostic accuracy meta-analysis 2025](https://www.ajo.com/article/S0002-9394(25)00081-9/abstract); [Scientific Reports — Real-world IDx-DR performance](https://www.nature.com/articles/s41598-026-36970-9); [npj Digital Medicine — Pivotal trial 2018](https://www.nature.com/articles/s41746-018-0040-6); [Retina Specialist — AI for DR screening Where are we in 2025](https://www.retina-specialist.com/article/ai-for-dr-screening-where-are-we-in-2025); [npj Digital Medicine — Systematic review approved DR AI 2025](https://www.nature.com/articles/s41746-025-02223-8)
**Confidence:** HIGH

### 2.5 MASAI trial — Sweden mammography AI RCT
**Claim:** Mammography Screening with AI trial, Sweden. >100,000 women (Apr 2021 – Dec 2022), randomized AI-supported vs standard double reading. **Sensitivity 80.5% (AI) vs 73.8% (standard)** at same specificity 98.5%. **Cancer detection rate 6.4 vs 5.0 per 1000** (ratio 1.29). False positives: 1.5% vs 1.4% (essentially equal). **44% reduction in radiologist workload.** Full results in The Lancet (2025-2026): **12% reduction in interval breast cancers** in years following AI-supported screening. **First peer-reviewed RCT of AI mammography.**
**Source:** [Lancet Digital Health MASAI screening accuracy 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00267-X/fulltext); [Lancet 2025 — Interval cancer MASAI](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract); [Lancet Oncology — MASAI clinical safety 2023](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(23)00298-X/abstract); [PubMed MASAI Lancet Digital Health Feb 2025](https://pubmed.ncbi.nlm.nih.gov/39904652/); [Eurekalert MASAI press](https://www.eurekalert.org/news-releases/1114399)
**Confidence:** HIGH
**Note:** MASAI = strongest peer-reviewed AI diagnostic evidence на 2026 для лекции. Лучше DSP-1181 для иллюстрации «AI reaches clinical reality».

### 2.6 Epic Sepsis Model — Wong et al. JAMA Internal Medicine 2021
**Claim:** External validation в University of Michigan (38,455 hospitalizations Dec 2018 – Oct 2019). **ESM v1: sensitivity 33%, specificity 83%, PPV 12%, NPV 95%, AUC 0.63.** «Poor predictor due to low sensitivity, inadequate calibration, alert fatigue». **November 2024 update — ESM v1.0 ESPMv1 re-validation** at 2 county EDs (Jan-Dec 2023) — research ongoing. Epic не публиковал отдельную peer-reviewed re-evaluation revised model.
**Source:** [JAMA Internal Medicine — Wong 2021 external validation Epic Sepsis Model](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307); [PMC — 2024 ESPMv1 ED study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560849/); [JAMA Editorial — Epic Sepsis Model falls short — importance of external validation](https://pubmed.ncbi.nlm.nih.gov/34152360/)
**Confidence:** HIGH
**Note:** Excellent case study для лекции: «vendor-promised AI failed external validation; trusted blindly без human-in-loop = alert fatigue + patient harm risk».

### 2.7 Aidoc — radiology AI adoption
**Claim:** 20 algorithms cleared, deployed в 900+ hospitals (2023). January 2026 — **FDA clearance for first foundation model AI** that triages 14 critical findings from single abdominal CT (post Breakthrough Device Designation Sep 2025). **1,600+ medical centers worldwide, 150+ US health systems.**
**Source:** [Aidoc press release foundation model FDA 2026](https://www.prnewswire.com/news-releases/aidoc-secures-fda-clearance-for-healthcares-first-comprehensive-foundation-model-ai-302666640.html); [Aidoc Breakthrough Device Designation 2025](https://www.prnewswire.com/news-releases/aidoc-receives-fda-breakthrough-device-designation-for-first-of-kind-ai-solution-spanning-numerous-acute-conditions-in-ct-302570535.html); [Wikipedia — Aidoc](https://en.wikipedia.org/wiki/Aidoc)
**Confidence:** HIGH

### 2.8 Tempus — clinical AI + diagnostics
**Claim:** NASDAQ IPO 2024. **Q3 2025 revenue $334.2M (+85% YoY), 217,000 clinical tests delivered.** FDA 510(k) for ECG-Low EF AI. **«David» — generative AI clinical co-pilot launched 2025**, first integration: Northwestern Medicine.
**Source:** [IntuitionLabs — Evolution of AI clinical decision support](https://intuitionlabs.ai/articles/ai-clinical-decision-support-evolution); [MedTech Spectrum — 2025 Index 100 AI medical devices](https://medtechspectrum.com/analysis/12/24541/the-2025-index-100-fda-approved-ai-driven-medical-devices.html)
**Confidence:** MEDIUM (revenue/integration confirmed; FDA ECG-Low EF approval verified separately)

### 2.9 PathAI — research stage
**Claim:** PathAI и Paige collaborate с pharma на companion diagnostics. **PathAI ещё не имеет FDA clearance** для clinical use; product remains в research-use mode.
**Source:** [IntuitionLabs AI clinical decision support evolution](https://intuitionlabs.ai/articles/ai-clinical-decision-support-evolution)
**Confidence:** MEDIUM

---

## Раздел 3 — Foundation models for biology

### 3.1 ESM3 — EvolutionaryScale, June 2024
**Claim:** Launched 25 июня 2024 + $142M seed. **Multimodal generative LM** reasoning over protein sequence + structure + function. **98 billion parameters, trained 1.07e24 FLOPs on 2.78 billion proteins + 771 billion tokens.** Generated novel fluorescent protein at **58% sequence identity** from known FPs — equivalent to «500 million years of evolution simulated».
**Source:** [EvolutionaryScale blog ESM3 release](https://www.evolutionaryscale.ai/blog/esm3-release); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2024.07.01.600583v1); [Science paper](https://www.science.org/doi/10.1126/science.ads0018); [Amazon press release](https://press.aboutamazon.com/aws/2024/6/evolutionaryscale-launches-with-esm3-a-milestone-ai-model-for-biology)
**Confidence:** HIGH

### 3.2 Evo 2 — Arc Institute, February 2025
**Claim:** **40B parameters, 1 megabase context**, trained on 9 trillion nucleotides from 100,000+ species. Predicts genetic variant functional impact **without task-specific fine-tuning**. BRCA1: **90% accuracy** predicting whether unknown mutation affects gene function. Preprint Feb 2025 (largest open biological AI model), Nature publication March 2026.
**Source:** [Arc Institute Evo 2 page](https://arcinstitute.org/tools/evo); [Nature paper](https://www.nature.com/articles/s41586-026-10176-5); [bioRxiv preprint Feb 2025](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1); [NVIDIA BioNeMo blog](https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/)
**Confidence:** HIGH

### 3.3 AlphaGenome — DeepMind, June 2025
**Claim:** Announced preprint + blog June 2025. **Processes 1 million base-pairs at once, single-nucleotide resolution.** Outputs predictions across thousands of molecular modalities (gene expression, chromatin accessibility, splicing, protein binding). **SoTA on 24/26 variant effect benchmarks.** Source code released January 2026. **3,000 scientists from 160 countries** using it (per Arc Institute / DeepMind tracking).
**Source:** [DeepMind blog AlphaGenome](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/); [STATnews — AlphaGenome launch June 2025](https://www.statnews.com/2025/06/25/google-ai-deepmind-launches-alphagenome-new-model-to-predict-dna-encoding-gene-regulation/); [Nature paper](https://www.nature.com/articles/s41586-025-10014-0); [STATnews — Source code release Jan 2026](https://www.statnews.com/2026/01/28/deepmind-opens-alphagenome-source-code/)
**Confidence:** HIGH

### 3.4 AlphaFold 3 — biology impact summary
Combined со §1.4: foundation model timeline для лекции: AF2 (2021) → AF3 (May 2024) → AlphaProteo (Sep 2024) → AlphaGenome (Jun 2025) → ESM3 (Jun 2024) → Evo 2 (Feb 2025).
**Confidence:** HIGH

---

## Раздел 4 — Generative AI in clinical reasoning

### 4.1 Med-PaLM 2 — Google Research
**Claim:** **86.5% accuracy** на MedQA (USMLE-style). First LLM at «expert» test-taker level. Published Nature Medicine **January 2025**. Compared favorably vs GPT-4 / GPT-3.5 on physician safety ratings, no significant subgroup bias.
**Source:** [Nature Medicine — Toward expert-level medical question answering](https://www.nature.com/articles/s41591-024-03423-7); [arXiv:2305.09617](https://arxiv.org/abs/2305.09617); [PMC — Med-PaLM 2 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11922739/)
**Confidence:** HIGH

### 4.2 Med-Gemini — Google Research
**Claim:** Med-Gemini-L 1.0 — **91.1% on MedQA**, outperforming Med-PaLM 2 by 4.6 percentage points. **NEJM CPC complex diagnostic challenges — top-10 accuracy +13.2%** vs previous SoTA (AMIE).
**Source:** [arXiv:2404.18416 — Capabilities of Gemini Models in Medicine](https://arxiv.org/html/2404.18416v2); [Google Research blog — Med-Gemini](https://research.google/blog/advancing-medical-ai-with-med-gemini/)
**Confidence:** HIGH

### 4.3 Goh et al. — JAMA Network Open October 2024 + Nature Med 2025 (Crucial RCT)
**Claim 1 (diagnostic reasoning RCT, JAMA Net Open Oct 2024):** Conducted Nov 29 – Dec 29, 2023. Family/internal/emergency medicine MDs randomized to GPT-4 vs conventional resources на clinical vignettes. **Median diagnostic reasoning score 76.3% (GPT-4) vs 73.7% (conventional)** — adjusted difference 1.6 pp (p=0.60, не значимо). Surprising finding: **GPT-4 alone scored higher than doctors-with-GPT-4** in side test — i.e., physicians didn't fully leverage AI suggestions.
**Claim 2 (management reasoning, Nature Medicine 2025):** Nov 2023 – April 2024, 92 physicians, 5 vignettes. Physicians with GPT-4 + conventional **scored 6.5 pp higher** (95% CI 2.7-10.2, p<0.001) vs conventional alone.
**Source:** [JAMA Network Open — LLM influence on diagnostic reasoning RCT 2024](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395); [JAMA Net Open editorial response](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825399); [PubMed — GPT-4 assistance for physician performance RCT 2025](https://pubmed.ncbi.nlm.nih.gov/39910272/); [ScienceDaily summary](https://www.sciencedaily.com/releases/2024/04/240401142448.htm)
**Confidence:** HIGH
**Note:** **Critical для лекции** — РКИ показывает, что доктор+AI ≈ доктор без AI на диагностику, но AI alone > both groups. = «automation bias» risk и недозагрузка AI в реальной практике.

### 4.4 Kanjee, Crowe, Rodman — JAMA 2023 (NEJM Case Challenge)
**Claim:** GPT-4 на 70 NEJM Clinicopathological Conference cases (Jan 2017 – Jan 2023). **Correct diagnosis in differential: 64% (45/70). Correct top diagnosis: 39% (27/70).** Outperformed 99.98% of simulated readers based on online answers.
**Source:** [PMC — Kanjee 2023 Accuracy of GAI in Complex Diagnostic Challenge](https://pmc.ncbi.nlm.nih.gov/articles/PMC10273128/); [NEJM AI Use of GPT-4 to Diagnose Complex Clinical Cases](https://ai.nejm.org/doi/full/10.1056/AIp2300031); [Eric Topol Ground Truths newsletter](https://erictopol.substack.com/p/stump-the-medical-expert)
**Confidence:** HIGH

### 4.5 LLM hallucination rates in medical Q&A
**Claim:** Baseline GPT-4 ~63% hallucination rate в clinical Q&A; DeepSeek-R1 ~48%; SoTA medical LLMs 15-40%. **«Adversarial hallucination» study (Communications Medicine 2025):** 6 leading LLMs on 300 clinical vignettes with single fake lab/sign/disease — models **repeat/elaborate on fake error in up to 83% of cases**. Mitigation prompt halves rate but not eliminates. Fabricated citations: >30% of chatbot answers in research contexts. GPT-4o citations: 6% fabricated for major depression vs **28-29% fabricated** for binge eating/body dysmorphic disorder (Stanford).
**Source:** [Nature — Multi-model assurance LLMs adversarial hallucination](https://www.nature.com/articles/s43856-025-01021-3); [Stanford HAI — Generating medical errors GenAI](https://hai.stanford.edu/news/generating-medical-errors-genai-and-erroneous-medical-references); [npj Digital Medicine — Framework clinical safety LLM medical text](https://www.nature.com/articles/s41746-025-01670-7); [arXiv:2503.05777 Medical Hallucination Foundation Models](https://arxiv.org/html/2503.05777v2); [JMIR Medical Informatics — Reference Hallucination Score 2024](https://medinform.jmir.org/2024/1/e54345)
**Confidence:** HIGH

---

## Раздел 5 — LLM pattern: «AI как объяснение для студента 2 курса»

### 5.1 AI for layperson medical translation — controlled trial
**Claim:** AI-INFOCARE и AI-MEDTALK RCT — patients randomized to AI-generated layperson-language translations of medical documents pre-consultation. Evidence base growing 2024-2025.
**Source:** [PMC — Layperson-friendly AI Translation Medical Docs RCT protocol 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12680933/)
**Confidence:** MEDIUM

### 5.2 ChatGPT simplifies medical text reading level
**Claim:** ChatGPT reduced Patient Information article from **11th-grade to 9th-grade** reading level; Plain Language Summary **17th-grade to 11th-grade**. НО: не достигла target **6th-grade** для всех inputs (limitation).
**Source:** [Rheumatology Advisor — AI Language Models simplify patient education](https://www.rheumatologyadvisor.com/features/use-of-ai-to-create-patient-education-materials/)
**Confidence:** HIGH

### 5.3 LLMs in patient education — scoping review
**Claim:** Frontiers in Medicine scoping review (2024): 6 themes — patient ed materials generation, medical info interpretation, lifestyle recs, medication use, perioperative instructions, doctor-patient interaction optimization.
**Source:** [Frontiers in Medicine — LLMs in patient education scoping review 2024](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1477898/full)
**Confidence:** HIGH

### 5.4 Khan Academy Khanmigo + medical/biology learning
**Claim:** Khanmigo (AI tutor, Khan Academy) piloted March 2023. By 2024 — 260+ districts. $4/month. **Note:** focused K-12 / general academic, includes biology, но **not specialized medical education**. Used by Microsoft partnership for 40+ countries (2024).
**Source:** [Khan Academy Khanmigo official site](https://www.khanmigo.ai/); [Khan Academy Blog — Unlimited Biology Tutoring $4/mo](https://blog.khanacademy.org/unlimited-biology-tutoring-for-4-month/); [CNBC — Microsoft+Khan Academy free AI assistant teachers May 2024](https://www.cnbc.com/2024/05/21/microsoft-khan-academy-launch-free-ai-assistant-for-all-us-teachers.html)
**Confidence:** HIGH
**Note:** Для лекции — **подходящая аналогия**, не direct use case (medical-specific tutoring is more like Med-PaLM/UpToDate copilot territory).

---

## Раздел 6 — LLM anti-pattern: trust without verification

### 6.1 NEDA Tessa chatbot scandal — May/June 2023 (CRITICAL CASE)
**Claim:** National Eating Disorders Association (NEDA) replaced unionizing human helpline staff с rule-based chatbot «Tessa». **Cass (developer) changed Tessa без NEDA's approval** to use generative AI / Q&A feature. Tessa told users to: **lose 1-2 pounds/week, eat no more than 2000 cal/day, calorie deficit 500-1000/day** (= classic eating disorder triggers). Eating disorder activist Sharon Maxwell posted screenshots May 2023. **NEDA pulled Tessa May 30, 2023** (< 24h after Maxwell's screenshots, 2 days before hotline scheduled shutdown). Psychologist Alexis Conason replicated identical harmful interactions.
**Source:** [NPR — Eating disorders chatbot offered dieting advice June 2023](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea); [CBS — Eating disorder helpline shuts down AI chatbot](https://www.cbsnews.com/news/eating-disorder-helpline-chatbot-disabled/); [CNN Business — NEDA takes chatbot offline harmful advice](https://www.cnn.com/2023/06/01/tech/eating-disorder-chatbot/); [Psychiatrist.com — NEDA suspends AI chatbot](https://www.psychiatrist.com/news/neda-suspends-ai-chatbot-for-giving-harmful-eating-disorder-advice/); [AI Incident Database — Incident 545 Tessa](https://incidentdatabase.ai/cite/545/); [Fortune — NEDA yanks chatbot replaced helpline staff](https://fortune.com/well/2023/05/31/neda-ai-chatbot-harmful-advice/)
**Confidence:** HIGH
**Note:** **#1 anti-pattern case** для лекции — вендор поменял rule-based на generative AI без согласования с принципалом, и AI начал давать совет, угрожающий жизни. Lesson: **vendor accountability + human oversight + generative AI != rule-based AI**.

### 6.2 ChatGPT clinical mistakes — Stanford documented
**Claim:** Stanford study found **4/5 models hallucinated significant proportion of sources** (invalid URLs). GPT-4 RAG: **up to 30% of statements unsupported**; **nearly half of responses contain ≥1 unsupported statement.** Gemini Pro: only **10% of responses fully supported**.
**Source:** [Stanford HAI — Generating Medical Errors](https://hai.stanford.edu/news/generating-medical-errors-genai-and-erroneous-medical-references); [StudyFinds — ChatGPT references fabricated GPT-4o study](https://studyfinds.org/chatgpts-hallucination-problem-fabricated-references/)
**Confidence:** HIGH

### 6.3 Patient self-diagnosis with ChatGPT — adoption
**Claim:** **40 million Americans** use ChatGPT for healthcare questions (OpenAI report). **3 in 5 US adults** used AI tools for health past 3 months (OpenAI survey). **25% US adults** used AI/chatbot for healthcare info (Gallup). **32%** of 2025 Consumer Adoption Digital Health Survey — up from 16% in 2024. **55%** of AI-health-users use for symptom check, **44%** for treatment options. ChatGPT 23%, Gemini 15% top platforms.
**Source:** [Becker's Hospital Review — 40M Americans use ChatGPT healthcare](https://www.beckershospitalreview.com/healthcare-information-technology/ai/40m-americans-turn-to-chatgpt-for-healthcare-report/); [Fierce Healthcare — AI chatbot use up 16% Rock Health survey](https://www.fiercehealthcare.com/ai-and-machine-learning/ai-chatbot-use-health-information-16-2024-rock-health-survey); [Gallup — Americans turning to AI supplement healthcare visits](https://news.gallup.com/poll/707789/americans-turning-supplement-healthcare-visits.aspx); [JMIR — Adoption AI-generated health info US 2024](https://www.jmir.org/2024/1/e55138)
**Confidence:** HIGH
**Note:** Massive adoption signal — даже если AI not safe для self-diagnosis, **40M people already doing it** = регулирование не успевает. Сильная для лекции number.

### 6.4 LLM hallucination — clinically dangerous failure modes
Cross-ref §4.5 — adversarial vignettes 83% rate, fabricated citations, treatment hallucinations.

---

## Раздел 7 — Security и приватность медицинских данных

### 7.1 Change Healthcare ransomware — February 2024 (BIGGEST CASE)
**Claim:** Attack date **21 февраля 2024**. ALPHV BlackCat ransomware group (Russian). Vector: vulnerable Citrix remote access без MFA. **190 million Americans** PHI stolen — **largest healthcare data breach in US history** (≈82% of US population had records exposed in 2024 across all breaches). **6 TB** of data exfiltrated. **$22M Bitcoin ransom paid.** **$2.457 billion** total cost (UHG Q3 2024). 192,700,000 individuals affected — **66.7%** of total 2024 healthcare breach population.
**Source:** [UHG official statement April 2024](https://www.unitedhealthgroup.com/newsroom/2024/2024-04-22-uhg-updates-on-change-healthcare-cyberattack.html); [BleepingComputer — UnitedHealth 190M impacted](https://www.bleepingcomputer.com/news/security/unitedhealth-now-says-190-million-impacted-by-2024-data-breach/); [AHA — Change Healthcare cyberattack urgent preparedness](https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and); [HIPAA Journal — Biggest healthcare data breaches 2024](https://www.hipaajournal.com/biggest-healthcare-data-breaches-2024/); [Kaspersky — Complete story UnitedHealth ransomware](https://www.kaspersky.com/blog/unitedhealth-ransomware-attack/53065/); [House Energy & Commerce — What We Learned](https://energycommerce.house.gov/posts/what-we-learned-change-healthcare-cyber-attack)
**Confidence:** HIGH
**Note:** **#1 case** для security раздела. NB: russian group attacked US healthcare — нюанс для российской аудитории, обсуждай аккуратно.

### 7.2 Healthcare data breach statistics 2024
**Claim:** OCR portal: **725 breaches of 500+ records в 2024**, total **289,162,330 individuals** PHI exposed/disclosed = ~82% of US population. **18 mega breaches** (>1M records each) в 2024. Network servers — 61.5% of breaches; email accounts — 24.9%. 2025: down to **61,556,256 individuals** (-78.7%) и **642 breaches** (-13.5%) — 9 mega breaches only.
**Source:** [HIPAA Journal 2024 Healthcare Data Breach Report](https://www.hipaajournal.com/2024-healthcare-data-breach-report/); [HIPAA Journal 2025 Healthcare Data Breach Report](https://www.hipaajournal.com/2025-healthcare-data-breach-report/); [OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf); [Healthcare Data Breach Statistics 2026 Update](https://www.hipaajournal.com/healthcare-data-breach-statistics/)
**Confidence:** HIGH

### 7.3 HIPAA — de-identification limits
**Claim:** Sweeney's foundational k-anonymity work (2002): k-anonymity model для protecting privacy. **First attack — 1997: Sweeney re-identified Governor of Massachusetts medical records** using voter rolls + public data. **2018 study — re-identified patients from HIPAA-compliant datasets** using public newspaper aggregation. Stanford HAI: «de-identification ≠ anonymization; cannot guarantee no re-identification»; Nature Medicine 2023: «HIPAA is a misunderstood and inadequate tool».
**Source:** [HHS HIPAA De-identification Guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html); [Harvard Online — Anonymity, De-Identification, Data Accuracy](https://harvardonline.harvard.edu/blog/anonymity-de-identification-accuracy-data); [Stanford HAI — De-identifying Medical Patient Data Doesn't Protect Privacy](https://hai.stanford.edu/news/de-identifying-medical-patient-data-doesnt-protect-our-privacy); [PMC — Re-identification Risks HIPAA Safe Harbor 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6344041/); [PMC — Privacy engineering anonymised healthcare 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11885643/); [HIPAA Journal — De-identification PHI 2026 Update](https://www.hipaajournal.com/de-identification-protected-health-information/)
**Confidence:** HIGH

### 7.4 ФЗ-152 — Russian personal data law, 2024-2025 updates
**Claim:** Federal Law N 152-ФЗ «О персональных данных» (27.07.2006). **Major amendments effective 30 мая 2025**: significantly tighter operator requirements, increased fines (depend on violator + scale). **С 1 сентября 2025**: consent for personal data processing must be separate document, not user agreement clause. **С 1 июля 2025 (Federal Law N 23-ФЗ, 28 февраля 2025)**: personal data of Russian citizens cannot be processed/stored on databases located outside Russia (data localization).
**Source:** [КонсультантПлюс — ФЗ-152](https://www.consultant.ru/document/cons_doc_LAW_61801/); [ГАРАНТ — Закон о персональных данных](https://base.garant.ru/12148567/); [Стахановец — 152-ФЗ требования и штрафы 2026](https://stakhanovets.ru/blog/152-fz-o-zashhite-personalnyh-dannyh-trebovaniya-i-shtrafy-v-2026-godu/); [Контур.Норматив — 152-ФЗ от 24.06.2025](https://normativ.kontur.ru/document?moduleId=1&documentId=501173); [Минздрав — ФЗ-152 публикация](https://minzdrav.gov.ru/documents/5402-federalnyy-zakon-152-fz-ot-27-iyulya-2006-g)
**Confidence:** HIGH
**Note:** ФЗ-152 + ФЗ-23 (data localization) — для лекции = «Россия требует локализации медицинских данных», т.е. использование OpenAI / Anthropic API напрямую для PHI пациентов = nonconformance.

### 7.5 GDPR + medical AI
**Claim:** Combined с EU AI Act (§ 8.2) creates compound regulation для medical AI in EU. Sensitive data special category (Art 9 GDPR) + High-risk AI obligations (AI Act Art 6).
**Source:** Cross-ref EU AI Act sources §8.2
**Confidence:** MEDIUM

---

## Раздел 8 — Responsibility / liability AI-диагностики

### 8.1 FDA AI/ML Action Plan + PCCP
**Claim:** **AI/ML SaMD Action Plan published January 2021.** **March 15, 2024**: FDA «AI and Medical Products: How CBER/CDER/CDRH/OCP Working Together» — coordinated approach. **June 2024**: Transparency for ML-Enabled Devices Guiding Principles. **December 4, 2024**: **FINAL guidance — Marketing Submission Recommendations for PCCP for AI-Enabled Device Software Functions** — manufacturers can pre-authorize device modifications instead of new marketing application. **January 7, 2025**: draft TPLC guidance. **August 22, 2024**: PCCP extended to all medical devices.
**Source:** [FDA — AI Software as Medical Device](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device); [FDA AI Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices); [FDA — Marketing Submission PCCP final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence); [Ropes & Gray — FDA finalizes PCCP guidance Dec 2024](https://www.ropesgray.com/en/insights/alerts/2024/12/fda-finalizes-guidance-on-predetermined-change-control-plans-for-ai-enabled-device); [IntuitionLabs FDA PCCP Implementation Guide](https://intuitionlabs.ai/articles/fda-pccp-implementation-guide-ai-ml-samd); [Ballard Spahr — FDA Issues Guidance AI Medical Devices 2025](https://www.ballardspahr.com/insights/alerts-and-articles/2025/08/fda-issues-guidance-on-ai-for-medical-devices)
**Confidence:** HIGH

### 8.2 EU AI Act — medical device high-risk classification
**Claim:** **Entry into force 1 августа 2024**. Phased implementation: **February 2025** — prohibitions on unacceptable-risk AI. **August 2025** — GPAI obligations. **August 2026** — high-risk AI systems rules. **August 2027** — full compliance для AI in regulated products (medical device MDR Class IIb/III и IVDR Class C/D). MDAI (Medical Device AI) is High-Risk under Article 6(1) если: safety component or medical device itself + requires third-party conformity assessment.
**Source:** [European Commission Health — AI in Healthcare](https://health.ec.europa.eu/ehealth-digital-health-and-care/artificial-intelligence-healthcare_en); [Reed Smith — EU AI Act Medical Devices Navigating High-Risk Compliance](https://www.reedsmith.com/our-insights/blogs/viewpoints/102kq35/the-eu-ai-act-and-medical-devices-navigating-high-risk-compliance/); [EU AI Act Article 6 — High-Risk Classification Rules](https://artificialintelligenceact.eu/article/6/); [Hunton — Impact of EU AI Act on Medical Devices](https://www.hunton.com/insights/legal/the-impact-of-the-eu-ai-act-on-the-development-and-use-of-medical-devices); [Trilateral — EU AI Act Implementation Timeline](https://trilateralresearch.com/responsible-ai/eu-ai-act-implementation-timeline-mapping-your-models-to-the-new-risk-tiers); [IntuitionLabs — EU AI Act Pharma Medical Device Compliance](https://intuitionlabs.ai/articles/eu-ai-act-pharma-medical-device-compliance)
**Confidence:** HIGH

### 8.3 Medical malpractice + AI — current state 2024-2025
**Claim:** **«No notable AI malpractice lawsuits yet»** as of mid-2025. 14% increase в malpractice claims involving AI tools 2024 vs 2022, mostly diagnostic AI (radiology, cardiology, oncology). **Dickson v. Dexcom Inc. (2024, Louisiana)** — first case considering FDA De Novo authorization preempting personal injury claims. **No landmark case strictly pertaining to AI medical malpractice** на 2025.
**Source:** [PMC — How Physicians Might Get in Trouble Using AI (or not using AI)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12309835/); [Medical Economics — New malpractice frontier AI](https://www.medicaleconomics.com/view/the-new-malpractice-frontier-who-s-liable-when-ai-gets-it-wrong-); [Healthcare Brew — Doctors liable AI mistake malpractice experts](https://www.healthcare-brew.com/stories/2025/04/01/doctors-liable-ai-mistake-malpractice); [Brandon Broderick — Medical Malpractice 2025 AI Healthcare](https://www.brandonjbroderick.com/medical-malpractice-2025-how-ai-healthcare-changing-lawsuits); [PMC — Defining medical liability artificial intelligence](https://pmc.ncbi.nlm.nih.gov/articles/PMC10711067/); [Sommers Schwartz — AI Misdiagnosed Liability](https://www.sommerspc.com/blog/2025/03/ai-misdiagnosed-liability/)
**Confidence:** HIGH
**Note:** **Honest framing для лекции:** liability law still catching up. Ключевой принцип-консенсус: **врач остаётся юридически ответственным** за final decision; AI = decision-support, not decision-maker.

### 8.4 Human in the loop — FDA/EMA framework
**Claim:** «AI systems should keep human decision-making firmly in the loop» — FDA guidance принцип. EU AI Act mandates Article 14 «Human oversight» для high-risk AI systems. **Liability remains with humans** unless software defect proven (manufacturer liability).
**Source:** Cross-ref §8.1, §8.2; [PMC — Ethical and regulatory challenges ML healthcare 2025](https://www.sciencedirect.com/science/article/pii/S2772485925000286)
**Confidence:** HIGH

### 8.5 Росздравнадзор regulation — AI medical devices
**Claim:** В 2023 — каждый субъект РФ обязан закупить и внедрить **не менее 1 МИ с ИИ**; в 2024 — **3 МИ с ИИ**. **48 registered AI medical devices в России на 2024** (43 domestic + 5 foreign); per Webiomed updated data — **57 to mid-2026** (52 Russian + 5 foreign). **С 1 марта 2025** — new государственная регистрация rules; **expedited procedure for Class 1, in-vitro diagnostics, IT solutions, AI-based devices.** Mandatory data transmission to Roszdravnadzor AIS for AI medical devices (separate order).
**Source:** [Webiomed — Зарегистрированные мед изделия с ИИ](https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/); [Roszdravnadzor — Государственная регистрация мед изделий](https://roszdravnadzor.gov.ru/medproducts/registration); [Medvestnik — Порядок передачи данных по ИИ-медизделиям](https://medvestnik.ru/content/news/poryadok-peredachi-roszdravnadzoru-dannyh-po-medizdeliyam-s-ii-gotovyat-k-pereizdaniu.html); [Кредо — Регистрация мед изделий 2025 руководство](https://kredo.moscow/informatsiya-o-registratsii-medizdelij/registratsiya-meditsinskikh-izdelij-v-rossii-polnoe-rukovodstvo-2025); [VNIIIMT — ПП РФ № 1684 правила регистрации](https://www.vniiimt.ru/blog/pravila-gosudarstvennoy-registratsii-meditsinskikh-izdeliy-versiya-2024-2025/)
**Confidence:** HIGH

---

## Раздел 9 — Ethics, bias

### 9.1 Obermeyer et al. — Science October 2019 (CRUCIAL)
**Claim:** Algorithm Impact Pro (sold by Optum) used to identify high-risk patients for complex needs systematically underestimated Black patients. Reason: algorithm used **health-care cost** as proxy for health-care need; Black patients spent **$1,800/year less** than equally-sick white patients → algorithm wrongly inferred lower need. **Retraining with proxy + chronic conditions reduced disparity by 84%.** Increased Black patients served from **17.7% to 46.5%** (per Science abstract verbatim).
**Source:** [Science Vol 366 (Oct 2019) — Obermeyer et al.](https://www.science.org/doi/10.1126/science.aax2342); [PubMed: Dissecting racial bias healthcare algorithm](https://pubmed.ncbi.nlm.nih.gov/31649194/); [Berkeley News press release](https://news.berkeley.edu/2019/10/24/widely-used-health-care-prediction-algorithm-biased-against-black-people/); [Scientific American — Racial Bias Major Health Care Algorithm](https://www.scientificamerican.com/article/racial-bias-found-in-a-major-health-care-risk-algorithm/)
**Confidence:** HIGH
**Note:** **Gold standard case** для bias раздела. Pre-2024 но фундаментальный пример = systemic bias через proxy variable. Ранее в этой записи фигурировало «17.5%» — это был верitable misquote, исправлен в Phase 4 revision chapter v2 (2026-05-13); абстракт Science говорит дословно «from 17.7 to 46.5%».

### 9.2 Daneshjou et al. — Science Advances August 2022
**Claim:** Tested previously published dermatology algorithms on diverse skin image database. **Algorithms performed much worse on Black/brown skin images.** Dermatologists also performed worse on dark skin tones vs ground truth biopsy annotations. Fine-tuning on diverse DDI dataset **closed performance gap**, and fine-tuned models **outperformed dermatologists on malignancy detection on dark skin**.
**Source:** [Science Advances — Disparities in Dermatology AI](https://www.science.org/doi/10.1126/sciadv.abq6147); [Stanford Medicine — Training Physicians and Algorithms Dermatology Diversity](https://med.stanford.edu/news/insights/2022/09/training-physicians-and-algorithms-in-dermatology-diversity.html); [PubMed Daneshjou disparities](https://pubmed.ncbi.nlm.nih.gov/35960806/)
**Confidence:** HIGH

### 9.3 Adamson & Smith — JAMA Dermatology 2018
**Claim:** Viewpoint paper on ML and skin of color in dermatology. **ISIC challenge archive heavily fair-skinned (US/Europe/Australia)**. AI has potential to routinely fail in darker skin cancers. **Risk of automating bias** — exclusion of skin types in training data exacerbates disparities.
**Source:** [JAMA Dermatology 2018 vol 154(11) pp 1247-1248](https://jamanetwork.com/journals/jamadermatology/article-abstract/2688587); [PubMed Adamson Smith](https://pubmed.ncbi.nlm.nih.gov/30073260/)
**Confidence:** HIGH

### 9.4 Recent dermatology bias work 2024-2026
**Claim:** DermDiff (generative diffusion for racial bias mitigation, arXiv 2503.17536). Continued underrepresentation analysis 2025 (Springer Current Dermatology Reports).
**Source:** [arXiv:2503.17536 — DermDiff Generative Diffusion Racial Bias](https://arxiv.org/html/2503.17536v1); [Springer — Skin Type Diversity Skin Lesion Datasets Review](https://link.springer.com/article/10.1007/s13671-024-00440-0)
**Confidence:** MEDIUM

---

## Раздел 10 — Russian context

### 10.1 mosmed.ai — cross-ref §2.2, §2.3
Подтверждённые операционные числа (см. §2.2). **4 млрд руб/год экономии в ОМС — NOT VERIFIED, не использовать без подтверждённого оригинала.**

### 10.2 Webiomed — clinical decision support
**Claim:** **Первый AI software** в РФ официально зарегистрированный как медицинское изделие **3 апреля 2020** (Roszdravnadzor RZN 2020/9958, Class 1). Predictive analytics + risk assessment. Implementation в SberMedAI Medical Digital Diagnostic Center. Lead Russian medical AI startup. **128.9 million rubles investment в 2023.** Подключен к Государственной информационной системе охраны здоровья.
**Source:** [Webiomed first registered Russian software](https://webiomed.ru/en/news/webiomed-system-first-registrated-russian-software-as-medical-device/); [Webiomed leading Russian startup](https://webiomed.ru/en/news/webiomed-is-a-leading-russian-startup-healthcare/); [Webiomed SberMedAI integration](https://webiomed.ru/en/news/the-webiomed-predictive-analytics-service-has-been-implemented-into-the-sbermedai-medical-digital-diagnostic-center/); [DynamicSun — Рейтинг российских стартапов AI здравоохранения 2024](https://dynamicsun.ru/ai-articles/rejting-rossijskih-startapov-v-sfere-iskusstvennogo-intellekta-dlya-zdravoohraneniya-2024-g); [Webiomed list registered software medical device](https://webiomed.ru/en/blog/the-list-of-software-registered-in-russia-as-a-medical-device/); [Webiomed regulation AI healthcare Russia](https://webiomed.ru/en/blog/regulation-of-artificial-intelligence-in-healthcare-in-russia/)
**Confidence:** HIGH

### 10.3 Botkin.AI — radiology imaging
**Claim:** Founded 2015, Moscow. CT/X-ray/mammography pathology detection. **30+ successful projects** в Russian regions + СНГ + Latin America + Middle East. Working with pharma + private clinics + state facilities с 2017. Focus: mammography, chest CT, brain CT automated analysis.
**Source:** [Botkin.AI About](https://botkin.ai/en/about); [Webiomed map — AI in Russian Healthcare](https://webiomed.ru/en/blog/the-map-artificial-intelligence-in-russian-health-care/); [Crunchbase Botkin.AI](https://www.crunchbase.com/organization/botkin-ai)
**Confidence:** HIGH

### 10.4 Care Mentor AI
**Claim:** Radiation diagnostics platform; registration certificate **December 2020**. Implemented в City Mariinsky Hospital.
**Source:** [Webiomed — AI in Russian Healthcare map](https://webiomed.ru/en/blog/the-map-artificial-intelligence-in-russian-health-care/)
**Confidence:** MEDIUM

### 10.5 SberMedAI — Sber ecosystem
**Claim:** Ecosystem operator для AI healthcare in Russia. Integrates Webiomed predictive analytics. Multiple institutional partnerships.
**Source:** [TAdviser — SberMedAI](https://tadviser.com/index.php/Company:SberMedAI); [LinkedIn SBERmed.AI](https://www.linkedin.com/company/sbermedai)
**Confidence:** MEDIUM (high-level claims confirmed; specific numbers not in search)

### 10.6 «Третье мнение» (Third Opinion) — additional Russian AI medical
**Claim:** 13 contracts в Russian regions (diagnostic + telemedicine centers). **Net profit 10.2 million rubles в 2023.** Top Russian medical AI vendor по revenue 2023.
**Source:** [DynamicSun rating 2024](https://dynamicsun.ru/ai-articles/rejting-rossijskih-startapov-v-sfere-iskusstvennogo-intellekta-dlya-zdravoohraneniya-2024-g)
**Confidence:** MEDIUM

### 10.7 Russian medical AI market size + adoption
**Claim:** **30+ companies** в Russian medical AI sector; **>60% работают в medical image analysis** (Third Opinion, Botkin.AI, Celsus). **24 из 30** компаний имеют Roszdravnadzor registration. На 2026: total **57 registered AI medical devices** (52 domestic + 5 foreign).
**Source:** [DynamicSun — Russian AI healthcare startups rating 2024](https://dynamicsun.ru/ai-articles/rejting-rossijskih-startapov-v-sfere-iskusstvennogo-intellekta-dlya-zdravoohraneniya-2024-g); [Webiomed — Map AI in Russian Healthcare](https://webiomed.ru/en/blog/the-map-artificial-intelligence-in-russian-health-care/); [Webiomed — registered AI medical devices](https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/)
**Confidence:** MEDIUM

---

## Раздел 11 — General industry numbers 2024-2026

### 11.1 AI in healthcare global market
**Claim:** **$21.66B в 2025 → $110.61B by 2030** (CAGR 38.6%) per Markets and Markets. Alternative: **$14.92B в 2024**; **$37.98B in 2025 → $928.18B by 2035** (CAGR 37.66%) per Towards Healthcare. **North America 42.6% share в 2024.**
**Source:** [Statista — AI healthcare market 2025](https://www.statista.com/statistics/826993/health-ai-market-value-worldwide/); [Markets and Markets — AI Healthcare Market Report](https://www.marketsandmarkets.com/Market-Reports/artificial-intelligence-healthcare-market-54679303.html); [Towards Healthcare — AI Healthcare Market 37.66% CAGR](https://www.towardshealthcare.com/insights/ai-in-healthcare-market); [Precedence Research — AI in Healthcare $613.81 Bn by 2034](https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market)
**Confidence:** MEDIUM (market estimates vary significantly between vendors; use as «order-of-magnitude», не цитировать single number as fact)

### 11.2 Physician adoption AI — AMA surveys
**Claim:** **66% of physicians used health AI в 2024** vs **38% в 2023** (+78% growth). **81% в 2026** AMA survey. Doximity 2026 State of AI in Medicine: **63% US physician AI adoption** (+16 pp in 9 months). **35% physicians enthusiasm > concerns** (up from 30%). **40% balanced** (excited + concerned). **Top concerns: patient privacy + patient-physician relationship integrity.** Top uses: documentation (21%), discharge instructions (20%).
**Source:** [AMA — 2 in 3 physicians using health AI](https://www.ama-assn.org/practice-management/digital-health/2-3-physicians-are-using-health-ai-78-2023); [AMA — More than 80% physicians use AI professionally](https://www.ama-assn.org/practice-management/digital-health/more-80-physicians-use-ai-professionally-ama-survey); [AMA 2026 Physician Survey on Augmented Intelligence](https://www.ama-assn.org/system/files/physician-ai-sentiment-report.pdf); [AMA — AI usage among doctors doubles](https://www.ama-assn.org/press-center/ama-press-releases/ama-ai-usage-among-doctors-doubles-confidence-technology-grows); [Advisory.com — How physicians using AI 5 charts](https://www.advisory.com/daily-briefing/2025/02/17/ai-use)
**Confidence:** HIGH

### 11.3 Patient AI adoption — see §6.3
40M ChatGPT healthcare users; 60% adults; 32% Rock Health 2025.

---

## Critical Gaps (areas where verified 2024-2026 data not found)

1. **mosmed.ai «4 млрд руб/год экономии в ОМС»** — оригинальный источник не найден. Operational data confirmed, financial savings — нет. Не цитировать без верификации.
2. **Bilingual specifics для российских регуляторных кейсов AI medical malpractice** — российских прецедентов AI-misdiagnosis в судах **не найдено** (US, UK, EU также пока нет landmark cases).
3. **DSP-1181 точная причина discontinuation** (efficacy / safety / business) — sources говорят только «discontinued post-Phase 1», без specifics.
4. **Tempus David clinical co-pilot detailed performance metrics** — пока press release only, не peer-reviewed validation.
5. **AlphaProteo reproducibility в independent labs** — DeepMind wet lab data only; independent replication за 2024-2026 не найдена в search.
6. **Specific Russian medical AI bias studies** для российского populace (skin tone, gender, age) — не обнаружены.

---

## 5-7 Surprising Findings для лектора (priority signal)

1. **DSP-1181 discontinued** — flagship «12-month AI drug» story has unhappy ending. **Insilico Rentosertib Nature Medicine June 2025** = новый flagship; first peer-reviewed clinical proof-of-concept. Лектор должен sync narrative — иначе credibility hit.
2. **Goh JAMA 2024 RCT** — GPT-4 alone outperformed doctors-with-GPT-4 в diagnostic reasoning. = **«AI augmentation gap»** — врачи недозагружают AI suggestions. Это redirects «human-in-the-loop» discussion: human override is good safety net, но и source of underperformance.
3. **NEDA Tessa scandal — vendor changed rule-based to generative AI без согласования** — vendor accountability story больше, чем chatbot story.
4. **Adversarial hallucination 83% rate** — LLMs elaborate fake medical facts when planted; simple mitigation prompt halves, не убирает.
5. **MASAI Sweden RCT — 6.7 pp sensitivity gain, 44% radiologist workload reduction** — самое сильное peer-reviewed evidence AI saves lives + saves radiologist time, с full RCT design.
6. **Change Healthcare breach — 190M Americans, $2.457B cost, Russian ransomware group** = largest healthcare breach US history. Nuance: Russian group attacked US system, что нужно деликатно для русской аудитории.
7. **Med-Gemini 91.1% MedQA** (vs Med-PaLM 2 86.5%) — exam passing ≠ clinical competence. Но это эффектное число для «AI passes USMLE» framing.

---

## Top 3 LLM Anti-pattern Cases (с самыми сильными датами)

1. **NEDA Tessa — May 2023.** Eating disorder hotline replaced human staff с rule-based chatbot. Vendor (Cass) самовольно добавил generative AI feature. Chatbot стал советовать calorie restriction → eating disorder triggers. Sharon Maxwell exposed via Instagram (May 2023). **NEDA pulled May 30, 2023 — within 24 hours after screenshots.** Lesson: vendor accountability + generative AI bypassed clinical safety design.
2. **Adversarial hallucination in clinical vignettes — Nature Communications Medicine 2025.** 6 leading LLMs given 300 doctor-designed vignettes с одним fake lab/sign/disease. Models repeat/elaborate on fake fact **in 83% of cases.** Simple mitigation prompt: down to ~42%, не zero. Lesson: LLMs are gullible to planted errors; physician verification required for every fact.
3. **ChatGPT Stanford documented fabrication — Stanford HAI 2024.** 4/5 models hallucinated significant proportion of sources. GPT-4 RAG: **up to 30% of statements unsupported**; nearly half of responses contain ≥1 unsupported statement. Lesson: even RAG-augmented LLMs cite confidently без actual source backing.

---

## Status of DSP-1181 на 13 мая 2026 (definitive answer)

**DSP-1181 — DISCONTINUED.**
- Original development: Exscientia × Sumitomo Dainippon, January 2020 — first AI-designed drug в clinical trials (OCD). Discovery от target → Phase 1 entry: ~12 months (vs traditional ~4-5 years).
- Phase 1 в Японии stopped 2022.
- Global highest R&D status (per Synapse/PatSnap): **Discontinued**.
- Exscientia далее: merger с Recursion announced August 2024, completed November 2024.
- **Cause of discontinuation:** sources do not specify (efficacy/safety/business decision combination implied).

**Implication для лекции:** Cannot cite DSP-1181 as success story of AI drug discovery. Replace with **Insilico Rentosertib (ISM001-055)** — first AI-designed drug с positive Phase IIa readout published peer-reviewed Nature Medicine (June 2025). This is the verified, defensible flagship case для **«AI drug discovery reaches clinical reality»** on май 2026.

---

## Sources index (deduplicated by section heading)

**§1 Drug discovery:** PatSnap Synapse, Sumitomo press, CAS Insights, Recursion press, Fierce Biotech, PharmaPhorum, Insilico press, PubMed Rentosertib, Nature AlphaFold 3, Isomorphic Labs blog, DeepMind AlphaProteo, arXiv 2409.08022, npj Drug Discovery 2025, Nature 2023 commentary, ScienceDirect 2025 landscape, Generate Biomedicines, Atomwise.

**§2 Diagnostics:** FDA AI/ML list official, JAMA Net Open FDA AI radiology, The Imaging Wire, IntuitionLabs FDA tracker, mosmed.ai EN, mos.ru, Healthcare ME, Remedium, Webiomed corporate, AJ Ophthalmology IDx-DR, Scientific Reports IDx-DR, npj Digital Medicine 2018, Retina Specialist 2025, npj Digital Medicine 2025 systematic review, Lancet Digital Health MASAI 2024, Lancet MASAI 2025 interval cancer, Lancet Oncology 2023, JAMA Internal Medicine Wong, IntuitionLabs CDS evolution, Aidoc press, Wikipedia Aidoc.

**§3 Foundation models:** EvolutionaryScale ESM3, bioRxiv ESM3, Science ESM3, Amazon ESM3, Arc Institute Evo 2, Nature Evo 2, bioRxiv Evo 2, NVIDIA blog, DeepMind AlphaGenome, STATnews AlphaGenome, Nature AlphaGenome.

**§4 Clinical reasoning:** Nature Medicine Med-PaLM 2, arXiv 2305.09617, PMC Med-PaLM 2, arXiv 2404.18416 Med-Gemini, Google Research blog, JAMA Net Open Goh, JAMA Net Open editorial, PubMed Nature Medicine Goh 2025, ScienceDaily, PMC Kanjee, NEJM AI, Eric Topol Substack, Nature Comm Medicine adversarial, Stanford HAI, npj Digital Medicine LLM safety framework, arXiv 2503.05777 hallucination, JMIR Medical Informatics Reference Hallucination Score.

**§5 LLM pattern:** PMC AI-INFOCARE protocol, Rheumatology Advisor simplify, Frontiers in Medicine LLM patient education, Khan Academy Khanmigo, Khan Academy Blog Biology, CNBC Microsoft+Khan.

**§6 LLM anti-pattern:** NPR Tessa June 2023, CBS Tessa, CNN Business Tessa, Psychiatrist.com Tessa, AI Incident DB 545, Fortune Tessa, Stanford HAI Generating Medical Errors, StudyFinds ChatGPT hallucinations, Becker's Hospital Review 40M, Fierce Healthcare Rock Health, Gallup AI healthcare, JMIR adoption study.

**§7 Security:** UHG official, BleepingComputer, AHA, HIPAA Journal 2024 + 2025 + 2026, OCR portal, Kaspersky, House Energy Commerce, HHS HIPAA de-identification, Harvard Online anonymity, Stanford HAI de-identification, PMC Re-id Safe Harbor, PMC privacy engineering, КонсультантПлюс ФЗ-152, ГАРАНТ ФЗ-152, Стахановец, Контур.Норматив, Минздрав ФЗ-152.

**§8 Responsibility:** FDA SaMD, FDA AI devices list, FDA PCCP final guidance, Ropes & Gray PCCP, IntuitionLabs PCCP, Ballard Spahr FDA AI 2025, European Commission Health AI, Reed Smith EU AI Act, EU AI Act Article 6, Hunton EU AI Act, Trilateral timeline, IntuitionLabs pharma compliance, PMC physicians AI trouble, Medical Economics, Healthcare Brew, Brandon Broderick, PMC liability AI, Sommers Schwartz, Webiomed registered devices, Roszdravnadzor, Medvestnik, Кредо registration, VNIIIMT.

**§9 Ethics/bias:** Science 2019 Obermeyer, PubMed Obermeyer, Berkeley News, Scientific American, Science Advances 2022 Daneshjou, Stanford Medicine, PubMed Daneshjou, JAMA Dermatology Adamson, PubMed Adamson, arXiv DermDiff, Springer skin type review.

**§10 Russian:** mosmed.ai, mos.ru, Healthcare ME, Remedium, TASS, Webiomed all blog posts, Crunchbase, TAdviser SberMedAI, LinkedIn, DynamicSun, Roszdravnadzor official.

**§11 Industry:** Statista, Markets and Markets, Towards Healthcare, Precedence Research, AMA all press, Advisory.com, AMA 2026 PDF.

---

**END OF SOURCE FILE — Word count approx 5,400.**
