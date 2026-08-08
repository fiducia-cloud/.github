# Fiducia Cloud desktop applications

Verified **2026-08-07**.

## Required pair

Fiducia Cloud is allocated two first-class desktop applications:

- Rust: [`fiducia-cloud/fiducia-desktop.rs`](https://github.com/fiducia-cloud/fiducia-desktop.rs) — **planned**, not yet verified as published.
- Flutter: [`fiducia-cloud/fiducia-flutter`](https://github.com/fiducia-cloud/fiducia-flutter) — **planned**, not yet verified as published.

Both repository names are allocation targets. Do not mark either implementation live until the remote, native build, packaging, tests, and supported-platform matrix are verified.

## Rust desktop kit: GPUI, fully native

The Rust application uses **GPUI**.

- Embedded WebViews are prohibited.
- React, JSX, and browser frontend stacks do not apply.
- Rust owns lock/lease/consensus/cron state, protocol validation, authentication, persistence, networking, telemetry aggregation, deep-link parsing, and privileged operations.
- GPUI owns native presentation, dense tables and timelines, keyboard navigation, virtualization, custom rendering, windowing, and low-latency interaction.
- OS-specific tray, notification, credential-store, single-instance, and URL activation behavior belongs behind narrow Rust platform adapters.

This choice prioritizes high-rate telemetry, deterministic rendering, low memory/CPU overhead, native security boundaries, and responsive incident/operator workflows.

The future Rust repository must contain `docs/DESKTOP_TOOLKIT.md` with the GPUI version policy, no-WebView rule, privilege boundaries, performance budgets, deep-link contract, native packaging matrix, and Flutter companion workflow.

## Why both Rust and Flutter remain active

The applications are developed side-by-side to compare native performance, security, dense operator UX, accessibility, platform integration, Flutter mobile/desktop reuse, developer velocity, release reliability, and long-term maintenance using the same product features.

Every desktop-facing feature must inspect both repositories, share acceptance criteria and fixtures, and normally update both. A one-sided change requires a documented no-change rationale, parity assessment, and follow-up work. Completion in only one repository is not full desktop completion.

The future `fiducia-desktop.rs` README, `AGENTS.md`, pull-request template, and `docs/DESKTOP_TOOLKIT.md` must state this parallel-development rule prominently.

## HTTPS-first deep links

Canonical route family:

```text
https://<verified-fiducia-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
fiducia://<route>?<bounded-query>
```

The production host must not be guessed. Rust and Flutter must consume the same versioned route types and golden fixtures from the Fiducia interfaces package.

Initial route families may include authenticated node views, lock/lease inspection, consensus groups, cron schedules, incidents, dashboards, and notification targets. No route is public until versioned and tested.

Required behavior:

- support cold start and already-running/single-instance delivery;
- validate the exact host, route version, node/company/resource identifiers, action, and bounded query values;
- preserve only a validated pending route through authentication;
- reject unknown routes, ambiguous encodings, unsafe return URLs, replayed handoffs, and unauthorized tenant/resource access;
- use short-lived, single-use, audience-bound codes for invitations or privileged handoffs;
- require confirmation before mutating locks, leases, schedules, membership, or failover state;
- provide browser fallback when the app is absent; and
- test macOS, Windows, Linux, Android, and iOS link behavior.

Passwords, bearer tokens, service tokens, private keys, tenant secrets, lock payloads, or other sensitive data must never appear in URLs.

## Shared product boundary

Both implementations should converge on compatible behavior for:

- company/tenant and role selection;
- node, shard, group, leader, lock, lease, vote, and cron inspection;
- real-time telemetry, alerts, incident timelines, and audit evidence;
- safe operator actions and confirmation flows;
- offline snapshots and reconnection;
- schemas, generated clients, route fixtures, simulation traces, and conformance tests.

## Project routing

- GitHub Project: [`fiducia-cloud-project` — Project 1](https://github.com/orgs/fiducia-cloud/projects/1)
- Linear project: `github.com/fiducia-cloud`
- Central private registry locator: `approved-private-registry` (opaque by policy; do not publish the backing repository name or URL here)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, toolkit changes, deep-link changes, renames, transfers, archival, or platform-status changes must update this document, Linear, the approved private registry, and both companion repositories together. Public documentation must keep the private registry locator opaque.
