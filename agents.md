# Organization-wide agent instructions

This lowercase `agents.md` is the canonical public agent-safety policy for **fiducia-cloud**. It applies directly to this repository and is the minimum policy every repository in the organization must mirror at its own root or replace with a stricter equivalent.

An organization `.github/agents.md` is not automatically inherited by sibling repositories or coding agents. Repository owners must copy or synchronize this policy into each repository and must not weaken it locally. Compatibility files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `OPENAI.md`, and `.github/copilot-instructions.md` must reference this file while retaining enough policy context for tools that do not follow pointers.

## Discover instructions hierarchically

Resolve the current working directory, walk upward to the filesystem root, and read every readable lowercase `agents.md` on that ancestor chain in root-to-leaf order. Do not search sibling directories. Report unreadable instruction files rather than silently ignoring them.

## Required integration strategy

**avoid git rebase in favor of git merge.**

Work directly on the existing `main` branch and use semantic merge commits. Do not create or use feature branches or Git worktrees. An alternate branch is permitted only when a human or a repository-specific release process explicitly requires it; merge that history back into `main` without rewriting shared history. Inspect the current branch, worktree, remotes, default branch, related Linear work item, open pull requests, and affected cross-repository contracts before editing.

## Main-branch and concurrent-agent policy

This organization policy overrides generic feature-branch and worktree defaults for agent tooling.

- Work directly on `main`, including when other agents are active. Coordinate repository and file ownership through the available agent communication channel instead of isolating routine work on another branch or worktree.
- Never create or use a Git worktree unless a human explicitly instructs you to do so for the current task. Concurrency alone is not permission to use a worktree.
- Keep edits scoped, inspect live state before each write, and hand off cleanly.
- Preserve unrelated in-progress changes and never overwrite another agent's work. If safe ownership of overlapping files cannot be established, pause that overlapping edit and coordinate before continuing.

## Required semantic conflict-resolution declaration

The original organization directive is preserved verbatim:

> resolve any and all git conflicts semantically, will full context, even looking back 3-10 commits in git log history for more context - never hastily pick sides in a conflict but merge things conceptually, using max context and complete conceptual awareness for a given github organization's repos and external org repos too

Operationally, resolve every Git conflict semantically and with full context.

Before finalizing any conflict resolution:

1. Read the merge base, both sides, surrounding code and documentation, relevant tests, schemas, generated artifacts, deployment files, and public contracts—not only conflict markers.
2. Inspect the affected history. When available and relevant, review 3–10 relevant prior commits from both sides with path-scoped `git log`, `git show`, and `git blame`.
3. Inspect related repositories in this organization and relevant external organizations whenever APIs, schemas, shared libraries, infrastructure, generated code, release processes, or runtime behavior cross repository boundaries.
4. Preserve all compatible intent and invariants. Synthesize a conceptual merge instead of accepting `ours` or `theirs` wholesale, or accepting current or incoming wholesale.
5. Scan the complete worktree for unresolved conflict markers and run the most relevant tests, formatters, linters, builds, contract checks, security checks, and end-to-end checks.
6. Document intentional tradeoffs, incompatible requirements, and discarded behavior in the commit, pull-request description, and linked Linear issue.

Never resolve a conflict by deleting unfamiliar work, relying only on the newest snapshot, or choosing a side merely because it is easier.

## Mandatory Linear tracking

Every discovered feature, fix, enhancement, bug, vulnerability, reliability concern, documentation gap, or technical-debt item must be represented by a Linear issue in the canonical project **before implementation begins**.

1. Search Linear first and link the existing issue when one already covers the work.
2. Create a new issue when no suitable issue exists.
3. Include the Linear identifier or canonical Linear URL in every pull request and material implementation commit.
4. Keep scope, acceptance criteria, validation evidence, dependencies, and final status synchronized between GitHub and Linear.
5. If GitHub-to-Linear routing is missing or ambiguous, stop and report it rather than guessing or making an untracked drive-by change.

Canonical Linear project: https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3

## Deny-by-default destructive operations

Automated agents must not execute or recommend commands whose purpose or practical effect is to discard, hide, rewrite, purge, delete, or irreversibly mutate existing state. A dirty worktree, an inconvenient branch, a failed migration, or a conflict is never permission to destroy state.

The following operations are explicitly blacklisted for agents:

