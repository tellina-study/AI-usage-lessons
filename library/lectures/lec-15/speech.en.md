---
lecture: 15
module: 3
title: "Lecture 15. AI in Scientific Research"
audience: "студенты-инженеры 3 курса (универсальная)"
status: draft
version: 2.0
target_duration_min: 75
target_words: ~5900
wpm_max: 95
keystone: "Лестница научного цикла из шести ступеней: Hypothesis → Design → Experiment → Analyse → Write → Review — циклична, не последовательна"
updated_at: "2026-05-27"
author: "speech-writer v2 (Phase 11 cascade fixes from Phase 10 SYNTHESIS)"

changelog:
  - "v2.0 (2026-05-27) — Phase 11 cascade fixes from Phase 10 SYNTHESIS (4 P0 + 13 P1):
    P0-1 Galactica 15 ноября launch / 17 ноября retraction (3 дня) — speech [s01];
    P0-3 MICrONS «120 000 нейронов» → «более 200 000» per Nature 640 — speech [s22];
    P0-4 Palgrave UCL + Schoop Princeton — speech [s17] (был «Ливерпульский»);
    P1-M1 anti-anglicism cleanup (Sto→Сто, upfront/milestone→первоначальный платёж/контрольные платежи, Open-weights→открытые веса, GNoME-inference→GNoME-вывод);
    P1-M2 WE-1 (s07) expanded 143→193 слов с 6-step deeper tree;
    P1-M3 Sakana arxiv 2504.08066 Yamada citation [s08];
    P1-M4 «Длительность» metadata leak L27 → frontmatter only;
    P1-F1 FrontierMath freshness alert [s19];
    P1-F4 WE-2 timing 3 часов → 4 часов [s28];
    P1-C2 s39 hero honest update: AlphaFold ribbon composite (не screenshot alphafold.ebi.ac.uk per Tier 1-6 failure);
    P2 Russification cluster (отбор лучших / фундаментальные / открытый исходный код / добросовестность);
    P2 BO/GP inline gloss s11, YaLM-100B gloss s37, s39 closing strengthened."

preflight:
  - "Открыть https://alphafold.ebi.ac.uk и сверить число структур на s14/s39 (текущее: «более 200 миллионов»); если AlphaFold DB обновили счётчик — поправить устно."
  - "Проверить https://epoch.ai/benchmarks/frontiermath — обновить процент GPT-5.5 Pro на s19 (текущее 52,4%, май 2026); проверить https://epoch.ai/blog — Epoch AI May 2026 announce: AI-assisted review flagged ~⅓ problems с possible errors; revised scores forthcoming."
  - "Запустить backup-скриншот hero s01 (assets/s01-alphafold-nobel-galactica-composite.png) на случай fail проектора. Verify даты на композите: Galactica запуск 15 ноября 2022 / отозвана 17 ноября 2022."
  - "Открыть https://www.ecmwf.int/en/about/media-centre/news/2025/aifs — проверить статус AIFS operational (текущее: с 25 февраля 2025); если ECMWF добавил детали — отразить."
  - "Проверить https://www.sakana.ai/ai-scientist-v2 — обновить статус новых релизов; если v3 — упомянуть как касательную. Verify arxiv 2504.08066 Yamada et al."
  - "Запустить https://www.semanticscholar.org для краткой демо на s27 (5 секунд: ввести запрос «AlphaFold IDP» — показать сеть цитат). Verify NotebookLM 17M MAU + Elicit 138M / 4× actuals (квартальная сверка)."
  - "Подготовить распечатку 5-шаговой рамки из §5.5 (s36): студенты должны унести бумажный артефакт; ≥30 экземпляров."
---

# Lecturer's Speech · Lecture 15. AI in Scientific Research

**Version:** v2.0 (Phase 11 cascade fixes from Phase 10 SYNTHESIS).

---

## [s01 · 3 min] — Hook: AlphaFold Nobel vs Galactica retraction

[slowly, seriously]

October ninth, twenty twenty-four. Stockholm. The Royal Swedish Academy of Sciences announces the Nobel Prize laureates in chemistry. Half — to David Baker, for computational protein design. The other half — split between Demis Hassabis and John Jumper. For AlphaFold.

[pause]

This is **the first time in history**. The first time a Nobel in fundamental science is awarded for work whose very formulation names a specific AI product.

[pause 2 sec]

Now shift back nearly two years. **November fifteenth, twenty twenty-two.** Meta launches Galactica — a large language model trained on forty-eight million scientific papers. The slogan — "help for scientists." **Three days later, on November seventeenth, the model is retracted.** In those three days — fabricated citations, instructions for synthesizing explosives presented as "safe scientific text," racist conclusions. The MIT Technology Review headline of November eighteenth — "Why Meta's Galactica only survived three days online" — became the reference cautionary tale.

[pause]

Two pictures. On the left — the AlphaFold Nobel. On the right — the Galactica retraction. **One and the same underlying technology. A large machine learning model. Two diametrically opposite outcomes.**

And the central question of today's lecture starts right here. **How an engineer must learn to tell apart**: where AI in science makes a Nobel-level breakthrough, and where it creates a paper factory.

This is the topic of Lecture Fifteen.

[Transition to s02]

---

## [s02 · 1 min] — Cover

Lecture Fifteen. AI in Scientific Research.

This is the third module of the course — applied applications. After Lectures Thirteen and Fourteen about logistics and cybersecurity — you and I enter the most intellectually complex field. Science.

Science is an activity in which a mistake is expensive, but not at the moment of writing. The cost of a mistake is paid at the moment of **verification**: peer review, replication, accumulation of citations. Today we will learn to diagnose at which rung of the scientific cycle AI works, and at which — it creates risk.

---

## [s03 · 1 min] — Keystone: the six-rung ladder of the scientific cycle

[more slowly]

This is the keystone slide. The keystone axis of the whole lecture. Memorize the picture — you and I will keep coming back to it on every slide.

Six rungs. **Hypothesis. Design. Experiment. Analyse. Write. Review.** Hypothesis, design, experiment, analysis, writing, review.

