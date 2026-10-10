---
id: n08
type: mechanics_map
duration_min: 1.25
assertion: "The agent runs on the user's machine; the server stands either on that same machine or at somebody else's — and the agent asks it the same way either way. It is the server that goes out to the external system, and it talks to that system in the system's own language: REST, gRPC, GraphQL, SQL"
learning_goal: "An introductory diagram ahead of the one-pager: it gives the picture in space — where the agent stands, where the server may stand, where the machine's boundary runs and where the request goes. The breakdown of the mechanics piece by piece comes next; here — only the placement and one conclusion: MCP is one and the same for the agent, and outward the server talks in the system's language"
visual:
  pattern: mechanics_with_figure
  figure: mcp-n08-gde-chto-stoit.png
  primary: "A diagram filling the slide. On the left a frame \"YOUR MACHINE\" — the agent is in it, and so is the first variant of the server; the arrow \"1 — MCP\" runs from the agent to the server inside the frame. The second arrow, \"2 — MCP over the network\", leaves the agent, crosses the machine's boundary and goes into a dashed frame \"SOMEBODY ELSE'S MACHINE\" with the second server in it. From each server an arrow \"request\" runs to the right, into the panel \"EXTERNAL SYSTEM\": four lines — the issue tracker, a database, a reporting mart, an internal service — and each with its own protocol mark (REST, SQL, GraphQL, gRPC). Under the diagram, two columns of general comments: who talks to whom and what comes back. At the bottom a gold bar: one server can go into several systems at once, into each in that system's own way, and the agent does not know those ways."
  backup: "Round 5 of the owner's edits (issue 225, ZADANIE-KRUG-5.md, verbatim): \"ahead of the mcp one-pager add a diagram slide marking the user's machine with the agent on it, and then the variants — the server on the machine and it goes into the external system, the server external and it goes into the external system. with some general comments on how mcp works. by the way show that it can go into different protocols at once — rest, grpc, graphql …\". The number is provisional — the running numbering is assigned by the round's consolidation.
    The source of the facts. The MCP specification, the page \"Architecture overview\" (modelcontextprotocol.io/docs/learn/architecture, accessed 2026-10-07), verbatim: \"MCP server refers to the program that serves context data, regardless of where it runs. MCP servers can execute locally or remotely\" — the server's two places are named by the specification itself, this is not an illustrative assumption. The same page on the conversation being the same regardless of place: \"The transport layer abstracts communication details from the protocol layer, enabling the same JSON-RPC 2.0 message format across all transport mechanisms\". The same page on the protocol not describing how the server obtains the data: \"MCP focuses solely on the protocol for context exchange\", while tools are defined as \"Executable functions that AI applications can invoke to perform actions (e.g., file operations, API calls, database queries)\" — hence the legitimacy of the four protocol marks on the diagram: REST, SQL, GraphQL, gRPC are named as the ordinary ways the systems themselves are asked, not as part of MCP. Confirmation that one and the same server exists in both places: the official GitHub server exists both remotely (hosted by GitHub, `https://api.githubcopilot.com/mcp/`) and as a local image (`ghcr.io/github/github-mcp-server`) — the README of the github/github-mcp-server repository, accessed 2026-10-07.
    What is deliberately NOT on the slide — checked line by line against n09 so as not to duplicate the one-pager: the names of the transports (stdio/http), the configuration file and the three scopes, capability discovery (tools/list), the format of a tool's full name, the three line items of the context's cost, the separate channel for the answer, and the call being signed with the server's name. The one deliberate overlap is a single line about the local server being brought up by the environment at the start of a session: without it the diagram does not answer \"who starts whom\", which the round's task named outright.
    The figure script is rendered/make_figures_mcp.py, function n08_gde_chto_stoit(). The canvas is 1600×760 px: at the slide's working width of 12.23″ that is 130.8 px/inch, and the smallest text on the diagram at 18 px is 9.9 pt against the deck's threshold of 7.5 pt. A 2400 px canvas (as on n09) would have given 6.6 pt on the same text — below the threshold, which is why the width was chosen before the first render rather than after the measurement."
