---
id: s42a
local_id: s3-03-2
section: "3. Design and new capabilities"
type: case_study
title: "Raptor's test fire"
assertion: "This is an actual static fire test of the Raptor engine on Starship SN4 — the very test stand that gives the final check to candidates selected by the surrogate model"
source: "[Wikimedia Commons, photo by Steve Jurvetson, 05/05/2020, CC BY 2.0](https://commons.wikimedia.org/wiki/File:Boca_Fuego!_The_Raptor_Engine_Test_on_the_SpaceX_Starship_SN4_%2849861436766%29.jpg)"
media: "assets/razdel-3/raptor/raptor-test-fire-boca-chica-sn4.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Photo: Steve Jurvetson, Wikimedia Commons, CC BY 2.0 — Raptor static fire test on Starship SN4, Boca Chica"
media_needed: "already downloaded (Tier 1, Wikimedia Commons, CC BY 2.0). A large illustration for the Raptor surrogate-model breakdown, added at the owner's instruction (Phase 10, issue #317) — every example now has a large illustration, not just a few."
in_bucket: false
status: draft
---

## Visible slide text

**This is exactly the final check named on the neighboring slide.** The surrogate filters thousands of variants in seconds — but only a selected candidate that has passed the full CFD simulation ever reaches this kind of fire.

**The fire is not an illustration of power, but a measuring instrument.** This is exactly where the surrogate model's accuracy is calibrated against real combustion physics.

## Speaker notes

The photo shows a static fire test of the Raptor engine on the Starship SN4 prototype at SpaceX's Boca Chica site, May 2020. This is a real, not staged, frame: a real flame under a real stage prototype, the very final stage that the whole process broken down on the neighboring slide leads to.

The neighboring breakdown already named the design: a surrogate neural network, trained on an array of combustion CFD simulations, predicts an engine configuration's behavior in seconds instead of hours of full physical computation, and the engineer sorts through thousands of variants instead of dozens. But the surrogate's prediction is not the final decision. It is exactly the static fire test shown in this slide — the step that confirms or rejects the prediction against real physics, not against a statistical approximation.

This is a direct illustration of the surrogate model's boundary, named nearby: the surrogate's accuracy is guaranteed only within the range it saw during training, and there is no way to find out that a specific configuration has stepped outside that range without a full check. The test stand visible in the photo is exactly that full check: expensive, slow, but the only one that truly confirms whether the engine will withstand the load in reality, not just in the network's prediction.
