---
id: s31
type: assertion_visual
section: "Section 6. Framework"
duration_min: 3
assertion: "Financial data/PII/biometrics must not go into a public LLM (Federal Law 152-FZ, localization, biometrics regime); biometrics are irreversible on leak; the «autonomous» Just Walk Out relied on >1000 reviewers"
learning_goal: "SECURITY: (A) 152-FZ/PII/on-prem-vs-cloud + (B) KYC/liveness/hidden human cost; forward→CV bias L7"
chapter_ref: "§6.3"
visual_brief: "2 EXPLICITLY separated panels (A data+law / B CV layer) — bold header cards MID/TEAL + a thick vertical divider. A large gold anchor band: the image «a password can be changed — a face cannot» (d31 password-vs-face, wide). Gold conclusion. Aggregation = 1 slide (s31_decision)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Financial data, PII (personal data), and biometrics must not go into a public LLM.

## Body
[Panel A — a separate Ocean box, bold MID header card | a thick vertical divider | Panel B — a separate Ocean box, bold TEAL header card]

**(A) Data and law: 152-FZ / PII**
- financial data + **PII** + biometrics = sensitive; 152-FZ — localization of personal data of Russian citizens, biometrics = a strict regime
- public cloud: the data **leaves the perimeter** · no control over **retention** · **auditability falls**
- the criterion — by the **sensitivity of the data and the regime**, NOT by the power of the model

**(B) CV layer: KYC, biometrics, hidden labor**
- **KYC** = client identification; **liveness** — a live human in front of the camera, not a photo/mask/deepfake (strict regime)
- **Just Walk Out** (Amazon) wound down in 2024: the «autonomous» checkout relied on **>1000 reviewers** in India — hidden labor
- *Computer-vision bias is deepened in Lecture 7.*

[Large gold anchor band — the image «a password can be changed, a face cannot» (d31)]
**Biometrics are irreversibly compromised on a leak** — the same logic «irreversible → strict gate» that ran through the whole lecture. Password: leaked → changed (REVERSIBLE) vs Face/fingerprint: leaked → a new one cannot be issued (IRREVERSIBLE).

[Gold callout, bottom]
«Fully autonomous» in marketing is a hypothesis to check, not a fact *(Amazon disputed the scale)*.

## Speaker notes

The course's through-line theme — data security — is sharper in finance and retail than anywhere else: this is where financial data, personal data, and biometrics are processed. The law on personal data sets requirements for processing the data of Russian citizens: in particular, the localization requirement — storage and processing on servers in Russia — and biometric data have a separate, stricter regime. The practical engineering conclusion: financial data, personal data, and biometrics must not be sent into a public uncontrolled cloud language-model service — this is both a methodologically wrong choice of AI type and a potential violation of localization requirements. A public cloud has three structural drawbacks that cannot be configured away: the data leaves the organization's perimeter, you do not control what the provider does with the transferred data, and auditability falls. The engineering criterion for the choice is by the sensitivity of the data and the regulatory regime, not by the power of the model.

The second block — computer vision, which we cover illustratively. Verifying a client during digital onboarding often includes a liveness check — that in front of the camera is a real human, not a photo, a mask, or a deepfake — and matching the face against a document. This is biometrics, that is, the strict regime of the law. Let us set out the key principle in a separate sentence: a biometric feature is irreversibly compromised on a leak — a password can be changed, a face and a fingerprint cannot. Therefore the cost of error in protecting biometrics is asymmetric in the same way as the cost of a forecasting error at Zillow.

And one more lesson — hidden human labor. Amazon's cashierless-store technology Just Walk Out was wound down from a number of formats in April 2024; by reports, the autonomous checkout relied on over a thousand human reviewers in India who processed problematic transactions, although Amazon disputed such an interpretation of the scale. The lesson: before automating a vision task, assess the real share of manual processing and the total cost of ownership — «fully autonomous» in marketing is a hypothesis to check, not a fact. Computer-vision bias across groups is deepened in Lecture 7.
