---
id: s20
type: assertion_visual
duration_min: 1.5
assertion: "An application = AI packaged into a product interface"
learning_goal: "Application as a layer; examples of unambiguous applications (without Copilot ambiguity)"
learning_outcomes: [LO1, LO4]
references: [google-translate-2026, anthropic-2024-effective-agents]
visual:
  pattern: app_logos_grid
  primary: "Google Translate metrics + a grid of 6 logos (Translate / Notion AI / YandexGPT in Search / Grammarly / Yandex Maps / Adobe Firefly)"
---

# An application = AI packaged into a product interface

## Assertion

An application = AI packaged into a product interface.

## Visual

At the top, an Ocean rounded box with Google Translate metrics: «1+ billion unique users per month, ~1 trillion words translated per month (across Translate, Search, Lens, Circle to Search)». Below, a 2×3 grid of six logos in small cards: Google Translate, Notion AI, YandexGPT in Search, Grammarly, Yandex Maps, Adobe Firefly. Under each logo, a one-phrase caption about the AI's role. No Copilot.

## Speaker notes

An application is a full-fledged product for the end user, in which AI is just one of the internal components. The user does not write prompts; they press buttons, fill in forms, speak by voice. The AI works «under the hood», and the user is rarely required to understand what's inside.

The basic characteristic — AI as a feature, not a product. The application solves a domain task, and the AI provides the corresponding functionality. A good application has a deterministic user interface — the same user action yields the same reaction, even if the AI output varies internally. The application adds guardrails, fallback scenarios, caching, and error review around the AI.

Canonical examples of unambiguous applications. Google Translate — inside is neural machine translation; the user sees an input box and a translation. As of 2026 — more than one billion unique users per month, about one trillion words translated per month. That trillion is counted across Google Translate, Search, Google Lens, and Circle to Search, not only in the Translate app itself.

Notion AI — inside is GPT-4 or Claude; the user sees «Summarize», «Improve writing», «Continue writing» buttons right in the interface of their workspace. AI here is not a separate chat but a functional button next to every block of text.

YandexGPT in Yandex Search — inside is Yandex's own LLM; the user sees a generated brief answer above the list of ordinary search results. This is the classic «AI as a feature»: to the user it's just improved search, not «chatting with an AI».

Grammarly — NLP models plus an LLM; the user sees underlines and suggestions in any text field. Yandex Navigator and Maps — ML models for routing, ETA forecasting, traffic-jam detection. Adobe Firefly — diffusion models, a «Generate» button in Photoshop.

A case where an application is the optimal choice: once a week you need to translate a small block of technical documentation from English to Russian. You don't need a standalone model — the volume doesn't justify deployment. You don't need a chat — using a chat for translation is cumbersome. You don't need an agent — the task is single-step. Google Translate or YandexGPT in Search are ready-made applications, optimized for exactly this type of use. Overpaying with complexity is an anti-pattern.

An important clarification before the next slide. Applications come in two types. The first — with a user interface, like all six examples on this slide: the user sees a UI and interacts with it. The second type — automated applications with no interface at execution time: an ETL pipeline with an AI classifier, a backend service that pulls in data on its own and puts the result into a table. On the next slide, when we assemble the checklist into a quadrant, these two types will end up in different corners.
