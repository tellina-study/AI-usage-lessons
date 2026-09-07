---
id: s25
type: assertion_visual
section: "Section 3. Build / Launch"
duration_min: 1.5
assertion: "Review doesn't scale alongside generation — an asymmetry between the cost of generating and the cost of verifying"
learning_goal: "AI limitations of Build/Launch: why review is a structural bottleneck, not a temporary staffing shortage"
learning_outcomes: [LO2, LO3]
chapter_ref: "§3.5 [for-slide-s25]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: a scale tilted heavily to one side — on the left a light weight
  "generation cost" (falls fast, cheap), on the right a heavy, motionless weight
  "verification cost" (hasn't moved) — visualizes the asymmetry.
---

# Visible content

## Title bar
Double the generation speed and you double the review queue — not the throughput

## Body
[Tilted scale: a light "generation" weight / a heavy motionless "verification" weight]

**The asymmetry of generation cost and verification cost**
- Generating plausible code — seconds; checking it — hasn't gotten faster
- The 70% problem: seniors rethink AI output, juniors ship a "house of cards made of code"

[Gold callout]
Shipping without an eval gate or a rollback plan isn't speed — it's a deferred cost

## Speaker notes

Review doesn't scale alongside generation — this is the section's load-bearing limitation: Anthropic's own measured finding about its own product, not outside criticism. It directly means that "we ship fast because building is now free" is a trap if review volume doesn't scale in parallel.

It's worth spelling out why review specifically became the bottleneck, because it's a direct consequence of the keystone asymmetry, not a coincidence. Generation and verification are operations of fundamentally different cost: a model can generate plausible code in seconds, but checking that it's correct, safe, and does what's needed still requires real-time human understanding, which hasn't gotten any faster. By making one side orders of magnitude cheaper and leaving the other unchanged, AI didn't remove the work — it moved its entire mass onto the side that didn't get cheaper. Hence the counterintuitive consequence: doubling generation speed doesn't double the product's throughput — it doubles the review queue.

The 70% problem: AI agents get a team roughly seventy percent of the way to a production-quality result; the remaining thirty percent is where senior engineers add value that AI doesn't automatically supply. Seniors actively rethink AI output; juniors accept it more readily, producing a "house of cards made of code." Both failures below are variations of exactly this limitation at the level of a launch decision. What stays from the classic: version control and PR review, feature flags, staged rollout as the prototype of the agency ladder, a kill switch, a human-owned specification. When this isn't AI-first: an irreversible or capital-intensive decision must not be made by a model at the lowest rung of the agency ladder without a deterministic business rule on top of it.
