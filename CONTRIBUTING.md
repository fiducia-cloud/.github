# Contributing

Thank you for contributing to fiducia-cloud.

## Before starting

1. Read [`AGENTS.md`](AGENTS.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and [`SECURITY.md`](SECURITY.md).
2. Find or create the relevant work item in the [fiducia-cloud Linear project](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3).
3. Confirm the affected repositories, contracts, generated artifacts, infrastructure, and deployment boundaries.

## Non-destructive workflow

Leave unrelated and uncommitted work untouched. Agents and automated contributors must not use `git stash`, `git reset`, `git clean`, `git filter-repo`, history rewrites, force pushes, recursive deletion, destructive database or infrastructure commands, or equivalent operations. Use additive branches, clean worktrees or clones, explicit staging, normal pushes, dry runs, and reversible roll-forward changes.

## Conflicts

Resolve every conflict semantically. Read both sides and the surrounding subsystem; inspect 3–10 relevant prior commits when useful; review related organization and external repositories when contracts cross boundaries; preserve compatible intent; run relevant validation; and explain tradeoffs in the pull request.

## Pull requests

Keep each pull request coherent and reviewable. Include:

- the linked Linear issue or project;
- the problem and intended outcome;
- important implementation and architecture choices;
- compatibility, migration, security, and operational risks;
- tests, checks, and manual validation performed;
- conflict-resolution details, when applicable.

Never commit secrets, production data, personal data, generated credentials, or local environment files.