[pause]

The main difference from the ladders of the previous two lectures — **it is cyclic**. In Lectures Thirteen and Fourteen the ladders were sequential. But the scientific cycle is iterative: the reviewer sends the paper back for revision, the author goes back to the analysis. Out of the analysis a new hypothesis arises.

This is a property **of science itself**. Keep this cyclicity in mind the whole hour.

---

## [s04 · 1 min] — Glossary: fifteen mandatory terms

A shared vocabulary. Fifteen terms. Without them the next hour won't come together.

Five key ones. **Foundation model** — a large general-purpose model: AlphaFold, Aurora, GNoME. **RAG** — retrieval with generation: NotebookLM, Elicit. **Hallucination** — a plausible but factually incorrect output. Not a bug — normal model behavior. **Closed and open world** — a closed task has a verifiable answer inside the system; an open one requires stepping beyond its bounds. **Human-in-the-loop, HITL** — explicit points of human decision in the pipeline.

The other ten — IDP, reference labeling, CASP, DFT, BO, ECMWF, FrontierMath, ICMJE, IMO, paper factory — we'll meet in context.

---

## [s05 · 1 min] — The central question

The central question of the lecture is this:

[slowly]

**Where does AI make a breakthrough in science, where does it create a paper factory, and how must an engineer decide which class their specific case falls into?**

By the end of the lecture you and I will build a five-step framework — classify the task, map the alternatives, apply four criteria, design HITL, verify before publication. This framework is applicable in engineering practice immediately. Write it down on a separate sheet — we will keep coming back to it.

---

## [s06 · 0.5 min] — Section 1: Hypothesis + Design

You and I enter the first section out of five.

**Hypothesis + Design** — where AI is sold on autonomy, but delivers narrow assistance.

This is the most hyped zone of the lecture. And the most fragile. When AI cannot be verified immediately, the temptation to accept the plausible as the true is great.

---

## [s07 · 2.5 min] — Worked example WE-1: decision tree "an idea for a grant"

Suppose your advisor asks you to come up with an idea for a grant. You have three options.

**First** — ask Sakana AI Scientist to generate fifty candidate hypotheses. **Second** — ask your advisor to propose three from their experience. **Third** — read thirty review papers yourself and build your own map.

Which do you choose?

[pause]

A six-step decision tree.

**Step one — classify the task.** Hypothesis is an open world. There is no reference labeling, verification comes through an experiment that takes years. This is already critically important: an open world means Sakana has no verifiable answer.

**Step two — coverage.** Sakana is trained on published texts. What was **not published** — closed dead ends known to senior colleagues, failed experiments of competitors — Sakana does not have. The basic counter-claim: a PhD advisor knows those dead ends from a decade of work.

**Step three — verifiability.** We'll verify the idea only through years of experiments. Over that interval — zero feedback from the AI about the quality of its own proposals.

**Step four — ethics.** ICMJE forbids AI as an author of a grant application. Disclosure of AI use is mandatory.

**Step five — designing HITL.** Sakana generates fifty, the advisor selects five by expertise, the graduate student verifies two through reading the literature and a pilot experiment. These are concrete gates.

**Step six — integrity of the submission.** The grant maker expects an original hypothesis, not a recombination of the literature. In the Methods part of the grant — an open disclosure of using Sakana as a brainstorm.

[pause]

Verdict. Sakana — a starting point for a brainstorm, not the final filter. The advisor plus your reading plus Sakana as an extension for generating variants. This is an **extension, not autonomy**.

---

## [s08 · 2 min] — Sakana AI Scientist: "1 of 3 passed peer review"

Sakana AI is a Japanese–San Francisco company, founded in twenty twenty-three. Their flagship — AI Scientist v2, April twenty twenty-five. They published a systematic paper on arxiv number twenty-five-oh-four-oh-eight-oh-six-six (Yamada and coauthors). Claim: "**1 of our 3 papers passed peer review** at an ICLR 2025 workshop."

[slowly]

Sounds impressive. But look at the dial more carefully.

Sakana runs in a mode of a hundred papers per cycle. Out of those hundred, a **human curator** selects the three best for submission. Of the three submitted, one gets accepted.

[pause]

Three different fractions that marketing merges into a single slogan. **Three percent** — this is the pick of the best: three out of a hundred generated. **Thirty-three percent** — this is the acceptance among the submitted. And only **one percent** — this is the true fraction of autonomous science: one out of a hundred generated, having passed the whole chain.

The marketing phrase "1 of 3" is thirty-three percent. The true rate is one percent. **Remember this difference** — it applies to any AI vendor advertising "successes."

---

## [s09 · 2 min] — Coscientist vs DeepMind Co-Scientist

Here a mandatory distinction. Two systems with almost identical names, constantly confused in the popular press.

**Coscientist** — without a hyphen, one word. This is Carnegie Mellon University, a Nature paper in December twenty twenty-three, Boiko and coauthors. This is an LLM-driven autonomous chemistry lab for synthesis. Architecture — GPT-4 and Claude **simultaneously**, in different agent roles. Application — synthesis of known palladium-catalyzed cross-coupling reactions. This is automation of known protocols, not the discovery of new chemistry.

**Co-Scientist with a hyphen** — this is Google DeepMind, a Nature paper in May twenty twenty-six. Architecture — debate and ranking of several agents. Application — the search for therapeutic targets for liver fibrosis, jointly with Stanford.

[pause]

Different systems, different phases of the cycle, similar names. Remember this distinction — it will come in handy when a colleague says "I heard about Co-Scientist."

---

## [s10 · 2.5 min] — Sakana pick-of-the-best — four structural problems

We return to Sakana. What the independent audit of the accepted paper showed.

**The first problem — the mechanics of picking the best.** A hundred papers generated, three selected by a human, one accepted. This is not autonomous science. This is AI-extended drafts with a heavy human filter.

**The second — hallucinated references.** The audit showed that some of the cited works either don't exist in the stated form, or the results are distorted. This is a structural property of language models generating bibliographies: the model knows what a scientific reference looks like and generates a plausible token sequence — but without an ontological link to a real publication.

