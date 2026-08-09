## Linear tracking

- Canonical issue or URL: <!-- Required for every material change; for example DEN-123 -->
- Newly discovered follow-up items: <!-- Link every feature, fix, enhancement, bug, vulnerability, reliability concern, documentation gap, or technical-debt item -->

## Summary

<!-- What changed, why, and who or what is affected? -->

## Architecture and compatibility

<!-- Repositories, APIs, schemas, generated artifacts, migrations, infrastructure, releases, or external dependencies affected. -->

## Validation

- [ ] Relevant tests, formatting, linting, builds, contract checks, integrity checks, and security checks passed
- [ ] Manual or end-to-end validation is described below
- [ ] Validation evidence and final status are synchronized to Linear

Validation details:

## Conflict-resolution record

- [ ] No conflicts occurred, or every conflict was resolved semantically and with full context
- [ ] The merge base, both sides, surrounding code/docs/tests/contracts, and relevant generated artifacts were reviewed
- [ ] At least 3 and up to 10 relevant prior commits from both sides were inspected when available
- [ ] Related repositories in this and relevant external organizations were reviewed when behavior crossed boundaries
- [ ] Compatible intent was preserved in a conceptual merge; no wholesale `ours`, `theirs`, current, or incoming selection was used
- [ ] The complete worktree was scanned for unresolved conflict markers after resolution

## Non-destructive and security checks

- [ ] I followed **avoid git rebase in favor of git merge** and did not rewrite shared history
- [ ] No prohibited Git operation, including stash/reset/clean/filtering/amend/force-push/ref deletion/pruning, was used
- [ ] No prohibited filesystem, data, infrastructure, release, artifact, or governance destruction was used
- [ ] Unrelated, uncommitted, and untracked work was left untouched; only intended paths were staged
- [ ] No hook, test, review, branch-protection, or security control was bypassed
- [ ] No secrets, credentials, personal data, customer data, or production data are included

## Risks and rollout

<!-- Operational risk, migration or roll-forward strategy, monitoring, and follow-up work. Prefer additive and reversible changes. -->

<!-- ore-org-baseline:begin -->
## Summary

Describe the behavior and intent, not only the files changed.

## Planning and dependencies

- Linear project or issue: [github.com/fiducia-cloud](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3)
- Related GitHub issues or pull requests:
- Related repositories or external contracts:

## Risk, security, migration, and rollback

- User or operational impact:
- Security/privacy impact and secret-handling review:
- Migration or compatibility considerations:
- Rollback or recovery approach:

## Validation

List exact commands, environments, and results. Include unit, integration, contract, build, and end-to-end evidence as applicable.

## Conflict-resolution record

- [ ] Remote state was fetched before editing and before pushing.
- [ ] Concurrent work was preserved; no destructive operation or history rewrite was used.
- [ ] Conflicts, if any, were resolved semantically using the merge base, both sides, 3–10 relevant commits, tests, contracts, linked work, and related repositories.
- [ ] The complete worktree was scanned for unresolved conflict markers.
- [ ] No `ours`/`theirs` side was accepted wholesale without conceptual review.

## Final checklist

- [ ] Focused commits and reviewable diff
- [ ] Documentation and generated artifacts updated from authoritative sources
- [ ] External Actions pinned to full commit SHAs
- [ ] Explicit least-privilege workflow permissions and timeouts
- [ ] No credentials, private data, or sensitive logs included
- [ ] Authoritative remote branch/PR/check evidence verified
<!-- ore-org-baseline:end -->
