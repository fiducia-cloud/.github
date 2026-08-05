# Claude instructions

The canonical repository instructions are in [`agents.md`](agents.md). Read and follow that file and the full `AGENTS.md` compatibility mirror before making changes.

**avoid git rebase in favor of git merge.** Resolve conflicts semantically with full context, inspect 3–10 relevant prior commits when useful, preserve compatible intent, keep all work linked to Linear before implementation, operate non-destructively, protect secrets, and validate before claiming completion.

<!-- ore-org-baseline:begin -->
Read and obey [`agents.md`](agents.md); the lowercase file is canonical.

At minimum: preserve concurrent work; fetch before editing and before pushing; avoid git rebase in favor of git merge; never use `git stash`, `git reset`, `git clean`, `git filter-repo`, force-push, or another destructive operation without exact authorization; resolve conflicts semantically using the merge base, 3–10 relevant commits, tests, contracts, Linear context, and related repositories; never choose `ours` or `theirs` wholesale; scan for conflict markers; validate affected behavior; and never claim remote completion without authoritative evidence.
<!-- ore-org-baseline:end -->