**The third — falsified results.** In the accepted paper, numerical values were found that **do not match** what Sakana's own experiment code generated. This is a hallucination in the writing phase: the author agent rewrites the Results section and makes up "plausible" numbers, without checking against the script.

**The fourth — exaggerated novelty.** The "new method" turned out to be an implementation of a technique published in twenty twenty-two in a different context.

[pause]

The main lesson. **Passing peer review is not proof of scientific validity.** Peer review is a filter that screens out obviously bad works, but does not guarantee the correctness of the accepted ones.

---

## [s11 · 1 min] — Alternative: Bayesian optimization + Gaussian process

What works instead of Sakana.

**Bayesian Optimization (BO)** — **forty-plus years** of theory. **Gaussian Process (GP)** — **sixty-plus years**. A mature, mathematically grounded alternative for designing experiments in catalysis, drug development.

In catalyst optimization, BO reaches a seventy-percent success rate versus thirty for random screening. Campaign acceleration — **five to ten times**.

This is not a fallback option. This is a **mature working tool** that outpaces Sakana in real applications. Everyone who plans research needs to know it.

---

## [s12 · 0.5 min] — Section 2: Experiment — the strongest success

We move on to the second section out of five.

**Experiment** — the longest section of the lecture and the most positive in tone. Here you and I will see Nobel-level breakthroughs. But Nobel-level success does not mean Nobel-level finality. Every subsection will have a crack.

---

## [s13 · 2.5 min] — AlphaFold timeline + Recursion–Roche cascade effect

The history of AlphaFold begins in twenty sixteen. The first version won CASP13 in twenty eighteen. The breakthrough — CASP14, December twenty twenty: mean GDT_TS ninety-two versus seventy-five for the previous best methods. On the hardest Free Modeling tasks — ninety-two versus sixty. **A fifty-three percent improvement.**

[pause]

AlphaFold 3 — May eighth, twenty twenty-four. Expansion of the application space from single proteins to **protein-ligand complexes** — critically important for drug development. Fifty percent accuracy gain versus AutoDock Vina and GLIDE.

And on October ninth — the Nobel.

The Nobel's cascade effect is concrete, measurable. **Recursion Pharmaceuticals** struck a deal with Roche in **December twenty twenty-one** — that is, **before the Nobel**, but within its effect. A hundred fifty million dollars upfront payment. Up to forty programs. Each program — up to three hundred million dollars in milestone payments. **The total potential — up to twelve billion dollars** if all milestones are reached.

[pause]

This is the scale of what the Nobel legitimized. Not a prize, but a **signal** that gives subordinate systems — markets, funding, pharma — an understanding of the relative importance of the direction.

---

## [s14 · 2 min] — AlphaFold DB: 200M structures + the closed-code debate

The archive of structures. DeepMind and the European Bioinformatics Institute launched the AlphaFold Protein Structure Database in July twenty twenty-one. By twenty twenty-six — **more than two hundred million** predicted structures.

Compare. The Protein Data Bank — the main repository of experimentally solved structures, founded in seventy-one. By twenty twenty-four — about two hundred thousand. **AlphaFold DB contains a thousand times more predicted structures than PDB contains experimentally solved ones over half a century of work by crystallographers around the world.**

[pause]

But AlphaFold 3, at its May twenty twenty-four launch, was **closed**. Only a web interface, request limits, no commercial use. A thousand scientists signed an open letter demanding the weights be opened. November — an academic license. February twenty twenty-five — public availability for non-commercial use.

[slowly]

This is a **business strategy, not a philosophical question**. Isomorphic Labs — a startup spun out of DeepMind — struck billion-dollar deals with Eli Lilly and Novartis in early twenty twenty-four. AlphaFold 3 is a competitive asset in those deals. Opening the weights meant a lower valuation.

---

## [s15 · 1.5 min] — Boltz-1: the open alternative overtakes

December twenty twenty-four. An MIT team — Corso, Wohlwend and coauthors — publishes **Boltz-1** on biorxiv 2024.11.19.624167. **Fully open source** — a competitor to AlphaFold 3. MIT license, permits commercial use, full code and weights.

By the end of twenty twenty-five, Boltz became the **most widely used** open model of its class. It overtook AlphaFold 3 in academic adoption.

[pause]

This is a pattern. Stable Diffusion 1.5 overtook DALL-E 2 within six months. LLaMA 2 overtook GPT-4-only deployment templates for academic research. Mistral 7B became the basis for several fine-tuned models.

The applicable lesson. When you choose an AI tool for academic work — **by default choose open source**, if there is a sufficiently close open alternative. This eliminates vendor lock-in and ensures the long-term reproducibility of your work three to five years out.

---

## [s16 · 2 min] — GNoME + A-Lab Berkeley: 41 of 58 in 17 days

November twenty twenty-three. DeepMind publishes in Nature the results of **GNoME** — Graph Networks for Materials Exploration. A foundation model for predicting stable crystalline structures.

**The numbers.** Two million two hundred thousand candidates generated. Three hundred eighty thousand passed stability validation via DFT — density functional theory. **Six rounds of active learning** — at each round both the training set and the candidate space expand.

Three hundred eighty thousand — that's **forty-four times more** than the Materials Project contained at the time of publication.

[pause]

In parallel — A-Lab Berkeley. The autonomous chemistry lab of Lawrence Berkeley National Laboratory under Gerbrand Ceder. A robotic synthesis platform plus GNoME predictions. And the main figure, the canonical one:

**A-Lab Berkeley synthesized 41 of 58 target compounds in 17 days of continuous operation.**

Seventy percent success rate. The baseline of manual chemistry — one target requires from weeks to months of a graduate student's work with no guarantee of success. **A-Lab is forty to sixty times faster** in synthesis productivity.

This is an impressive result. But we must immediately move to the next slide.

---

## [s17 · 2 min] — The Palgrave–Schoop critique: 35 of 36 had errors

