---
id: n16
type: code_artifact
duration_min: 1.5
assertion: "The result of the conversation is a file with four lines of substance: the server's name, what starts it, what gets started, where the key comes from; outside the file but no less important — what permissions that key has; and if the server's name coincides in two configuration scopes at once, the more personal scope wins, with the organization's policy above all six"
learning_goal: "The artifact of the decision from the two co-buildings, broken down line by line — not the fragment already seen on the one-pager (n09), but the full version with an explanation of every line. With the mechanics of the three configuration scopes and the order of precedence. Named honestly as the target decision, not confirmed by a commit. Round 2 of the owner's edits (issue 225): more detail on the structure of the file, a line-by-line explanation; two specific confusions were fixed — the \"identical addresses\" on the precedence diagram and the mention of the server crashing"
visual:
  pattern: code_artifact
  figure: mcp-n16-prioritet.png
  primary: "The code of the .mcp.json file on a light field, with every line captioned through an arrow saying what it means. Below — the diagram of precedence on a clash of names (six rungs, with the file's location on each; the local and user rungs explicitly explained as one and the same physical record, different places inside it)."
  backup: "Source — rework/section-1-mcp.md §A.1.8 (rewritten), §B.8 (part1c.md, rewritten). The honest gap — this is the section's target decision, taken from an earlier capture of the demo repository; there is no commit with it in the current branch of the demo project, and there is no such file in the course's repository either (§A.00, named once for the whole section).
    Round 2 of the owner's edits (issue 225): the slide was expanded (1.25→1.5 min) — a
    line-by-line explanation of every key in the file instead of one general caption, \"four lines
    of substance\"; n09 shows a fragment of this same template, and here is the full version with a
    breakdown.
    The precedence diagram (mcp-n16-prioritet.png) was edited — the local/user rungs are captioned
    explicitly as one physical record, ~/.claude.json, with different keys inside it, rather than
    two similar addresses (sem-05/research/mechanics-5-mcp.md §1.2), plus a separate explanatory
    line at the bottom of the diagram.
    The crash of the stdio process — one sentence here, as an honest reminder that the command
    starts a live process; what is visible from outside when it does is on the next screen (n17).
    The visual session (issue 225, round 1): the table \"Scope · Physically · Precedence\" (3 rows)
    was replaced by a vertical ladder of precedence — all six rungs (personal → project → general
    personal → plugin → connector → the organization's policy), with the physical file captioned on
    each.
    The second roast (issue 225, P2 — \"n16 runs two different pieces of business, and only one of
    them is named in the title\"): the title and the assertion named only the line-by-line breakdown
    of the file, even though the bottom third of the slide is a second topic, precedence on a
    coincidence of server names. The title was extended with the short phrase \"and the order on a
    clash of names\", and the assertion with the victory of the more personal scope (\"the
    organization's policy is above all six\") — the five-second test now covers both pieces of the
    slide's business, not only the upper two thirds. The title was left short (not \"who wins when
    the name coincides…\", the first version of the edit) — the longer variant squeezed the title's
    point size and crowded the precedence diagram lower (measured by build_sem06.py: \"DIAGRAM
    SQUEEZED\" + \"AT THE BOTTOM OF THE POINT SIZE\" appeared at full length and disappeared at the
    short one). The facts about the order of the rungs did not change."
---

# The assembled file — and the order on a clash of names

## Assertion

The result of the conversation is a file with four lines of substance: the server's name, what starts it, what gets started, where the key comes from. Outside the file but no less important — what permissions that key has: one repository, not the whole account. And if the same server name is declared in two configuration scopes at once, the more personal scope wins, while the organization's policy stands above all six.

## Visual

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PAT}" }
    }
  }
}
```

- `mcpServers` — the root: all the servers of this scope. `"github"` — the server's name: it is the name the agent calls the tools under, `mcp__github__…`.
- `"command"` and `"args"` — what starts it and what exactly gets started: the server's own package.
- `"env"` — the process's environment; `${GITHUB_PAT}` is a substitution, not the secret itself.

## Speaker notes

The result of the conversation is a file with four lines of substance. Each answers a question of its own.

`mcpServers` — the root: the list of all servers declared in this scope. One file can hold several servers, and each gets a record of its own.

`"github"` — the server's name. It is under this name that the agent will call its tools: `mcp__github__…`. You choose the name, and it ends up in every place the server is referred to — in the permission rules, in tool lists, in the output of a call. Renaming it later means walking through all of those places.

`"command"` — what starts it: the specific launcher program, here `npx`. `"args"` — what gets started: the server's own package. Together those two lines are that command which will be executed at the start of a session.

`"env"` — the environment variables for the process. The value here is the substitution `${GITHUB_PAT}`; the secret itself does not lie in the file as text.

This key's permissions do not enter the file at all, and that is worth keeping in mind while looking at the screen. One repository instead of the whole account is a decision taken on the service's side, where the token was created; it is not visible from the configuration and cannot be caught in review by this file. The file shows where the key comes from and says nothing about what can be done with that key.

About the file itself: it lies in the root of the repository and is visible to everyone who clones the project. The personal and general personal scopes live in a separate file outside the repository — secrets do not get from there into the code simply because the file is physically not in the git tree.

This command starts a live process on your machine. If it crashes in the middle of a session, it will not restart by itself — a new session is needed. What is visible from outside when it does, and why the green marker says nothing about it, is on the next screen.

The precedence diagram under the file answers the question that arises when one and the same server name is declared twice. Six rungs, and the physical file is captioned on each. The `local` and `user` rungs are both captioned with the file `~/.claude.json` — the same construction and the same reason as on the MCP one-pager: one physical file, two records inside it. On a clash of names those are records of different weight, despite the shared file.

There are exactly three scopes, and that number is not an arbitrary setting: three hard-coded places are exactly what the product can do. Changing the scope of a server that is already connected means rewriting the same record in another place; the token's permissions meanwhile stay as they were, and they are changed where the token was created.

And the honest gap, which is worth naming outright. This file is the section's target decision, assembled from an earlier capture of the demonstration repository. There is no commit with it in the current branch, and there is no such file in the course's repository either. The breakdown rests on the evidence base of the research, with no live commit behind it; the same goes for the next two cases of this section — that gap is common to them. The screen shows the example being broken down and promises no "clone it and repeat".