- **Git worktree/history destruction or concealment:** every form of `git rebase`, `git stash`, `git reset`, `git clean`, `git filter-repo`, `git filter-branch`, `git commit --amend`, `git checkout --`, destructive `git restore`, `git branch -D`, deletion of refs or tags, `git reflog expire`, aggressive or pruning `git gc`, `git push --force`, `git push --force-with-lease`, `git push -f`, and equivalent worktree or history rewrites.
- **Filesystem destruction or opaque rewrites:** `rm`, `rm -rf`, `mv`, `sed`, recursive or bulk deletion, `find -delete`, `xargs rm`, `truncate`, `shred`, `dd`, destructive overwrites, disk formatting, mass moves that erase destinations, or permission and ownership changes that can remove access. Use explicit, reviewable file APIs or targeted patch operations instead.
- **Data destruction:** `DROP`, `TRUNCATE`, unbounded `DELETE`, destructive schema rollback, irreversible migrations, storage-bucket purges, queue or topic deletion, and bulk record mutation without a reviewed, bounded, reversible plan.
- **Infrastructure destruction:** `kubectl delete`, `helm uninstall`, `terraform destroy`, `pulumi destroy`, cloud-provider delete or purge commands, cluster or namespace teardown, secret, key, or certificate revocation, and equivalent destructive control-plane actions.
- **Release and governance destruction:** package or release unpublishing, artifact deletion, registry purges, disabling branch protection, bypassing required reviews, disabling tests or security checks, and use of `--no-verify` or equivalent policy bypasses.

This blacklist is illustrative, not exhaustive. When an operation may destroy, discard, conceal, or rewrite state, treat it as prohibited by default. Agents may prepare a reviewed runbook for a human, but must not execute the destructive operation themselves.

### Safe alternatives

- Inspect with `git status`, `git diff`, `git log`, `git show`, and `git blame`.
- Leave unrelated, uncommitted, and untracked work untouched.
- Prefer the existing `main` branch and coordinate concurrent file ownership directly. Use another branch or clone only when explicitly required, and never use a worktree without explicit human instruction.
- Stage explicit intended paths; do not stage unrelated work.
- Commit new work normally, merge semantically, and push without force.
- Prefer dry runs, read-only queries, backups, additive migrations, and reversible roll-forward changes.
- When safe progress is impossible, report the exact blocker and preserve all state.

## Secrets and sensitive data

Never print, log, commit, paste into issues, or expose tokens, credentials, private keys, personal data, production data, or secret-bearing environment variables. Use placeholders in examples and redact diagnostics.

## Pull requests, evidence, and validation

Keep changes scoped, explain risks and migration effects, list exact validation performed, state whether conflicts occurred and how they were resolved, and never claim a remote action passed without authoritative evidence.

GitHub Actions must use least-privilege permissions, explicit timeouts, concurrency cancellation where appropriate, checkout without persisted credentials, and immutable full-commit action pins. Dependency updates must remain reviewable and reproducible.

## Precedence

Repository-local instructions may add stricter requirements, but they must not weaken the integration strategy, semantic conflict-resolution policy, mandatory Linear tracking, destructive-operation blacklist, secret-handling requirements, or validation expectations in this file.


<!-- ore-org-baseline:begin -->
These instructions apply to this repository. Repository-local instructions may add stricter requirements, but they must not weaken this baseline.

## Canonical organization links

- GitHub organization: https://github.com/fiducia-cloud
- Public organization defaults: https://github.com/fiducia-cloud/.github
- Canonical Linear project: https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3
- Fleet tracking issue: https://github.com/ORESoftware/k8s-cluster/issues/1222

## Instruction discovery

Lowercase `agents.md` is canonical. Read every applicable lowercase `agents.md` from the repository root toward the current working directory before editing. Uppercase `AGENTS.md` and provider-specific instruction files are compatibility mirrors and must remain aligned with the applicable lowercase policy.

## Inspect before editing

Inspect the current branch, complete working tree, remotes, default branch, open pull requests, linked GitHub issues, linked Linear work, repository documentation, tests, schemas, generated artifacts, deployment definitions, and relevant related repositories. Preserve every unfamiliar or uncommitted change.

Use read-only inspection and non-pruning synchronization such as `git status --short --branch`, `git remote -v`, `git fetch --all`, `git diff`, `git log`, `git show`, and `git blame`. Never treat a dirty worktree or inconvenient branch as permission to discard state.

## Mandatory semantic conflict resolution

> resolve any and all git conflicts semantically, will full context, even looking back 3-10 commits in git log history for more context - never hastily pick sides in a conflict but merge things conceptually, using max context and complete conceptual awareness for a given github organization's repos and external org repos too

For every conflict:

