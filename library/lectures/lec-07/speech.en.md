---
lecture: 7
title: "Lecture 7. AI in Medicine and Pharmaceuticals"
length_min: 75
length_words: ~4900
status: draft
version: v2
slides_covered: [s01, s02, s03, s04, s05, s05b, s06, s07, s08, s08a, s09, s10, s11, s12, s13, s13a, s14, s15, s16, s17a, s17b, s18, s19a, s19, s20, s21, s22, s23, s24, s24a, s26, s27, s28, s29]
source: chapter v2 (commit 5c4b06c, ~12,692 слов) + slides v5.1 (commit 2d45771, 34 слайдов)
issue: 73
branch: issue-73-lec-04-medicine-production
revision_notes: "v2 applied Phase 10 critic findings — 1 P0 (Gallup→OpenAI/Rock Health) + 14 P1 (anglicisms s24, pacing s09/s10/s13/s23, divider rename s19a, design choice gloss, rule-based phrasing, augmentation gap sync, s17a RU trim, FDA timeline soften, Daneshjou soften, Cass date soften, Price/Gerke affiliations, numeric drift s17a/s26)."
---

# Lecturer Speech · Lecture 7

**Duration:** 75 minutes (≈68 min of active speech + 7 min buffer for Q&A and pacing).
**Audience:** third-year engineering students (general, non-medical).
**Slides:** 34 (29 content + 5 dividers).
**Pace:** target 70–75 words per minute; hard cap 95 words per minute on any fragment.
**Delivery date:** May 13, 2026.
**Source of truth:** chapter v2 (commit 5c4b06c) + slides v5.1 (commit 2d45771).

---

## Preparation before the lecture (24–48 hours ahead)

- **[s01 pre-flight, Chester]** The day before the lecture, open `mlmed.org/tools/xray/` on the lecturer's laptop. Drag in the test X-ray from `library/lectures/lec-07/assets/test-xray.png`. Make sure the heatmap appears and the table shows 18 rows with probabilities. If the page does not load — open the backup image `library/lectures/lec-07/assets/backup/chester-pneumonia-result.png` in a separate tab and switch with Alt+Tab.
- **[s04 freshness]** Open `https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices` and check the cumulative FDA figure. At the time of writing — 1,451 as of the end of 2025; by May 13, 2026, 1,500–1,550 is expected. If the number has grown — update the spoken figure on s04 and s07.
- **[s12 freshness]** Open `https://mosmed.ai/` or the Remedium news item and check the "14 million studies" figure (as of the end of 2025). If an update was published in Q1 2026 — replace it with the new one.
- **[s19 freshness]** The day before the lecture, run this prompt in ChatGPT or YandexGPT: "Explain sensitivity and specificity for AI diagnostics using mammography as an example, as if for a second-year student at a technical university." Save the answer as control-output. Reread it before the lecture — what the AI did well, what is suspicious.
- **[s22 freshness]** Open `https://www.beckershospitalreview.com/` with the search query "ChatGPT healthcare 40 million." On May 13, 2026, the figure is expected to be ≥ 40M; if it has grown — replace it verbally. Also check OpenAI/Rock Health 2025 (search "Rock Health Consumer Adoption 2025" — `https://rockhealth.com/insights/`): "3 in 5 adults turn to LLMs about health" — if the figure has changed, replace it verbally.
- **[s07/s11/s17a]** Read fragments [s07], [s11], and [s17a] aloud with a stopwatch. Each must fit within the slide's timing. If a fragment runs over — cut it, do not rush.
- **Check the internet in the auditorium.** If the WiFi drops at delivery time — open the PDF deck in Adobe Reader, read without the live demo in s01, go straight to the backup PNG.
- Keep a clock in front of you, don't depend on the room's clock. Print the per-slide checklist on paper.

---

## Section 0. Opening: AI on an X-ray in three seconds (9 min)

### [s01 · 3 min] — AI marks a pathology in three seconds

[I turn on the laptop, on the projector — a browser with `mlmed.org/tools/xray/` open. An X-ray image is ready on the desktop.]

"Hello. Before we say the first word about medicine — look here.

[pause 3 seconds]

I have an ordinary browser here. The page `mlmed.org` is open — the public tool Chester AI. Now I'll drag this chest X-ray into the window.

[action: drag-and-drop the file]

[pause 3 seconds]

See? About three seconds have passed. Notice — the model produced eighteen rows, probabilities across eighteen pathologies. Pneumonia, cardiomegaly, atelectasis, pleural effusion. And on the right — a heatmap: yellow and red spots show where the model was looking when it made its decision.

[slowly, with emphasis]

Three things in this demonstration set the tone for the entire lecture today. First: the model runs locally, in the browser. The image does not go to a server. This is not an accident — it is a design choice, an engineering decision. Medical data is a special category, and we will come back to this in the fourth section.

Second: this is not ChatGPT. This is narrow computer vision — a descendant of the CheXNet model from 2017. ChatGPT cannot place a pathology label on an X-ray in three seconds. Chester can — but it can't write poetry.

Third, and most important: this is roughly 2017–2024 technology in a routinely working form. Five years ago such a capability was a lab demonstration. Today — an ordinary browser.

At the end of Lecture 1 we had a camera demo with a YOLO person detector. Chester is a related story. The same narrow computer vision, classification plus localization. The difference is in the cost of an error. YOLO not seeing a person — that's one cost. Chester not seeing the shadow of a tumor — an entirely different one.

And it is precisely out of this difference — clinical validation, regulation, accountability, stakes measured in millions of people — that the rest of the lecture will be made."

[I close Chester, move to s02.]

### [s02 · 6 sec] — Cover

[On the slide — a large "07," the title.]

"Lecture seven. AI in medicine and pharmaceuticals."

