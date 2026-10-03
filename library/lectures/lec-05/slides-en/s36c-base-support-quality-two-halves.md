---
id: s36c
type: concept
section: "Section 5. Support and operations"
duration_min: 2
assertion: "Support holds a product's quality in place after launch, and that quality is made of two halves with different instruments: the user's satisfaction with the product (people) and the system's reliability (the machine); AI enters both, and from here the section runs along both"
learning_goal: "Introduce the section's subject from scratch: what support is, which two halves quality is made of, what each is measured with, what both disciplines are called, and where AI appears in each"
learning_outcomes: [LO1]
chapter_ref: "§5.0 (new) [for-slide-s36c]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
revision: >
  issue #212, owner-review 2026-10-01, remark on slide 37 ("we start telling the SRE story
  from the middle — introduce the notion and say what it is, a separate preceding step is
  fine; and show the work with users in the same place"). The slide is newly created: it
  introduces the section's subject before the first descent into numbers. It carries the
  frame of the section — support as the holding of quality, quality as two halves (the
  user's satisfaction with the product + the system's reliability) — and names both
  disciplines, with their abbreviations expanded. The turn in the section's subject (owner:
  "right now it is about controlling and supporting AI models, and it needs to be about
  using AI in support") starts here: the line "where AI enters" is present in both halves,
  and in the "people" half it leads on to the slide about assistants and bots. Style rule:
  the contrastive "not X, but Y" format is absent from the slide text and the notes.
meme_or_visual: >
  concept: a wide "what this is" panel at the top. Below it two columns of equal weight —
  "PEOPLE · satisfaction with the product" (Lucide users icon) and "SYSTEM · reliability"
  (Lucide activity icon), each with: what it deals with, three measures as a list, the name
  of the discipline, and a teal "where AI enters" line. At the bottom a gold panel saying
  that the halves hold quality only together, with the map of the section.
source: "Google, Site Reliability Engineering (O'Reilly, 2016) — the reliability discipline given its shape; ITIL 4 (Axelos, 2019) — the IT service management framework the help desk and its measures come from"
---

# Visible content

## Title bar
Support holds quality in place: one half is people, the other is the system

## Body
[A "what this is" block on top; two columns with measures below it; a gold panel at the bottom]

**WHAT SUPPORT IS.** After launch a product makes the same promise every day: an answer will come, it will be correct, and what breaks will be mended. Support is the work that holds that promise for years. The promise has two halves, and they are measured with different instruments: one you ask a person about, the other you read off the system.

**PEOPLE · the user's satisfaction with the product**
The half turned towards the person: questions, complaints, tickets, returns. The discipline grew out of the help desk and the IT service management framework (ITIL).
The measures are what the person sees:
· the share of tickets closed on first contact;
· time to first response and time to resolution;
· the rating a person gives once a ticket is closed.
**Where AI enters:** a suggester at the agent's elbow, and a bot answering the customer on its own — the next slide.

**SYSTEM · reliability**
The half turned towards the machine: availability, latency, outages, deployments. The discipline was given its shape at Google and published as a book in 2016 — site reliability engineering (Site Reliability Engineering, SRE).
The measures are what you read off the system:
· the share of requests served successfully;
· response latency;
· the error budget — how many failures are permissible in a period.
**Where AI enters:** the object of observation, and an instrument of failure drills.

[Gold callout]
The halves hold quality only together. A system that never fails but leaves a person unable to get an answer to their question loses the product's promise; attentive support on top of a service that keeps falling over loses it just the same. From here the section runs along both: reliability in numbers, AI in the work with people, and the failure drill that tests both.

## Speaker notes

Let us start with the subject. What support is, said in one sentence. After launch, a product promises people the same thing every day: an answer will come, it will be correct, and what breaks will be mended. Support is the work that holds that promise for years. Everything else in the section is a way of holding it.

Now the thing the whole section rests on. The quality being held is made of two halves, and they have different instruments. The first you ask a person about, the second you read off the system.

The first half is the user's satisfaction with the product. These are the questions, complaints, tickets and returns: everything a person comes with when something has gone wrong, or is simply unclear. Its discipline is an old one, grown out of the help desk and the IT service management framework — ITIL, short for Information Technology Infrastructure Library. What gets measured here is what the person feels: what share of tickets closed on first contact, how long they waited for a first response and how long for a resolution, what rating they gave when the ticket was closed.

The second half is the reliability of the system. Availability, latency, outages, deployments. This discipline was given its shape at Google, a book came out in two thousand sixteen, and since then it has been called site reliability engineering, SRE for short. It is measured by what the system itself reports: the share of requests served successfully, latency, the error budget.

Keep in mind that the halves work only as a pair. A system that never fails but leaves a person unable to get an answer to their question loses the product's promise. Attentive support on top of a service that falls over every day loses it in exactly the same way. Quality lives at the intersection.

And the last thing. AI comes into both halves, and it comes in differently. Into reliability — as the thing being watched, and as an instrument of failure drills. Into the work with people — as a suggester at the agent's elbow and as a bot that answers the customer on its own. From here we go along both: reliability in numbers first, then AI in the work with people, then the failure drill that tests both halves at once.
