---
lecture: 5
title: "Lecture 5. AI in the Financial Sector and Retail"
length_words: ~5800
length_min: 75
status: finalized
version: v2
derived_from: "chapter v2 finalized (3 части, ~22650 слов) + deck v2 (33 слайда LOCKED: s01–s32 + s04a) + plan v2-final (USER GATE 0)"
slides_covered: [s01, s02, s03, s04, s04a, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32]
issue: 100
changelog:
  - "v1 (2026-05-17): первый draft Phase 9 — устная развёртка chapter v2 по 33 слайдам deck v2. ЦВ символьно из §0.3/s04; 5 точек возврата (s09/s14/s18/s23/s28); failure-нить Zillow→fraud-FP→Apple Card→Air Canada/Klarna→Wendy's, Knight = callback; 5 divider bridge phrases; pre-flight verify-day-of по cbr/Сбер/X5/vendor. (Самооценка v1 ОШИБОЧНО заявляла «все 33 ≤95 / max s28=94.7 PROVEN PASS» — скрипт v1 использовал non-greedy `«…»` извлечение, обрывавшее многоабзацные блоки и занижавшее WPM. Реальные v1-числа были выше; см. v2.)"
  - "v2 (2026-05-17, Phase 11 единая ревизия по 3 отчётам Phase 10): [P1-1 methodology] WPM-trim 6 фрагментов, которые по корректной методике (greedy, многоабзацные блоки целиком) превышали 95: s28 (Phase10-методика 100.3), s29 (98.0), s32 (97.3), s09 (96.0), s23 (96.0), s14 (95.7). Срезан только filler/упрощены предложения; критерии, 5 точек возврата, альтернативы, аналогии, Knight/Opendoor-callback'и НЕ тронуты. Пост-trim (официальная методика greedy-strip-cue): ВСЕ 33 фрагмента ≤95, max = s28 91.3 WPM (strict keep-cue max = s32 94.7). [P1-2] секция самооценки переписана честно — без «PROVEN PASS», реальные пофрагментные числа. [P2 fact] s17 «с марта 2024»→«в феврале–марте 2024 года» (паритет с chapter §3.2). [P2 meth] «мы с вами» честно = 8 (не 10); Σ slide-duration = 69.0 мин (per-slide), ≈70 по deck-totals, активный темп + Q&A-буфер = 75 мин. ЦВ s04 без изменений (устная запятая-нормализация, лексемы/порядок идентичны §0.3 — consistency D1 = опционально, оставлено как есть)."
---

# Lecturer's Speech · Lecture 5 "AI in the Financial Sector and Retail"

**Duration:** 75 min (Σ per-slide ≈ 69 min active + ~6 Q&A buffer; ≈70 by deck totals).
**Version:** v2 (Phase 11 revision based on 3 Phase 10 reports; status=draft, finalized by the orchestrator after GATE C).
**Source of truth:** chapter v2 finalized. This is an oral unfolding, not a reading of the chapter and not speaker notes.

## Preparation before the lecture

- Check the projector and slide order: 33 slides. Dividers — s04a / s10 / s15 / s20 / s25. These are the oral cue points for "moving on to section N of five."
- `[VERIFY-DAY-OF]` Open cbr.ru, find the Consultation Paper "AI Application in the Financial Market: Current Status" (`Consultation_Paper_20112025.pdf`). Verify the oral phrasings of s12 (anti-fraud is widely applied), s17 (scoring autonomy at SIB ≈100%, over 80% offer opt-out to a human). If the Central Bank has released a new edition — update the phrasing orally, do not change the direction. On the visible layer — only "per Bank of Russia materials," no bare number without attribution.
- `[VERIFY-DAY-OF]` Sber: check TAdviser/Interfax for fresh operational numbers — ~100% of retail decisions by AI, up to 5000 parameters, +350 billion ₽/2023. These are the bank's claims, February–March 2024. Phrase as "per the bank's claims"; update the number orally if there is a newer one.
- `[VERIFY-DAY-OF]` X5: check TAdviser for the status of demand forecasting — >70% accuracy, +5 billion ₽, −2% write-offs. Magnit F&R: a pilot after the departure of SAP/Blue Yonder, status 2025–2026. Phrase as claimed by the company.
- `[FACT-CHECK]` Vendor numbers for s12: Stripe Radar fraud reduction ~32% while approving >99% (stripe.com/radar); JPMorgan −30% false positives; Visa prevented ~$40 billion in FY2023 (≈80 million transactions, per Reuters/CNBC reports, July 2024). These are vendor claims — deliver them with attribution, not as an independent fact.
- `[FACT-CHECK]` s21: T-Bank chatbot >40% of inquiries; ~70% of banks planned voice by 2025 (TAdviser, 2025). Do NOT deliver the figure ">90% of banks' inquiries" as a fact — only as a teaching example of base substitution (class 5).
- `[FACT-CHECK]` s23: Klarna ~$40 million savings, two-thirds of inquiries, −resolution time from ~11 to <2 min — claimed by the company in 2024; the rollback to humans and the CEO's words — in indirect speech (Bloomberg/Entrepreneur/CX Dive, 2025), without verbatim quotes.
- `[FACT-CHECK]` s27: Amazon ~35% / Netflix ~75% — a historical estimate of a single origin (McKinsey ~2013), NOT a fresh headline. Deliver as "a historically cited estimate."
- `[FACT-CHECK]` s31: Just Walk Out relied on over 1000 reviewers in India (CNBC/Axios, April 2024); Amazon disputed the interpretation of the scale — name both sides.
- Run through aloud with a stopwatch the dense fragments — s11, s13, s14, s16, s22, s23, s26, s27, s28, s29. If the time-box is exceeded, remove one sentence of explanation, do NOT speed up speech and do NOT cut the return points, criteria, and alternatives.
- Clock: 5 return points of the central question — s09, s14, s18, s23, s28. If falling behind — cut explanations, not the return points.
- Note the interactives: s01 (open question, 30 sec), s09 (pause-think, 30 sec), s14 (poll, 20 sec), s23 (pause-think, 30 sec), s28 (pause-think, 30 sec).

---

## [s01 · 3 min] — Hook: the collapse of Zillow

"Let's begin not with excitement and not with a warning, but with one date and one number.

[lower voice] November 2021. Zillow — the largest real estate listings platform in the US — is shutting down an entire line of business. It was called Zillow Offers. The idea was beautiful. A computer model forecasts how much a particular house will cost. Based on the forecast, Zillow itself, automatically, buys that house, does cosmetic repairs, and resells it for more. This is called iBuying — the algorithmic purchasing of housing. Remove the human appraiser, scale to thousands of houses in dozens of cities at once.

[pause 2 sec] In practice, the model systematically overvalued houses. The company bought at higher prices than it could sell for. The outcome in three numbers. Inventory write-down — more than three hundred million dollars in a single quarter. Cumulative losses of the line — an estimated half a billion and above. About twenty-five percent of the staff was laid off, around two thousand people. The stock fell by about a quarter in the days after the announcement.

