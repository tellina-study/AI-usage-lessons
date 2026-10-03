---
id: s19
type: case_study
section: "Section 2. Design"
duration_min: 2
assertion: "All 2,031,220 cars with the driver-assistance feature were recalled: the manufacturer wrote in its own defect report that the prominence and scope of the system's controls may be insufficient to prevent driver misuse — what was remedied was the system's behaviour and its warnings, while the driving model itself was left untouched"
learning_goal: "A failure of the design step: the gap between the person's picture of the system and the system's behaviour — mode confusion; the criterion \"a measure that can be switched off stays a request\""
learning_outcomes: [LO1, LO3, LO6]
chapter_ref: "§2.5, §2.7"
in_bucket: true
interaction: none
protected: true
verify_day_of: false
note: >
  issue #212, owner remark R2-2026-10-01: "a teenager's death in the design section?! what
  is that even doing there". The Character.AI case is taken off: its root is an absent
  safety requirement, and in the section on interaction design it was standing in the wrong
  place. In its place goes a case where interaction design itself is what failed: the
  system's behaviour, its warnings, and the picture of the system in a person's head. The
  choice is confirmed by the wording in the manufacturer's own defect report ("prominence
  and scope of the system's controls may be insufficient to prevent driver misuse") and by
  the fact that the remedy lay entirely in this layer — the prominence of the warnings and
  the strictness of the attention checks, with no changes to the driving model. The
  Character.AI screenshot has been removed from the visible layer and replaced by the real
  Tesla logo (Wikimedia Commons, public domain, see
  assets/screenshots/s19-tesla-real-source.png.url). The abbreviation NHTSA is expanded at
  its first appearance. The new text is written without the contrastive "not X, but Y"
  construction (tools/editorial/README.md §1).
meme_or_visual: >
  case_study: at the top, a "what the case is" block with the manufacturer's real logo and a
  plain-words description of the feature and the event, so that the slide reads without the
  lecturer. Below it two cards: on the left "What broke" (Lucide eye-off icon) with mode
  confusion named, on the right "Why this is a design-phase decision" (layers icon). Under
  them a five-point axis with dates, the recall point picked out in gold. At the bottom a
  gold analysis block and a teal criterion block. No memes: there are dead people in this case.
source: "NHTSA — recall report 23V-838 (12 Dec 2023); NHTSA — closing of investigation EA22-002; NHTSA — recall query RQ24-009 (25 Apr 2024)"
---

# Visible content

## Title bar
All 2,031,220 cars with the driver-assistance feature recalled: the prominence of the controls was found insufficient

## What the case is
**Autopilot** is the set of driver-assistance features in Tesla cars: it holds the lane, the speed and the following distance while the person watches the road and keeps their hands on the wheel.

On 13 August 2021 the National Highway Traffic Safety Administration (NHTSA) opened an investigation: cars with Autopilot engaged were running into emergency vehicles stopped on the road. On 12 December 2023 Tesla recalled all 2,031,220 cars carrying the feature — the entire fleet built since 2012. In the defect report the company wrote, in its own words, that the prominence and scope of the system's controls may be insufficient to prevent driver misuse.

## What broke
Over the course of the investigation, from August 2021 to December 2023, at least 13 fatal crashes accumulated in which foreseeable misuse played its part.

The driver's picture of the system diverged from what the system was doing. The name of this error is **mode confusion**.

## Why this is a design-phase decision
The recall touched not one line of the driving model. What was fixed was how the system presents itself: the prominence of the warnings, the frequency of the attention checks, the threshold past which the feature switches off.

The name "Autopilot" is a decision from the same layer: it sets the picture before the first warning does.

## How it ran in time
Investigation 08.2021 → **Recall of 2,031,220 cars 12.12.2023** → Over-the-air update 12.2023 → Recall query 25.04.2024 → ≥20 crashes after the update

## Analysis
The root is a decision about how the system presents itself to a person: what it reports, how insistently, and when it refuses to carry on. Two years and four months passed between the opening of the investigation and the recall, and all that time the fleet drove with the picture it had been given. Testing the model does not catch an error of this kind: the model behaved exactly as advertised.

## The criterion
The agency opened its query into the remedy on 25 April 2024: in the first four months after the update, at least 20 crashes accumulated with the system suspected of involvement, and some of the measures are switched on by the driver's own consent and switched off the same way. The criterion that carries forward: a measure a person can switch off stays a request — what turns it into a mechanism is the ability to stop the action.

## Speaker notes

The section's failure is about interaction design in its pure form: the model worked as advertised, and what broke was the picture of the system in a person's head.

What the case is. Autopilot is the set of driver-assistance features in Tesla cars: it holds the lane, the speed and the following distance while the person watches the road and keeps their hands on the wheel. In August of twenty-one the American highway traffic safety administration opened an investigation: cars with the feature engaged were running into emergency vehicles stopped on the road. On the twelfth of December of twenty-three Tesla recalled every car with the feature built between twenty-twelve and twenty-three — two million thirty-one thousand two hundred and twenty of them, the entire fleet to the last one. Pay attention to the wording in the defect report, written by the company itself: the prominence and scope of the system's controls may be insufficient to prevent driver misuse.

What broke. Over the course of the investigation, at least thirteen fatal crashes accumulated in which foreseeable misuse played its part. This error has a name that comes from aviation: mode confusion. The person was driving with one picture of what the car does and what they themselves are responsible for; the car was working to a different one.

Now, why the case stands in the section on design. The recall touched not one line of the driving model. What was fixed was the prominence of the warnings, the frequency of the attention checks and the threshold past which the feature switches off — that is, the behaviour of the system and its surfaces of contact. And the name itself, Autopilot, is a decision from the same layer: it sets the picture before the person sees the first warning. Go back to the slide on the scope of design: the name, the promise at the entrance, the right to stop. That is what correcting the picture came to — a recall of two million cars, two years and four months after the investigation opened.

And the sequel, without which the lesson is incomplete. On the twenty-fifth of April of twenty-four the agency opened a query into the remedy itself: in the first four months after the update, at least twenty crashes accumulated with the system suspected of involvement, and some of the measures are switched on by the driver's own consent and switched off the same way. This is exactly what we talked about on the design-system slide: a measure a person can switch off stays a request. What turns it into a mechanism is the ability to stop the action.
