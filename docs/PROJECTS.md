<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [fiducia-cloud](https://github.com/fiducia-cloud)
- **Canonical GitHub Project:** [fiducia-cloud-project](https://github.com/orgs/fiducia-cloud/projects/1) (project 1)
- **Canonical Linear project:** [planning workspace](https://linear.app/denman/project/githubcomfiducia-cloud-8fd5e1bec9d3)
- **Organization documentation repository:** [fiducia-cloud/.github](https://github.com/fiducia-cloud/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, commits, pull requests, reviews, CI checks, releases, deployable artifacts, and runtime evidence. Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. The GitHub Project is the organization-level execution board and should contain the governance issue maintained by this repository.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.
<!-- org-project-routing:end -->

## Audited organization snapshot

The production-organization repository snapshot dated **2026-08-05** contains **34 repositories**: **33 active** and **1 archived**. The sole archived repository is `fiducia-customer-ui.web`. The machine-readable source is [`repository-map.json`](./repository-map.json), and the human routing view is [`REPOSITORY_MAP.md`](./REPOSITORY_MAP.md).

This snapshot is an inventory and routing classification. It does not certify that a repository is implemented, deployed, secure, released, supported, or production-ready. Independent release certification remains governed by the production/test boundary above.

## Repository evidence lifecycle

1. Product intent, priority, owner, blockers, and acceptance criteria live in the shared `fiducia-cloud` Linear project.
2. Every code or policy change uses a branch and commit message that include the Linear identifier when one exists.
3. The pull request links the Linear issue and records exact validation evidence.
4. Required production checks pass before merge; conflicts are reconciled semantically against the latest default branch.
5. Merge, release, deployment, and product-side evidence are linked to the production GitHub Project item.
6. Independent acceptance evidence is linked from the test-fleet GitHub Project item to the same Linear issue.
7. A Linear issue is not completed merely because a pull request exists; the acceptance criteria and required evidence must be satisfied.

## Recommended GitHub Project fields

Both organization Projects should use one item per durable issue or pull request and, at minimum, expose:

- **Status:** Backlog, Ready, In progress, In review, Blocked, Done.
- **Repository:** exact owning repository.
- **Linear:** canonical issue identifier in the shared project.
- **Workstream:** one routing category from the repository map or independent test catalog.
- **Evidence:** pull request, workflow run, release manifest, deployment, or certification bundle.

Automation may mirror status, but Linear remains authoritative for planning state and GitHub remains authoritative for engineering and certification evidence.

## Public-data boundary

Do not place credentials, mailbox bodies, private application answers, legal attestations, customer data, payment details, or unpublished funding information in this public repository or either public GitHub Project. Public application reporting should use bounded outcome metadata and non-secret evidence references only.