[pause] An entire line of a large public company shut down because of the errors of a single predictive model.

And here let's ask together the question we will be answering the whole lecture. What type of AI was this — and why did an ordinary model error turn into a loss of business rather than a minor inaccuracy? Let me say right away: this was not ChatGPT. Not "artificial intelligence that can do everything." This was a predictive model estimating a number — a price — from tabular and geographic data. A language model was not applied here and could not be.

[address the room] Thirty seconds, think to yourselves. Here is a model error. When does it cost near zero, and when — half a billion dollars? What distinguishes one case from the other? [pause 30 sec]

Hold your answer in your head. We will return to Zillow in detail — and check whether it matched."

[Transition to s02.]

---

## [s02 · 0.5 min] — Cover and map

"Lecture five. AI in the financial sector and retail. This is the course's second industry topic. In Lecture 4 we took software development — one type of AI, but in depth. Today — a palette of types. Seven blocks on the map below: discovery, forecasting, anomalies, scoring, LLM, recommendations, and assembly into an apparatus."

[Transition to s03.]

---

## [s03 · 2 min] — KEYSTONE: the palette of five types

"Remember this picture — it holds the whole lecture together.

In Lecture 4, in software development, we essentially examined one type of AI — a generative coder model — but in depth, along the ladder of autonomy. In finance and retail the picture is different. Here a whole palette of different types of AI works for different tasks, and most of the value comes not from a language model at all.

Here are the five types we will go through. Demand forecasting — that's one. Fraud detection — that's two. Credit scoring — that's three. Language assistants in support — that's four. Recommendations and pricing — that's five. And as a sixth layer, a cross-cutting illustration, computer vision will run through — the cashierless checkout, biometrics at the bank entrance.

[pause] These are structurally different types of AI. And applying a language model everywhere would be an engineering error. Remember the phrase, it runs through the whole lecture: the LLM is not a universal hammer.

And one more honest caveat. Four concepts we will be introducing right today, from scratch: type I and type II errors, the confusion matrix, the mechanism of proxy bias, and distribution shift. It's normal that they're new — we'll break each one down in plain terms when we get there."

[Transition to s04.]

---

## [s04 · 2.5 min] — The central question and the unified pattern

"Here is the central question of the whole lecture. Write it down — we will return to it five times, at the end of each section.

[lower voice, read slowly] Finance and retail are the industries of maximum AI adoption. For which task — which type of AI, why exactly it and not an LLM everywhere, and where does this type break?

[pause 2 sec] Note: the question has two halves. The first — "which type and why exactly it." The second — "where it breaks." Both are mandatory, and the second is more important.

To examine the five types uniformly, we will take one frame — a unified card pattern. Five steps. Step one — what the task is. Step two — which type of AI and why exactly it, and not a language model. Step three — a real example, ours and the world's. Step four — where it breaks, a documented failure. Step five — the alternative and the criterion: under what condition this type is inapplicable.

An important caveat. This "card pattern" is not an industry standard and not a term from a textbook. It's a way to organize the material, our working construct for the lecture — like the ladder of autonomy last time. You are not required to understand everything at once. Each type goes by the same scheme, and by the end the scheme will become your tool of choice."

[Transition to s04a.]

---

## [s04a · 0.3 min] — Divider: Section 1

"**Section one of five.** Time series forecasting. Let's begin with the most widespread task of retail — and right away with a type of AI that is NOT a language model."

[Transition to s05.]

---

## [s05 · 1.5 min] — Series forecasting: why not an LLM

"Time series forecasting is the prediction of future values of a number that is measured regularly over time. How much milk will be bought next Tuesday. What the cash inflow will be next month. The key word is series: a sequence of numbers over time that has trend, seasonality, and noise.

The type of AI — classical statistics and tabular learning: the ARIMA family, gradient boosting. Not a generative model and not an LLM.

[pause] Why not an LLM? A language model predicts the next token of text. Series forecasting is the next number in a sequence with trend and seasonality. A language model has no internal notion of "sales seasonality" — it has seen texts about sales, not your series. Remember the intuition: for a series of numbers over time you need a tool that can handle a series of numbers over time. The right type of AI is determined by the structure of the task, not by the trendiness of the tool."

[Transition to s06.]

---

## [s06 · 2.5 min] — The forecasting task: the criterion in full

"In retail, demand forecasting is the foundation of the entire operational chain: how much to order, how much to keep on the shelf, when to launch a promotion. An error in one direction — an empty shelf and a lost sale. In the other — an overflowing warehouse and the write-off of expired goods. In finance the analogue is forecasting cash inflow and forecasting customer churn.

It is important for us to understand the selection criterion in full — three arguments.

First — the structure of the data. These are tabular series: date, product, quantity, price, features. Models for series are designed to extract trend and seasonality. To turn a series into text for a language model means losing exactly the structure that must be used.

Second — measurability. A forecast needs a numerical error metric and a confidence interval, because the purchasing decision is built on these numbers. Classical models provide this out of the box. A language model does not.

Third — what will break. Take an LLM — and you get a plausible number without justified uncertainty. The purchasing decision still has to be made, and the cost of a systematic error is multiplied by volume. Remember the mechanism — it is exactly what ruined Zillow.

And the cross-cutting theme — data security. If the data contains citizens' personal data — the personal data law applies to it. Sending such series to a public cloud is both the wrong type of AI and a risk of violating localization. The right type here is also safer: a tabular model is deployed on your own infrastructure."

[Transition to s07.]

---

## [s07 · 2.5 min] — Example: X5 and Magnit

"A real example, our country. X5 — that's "Pyaterochka," "Perekrestok" — has been developing its own demand-forecasting algorithms since 2019. According to the company, forecast accuracy exceeds seventy percent. By the end of 2023 ML tools brought, per the company's claim, about five billion rubles of additional revenue and reduced write-offs of expired goods by about two percent.

Why does this matter to an engineer in essence? A forecast is not an end in itself. It is connected to the decision about purchasing and restocking the shelf. Accuracy converts directly into money: fewer write-offs, fewer lost sales.

[pause] The second example is especially instructive. Magnit (a large Russian grocery-retail chain) until 2022 used the forecasting-and-logistics systems of foreign vendors — of the SAP, Blue Yonder class. After they left the market, the company is building its own demand-forecasting and auto-ordering system. The pilot started at a distribution center.

The conclusion for us: the departure of foreign vendors made import substitution of forecasting systems not a theoretical but a direct engineering task of our industry. This is the context in which you will work. And note: neither X5 nor Magnit solves this task with a language model. They build specialized forecasting systems, because the type of AI is dictated by the task."

[Transition to s08.]

---

## [s08 · 1.5 min] — How it works: the merchandiser

