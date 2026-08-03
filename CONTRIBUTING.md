# Contributing

Thank you for contributing to fiducia-cloud.

## Before starting

1. Read [`AGENTS.md`](AGENTS.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and [`SECURITY.md`](SECURITY.md).
2. Search for the relevant work item in the [fiducia-cloud Linear project](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3); create one when no suitable item exists.
3. Every discovered feature, fix, enhancement, bug, vulnerability, reliability concern, documentation gap, or technical-debt item must have a Linear issue before implementation begins.
4. Confirm the affected repositories, contracts, generated artifacts, infrastructure, deployment boundaries, and external dependencies.

## Non-destructive workflow

**avoid git rebase in favor of git merge**

Leave unrelated, uncommitted, and untracked work untouched. Agents and automated contributors must not use `git rebase`, `git stash`, `git reset`, `git clean`, `git filter-repo`, `git filter-branch`, `git commit --amend`, destructive checkout or restore, branch or ref deletion, pruning, `git push --force`, `git push --force-with-lease`, `git push -f`, `rm`, `mv`, `sed`, recursive deletion, `find -delete`, `xargs rm`, `truncate`, `shred`, `dd`, destructive database commands such as `DROP`, `TRUNCATE`, or unbounded `DELETE`, destructive infrastructure commands such as `kubectl delete`, `helm uninstall`, `terraform destroy`, or `pulumi destroy`, release or artifact deletion, branch-protection bypass, `--no-verify`, or equivalent operations. Use additive branches, clean worktrees or clones, explicit staging, normal pushes, dry runs, backups, additive migrations, and reversible roll-forward changes.

## Conflicts

Resolve every conflict semantically and with full context. Read the merge base, both sides, and the surrounding subsystem; inspect at least 3 and up to 10 relevant prior commits from both sides when available; review related organization and external repositories when contracts cross boundaries; preserve compatible intent in a conceptual merge instead of accepting `ours` or `theirs` wholesale; run relevant validation; and explain tradeoffs in the pull request and Linear issue. Stop and report whenever safe progress or routing is blocked.

## Pull requests

Keep each pull request coherent and reviewable. Include:

- the linked Linear issue or canonical Linear URL;
- the problem and intended outcome;
- important implementation and architecture choices;
- compatibility, migration, security, and operational risks;
- tests, checks, and manual validation performed;
- conflict-resolution details, when applicable;
- newly discovered follow-up work and its Linear references.

Never commit secrets, production data, personal data, generated credentials, or local environment files. Repository-local rules may be stricter but may not weaken this baseline.