---

# The server — at your place or outside, the conversation is the same

## Assertion

The agent runs on the user's machine. The server stands either on that same machine or at somebody else's — and the agent asks it the same way either way. It is the server that goes out to the external system, and it talks to that system in the system's own language: REST, gRPC, GraphQL, SQL.

## Visual

## Speaker notes

Before breaking the construction down piece by piece, it is worth looking at where everything stands. There is not a single new term on this diagram — only the placement of the figures in space; the mechanics come with the next screen.

The point of reference is your machine, the solid frame on the left. The agent runs on it: the one you talk to in a session. Everything else on the diagram is positioned relative to that frame, and the first thing worth finding on it is yourself.

**A server is a separate program** living outside the agent: somebody started it, it listens for what it is asked and it answers. It can be written in anything, it is installed like any other package, it crashes and restarts like any other program. One ability sets it apart — it talks MCP, that one shared conversation all of this was set up for.

That program has two places, and the protocol's specification says so outright: a server is a program that serves data, regardless of where it runs; it can run locally or remotely.

**The first place is the same machine,** next to the agent. Such a server is brought up by your environment at the start of a session: a command is written in the configuration, the command is executed, and the process lives as long as the session does. On the diagram it stands inside the solid frame, and the arrow to it does not cross that frame.

**The second place is somebody else's machine.** The server there is already running, somebody else keeps it and updates it, and you connect to it over the network. On the diagram it is in a dashed frame, and the arrow to it does cross the boundary of your machine. Dashed against solid is the whole visible difference: solid is yours, dashed is somebody else's.

The agent's conversation with the server is the same in both cases; the only thing that changes is the route to the server — a process next door or the network. The specification puts it this way: the transport layer hides the details of the connection from the protocol layer, and one and the same message format works across all means of delivery. That is why the numbers of the variants stand on the arrows on the diagram: a variant is a route, and in both variants the agent is the same and stands in the same place.

On the right is the external system: the issue tracker, a database, a reporting mart, an internal service. It is the server that goes there. The key to the system is held by the server; it does not hand the key to the agent, and what the agent gets back is the text of the answer, never touching the system itself. That placement is easiest to see on a diagram and hardest to reconstruct from a configuration file — which is why the picture comes before the file.

And now what the diagram was drawn for in the first place. Every system has its own way of being asked: the issue tracker over REST, the database in the SQL language, the reporting mart through GraphQL, the internal service over gRPC. The server is what talks in those ways. The systems existed before MCP and had had their own ways of being asked for a long time; the server is a wrapper on top of them: inward it accepts a call over MCP, outward it reaches out the way the system can manage. One server can go into several systems at once, into each in that system's own way. The agent does not know those ways, and it does not need to: with any server it has one conversation.

The protocol does not describe what is behind the server at all — it describes only the agent's conversation with the server. Tools in the specification are defined as executable functions an application can invoke in order to do something: file operations, API calls, database queries. Hence the four marks on the right-hand side of the diagram; they stand there as the ways the systems themselves are asked.

The server, meanwhile, is not obliged to go outside at all. A server for the file system or for a local database does not reach anywhere over the network — it simply gives the agent operations over what lies next door. The external system is on the diagram because our case is exactly that kind: the tracker lives apart from the project.

One and the same server not infrequently exists in both places at once. The official GitHub server exists remotely — hosted by GitHub itself — and as an image that runs on your machine. The operations in them are the same, what differs is the place. Which of the two variants to take is not something the diagram decides: the case itself breaks the choice down, and the cost of each is counted there.

By the conversation, the agent sees no difference between the variants. Where the server stands can only be seen from the record in the configuration — and for permissions and secrets that difference is a large one: in one case the key lies in the environment of a process on your machine, in the other you hand it to whoever keeps the service.