January twenty twenty-four. Robert Palgrave from University College London and Leslie Schoop from Princeton University publish on ChemRxiv a critique — a preprint with DOI ten dot two-six-four-three-four. They analyzed thirty-six "successful" A-Lab samples — those thirty-six out of the forty-one synthesized, for which sufficient data were available.

And the result:

[slowly]

**Of the 36 analyzed "successful" A-Lab samples — 35 contained at least one of three errors.**

Type one — twelve of thirty-five. **Incorrect phase assignment.** GNoME predicted, for example, the ternary compound AlMnO3. A-Lab showed XRD peaks, the automatic system interpreted them as the target. But under manual analysis the real product is a mixture of Al2O3 + Mn2O3, not AlMnO3.

Type two — fifteen of thirty-five. **A derivative or a solid solution.** The target — BaSn2O6. The real — Ba0.97Sn2.03O6 with a slight stoichiometry deviation, or BaSnO3 + SnO2 — decomposition into known phases. These are not new compounds.

Type three — eight of thirty-five. **Absence of functional validation.** The compound exists. XRD confirms. But **what it does** — there are no measurements at all. This is meaningless for applications.

[pause]

**Only one of thirty-six** passed independent verification without objections. The real fraction of confirmed discoveries is closer to one or two out of fifty-eight, not forty-one.

**Prediction does not equal discovery.** Remember this phrase.

---

## [s18 · 2 min] — Aurora 5000× and the operational status of ECMWF AIFS

Aurora. Microsoft Research, June twenty twenty-four, Nature. A foundation model for the atmosphere with one billion three hundred million parameters. Trained on the ERA5 reanalysis data corpus. The claimed headline result — **5000 times faster** than the ECMWF IFS benchmark.

[pause]

Five thousand times. What ECMWF does in an hour on a supercomputer, Aurora does in less than a second on a single GPU.

This is a **valid benchmark claim for a specific application**. But an **invalid policy claim**.

Aurora **is not used operationally** in any national weather service. A similar situation with GraphCast, Pangu-Weather, FourCastNet. All these foundation models are benchmark tests, not deployed in production.

**ECMWF AIFS** — a different story. This is ECMWF's own development, **operational since February twenty-fifth, twenty twenty-five**. Open weights, available through the ECMWF API. Not Aurora, not GraphCast — an internal integration of AI together with the classical IFS.

[pause]

And the crack. All ML weather models **systematically underperform** on extreme events — peak hurricane intensity, local precipitation, atmospheric blocking. This is tied to a fundamental property of training on a histogram: extreme events get smoothed out. This is not a defect of Aurora — it is a structural property of the ML approach in weather.

---

## [s19 · 2 min] — AlphaProof IMO 2024: silver + unsolved combinatorics

July twenty twenty-four. DeepMind announces: **AlphaProof plus AlphaGeometry 2 solved four of the six problems of the International Mathematical Olympiad**. Twenty-eight points out of forty-two. A silver medal. Nature 2025, DOI 10.1038/s41586-025-09833-y.

AlphaProof solved P1 — algebra, P2 — number theory, P6 — algebra. AlphaGeometry 2 — P4, geometry. And **P3 and P5 — combinatorial — remained unsolved**.

[pause]

This is illustrative. **Formal proof in combinatorics remains an open frontier.** Algebra and number theory have a rich structure of lemmas in Lean — a proof assistant. Combinatorics requires specific inductive constructions or explicit bijections.

And the crack. Each problem required **hours of GPU time**. A human olympiad participant has **ninety minutes**. The AI solved correctly, but slowly.

FrontierMath from Epoch AI. Launch November twenty twenty-four — less than two percent for GPT-4o, Claude 3.5, o1-preview. By May twenty-six — fifty-two and a half percent for GPT-5.5 Pro. **Freshness alert:** Epoch AI in May twenty-six announced — a review found possible errors in a third of the problems; revised scores are pending. **But even now forty-eight percent of the problems remain unsolved.**

---

## [s20 · 0.5 min] — Section 3: Analyse — reliable applications

The third section out of five.

**Analyse** — the data analysis phase. The most production-ready rung of the scientific cycle for AI in twenty twenty-six. Here, as you and I will see, there are fewer scandals and more everyday usefulness.

Why. Here there is **reference labeling**.

---

## [s21 · 2 min] — TESS+Kepler CNN: 1,595 candidates, 83.9% accuracy

The search for exoplanets. TESS — Transiting Exoplanet Survey Satellite — launched in twenty eighteen, the successor to Kepler. TESS continuously observes the brightness of tens of thousands of stars every two minutes. When a planet transits the disk of a star, the brightness briefly drops by fractions of a percent.

The classical pipeline before AI — **Box Least Squares**, BLS, Kovács and coauthors twenty oh two, A&A 391. A statistical method for finding periodic dips. It worked, but required manual review.

Since twenty eighteen — CNN. Shallue and Vanderburg, Google plus UT Austin. Trained on labeled positives and negatives. AUC 89 percent versus 78 for BLS.

[pause]

By twenty twenty-six — production pipelines. A concrete work — Huang and Jiang, arxiv 2512.00967. The model identified **one thousand five hundred ninety-five high-confidence planets, accuracy 83.9 percent** on held-out validation.

Structurally. AI works because there is **clear reference labeling** — confirmed planets versus known false positives. **The transit pattern has a clear morphology**. And the final confirmation of each candidate requires follow-up observations, which are done by human astronomers. **Extension, not autonomy.**

---

## [s22 · 2 min] — Allen MICrONS: 1 mm³ of visual cortex

Allen Institute MICrONS — Machine Intelligence from Cortical Networks. Published in April twenty twenty-five. The main paper — Nature 640 (MICrONS Consortium, DOI 10.1038/s41586-025-08790-w), and accompanying ones in Nature and Science.

Reconstruction of one cubic millimeter of a mouse's visual cortex. Concrete numbers: **more than two hundred thousand anatomically reconstructed neurons. About five hundred million synapses. Four kilometers of axons.**

