<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [fiducia-cloud](https://github.com/fiducia-cloud)
- **Organization GitHub Project:** [fiducia-cloud-project](https://github.com/orgs/fiducia-cloud/projects/1) (project 1)
- **Shared Linear project:** [fiducia-cloud](https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3)
- **Independent test organization:** [fiducia-cloud-test](https://github.com/fiducia-cloud-test)
- **Test-fleet GitHub Project:** [fiducia-cloud-test-project](https://github.com/orgs/fiducia-cloud-test/projects/1) (project 1)
- **Program issue:** [DEN-2353 — Everything E2E](https://linear.app/denman/issue/DEN-2353/e2e-program-certify-every-fiducia-production-surface-through)
- **Program plan:** [Everything E2E — Full-System Test Program](https://linear.app/denman/document/everything-e2e-full-system-test-program-57e84c9eb677)
- **Organization documentation repository:** [fiducia-cloud/.github](https://github.com/fiducia-cloud/.github)

## One planning project, two execution boards

Both GitHub organizations share the single Linear project `fiducia-cloud`. Linear owns product outcomes, priorities, dependencies, milestones, acceptance criteria, and release-readiness status. Do not create a parallel test-only Linear backlog.

Each organization keeps GitHub Project #1 for its execution boundary:

- `fiducia-cloud` owns product code, white-box tests, interfaces, migrations, packages/images, releases, deployments, and product-side evidence.
- `fiducia-cloud-test` owns independent black-box probes, clean consumers, compatibility matrices, chaos/scale/recovery execution, and retained certification evidence.

Every GitHub Project item should link to a canonical Linear issue. Every Linear issue should link to the relevant repositories, pull requests, workflow runs, release manifests, and evidence bundles.

## Release boundary

A production repository's green unit/integration checks are necessary but do not independently certify a release. Required capabilities must also pass the independent paths defined in [`INDEPENDENT-E2E.md`](INDEPENDENT-E2E.md) and the test organization's machine-readable catalog. Missing, skipped, blocked, quarantined, or mutable-artifact execution never satisfies a release gate.

## Change and merge policy

Documentation and automation changes use pull requests and merge after review/checks. Concurrent edits are reconciled semantically against the latest default branch. Preserve unrelated prose and regenerate managed blocks without blindly choosing one side of a conflict.
<!-- org-project-routing:end -->

## Audited organization snapshot

The production-organization repository snapshot dated **2026-08-05** contains **34 repositories**: **33 active** and **1 archived**. The sole archived repository is `fiducia-customer-ui.web`. The machine-readable source is [`repository-map.json`](./repository-map.json), and the human routing view is [`REPOSITORY_MAP.md`](./REPOSITORY_MAP.md).

This snapshot is an inventory and routing classification. It does not certify that a repository is implemented, deployed, secure, released, supported, or production-ready. Independent release certification remains governed by the production/test boundary above.

## Repository evidence lifecycle

1. Product intent, priority, owner, blockers, and acceptance criteria live in the shared `fiducia-cloud` Linear project.
2. Every code or policy change uses a branch and commit message that include the Linear identifier when one exists.
3. The pull request links the Linear issue and records exact validation evidence.
4. Required production checks pass before merge; conflicts are reconciled semantically against the latest default branch.
5. Merge, release, deployment, and product-side evidence are linked to the production GitHub Project item.
6. Independent acceptance evidence is linked from the test-fleet GitHub Project item to the same Linear issue.
7. A Linear issue is not completed merely because a pull request exists; the acceptance criteria and required evidence must be satisfied.

## Recommended GitHub Project fields

Both organization Projects should use one item per durable issue or pull request and, at minimum, expose:

- **Status:** Backlog, Ready, In progress, In review, Blocked, Done.
- **Repository:** exact owning repository.
- **Linear:** canonical issue identifier in the shared project.
- **Workstream:** one routing category from the repository map or independent test catalog.
- **Evidence:** pull request, workflow run, release manifest, deployment, or certification bundle.

Automation may mirror status, but Linear remains authoritative for planning state and GitHub remains authoritative for engineering and certification evidence.

## Public-data boundary

Do not place credentials, mailbox bodies, private application answers, legal attestations, customer data, payment details, or unpublished funding information in this public repository or either public GitHub Project. Public application reporting should use bounded outcome metadata and non-secret evidence references only.
