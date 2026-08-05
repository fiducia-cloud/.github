# Fiducia Cloud repository map

Snapshot date: **2026-08-05**  
Canonical GitHub organization: [`fiducia-cloud`](https://github.com/fiducia-cloud)  
Canonical GitHub Project: [`fiducia-cloud-project`](https://github.com/orgs/fiducia-cloud/projects/1)  
Canonical Linear project: [`fiducia-cloud`](https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3)

## Scope and interpretation

This document classifies the **34 repositories visible to the connected organization installation** into routing workstreams. There are **33 active repositories** and **1 archived repository**.

A routing category describes where planning and review should be coordinated. It is not evidence that a repository is implemented, deployed, released, secure, maintained, or production-ready. Those claims require repository-specific tests, releases, deployment evidence, and runtime observations.

The exact inventory, visibility, archive state, default branch, and category are maintained in [`repository-map.json`](./repository-map.json) and validated in CI.

## Organization governance

| Repository | Visibility | State | Routing role |
| --- | --- | --- | --- |
| `.github` | Public | Active | Organization policy, community health, project routing, and portfolio documentation |

## Sites

| Repository | Visibility | State | Routing role |
| --- | --- | --- | --- |
| `fiducia-cloud.github.io` | Public | Active | Organization site routing |
| `fiducia-marketing.web` | Public | Active | Marketing-site routing |
| `fiducia-customer-ui.web` | Public | **Archived** | Historical customer UI; no new active work should be routed here without an explicit unarchive decision |

## Core runtime

| Repository | Visibility | State |
| --- | --- | --- |
| `fiducia-brain.rs` | Public | Active |
| `fiducia-edge` | Public | Active |
| `fiducia-load-balance.rs` | Public | Active |
| `fiducia-node-sidecar.rs` | Public | Active |
| `fiducia-node.rs` | Public | Active |
| `fiducia-routing.rs` | Public | Active |

## Platform services

| Repository | Visibility | State |
| --- | --- | --- |
| `fiducia-admin.rs` | Public | Active |
| `fiducia-auth.rs` | Public | Active |
| `fiducia-customer.rs` | Public | Active |
| `fiducia-lambda-service.rs` | Public | Active |
| `fiducia-memory` | Public | Active |
| `fiducia-memory.rs` | Public | Active |
| `fiducia-messaging` | Public | Active |
| `fiducia-messaging.rs` | Public | Active |
| `fiducia-payments.rs` | Public | Active |
| `fiducia-telemetry.rs` | Public | Active |

The paired names `fiducia-memory` / `fiducia-memory.rs` and `fiducia-messaging` / `fiducia-messaging.rs` are inventory facts, not evidence that the pairs are redundant. Any consolidation requires an explicit history, API, release, and deployment comparison.

## Agent and operations control planes

| Repository | Visibility | State |
| --- | --- | --- |
| `fiducia-ai-agent-bridge.rs` | Private | Active |
| `fiducia-ai-agent-control-plane` | Private | Active |
| `fiducia-ai-agent-coordinator.rs` | Private | Active |
| `fiducia-ai-agent-manager.rs` | Public | Active |
| `fiducia-operations-control-plane` | Private | Active |

## Interfaces and tooling

| Repository | Visibility | State |
| --- | --- | --- |
| `fiducia-cli.rs` | Public | Active |
| `fiducia-clients` | Public | Active |
| `fiducia-interfaces` | Public | Active |
| `fiducia-mcp-server.rs` | Public | Active |
| `fiducia-monorepo` | Public | Active |
| `fiducia-sync` | Public | Active |

## Infrastructure and independent validation

| Repository | Visibility | State |
| --- | --- | --- |
| `fiducia-e2e` | Private | Active |
| `fiducia-infra` | Public | Active |
| `fiducia-test-config` | Public | Active |

## Routing rules

- Create product and portfolio planning in the shared `fiducia-cloud` Linear project, not in repository-local prose or a parallel test-only backlog.
- Add durable production engineering issues and pull requests to the production organization GitHub Project; route independent certification to the test-fleet GitHub Project.
- Route cross-repository behavior through the narrowest owning workstream; do not create another repository merely to avoid resolving an ownership boundary.
- Keep independent end-to-end evidence in `fiducia-e2e`, `fiducia-cloud-test`, or another explicitly designated test repository rather than allowing a production repository to self-certify every external contract.
- Treat archived repositories as read-only history unless an explicit issue records the reason, owner, migration impact, and unarchive decision.
- Store no secrets, mailbox bodies, portal credentials, payment details, or private company attestations in this public map.

## Updating the snapshot

1. Re-query the connected GitHub organization inventory.
2. Reconcile additions, removals, visibility changes, archive state, and default branches.
3. Update `repository-map.json` in sorted repository-name order.
4. Update this routing view only when a category or explanatory boundary changes.
5. Run:

```bash
python3 tools/validate_repository_map.py
python3 -m unittest discover -s tests -p 'test_repository_map.py' -v
```

6. Open a pull request linked to the corresponding Linear issue and merge only after checks pass.