The procedure. The brain tissue is fixed and cut into ultra-thin sections of thirty nanometers. Each section is imaged on an electron microscope. **AI segmentation** identifies each neuron in each section. **AI tracing** links the segments across sections into three-dimensional neurons. Without specialized deep learning — U-Net architectures for segmentation, transformer-based methods for tracing — this connectome would have been **literally impossible**. Manual tracing of more than two hundred thousand neurons would have required thousands of person-years.

[pause]

This is the canonical case of applying AI in biology. A task that was previously impossible becomes possible thanks to AI.

And the boundary. One cubic millimeter is a very small part of the brain. A whole mouse brain — five hundred of these. A human one — a million. Extrapolation from one millimeter to the organism level is an open problem. And a full reconstruction of a mouse brain is at least a decade in the future.

---

## [s23 · 2 min] — LIGO ML pipeline + conformal prediction

LIGO — Laser Interferometer Gravitational-Wave Observatory. An array of gravitational-wave detectors, launched in twenty fifteen. By the year twenty-six, about a hundred fifty confirmed events have been detected.

The classical pipeline — **template matching**. The Wiener method of nineteen forty-nine. Eighty-plus years in signal processing.

Where AI helps. ML methods — CNNs on raw strain time series — are added for **fast initial screening** in real time. They don't replace template matching — they add to it. A concrete paper — Ashton, Malz, Colombo, arxiv 2504.17587 of twenty twenty-five.

[pause]

And an important methodological term — **conformal prediction**. This is a statistical method for quantifying uncertainty. For each predicted event, conformal prediction gives a **calibrated confidence interval**: "this signal is real with ninety-five percent confidence."

The difference from classical confidence intervals — **it is distribution-free**. It does not assume that the residuals are normally distributed. This is an important methodological innovation — every AI prediction must be accompanied by uncertainty quantification for responsible scientific use.

ML — an extension of template matching, not a replacement. The final attribution remains with physics.

---

## [s24 · 2.5 min] — AlphaFold IDP: 22% hallucinations, α-synuclein

You and I return to AlphaFold — now to its failure. A deep dive.

**IDP** — intrinsically disordered protein. Proteins or regions without a stable three-dimensional structure. About thirty to forty percent of the human proteome contains IDP regions. They are critically important in signaling, regulation, phase transitions.

Why AlphaFold does not work on IDP. The model is trained on PDB structures. PDB contains **only stable, structured** proteins. IDPs **cannot be crystallized**, their signatures show a conformational ensemble. Therefore IDPs are **underrepresented in the training distribution** of AlphaFold.

[pause]

A concrete metric. **About twenty-two percent of the residues** in IDP regions are systematically hallucinated. This is a **systematically incorrect structure**, not "low accuracy." The source — Akdel and coauthors, Nature Structural and Molecular Biology 2022; a follow-up analysis — Gopalan and Narayanan, arxiv 2510.15939.

And a concrete example. **α-Synuclein** — a protein associated with Parkinson's disease. A large IDP region. Physiologically it exists in a conformational ensemble. The AlphaFold prediction shows a specific α-helical bundle, which **does not correspond to the physiological conformation**.

If a drug developer uses this prediction to design a drug against α-synuclein aggregation — they are working against the **wrong target**.

[pause]

What to do. Check the pLDDT for each residue of your target. For regions with pLDDT below seventy, treat it as high uncertainty. Cross-check with NMR data. For IDP regions, use specialized ensemble modeling tools.

**Do not publish drug docking results based on AlphaFold for IDP regions without a caveat.** This is a concrete commitment.

---

## [s25 · 2.5 min] — Worked example WE-TESS: the five-step framework

Let's apply the methodology to a concrete case. You are given a thousand hours of TESS data — light curves for fifty thousand stars. What approach do you use?

Four options. **A** — a pretrained NASA Kepler CNN, fine-tuned for TESS. **B** — train your own CNN. **C** — classical BLS plus manual review. **D** — a hybrid, BLS primary plus CNN secondary.

The five-step framework.

**Step one — data overlap analysis.** TESS versus Kepler. Different cameras, different cadence, different noise model. The distribution shift is substantial. A pretrained Kepler CNN will underperform without fine-tuning.

**Step two — labeling availability check.** The TOI catalog — about six thousand records. A modest size versus Kepler's thirty thousand candidates.

**Step three — GPU cost estimate.** Training your own CNN — weeks on eight GPUs, ten thousand dollars. Fine-tuning a pretrained one — hours on one, one hundred to five hundred dollars. Classical BLS — minutes on a CPU, zero dollars.

**Step four — false-positive rate benchmark.** BLS — AUC seventy-eight percent. A pretrained Kepler CNN on TESS with fine-tuning — eighty-nine. Your own TESS CNN — ninety-two. The gain of your own over the fine-tuned one — three percent AUC.

**Step five — verification on a held-out hundred hours.** Run all four, manually check the candidates.

[pause]

The decision for a typical graduate student without super-resources. Stage one — **option A**, pretrained plus fine-tuning. Stage two for production — the hybrid D, BLS plus CNN. Your own CNN is justified only with a large labeled sample and a budget for weeks of GPU. **Classical BLS — the comparison benchmark against which you always compare.**

This five-step framework is applicable to any ML decision in the analysis phase. Not a "framework for exoplanets" — a **framework for responsible AI deployment in any scientific task**.

---

## [s26 · 0.5 min] — Section 4: Write + Review — against academic integrity

We move on to the fourth section out of five.

**Write plus Review** — the most concentrated failure zone of the lecture. Here AI does not help carefully. Here AI **actively creates risk** for the scientific method — and it's important for you and me to understand this.

If you retain only one memory from the lecture — it should be from here.

---

## [s27 · 2 min] — NotebookLM (17M) + Elicit (138M papers, 4× speedup)

Mature literature-review tools. Used at scale.

**NotebookLM** — Google, launched in twenty twenty-three. A RAG tool for a personal corpus. You upload fifty PDFs, ask questions, get answers with references to specific sentences. By the end of twenty twenty-five — **more than 17 million monthly active users**.

**Elicit** — Ought.io, twenty twenty-one and onward. A RAG tool specifically for literature review. The database — **138 million academic papers**. Cuts literature-review time **by 4 times, per a validated user study**.