1. Read the merge base, both complete sides, surrounding implementation, tests, schemas, generated artifacts, documentation, deployment configuration, and public contracts—not only conflict markers.
2. Inspect the affected path history and normally review 3–10 relevant commits on each side with `git log`, `git show`, and `git blame` where useful.
3. Review linked pull requests, issues, Linear work, related repositories in `fiducia-cloud`, and relevant external-organization repositories whenever behavior or contracts cross boundaries.
4. Preserve compatible intent and invariants from both sides. Synthesize a conceptual merge; never resolve by selecting `ours`, `theirs`, `current`, or `incoming` wholesale.
5. Scan the complete tree for unresolved markers and run the applicable formatter, linter, unit, integration, contract, build, security, and end-to-end checks.
6. Document incompatible requirements, intentional choices, and any discarded intent in the commit and pull-request description.

## Hard denylist for automated agents

Automated agents must **never execute or recommend** destructive, state-concealing, history-rewriting, purge, revocation, or policy-bypass operations. This is a hard denylist: authorization may support a reviewed human-run procedure, but it does not authorize an automated agent to perform the destructive step.

The blacklist includes, without limitation:

- every form of `git stash`, every mode of `git reset`, every mode of `git clean`, `git filter-repo`, `git filter-branch`, BFG, `git rebase`, interactive history rewriting, `git commit --amend`, commit replacement, destructive `git checkout -- <path>`, destructive `git restore`, `git branch -D`, ref or tag deletion, `git reflog expire`, `git gc --prune`, `git push --force`, and `git push --force-with-lease`;
- recursive or bulk deletion and destructive filesystem mutation, including `rm -rf`, `find -delete`, truncation, shredding, destructive overwrite, formatting, and access-removing ownership or permission changes;
- destructive data operations, including `DROP`, `TRUNCATE`, unbounded `DELETE`, destructive rollback, irreversible migration, bucket/object purge, queue/topic deletion, and bulk mutation without a bounded reversible plan;
- destructive infrastructure or identity operations, including `kubectl delete`, `helm uninstall`, `terraform destroy`, `pulumi destroy`, cloud delete/purge calls, cluster or namespace teardown, and autonomous secret, key, certificate, credential, factor, or session revocation or rotation;
- deleting repositories, worktrees, submodules, branches, tags, releases, packages, artifacts, registries, environments, evidence, audit logs, customer data, or production state;
- bypassing hooks, reviews, branch protection, rulesets, required checks, security/compliance gates, approvals, or audit logging, including `--no-verify` and equivalent bypasses.

Do not use destructive commands merely to make tests pass, clear a conflict, simplify a migration, or hide an inconvenient state.

### Required safe alternatives

Use direct `main`-branch work, coordinated file ownership, explicit path staging, ordinary commits, non-force pushes, patch-based edits, read-only queries, dry runs, backups, additive migrations, and reversible roll-forward changes. Do not create a branch or worktree merely to avoid coordination. Leave unrelated work untouched. When safe progress is impossible, preserve all state and report the exact blocker.

## Source ownership and cross-repository context

Edit authoritative sources rather than generated mirrors, vendored copies, caches, or downstream consumers. Identify generators and regenerate derived artifacts from reviewed sources. Never detach, absorb, relocate, remove, or rewrite a submodule or worktree. Cross-repository behavior must be understood across the owning organization and relevant external organizations before contracts are changed.

## Secrets and sensitive data

Never print, log, commit, paste into issues, include in fixtures, or expose tokens, passwords, private keys, session material, database URLs, customer data, legal records, private health data, production data, or unpublished security details. Use approved secret stores, placeholders, and redacted diagnostics.

## Pull requests, validation, and evidence

Use focused commits on `main`; use an alternate branch or pull request only when a human or repository-specific release process explicitly requires one. Link the relevant Linear issue or project. Explain behavior, risks, migration and roll-forward considerations, security impact, tests run, conflicts and their semantic resolution, and cross-repository dependencies. Never report a branch, commit, pull request, merge, deployment, test run, or external update as complete without authoritative remote evidence.
<!-- ore-org-baseline:end -->

## Repository-local Git worktrees

- Create or use a Git worktree only when the human operator explicitly authorizes it for the current task. Concurrency or a dirty checkout is not permission by itself.
- Put every authorized worktree at `<repository-root>/tmp/worktrees/<name>`; from the repository root, use `./tmp/worktrees/<name>`. Never place worktrees beside repositories or organization directories.
- Keep `tmp`, `temp`, `tmp/worktrees`, and `temp/worktrees` ignored in the repository-root `.gitignore`. Do not commit files from those directories.
- Relocate or remove a worktree only when the operator explicitly requests it. Before removal, preserve and publish intended changes, verify its commit is represented on the target branch, and confirm there are no tracked, untracked, ignored-sensitive, or in-use files that must survive. Remove it with `git worktree remove <path>` without `--force`; never delete a worktree directory with `rm`.
