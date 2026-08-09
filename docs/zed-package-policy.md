# Fiducia Zed package policy

This policy applies to every Zed package in the `fiducia-cloud` GitHub organization.

## Canonical coordinates

- Use `fiducia-cloud` as `[package].org`.
- Package dependencies must use the same canonical organization, for example `fiducia-cloud/fiducia-interfaces`.
- Do not add a dependency for a repository or package that does not exist. Track the missing topology explicitly instead.
- Use the repository's real package version and source URL. Do not claim a published version that has not been released.

## Source artifacts and native artifacts are different claims

A valid Zed source package does not prove that a native package can be published.

Declare a native registry route only when all of the following are true:

1. the native package root is isolated from unrelated language/package roots;
2. the native manifest name and version match the coordinated release;
3. the native package manager accepts every dependency source;
4. licensing permits redistribution;
5. a dry run succeeds from the exact revision;
6. CI verifies an install from the produced artifact.

Examples of invalid native claims include:

- a crates.io package whose Cargo manifest contains Git dependencies;
- a polyglot target rooted at `.` presented as one isolated crates.io crate;
- a native package still at `0.1.0` declared as a coordinated `0.2.0` release;
- an `UNLICENSED` private package routed to a public registry.

When a native route is not truthful, keep the Zed source artifact and document the exact prerequisite for enabling native publication later.

## Target isolation

Every target must own an isolated source root. Multiple runtime targets cannot point to the same directory merely because the implementation is portable.

For Node.js, Deno, Bun, and edge runtimes, choose one of these designs:

- one runtime-neutral Zed target with separately tested runtime compatibility; or
- isolated, self-contained runtime packages generated from one canonical source with a fail-closed drift check.

Do not duplicate a mature SDK with placeholder client classes simply to satisfy a directory matrix.

## Lockfiles

- Generate `.zpkg.lock` with the canonical resolver.
- A lock containing only `version = 1` is valid only when the manifest has no Zed dependencies.
- Never hand-author dependency source, checksum, or revision records.
- A dependency change and its regenerated lock must be reviewed together.

Native Cargo, npm, Dart, and other lockfiles remain owned by their native package managers.

## Installation and publication exclusions

Project installs should use the canonical repository-local directory:

```toml
[install]
dir = ".vendor/.zed"
```

Publication exclusions must include `.vendor/.zed/**` and generated dependency/build trees appropriate to the repository.

## Security exceptions

A vulnerability exception must be narrower than the advisory itself.

For optional packages present only in a native lockfile:

1. compile, lint, and test the supported feature surface;
2. ask the native package manager for the feature-unified build tree;
3. fail if the affected package is reachable;
4. only then apply the single named audit exception;
5. remove the exception when the upstream lock can be updated.

A raw lockfile or metadata resolve list is not an execution-reachability proof.

## Pull-request merge gate

Before merging a package PR:

- the exact final head must pass repository CI and canonical Zed validation;
- the PR description must distinguish source packaging, native publication, and actual release state;
- no unresolved review thread may remain;
- publication credentials, tags, releases, and registry mutations must not be introduced unless the PR is an explicitly approved release workflow;
- overlapping package PRs must be reconciled semantically, not merged in arbitrary order.

A merged manifest is not evidence that a registry artifact, tag, release, or downstream frozen installation exists.
