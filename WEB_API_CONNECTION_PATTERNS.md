# Fiducia Cloud web/API connection patterns

Status: organization architecture guidance, tracked by [DEN-4263](https://linear.app/denman/issue/DEN-4263/document-fiducia-cloud-webapi-connection-patterns).

## Scope exclusion

This guidance applies only to traditional customer/admin web/BFF, API, control-plane, billing, and background services. It **does not apply to `fiducia-brain.rs` or `fiducia-node.rs`**. Those components retain their own protocol, trust, safety, and architecture decisions and must not inherit exceptions from this document.

## Four supported avenues for traditional services

| Avenue | Appropriate use | Boundary |
| --- | --- | --- |
| Direct database read | Named, stable, non-sensitive public/reference or control-plane read projection with a measured need | Never identity, credentials, tenant-private state, billing, authorization, node/brain state, or writes; require distinct `SELECT`-only, `READ ONLY`, non-owner, `NOBYPASSRLS` access |
| Stateless HTTP/JSON | Default synchronous web-to-API path | Required for customer-private reads, control-plane commands, administration, billing, and every mutation |
| Stateful TCP | Measured traditional-service subscription or high-frequency status stream | Not an authorization, persistence, command, or billing authority; require ADR, mTLS/delegated identity, bounded frames, deadlines, backpressure, and reconnect policy |
| NATS/message queue | Durable post-commit effects, fan-out, notifications, and reconciliation work | Never login, authorization, billing approval, control-plane command acknowledgement, or immediate response; require transactional outbox and idempotent consumers |

HTTP is the default for traditional services. Direct reads, TCP streams, and messaging are specific reviewed exceptions, not general substitutes.

## Decision and ownership

1. Tenant-private data, product authorization, control-plane commands, billing, and all mutations use HTTP.
2. Immediate authoritative answers use HTTP with typed/versioned interfaces, bounded bodies/timeouts, correlation context, and idempotency.
3. Durable post-commit effects publish from a transactional outbox to NATS.
4. A measured traditional-service stream may use TCP after an ADR and API authorization.
5. Direct reads remain limited to named safe projections under a dedicated restricted role.

The traditional web/BFF owns HTML, opaque secure sessions, CSRF, and authorization-code plus PKCE. The traditional API owns product authorization, commands, and state transitions. A core/data package owns typed mappings and query helpers. The canonical migration repository owns DDL; application services verify schema compatibility and do not migrate production at boot.

Shared Auth proves identity and session assurance, not Fiducia Cloud tenant or product permission. Validate realm, issuer, audience, tenant, app/client, scopes, session, freshness, and assurance. Protected introspection authenticates the service independently while carrying the user's token only in the body. Never log bearer tokens, cookies, authorization codes, PKCE verifiers, credentials, billing data, or raw introspection results.

Use immutable dependency revisions. `opto-sync` may implement only declared synchronization/outbox workflows, `ores-otel` provides bounded redacted telemetry, and `zed-pkg` records dependency provenance. These tools do not relocate authorization or data ownership.

## Operational requirements

- Bound HTTP bodies, TCP frames, deadlines, retries, queues, and buffers; propagate correlation and trace context.
- Require mutation idempotency and duplicate-safe message consumers.
- Fail closed; never replace failed API authorization with a direct read.
- Record an owner and review/expiry date for each direct-read or TCP exception.
- Code comments identify the selected avenue and why its traditional-service constraints are satisfied.

Again, this policy intentionally excludes `fiducia-brain.rs` and `fiducia-node.rs`.
