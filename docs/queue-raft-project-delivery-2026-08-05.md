# Fiducia queue and Raft project delivery — August 5, 2026

## Project routing

- GitHub organization: [`fiducia-cloud`](https://github.com/fiducia-cloud)
- GitHub Project: [`fiducia-cloud-project` #1](https://github.com/orgs/fiducia-cloud/projects/1)
- Linear project: [`github.com/fiducia-cloud`](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3)
- Linear evidence: [Fiducia queue and Raft hardening evidence — August 5, 2026](https://linear.app/denman/document/fiducia-queue-and-raft-hardening-evidence-august-5-2026-ddefb3921886)
- Primary Linear issues: DEN-80, DEN-566, DEN-437, DEN-1154

Queue, lock/lease state-machine, Raft, fencing, and durable distributed-ownership work belongs on this organization’s Project and Linear project. Shared Kubernetes and CI infrastructure belongs to the ORESoftware project rather than this board.

## Final merge receipts

| Repository | Pull request | Exact validated head | Merge commit |
|---|---:|---|---|
| `fiducia-cloud/fiducia-node.rs` | [#29](https://github.com/fiducia-cloud/fiducia-node.rs/pull/29) | `3f07402474c2edc98f17a87e951e6116fad1d80d` | `b9177646f9c69c67b76b3fbee9fded9b585e9c0c` |
| `fiducia-cloud/fiducia-brain.rs` | [#25](https://github.com/fiducia-cloud/fiducia-brain.rs/pull/25) | `8acbfe76bb03f9a693acdbe0f4649bc8851f2ab1` | `588d1bc2d6a61514ef0d036280f9cde20fb6284d` |

## Queue and Raft authority boundary

The indexed queue and Raft remain separate implementation layers, but committed Raft state is the only durability authority for logical queue order and transitions.

The queue owns deterministic mechanics: stable FIFO order, keyed lookup and cancellation, canonical key sets, ordered promotion, memory reclamation, and validation of list/map/slab/free-list internals. It does not determine terms, leaders, quorums, transport authority, or commit order.

Raft owns authoritative enqueue, cancel, logical-time expiry, promotion, grant, renew, and release order. Recovery comes from committed log state or a strictly validated state-machine snapshot.

Do not add an independent queue WAL. A second journal would create two competing durability authorities. Slab indexes, linked-list pointers, map buckets, response channels, and process-local waiter objects remain non-authoritative implementation details.

## Validation evidence

`fiducia-node.rs#29` passed:

- 265 product tests;
- 129 formal/refinement tests;
- a deterministic 25,000-operation differential queue test;
- warnings-denied all-target/all-feature Clippy;
- permanent CI and Nix validation.

The change rejects duplicate restored identities, cycles, stale indexes, unreachable occupied nodes, malformed free lists, inconsistent holders/grants/semaphores/fencing tokens, and impossible durable Raft term/log combinations.

`fiducia-brain.rs#25` passed formatting, all-target tests, warnings-denied Clippy, permanent CI, and formal-method workflows. It hardens AppendEntries and snapshot validation, request-bounded follower acknowledgements, prefix proof before truncation, first-index retry progress, sender/message identity, WAL framing, torn-write handling, and restart consistency.

## Remaining proof obligations

1. Add authenticated per-member transport, preferably mTLS/SPIFFE identity.
2. Run true multi-process partition, stale-leader, leadership-transfer, delayed/duplicate-delivery, and restart tests.
3. Prove restart-durable lost-response retry behavior using request IDs and fencing tokens.
4. Run sustained-contention fairness/starvation campaigns and long queue-memory soaks.
5. Exercise PVC snapshot, backup, restore, and log replay.
6. Keep request IDs mandatory wherever cancellation-race safety is required.