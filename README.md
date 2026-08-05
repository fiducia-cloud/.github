# fiducia-cloud organization context

This special public `.github` repository is the discoverable organization anchor for humans and AI agents.

- `profile/README.md` is the visible organization profile.
- `project-context.yaml` is the generated GitHub owner ↔ Linear project mapping.
- `org-context-manifest.json` records deterministic SHA-256 hashes for every other managed file.
- `agents/org-context.agent.md` is the organization-level GitHub Copilot custom-agent profile.
- `.github/workflows/org-context-integrity.yml` verifies this mirror against its immutable central registry commit.
- The generated profile and custom agent carry the mandatory semantic Git conflict-resolution policy.

The source of truth is the reviewed central registry named in `project-context.yaml`. Generated files should not be edited independently. Keep this repository public-safe.

<!-- ore-org-baseline:begin -->
## Account-wide defaults

This public repository is the canonical source for GitHub-supported fallback community files, organization profile content, reusable workflow examples, and public contributor guidance for [`fiducia-cloud`](https://github.com/fiducia-cloud).

- GitHub owner: [`fiducia-cloud`](https://github.com/fiducia-cloud)
- Linear project: [github.com/fiducia-cloud](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3)
- Public context: [`ORG_CONTEXT.md`](ORG_CONTEXT.md)
- Canonical agent policy for this repository: [`agents.md`](agents.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Public repository graph: [`repository-relationships.json`](repository-relationships.json)
- Relationship guide: [`docs/REPOSITORY_RELATIONSHIPS.md`](docs/REPOSITORY_RELATIONSHIPS.md)
- Security reporting: [`SECURITY.md`](SECURITY.md)

GitHub applies only its documented fallback community files automatically. Agent instructions, relationship files, and reusable workflows are **not copied into sibling repositories**; repositories that need local enforcement must carry their own lowercase `agents.md` and explicitly call or copy the provided workflow.

`repository-relationships.json` retains the owner's existing contract. A generated public graph is staged under `.github-hardening/proposed/relationship-graph-v1/` for semantic compatibility review. It is public-safe: private repository names are omitted. The complete graph is synchronized separately to the approved private project registry.

## Safety baseline

Changes are pull-request driven. Contributors and agents must preserve concurrent work, avoid destructive Git operations, resolve conflicts semantically with full history and cross-repository context, validate affected contracts, and never claim a remote action completed without authoritative evidence.

Generated baseline version: `2026-08-04`.
<!-- ore-org-baseline:end -->
