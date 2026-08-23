# Fiducia opportunity operations policy

## Purpose

This public document defines the non-sensitive operating boundary for startup credits, grants, accelerators, sponsorships, developer programs, and conference submissions. It is policy, not a live provider ledger and not evidence that Fiducia qualifies for, submitted to, or was accepted by any program.

## Ownership

- `fiducia-cloud/.github` owns public policy, terminology, and the boundary between public evidence and private application material.
- `fiducia-cloud/fiducia-infra` owns the public provider catalog and dated, official-source candidate snapshots under `funding/`.
- `approved-private-application-control-plane` is the opaque owner for private application packets, exact-revision approvals, mailbox evidence, provider receipts, and submission reconciliation.
- Linear is authoritative for priority, owner, blockers, approval state, and acceptance criteria. GitHub is authoritative for reviewed code, tests, pull requests, and immutable engineering evidence.

Do not duplicate provider-specific values, deadlines, eligibility statements, application status, or terms in this static policy. Read them from the validated catalog or the approved private application control plane at the time of action.

## Public-data boundary

Public files may contain official public URLs, bounded product descriptions, evidence-state names, non-sensitive workload fit, and opaque references to private evidence.

Public files must not contain mailbox bodies, recipient lists, message headers, portal-only answers, private account identifiers, credentials, signed links, payment details, legal attestations, unpublished funding or customer facts, identity documents, or confidential provider feedback.

## Evidence states

Keep these concepts distinct:

- `discovered` — an official public route exists; eligibility is not established;
- `inquiry_sent` — a routing or information request was sent; this is not a formal application;
- `portal_required` — authenticated or manual form work remains;
- `drafted` — answers exist but the exact revision is not approved for submission;
- `approval_required` — the exact revision is complete enough for Alex to review;
- `submitted` — a durable provider receipt or equivalent evidence exists;
- `under_review`, `approved`, `declined`, `ineligible`, `blocked`, and `closed` — outcome states supported by bounded evidence.

A later email, support-ticket change, alias, reroute, or repeated receipt must not create a duplicate opportunity record.

## Mailbox identity boundary

`hello@fiducia.cloud` is the official company contact. Presence in To/Cc, forwarding, successful routing, or absence of a bounce does not prove sender authentication. Each outbound action that claims company-domain origination requires per-action evidence that the connected sending identity matches the company address.

Do not infer inbox receipt, reading, review, or human consideration from delivery alone.

## Approval boundary

A consequential application requires all of the following before submission:

1. every required company fact is verified or explicitly unresolved;
2. the final application packet has a deterministic exact-revision identity;
3. Alex has approved that exact revision;
4. legal terms, payment methods, overages, pricing, equity, travel, publicity, recording, data use, signatures, and identity-document requirements are surfaced as separate human gates;
5. the executor can record a durable provider receipt or stop in an explicit reconciliation state.

Approval for one revision does not authorize a changed revision, a second provider, a paid account, or future overages.

## Update workflow

1. Search Linear and the canonical catalog before creating a provider or opportunity record.
2. Verify current facts from official sources and store only bounded public metadata in `fiducia-infra`.
3. Keep private answers and correspondence in the approved private application control plane.
4. Prepare the complete exact revision and present it to Alex before consequential submission.
5. Record the resulting receipt, rejection, blocker, or ambiguity without upgrading evidence beyond what was observed.
6. Update public policy only when the operating contract changes; do not turn this document into a dated provider list.

Related Linear work: `DEN-3789`, `DEN-812`, `DEN-519`, `DEN-521`, and `DEN-850`.
