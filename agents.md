# Organization-wide agent instructions

This lowercase `agents.md` is the canonical public agent-safety policy for **fiducia-cloud**. It applies directly to this repository and is the minimum policy every repository in the organization must mirror at its own root or replace with a stricter equivalent.

An organization `.github/agents.md` is not automatically inherited by sibling repositories or coding agents. Repository owners must copy or synchronize this policy into each repository and must not weaken it locally. Compatibility files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `OPENAI.md`, and `.github/copilot-instructions.md` must reference this file while retaining enough policy context for tools that do not follow pointers.

## Discover instructions hierarchically

Resolve the current working directory, walk upward to the filesystem root, and read every readable lowercase `agents.md` on that ancestor chain in root-to-leaf order. Do not search sibling directories. Report unreadable instruction files rather than silently ignoring them.

## Required integration strategy

**avoid git rebase in favor of git merge.**

Use additive branches and semantic merge commits. Never rewrite shared history to make integration appear simpler. Inspect the current branch, worktree, remotes, default branch, related Linear work item, open pull requests, and affected cross-repository contracts before editing.

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
- Use a new additive branch, a separate clean worktree, or a separate clone when available.
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

## Discover instructions hierarchically

Resolve the current working directory, walk upward to the filesystem root, and read every readable **lowercase** `agents.md` on that ancestor chain in root-to-leaf order. Do not search sibling directories. Report unreadable instruction files rather than silently ignoring them.

Lowercase `agents.md` is canonical. Uppercase or provider-specific files are compatibility mirrors and must direct the agent back to the applicable lowercase file.

## Inspect and synchronize before editing

Before changing files, inspect the current branch, complete working tree, remotes, default branch, open pull requests, linked GitHub issues, linked Linear work, repository-local documentation, and relevant related repositories.

Use non-destructive inspection and synchronize remote knowledge before making decisions:

```sh
git status --short --branch
git remote -v
git fetch --all --prune
```

Preserve every uncommitted user or agent change. Never treat unfamiliar work as disposable. Before pushing, fetch again, incorporate the current remote branch and default branch, and **avoid git rebase in favor of git merge.** Push a feature branch and use a pull request unless the repository is being initialized from an otherwise empty bootstrap commit.

## Mandatory semantic conflict resolution

> resolve any and all git conflicts semantically, will full context, even looking back 3-10 commits in git log history for more context - never hastily pick sides in a conflict but merge things conceptually, using max context and complete conceptual awareness for a given github organization's repos and external org repos too

For every conflict:

1. Read the merge base, both sides, surrounding implementation, tests, schemas, generated artifacts, documentation, deployment configuration, and public API contracts.
2. Inspect the affected path history and normally review 3–10 relevant commits on each side using `git log`, `git show`, and `git blame` where useful.
3. Review linked pull requests, issues, Linear work, and related repositories in this organization and external organizations whenever behavior or contracts cross repository boundaries.
4. Preserve compatible intent and invariants from both sides. Synthesize a conceptual merge; never resolve merely by selecting `ours`, `theirs`, `current`, or `incoming` wholesale.
5. Scan the complete worktree for unresolved markers:

   ```sh
   git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' -- .
   ```

6. Run the smallest relevant checks while iterating, then the complete applicable formatter, linter, unit, integration, contract, build, and end-to-end gates.
7. Document incompatible requirements, intentional behavioral choices, and discarded intent in the commit or pull-request description.

## Destructive operations are default-deny

Do not run or recommend destructive or history-rewriting operations unless the user explicitly authorizes that **exact operation for the exact paths or refs** after the impact has been explained. The blacklist includes, but is not limited to:

- `git stash` in any form;
- `git reset` in any mode;
- `git clean` in any mode;
- `git rebase` and interactive history rewriting;
- `git filter-repo`, `git filter-branch`, BFG, or equivalent repository-history rewrites;
- `git push --force` or `--force-with-lease`;
- `git branch -D`, forced checkout, destructive `git restore`, or discarding worktree/index changes;
- amending or replacing shared commits;
- deleting or moving worktrees, submodules, branches, tags, repositories, releases, packages, environments, secrets, databases, buckets, clusters, namespaces, or infrastructure state;
- shell-level destructive edits such as recursive `rm`, `find -delete`, truncation, shredding, or broad in-place replacement over unreviewed paths;
- bypassing hooks, review, branch protection, required checks, policy gates, or audit logging.

Do not use destructive commands merely to make tests pass or to simplify a merge. Prefer additive edits, patch-based changes, new branches, explicit copies, and reversible migrations.

## Source ownership, generated files, worktrees, and submodules

Edit the authoritative source repository, not a generated mirror, vendored copy, build output, deployment artifact, package cache, or downstream consumer. Identify generators and regenerate derived artifacts from reviewed sources. Never detach, relocate, absorb, remove, or rewrite a submodule or worktree without explicit authorization and full cross-repository context.

## Secrets and sensitive data

Never commit, print, log, paste into prompts, or place in fixtures any token, password, private key, session secret, database URL, customer data, legal record, private health data, or unpublished security detail. Use documented secret stores and redacted examples. If a credential is exposed, stop using it, remove it from active artifacts where safely possible, revoke or rotate it, and document the incident through an approved private channel. History rewriting still requires exact authorization.

## Pull requests, tests, and evidence

Use focused commits and draft pull requests. Link the relevant Linear project or issue. Explain behavior, risks, migration and rollback considerations, security impact, tests run, and any cross-repository dependencies. Pin external GitHub Actions to full commit SHAs; declare least-privilege workflow permissions, explicit timeouts, concurrency cancellation where appropriate, and `persist-credentials: false` for checkout.

Never report a branch, commit, pull request, merge, deployment, test run, or external update as completed without authoritative remote evidence. Local files and generated archives are not a substitute for a pushed repository and verifiable GitHub state.
<!-- ore-org-baseline:end -->
