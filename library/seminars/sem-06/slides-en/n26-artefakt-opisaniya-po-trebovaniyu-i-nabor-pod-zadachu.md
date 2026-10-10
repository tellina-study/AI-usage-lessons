---
id: n26
type: code_artifact
duration_min: 1.25
assertion: "Four lines of the decision: the server in the project file has no flag forcing definitions to load, deferred loading is not switched off in the environment, only the toolsets needed are passed to the server, and he keeps his own set of servers in the personal scope"
learning_goal: "The artifact of the third case: checking the loading mode of the definitions, choosing toolsets on the server's side, and dividing the set of servers between the project and the personal scope. The first two lines are a check on what is already on by default; the fourth is the only one that requires work. Here it is also shown that a particular server's flag for on-demand issuing may have been removed by its author: what has to be checked is the current version, not the result of a search"
visual:
  pattern: code_artifact
  primary: "Four items on a light card with inline code: the removed flag forcing loading on the server, the value of the deferred-loading variable in the environment, the choice of toolsets in the server's start-up command, the personal scope for one's own set of servers. Under them — a summary formula about what is settled by what."
  backup: "Source — rework/section-1-mcp-part1b.md §A.3.6, §B.26 (part1e.md). Round 5 (issue 225): the artifact was written anew for the replacement of the case; the previous one (pinning the package version plus a record of the check in the decision log) was removed along with the case.
    The owner, round 5: \"show the do-not-load-at-once flag on the server, so as to get definitions from the server only when they are really needed\". The flag is shown from three sides, all three read in the primary sources: the field alwaysLoad: true on a particular server in the project file cancels the deferral forcibly (sem-05/research/mechanics-5-mcp.md §2.3, the documentation, accessed 2026-09-27; the cost is named there too — \"each upfront tool consumes context that would otherwise be available for your conversation\"); the ENABLE_TOOL_SEARCH variable governs the deferral as a whole, including a threshold value of the form auto:10; the --toolsets flag on the side of the server itself hands over only the sets chosen — GitHub's official server names the purpose outright: \"Enabling only the toolsets that you need can help the LLM with tool choice and reduce the context size\" (raw.githubusercontent.com/github/github-mcp-server/main/README.md, read 2026-10-07). At the level of the model's protocol the same technique is called defer_loading: true on a particular definition (docs.claude.com, tool search tool) — it is not brought onto the slide, as it is not a setting on the connecting side.
    The fourth line rests on the scopes from the first case (n14) and introduces nothing new about them: there the choice was where to keep the key, here it is where to keep the set of servers.
    The caveat about the removed flag rests on a verified case: --dynamic-toolsets and GITHUB_DYNAMIC_TOOLSETS on that same GitHub server existed up to and including v1.0.0 (in the README of v1.0.0 the word dynamic appears 11 times, together with GITHUB_DYNAMIC_TOOLSETS=1) and were deleted in v1.1.0; pull request github/github-mcp-server#2512 \"refactor: remove dynamic toolsets and deprecated closure constructor\", SamMorrowDrums, created and merged 2026-05-20, 24 files, +51/−942; in the current README there is not one instance of the word dynamic, nor is there in the code. The reason named by the author of the PR is \"tech debt cleanup\" and \"Dynamic mode was local-only — never offered by the remote server\", that is, there is no conclusion \"the idea does not work\" in the PR and it must not be imputed to it. Verified twice: research/mcp-kontekst-otkaz.md §4 and an independent repeat pass by the session's orchestrator (the pull request's API and the README at the tags).
    Rule A4 holds: there is no dark monospaced card on the slide, and the code runs inline on a light background."
---

# Definitions — on demand. The set — for the task

## Assertion

Four lines of the decision: the server in the project file has no flag forcing definitions to load, deferred loading is not switched off in the environment, only the toolsets needed are passed to the server, and he keeps his own set of servers in the personal scope.

## Visual

- `.mcp.json`: `alwaysLoad: true` has been removed from the server — the definitions of its tools arrive on demand. The flag is left on one tool that is needed at every step, and the reason why is written down next to it.
- The project's environment: `ENABLE_TOOL_SEARCH` is not set to `false`. A threshold value of the form `auto:10` is a compromise: while the definitions take up less than the named share of the context, they are loaded at once.
- The server's start-up command: only the toolsets needed — `--toolsets repos,issues` instead of the full set. Check the flags against the server's current version: GitHub's official server had a mode for issuing sets on demand and it was removed in May 2026.
- The personal connection scope: servers for your own work go there. The shared project file stays the team's, and nobody throws the other person's three servers out of it.

> The project file says what is connected for everybody. The personal scope says what is connected for you. The loading mode of the definitions settles what that costs before the first question.

## Speaker notes

Four lines of the decision, and the first two are a check; they change no settings.

The first. In the connection file `.mcp.json`, `alwaysLoad: true` has been removed from two servers: the definitions of their tools arrive on demand again. The flag has a legitimate use, and banning it altogether would be unreasonable — a tool that is needed at literally every step is cheaper to describe once at start-up than to pull its schema in before every call. So the flag is left on one such tool, and next to it is written down which one and why. An exception with no reason written down is, a month later, indistinguishable from an accidental line, and the next person will either wipe it out blindly or be afraid to touch it.

The second. In the project's environment, `ENABLE_TOOL_SEARCH` is not set to `false`. This is a check on one value, and it costs a minute. A threshold value of the form `auto:10` is a sensible compromise for those who care about the speed of the first call: while the definitions take up less than the named share of the context, they are loaded at once, and once the threshold is reached they go into deferral.

The third line lives on the side of the server itself. In the start-up command, only the toolsets needed are passed: `--toolsets repos,issues` instead of the full set. GitHub's official server explains the purpose of that flag in its own words: enabling only the sets you need helps the model with tool choice and reduces the size of the context. A server that can hand over its tools in sets removes part of the cost before it reaches the client.

Here too is the caveat about how fresh the flags are, and this is a verified case with the number of a change request and a date. That same GitHub server had a mode for issuing sets on demand: the flag `--dynamic-toolsets`, the environment variable `GITHUB_DYNAMIC_TOOLSETS` and three service tools for listing and enabling sets. In the description of version 1.0.0 the word `dynamic` occurs eleven times; starting with version 1.1.0 — not once, and it is not in the code either. The mode was deleted by a single change request in May 2026: twenty-four files, fifty-one lines added, nine hundred and forty-two removed. The reason named by the author is maintenance debt and the fact that the mode worked only locally — the remote server never offered it. There is no conclusion "the idea does not work" in the request, and it must not be imputed to it.

The lesson from that caveat is a general one, and it is about the ordinary fate of a flag. A search still returns the page for the previous version, it reads as current instructions, and there is no way to tell it from current ones by its look. It is checked in one way: open the description of the server's current version and find the flag there.

The fourth line is the only one that requires work. The servers for one's own personal work are moved into the personal connection scope: the same user settings file that was broken down when the choice was where to put the key. The project file stays the team's, and nobody throws the other person's servers out of it. Keeping everything in the project file is simpler while everybody's sets coincide; the moment the work diverges, the shared file charges each person for all the kinds of work at once — exactly what happened in the scene.

In the scene everything was arranged the other way round: the flag was set, one person set it, and everyone who opened a session paid.
