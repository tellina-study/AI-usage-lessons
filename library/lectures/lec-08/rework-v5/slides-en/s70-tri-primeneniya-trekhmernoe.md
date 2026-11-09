---
# Source: chapter/chapter-part3.md § 4.6 (StageCraft), chapter-part3b.md §§ 4.9 (Tripo
# and the base we don't have), 4.10 (Genie 3).
# Deviation from DECK-KARTA: the map's heading is "Three observations, each with a number" —
# it names the slide's form, not its subject (§6.2 of the form canon requires the opposite).
# The slide carries a list of subjects. The content of the rows is unchanged.
# Each row carries an observation, not a name (§5.15): the lecturer waves off a list of names.
id: s70
local_id: "s70"
section: "4. 3D Scenes and Real Time"
type: assertion_visual
title: "The LED stage, the asset generator, the described environment"
assertion: "Three applications, each with its own number and its own base: the LED stage StageCraft from 2019 — 1,326 panels, a 270-degree arc, more than half of the first season shot inside it, with the in-camera background already computed rather than shot; the Tripo generator produces an asset in 8 seconds on average, and we have no base for comparison at all, because the duration of the same work by a modeler isn't named in any source; Genie 3 delivers 720p at 24 frames per second and environment coherence of several minutes against 10–20 seconds for its predecessors"
source: "Google DeepMind, Genie 3, August 2025 · independent verification WRBench, 23 models, June 2026 (arXiv:2606.20545) · Waymo World Model, February 2026 (demonstration, no independent verification)"
chapter_ref: "chapter-part3.md § 4.6; chapter-part3b.md §§ 4.9–4.10"
media: "assets/screenshots/s70-led-volume-studio.jpg"
media_needed: ""
media_note: "Wikimedia Commons, File:University of Portsmouth CCIXR 1 Virtual Production and Mixed Reality Studio.jpg, CC BY 2.0, author Tim Sheerman-Chase, shot 2023-12-14. Tier 2 (Wikimedia Commons: imageinfo API, then direct download via thumb.wikimedia.org — upload.wikimedia.org on a thumb URL returns 400). An LED stage of the same design the slide is about: a curved wall of panels, a floor in front of it, a camera inside. No source caption on the slide — provenance lives here and in images-log.md"
media_note: ""
blocks:
  - {label: "StageCraft LED wall, October 2019", value: "1,326 panels, 270° arc", note: "2.84 mm pixel pitch, 6 m tall, a 23 m floor across; more than half of season one shot inside it"}
  - {label: "Tripo generator: first asset output", value: "8 seconds on average", note: "no base for comparison: the duration of the same work by a modeler isn't named anywhere, estimates differ by an order of magnitude", key: true}
  - {label: "Genie 3: environment from description", value: "720p, 24 frames/s", note: "environment coherence of several minutes against 10–20 seconds for predecessors of the same class; 11 billion parameters"}
blocks_per_row: 3
timing_min: 1.0
in_bucket: false
method_steps: ["mentions with an observation"]
form: []
vfy: true
status: собран
---

## Visible slide text

**Generating an image without shooting didn't start in 2024.** Nobody was shooting the background of the LED stage back in 2019 either — it was computed in the engine. What changed is how the scene is produced: once it was built by hand, now it's described in words.

## Speaker notes

Three applications, one established and two young. Each is here for the sake of one observation, not for its name.

The first is the LED stage, and it has an exact date and a measurable installation. In October 2019, StageCraft went live, the first permanent virtual-production stage, built for the series "The Mandalorian." A semicircular wall of 1,326 LED panels at a pixel pitch of 2.84 millimeters, six meters tall, a 270-degree arc, around a floor twenty-three meters across. The image is computed in a game engine in real time and goes straight into the camera, not into post. More than half of the first season was shot inside this stage. The cost of the complex was estimated at around a hundred million dollars, but that's an industry-supplier estimate, not an official studio figure, and it needs to be checked separately. By 2024 around a hundred similar stages were operating worldwide, with at least another one and a half hundred under construction.

There's one observation here, and it matters for the evening's axis: StageCraft is already generation of an image without shooting. Nobody shot the background that lands in the camera — it's computed. So the difference between 2019 and 2026 doesn't run along the line "synthetic picture versus shot picture": the picture was synthetic back then too. The difference is in how it's produced. Before generative models, the scene had to be built by hand in the engine, meaning the entire pipeline of the previous slide had to be gone through for every object in it; now it can be described in words. The operation that's disappeared is manual scene building, the location scouting for the backdrop, and building the set in a soundstage.

The second application is industrial 3D asset generators, which by 2026 had moved from promises to delivery schedules. Tripo produces a usable 3D shape in 8 seconds on average; as of February 2026, automatic rigging covers not just humanoid shapes but also quadrupeds, hexapods, birds, snakes, and aquatic creatures. Meshy version six claims cleaner geometry suitable for printing; among the open and self-hostable options are Hunyuan3D 2.1 and TRELLIS.2.

And here we need the direct line that's the whole reason this mention is on the slide at all. How long the same asset takes a modeler isn't named in any source. Estimates that come up in industry discussions differ by an order of magnitude — from a few hours to a few days — depending on topology requirements, and those requirements are exactly the variable everything hinges on. So the eight seconds stand without a multiplier: saying "a thousand times faster" would mean dividing a measured number by a made-up one. Hence the working rule: eight seconds measures the first output, not the finished asset. Between the first output and something you can put into production lie retopology, unwrapping, and rigging, and how long those take isn't covered by this number at all. Comparing a generator's eight seconds to a modeler's days means comparing a rough shape to a finished piece.

The third is the direction the modality is heading. August 2025, Google DeepMind, Genie 3: an interactive 3D environment is generated in real time from a text description. Resolution 720p, twenty-four frames per second, eleven billion parameters, environment coherence of several minutes straight, against ten to twenty seconds for predecessors of the same class. The next frame is predicted from the current state, the internal world representation, and the user's action. The developer has shown a clip about an object left by the camera and seen again, where a wall stays painted. An independent check from June 2026, across twenty-three models, finds world models have the same limitation as the video models from the video section: an object comes back the way it was last seen, not the way it would have become over the time that passed — the only difference is the size of the window, minutes instead of seconds.

Why this deserves its own line. A video model generates a recording — a sequence of frames you can watch. A world model generates a space you can be inside: the frame depends on what the person did. For games, for virtual production, and for simulators, that's a different thing, not an improved version of the old one. There is no classical mode at all here in the same units, and the numbers exist only on the model's side — which is why this is a mention, not a breakdown.

And one last number, without which "720p at 24 frames per second" doesn't read the way it should. By pixels per second, that's roughly a quarter of the accepted level in games — 1080p at 60 frames. The direction called world models impresses not with resolution and not with frame rate, but with its design: the next frame is built not just from a description but from the scene's internal state and the user's action, and that's what sustains environment coherence of several minutes against ten to twenty seconds for predecessors of the same class — a wider window, not a different kind of persistence. There's already a case of industrial use for the direction: since February 2026, Waymo has used a model based on Genie 3 to simulate rare driving scenarios when training drivers. A costed outcome is still absent: nobody has published a comparison with real safety figures, and there's no information on inference cost either.
