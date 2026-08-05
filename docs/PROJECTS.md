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