[pause]

This is a working extension. Mature, at scale. But:

The psychological risk — **automation bias**. When you get an "authoritative" answer from NotebookLM, there is a bias toward accepting it without checking. NotebookLM sometimes invents "citations" within the corpus that, upon checking, are not tied to real content. The quality of the synthesis is limited by the quality of the source documents. And most importantly — a student who relies on NotebookLM **does not read** the papers deeply.

The correct mode of use — a **starting point**, not the final synthesis. Verify every important claim by manual reading. This turns four hours of manual reading per week into one hour of NotebookLM plus one hour of targeted verification. A net saving of two hours per paper **while preserving depth**.

---

## [s28 · 2.5 min] — WE-2: a 4-step bibliography check from a coauthor

This is the most important worked example of the lecture. Tomorrow you will be in this situation.

[slowly]

**Context. Your coauthor sends you a paper draft with an LLM-generated bibliography of 47 citations. A coauthor position is offered. What do you do?**

[pause]

First, let's acknowledge the emotional moment. This is an uncomfortable situation. The coauthor is usually senior or equal. Doubts about their work are socially awkward. **But**: your name on the paper is your scientific reputation. If the paper is retracted because of fake citations, your name goes along with it.

This is **not the time for social politeness**. This is the time for professional rigor.

A four-step process.

**Step one — DOI resolution of every citation.** Open Zotero's automatic resolution. Ten minutes for forty-seven citations. **The failure criterion — three or more fakes.** Citations that don't resolve or resolve to different papers. STOP. Decline coauthorship.

**Step two — relevance check.** A sample of ten random ones. Read the abstract and the relevant section. Does the citation support the claim? Thirty minutes. **The failure criterion — three of ten are irrelevant or contradictory.** STOP.

**Step three — GPTZero on the style.** Run the bibliography plus the introduction plus the conclusion through it. Five minutes. If seventy percent is "likely AI-generated" — a signal. Cross-check via Originality.ai and Crossplag.

**Step four — request the source files.** Ask the coauthor to send the PDFs of the cited papers. If they refuse or send them with a delay of more than two days — a diagnostic signal.

[pause]

Forty-five minutes of your time. Against **four hours** of manual checking of forty-seven citations. Against the permanent career damage of a retraction. **The cost-benefit ratio is clear.**

---

## [s29 · 1.5 min] — The Frontiers "rat": February 13–16, 2024, Midjourney

On February thirteenth, twenty twenty-four, the journal Frontiers in Cell and Developmental Biology published a paper with **rat anatomy drawn by Midjourney**.

[slowly]

On the figure. **"Protemns"** instead of "proteins." **"Zxpens"** instead of "sperm." Nonexistent terms. Anatomically impossible organs. Hypertrophied reproductive structures.

Retracted three days later — on February sixteenth.

[pause]

And here is what is important. The paper **disclosed the use of AI**. The authors wrote in Methods: "Figures generated using Midjourney." That is, **the AI disclosure did not save it** — the reviewers missed the obviously ridiculous anatomy.

The main lesson. Disclosure is necessary, but not sufficient. Peer review must check figures **separately**, systematically, with an anatomy expert when the paper contains anatomical illustrations. If an AI-generated figure looks plausible to a non-specialist reviewer, no disclosure will save it.

This is a concrete anti-pattern. If a coauthor proposes an AI-generated figure — you personally check it for absurdities. Anatomically? Physically? Biologically? If you don't have the expertise to check — ask an expert colleague or **decline to use** the figure.

---

## [s30 · 2 min] — NeurIPS 2025: 100+ fake citations in 53 papers

Twenty-five to twenty-six. NeurIPS — the main machine learning conference. The twenty twenty-five acceptance figures:

[slowly]

**Twenty-one thousand five hundred seventy-five submitted. Five thousand two hundred ninety accepted. Acceptance rate — 24.52 percent.**

Remember this number. Twenty-four and a half percent. This is the **peer-reviewed** acceptance rate of a top conference.

And a separate report from the year twenty-six, GPTZero Research, arxiv 2602.05930. **More than a hundred fake citations penetrated into fifty-three accepted papers.**

[pause]

Structurally. Each paper has a hundred to two hundred citations. Fifty-three papers out of five thousand two hundred ninety — that's one percent of the accepted. But **a hundred fake citations** — that's a hundred entries in the scientific literature that **do not exist**, but that may be cited by future works.

The cascade effect. Today's fake citation → tomorrow's paper cites it → the next work cites it. **Three to five years later, the contaminated citation network becomes indistinguishable** from a real one for a non-specialist reader.

This is exactly the **paper factory** — the paper mill — in action. But it's not the paper itself that gets fabricated — it's the **citation network** that gets fabricated, making the paper more authoritative than it is.

And most importantly. Peer review **failed**. Two hundred reviewers, thousands of meta-reviewers, NeurIPS's complex processes — missed it. **This is a structural failure mode**, not an individual mistake.

Every LLM-generated citation requires **verification. Every one. Without exception.**

---

## [s31 · 2 min] — ICMJE + publication policies 2024

A summary rule of academic integrity.

**ICMJE** — International Committee of Medical Journal Editors. The recommendations were updated in twenty twenty-three and twenty-four. They explicitly address the use of AI.

[slowly]

**Rule one.** AI cannot be listed as an **author**. Authorship requires responsibility for the work. AI cannot bear legal and ethical responsibility.

**Rule two.** AI assistance must be **disclosed** in the Methods or Acknowledgements section. Specifically — which tools, for which tasks.

**Rule three.** The authors remain **fully responsible** for the content. "I didn't write this, ChatGPT wrote it" — is an invalid defense.

**Rule four, added in twenty-four.** The use of AI in peer review must be disclosed to the editors. Most journals — Frontiers, Springer, Elsevier — **fully forbid** AI in peer review without explicit prior approval.

[pause]

Parallel policies. Springer Nature August twenty twenty-four. Elsevier June. Frontiers March. Nature January. ACS twenty twenty-four. **All updated to explicit AI disclosure requirements.**

