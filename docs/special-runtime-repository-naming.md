# Special runtime repository naming

The standard application topology remains public web, public API, admin web and admin API. Extra long-running runtimes require a real deployment boundary and should use role names that communicate that boundary.

Preferred suffixes:

- `*-node.rs` — distributed state/consensus member;
- `*-brain.rs` — global control/reconciliation plane;
- `*-daemon.rs` — persistent local/background agent;
- `*-worker.rs` — long-running queued executor;
- `*-runner.rs` — privileged build/migration execution;
- `*-gateway.rs` — special protocol/device/agent gateway;
- `*-relay-server.rs` — opaque or realtime connection relay;
- `*-ingest-server.rs` — high-volume streaming ingest;
- `*-collector.rs` — telemetry/event collector;
- `*-sidecar.rs` — colocated auxiliary process;
- `*-mcp-server.rs` — MCP protocol boundary.

Avoid generic `*-foo-server.rs` names when the role can be expressed by one of these lifecycle/deployment categories. A special suffix does not itself authorize a new runtime; the repository still must document its trust, protocol, placement, state-machine, resource or fault-containment reason.

Business-domain nouns such as billing, users, reports, projects or messages normally remain modules inside the four application planes. Scheduled/retryable/bursty work belongs in `*-lambdas` unless it needs a persistent runtime lifecycle.

When `ores-cli` audits an organization, these names should be treated as documented special-runtime exceptions rather than standard-family members. New exceptions should include an ADR and exact-head evidence before being added to a monorepo as deployable submodules.
