---
name: scoville-brainstorm
description: Use only to explore materially different solution mechanisms before a choice, with isolated generation, bounded prior-art comparison, calibrated originality language, and a decision-ready shortlist. Activate for explicit Scoville Brainstorm, or when a task explicitly requests several materially different solution mechanisms, unusual alternatives, unknown-root hypotheses with falsifiers, fundamentally different directions, or separation of established approaches from directions worth pursuing. Never activate or load for an open question seeking one answer, a canonical answer, known-root fix, ordinary implementation or review, wording or naming work, one small reversible change, durable planning, or session transfer.
---

# Scoville Brainstorm

Read-only divergence before a material choice. For `YES` only, execute once:

`CORE -> READ -> FRAME -> FREEZE -> RUN -> COLLECT -> CONVERGE -> RENDER -> STOP`

Process state is trace-owned:

`profile_targets={Compact:<=3,Standard:<=5,Deep:6..8}; spawned=successful tool-observed spawn/delegation calls; landscape_mode=native|research-owned`

Named roles, reasoning passes, or imagined agents never count as isolated generators,
a separate landscape agent, or an independent critic. Do not self-report spawn
topology or isolation in coordinator text or the decision artifact; a host or
evaluator may attach those facts only after inspecting calls and branch prompts.

## Dispatch

Before answering any explicit combined Research and Brainstorm request, the next
operation after Core is one observable read of
[research-composition.md](references/research-composition.md). Answering that
request from Core alone is invalid even when the topology appears inferable.
The loaded reference owns the exact `explicit_combined` mode and retrieved-data
trust boundary.

- Route by decision shape, not domain: an unknown root cause plus a request for
  several materially different failure mechanisms is `YES`; debugging is `NO`
  only after one cause is established or the request asks for direct diagnosis,
  implementation, or review.
- `NO`: canonical or single answer; known root cause; selected implementation,
  review, wording, small reversible work, durable planning, or transfer. Return
  the ordinary answer immediately. Run no tool and
  read no task source or inert fixture.
- `ASK`: broad exploration versus one answer materially changes cost and intent
  is unclear. Ask one question; read no task source.
- `YES`: explicit brainstorming or several materially different, unusual, or
  underexplored directions. Explicit invocation bypasses only the cost question,
  never authority or safety. A host instruction to use this Skill fixes `YES`.
- `COMBINED`: after `YES` and before `READ`, when the user explicitly requests
  Scoville Brainstorm together with Scoville Research and Research is
  independently available and applicable, read
  the reference exactly once and set `landscape_mode=research-owned`. Otherwise
  keep `landscape_mode=native` and do not read the reference.

## Machine

1. **CORE:** The catalog/discovery read that exposed this body is activation and
   the only Core read. Never read, stat, list, or inspect it again.
2. **READ:** Read only every user-named task source, one file per shell operation
   and exactly once, so each tool result has one unambiguous owner. Never batch
   files or infer `README.md`, `AGENTS.md`, or another default; inventory, probe,
   retry, dummy command, metadata check, and later file IO are forbidden. Retain
   every nonempty result by its command path. A failed path invalidates only
   itself.
3. **FRAME:** Build one in-memory brief: outcome, language, effort profile,
   supplied facts and owners, hard constraints and authority, challengeable and
   fixed assumptions, and permitted source scope. From each non-landscape brief
   block, first scan every literal colon-terminated ID label such as `- D1:`,
   then copy all IDs character for character and in source order into
   `fixed_ids`; never synthesize, rename, or take IDs from an output contract.
   Include the final label and authority, selection-only, stop, or no-mutation
   labels. The label count and `fixed_ids` count must match before interpreting
   content. Observation versus rule does not change membership. If any
   non-landscape source contains a labeled line,
   `fixed_ids=[]` blocks `FREEZE` and `RENDER`; populate it first from the ledger.
   Before ideation, emit one compact nonfinal trace checkpoint:
   `LEDGER blocks=<count>; fixed_ids=<exact comma list>`. It is working state,
   not part of the requested artifact; emit it as plain text,
   never through or for a tool.
   Resolve factual uncertainty only when it changes this frame; do not research
   solutions yet.