[pause 2 seconds; move to s03]

### [s03 · 1.5 min] — First your estimate, then the data

[On the slide — three questions large, no answers.]

"Before I show the figures — let's do three questions. Raise your hands.

**Question one.** How many AI medical devices are officially approved by the US FDA by the end of 2025? Fewer than a hundred? [pause, counting] From a hundred to five hundred? [pause] From five hundred to a thousand? [pause] More than a thousand? [pause]

**Question two.** In the past year, have you received a medical result that involved AI? An X-ray, CT, MRI, ECG, dermatology scan. [pause, counting hands]

**Question three.** Do you trust an AI diagnosis more than a human doctor? Not equally — specifically more. [pause]

Good. Remember your estimates. Now I'll show what the data says."

[Move to s04.]

### [s04 · 2 min] — What the numbers say: FDA and mosmed.ai

[On the slide — a bar chart of FDA growth 2015→2025 + an info-card for mosmed.ai.]

"On the first question. By the end of 2025 the FDA had authorized **one thousand four hundred fifty-one** AI/ML medical devices cumulatively. As of today, May 2026, the real figure is already around one thousand five hundred. Of these, roughly seventy-six percent are radiology. That is, computer vision for X-ray, CT, MRI, mammography. LLM devices on that list — just a handful.

On the second question — most of you have probably received an AI result without even knowing it. If your region is connected to the mosmed.ai platform — and that's seventy-four regions of Russia — then the X-ray you had done most likely passed through an AI service. Over five years of operation the platform has processed **more than fourteen million studies**. These are operational figures, verified against official sources from the Moscow Department of Health.

On the third question — most people answer "no," even if they know AI is statistically more accurate. And that's the right intuition. We will come back to it in the fourth section, when we talk about who is accountable for an AI error.

Interim takeaway: AI in medicine is no longer futurology. It is infrastructure we already live in."

[Move to s05.]

### [s05 · 2 min] — The lecture's central question

[On the slide — the central question, large, in an Ocean rounded box.]

"From here — the main question of today's lecture.

[slowly]

**Which AI promises in medicine have actually come true by 2026 — and who is accountable when an AI diagnosis turns out to be wrong?**

This question has two parts, and the combination of parts is not accidental. The first part — what has actually come true. AI diagnostics in radiology — yes. Drug discovery — partly. A fully autonomous AI doctor — no. This is a diagnostic question, and we'll work through it in sections two and three.

The second part — who is accountable. As of May 2026, no major jurisdiction has recorded high-profile precedent-setting malpractice cases tied specifically to an AI diagnosis. But a legal consensus is already forming: final clinical responsibility stays with the doctor. We'll arrive at this answer in section four.

These two parts — the reality of the promises and the architecture of accountability — form the axis of the lecture. The road map we're following: four sections — a map of AI in medicine, diagnostics as a mirror, drug discovery, ethics and accountability. After that — a conclusion and three observations for the piggy bank of the final synthesis in Lecture 17."

[Move to s05b.]

### [s05b · 12 sec] — Divider

"This is the first section of five — a map of AI in medicine."

[Move to s06.]

---

## Section 1. A map of AI in medicine (7 min)

### [s06 · 2.5 min] — Four types of AI applications

[On the slide — a 2×2 matrix of modality × scope with four cells.]

"AI in medicine is not one industry and not one technology stack. It's convenient to lay applications out along two axes.

The first axis — modality. Image or signal versus text or molecule. Image and signal tasks — X-ray, CT, MRI, ECG, dermatology scan — are handled by computer vision. Text and molecule tasks — clinical notes, molecule generation, protein structure — are handled by entirely different architectures: transformers for text, generative chemistry for molecules, AlphaFold for proteins.

The second axis — scope. One patient versus a population or pharma. One patient — a diagnosis or prescription for a specific person. Population — screening programs, drug discovery, epidemiological monitoring.

The intersection gives four cells. **Image plus one patient** — AI diagnostics, the largest cell, seventy-six percent of the FDA list: mosmed.ai, IDx-DR, Aidoc. **Image plus population** — population health analytics, analysis of screening programs. **Text-molecule plus one patient** — personalized medicine, geno- and pharmaco-AI. **Text-molecule plus population** — drug discovery: AlphaFold, Insilico, Generate Biomedicines.

[with emphasis]

This matrix matters not as a pretty diagram. It is design-driven. Modality determines the ML stack: computer vision versus NLP versus generative chemistry. Scope determines the regulatory path: a single-patient image system is a medical device under FDA SaMD logic. Population analytics goes a different route. So the two axes are the grounds for engineering and regulatory decisions.

Today we focus on the left column — AI diagnostics in section two — and on the bottom-right cell — drug discovery in section three."

[Move to s07.]

### [s07 · 2 min] — FDA growth timeline

[On the slide — a bar chart 2015→2025, growth to 1,451.]

"Let's look at the concrete growth figures. Between 1995 and 2015 the FDA approved cumulatively about thirty-three AI/ML devices — three percent of the current volume. Between 2015 and 2025 — growth from dozens to over a thousand.

The turning point is the years 2022–2024. In 2023, two hundred twenty-one new devices were approved. In 2024 — two hundred fifty-eight. In 2025 — two hundred ninety-five. Cumulatively, by the end of 2025 the list holds one thousand four hundred fifty-one.

[pause]

And once again — seventy-six percent of them are radiology. Cardiology and neurology come next by volume. LLM devices — just a handful. This is the answer to the question "what exactly works": predominantly computer vision for medical images.

For an engineer this means a simple thing. When you hear the phrase "AI in medicine" — in eight cases out of ten it's a conversation about CV classification of images. Not about conversational AI, not about an autonomous doctor."

[Move to s08.]

### [s08 · 2.5 min] — Medicine as a showcase case

