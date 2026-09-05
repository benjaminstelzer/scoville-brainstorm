# W-004 open diagnostics

Date: 2026-08-11

This is development evidence, not a qualification report. The opaque Test
payload remained unexecuted and was accessed by the coordinator only through
its seal, byte count, and SHA-256 binding.

## Reliability v2

The frozen v2 candidate did not qualify across repeated open Train runs. Its
hard results were 5/8, 6/8, and 5/8. Later targeted diagnostics showed that
batched task-source reads were not reliably assimilated by the Terra executor:
the shell trace contained nonempty source data while the response sometimes
reported an empty source ledger. Separate one-file reads improved the result,
but one of three Product repetitions still discarded visible tool output.

The exact historical package and controller binding are recorded in
`w004-reliability-v2-manifest.json`. Raw Studio artifacts remain under the
`scoville-brainstorm-v2-*` run roots.

## Source-mirror v3

v3 added an authoritative mirror of the same public task fixtures to each
agent request while retaining real one-file reads as trace evidence. This
separates Skill semantics from the observed CLI tool-output transport defect.
The benchmark was frozen before model calls with 8 Train, 5 Validation, and 4
opaque Test cases.

The first v3 Train run was stopped after two completed rows because both exposed
a benchmark defect: Studio had already injected the full Core as system
instructions, but its user prompt also required a filesystem read of that Core.
Codex consequently read `SKILL.md` twice. Both completed artifacts passed the
requested semantic output contract; raw hard scores failed only exact-once and
shell-budget checks caused by the duplicate Core reads. The interrupted run is
retained as diagnosis and cannot qualify the Skill.

## Injected-Core v4 and later reliability work

v4 makes the actual execution boundary explicit:

- the full Core is already loaded in system instructions;
- the agent must not inspect `SKILL.md` through a tool;
- loaded-Core tokens are counted even without a shell read;
- only user-named task sources remain in exact-once and shell-budget gates;
- Train and Validation load without parsing the sealed Test payload;
- the Test payload loads lazily only for an authorized `valid_unseen` run.

The v4 open splits were derived mechanically from v3. A separate blind author
applied the same transformation to Test and resealed it without disclosing its
items or Gold. Later open iterations exposed three more evaluation or contract
problems that could otherwise be mistaken for Skill behavior:

- final-answer booleans cannot prove process topology or branch isolation;
  those facts now remain trace-owned;
- activation cannot be judged from a semantic answer produced after the Core
  was already injected, so description-only activation has a separate gate;
- a generic request to read every materialized path contradicted explicit
  negative controls that required zero reads; the harness now obeys explicit
  no-read instructions and never treats fixture existence as a read mandate.

The v11-v13 contracts removed process and activation self-report from semantic
artifacts and made fixed-constraint reporting explicit wherever a case requests
it. The opaque Test was not changed when its blind author confirmed that none
of its output contracts requested those fields.

## Compact Fable review

Fable 5 High found three concrete single-Core gaps: no zero-subagent fallback,
an ambiguous sentence implying no tool could follow the ledger checkpoint, and
no default output slot for process degradation. The candidate now permits
truthfully degraded coordinator passes when isolated agents do not exist,
clarifies that the ledger is plain working-state text, and includes Process
evidence in the default artifact. Skill Creator validation passes after these
changes. A second focused Fable 5 High review returned `READY` for all three
corrections.

## Exact-byte open qualification

The final reliability candidate was repeated on the complete open split with
its exact current bytes:

- Train: `v14-train-r1`, `v14-train-r2`, and `v14-train-r3`, each 8/8;
- Validation: `v14-val-r1`, `v14-val-r2`, and `v14-val-r3`, each 5/5;
- combined semantic gate: **39/39**, with no Skill, infrastructure, or retry
  failure;
- description-only activation gate: **36/36** across 12 positive and negative
  cases repeated three times, with no tool calls.

The qualified Core is 8,060 bytes and 1,712 loaded Skill tokens, SHA-256
`144590B8D3804945D9181C08DBEB5F71286CF76896415FA2AECC687560EAD40B`.
Its frozen reliability-control snapshot is
`skillopt-studio/snapshots/scoville-brainstorm-v14-reliability-control`.

## Live orchestration check

A separate integration check used two fresh isolated generator agents, a
landscape agent that saw only bounded prior-art patterns, and a fresh critic
that received candidate and landscape summaries only after divergence. The
generators produced four mechanisms. The critic clustered overlaps, preserved
the fixed constraints, identified one conditional hazard, and selected a
practical direction, a non-obvious viable direction, and a research bet. This
checks the actual orchestration boundary that cannot be proven by final-answer
self-report.

## Reduction policy

Brainstorm loads one Core and no conditional references. Compression therefore
has much less practical value than it has for repeatedly routed Skills. One
conservative SkillOpt/SkillReducer-style comparison is permitted against the
frozen reliability control. A shorter candidate may replace the control only
if it preserves every open gate; otherwise the qualified control remains the
release candidate.

That comparison ran as `v15-conservative-reducer-r1` on Microsoft SkillOpt
commit `ba820b500f9da96685cf2780c7dc85ed4eb6563e`. Sol 5.6 xhigh analyzed and
Terra 5.6 Medium executed. The eight-case Train rollout passed 8/8. SkillOpt
performed one optimization step, rejected it, accepted no edit, and retained
the initial Skill byte-for-byte. The only raw baseline-selection miss was the
already documented output-contract type ambiguity (`false` versus `[]`) in a
negative control; activation, answer, zero-read, and no-side-effect behavior
were correct. The selected package therefore remains the frozen 1,712-token
reliability control. Relative to that immediately preceding candidate, the
loaded-token change is 0%; there is no previous released Brainstorm version for
a meaningful release-to-release savings claim.
