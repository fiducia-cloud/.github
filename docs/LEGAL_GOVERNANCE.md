# Legal governance and executable contract policy

This organization uses `fiducia-cloud/fiducia-docs` as the reviewable legal-document workspace and `ores-legal` as a reusable drafting/governance pattern source. Text from another organization never automatically governs Fiducia: every customer, workforce, product, jurisdiction, and release use requires Fiducia-specific review and approval.

## Source and execution layers

The standard legal contract layout is:

- human sources: `fiducia-docs/docs/legal/**` and reviewed top-level policies;
- independent TypeSpec authority: `fiducia-docs/contracts/main.tsp`;
- independent JSON Schema Draft 2020-12 authority: `fiducia-docs/contracts/authored.schema.json`;
- executable registry corpus: `fiducia-docs/contracts/instances/LegalRegistry/valid/registry.json`;
- deterministic human projection: `fiducia-docs/generated/legal-coverage.md`;
- deterministic runtime projection: `fiducia-docs/generated/legal-runtime-manifest.json`.

`@oresoftware/typespec-json-schema-validator` (`tjsv`) compares the two independent authorities and validates the registry corpus. Generated schema is comparison evidence only; it is not allowed to overwrite the authored schema. `ores-cli`/`oresc` is the repository/governance integration layer and delegates contract parity to `tjsv` rather than implementing a second schema engine.

## Approval and release rule

Legal registry states are `approved`, `draft`, `review_required`, and `gap`. Only `approved` documents that are explicitly distributed to an end user/customer may enter the runtime approved manifest. Runtime consumers must bind to document ID plus exact content hash and fail closed if a required ID is missing, blocked, stale, or presented through the wrong acceptance mechanism.

Installation, account creation, IAM permission, API use, device permission, or possession of software does not silently constitute acceptance of unrelated terms. Acceptance records belong in the product's protected system of record, not in Git.

## Fiducia release triggers

A legal-impact review is required when code changes alter: CLI commands that create/delete/deploy/rotate or otherwise cause external effects; local files or caches; customer-hosted node/sidecar privileges; credentials; networking; telemetry/logging; subprocessors/cloud APIs; data locality/retention; billing; support/service levels; auto-update/removal; incident access; professional services; or onboarding/offboarding behavior.

SLOs are engineering objectives. Contractual availability, service credits, exclusions, measurement windows, remedies, and support commitments belong in the SLA/MSA/SOW stack and must not be inferred from dashboards or constants.

## Repository privacy boundary

Never commit executed agreements, signatures, customer evidence, credentials, privileged communications, personnel records, identity documents, or matter-specific legal advice to organization repositories. Git may contain blank templates, policy text, public notices, non-sensitive routing metadata, approval references, and deterministic content hashes.

## Reusable CI

Runtime and docs repositories may call:

```yaml
jobs:
  legal-contract:
    uses: fiducia-cloud/.github/.github/workflows/reusable-legal-contract-audit.yml@main
```

Repositories with the standard `contracts/**` layout receive TypeSpec/JSON Schema/corpus and projection checks. Private/release runners should set `require_ores_cli: true` once `oresc` is provisioned so absence of the governance CLI becomes fail-closed.

Counsel and accountable business owners remain responsible for substantive legal approval; CI verifies synchronization, coverage state, and release metadata, not legal sufficiency.