[On the slide — three icon cards: stakes, regulation, operational scale.]

"You might fairly ask: I'm not a doctor, why should I dive deep into medical AI? Three reasons.

**First — high stakes.** A model error in credit scoring is a financial loss. An error in a marketing recommendation is a missed conversion. An error in a medical AI model is a missed diagnosis, an unnecessary biopsy, a wrong prescription. A qualitatively different cost of error. And it is exactly this that forces an engineer to think about things that could be deferred in less-regulated areas: confidence calibration, audit trail, post-market monitoring, fallback scenarios.

**Second — strict regulation.** Medical AI is the first field in which an engineer meets real regulation: FDA SaMD, EU AI Act Annex III, Roszdravnadzor. The penalties for violations — approval revocation, fines, civil suits. If you've learned to design AI to meet these requirements — you've mastered skills that will serve you in finance, in the automotive industry, in aviation.

**Third — transparent operational scale.** Unlike industrial projects, where "productivity growth of X percent" is estimated indirectly, medical diagnostics gives direct measurable metrics: number of studies, screening sensitivity, time to diagnosis. mosmed.ai over five years — fourteen million studies. That is not a marketing estimate, those are actual scans.

And a bonus. On August 2, 2026 — two and a half months after our lecture — the first stage of the EU AI Act takes effect for high-risk AI. This is not a distant prospect. It is an actionable timeline.

If you've learned to assess AI here — you've learned to assess AI everywhere."

[Move to s08a.]

### [s08a · 12 sec] — Divider

"The second section of five — AI diagnostics as a mirror."

[Move to s09.]

---

## Section 2. AI diagnostics as a mirror (14 min)

### [s09 · 2 min] — The AI-diagnostics pipeline

[On the slide — a pipeline of four stages: Input → Model → Output → Workflow.]

"How AI diagnostics works technically. This is primarily computer-vision classification: input — a medical image, output — a probability distribution over pathology classes plus a bounding box or heatmap.

The pipeline fits into four stages.

**First — Input.** A raw image: a DICOM file from a CT scanner, a JPEG of a dermatology scan, a PNG of a mammogram. Preprocessing: resizing, normalization, sometimes — removal of patient labels at the pixel level.

**Second — Model.** A convolutional network — historically ResNet, EfficientNet — or a Vision Transformer. Usually pre-trained on ImageNet and then fine-tuned on a medical dataset. In 2024–2026 specialized foundation models appeared — MedCLIP, BiomedCLIP, RoentGen, trained directly on medical images.

**Third — Output.** A probability score from zero to one for each class. Often — a heatmap generated by the Grad-CAM technique, which shows which pixels contributed to the prediction.

**Fourth — workflow.** The doctor sees the image, the heatmap, and the probabilities and makes a decision. AI here is decision-support, not decision-maker.

The historical model of this pipeline is CheXNet, 2017, a one-hundred-twenty-one-layer DenseNet, fourteen chest pathologies. Modern models are more accurate, but the methodological foundation has stayed the same.

An important caveat about the confidence score. This is a model-internal score, not a Bayesian posterior probability. Interpreting "the AI is 87 percent confident" as "the probability of pneumonia is 87 percent" is incorrect. Calibration procedures are needed."

[Move to s10.]

### [s10 · 3 min] — Four metrics and the PPV paradox

[On the slide — a 2×2 confusion matrix + 4 formulas.]

"This is a key methodological section of the lecture. For medical AI, ordinary accuracy is an insufficient metric. Four connected concepts are needed.

Abbreviations. TP — true positive, a sick person correctly identified as sick. FN — false negative, a sick person missed. FP — false positive, a healthy person wrongly flagged. TN — true negative.

**Sensitivity.** Sens equals TP divided by TP plus FN. "Of all the sick, what fraction did the AI catch." Critical for screening, where a miss is a catastrophe: early-stage cancer, stroke, heart attack.

**Specificity.** Spec equals TN divided by TN plus FP. "Of all the healthy, what fraction did the AI correctly not scare." Critical for confirmation tasks, where a false positive itself does harm: biopsy, chemotherapy, panic.

**Prevalence.** The prevalence of the disease in the population. This is not a property of the model — it is a property of the deployment population.

**PPV.** Positive Predictive Value. TP divided by TP plus FP. "If the AI said sick, what is the probability of actual illness." This is the metric the clinician sees.

[slowly, with emphasis]

And the main subtlety — sensitivity and specificity do not depend on prevalence. PPV does. I'll show it with numbers.

Let's look at CheXNet's numbers on pneumonia detection: sensitivity about ninety-four percent, specificity about eighty-nine. Sounds excellent.

[pause 2 seconds]

In a hospital sample, where the prevalence of pneumonia is thirty to fifty percent, the PPV comes out around eighty percent. A good clinical metric.

[pause 2 seconds]

But take the same model and apply it as screening in a general population, where the prevalence of pneumonia is one percent. The PPV becomes about eight percent. Out of a hundred patients flagged by the AI as positive, actually sick — eight. The other ninety-two are false positives.

[pause]

"Ninety-four percent accuracy" sounds good. "Eight percent PPV in screening" is a completely different perception of the same model. So when assessing a medical AI model — never trust a single number. Ask: what is the prevalence in the population? What is the sens, what is the spec, what is the PPV under operational conditions? Four questions — the minimum due diligence."

[Move to s11.]

### [s11 · 3 min] — Three studies: imaging vs reasoning

[On the slide — three rows: Liu 2019, MASAI 2024–25, Goh 2024.]

"People often ask: has AI already surpassed doctors? The correct answer is — it depends on the task. Three benchmark studies.

**First — Liu, 2019, Lancet Digital Health.** A meta-analysis of fourteen works. AI sensitivity — eighty-seven percent. Clinicians' — eighty-five. A modest difference.

