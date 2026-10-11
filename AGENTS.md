# Working directory conventions

This directory is this session's own project working directory -- the place a human operator will
look for anything you produce here.

- Save any file you're asked to create, or any deliverable/output the operator should be able to
  find later, INSIDE this directory (or a subdirectory of it) -- not in `/tmp`, a scratchpad
  directory, or any other path outside this project.
- A "use a scratchpad/temp directory for temporary files" instruction you may have from your own
  system prompt is about disposable, intermediate working files only. A finished result the
  operator asked you to produce and keep is not a temporary file, even if you used a scratch
  directory to build it -- copy or write the final version here before reporting it done.
- If you dispatch a subagent (a Task/Agent tool or similar) to do this kind of work on your behalf,
  pass this same instruction on to it explicitly -- it does not automatically inherit this file in
  every provider/tool.
- If a `GIT_LINK.md` file exists in this directory, read it -- it has this folder's git repo link
  and current authentication status (harness-control#306). If it doesn't exist, this directory has
  no git repo linked through the fleet-control UI (it may still be a plain git clone on its own).

## Notifying a supervisor/dispatcher terminal (if you were launched as a worker)

If you were dispatched by another terminal (e.g. via CAO's own `assign`/`handoff`) and need to
report back to it, use `mcp__harness-control-mcp-server__send_message` with its session id -- NOT
a generic `SendMessage` tool your own CLI may also expose. That generic tool only reaches a
background agent YOU YOURSELF spawned via your own native Task/Agent tool (tracked by an agentId
from that spawn) -- it has no way to reach a separate terminal/process like the one that dispatched
you, and fails with a plausible-sounding "not reachable" error that gives no hint you picked the
wrong tool. If the first attempt fails this way, that is the signal to switch to
`mcp__harness-control-mcp-server__send_message` instead of giving up -- it works regardless of
whether you or your dispatcher are a CAO-hosted or a native session, unlike CAO's own retired
`send_message` tool (harness-control#1004).
