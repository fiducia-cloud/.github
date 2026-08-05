# fiducia-cloud

This organization and its independent acceptance organization, [`fiducia-cloud-test`](https://github.com/fiducia-cloud-test), share the Linear project [fiducia-cloud](https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3).

## AI agent context

- GitHub owner ID: `297262292`
- Linear project ID: `d9e89bd3-19da-47f3-9bf7-6dc8cc910b70`
- Linear team: `DEN` (`eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc`)
- Machine-readable context: [`project-context.yaml`](https://github.com/fiducia-cloud/.github/blob/main/project-context.yaml)
- Canonical registry: [`ORESoftware/ai-agent-coordinator.rs/config/org-project-registry.yaml`](https://github.com/ORESoftware/ai-agent-coordinator.rs/blob/d3e03ecc2e175a7f6261523d35c73ac775c49942/config/org-project-registry.yaml)

No default repository is declared; agents must resolve the exact repository and fail closed on ambiguity.

Repository-local `AGENTS.md`, `agents.md`, and tool instructions remain authoritative for build, test, and implementation details. The central registry remains authoritative for GitHub/Linear identity and routing. Unmapped or ambiguous work must be rejected rather than guessed.

## Independent release certification

`fiducia-cloud` owns production code, white-box confidence, deployable artifacts, migrations, and runtime integration. `fiducia-cloud-test` owns independently versioned black-box probes, clean SDK consumers, compatibility matrices, chaos/scale/recovery execution, and certification evidence.

- [Everything E2E program](https://linear.app/denman/issue/DEN-2353/e2e-program-certify-every-fiducia-production-surface-through)
- [Full-system plan](https://linear.app/denman/document/everything-e2e-full-system-test-program-57e84c9eb677)
- [Production-side responsibilities](../docs/INDEPENDENT-E2E.md)
- [Test-fleet catalog](https://github.com/fiducia-cloud-test/.github/blob/main/test-program/catalog.json)

A generated test plan, source-pin check, clean skip, or workflow that only validates its harness is not product certification. Release-required tests must consume immutable artifacts, execute real assertions, fail closed, and retain evidence.

## Semantic Git conflict resolution

> resolve any and all git conflicts semantically, will full context, even looking back 3-10 commits in git log history for more context - never hastily pick sides in a conflict but merge things conceptually, using max context and complete conceptual awareness for a given github organization's repos and external org repos too

Before resolving a conflict, inspect the merge base and 3–10 relevant commits from both sides when available, including path-scoped history for every conflicted file. Read repository-local instructions, linked Linear issues, pull requests, architecture decisions, tests, migrations, schemas, and documentation. When a contract crosses repository boundaries, inspect relevant repositories in the same GitHub organization and relevant repositories in external GitHub organizations too.

Never resolve by blindly or wholesale selecting `ours`, `theirs`, current, or incoming. Produce a conceptual merge that preserves compatible intent, invariants, APIs, schemas, migrations, tests, documentation, security controls, and operational safeguards from all relevant sides. Document non-obvious decisions, scan the whole worktree for conflict markers, and run every affected validation contract. “Max context” means all relevant authorized context; it never authorizes exposing credentials, private data, or hidden reasoning.

This public repository contains identifiers, links, and public operating guidance only. Do not place credentials, private customer data, or private operational details here.

<!-- org-project-routing:start -->
## Planning and delivery

- [Shared Linear project: fiducia-cloud](https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3)
- [Everything E2E program issue](https://linear.app/denman/issue/DEN-2353/e2e-program-certify-every-fiducia-production-surface-through)
- [GitHub Project: fiducia-cloud-project](https://github.com/orgs/fiducia-cloud/projects/1)
- [Independent test GitHub Project](https://github.com/orgs/fiducia-cloud-test/projects/1)
- [Detailed project-routing contract](../docs/PROJECTS.md)

Linear owns outcomes, priorities, dependencies, milestones, and release-readiness status. This organization Project owns production delivery; the test organization Project owns independent acceptance. Pull requests, workflow runs, immutable artifacts, evidence bundles, releases, and deployment attestations are the implementation record.
<!-- org-project-routing:end -->