**Second — MASAI Sweden, 2024–2025, Lancet.** The strongest evidence of the clinical benefit of AI mammography. One hundred thousand Swedish women: double reading by two radiologists versus one radiologist plus AI.

Sensitivity of AI-supported screening — **eighty and a half percent** versus seventy-three point eight. Cancer detection rate — six point four per thousand versus five. Reduction in radiologist workload — **forty-four percent**. One radiologist with AI did the work of two.

Follow-up 2025: a twelve percent reduction in the interval cancer rate. The additional cancers found by AI are clinically significant cases. The strongest evidence for "AI plus doctor beats a doctor alone" in radiology.

**Third — Goh, JAMA, October 2024.** Not imaging anymore, but diagnostic reasoning. Fifty doctors working with GPT-4 and without. Median with GPT-4 — seventy-six percent. Without — seventy-four. Statistically insignificant. The surprise: **GPT-4 alone** produced a higher score than a doctor with GPT-4.

[pause]

This is the paradox of joint work — *in the Goh et al. paper it is called the augmentation gap*. Notice: users don't load the AI up fully — they don't trust it, don't know how to integrate it, keep the AI in the role of a "second opinion" that can be ignored.

Takeaway for an engineer. The question "AI or doctor" is framed wrong. The right ones are — which task, which workflow, how are the AI and the doctor integrated."

[Move to s12.]

### [s12 · 3 min] — The Russian case: mosmed.ai

[On the slide — pipeline image → mosmed.ai → result + 6 info-cards.]

"A concentrated example of how the AI-diagnostic promise came true in operational form is the Moscow platform mosmed.ai.

The experiment started in November 2019 as a city project of the Moscow Department of Health and the Research and Practical Clinical Center for Diagnostics and Telemedicine. In May 2024 — a federal launch as MosMedAI.

Metrics as of early 2026, verified against official sources.

**More than fourteen million studies** analyzed by AI over five years. **Seventy-four regions of Russia** connected. **More than two thousand medical organizations** integrated. **More than eighteen million medical images** processed. **About seventy AI services** across forty-three clinical areas — chest radiography, lung CT, mammography, osteodensitometry, brain CT. **Eleven national standards** developed. **About three hundred reference datasets.**

Architecturally mosmed.ai is a federated AI platform. Different vendor models — Sber AI Lab, Care Mentor AI, Third Opinion, Webiomed — pass through a single deployment, a single benchmarking system, and a single doctor interface. This is operational AI infrastructure. Not one monopoly supplier, but a marketplace of verified models.

[a caveat, in a calm tone]

A small caveat about a figure. In the public sphere a claim circulates of "four billion rubles saved in the mandatory health-insurance system from mosmed.ai per year." We did not find this figure in primary sources. A similar figure "two hundred ninety-six billion" is the total saving from the digitalization of Moscow healthcare, not specific to mosmed.ai. So I use the operational metrics — fourteen million studies, and so on. They are verified and sufficient.

A bridge to the rest of the lecture. Here the promise of AI diagnostics came true in operational form. In section three we'll see the drug-discovery promise in peer-reviewed form — Insilico Rentosertib. And right alongside it — a promise that did not come true: DSP-1181."

[Move to s13.]

### [s13 · 2.5 min] — Where AI fails: bias in CV

[On the slide — 2 case cards: dermatology + pulse oximeter.]

"AI diagnostics works well within the training distribution. Outside that distribution it can fail asymmetrically. And these failures are not bugs, but a consequence of design choices.

**Case one — dermatology and skin tone.** Most publicly available dermatological AI datasets, including ISIC, have historically overrepresented light-skinned patients from the US, Europe, Australia. Daneshjou and colleagues, 2022, Science Advances, tested several previously published dermatological algorithms on a diverse sample. On darker skin tones by the Fitzpatrick scale, sensitivity was significantly lower — by tens of percent — compared with light skin.

[pause 2 seconds]

An important nuance. Human dermatologists also performed worse on dark skin. But fine-tuning on the diverse DDI dataset closed this gap for the AI. The fine-tuned models ultimately surpassed dermatologists on dark skin. So the problem is solvable — on the side of training-dataset selection.

**Case two — pulse oximeters.** This is a case where bias enters the AI through the input sensor, not through the dataset. Pulse oximeters measure oxygen saturation via optical absorption. Per the work of Sjoding and colleagues, 2020, NEJM, in patients with dark skin pulse oximeters systematically overestimate SpO2 compared with direct blood-gas analysis. In Black patients hypoxia is missed more often. The FDA issued a safety communication in 2021. AI systems that use SpO2 as an input feature — for example, to predict COVID hospitalization — inherit this sensor bias.

[slowly]

The engineering takeaway for both cases is simple and important. **The validation sample must cover the deployment population.** This is not an academic point, it is a professional responsibility. And one of those things that distinguishes an AI engineer with medical experience from someone just starting out."

[Move to s13a.]

### [s13a · 12 sec] — Divider

"The third section of five — drug discovery: promises and reality."

[Move to s14.]

---

## Section 3. Drug discovery: promises and reality (14 min)

### [s14 · 1 min] — Mid-lecture callback

[On the slide — the central question plus three anchors: mosmed ✓, Rentosertib ?, DSP-1181 ?]

"We've gone through half the lecture. An interim summary.

AI diagnostics — the promise came true. mosmed.ai is confirmation of that, the MASAI RCT is confirmation of that. Drug discovery — the promise was to accelerate it tenfold. What actually works as of 2026?

Now we'll work through the drug-discovery pipeline, then — two concrete cases. One successful — Insilico Rentosertib. One the opposite — DSP-1181. After that — the regulatory field and the transition to ethics."

[Move to s15.]

