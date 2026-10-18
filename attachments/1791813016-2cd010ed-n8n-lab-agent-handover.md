# n8n training stand — agent hand-over sheet

Everything an agent needs to connect to the `n8n-lab` stand, in one page. Hand this over as-is.
Provisioned by `workain/infra`, `environments/n8n-lab` (issue #88); operations manual:
[`docs/n8n-lab.md`](n8n-lab.md).

## 1. Where it is

| | |
|---|---|
| URL | **`https://n8n.lessons.tellian.io/`** — live, Let's Encrypt cert, verified from outside |
| URL (always-works fallback) | `https://95-179-132-79.sslip.io/` — same stand, needs no DNS |
| n8n version | `2.42.7` (pinned image `n8nio/n8n:2.42.7`) |
| Public API | `n8n Public API 1.1.1` at `<base>/api/v1`, interactive docs at `<base>/api/v1/docs/` |
| Box | `vc2-2c-4gb` — 2 vCPU / 4 GB / 80 GB, Vultr Amsterdam |
| Open ports | 443 and 80 only (80 redirects). n8n's `5678` is bound to `127.0.0.1` and unreachable from outside |

Both hostnames stay valid once the switch is done — Caddy serves the primary name *and* the
`sslip.io` one, so nothing you configure against the sslip URL breaks.

## 2. The three values you need

| value | what it is | where it comes from |
|---|---|---|
| `N8N_API_KEY` | management-API key, sent as `X-N8N-API-KEY` | minted **only** in the UI: **Settings → n8n API → Create an API key**. Shown once |
| `N8N_MCP_URL` | the MCP endpoint of a published MCP-Server-Trigger workflow | `https://<host>/mcp/<path>` — created by `scripts/n8n-lab-agent-setup.sh` |
| `N8N_MCP_BEARER` | bearer token for that endpoint | generated (`openssl rand -hex 32`) and stored as an n8n `httpBearerAuth` credential by the same script |

```ini
# current values — rotate as described in §6
N8N_API_URL=https://n8n.lessons.tellian.io/api/v1
N8N_API_KEY=<PASTE: Settings → n8n API → Create an API key>
N8N_MCP_URL=<PASTE: printed by scripts/n8n-lab-agent-setup.sh>
N8N_MCP_BEARER=<PASTE: printed by scripts/n8n-lab-agent-setup.sh>
```

Nothing in `workain/infra` can mint the API key for you, and that is deliberate: this repo commits
`terraform.tfstate`, so any key it provisioned would be a key published to git history.

## 3. Path A — the agent DRIVES n8n (management API)

```bash
export N8N_API_URL=https://n8n.lessons.tellian.io/api/v1
export N8N_API_KEY=...

# list workflows
curl -fsS -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows" | jq '.data[] | {id, name, active}'

# create one (minimum body is {name, nodes, connections, settings} -- all four are required)
curl -fsS -X POST -H "X-N8N-API-KEY: $N8N_API_KEY" -H 'Content-Type: application/json' \
  "$N8N_API_URL/workflows" -d '{"name":"demo","nodes":[],"connections":{},"settings":{}}' | jq .id

# publish it (a workflow must be PUBLISHED for its production URL to exist -- in n8n 2.x
# /activate and /publish are the same operation; "active" alone is not enough)
curl -fsS -X POST -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows/<id>/publish" -d '{}'

# what ran, and what it returned
curl -fsS -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions?limit=5&includeData=true" | jq '.data[] | {id, workflowId, status}'
```

Useful endpoints (taken from this stand's own `GET /api/v1/openapi.yml`, not from memory):

- `GET|POST /workflows`, `GET|PUT|DELETE /workflows/{id}` (`PUT` takes `?publishIfActive=`)
- `POST /workflows/{id}/publish` · `/activate` · `/deactivate` · `/archive` · `/unarchive`
- `GET /workflows/{id}/history`, `GET /workflows/{id}/versions/{versionId}`
- `POST|GET /workflows/{id}/test-runs`, `POST /workflows/{id}/test-runs/{runId}/cancel`
- `GET /executions` (filters: `status`, `workflowId`, `startedAfter/Before`, `includeData`), `GET|DELETE /executions/{id}`
- `GET|POST /credentials`, `GET /credentials/schema/{credentialTypeName}`, `POST /credentials/{id}/test`
- `GET|POST /variables`, `GET|POST /projects`, `GET|POST /tags`

**One thing the API cannot do: run a workflow on demand.** There is no "execute" endpoint — the only
trigger-like call is `POST /workflows/{id}/test-runs` ("Trigger a test run"). To *invoke* logic from
an agent, give the workflow a **Webhook** trigger and call its URL (§5).

## 4. Path B — the agent USES n8n workflows as tools (MCP)

The stand exposes an MCP server per published workflow whose trigger is the **MCP Server Trigger**
node. Transport is streamable HTTP; auth is a bearer header.

```bash
# Claude Code
claude mcp add --transport http n8n-lab "$N8N_MCP_URL" \
  --header "Authorization: Bearer $N8N_MCP_BEARER"
```

```json
{
  "mcpServers": {
    "n8n-lab": {
      "type": "http",
      "url": "<N8N_MCP_URL>",
      "headers": { "Authorization": "Bearer <N8N_MCP_BEARER>" }
    }
  }
}
```

Verified live on 2026-10-12 against this stand (n8n 2.42.7) — the handshake, not just the HTTP code:
`initialize` → `protocolVersion 2025-06-18`, `serverInfo.name = MCP_Server_Trigger`; `tools/list` →
the attached tool; `tools/call` → the workflow ran and n8n recorded the execution as `success`.

Notes that save an hour of debugging:

- **Transport depends on the trigger node's `typeVersion`, and the default is the wrong one.**
  `typeVersion: 1` registers the legacy **SSE** transport — `GET /mcp/<path>/sse` plus
  `POST /mcp/<path>/messages` — and the bare path 404s with *"This webhook is not registered for
  POST requests"*. `typeVersion: 2` serves **streamable HTTP on the bare path** (`GET` and `POST`
  both 200), which is what `--transport http` and the current MCP spec expect. Measured both ways;
  `scripts/n8n-lab-agent-setup.sh` pins version 2. If you build the workflow by hand in the UI and
  a client cannot connect, check this first.
- A workflow has **two** MCP URLs: `/mcp-test/<path>` (only live while the editor is open) and
  `/mcp/<path>` (the real one, exists only once the workflow is **published**). Configure the
  production one.
- Each tool you attach to the trigger node becomes one MCP tool, named by that node. Changing the
  tool set changes what the agent sees — republish after editing.
- Auth failures are **`403`**, not `401`: both a missing and a wrong bearer token return 403.
- A bare `GET https://<host>/mcp` (no path) returns `200 text/html`. That is the SPA catch-all (a
  random path returns the same) — **not** evidence an MCP endpoint exists. Verify with a handshake.

## 5. Path C — the agent triggers business logic (webhook)

Add a **Webhook** node to a workflow, publish it, and the production URL is
`https://<host>/webhook/<path>` (`/webhook-test/<path>` while editing). Put **Header Auth** on the
node and pass that header from the agent — the stand is internet-facing, so an unauthenticated
webhook is open to anyone who guesses the path.

`WEBHOOK_URL` on the stand is set to its own public hostname, so the URL n8n shows you in the editor
is the real external one, not `localhost`.

## 6. Rotating or revoking

- **API key** — UI: Settings → n8n API, delete the key; create a new one. Nothing caches it.
- **MCP bearer** — UI: Credentials → `agent-mcp-bearer`, replace the token (or delete it and re-run
  `scripts/n8n-lab-agent-setup.sh`, which generates a fresh one). Clients must be updated.
- Both are per-stand, not per-agent: handing the same key to several agents means you cannot tell
  their actions apart in `GET /executions`. Mint one API key per agent if that matters.

## 7. Ground rules for an agent working on this stand

- **It is a training box and it is public.** Only n8n's own login protects the UI. Do not store real
  production credentials in workflows here.
- **No backups.** n8n's database is SQLite on the box's disk (`/opt/n8n-lab/n8n-data`). A reprovision
  destroys it. Treat anything built here as losable.
- **2 vCPU / 4 GB, with 2 GB of swap.** Fine for a class; a workflow fanning out hundreds of parallel
  executions will swap.
- **Logs**: `docker compose -f /opt/n8n-lab/docker-compose.yml logs -f` on the box;
  `n8n-lab-status` prints the URL, container state and both reachability checks.
- Changing the stand's hostname is `n8n-lab-set-host <name>` **on the box** — never a Terraform
  taint, which would destroy the database.
