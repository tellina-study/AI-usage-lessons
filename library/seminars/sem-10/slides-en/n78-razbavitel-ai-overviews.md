---
id: n78
type: content
duration_min: 1.5
assertion: "Google AI Overviews found text that really was about cheese and pizza — the source turned out to be an old joke, not a cooking recommendation"
learning_goal: "Incident 1 of the concept interlude: Google AI Overviews, 2024. The facts are given at the level of a widely documented public incident (multiple independent media outlets), without an inflated precision of dates/quotes that this level of verification cannot confirm."
visual:
  pattern: content
  primary: >
    A fact tile about the incident, a conclusion tile about the
    difference between "relevant" and "correct."
  backup: >
    The incident is widely and independently documented by multiple
    outlets (May 2024, the launch of AI Overviews in Google Search) — one
    of the year's most publicly discussed examples. The exact wording of
    the source (a joking forum comment) is given without asserting an
    exact publication date for the original comment — see
    fact_check_flags rework/section-5; this level of detail was not
    verified by reading the primary source directly within this session.
---

# Incident 1. Google AI Overviews and the Pizza Advice

## Assertion

The system found text that genuinely addressed the question's topic. By search standards, that's a success — by the standard of the answer the user got, it's a failure.

## Visual

> In 2024, Google Search's AI-generated-overviews feature several times served users advice drawn from sources that sounded credible in form but were, in content, a joke: one widely discussed incident was a recommendation to add non-toxic glue to pizza sauce, whose source turned out to be an old joking comment on an internet forum.

> The system found text that really was about exactly that — about cheese, about pizza, about how to make it less runny. By search standards — a success: high relevance. By the standard of the answer the user got — a failure: the source turned out to be a joke, not a cooking recommendation.

## Speaker notes

In 2024, Google Search's AI-generated-overviews feature — AI Overviews, which gives a short generated answer on top of the ordinary search results — several times served users advice drawn from sources that sounded credible in form but were, in content, a joke or satire. One of the most widely discussed incidents of that year was a recommendation to add non-toxic glue to pizza sauce, so the cheese would hold better and not slide off the crust. The source of this advice turned out to be an old joking comment from an internet forum, which the system found as a topically relevant answer to a question about cheese sticking to pizza.

It's worth working out exactly where this failure actually sits, because it isn't where it looks at first glance. The system found text that really was about exactly that — about cheese, about pizza, about how to make it less runny during baking. By search standards, this is a genuine success: high topical relevance, the chunk topically answers the question asked with precision. But by the standard of the answer a real human receives, it's a failure: the source turned out to be a joke — it was never a cooking recommendation, and the system had no way — and wasn't designed — to tell the two apart based on topical closeness alone.

This is exactly the gap today's whole interlude is built around: relevance and the correctness of content are different things.

It's worth noting that not one of the metrics we measured all day today — not recall, not average rank — is capable of telling this incident apart from a correct answer. A joking comment about glue in pizza sauce, found by the search, would score the same, if not a higher, relevance rating as a real cooking recommendation: both texts contain exactly the same keywords — "cheese," "pizza," "crust," "doesn't stick." A metric that measures topical closeness simply cannot see the difference between a joke and a fact, because that difference lies in the source and the trustworthiness of the text, and topic has nothing to do with it — these are two different dimensions that search on its own does not distinguish.