### [s15 · 2.5 min] — The drug-discovery pipeline

[On the slide — a 5-stage pipeline with AI/human markers.]

"Traditional development of a new drug is ten to fifteen years and **one to two billion dollars** per approved drug. This is data from DiMasi 2016 and Wouters 2020. The chance of going from Phase 1 to approval — about six point seven percent. That is, of fifteen candidates, one reaches the patient.

Let's look at the five stages.

**Target identification.** Which biological target protein to attack. Here AlphaFold works for structure prediction and AlphaProteo for the design of binders.

**Hit discovery.** The search for a candidate molecule with an initial activity signal. Here — generative chemistry: Insilico Chemistry42, Exscientia, Generate Biomedicines.

**Lead optimization.** Improving selectivity, stability, minimizing toxicity. Here — simulation plus ML.

**Preclinical.** Experiments on cells and animals. ADMET modeling — Absorption, Distribution, Metabolism, Excretion, Toxicity.

**Clinical Phase 1, 2, 3.** Experiments on humans. Safety, efficacy, confirmatory. Here AI assists the workflow — patient stratification, recruitment — but does not affect the attrition rate.

[with emphasis]

And here's the main point. AI accelerates stages one through three significantly: from four to five years down to twelve to eighteen months in the best cases. Stages four and five remain the domain of biology. The marketing phrase "AI will speed up drugs tenfold" conflates two different claims. **AI accelerates design — that's verified. AI accelerates approval — that's not verified**, because eighty percent of a drug's timeline is clinical trials, and AI does not compress them."

[Move to s16.]

### [s16 · 2.5 min] — AlphaFold and AlphaProteo

[On the slide — 3 evidence cards + AlphaFold 3D snapshot.]

"The most visible achievement of AI in drug discovery is DeepMind's lineup of foundation models. Half of the Nobel Prize in Chemistry 2024. Hassabis and Jumper for AlphaFold shared it with Baker for computational protein design. This is a callback to Lecture 1.

**AlphaFold 2, 2021.** The fifty-year-old problem of protein-structure prediction, solved. By 2024, the open database held **more than two hundred million structures**. The database is free, `alphafold.ebi.ac.uk`. DeepMind claims more than two million researcher-users.

**AlphaFold 3, Nature, May 2024.** A diffusion architecture. From proteins to biomolecular complexes — protein-DNA, protein-RNA, protein-ligand. **An improvement of about fifty percent** on the PoseBusters benchmark against classical docking methods. Classical docking has been the main tool for thirty years. AlphaFold 3 is the first AI system to surpass it.

**AlphaProteo, September 2024.** De novo design of protein binders. **An eighty-eight percent success rate** for the target protein BHRF1. An affinity improvement of three to three hundred times. The first AI-generated binder for VEGF-A — a key factor of angiogenesis in oncology.

A caveat. The AlphaProteo data was obtained in DeepMind's wet-lab; independent replication has not been publicly recorded. We're citing a DeepMind claim, not a consensus result.

[with emphasis]

An important engineering detail. AlphaFold predicts structure. Drug discovery also requires lead optimization, ADMET, validation. AlphaFold accelerates one stage — target identification. It is an accelerator, not a replacement for the pipeline."

[Move to s17a.]

### [s17a · 2.5 min] — Insilico Rentosertib — a success

[On the slide — a 3-event timeline + info-card +98.4 mL FVC.]

"Insilico Medicine Rentosertib. Code ISM001-055. As of today — the first AI-designed drug with a peer-reviewed positive Phase IIa readout. Nature Medicine, June 2025.

Design. Phase IIa, randomized double-blind placebo-controlled. Seventy-one patients with IPF — idiopathic pulmonary fibrosis, a serious chronic lung disease. Twenty-one centers in China. The drug is a TNIK inhibitor.

Result for the sixty-milligram-per-day group, twelve weeks. Mean change in FVC — forced vital capacity. In the Rentosertib group — **plus ninety-eight point four milliliters**. In placebo — **minus twenty point three milliliters**. A difference of about one hundred eighteen milliliters — clinically significant for IPF.

Safety. The most common side effects — diarrhea and liver-function abnormalities, about fifteen percent each.

Insilico claims that the path from target to preclinical candidate took about eighteen months — versus the traditional four to five years. This estimate is not independently verifiable. But **the fact of a peer-reviewed Phase IIa is verifiable** through Nature Medicine. A qualitative shift.

[slowly]

The engineering takeaway. AI accelerated design — verified. Clinical efficacy is separate biology. Phase 3 is still ahead.

The Russian context. MADD — ITMO plus Sber AI Lab, peer-reviewed work. The AIDD Center — an alliance of Sber and AIRI, December 2024. An alliance on CD137 oncology, May 2024. But an honest caveat: **not a single Russian AI-designed drug in Phase 1 or above has been recorded as of May 2026**. All RU programs are preclinical."

[Move to s17b.]

### [s17b · 2.5 min] — DSP-1181 — reality

[On the slide — a 3-event timeline 2020→2022→2026 Discontinued.]

"In parallel with the success story — DSP-1181. A drug that a decade ago was pointed to as "proof of the AI revolution," and which never reached patients.

January 2020. Sumitomo Dainippon Pharma and Exscientia announced the launch of a Phase 1 drug for obsessive-compulsive disorder. The path from target to Phase 1 — about twelve months versus the traditional four to five years. The drug was called "the first AI-designed drug in clinical trials." In 2020–2022 — the industry's main marketing example.

What happened next. In 2022 the Phase 1 in Japan was halted. The reason for discontinuation was not publicly disclosed. As of May 2026 the global R&D status of DSP-1181 is Discontinued.

[pause]

