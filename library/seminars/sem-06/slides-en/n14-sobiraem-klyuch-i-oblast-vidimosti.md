---
id: n14
type: cobuilding
duration_min: 1.25
assertion: "The key is kept in an environment variable, not in a file; the configuration's scope is one of three, and the default of the connect command puts the server somewhere other than where many people expect"
learning_goal: "Co-building, part 2 of two: the third and fourth moves — where to keep the key, and which scope to put the configuration file in. The command's default is named explicitly, so as to clear up the typical confusion of \"it works for me — it does not for you\". Round 2 of the owner's edits (issue 225, part A3): the word \"barrier\" was removed from the title"
visual:
  pattern: cobuilding_config_reveal
  figure: mcp-n14-oblasti.png
  primary: "Two moves on one screen. Move 3 — the key in an environment variable. Move 4 — the three scopes of the configuration with a mark on which is for what and which is the default of the connect command."
  backup: "Source — rework/section-1-mcp.md §A.1.7 (part 2), §B.7 (part1c.md). The order of precedence of the scopes and the physical files are carried over to the next slide together with the .mcp.json artifact.
    The visual session (issue 225): the table \"Scope · When it is appropriate\" was replaced by a
    layered diagram (rendered/make_figures_mcp.py) — the three scopes in a stack of cards, the
    local default marked in gold, and the closing caveat about the \"it works for me\" divergence
    moved into the diagram in full. The markdown body of Visual was left empty by the same
    convention as on n31/n48: the visual content lives in the diagram.
    The storytelling revision (issue 225): the slide was not edited substantively — two breakdowns
    were added to the reference material (why a configuration belongs in the repository; what to do
    with an experiment that has taken root). The slot, the screen, the diagram and the speech are
    as before."
---

# We settle it: where to keep the key and which scope to put the file in

## Assertion

The key is kept in an environment variable, not in a file. The configuration's scope is one of three, and the default of the connect command puts the server somewhere other than where many people expect.

## Visual

## Speaker notes

The third move is about the key, and the answer to it is named almost at once: the key is kept in an environment variable, and the value is not written into the file.

The reason for that is not a stylistic one. The mechanics of the configuration here are executable: the command that connects the server genuinely runs on the machine at the start of a session, it does not remain a mere description. A value written literally into the command would become part of what is physically executed — and would travel along with the file into the repository, into the commit history, into review, into any export of the project. The environment variable is a direct consequence of that fact.

An honest caveat to the practice: moving a secret out into an environment variable does not guarantee it will not surface as text somewhere. The diagnostic command used to check the status of a connection can itself turn out to be one more leak channel for that same secret. That does not cancel the practice, but it takes away the false sense of complete protection: an environment variable removes the secret from the file and does not remove it from every possible place.

The fourth move is the configuration's scope, and there are three variants: only on this machine of mine; into the repository, for everyone; globally across all my projects. A server that has been checked goes into the repository — the configuration then becomes code, and a change to it is visible in review on a par with code. A new server appears in the project together with a discussion, and it is visible before it starts working. An experiment that has not been checked stays only at your own place.

And a fact about the default worth knowing before the first connection: by default the connect command puts the server into the personal configuration, not into the project. Not knowing that, it is easy to end up in the conversation "I connected it, everything works" — "well, not for me", in which both are right: the record exists, and one person sees it.

An experiment that has taken root is moved from the personal scope into the project's one by the same conversation you use to bring any other edit into the repository. The key's permissions stay as they were in the move: they are changed on the service's side, where the key was created.

The choice of scope is a decision about visibility, and it is worth measuring with one question: who is supposed to break if the connection disappears? If the team's work stops without that server, the record has to lie in the repository — then its disappearance is visible in review and is restored the same way as any other edit to a file. If the only thing that stops without the server is your personal experiment, then a record in the repository will get in everyone else's way: they clone the project and receive a process they did not ask for, along with a demand for a key they do not have.

Separately — what happens when names coincide. If one and the same server name is declared in two scopes, the whole record of the higher-precedence scope wins in its entirety; fields from different sources are not merged together. The case people get caught by: the personal record has no key in it, the project's one does, the names coincided — in a conflict you get the personal record in its entirety, together with the missing key, and the server does not work for a reason that is not visible in the project file. The order of precedence: the personal scope is above the project's, the project's is above the general personal one, then comes a server from a plugin, then a connector, and above all of them the organization's policy, if there is one.