Five ethical criteria. **Disclosure. Verifiability. Authorship integrity. Accepted responsibility. Reproducibility.** Each is a protective function against a specific failure mode.

The cascade risk. If a paper is retracted because of undisclosed AI or fake citations — this is **permanent career damage**. A retraction stays on your CV forever. **The cost of a single retraction often exceeds the cumulative benefit of a hundred successful AI-assisted papers.** This is arithmetic, not rhetoric.

---

## [s32 · 0.5 min] — Section 5: When AI is not needed — criteria + alternatives

The fifth section out of five.

**The resulting section.** After four sections of analysis of where AI works and where it doesn't, you and I synthesize an applicable mental model. This is what you carry out of the lecture into your professional life.

---

## [s33 · 2 min] — Four categories of criteria "AI is not needed / harmful"

Four categories. Any trigger is a signal that AI may be inappropriate.

**Category A — an open world without verifiable reference labeling.** Organism-level biology, psychology, history, comparative literature. AI here either paraphrases the existing literature or hallucinates.

**Category B — underrepresented in the training data.** Rare diseases, neonatal medicine, new materials without analogs, specialized subfields. Distribution shift makes predictions unreliable.

**Category C — verifiability cannot be carried out independently.** Peer review, citation networks, historical claims. AI-generated content becomes **self-fulfilling** — this is exactly the NeurIPS problem.

**Category D — ethical risk.** AI as a coauthor, undisclosed use, AI generation of clinical guidelines without oversight, fabrication of data.

And a bonus — **category E — closed physics is better available**. If there is DFT, a matched filter, a classical statistical test — use it. Add AI only if it measurably improves over the classical benchmark.

Application. Take your specific case. Go through the five categories. **Several triggers — a strong signal against AI.**

---

## [s34 · 2.5 min] — WE-3: a propylene oxidation catalyst

The third worked example. It shows how to work **correctly** with AI in materials science.

Context. The advisor asks you to build an AI pipeline for propylene oxidation catalysts. An industrial process — seven million tons annually globally.

The five-step framework.

**Step one — classify the task.** A closed world. Catalysis — quantum chemistry is well defined, stability via DFT. AI can work as an extension.

**Step two — map the alternatives.** First-principles DFT via VASP. GP-BO over the reaction parameter space. Inverse design in the GNoME style. Queries to Materials Project plus the Open Catalyst Project.

**Step three — apply the four criteria.** Open world — no. Coverage — Materials Project contains one million two hundred thousand points, mostly transition metals; propylene oxidation is underrepresented. **A risk flag.** Verifiability — yes. Ethics — yes. **Verdict. AI is applicable with careful HITL and DFT verification.**

**Step four — design HITL.** AI screens five thousand candidates via GNoME inference, one hour of GPU. About five hundred with a reasonable composition. **A human selects the top 50** by synthesizability, precursor cost, novelty. DFT validates fifty, fifty GPU-hours. The top 10. Synthesis in the lab confirms three.

**Step five — verify before publication.** For each new catalyst — DFT stability plus synthesis plus XRD plus a catalytic-activity test via thermogravimetric analysis. **All four confirmed before submitting the paper.**

[pause]

The bottom line. **Not "AI makes a discovery." But "AI accelerates the screening, a human selects, DFT verifies, the lab confirms."** The timeline — four months for three confirmed catalysts. The manual approach — one to two candidates per year. **A 4-to-6-fold acceleration, with verification gates.**

---

## [s35 · 2 min] — Five mature alternatives: 30–70 years each

Five non-AI alternatives that work today.

**The first — Bayesian optimization plus Gaussian process.** Forty plus sixty years. Experiment design, catalyst optimization, drug formulation development. A five-to-ten-fold acceleration versus the manual approach.

**The second — DFT plus first-principles molecular dynamics.** Sixty plus sixty years. The Nobel Prize of ninety-eight. Catalysis, materials, drug development, structural biology. **Physical groundedness.** When you use DFT, the errors are well characterized and predictable.

**The third — classical statistical methods.** A hundred plus years. Gosset's t-test of nineteen oh eight. Fisher's ANOVA of twenty-five. **Interpretability plus acceptance in peer review.** For explanation tasks — statistics is better than ML. For prediction tasks — ML is better. These are different tasks, often confused.

**The fourth — operations research and OR-Tools.** Seventy plus years. Dantzig's simplex of forty-seven. Scientific logistics, clinical-trial planning, grant allocation. **Provable optimality** under the given constraints.

**The fifth — human peer review with enhancements.** Not a classical tool in the technical sense, but **a mature institutional infrastructure**. Structured rubrics, double-blind, statcheck, image forensics. **A combined human plus tool is better than each separately.**

[pause]

**The conservation principle.** Mature methods **rarely become obsolete**. They become components in larger pipelines. Classical statistics of the seventies is still used in the twenties. DFT of the eighties — too. **Skill in mature methods accumulates over a whole career.**

---

## [s36 · 2 min] — Three questions for a vendor + the five-step framework

An applicable artifact. What you carry in your pocket.

When a vendor sells "an AI tool for scientific task X" — ask **three questions**.

**Question one — the benchmark before AI.** "What was the benchmark before your tool was adopted? What accuracy, time, cost of the classical method for the same task?" If they can't answer — they don't know the benchmark, or they know but don't want to say. A red flag.

**Question two — reproducibility.** "Where are the code, training data, weights published? Can I reproduce your results on my data?" If "proprietary, we don't share" — a structural problem for academic use.

**Question three — failure cases.** "Describe cases where your model works badly. What's the hallucination rate? Which out-of-training distributions?" If "the model always works well" — **the final red flag**.

[pause]

And the five-step framework, the synthesis of the whole lecture.

First — **classify the task**: open or closed world. Second — **map the alternatives**: BO, DFT, classical statistics, OR-Tools. Third — **the four criteria** for "AI is not needed." Fourth — **design HITL** with explicit gates. Fifth — **verify before publication** via a classical benchmark.

Write these five steps down on a separate sheet of paper. Put it in your pocket.