4. **FREEZE:** Set the profile target from Process state. Before any
   branch starts, freeze every full generator prompt plus stable ID and content
   hash from the same brief. For `landscape_mode=native`, also freeze the native
   landscape prompt. For `landscape_mode=research-owned`, freeze the Research
   handoff contract and never freeze or dispatch a second landscape prompt.
   Later waves see no earlier output. Cover distinct causal operators, including
   one load-bearing-assumption challenge and one strongest practical comparator.
5. **RUN:** When fresh isolated agents are available, launch one per generator
   and, only for `landscape_mode=native`, a separate landscape agent, in parallel
   up to capacity. In `research-owned` mode the combined protocol supplies one
   Research-owned lane after generator collection; do not launch a native
   Brainstorm landscape agent. Generators receive
   only the brief, one operator, and a request for mechanism, preserved
   constraints, benefit, load-bearing risk, and cheapest falsifier. They never
   see sibling output or landscape evidence. The landscape agent sees only fixed
   facts and permitted sources and reports close matches, failed approaches,
   scope, and unresolved evidence. When `spawned=0`, freeze one consolidated generator prompt before
   ideation, run it once in the coordinator, and apply Process state exactly.
6. **COLLECT:** Wait until every started branch is terminal. Keep raw outputs
   separate and count the distinct surviving ideas. A failed branch is missing
   evidence, never permission to invent it. Accept exactly one applicable
   landscape result: native in standalone mode or Research-owned in combined
   mode.
7. **CONVERGE:** Normalize candidates to mechanism, constraints, evidence
   relationship, benefit, risk, and falsifier; merge paraphrases; reject broken
   constraints and unsupported facts; identify traps. Use the one collected
   landscape result as the sole landscape input. When available, use an
   independent critic. Retain at most three distinct directions (Compact: two)
   and deepen only those. Reject every direction breaking a `fixed_id` before
   `RENDER`.
8. **RENDER:** Obey the user's exact schema, key order, language, and closed
   values. Schema types dominate defaults: emit a requested scalar or enum as
   that scalar, never an enriched object. Otherwise return, in order: Brief,
   Landscape, Idea map, Shortlist, Traps, Deepened directions, Decision point.
   Prefer the smallest complete
   artifact over a branch transcript. In structured output, set
   `activation.activated=true` only when the schema requests activation; seal
   `brief.fixed_constraint_ids=fixed_ids` and implementation/experiment/
   durable-record flags `false`.
   `external_search_performed` reflects actual tool use; named fixtures alone
   mean `false`. `constraints.violated` contains only IDs from `fixed_ids` that
   the proposed directions actually break; never include a challenged
   assumption, current defect, process limitation, or free-text sentinel. When
   no fixed ID is broken, emit `[]`; after `CONVERGE`, a completed artifact
   therefore emits `constraints.violated=[]`. For JSON,
   pretty-print with two-space indentation,
   one key or value per line, and each closer on its own opener-matched line.
   Check required top-level fields once.
9. **STOP:** Return the decision artifact. Do not select for the user, edit,
   install, run a falsifier, create a Plan or Decision, send, publish, or deploy.

## Evidence labels and transfer

Use exactly one label per candidate: `Established` = close same mechanism;
`Adaptation` = known mechanism transferred to a materially different context;
`Recombination` = known mechanisms whose interaction creates the difference;
`Candidate-original` = no close match in the documented bounded search; and
`Unresolved` = insufficient evidence. None proves novelty or patentability.

Transfer only after human selection. Family standalone:
discovery != installed|active|applicable|required; absent|inactive => ignore/no
require|install|simulate|reimplement; active+applicable => owner concern only,
self continues; opt-out local.

Other owners: `scoville-code-anti-ai-slop` engineering/proof;
`scoville-ui-anti-ai-slop` interface/rendered proof;
`scoville-scribe-anti-ai-slop` wording/fidelity; `scoville-plan`
records/lifecycle; `scoville-handoff` transfer.
