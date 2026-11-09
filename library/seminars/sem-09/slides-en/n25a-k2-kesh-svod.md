---
id: n25a
type: measured_outcome_table
duration_min: 1.5
assertion: "A cache read costs 0.107 of a direct read -- confirmed. But only three of the five models hand caching back at all, and our real knowledge base doesn't even reach the threshold on two of them"
learning_goal: "Beat S2-2 (outcome round-up, review 2026-10-29): totals by provider, in big numbers, the same order and group names as n25 word for word. Read vs. direct read is the frame's central pair of numbers (A11)."
visual:
  pattern: measured_outcome_table
  primary: >
    A banner with a pair of large numbers: a read at 0.107x against a
    direct read at 1.0x. Below it, a table across five providers (caching
    works / doesn't), and separately a table on "does OUR knowledge base
    reach the threshold".
  backup: >
    THE NUMBERS AND THEIR SOURCE. 0.107x and 1.25x (a write) are from
    `stend/zamery-k2-kesh/README.md`, Table 3: the same prompt at
    3793-3794 tokens, `anthropic/claude-haiku-5.5`, a direct read at
    $0.00037940 against a cache read at $0.00004045 -- a ratio of 0.107, a
    9.4x difference. A write (a cold call) is $0.00047342, a ratio of
    1.248.

    BY PROVIDER (Table 1): caching metrics are returned by Anthropic (with
    an explicit breakpoint), Gemini, and OpenAI -- all three show a read
    ratio from 0.1x to 0.25x. DeepSeek and Qwen, through this broker
    (DeepInfra, Phala), don't return cache metrics at all -- `cached` = 0
    on every call for both models; this isn't a measurement error, it's an
    honest fact about the broker: DeepSeek's own automatic caching lives on
    its native API, and it isn't exposed through DeepInfra (`README.md`,
    "Honest boundaries", item 2).

    THE LENGTH THRESHOLD OF OUR OWN KNOWLEDGE BASE (Table 7): the session's
    real text -- the instruction plus ten items, 266 words -- comes out to
    851 tokens at Anthropic, 547 at Gemini, 549 at OpenAI (each provider
    has its own tokenizer, hence a one-and-a-half-times spread on the same
    text). Anthropic's `haiku-5.5` threshold is 512 tokens -- our text
    clears it, caching turns on. Gemini 2.5 Flash's threshold is 2048,
    OpenAI's is 1024 -- our text doesn't reach either one, in any of three
    identical calls.

    THE BASELINE IS NAMED TWICE (Baseline Mandate): 0.107x is a share OF
    THE ORDINARY input-token price, not savings in the abstract;
    851/547/549 is a token count by one specific provider's specific
    tokenizer on one specific text, not a universal measure of length.

    The order and names of the three provider groups match n25 word for
    word (the S2 rule: the exposition and the round-up name the groups the
    same way).
---

# Round-up: Who Hands Back Caching, and Does Our Text Reach the Threshold

## Assertion

A cache read is 0.107 of a direct read, confirmed by a real bill, not an expectation. But this only works where caching turned on in the first place.

## Visual

> **0.107x -- a cache read. 1.25x -- a cache write. 1.0x -- a direct read.** All three are shares of the same ordinary input-token price, measured on a 3793-token prompt, `claude-haiku-5.5`.

| Provider | Caching works | Read vs. direct price | Write vs. direct price |
|---|---|---|---|
| Anthropic (`claude-haiku-5.5`) | yes, with an explicit breakpoint | 0.100x | 1.250x |
| Google Gemini (`gemini-2.5-flash`) | yes, automatically | 0.100x | 0.278x |
| OpenAI (`gpt-4.1-mini`) | yes, automatically | 0.250x | not priced separately |
| DeepSeek (`deepseek-chat`, via DeepInfra) | the broker doesn't return cache metrics | -- | -- |
| Qwen (`qwen-2.5-7b-instruct`, via Phala) | the broker doesn't return cache metrics | -- | -- |

> **Does our real knowledge base (266 words, one question) reach the threshold.** Anthropic (851 tokens, threshold 512) -- yes, caching turned on. Gemini (547 tokens, threshold 2048) -- no. OpenAI (549 tokens, threshold 1024) -- no.

## Speaker notes

Let's start with the pair of numbers this whole thing was for. A cache read costs zero point one zero seven of the ordinary input-token price -- this is a real bill, not an expectation: the same text at three thousand seven hundred ninety-three tokens, the same model, a direct read against a cache read -- a difference of nine point four times. A cache write, on the other hand, costs one point two five times a direct read -- that's the price of the first call, and it pays for itself from the second one on.

Now, who this actually works for, out of the five. Three providers out of five return caching metrics and actually turn it on: Anthropic only if you set an explicit breakpoint, Gemini and OpenAI automatically, with no configuration at all. For the remaining two, DeepSeek and Qwen, the broker we call the model through doesn't return caching information at all -- and that's an honest fact about how the system is built, not a flaw in the measurement: DeepSeek's own caching lives on its native API, not on the broker sitting on our rig.

And the last, most uncomfortable number in this round-up. Our real knowledge base -- exactly the ten items that travel to the model in this session, not a padded test text -- weighs eight hundred fifty-one tokens at Anthropic, five hundred forty-seven at Gemini, five hundred forty-nine at OpenAI. Anthropic's caching threshold is five hundred twelve tokens, and our text clears it, caching turns on. Gemini's threshold is two thousand forty-eight, OpenAI's is one thousand twenty-four, and our text doesn't reach either one. That means for two providers out of three, talking about caching on today's task is talking about a task we don't actually have yet: caching shows up once the knowledge base grows three or four times over.

What follows from this, and exactly how the savings break -- next screen.
