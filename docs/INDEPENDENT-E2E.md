# Independent E2E and release-certification responsibilities

Audit date: 2026-08-05

This organization and [`fiducia-cloud-test`](https://github.com/fiducia-cloud-test) share one planning project: [fiducia-cloud](https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3). They deliberately keep separate GitHub Project #1 boards and separate repository ownership boundaries.

- Production execution board: https://github.com/orgs/fiducia-cloud/projects/1
- Independent acceptance board: https://github.com/orgs/fiducia-cloud-test/projects/1
- Program issue: [DEN-2353](https://linear.app/denman/issue/DEN-2353/e2e-program-certify-every-fiducia-production-surface-through)
- Program plan: [Everything E2E — Full-System Test Program](https://linear.app/denman/document/everything-e2e-full-system-test-program-57e84c9eb677)
- Machine-readable test catalog: https://github.com/fiducia-cloud-test/.github/blob/main/test-program/catalog.json

## Production repository contract

Every active production repository owns:

1. unit, component, schema/serialization, migration, and deterministic fault tests appropriate to its boundary;
2. reproducible build and package/OCI publication;
3. exact source SHA, package version, OCI digest, interface/schema version, migration set, and feature-gate identity;
4. a documented test-impact statement when behavior or contracts change;
5. local fixtures or stable test interfaces that do not require independent probes to import private implementation details;
6. observability and cleanup behavior needed to diagnose and safely tear down E2E runs; and
7. links from the production GitHub Project item to the canonical Linear issue and independent acceptance evidence.

A production test should be as white-box as useful. The independent probe must remain black-box: it consumes a released or immutably pinned artifact and public/trusted test contracts rather than reaching into private modules.

## Cross-system ownership

### `fiducia-e2e`

`fiducia-cloud/fiducia-e2e` is the canonical orchestration and shared assertion engine. It already documents real HTTP conformance, disposable local web/auth composition, a real three-node Raft system, real-browser journeys, three independent local clusters, chaos, and strict Hetzner proof/attestation.

It should provide reusable libraries and executable reference journeys without absorbing all independent repository ownership. Specialized probes may reuse versioned orchestration/assertion packages or invoke documented modes, but they retain their own narrow acceptance responsibility and evidence.

### `fiducia-test-config`

`fiducia-cloud/fiducia-test-config` owns shared test infrastructure: environment/topology schemas, process lifecycle, deterministic fixtures and seeds, retry/time budgets, cleanup, redaction, JUnit/evidence writers, and local/CI parity utilities. It must publish versioned or immutable consumable artifacts.

### `fiducia-interfaces` and `fiducia-clients`

These repositories own the canonical wire/interface definitions, generated clients, compatibility policy, examples, and shared contract fixtures. Independent language and clean-consumer repositories prove that published artifacts—not monorepo-relative imports—install and behave correctly.

### `fiducia-infra`

Infrastructure owns disposable and provider-backed topology creation, provider/Kubernetes/member identity, network-failure hooks, image deployment by digest, backup/restore/rollback mechanisms, cleanup, and proof inputs. Application-level E2E owns semantic assertions against that topology.

## Production-to-acceptance routing

| Production domain | Primary repositories | Independent acceptance |
|---|---|---|
| API, consensus, routing, coordination | `fiducia-node.rs`, `fiducia-brain.rs`, `fiducia-routing.rs`, `fiducia-load-balance.rs`, `fiducia-infra` | API, Raft/chaos, locks/leases/fencing, semaphore/rate-limit, idempotency, cron, routing/election, discovery, and multi-cloud suites |
| Identity, admin, customer, edge | `fiducia-auth.rs`, `fiducia-admin.rs`, `fiducia-customer.rs`, `fiducia-edge`, sidecar and web/site repos | tenant-isolation, control-plane, edge-partition, telemetry, and real-browser `fiducia-e2e` journeys |
| Messaging, memory, sync, WebSockets | `fiducia-messaging.rs`, `fiducia-memory.rs`, `fiducia-sync`, `fiducia-edge`, agent bridge | NATS/DLQ, WebSocket scale, memory resize, sync convergence, and edge recovery suites |
| Agent and operations control planes | control-plane, manager, coordinator, bridge, Lambda, payments, telemetry repos | control-plane, Lambda, payment-idempotency, telemetry, and messaging suites |
| Interfaces and consumers | interfaces, clients, CLI, MCP | all language E2E repos, clean consumer repos, package matrix, API, CLI, and MCP suites |
| Release operations | infra plus all stateful/deployable services | multi-cloud, Raft/partition, strict proof, upgrade/rollback, backup/restore, migration, provenance, and game-day coverage |

The authoritative repository-level mapping is generated and validated in the test organization's catalog.

## Maturity and release rules

- `L0`: declaration/source intent only.
- `L1`: harness or schema self-test.
- `L2`: real product artifact launched locally and asserted.
- `L3`: multi-component or multi-node local execution.
- `L4`: independent test-org execution against pinned artifacts.
- `L5`: destructive, partition, scale, security-adversarial, or recovery execution.
- `L6`: staging/production-like release certification with retained attestation.

A clean skip is not a passing product test. Missing routes, capabilities, credentials, providers, browsers, artifacts, or evidence are `blocked`/`not-run` in ordinary lanes and fail closed in release certification. Quarantined or retried outcomes remain visible. Required release gates cannot be satisfied by mutable branches, floating package ranges, or `latest` images.

## Evidence handoff

A production release candidate publishes one immutable release manifest. Independent suites consume that same manifest and emit a versioned evidence bundle containing exact artifacts and topology, run identity, deterministic seed, assertions, failure-injection timeline, telemetry references, failure classification, cleanup result, and cryptographic artifact hashes.

The final release decision belongs to [DEN-2371](https://linear.app/denman/issue/DEN-2371/e2e-1010-run-immutable-release-candidate-certification-and-publish-the). Missing evidence is a no-go; a collection of unrelated green badges is not a release record.

## New test repositories

The test organization already has broad repository coverage. New repositories are created only under [DEN-2367](https://linear.app/denman/issue/DEN-2367/e2e-910-create-only-catalog-proven-missing-test-repositories-and) after the catalog proves a unique, non-overlapping acceptance boundary. Deepening existing generated scaffolds into executable probes takes priority over increasing repository count.