"Let's look at the mechanics in plain terms, without formulas.

Imagine a sales chart for one product over two years. The eye almost immediately sees three things. An upward slope — the trend. A regular comb, where every Saturday there's a peak and a hump toward December — seasonality. A small trembling around it — noise. The model does the same numerically: it decomposes the history into trend, seasonality, and noise and extends the regularity into the future.

An analogy, remember it. A forecasting model is like an experienced merchandiser who, looking at the history, says: "toward the weekend take more, before New Year — much more." Only for millions of "store and product" pairs at once.

[lower voice] And here a vulnerability is built in. A forecast extends the patterns of the past. As long as tomorrow resembles yesterday — it works beautifully. But if the world changes qualitatively, the model confidently extrapolates patterns that no longer exist. It doesn't understand that the world has changed. Remember — this is the key to the next slide."

[Transition to s09.]

---

## [s09 · 2 min] — The Zillow failure: return point 1

"The central question returns for the first time. We unpack Zillow.

The model forecast the price of a house, and per the forecast Zillow automatically bought up housing. In 2020–2021 the market went through a pandemic shock. The model, trained on a stable market, systematically overvalued. Half a billion in losses.

Let's introduce a term from scratch. **Distribution shift** — when the data in reality stops resembling the training data. In one phrase: the model learned on one world, works in another.

[pause] But shift by itself does not ruin you — models drift constantly. What ruined you was what the output is connected to. The key concept: **asymmetry of the cost of error**. The same error in a recommendation costs near zero; in the auto-purchase of a house — tens of thousands, irreversible.

[lower voice] Callback. Knight Capital in 2012 lost four hundred forty million in forty-five minutes — automation placed orders without control. An ordinary algorithm, not ML. The class of error is the same: automation of the irreversible without a kill switch.

The lesson we take away. The type of AI was chosen correctly — a forecast is a forecast. The error was the decision about where to connect the output: irreversible, automatically, without a switch. The competitor Opendoor survived the same period on the same type — thanks to conservative wrapping. The same AI, different judgment — bankruptcy or survival.

[address the room] Thirty seconds to yourselves: where else is an irreversible auto-action on a forecast dangerous? [pause 30 sec]"

[Transition to s10.]

---

## [s10 · 0.3 min] — Divider: Section 2

"**Section two of five.** Anomaly detection: fraud and anti-money-laundering. The forecast was about the future. Now — about the present: catch the anomaly in milliseconds, while the payment has not yet gone through."

[Transition to s11.]

---

## [s11 · 3 min] — The fraud task and why anomaly detection

"The task: detect a fraudulent transaction in real time. A stolen card, an atypical payment — in a stream where the overwhelming majority of operations are honest, and the share of fraud is extremely small.

The type of AI — anomaly detection. The model builds a representation of the customer's normal behavior: how they usually pay — amounts, geography, time, merchants — and signals deviations. This is not series forecasting: we are not predicting a future value. And it's not generation: we produce nothing. This is calibration of the boundary "normal or anomalous."

[pause] Let's look at why exactly this type, and not others — this is an important fork.

Why not ordinary classification "fraud or not fraud" on labeled examples? Because fraud is by definition rare and constantly changes form. There are few labeled examples, and they become obsolete as soon as a fraudster invents a new scheme. Learning "what fraud looks like" is fragile, because fraud is a moving target. Anomaly detection flips the task: learn not "what fraud looks like" but "what this customer's normal looks like" — there is a lot of data, all of their honest history — and catch deviations.

Why not a language model? A transaction is a structured record: amount, time, geo, merchant. Not text. The task is geometric — how far a point is from the cloud of normal. Not linguistic.

An analogy, remember it. Imagine a cloud of points: the customer's ordinary transactions lie clustered together. The model outlines this cloud. An operation that fell far outside the edge — a payment in another country for an atypical amount at four in the morning — is a candidate for an anomaly. The model doesn't know that it's fraud. It knows that it doesn't resemble the norm, and it raises a flag.

And in one line — anti-money-laundering, AML. This is a set of regulatory requirements to identify suspicious schemes. From the point of view of the type of AI, this is a subset of the same anomaly-detection task, not a separate type. But part of the AML logic — hard legislative thresholds, and they are implemented with deterministic rules, not a probabilistic model. Why — we'll see further on."

[Transition to s12.]

---

## [s12 · 2 min] — Examples: Stripe, JPMorgan, Visa, Russia

"Real examples. Stripe Radar — the payment platform's anti-fraud — according to the company reduces fraud on average by about thirty-two percent, while approving more than ninety-nine percent of honest operations. JPMorgan reports a reduction of false positives by about thirty percent. Visa reported preventing on the order of forty billion dollars of fraudulent operations for fiscal year 2023 — almost twice as much as the year before.

In our country, anomaly detection in transactions is standard practice at large banks. Per Bank of Russia materials, traditional AI is widely applied in anti-fraud and risk management.

[pause] Note the phrasing of all these figures: "reduction of false positives." This is a hint. The key metric of anti-fraud is not "accuracy in general," but the ratio of two types of error. To understand why "accuracy of ninety-nine point nine" in anti-fraud is a deceptive and even dangerous number, we need the apparatus of the confusion matrix. Let's introduce it from scratch."

[Transition to s13.]

---

## [s13 · 3 min] — The confusion matrix from scratch

"This is the first appearance of the confusion matrix in the course. We introduce it from scratch, in plain terms.

Any system that divides events into two classes — "block or pass" — can err in two different ways, and they are not equivalent. Four cells.

True positive: it was fraud, the system caught it. Good. True negative: it was honest, the system passed it. Good.

Next, two errors. **False positive**: an honest operation is mistakenly flagged as fraud and blocked. This is a type I error — an honest customer suffered. **False negative**: fraud the system passed. This is a type II error — money went to the fraudster. These four cells are the confusion matrix.

[pause] Now — why "accuracy lies." Accuracy is the share of correct answers. Imagine a million transactions, a thousand of them fraud — one tenth of a percent. A model that does nothing and says "everything is honest" gives accuracy of ninety-nine point nine: it "guessed" almost a million honest ones, and a thousand fraud doesn't move the share.

[lower voice] That is, a useless model shows excellent accuracy. Remember: under strong class imbalance, accuracy measures the size of the larger class, not the ability to catch a rare important event.

From here the key idea — **cost-weighted evaluation**. The two errors are different not only in meaning but also in cost. The cost of missed fraud — the bank's loss. The cost of a blocked honest customer — a spoiled experience, in the worst case departure to a competitor. The correct formulation is not "maximize accuracy," but minimize the expected cost of errors, where each is weighted by its real cost.

And a forward-pointer: the formal apparatus — sensitivity, specificity — we will build in Lecture 7, on a medical example. Today the intuition is enough: two types of error, different costs, accuracy under imbalance is deceptive."

