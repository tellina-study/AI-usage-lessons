---
id: n27
type: failure_vignette_table
duration_min: 1.5
assertion: "The protocol's author called loading all the definitions at start-up a problem and measured it on his own examples; the same documentation gives 55,000 tokens on five servers and a drop in the accuracy of tool choice past 30–50 tools; one team cut its set from 40 tools to 13, another tried loading on demand and declined it — and nobody removed their connected servers in the process"
learning_goal: "The checkable cases of the second case: what exactly well-known teams did with tool definitions, and how we know about it. The slide takes away a convenient false frame — the refusal concerns the loading of definitions at start-up, and the servers stayed; and there is no single answer across the industry, the last row being the direct opposite of the first three"
visual:
  pattern: failure_vignette_table
  primary: "Four numbered rows: what was done and where it is known from, each with its own source and date. At the bottom, in a gold line — what follows from this for the room, with a direct statement that the industry has no identical answer."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.7, §B.27 (part1e.md). Round 5 (issue 225): the slide was written anew for the replacement of the case. The previous three cases (Unicode hiding, the Deadbugz campaign, the postmark-mcp incident) were taken out of the seminar along with the previous case and were not carried over into the new one.
    The evidence base is research/mcp-kontekst-otkaz.md, all four rows VERIFIED against the primary sources, twice: by a fact-checker subagent and then independently by the session's orchestrator through a verbatim substring search over the downloaded page (not over the search snippet), accessed 2026-10-07.
    Row 1: anthropic.com/engineering/code-execution-with-mcp, \"Nov 04, 2025\" (the machine-readable date on the page is 2025-11-04) — \"Tool definitions overload the context window\"; \"This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%\"; \"present MCP servers as code APIs rather than direct tool calls\". The example in the article is the Google Drive and Salesforce servers, the method of measurement is not disclosed on the page, and so on the slide this is called an example from the article, not an industry norm.
    Row 2: docs.claude.com/en/docs/agents-and-tools/tool-use/tool-search-tool — \"A typical multiserver setup (GitHub, Slack, Sentry, Grafana, and Splunk) can consume ~55k tokens in definitions before Claude does any work. Tool search typically reduces this by over 85 percent, loading only the 3–5 tools Claude needs for a given request\"; \"Claude's ability to pick the right tool degrades once you exceed 30–50 available tools\". In that paragraph of the documentation it says \"multiserver setup\" and the word MCP is absent — which is why the slide lists the servers themselves and does not impute the protocol to them. This is also an independent confirmation of the figure of 55,000 that stands in the deck on n18 from a different source.
    Row 3: github.blog \"How we're making GitHub Copilot smarter with fewer tools\", Anisha Agarwal & Connor Peet, November 19, 2025 — \"trims the default 40 built-in tools down to 13 core ones\"; \"improve success rates by 2-5 percentage points\" (the page's markup has non-breaking spaces, so a direct grep for the string without them returns nothing — checked and recorded). The limit of 128 tools per request — code.visualstudio.com/docs/copilot/agents/agent-tools, \"Cannot have more than 128 tools per request\". The pair of figures 190/400 milliseconds from the same blog the slide deliberately does NOT take: on the page the acronym TTFT is expanded two different ways in one sentence, which is a defect in the primary source.
    Row 4: manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, Yichao 'Peak' Ji, 2025/7/18 — \"We tried that in Manus too. But our experiments suggest a clear rule: unless absolutely necessary, avoid dynamically adding or removing tools mid-iteration\"; the reasons are the invalidation of the KV cache and the model getting confused about earlier steps; in its place the section \"Mask, Don't Remove\".
    What was NOT confirmed and is not put on the slide: the owner's formulation that \"large companies have started abandoning MCP\" — not one primary source confirms it, and every team checked keeps its servers; Cloudflare Code Mode explains its own move by the distribution of training data, there is not one instance of the words \"context window\" on their page, and they give no figures at all; the --dynamic-toolsets flag of GitHub's official server was deleted in v1.1.0 (see n26); Block/Goose, Shopify, Stripe, Vercel, Sourcegraph — no public statements on the topic were found. The details are in research/mcp-kontekst-otkaz.md § \"What was NOT confirmed\".
    An edit after two delivered classes (issue 225, qa/RAZBOR-PROVEDENIYA.md §A5): in both classes
    something unverified was said aloud — that large companies, named by name, had abandoned MCP en
    masse — followed immediately by a promise to look into how the story ended. The slide stood on
    verified material the whole time, but the refutation lay in the reference material as a general
    paragraph and did not fire when spoken aloud. It is now carried out as a separate direct line at
    the start of the note: \"this is how it gets retold — the primary sources do not confirm it —
    this is what they do confirm\". There are no names in the refutation, deliberately: there is no
    primary source on them in either direction (research/mcp-kontekst-otkaz.md § \"What was NOT
    confirmed\", items 1, 9, 10), and naming them would mean arguing with an equally unverifiable
    formulation. The figures, sources, dates and four rows of the visible layer did not change."
---

# The definitions were taken off start-up. The servers stayed

## Assertion

Loading all the definitions at start-up was called a problem by the protocol's own author, who measured it on his own examples. One team cut its toolset from 40 to 13, another tried loading on demand and declined it. Nobody removed their connected servers in the process.

## Visual

1. **The protocol's author called this a problem.** "Tool definitions overload the context window" — that is how his own analysis opens. The move in its place: present servers as a code interface that the agent reads on demand; in the example analyzed in the article — 150,000 tokens against 2,000. The servers stayed where they were (Anthropic, engineering blog, 04.11.2025).
2. **The count on five servers.** The set GitHub, Slack, Sentry, Grafana, Splunk takes up about 55,000 tokens of definitions before the work begins; loading on demand removes more than 85% of that, pulling in the 3–5 tools that are needed. From the same page: the accuracy of choice drops once there are more than 30–50 available tools (documentation from the same vendor, accessed 07.10.2026).
3. **They cut their own set.** There were 40 built-in tools, and 13 core ones were kept — and it was measured: the success rate on two sets of tasks grew by 2–5 percentage points. The platform's limit is 128 tools per request (GitHub, engineering blog, 19.11.2025).
4. **They tried it and declined.** Loading tools on demand was tried and declined: changing the set in the middle of the work wipes the cache and confuses the model about earlier steps. The move in its place — mask the surplus ones, leaving the definitions where they are (Manus, 18.07.2025).

> Look at which mode the definitions are loaded in at your place, and keep the set to the task. The industry has no identical answer: the last row is the direct opposite of the three before it.

## Speaker notes

Now the same thing beyond this project, with sources. Four cases, each read in the primary source.

It is worth beginning with what is not in those sources.

**This story is often retold as companies abandoning MCP — sometimes with the names of large companies attached. In the primary sources that is not confirmed in a single case. What is confirmed is something else: tool definitions were taken off the start of the context, and the servers stayed.** Not one of the teams that has a public primary source on this topic dropped the protocol or removed its servers; for the names that circulate in the retelling, no public statement on the topic was found at all — neither confirming nor refuting.

In the protocol's own author it is said verbatim: the move in its place is to "present MCP servers as code APIs". The servers stay where they are, and what changes is the way their definitions reach the model. The refusal in all four cases below concerns exactly one practice — loading the definitions of all the tools into the context in advance.

The first case: the problem was named by the protocol's own author. "Tool definitions overload the context window" — that is how his own analysis in the engineering blog opens, published on 4 November 2025. The move proposed in its place is this: present servers as a code interface that the agent reads on demand off the file system, instead of enumerating the tools directly. In the example analyzed in the article the spend falls from 150,000 tokens to 2,000. The example is a specific one — two named servers — and the method of measurement is not disclosed on the page, so as an order of magnitude it is useful, while as an industry norm it does not read. The servers stay where they are in that move: what changes is the way the definitions reach the model.

The second case: the count on five servers, from the same vendor's documentation. A set of GitHub, Slack, Sentry, Grafana and Splunk takes up about 55,000 tokens of definitions before the work begins. Deferred loading removes more than 85 percent of that spend, pulling in the 3–5 tools a particular request needs. This is an independent confirmation of the figure that stands in the section's first case as the cost of a connection — now from a second source. The same page names a second boundary, a non-monetary one: the accuracy of tool choice drops once there are more than 30–50 available tools.

The third case: a team cut its own set. There were 40 built-in tools, and 13 core ones were kept — and the result was measured on two sets of tasks with two models: the success rate grew by 2–5 percentage points. The same page states a hard limit on the platform: no more than 128 tools per single request, and past that the request is rejected. The publication is dated 19 November 2025.

The fourth case is the opposite, and it stands last deliberately. Another team tried loading tools on demand and declined it. Two reasons are named. Tool definitions lie at the start of the context, so any change of the set in the middle of the work wipes the cache for everything that comes after. And the model gets confused when earlier steps refer to a tool that is no longer in the current set. The move in its place is to mask the surplus tools, leaving their definitions where they are.

Hence the practical conclusion, and it is more modest than one would like. The industry has no identical answer: the fourth row is the direct opposite of the first three, and both positions are backed by practice that works. What remains to be done in a situation like that is to look at which mode the definitions are loaded in at your place, and to keep the set to the task. Those are the two actions that work under any of the four approaches.

The boundary of "30–50 tools" deserves separate attention, because it is more expensive than the monetary one. An overflowing context costs tokens, and that is visible in the bill. A drop in the accuracy of choice means the agent takes an unsuitable tool — that is visible in the result of the work, while the bill stays silent. A mistake with no line in the bill takes the longest to find.
