# GitHub Copilot repository instructions

The canonical lowercase policy is [`/agents.md`](../agents.md). `/AGENTS.md` is the full compatibility mirror. Follow both in full; organization-level files are not automatically inherited by other repositories, so every repository must maintain compatible root instructions.

**avoid git rebase in favor of git merge**

Resolve every Git conflict semantically and with full context. Read the merge base, both sides, surrounding code, documentation, tests, schemas, generated artifacts, and contracts. When available and relevant, inspect at least 3 and up to 10 prior commits from both sides with `git log`, `git show`, and `git blame`. Review related repositories in this organization and relevant external organizations when behavior crosses repository boundaries. Never accept `ours`, `theirs`, current, or incoming wholesale; preserve compatible intent and produce a conceptual merge.

Every discovered feature, fix, enhancement, bug, vulnerability, reliability concern, documentation gap, or technical-debt item requires a canonical Linear issue before implementation begins. Search first, link or create the issue, reference it in every pull request, synchronize status and evidence, and stop when routing is missing or ambiguous.

Operate non-destructively. Never use `git rebase`, `git stash`, `git reset`, `git clean`, `git filter-repo`, `git filter-branch`, `git commit --amend`, destructive checkout or restore, branch or ref deletion, pruning, `git push --force`, `git push --force-with-lease`, or `git push -f`. Never use `rm`, `mv`, `sed`, `find -delete`, `xargs rm`, `truncate`, `shred`, `dd`, recursive deletion, destructive overwrites, `DROP`, `TRUNCATE`, unbounded `DELETE`, destructive rollback, `kubectl delete`, `helm uninstall`, `terraform destroy`, `pulumi destroy`, cloud deletion, package unpublishing, artifact purging, branch-protection bypass, or `--no-verify`. Do not bypass hooks, tests, reviews, or security checks.

Leave unrelated, uncommitted, and untracked work untouched. Prefer inspection, additive branches, separate clean worktrees or clones, explicit staging, normal non-force pushes, dry runs, backups, additive migrations, and reversible roll-forward changes. If safe progress is blocked, preserve state and report the blocker.

Never expose secrets or sensitive data. Run relevant validation and document conflict decisions, risks, and the linked Linear work item.

Linear project: https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3
