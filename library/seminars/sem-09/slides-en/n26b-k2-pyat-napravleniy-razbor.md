---
id: n26b
type: measured_outcome_table
duration_min: 2.0
assertion: "None of the five directions cleaned up Case 1's number-comparison errors -- and a strict conditional rule form measured worse than ordinary prose, not better"
learning_goal: "Beats S2-2+S2-3 (round-up and breakdown by direction, merged -- this measurement isn't about right/wrong answers by group but about structure's effect, so the breakdown runs shorter than five screens): a result for each direction with a verdict and a takeaway (C3, C10), plus an honest correction on the 'prefix stability' direction -- latency isn't a caching metric, and that question has since been measured separately and correctly."
visual:
  pattern: measured_outcome_table
  primary: >
    The same five-direction table, now with an outcome column and a
    verdict. Below it, a highlighted banner on the conditional form
    (worse than prose) and a banner on the honest boundary: what these
    five directions don't fix.
  backup: >
    NAMES AND ORDER OF DIRECTIONS -- word for word the same as on n26a
    (S2: the exposition and the round-up name the groups the same way).

    THE NUMBERS -- `stend/zamery-k2/README.md`, the same run as on n26a.

    THE CORRECTION ON "PREFIX STABILITY" (removes the stale "the cache
    effect isn't confirmed"). The earlier wording rested on a latency
    measurement through the `chainLlm` node (1178 ms against 794 ms) --
    that's RESPONSE TIME, not a caching metric: the node only exposes the
    text and `executionTime`, the `usage.cached_tokens` field isn't
    visible at all, and latency is driven by the network and the broker's
    queue, not by a cache hit (`stend/zamery-k2-kesh/README.md`, "Why the
    earlier measurement couldn't show anything"). On top of that, that
    measurement's model, `qwen/qwen-2.5-7b-instruct`, has no caching
    discount at all with its own provider -- there was nothing to measure
    there in the first place. The question "does caching work, and what
    does it depend on" has since been measured separately, through the
    real provider's own `usage` field, not through response time -- 119
    calls, five providers, a result stated not as "unconfirmed" but as an
    exact condition. This table row no longer carries a conclusion about
    caching -- only the fact that THIS way can't measure it, and a pointer
    to the question being settled correctly elsewhere.

    The "prefix stability" direction no longer has a number of its own in
    THIS table -- it's the only one of the five where the claimed result
    turned out to be a measurement-design error, not a finding; the other
    four are kept as measured.
---

# Round-up and Breakdown: What the Five Directions Showed

## Assertion

Format, position, repeating the question -- a weak effect within the noise on a sample this size. A conditional rule form -- measurably worse than prose. Caching can't be measured this way at all.

## Visual

| Direction | Result | Verdict |
|---|---|---|
| Format (list / headers / with description) | 2/5 · 3/5 · 3/5 -- simple questions correct everywhere, the difference is within the noise | didn't clean it up |
| Position of the needed item (start/middle/end) | 4/5 · 3/5 · 4/5 -- the middle's dip is there, but weak on a short list | didn't clean it up |
| Rule wording (prose / "IF...THEN...") | **5/12 for prose against 2/12 for the conditional form -- worse, not better** | conditional form rejected |
| Question before and after the list | 2/5 · 3/5 -- a small plus, within the noise at this volume | didn't clean it up |
| Stability of the prompt's start (for caching) | caching can't be measured this way (a response-time measurement) -- the caching metric lives in a different response field, not in latency. The question is settled by a separate measurement, through the real provider metrics | a measurement-design error, not a finding |

> **The most unexpected part.** The explicit formula "IF the amount is more than 3,000 rubles -> the manager decides, ELSE -- no" didn't help the model compare 2,500 against 3,000: 0 correct out of 8 attempts, in prose and in conditional form alike. The error doesn't live in how the rule is written -- it lives in how the model compares two numbers inside its own answer.

> **Honest boundary.** The five directions work on the prompt's DESIGN. Case 1's number-comparison error lives on a different layer -- no amount of prompt structuring fixes it.

> **The final prompt** (`stend/zamery-k2/promt_itogovyi.md`) keeps what didn't test worse: headers, the question before and after the list, prose rules, not conditional form.

## Speaker notes

The result is honest, and it isn't what we expected. Format -- markdown headers and brief descriptions are slightly better than a bare list, but on a sample of five questions the difference is within the noise. Position -- the middle's dip is there, but weak: the list is short, six to ten items, not the scale where the effect is documented strongly -- the same effect we broke down on twenty documents of academic length would dip noticeably more here.

The most interesting part is rule wording. We took the question about a 2,500-ruble refund that already confused the model back in Case 1, and rewrote the rule as an explicit formula: if the amount is more than three thousand -- a manager, otherwise -- no. The result got worse, not better: two correct answers out of twelve, against five for ordinary prose. On the specific question about two thousand five hundred rubles -- zero correct out of eight attempts, in both forms of the rule. The model confidently answers "yes, through the manager," without noticing that two thousand five hundred is less than three thousand, even when the inequality is written in plain text right in front of it.

Now, honestly, about the fifth direction -- stability of the prompt's start, for caching. This measurement was designed wrong, and I'll say exactly how: we measured response time, not a cache hit. Response time depends on the network and on the broker's load, and the caching metric lives in a separate field of the provider's response, which this calling method never showed at all. On top of that, that run's model doesn't even have a caching discount with its own provider -- there was nothing to measure there in the first place. We've since measured "does caching work, and what does it depend on" correctly: through the real metrics of five providers, not through response seconds.

One takeaway worth carrying separately. The five directions work on the prompt's design -- how it's put together. The error we found in Case 1 -- the model mixing up a comparison between two numbers -- lives on a different layer. A well-built prompt doesn't fix this class of error no matter how much you improve it, and a conditional rule form doesn't help here -- it gets in the way.
