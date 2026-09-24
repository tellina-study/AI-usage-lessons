---
id: s25c
type: schema_matrix
section: "Section 4. Testing — TDD as a discipline"
duration_min: 3
assertion: "The coding agent's local toolkit closes five channels in which the agent is blind without a tool: data (Testcontainers), network (MSW / WireMock OSS), user interface (Playwright), your own checks (a skill wrapper), an air-gapped setup (local test generation) — and for each one it names exactly what cannot be done without it"
learning_goal: "Five categories of local test tooling, framed by the question \"what can the agent physically not check without it\"; Playwright is a category of its own (without it, front-end debugging is blind)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.5 [for-slide-s25c]"
references: [testcontainers, msw, wiremock, pytest-generator-distil]
verify_day_of: true
visual_brief: >
  Five cards in a 3 + 2 grid (the sixth cell is a teal "How to choose" block so the bottom row is not half-empty).
  Each card: a colored header plate with an icon (database / route / monitor / terminal / lock) + the category + the tool;
  a "WHAT IT DOES" row on surface; an "IMPOSSIBLE / VERY HARD WITHOUT IT" row on gold tint (gold on every card,
  not selectively). At the bottom — one muted "Honest limits" line (the MSW mock is a guess, WireMock Cloud vs OSS,
  the vendor-claimed accuracy of pytest-generator).
interaction: none
---

# Visible content

## Title bar
The agent's local toolkit: closing its five blind channels

## Body
[Card 1 — Data · Testcontainers]
WHAT IT DOES: spins up a real Postgres / Kafka / Redis in Docker on a temporary port — on the agent's own machine.
IMPOSSIBLE WITHOUT IT: the agent checks a query against an imagined schema — the test is either never written, or green on a stub and red in prod.

[Card 2 — Network · MSW]
WHAT IT DOES: intercepts HTTP inside the process: one handler for both unit and end-to-end tests. Outside JS — WireMock (open source).
IMPOSSIBLE WITHOUT IT: the agent either hits the real API — flaky, paid, rate-limited — or does not test networking code at all.

[Card 3 — User interface · Playwright]
WHAT IT DOES: gives the agent a browser: not a picture, but the page's element (accessibility) tree — it clicks, fills forms, emits a test.
IMPOSSIBLE WITHOUT IT: the agent never sees the real interface — front-end debugging runs blind and is essentially pointless.

[Card 4 — Your own checks · a skill wrapper]
WHAT IT DOES: packs the repository's existing "linter → type check → tests" loop into a single call.
IMPOSSIBLE WITHOUT IT: the agent guesses the project's commands every time — and silently skips the check it never knew about.

[Card 5 — Air-gapped setup · pytest-generator]
WHAT IT DOES: a fine-tuned 8-billion-parameter model (~5 GB, a CPU build exists) writes test skeletons on the machine.
IMPOSSIBLE WITHOUT IT: any AI test generation = sending source code to an external service: in an air-gapped setup that is a ban.

[Sixth cell — how to choose]
Each tool closes exactly one channel the agent is blind in: data, network, user interface, your own checks, an air-gapped setup. Local, deterministic and already working — take it and wrap it; the only thing worth writing yourself is a wrapper around your own check loop.

[Muted bottom line]
Honest limits: without a real sample API response an MSW mock is the agent's guess, not a contract · WireMock's AI features live in the paid WireMock Cloud, not in the local open-source core · pytest-generator — ~77% accuracy claimed by the vendor, not independently verified, adoption low.

## Speaker notes

Five channels in which a coding agent is blind without a tool, and what closes each one — locally, on the developer's machine, without reaching out to a cloud service.

Data — Testcontainers: it spins up a real Postgres, Kafka or Redis in a container on a temporary port and shuts it down after the run. Without it, the agent checks a query against an imagined schema: the integration test either never gets written at all, or turns out green on a stub and red in production.

Network — MSW: it intercepts HTTP right inside the process, and one handler works for both unit and end-to-end tests; outside JavaScript the same class of task is covered by the open-source WireMock. Without it, the agent either hits the real API — flaky, paid, rate-limited — or does not test networking code at all.

User interface — Playwright: it gives the agent a browser and, more importantly, not a picture but the page's element tree, which it uses to click, fill forms and emit a test. Without it, the agent never sees the real interface — front-end debugging runs blind and is essentially pointless. This is precisely the category that neither a database nor a network mock covers.

Your own checks — a skill wrapper: the "linter, type check, tests" loop that already exists in the repository, packed into a single call. Without it, the agent guesses the project's commands every time and silently skips the check it never knew existed.

An air-gapped setup — pytest-generator: a fine-tuned eight-billion-parameter model writes test skeletons right on the machine. Without it, any model-driven test generation means sending source code to an external service: in an air-gapped setup that is a ban, not an inconvenience.

The honest limits deserve naming too. Without a real sample API response, a mock is the agent's guess rather than a contract. WireMock's AI features live in the paid cloud, not in the local core. And the claimed accuracy of pytest-generator, around seventy-seven percent, is the vendor's own and has not been verified independently.