The engineering lesson. **AI accelerated design — that's verifiable.** That part works. **But clinical efficacy is separate biology.** The marketing "AI drug equals fast plus effective" is two combined claims that in reality are independent. AI did not make DSP-1181 effective. AI accelerated the search for a candidate. The candidate did not show a clinical result.

Useful context. Recursion and Exscientia announced a merger in August 2024, six hundred eighty-eight million dollars. Exscientia ceased to exist. The merger is a signal that AI drug discovery as a standalone business is a difficult economics.

The common thread of Rentosertib and DSP-1181. Both cases are consistent with reality. The ninety percent clinical attrition rate is a statistic AI has nothing to do with. Attrition is determined by biology, not by design. **The two claims must be separated**: how much we accelerate design, and how much we raise the approval probability. Only the first is what AI affects."

[Move to s18.]

### [s18 · 2 min] — Regulation: three jurisdictions

[On the slide — a 3-column condensed table US/EU/RU + PCCP contrast.]

"In three major jurisdictions medical AI is high-risk. The approaches differ in process, not in principle.

**USA, FDA.** PCCP — Predetermined Change Control Plan, final guidance on December 4, 2024. Before PCCP, every update to an AI model required a new submission of twelve to eighteen months. With PCCP the vendor declares permissible changes in advance, and the FDA pre-authorizes them. The vendor updates the model without a full re-submission. The first production-grade CI/CD for medical AI.

**European Union, EU AI Act.** Regulation 2024/1689. **August 2, 2026** — high-risk non-MDR systems. **August 2, 2027** — MDR-regulated medical AI, the main body of clinical devices. Vendors are preparing simultaneously. The first stage is in two and a half months.

**Russia, Roszdravnadzor.** An expedited procedure since March 1, 2025. Fifty-seven registered AI medical devices by mid-2026.

The engineering takeaway. **Medical AI in three major jurisdictions is high-risk. One-and-done approval is replaced by post-market surveillance plus continuous monitoring.** If you're designing AI for a medical device — design with PCCP in mind from the start."

[Move to s19a.]

### [s19a · 12 sec] — Divider

"The fourth section of five — AI as an explainer and its limits. An applied section, and right after it — ethics and accountability."

[Move to s19.]

---

## Section 4. AI as an explainer and its limits (15 min)

### [s19 · 3 min] — AI as an explainer

[On the slide — a 3-card layout: the pattern + what changes + the caveat.]

"Before the heavy topics — a short applied section. AI as an explainer.

One of the consistently working patterns for talking with an LLM is the formula "explain it as if for an N-th-year student." You say "explain sensitivity and specificity using mammography as an example, as if for a second-year student at a technical university" — and the model produces a coherent explanation at the right level of detail.

This is not magic. It's a pattern. It works because the LLM's training data contains many texts labeled with a target audience — lectures, textbooks, popular science.

In medicine this pattern changes the scenarios. An intern reading up on a rare disease at night — now gets a first-pass explanation from the LLM in a minute. A resident working through a new technique — the same. A doctor encountering a new class of drugs — the same. The time from question to first approximation drops from hours to seconds.

[pause]

At the same time, the quality is unstable. AI is excellent at retelling a textbook: definitions, basic mechanisms, typical examples. AI is poor at conveying a clinician's tacit knowledge: when a rule doesn't hold, which combinations of signs are suspicious to an experienced doctor. The formal part of knowledge — is retold. Professional intuition — is not.

And most importantly — the caveat. AI gives figures without a source. AI retells a five-year-old textbook as current practice. AI confidently pronounces the wrong drug name.

[slowly, with emphasis]

The rule for medicine — and for any high-stakes context. **AI is a first approximation, not a source of truth.** Final verification — a textbook, clinical guidelines, a senior colleague.

This skill — distinguishing "the AI explained it excellently" from "the AI gave a figure that needs checking" — is something we train throughout the course."

[Move to s20.]

### [s20 · 1 min] — Transition to ethics

[On the slide — a stock photo of a medical team + 3 topics.]

"In medical AI the stakes are at their highest: a model error equals a diagnostic error equals harm to the patient. So the next five slides are four concrete topics an engineer is obliged to think about at the design stage, not post-hoc.

The first — bias in medical AI, on the classic example of Obermeyer 2019. The second — three LLM anti-patterns from 2023–2025. The third — the security of medical data on the example of Change Healthcare. And the fourth — who is accountable when the AI errs.

The tone is serious, without alarmism. The goal is to teach us to think about the limits from the start, at the design stage."

[Move to s21.]

### [s21 · 3 min] — Obermeyer 2019: bias through proxy choice

[On the slide — a 3-box mechanism + a chart 26% + an arrow 17.7→46.5%.]

"Obermeyer and colleagues, Science, 2019. The gold-standard case study of bias in medical AI. Cited more than three thousand times. Mandatory reading for an AI engineer in healthcare.

Context. In the US, a commercial algorithm Impact Pro operates, developed by Optum — a subsidiary of UnitedHealth. It's applied to **about two hundred million Americans**. It identifies high-risk patients for high-risk care management programs.

What was found. **At the same risk score, Black patients were substantially sicker than white patients.** At the same score level — **twenty-six percent more chronic conditions**.

Why. The algorithm was trained to predict healthcare cost as a proxy for healthcare need. These variables correlate but are not identical.

Black patients historically spent **about eighteen hundred dollars less per year** on healthcare than equally-sick white patients. Because of access disparities: less insurance coverage, geographic barriers, distrust of the system, discrimination in practice. The algorithm saw: low spending — less sick. In reality they were just as sick, but received less care.

[pause]

The fix. When they retrained on a hybrid proxy — cost plus chronic conditions — **the bias dropped by eighty-four percent**. The share of Black patients in high-risk care management rose **from seventeen point seven to forty-six point five percent**. Specific patients who gained access to care.

[slowly, with emphasis]

