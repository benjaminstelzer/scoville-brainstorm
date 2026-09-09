---
format_version: 1
id: PLAN-0003
status: completed
created: 2026-09-09
updated: 2026-09-09
---

# Close completed ideation agents

## Goal

Bound the lifecycle of generator, landscape, Research-owned lane, and critic agents so collected results survive verified closure and unavailable close capacity remains explicit.

## Non-goals

- Do not change activation, profiles, frozen prompts, isolation, convergence, or output schemas.
- Do not raise global agent limits or rewrite benchmarks, snapshots, frozen controls, evaluations, backups, vendor files, or outputs.
- Do not publish, release, or replace installed Skill bytes.

## Work items

### W-001 Add and validate branch-agent closure
Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Brainstorm preserves each branch result and provenance, releases completed agents when possible, and degrades honestly when closure or capacity is unavailable.
Acceptance: RUN checks close capability and observable capacity; COLLECT preserves results and handles before verified closure; active descendants remain open; native and Research-owned landscape lanes plus an independent critic follow the same boundary; status questions resume waiting; blockers surface immediately; the Skill validator and lifecycle scenarios pass without claiming a live close.
Steps:
1. Add the lifecycle boundary to RUN, COLLECT, critic use, waiting, and blockers.
2. Inspect the package-only diff and run existing tests and the Skill validator.
3. Exercise bounded capacity, optional critic, combined landscape, active-descendant, status-question, and blocker scenarios without spawning an agent.
Evidence: [Documented unittest discovery found zero tests; two v2 normalizer tests passed; Skill quick validation passed, Lifecycle contract scenarios passed without live close_agent execution; native profile validation passed]
