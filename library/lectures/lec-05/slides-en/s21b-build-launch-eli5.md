---
id: s21b
type: eli5_overview
section: "Section 3. Build / Launch"
duration_min: 1.5
assertion: "Build and launch in plain terms: writing code is now nearly free, so what matters most is no longer \"write it\" but \"ship it safely and stop it in time\""
learning_goal: "ELI5 overview of the build-and-launch phase: why release mechanics matter, the mental model \"a valve, not a switch\""
learning_outcomes: [LO1]
chapter_ref: "§3.1 [for-slide-s21b]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  eli5_overview: three cards, a "valve/faucet" icon on the left (a smooth feed, not an on/off
  switch). Plain language.
---

# Visible content

## Title bar
Build and launch in plain terms

## Body
**What it is.** The phase where an artifact becomes a working product for users. AI has made writing the code itself nearly free.

**Why release mechanics matter.** Since building is cheap, the cost of a mistake is no longer "writing it" but "shipping the wrong thing to everyone at once." You need a way to turn on something new gradually and roll it back fast.

**Mental model.** A launch is a valve, not a switch: feed the new feature to 1% → 10% → 100%, watch the reaction, close it if there's trouble. And keep a "kill" decision ready, not just "keep polishing forever."

## Speaker notes

Build and launch is the phase where AI has changed the most, so it's important to set the right emphasis right away. Writing code is now nearly free: what used to take weeks, an agent does in minutes. But that's exactly why the center of gravity shifted. Since code is cheap, what became expensive isn't building — it's the two human ends of the process: precisely stating what we want, and properly checking what came out.

Launching isn't "press a button and turn it on for everyone." The right mental model is a valve, not a switch. You feed a new feature gradually: first to one percent of users, then ten, and only once you've confirmed everything is fine — to everyone. This mechanics — feature flags, canary and staged rollout, rollback — is familiar to you from engineering practice. What's new here is that a product decision now steers those same levers: whether this feature is even worth keeping in the product at all.

And the second half of the launch discipline is knowing when to stop in time. A good product process has failure thresholds written down in advance and isn't afraid to kill an initiative that hasn't reached reliability for years. Next we'll see both failures: a giant that shipped to everyone at once with no rollout, and a company that, by contrast, showed exemplary stopping discipline.