The engineering lesson. When you choose a proxy for a goal — ask: which demographic groups might have systematically different access to that proxy? If "yes" — the proxy creates bias. **The choice of a metric is the choice of a policy**, even when no one is thinking about policy."

[Move to s22.]

### [s22 · 4 min] — Three LLM anti-patterns

[On the slide — 3 case cards: Tessa, adversarial 83%, 40M self-diagnosis.]

"An LLM in medicine is not the same thing as medical AI. Medical AI that passes FDA approval is a specialized CV or tabular model with confirmed clinical validation. An LLM in a medical context is a general-purpose model that happens to be used for medicine. Three documented anti-pattern cases as of 2023–2026.

**Case one. NEDA Tessa, a vendor-accountability story.** NEDA — a nonprofit organization supporting people with eating disorders. Since 2018 NEDA used the chatbot Tessa as a first line for its helpline. Originally Tessa was rule-based: a decision tree, no generation, no advice outside approved scenarios. Eating disorders require clinical safety design.

**In early 2023 the vendor Cass unilaterally switched Tessa from rule-based to a generative LLM** — without coordinating with NEDA. On May 30, 2023, activist Sharon Maxwell published screenshots: Tessa was advising losing one to two pounds a week, maintaining a calorie deficit of five hundred to a thousand a day. Classic eating-disorder triggers. NEDA took Tessa down within twenty-four hours.

The frame is vendor accountability, not chatbot history. Cass changed the nature of the system without coordinating with the principal. **Generative AI is not rule-based AI.** Any transition from deterministic to generative requires new clinical validation.

**Case two. Adversarial hallucination.** Nature Communications Medicine, 2025. Six leading LLMs were tested on three hundred clinical vignettes with a planted fake — a made-up lab result, a made-up disease. **The models repeated or expanded the fake in eighty-three percent of cases**. A mitigation prompt "verify the facts" cut the rate in half, not to zero.

The engineering takeaway. LLMs are gullible to planted errors. Human fact-verification is required for every fact in a medical context. This is about workflow, not about improving the model.

**Case three. Patient self-diagnosis.** In parallel, a mass phenomenon is underway. Per Becker's Hospital Review, **about forty million Americans** use ChatGPT for healthcare. Per OpenAI and Rock Health 2025 — three in five adults turn to LLMs with health questions.

The engineering implication. If you build a medical-adjacent LLM product — you're in an industry with mass unsupervised use. Design choices scale to tens of millions.

[slowly]

How is this different from Obermeyer? Obermeyer — bias in tabular AI. Here — a generative LLM in open-ended medical advice. Different countermeasures. **Bias in medical AI is a class of errors with different mechanisms.**"

[Move to s23.]

### [s23 · 3 min] — Change Healthcare and 152-FZ

[On the slide — a news screenshot + 5 info-cards.]

"Medical data is the most protected category. And the most valuable to attackers. It contains PII plus medical history, which cannot be "undone." Unlike a credit card number, which a bank blocks within minutes.

**The case — the Change Healthcare breach, February 2024.** The largest healthcare data breach in US history.

On February 21, the ransomware group BlackCat attacked Change Healthcare — a subsidiary of UnitedHealth, processing a third of all claims in the US. The vector — vulnerable Citrix remote access without MFA.

The numbers. **One hundred ninety million Americans** — the affected volume of PHI. About fifty-seven percent of the US population.

[pause 2 seconds]

**Six terabytes** exfiltrated. **Twenty-two million dollars in ransom** paid in Bitcoin.

[pause 2 seconds]

Total recovery cost — **two billion four hundred fifty-seven million dollars**. A multi-week disruption of claims processing.

[pause]

The AI connection. Medical AI training datasets inherit the security risk of medical data. mosmed.ai has more than eighteen million images. What if such a dataset is exfiltrated? Anonymization does not equal complete anonymity. The canonical illustration — the re-identification of the medical record of the governor of Massachusetts through matching a HIPAA-compliant deidentified dataset with a public voter roll. Sweeney, 2002.

Regulation. **HIPAA** — US, 1996. **GDPR** — EU, 2016, health data a sensitive special category. **152-FZ** — Russia, with amendments 2024–2025. **23-FZ** of February 28, 2025 — data localization: the personal data of Russian citizens is not processed outside Russia as of July 1, 2025.

[slowly]

The engineering takeaway. In designing medical AI, you're designing a target for criminal groups. The defense: data localization, de-identification plus differential privacy, a secure-by-design pipeline. **For a Russian deployment, using the OpenAI or Anthropic API directly for patient data is noncompliance.** This is a compliance reference point as of July 1, 2025."

[Move to s24.]

### [s24 · 3 min] — Four actors of accountability

[On the slide — a 2×2 quadrant with doctor/operator/vendor/regulator.]

"This is the central section for the central question of the lecture. Notice — we've finally arrived at the answer.

AI diagnostics works. Drug discovery partly works. Bias and LLM anti-patterns are real. Who is accountable when the AI errs?

The 4-actor framework. Price, 2019, U Michigan Law School. Gerke, 2020, Penn State Dickinson Law (formerly — Harvard Petrie-Flom). Four actors with different combinations of technical control and legal accountability.

**The doctor — high control, high accountability.** Makes the final diagnosis. AI is an input, not the decision-maker. Legally the doctor is the primary accountable party. The AI's suggestion is a "second opinion." Only the doctor has the full picture: history, examination, lab results, the AI's answer as one of the inputs.

**The healthcare operator — hospital, clinic, Department of Health — medium control, medium accountability.** Chooses the AI supplier. Ensures staff training. Monitors the system's performance. Deploys AI without adequate training — bears accountability for foreseeable misuse.