[Transition to s14.]

---

## [s14 · 3 min] — The false-positives failure: return point 2

"The central question returns for the second time. The failure side is more important than the advertising figures.

The optimistic picture: false positives at fractions of a percent, approval above ninety-nine. Seems excellent. But multiply by scale. Billions of transactions a year — even half a percent is tens of millions of blocked honest operations. Behind each one is a specific person.

Why can't this be removed by a setting? The trade-off works — **precision versus recall**. Let's separate two ideas. Cost evaluation — at what cost to choose the trigger point. The precision-recall trade-off — the trade-off itself is unavoidable. The more suspicious the model — the more blocked honest ones. The more tolerant — the more missed fraud. A better model shifts the curve, but does not cancel the choice of a point on it.

[pause] Specifics. Two false positives. The first: a block on a five-dollar coffee. The customer repeated with another card, forgot about it an hour later. Cost near zero, reversible.

[lower voice] The second: a block on a five-thousand payment for urgent medicine in a foreign country — "atypical amount plus atypical geolocation," exactly the pattern the model was trained to treat as suspicious. The same class of error — but the cost is orders of magnitude higher, and the case is irreversible in its consequences.

The conclusion: "we reduced false positives by twenty-five percent" is a figure meaningless without context, it averages the trivial and the catastrophic case.

Callback to Knight: auto-blocking a large irreversible payment without a human — the same class of "automation of the irreversible without a gate."

The criterion. Hard auto-blocking — only for reversible or small operations. For large ones — not a flat refusal, but a soft request for confirmation: a 3-D Secure code, a call, plus a fast human unblocking channel. And hard AML thresholds are law, executed by a deterministic rules engine, not a probabilistic model.

[address the room] Twenty seconds to yourselves: block a five-thousand payment for treatment on an anomaly — your threshold? Block, soft request, pass with a flag? [pause 20 sec] This is the second return point: the type was chosen correctly, but which action to automate is a separate decision by the cost of the error."

[Transition to s15.]

---

## [s15 · 0.3 min] — Divider: Section 3

"**Section three of five.** Credit scoring. The anomaly was found. Now — the decision that changes the customer's life: grant a loan or refuse. And here a black box is fundamentally impossible."

[Transition to s16.]

---

## [s16 · 3 min] — Scoring: why not a neural network

"Credit scoring is the assessment of a borrower's creditworthiness. From data about the customer the system produces an assessment of default risk, and on its basis — the decision about issuance, limit, rate.

The type of AI in the industry — classical tabular ML: gradient boosting, logistic regression, scorecards. Deliberately not a neural network and not an LLM. The reason is not that "neural networks compute worse." It is important for us to understand the criterion — four arguments.

The first, load-bearing. Explainability is a regulatory requirement, not a wish. A customer who was refused is entitled by law to an understandable explanation — reason codes: "high debt load," "short history." The answer "the algorithm decided so" is legally inadmissible. A model from which a reason cannot be extracted is inapplicable here in principle — not "less convenient," but inapplicable.

The second — the data is tabular. On tabular data, boosting is competitive or stronger, at incomparably greater intelligibility.

The third — auditing is more important than one percent of accuracy. The regulator must be able to reproduce the decision and check the absence of discrimination.

The fourth — what breaks with a black box. Can't explain — a violation. Can't audit for bias — a crisis, exactly the next slide. Not stably reproducible — nothing to defend yourself with before the regulator.

[pause] An analogy, remember it. An interpretable model is a credit inspector who doesn't just say "no," but shows the calculation line by line. A black box is an inspector who says "no" and refuses to explain. From boosting, by a standard method — it's called SHAP — the same line-by-line answer is extracted: which feature shifted the decision by how much.

[lower voice] And honestly about the reflex "new — means neural network, means better." In scoring this is a direct engineering error, structurally. Here explainability is not a bonus, but a condition of legality. An engineer who chose a language model for scoring made the same categorical error as one who chose an LLM for series forecasting."

[Transition to s17.]

---

## [s17 · 2 min] — Example: Sber

"A real example, our country. Sberbank (largest Russian bank, now a tech-and-AI conglomerate), per the bank's claims, in February–March 2024 transitioned to accepting retail credit decisions almost entirely to AI. The scoring model takes into account up to five thousand customer parameters. The additional effect from AI across all directions the bank estimated at about three hundred fifty billion rubles for 2023.

Per Bank of Russia materials, the degree of AI autonomy in retail scoring at systemically important banks approaches one hundred percent. And an important detail for the cross-cutting theme "human versus AI": per the same document, over eighty percent of financial organizations that use AI on an ongoing basis give the customer the option to decline AI processing and switch to an employee.

[pause] Here it is important for us to understand this. "The decision is made by AI one hundred percent" does not mean "a black-box neural network decides the customer's fate without control." It means high automation of the pipeline on interpretable models with reason codes, under the regulator's oversight, with the customer's preserved right to a human. The type of AI is tabular ML, chosen precisely because of explainability, and not in spite of it."

[Transition to s18.]

---

## [s18 · 3 min] — The Apple Card failure and proxy bias: return point 3

"The central question returns for the third time. The case — Apple Card and Goldman Sachs, 2019.

The precise facts cannot be simplified. The developer David Hansson published a viral thread: he was approved for a limit about twenty times higher than his wife's — with a joint declaration and a higher rating for the spouse. Similar complaints, including Steve Wozniak. The New York State regulator opened an investigation.

[lower voice] The critical nuance. In March 2021 the regulator, after analyzing about four hundred thousand applicants, found no violation of fair-lending laws. To assert "Apple Card provenly discriminated against women" is factually incorrect. But the regulator pointed to opacity: customers could not get an explanation, and "the algorithm decided so" undermined trust.

That is, the failure is not proven discrimination, but a crisis due to inexplicability. Even a formally lawful model without reason codes creates a crisis. The precision of this formulation is itself a lesson in fact-checking.

[pause] Let's introduce from scratch a mechanism dangerous even without malicious intent — **proxy bias**. The engineer deliberately does not feed in sex and race. It seems discrimination is excluded. But there remain features correlated with the forbidden ones: postal code, spending structure, type of employment. The model, optimizing accuracy, indirectly reconstructs the forbidden feature through these proxies — and treats groups differently, formally without seeing them.

An analogy. You removed the "sex" field, but left a dozen fields by whose combination sex is guessed almost unambiguously. The model does exactly that, without intent. Therefore "we don't use protected features" is not proof. The only proof is a direct audit of outcomes by protected groups. Forward-pointer: the canonical analysis — the Obermeyer case — we will see in Lecture 7.

The criterion. A regulated credit decision requires three things simultaneously: reason codes; a human appeal channel for the disputed; an audit of outcomes for bias before production, not after a scandal. Without any of the three, scoring cannot be applied. This is the third return point: the type was chosen correctly, but without explainability and auditing it still produces a crisis."