---

## [s37 · 2.5 min] — The Russian context: AIRI / Sber / Yandex + Decree No. 490

The Russian context. What changes for the applicability of the previous sections.

**AIRI — the Artificial Intelligence Research Institute, twenty twenty-one.** An independent research institute. Publications in Nature Communications on protein structure prediction — open competitors to AlphaFold. Collaboration with medical centers on AI in radiology. Climate modeling of the Arctic. **Direction — emerging research**, not yet at industrial scale.

**Sber AI Lab.** A research arm within Sber. AI4Science applications — climate modeling, energy demand forecasting. An internal cluster — about five thousand H100s. **One of the few Russian institutes capable of training large models at scale.**

**Yandex Research.** YaLM-100B — Yet Another Language Model, 100 billion parameters, opened in twenty-two. The RuGPT family. Contributions to ICML, NeurIPS, ICLR. **The most internationally visible Russian direction of AI research.**

The regulatory framework. **Presidential Decree number 490 of October 10, 2019** — the National Strategy for the Development of Artificial Intelligence to 2030. **Updated by Decree number 124 of February 15, 2024.** AI4Science — a priority category of the RSF.

[pause]

The cracks. **The compute gap.** AlphaFold 3 — from ten to fifty million dollars. A typical RSF grant — fifty to a hundred fifty thousand. **A structural gap of 20 to 50 times.** Most groups depend on **open foundation models** — AlphaFold, Boltz-1, LLaMA.

**Citation visibility.** Russian-language publications — less than one percent of Semantic Scholar, against two to three percent of world output. **A threefold underrepresentation** in language-model data. A Russian graduate student must not rely on NotebookLM or Elicit for coverage of Russian-language sources.

What this means. **Adaptation of foundation models**, not development from scratch. Geographic advantages — the Arctic, domestic data. International visibility through English-language publications.

---

## [s38 · 3 min] — Q&A: tomorrow, an LLM bibliography from a coauthor + a positive recap

This is the Q&A slide. A return to the failure and a built-in positive recap for you and me.

[slowly]

**Tomorrow you receive an LLM-generated bibliography from a coauthor. What do you do?**

Step one — **verify every citation via DOI resolution**. Ten minutes.

Step two — **a sample of ten random citations for relevance**. Thirty minutes.

Step three — **GPTZero on the style**. Five minutes.

Step four — **request the source documents from the coauthor**.

If three or more citations fail — **decline coauthorship**. This is not a breach of politeness. This is professional rigor.

[pause 2 sec]

And a built-in positive recap. So that you don't carry out of the lecture only the failures.

**AlphaFold — two hundred million protein structures** in an open database. Access for any student at any university in the world. This is **a thousand times more** than PDB accumulated over half a century.

**Aurora — five thousand times faster than the ECMWF benchmark** on a benchmark test. ECMWF AIFS operational since February twenty-fifth, twenty twenty-five.

**AlphaProof — silver at the IMO 2024.** Four problems out of six. The first prize-level case for AI.

These results are **real**. AI in science does **not "not work."** It works on Nobel-level tasks, **when applied correctly**. A closed world plus reference labeling plus mature technology plus HITL equals an **extension** that accelerates the scientific workflow in meaningful ways.

The main test you must learn is **to tell apart work extended by AI from work contaminated by AI**. This is exactly what you and I went through today.

Questions — go ahead.

---

## [s39 · 2 min] — Closing hero: AlphaFold → bridge to Lecture 16

[slowly]

This cover composition — AlphaFold protein structures. A symbol of the closed world of the scientific cycle. Two hundred million structures. Free. Open. To anyone.

Biology is now **a little more known**. But the final map is far off — every predicted structure remains a starting point, not the end of the research.

[pause]

AlphaFold showed that **closed-world tasks** in science are accessible to AI. **But only on the condition of reference labeling plus a human in the loop plus open weights.** This formula — a closed world plus a benchmark plus HITL plus openness — you carry out as the engineer's main weapon.

Lecture Sixteen — **AI in the oil and gas industry**.

This is an interesting case, because the tasks here are **partly closed-world — geophysics, physics-based subsurface modeling**. And **partly open-world — reservoir characterization, exploration risk assessment, a lot of uncertainty**. The same cycle ladder applies, but with a different structure of success and failure.

[pause]

Let's look at the direct analogy. On the Experiment rung in Lecture Fifteen, AI works in a closed world — AlphaFold. In oil and gas the analog is **seismic interpretation** via a CNN on seismograms. On the Hypothesis rung, AI sells autonomy — Sakana. In oil and gas the analog is **exploration risk assessment**, where vendors sell "a forecast of finding oil," but the real work requires geological expertise.

The same framework. A different industry specificity. **An engineer who learned to tell apart today is ready to tell apart tomorrow.**

**See you at the next lecture.**

[Closing pause]

---

## [Reserve · 5 min] — Q&A buffer + backup contingencies

- **If the NotebookLM/Semantic Scholar demo doesn't launch on s27** — we switch to a verbal description of the interface; result — the lecturer shows on the projector a screen from the preflight screenshot.
- **If the question "Does Claude / GPT-5 in science also work?"** — we answer: general LLMs work as a black box; AlphaFold / Aurora / GNoME — are **domain-specialized** foundation models, trained on specific scientific data. These are different classes of tools. GPT-5 as a Write assistant — OK with disclosure; GPT-5 as a replacement for an experiment — no.
- **If the question "And when will AI replace the research advisor?"** — we answer: never in the foreseeable future. A research advisor knows what was **not published** — closed dead ends, lab failures, the context of a specific research community. An LLM knows only **what was published**, which is already a filtered result of human judgment.
- **If the question is about a specific Russian institute / your home university** — we answer in general terms: "specialized technical universities of Russia are actively working with AlphaFold for biotech research; concrete results — publications in Nature Communications of twenty-four to twenty-five jointly with AIRI." Without specifics on institutions — this is a political field.
- **If time remains** — we expand into a seminar on the Q&A backup from chapter-part4 §Q&A (15 main + 3 bonus questions).