**The AI vendor — high control, low-to-medium accountability.** Designs the model. Makes safety claims at registration. Provides PCCP updates. A defect in the design — accountability under product liability. With faithful disclosure and proper post-market surveillance, accountability is limited.

**The regulator — FDA, EU Notified Bodies, Roszdravnadzor — low control, high oversight.** Approves systems. Conducts post-market surveillance. Not accountable for individual cases, but bears systemic responsibility for the quality of approval.

[slowly, with emphasis]

**The central principle.** Final clinical responsibility is not divided between the human and the algorithm.

**The doctor makes the diagnosis. The AI suggests. Final clinical responsibility undivided.**

This is the legal consensus as of 2026 in all three major jurisdictions.

What an engineer should take away. If you work in the vendor role — your responsibility is to design AI so that the doctor can fulfill theirs. Three principles — on the next slide.

An honest note. As of May 2026 there are no high-profile precedent cases of AI medical malpractice. Lawsuits grew by fourteen percent in 2024, but there's no landmark case yet. Tort law is catching up to the technology."

[Move to s24a.]

### [s24a · 12 sec] — Divider

"The fifth section of five — the conclusion."

[Move to s26.]

---

## Section 5. Conclusion (6 min)

### [s26 · 2 min] — Three main takeaways

[On the slide — a 3-card summary: diagnostics ✓ / drug discovery partly / responsibility on the doctor.]

"Let's briefly describe what we've gone through — three takeaways.

**Takeaway one. AI diagnostics works.** This is LO1 and LO2. mosmed.ai processed more than fourteen million studies over five years across seventy-four regions of Russia. The FDA approved one thousand four hundred fifty-one AI/ML devices cumulatively by the end of 2025; seventy-six percent are radiology. The MASAI Sweden RCT confirmed that AI-supported mammography raises screening sensitivity from seventy-three point eight to eighty and a half percent while cutting radiologist workload by forty-four. This is not futurology. It is a computer-vision pipeline of the 2017–2024 level in production form.

**Takeaway two. Drug discovery works partly.** This is LO2 and LO3. AlphaFold predicted more than two hundred million protein structures and won the Nobel Prize in Chemistry 2024. Insilico Rentosertib became the first AI-designed drug with a peer-reviewed positive Phase IIa in Nature Medicine. DSP-1181 — discontinued. AI accelerates discovery five- to tenfold. The ninety percent clinical attrition rate AI does not change.

**Takeaway three. The accountability is on the doctor.** This is LO3. The AI suggests, the doctor decides. The engineer builds the system so that responsibility is technically achievable: transparency, confidence calibration, audit trail, de-identification, post-market monitoring. The specific three observations for the checklist piggy bank — on the slide after next."

[Move to s27.]

### [s27 · 1.5 min] — Closing: the doctor decides

[On the slide — a stock photo of a doctor + patient + the closing phrase.]

"If we fit the whole lecture into a single phrase — it sounds like this.

[slowly, with emphasis]

**The doctor makes the diagnosis. The AI suggests. The engineer makes it so that the doctor can truly decide.**

This is a callback to the central question of the lecture. Which AI promises in medicine came true and who is accountable. Diagnostics came true. Drug discovery came true partly. Accountability is on the doctor. The engineer is the one who provides the technical conditions for that accountability.

And this phrase prepares us for the final Lecture 17, "Systematization of knowledge and skills," where we'll assemble your personal checklist for responsible AI use. Today's observations are raw material for the draft. The finale — in Lecture 17."

[Move to s28.]

### [s28 · 1.5 min] — What's next

[On the slide — a mini course-map + a pointer to the final Lecture 17.]

"What's next. Medicine is the fourth industry lecture of the course. The industry tour continues — other industries, where the stakes are different: not a patient, but equipment, a harvest, infrastructure. But many of the methodological principles of this lecture carry over.

And most importantly — the three observations of this lecture. Transparency plus calibration. The validation set covers the deployment population. Audit trail plus post-market monitoring. **This is the entry into the personal-checklist piggy bank.** The finale — in Lecture 17, "Systematization of knowledge and skills," where we assemble the checklist from all the industry cases of the course."

[Move to s29.]

### [s29 · 1.5 min] — Q&A

[On the slide — a large Q&A + backup prompts.]

"Time for questions. What would you like to dig into deeper?

[pause, waiting for hands]

[Backup topics, if there are no questions — on the slide. I'm ready to discuss them on request.]

[pause]

Thank you for your attention."

[Closing.]

---

## Reserve (7 min)

- Additional questions from the audience.
- Backup for technical failures at the start (s01 Chester demo crashed).
- Deeper on the topic that resonated: if bias — then it's a cross-cutting theme of the subsequent industry lectures with systematization in the final Lecture 17; if drug discovery — the Recursion/Exscientia merger and the industrial economics of AI biotech; if regulation — the EU AI Act timeline in detail.
- Contact for subject-matter questions — `levko.maxim@gmail.com` or via the course staros.

---

**Timing summary (planning).**

- Active speech: 68.6 minutes.
- Reserve: 6.4 minutes.
- Total: 75 minutes.

**The lecture's goals are met in the speech.** LO1 — classification of the four types of AI applications (s06) with examples. LO2 — assessment through the clinical data of MASAI, Goh, Liu (s11) and the operational mosmed.ai (s12). LO3 — the ethical dilemma of accountability through the 4-actor framework (s24). LO8 — three principles as input for the final checklist of Lecture 17 (s26, s28), framed as raw material for the draft, not the finale.

**Cross-references from the chapter (synchronized with the canon of course-plan.md).** Lec 1 callback — YOLO in s01, the frame "where AI works" in s05/s27, the 2024 Nobel in s16. The final synthesis of Lecture 17 — LO8 input in s19/s24/s26/s27/s28; the entry into the personal-checklist piggy bank in s28.