[Transition to s19.]

---

## [s19 · 2 min] — The criterion: automation without a gate

"Let's assemble a cross-cutting criterion from three sections. We have seen one and the same class of error in three types of AI. Zillow — a forecast connected to automatic irreversible purchasing. Anti-fraud — an anomaly connected to automatic irreversible blocking. Knight Capital — a deterministic algorithm, automatic irreversible orders.

Let's formulate the generalization as a conclusion-criterion. [lower voice] Automation executing irreversible financial actions in an open loop without a kill switch, without limits, without verified deployment — turns an ordinary model error into the speed of ruin.

[pause] What this means for scoring specifically. In our country scoring is automated almost one hundred percent — which means the criterion applies to it acutely. "One hundred percent of decisions are made by AI" is acceptable only within the wrapping: reason codes on every decision, a preserved human channel, an audit of outcomes on a regular basis, drift monitoring, regulatory oversight. Remove the wrapping — and one hundred percent of automation turns from efficiency into Apple Card at the scale of an entire bank.

Remember the formulation: high autonomy is neither a goal nor an evil in itself. The goal is autonomy around which stand paid-for gates, proportional to the cost of the error and the irreversibility of the action."

[Transition to s20.]

---

## [s20 · 0.3 min] — Divider: Section 4

"**Section four of five.** Language models in finance. Until now — deliberately NOT an LLM. Now the LLM, and right away about its limits."

[Transition to s21.]

---

## [s21 · 2 min] — Where the LLM is appropriate

"A task where a language model is appropriate in a bank: customer support, a voice assistant, help for an employee — summarize an inquiry, explain a product in simple language. Text-and-dialogue tasks — exactly what the LLM was designed for, unlike the first three sections.

Scale. Per verified data, T-Bank's (a large Russian digital bank) chatbot processes over forty percent of inquiries. About seventy percent of banks planned voice assistants by 2025.

[lower voice] An important caveat, and also an illustration of the topic. One encounters the phrasing "voice assistants process more than ninety percent of banks' inquiries." A figure around ninety exists somewhere — but it refers to the share of calls in one bank's call center, not to banks' inquiries in general. This is a classic base substitution. Therefore we use only the verified figure. To build a claim on a substituted base would be to violate exactly what the lecture teaches.

[pause] And symmetry. The impression may remain "the LLM is inappropriate everywhere" — this is incorrect. In forecasting, anomalies, scoring the LLM is the wrong type, because the tasks are not textual. In support — the right one, because the task is text-and-dialogue. "A different task — a different type of AI" means not "the LLM is bad," but "the LLM is good exactly where the task is text-and-dialogue.""

[Transition to s22.]

---

## [s22 · 3 min] — The fact-checking and grounding pattern

"Here — the cross-cutting pattern of the whole lecture: fact-checking. The criterion in full "when the LLM is NOT the source of truth" — three arguments and an alternative.

The thesis. In finance, a language model's answer about rates, terms, the customer's rights must be **grounded** — rely on a verifiable primary source: the tariff from the system, the text of the contract. The LLM here is not the source of truth, but an interface to it.

First — the hallucination mechanism. A language model generates a plausible continuation, not extracts a verified fact. Plausible does not equal true. Ask for the exact rate — it will produce a confidently sounding but incorrect number.

Second — the cost of error in finance is legal. An incorrect rate is potential misleading and direct harm to the customer, for which the organization is responsible.

Third — what will break. Free generation of answers about regulated facts is a scalable generator of disinformation with the bank's legal liability for every answer.

The alternative. For fixed facts, the answer is built by deterministic retrieval from the system. A mini-reminder of Lecture 3 — RAG, generation grounded in a verifiable fragment. The LLM phrases the found information in language, but does not invent the number itself.

[pause] An analogy for grounding, remember it. Without grounding the model answers like a student on an exam who doesn't remember the figure but doesn't want to stay silent: plausibly and in a confident tone. With grounding the same student first opens the reference book, reads the exact value, and only then phrases it in their own words.

Five classes of AI errors. First — hallucination of a fact: a number without a source reference. Second — outdated data: a figure without a date. Third — proxy bias in the output. Fourth — deception by metric: "accuracy ninety-nine" without a base. Fifth — base substitution: a loud share without the exact formulation "the share of what out of what" — exactly our ninety percent.

The boundary with the seminar. In the lecture — recognize the class and name the principle of verification. To independently verify five claims against Bank of Russia primary sources — that is Seminar 5, the Apply level. The lecture prepares the skill, the seminar brings it to practice."

[Transition to s23.]

---

## [s23 · 3 min] — Air Canada and Klarna: return point 4

"The central question returns for the fourth time — with two cases.

Case one — Air Canada, a callback to Lecture 3, not a duplicate. The airline's chatbot told a passenger a nonexistent refund policy. The passenger acted on this answer. In February 2024 a Canadian tribunal ruled: the company is responsible for the information from its chatbot, and ordered it to pay compensation. The class of error: hallucination of a financially significant fact equals the organization's legal liability. The transfer to a bank is direct: a chatbot that named an incorrect rate creates the same liability.

[pause] Case two — Klarna, the arc from 2023 to 2025. The fintech deployed a language support assistant. It closed about two-thirds of inquiries, cut resolution time from about eleven minutes to less than two. The claimed savings — about forty million dollars a year. It was presented as "AI replaces support."

[lower voice] The denouement. By mid-2025 Klarna recorded a drop in customer satisfaction and returned to hiring people. Per media reports, the CEO admitted: the bet on cost reduction gave lower quality.

Why this is not "AI is bad," but subtler. The assistant worked — the savings are real. The failure is in a categorical error: the task "answer inquiries" was confused with the system "customer service." Service is also the rare, emotionally charged, disputed cases where trust is at stake. There are few of them, but exactly by them the customer decides — to stay or to leave. Full replacement optimized the average cost of a contact and crashed the heavy tail. The same class as cost evaluation from the fraud section.

The criterion. Hallucination of a financial fact equals legal liability — which means regulated facts must be grounded. Full auto-replacement of support is unstable — the correct role of the LLM is augmentation, not replacement: AI on the routine plus guaranteed human escalation on a dispute.

[address the room] Thirty seconds to yourselves: a bank's chatbot named a rate to you — how do you RECOGNIZE the risk of hallucination, without checking the rate itself? [pause 30 sec] This is the fourth return point: the LLM is the right type for dialogue, but in a regulated industry it must be grounded and have a human exit."

[Transition to s24.]

---

## [s24 · 2 min] — Pivot: what surrounds any type of AI

"Let's make a turn — not a summary, but a bridge.

We have gone through four different types of AI: forecasting, anomalies, scoring, dialogue LLM. In each the failure had the same form. The type was chosen correctly for the structure of the task. What broke was not in the type, but in the wrapping: on the irreversible action at Zillow, on the large block at fraud, on the regulated decision at Apple Card, on the binding fact at Air Canada.

