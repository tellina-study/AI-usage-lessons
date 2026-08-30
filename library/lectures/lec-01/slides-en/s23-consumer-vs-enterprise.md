---
id: s23
type: comparison
duration_min: 3
assertion: "Consumer vs enterprise plans — where your data goes"
learning_goal: "Consumer plans train on data by default; Samsung 2023 + EU AI Act"
learning_outcomes: [LO6]
references: [bloomberg-2023-samsung, openai-terms-2025, eu-ai-act-2024]
visual:
  pattern: two_column_with_case_anchor
  primary: "Consumer (data→training) vs enterprise (data≠training) + Samsung incident + EU AI Act fines, all inside a single Ocean rounded box container"
---

# Consumer vs enterprise plans — where your data goes

## Assertion

Consumer vs enterprise plans — where your data goes.

## Visual

Visual overhaul issue #155 fix #194 (owner: "abrupt and sloppy").

A compact bridge label at the top of the slide (under the title): "From the shared zone of
responsibility — to the first concrete risk: data". Below — a **single
outer Ocean rounded box container**, framing the whole composition (2
columns + bottom strip), instead of the previous 4 disjointed floating
islands — the pattern brought into line with s08/s12 (single-container).

Inside the container — two columns: on the left "CONSUMER PLANS"
(GOLD_TINT/GOLD): ChatGPT Free / Plus, Gemini Free, YandexGPT Free —
data used for training by default. On the right "ENTERPRISE
PLANS / API" (TEAL_TINT/TEAL, heading kept as-is): ChatGPT Enterprise, OpenAI API (since March 2023), Anthropic Business,
Google Workspace — data not used for training. Bullets in both
columns broken onto 2 lines for readability without overlaps.

At the bottom inside the same container — 2 blocks: on the left a gold callout with
the Samsung case ("3 leaks in a month, March–April 2023; ban on external
AI"), on the right a mini-block on EU AI Act fines ("up to €15M / 3% of turnover,
top tier — €35M / 7%").

## Speaker notes

We opened section four with the general frame — the boundaries of AI as your zone of responsibility. The first concrete question in this zone is where your data physically goes when you type a query into a cloud AI service.

Your text — and often the attached files, images, voice messages — is sent to the provider's servers. What happens to it next depends on the plan.

Consumer plans — free and standard paid. OpenAI ChatGPT Free and Plus use user data to fine-tune models by default; a user can turn this off in settings, but the option requires a deliberate action. Anthropic Claude, since September 2025, asks the user whether they agree to share data for training; if they agree, the retention period increases to five years. Google Gemini on consumer plans uses data for training by default; part of the conversation is selectively reviewed by humans and stored for up to three years with anonymization.

Enterprise and API plans. OpenAI Enterprise, ChatGPT Business, OpenAI API since March 2023, Anthropic for business, Google Workspace, Google Cloud Vertex AI — data is not used to train foundation models. Zero Data Retention agreements are available — the provider doesn't store prompts and responses at all. SOC 2 compliance, encryption at rest and in transit are becoming the standard.

The canonical incident. March–April 2023, Samsung. Engineers of the semiconductor division, in three separate episodes, uploaded to consumer ChatGPT proprietary database code, a transcript of a corporate meeting, and test sequences for chip debugging. Since consumer ChatGPT at that time used data for training by default, Samsung's corporate secrets effectively ended up in OpenAI's dataset. Samsung in response banned employees from using external generative AI services and temporarily introduced a limit of 1024 bytes per prompt.

Regulation. In the European Union, the EU AI Act is in force, being phased in from 2024. The standard tier of fines is up to fifteen million euros or three percent of global annual turnover. The top tier for prohibited practices is up to thirty-five million or seven percent. The NIST AI RMF and NIST AI 600-1 are voluntary but influential US standards. Russian regulation of AI as of 2026 is still taking shape.

The practical takeaway for the engineer: never upload confidential data into consumer AI services without an explicit check of the data-usage policy of the specific plan at the moment of use. This rule is simple but systematically broken.
