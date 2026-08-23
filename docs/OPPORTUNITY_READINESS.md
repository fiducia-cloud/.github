# Fiducia startup-program and OSS-funding readiness

This document is the public, non-sensitive coordination surface for startup credits, open-source funding, sponsorships, accelerators, and conference submissions.

## Safety boundary

Do not publish mailbox bodies, credentials, legal attestations, payment details, unpublished funding information, customer data, or portal-only application answers here. A program may be listed as a candidate without implying eligibility, acceptance, submission, or contractual commitment.

## Current priority queue

| Opportunity | Why it fits | Public readiness action | Approval gate |
| --- | --- | --- | --- |
| Civo Startup Program | Kubernetes and multi-cloud reliability testing | Document portable cluster test workloads and expected standard-compute usage | Final application facts and submission |
| Grafana Labs Startup Program | Consensus and coordination observability | Publish OTEL metrics/traces coverage and dashboards without claiming production maturity | Reference-customer / marketing obligations |
| Cloudflare for Startups | Edge ingress, security, routing, Workers/R2 experiments | Document provider-neutral ingress and public API architecture | Payment method, overages, marketing rights, final application |
| OVHcloud Startup Program | Independent Kubernetes/cloud portability | Add OVHcloud as a candidate environment in failure-injection plans | Final application facts and terms |
| GitHub Secure Open Source Fund | Security-sensitive infrastructure and OSS | Add OSS license, SECURITY.md, CONTRIBUTING.md, governance, releases, SBOM/provenance, and adoption evidence before applying | Final application and any program obligations |
| Neon Open Source Program | Potential Postgres control-plane integration | Apply only after a real supported Neon/Postgres integration is documented | Final application facts |

## Evidence required before claims

Applications must distinguish these states:

- **implemented** — present in reviewed source;
- **tested** — exercised by automated or documented validation;
- **deployed** — backed by environment/runtime evidence;
- **adopted** — backed by external usage evidence;
- **planned** — not yet evidence for implementation or eligibility.

Unknown legal entity, incorporation date, headcount, funding, revenue, customers, cloud spend, or co-founder facts remain `unverified` until confirmed by an authorized company source.

## Reusable public product description

Fiducia is a Rust-based distributed coordination platform for cloud-native systems. The project targets strongly consistent coordination primitives such as distributed locks and leases, fencing, leader election, service discovery, idempotency, scheduling, rate limiting, and configuration state across provider-independent infrastructure.

This description is intentionally bounded: repository-specific implementation, deployment, performance, and production claims still require direct evidence.

## Conference proposal themes

Conference submissions should remain vendor-neutral and teach reusable engineering principles. Current themes include:

1. fencing tokens, leases, stale holders, and multi-key coordination;
2. sharded Raft and quorum placement across Kubernetes/cloud failure domains;
3. failure injection and evidence-driven multi-cloud claims;
4. observability for consensus health, leader churn, replication lag, and contention.

## Workflow

1. Track opportunity, deadline, eligibility questions, and missing facts in Linear.
2. Put only public/non-sensitive evidence in GitHub.
3. Link every evidence PR to the canonical Linear issue.
4. Run repository and security readiness checks before any OSS-funding application.
5. Prepare the completed application for Alex's review before consequential submission.
6. Do not accept terms, add payment methods, commit spend, equity, travel, marketing rights, or other company obligations through automation.

Related Linear work: DEN-519, DEN-518, DEN-812, DEN-850, DEN-1180, DEN-1299.