[lower voice] From here a two-level conclusion, remember it. The first half of the question — "which type and why" — is resolved by the structure of the task, most often unambiguously. The second — "what surrounds the AI at the cost of error" — is designed separately. The correct choice of type is necessary, but not sufficient. An engineer who has absorbed only the first half will correctly name the type — and still build Zillow-class systems.

[pause] And the transition to the last type. Until now all types touched actions with a high cost of error: money, credit, a legal fact. The last one — recommendations and pricing — seems the most harmless. Well, recommended the wrong movie. That is exactly why it is more dangerous: the low visible cost lulls you, and the failure is quiet — the system reports success exactly when it destroys what did not get into the metric."

[Transition to s25.]

---

## [s25 · 0.3 min] — Divider: Section 5

"**Section five of five**, the last substantive one. Recommendations and dynamic pricing. The most harmless type by visible cost of error — and with the subtlest pathologies."

[Transition to s26.]

---

## [s26 · 3 min] — Collaborative and content-based from scratch

"The task: personalization — "what else to buy or watch," ranking the feed. The type of AI — recommender systems. You are seeing this concept for the first time, so we'll unfold two basic approaches in plain terms.

Approach one — **collaborative filtering**. The idea in one phrase: "people similar to you in behavior bought X — which means you'll probably like it too." The system builds a large "user and product" table — who bought what — and looks for similar rows. Importantly: it doesn't know what the product is, only who interacted with what. The strength — it catches unexpected connections: "buyers of a drill often take exactly these gloves," the system sees this even without knowing what a drill is. The weaknesses, let's name them right away: **cold start** — for a new product there is no history, nothing to recommend on; and **popularity bias** — the system tends to recommend what is already popular, because there is the most data on it.

[pause] Approach two — **content-based filtering**. The idea: "this product is similar by its features to what you already liked." The system uses the product's attributes — genre, brand, category, price — and recommends the similar. The strength: no cold-start problem for a new product, as soon as it has attributes. The weakness — **over-specialization**: the system locks the user into a narrow niche of "more of the same," not opening anything beyond the already known.

An analogy separating the two approaches. Collaborative — "ask people similar to you what they took." Content-based — "take another thing similar in description to your favorite." The first risks drowning you in the popular, the second — locking you in a niche. Remember what these approaches are and what each one's weakness is by name. The mechanism — why exactly these weaknesses grow from here — is on the next slide, on a concrete table."

[Transition to s27.]

---

## [s27 · 3 min] — Hybrid, filter bubble, dynamic pricing

"Approach three — **hybrid**. Most real industrial systems are a hybrid: collaborative plus content-based plus context — time, device, session history. Combined so that the strengths of one compensate for the weaknesses of the other. The content-based part closes cold start, the collaborative one breaks the lock-in in a niche. This is not a third separate algorithm, but an engineering composition of the first two.

[pause] Let's introduce from scratch two pathologies. The **filter bubble** — the effect where the system, optimizing relevance to already-revealed preferences, narrows the diversity of what the user sees. The mechanism: the model shows the similar, the user interacts with the similar, the model learns to show even more similar. This is not malicious intent, but a direct consequence of optimizing for short-term relevance.

**Dynamic pricing** — automatic adjustment of price to demand, time, the competitor, context. Technically — optimization of the objective function "revenue." Let's fix the engineering-ethical boundary right away: the perception of price fairness and regulatory constraints are constraints of the task, not optimizable variables. An attempt to optimize price "head-on," ignoring them, is the classic error of "proxy instead of goal," which the next slide will unpack.

[lower voice] And with the discipline of fact-checking — we just talked about it. It is widely cited that Amazon has about thirty-five percent of revenue from recommendations, Netflix about seventy-five percent of views. We present it correctly: these are historically cited classic estimates, tracing back to a single source around 2013, not fresh verified indicators. For Ozon and Wildberries the share could not be confirmed by a primary source, so the Amazon figure cannot be transferred here. The correct formulation: recommendations are a key driver of marketplace conversion, the companies do not disclose the exact share. This is a practical illustration: a modest attributed formulation instead of a beautiful but unverified transfer."

[Transition to s28.]

---

## [s28 · 3 min] — Wendy's and proxy≠goal: return point 5

"The central question returns for the fifth, last time. The failure of this type is subtler than the previous ones.

The root — **proxy instead of goal**. A recommender system optimizes what is measurable in the moment: clicks, view time, conversion. But this is a proxy — an indirect indicator, not the real goal: the long-term value and trust of the user. When the proxy diverges from the goal, the system honestly maximizes the proxy — and gets pathologies: the filter bubble, dark interface patterns, homogenization.

[pause] The case — Wendy's, February 2024. The fast-food chain announced on the order of twenty million dollars into digital menu boards with dynamic pricing. In the media this was interpreted as "the price rises during peak hours, like a taxi." A scandal flared up, a boycott on social media. Within a few days the company publicly rolled back the wording.

Why this is a clean illustration, and not "bad PR." Technically, surge pricing is a solvable optimization task. Set it up that way — and the optimizer will honestly solve it and lead to exactly what caused the boycott. The error is not in the model, but in the framing: "fairness" and "loyalty" were discarded because they are poorly measurable, while measurable revenue was in the function.

[lower voice] And the main thing. This is the same mechanism as the filter bubble: the proxy (a click, revenue per shift) diverges from the goal (long-term value, trust in the brand). The pathology does not look like a failure: the metric grows, the failure is visible only if you look at what did not get into the metric. For forecasting and scoring the failure is loud, for recommendations — quiet.

The criterion. A proxy metric does not equal the goal — which means it is mandatory to build in a deliberate share of unexpected recommendations, explainability, an audit for discrimination. And pricing policy is a human decision within a legal frame, not the output of an optimizer. Fairness and law are constraints, not variables.

[address the room] Thirty seconds to yourselves: where in a familiar service have you noticed a filter bubble or an unfair price — what there is the proxy, and what is the goal? [pause 30 sec] This is the fifth, closing return point, and here we see: even a harmless type of AI requires a human and a frame around it."

[Transition to s29.]

---

## [s29 · 3 min] — The "task × type of AI" matrix

"Section six, without a divider — the assembly. Let's assemble the five sections into one apparatus — the answer to the central question.

The matrix. The row — the task, the columns — the correct type, why exactly it, the typical failure. This is a compact packaging of five already-proven facts, not new material. By rows.

Demand, churn forecasting — the type of AI is time series forecasting. Why not an LLM: a series of numbers with a trend, not text, a calibrated error is needed. The typical failure — distribution shift on an irreversible auto-action, Zillow. The criterion — a human gate on the capital-heavy, a narrow segment, a kill switch.

Fraud in real time — anomaly detection plus a rules engine. Why not an LLM: the task is normal-deviation, not generation; the AML threshold is law. The failure — false positives at scale, accuracy lies under imbalance. The criterion — cost evaluation, a soft request for confirmation on the large.

Credit scoring — classical tabular ML. Why not a neural network: explainability is a regulatory requirement. The failure — proxy bias plus opacity, Apple Card. The criterion — reason codes, an appeal channel, an audit before production.

Support and explanation — a language model with grounding. Why exactly it: the task is text-and-dialogue. The failure — hallucination of a financial fact as legal liability, replacement does not equal augmentation. The criterion — grounding, verifiability, a path to a human.

Recommendations and pricing — a recommender system; the price — an optimizer within a frame. The failure — proxy does not equal goal, Wendy's. The criterion — diversification, auditing; the price — a human plus law.

[pause, lower voice] And the bottom row — deliberately. A deterministic, verifiable regulatory task — the hard AML threshold, a mandatory check. The right tool — ordinary code, a rules engine. NOT AI. Why: precision, repeatability, auditability are needed. Law does not equal probability. AI here doesn't "not hurt" — it would add nondeterminism and an error surface where precision and auditing are required. The matrix is not "choose a trendy model," but "name the type for the structure of the task, and sometimes the right type is not AI at all.""

[Transition to s30.]

---

## [s30 · 2 min] — When AI is not needed or is dangerous

"Let's assemble the cross-cutting criterion "when AI is not needed or is dangerous." This is not five different warnings, but one principle in five manifestations: the correct choice of type is necessary, but not sufficient; AI is dangerous where its output is connected to an action whose cost of error is not paid for by the wrapping.

An irreversible auto-action without a gate — Zillow, Knight. The solution: a human gate, a narrow segment, live monitoring.

A regulated decision without explainability — Apple Card. The solution: an explainable model, a human on escalation, an audit of outcomes.

A financial fact without grounding — Air Canada. The solution: grounding, verifiability, a path to a human.

Full replacement of people in service — Klarna. The solution: augmentation with guaranteed escalation.

Price discrimination without a legal frame — Wendy's. The solution: the price — a human within a legal frame, the optimizer only within the boundaries.

[lower voice] Note the main thing. In none of the five cases is the fix "a better model." In all — better judgment about what stands around the AI at the cost of error. This is the substantive answer to the central question: "where it breaks" — not in the type of AI, it was chosen correctly, but in the absence of wrapping proportional to the irreversibility and regulated nature of the action."

[Transition to s31.]

---

## [s31 · 3 min] — Security: FZ-152, PII, biometrics, hidden labor

"Data security in finance and retail is sharper than anywhere. Two blocks.

Block one — data and the law. Here financial data, personal data, and biometrics are processed. The personal data law requires localization — storage and processing of citizens' data on servers in the country, and biometrics — a separate, stricter regime. The practical conclusion: financial data, personal data, and biometrics cannot be sent to a public cloud LLM. A public cloud has three structural downsides that are not configurable: the data leaves the organization's perimeter; you don't control what the provider does with it; auditability falls. The selection criterion — by data sensitivity and regulatory regime, not by the power of the model.

[pause] Block two — computer vision, we go through it illustratively. KYC — "know your customer" — mandatory identification when onboarding a customer. In digital form it often includes **liveness** — a liveness check: that a real live person is in front of the camera, and not a photo, mask, or deepfake. This is biometrics — a strict regime.

[lower voice] The key principle of biometrics in a separate sentence. A biometric feature is irreversibly compromised upon leak. A password can be changed, a face and a fingerprint — cannot. The cost of error here is asymmetric in the same way as with the forecast in Zillow.

And another lesson — **hidden human labor**. Amazon Just Walk Out — cashierless stores on computer vision — in April 2024 was rolled out of a number of formats. According to reports, the autonomous checkout relied on over a thousand reviewers in India, post-processing problem transactions. Amazon itself disputed such an interpretation — the presence of two versions is itself an illustration of fact-checking: one event, two sides, a verifiable base is needed. The lesson: before automating vision, assess the real total cost and the hidden labor. "Fully autonomous" in marketing is a hypothesis for checking, not a fact. Forward-pointer: recognition errors across groups we will deepen in Lecture 7."

[Transition to s32.]

---

## [s32 · 1.5 min] — Checklist, bridge to Seminar 5, Q&A

"We fold the five sections into a checklist — before choosing AI. Eight questions on the screen: which type; why not an LLM; can it be done without AI; is the action reversible; how to verify a fact; is the decision regulated; who is responsible; is there PII or biometrics?

[pause] This apparatus is a lens for all the industry lectures ahead. The paired Seminar 5 brings the skill to practice: teams verify five claims about AI in banks against primary sources of the Bank of Russia and VCIOM (Russian state pollster / public-opinion research center). The boundary is strict: the lecture teaches to recognize the class and the principle, the seminar — to verify independently.

[lower voice] And the last thing. AI here gives enormous measurable value — X5, Sber, Stripe. And erroneous judgment costs half a billion or the trust of millions. Between excitement and denial stands the engineer who can say: which type, why it, where it breaks, and who is responsible. This skill, which we have assembled, does not become obsolete with the release of the next model.

[pause] Thank you. We have time for questions."

[Q&A — reserve ~5 min.]

---

## [Reserve · ~5 min] — Q&A and buffer

Backup answers (from the chapter's "Likely audience questions"):
- "If predictive models are so vulnerable to shift, maybe don't automate forecasting?" → Automation is necessary: millions of "store-product" pairs are impossible by hand, X5 gets a measurable effect. The Zillow lesson is not "don't forecast," but "don't connect to an irreversible action without a gate." The cost of error determines whether a human is needed.
- "Why can't you give an LLM a numerical series — models can compute, after all?" → To compute in text is not to be a predictive model of a series. Forecasting is extracting trend and seasonality with calibrated uncertainty. An LLM has no internal representation of a series as a series.
- "If NYDFS found no violation, why is Apple Card a failure?" → The failure is not proven discrimination, but a crisis due to opacity: "the algorithm decided so" triggered an investigation and reputational damage. The precision of the formulation is itself a lesson.
- "Klarna saved forty million — isn't that a success?" → A success on one metric, a failure on another (retention), and the company publicly rolled back. The lesson — "full replacement does not equal transformation," augmentation is stable.
- "Where is AI useful at all, it seems like nothing but failures?" → Useful and measurably so: X5 +5 billion ₽ and −2% write-offs; anti-fraud blocks billions while approving >99%; scoring almost 100% at the largest bank; LLM support saves on the routine; recommendations are a driver of conversion. There are many failures deliberately: judgment is taught by limits, not by excitement.
- Backup in case of a technical projector failure: lead by the structure "five types plus assembly"; all numbers are in this speech orally; the central question and the five return points hold the frame.

---

## Self-assessment (Phase 11, honest — for pre-gate, not part of what is spoken)

**Word count:** ~5900 words with cue markers; ~5700 stripped (frontmatter/pre-flight/self-assessment not counted). 4.5–6k. ✓

**Pacing / WPM (hard cap ≤95 per-fragment) — PASS after the Phase 11 trim, WITHOUT a false "PROVEN."** The method (correct): words in the spoken body of a fragment (`## [sNN]`→next `## [`), multi-paragraph `«…»` blocks in full (greedy, not non-greedy), minus `[cue]` insertions and guillemets, / `duration_min`. Correction of the false v1 self-assessment (methodology P1-2): v1 ERRONEOUSLY claimed "all 33 ≤95 / max s28=94.7 / PROVEN PASS" — the v1 script extracted `«…»` non-greedy and underestimated WPM; the real v1 numbers by the Phase 10 method were **>95 on 6 fragments**. v2 = a targeted trim of only these 6 (filler/simplification; criteria / 5 return points / alternatives / analogies / Knight-Opendoor NOT touched).

| Fragment | dur | Phase10-method (v1) | v2 strip-cue WPM | v2 strict keep-cue WPM |
|---|---|---|---|---|
| s28 | 3.0 | 100.3 | **91.3** | 94.3 |
| s29 | 3.0 | 98.0 | **86.0** | 87.0 |
| s32 | 1.5 | 97.3 | **88.7** | 94.7 |
| s09 | 2.0 | 96.0 | **90.0** | 94.5 |
| s23 | 3.0 | 96.0 | **90.3** | 93.3 |
| s14 | 3.0 | 95.7 | **86.7** | 89.7 |

**ALL 33 ≤95** by the official greedy-strip-cue method: max = **s28 91.3 WPM**. By the strictest keep-cue (cue brackets also counted as words, deliberately overestimates): max = **s32 94.7** — also ≤95. Average ~80 WPM. The trim hit filler/OUT; in-bucket fragments preserved failure+lesson+criterion+alternative. Σ slide-duration = 69.0 min (per-slide); ≈70 by deck totals; active + Q&A buffer = 75 min.

**The central question — lexemes and order identical to §0.3/s04 (consistency D1 = optional P2):** the central question on s04 is spoken with the same words and in the same order as chapter §0.3 / deck s04: "Finance and retail are the industries of maximum AI adoption. For which task — which type of AI, why exactly it and not an LLM everywhere, and where does this type break?". The only difference — punctuation for oral delivery: the written parenthesis `(and not an LLM everywhere)` → the oral comma insertion `, and not an LLM everywhere,`. The consistency-checker qualified this as correct oral normalization (NOT a central-question mismatch, not a REVISE trigger), the edit is optional — the chapter is not touched, the speech is left as is. ✓ (with P2 D1)

**Invariants (checked by the v2 script, intact after the trim):** 5 return points (s09/s14/s18/s23/s28, live language, without §); failure thread Zillow(s01→s09)→fraud-FP(s14)→Apple Card(s18)→Air Canada+Klarna(s23)→Wendy's(s28), Knight = callback (s09/s14/s19), Just Walk Out = s31; 7 analogies intact (merchandiser/cloud+outlier/inspector/the "sex" field/student-reference book/"ask the similar"/password≠face); 5 divider bridge phrases (s04a/s10/s15/s20/s25); forward-pointers to L7 (s13/s18/s31) + Seminar-5 = Apply (s22/s32); universality (without IU6); anti-hype (s32 "between excitement and denial"); strip in the body 0/0/0/0/0/0; 0 forbidden anglicisms; glossary lock observed; the RPD ">90%" — ONLY class-5 teaching (s21/s22); 33 fragments 1:1 with the slides, 0 orphan refs.

**Inclusive voice (honestly):** "we together" = **8** (NOT 10, as v1 erroneously claimed), distributed across 8 fragments of different sections (s03/s04/s09/s13/s18/s28/s31/s32). The markers were NOT added deliberately — the methodology-critic in Phase 10 independently confirmed the conversational/inclusive voice as PASS (53 stage cues, broad inclusive density ≈0.6/200 words). The edit is only the honest number.

## Residual risks for Phase 11.5 pre-gate

1. **WPM (methodology P1-1) — closed, but check with a stopwatch.** ALL 33 fragments ≤95 by both methods (official greedy-strip-cue max = s28 91.3; strictest keep-cue max = s32 94.7). The margin from the cap by the strictest keep-cue method is thin on s32 (94.7) and s09/s28 (94.3–94.5) — the pre-flight instructs the lecturer to run s11/s13/s14/s16/s22/s23/s26/s27/s28/s29 through with a stopwatch and, on a real overrun, remove one explanatory sentence, NOT cut a criterion/return point/alternative. The false v1 self-assessment ("PROVEN PASS / max 94.7") is corrected (P1-2): see the table above — no false PASS.
2. **strict-in (methodology, AI-Failure Rule) — PASS with margin, holistic.** The methodology-critic in Phase 10 by an independent recount by minutes: strict set 56.7%, extended 64.9% ≥ 30%, distributed across all 6 sections (S1 s05/s06/s08/s09 · S2 s11/s13/s14 · S3 s16/s18/s19 · S4 s22/s23/s24 · S5 s28 · S6 s29/s30/s31), not single-cluster. The Phase 11 trim hit only filler/OUT — spot-checked: s09/s14/s23/s28 preserved failure+lesson+criterion+alternative; s29 preserved all 6 matrix rows + the bottom "not AI"; s32 preserved the Seminar-5 boundary + anti-hype. L5 ∈ L4–L17 → owner waiver unavailable and unneeded.
3. **Fact-checker — APPROVE-CLEAN, 0 P0/P1.** All numbers = chapter v2 (Zillow $300M/quarter+$500M+/~2000/−25%; X5 >70%/+5 billion ₽/−2%; Sber ~100%/5000/+350 billion; Stripe ~32%/>99%; JPMorgan −30%; Visa ~$40 billion FY2023; Klarna ~$40M/2/3/−11→<2 min; Amazon ~35%/Netflix ~75% historical McKinsey ~2013; Just Walk Out >1000 + Amazon disputed). P2-1 closed: s17 "since March 2024" → "in February–March 2024" (parity with §3.2). The RPD ">90%" — ONLY class-5 teaching (s21/s22). verify-day-of items in pre-flight synchronized with deck-part2.
4. **Consistency — APPROVE-WITH-POLISH, 0 P0/P1.** One speech fragment per slide (33:33:33); the central question lexemes/order identical to §0.3 (D1 = optional oral punctuation, left as is per instruction); 5 return points, failure thread, Knight-callback discipline, forward-pointers, Seminar-5 Bloom boundary, glossary lock, 0 forbidden anglicisms in the body — all intact after the trim.

The content is committed by the orchestrator (Phase 11). status=draft remains — the orchestrator finalizes after USER GATE C.
