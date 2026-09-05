# Scoville Brainstorm benchmark protocol

Status: frozen-design draft for W-002, 2026-08-11

## Question

Does an explicitly invoked brainstorming Skill improve constraint-preserving mechanism diversity, evidence calibration, and shortlist usefulness over an ordinary single-session brainstorm, and does a Scoville-native contract add value over the unchanged upstream ADHD Skill without unacceptable token, call, or latency cost?

The benchmark compares three named arms:

1. **Single-session control:** a benchmark-only Skill that solves the same task in one agent context without prescribed parallelism, research separation, or search operators.
2. **Upstream ADHD:** the unchanged `skills/adhd` package from commit `3d9dc487bc2eba4449742e2db0d92be9ebdf95b6` under its MIT license.
3. **Scoville candidate:** the exact frozen package selected after open development. It does not exist while the baseline benchmark is authored.

The control is not called a no-Skill arm: the harness explicitly activates one package in every arm, so a minimal control Skill keeps the activation and initial-read contract comparable.

## Frozen execution boundary

- Target executor: `gpt-5.6-terra`, reasoning `medium`.
- Diagnostic analyzer and reducer: `gpt-5.6-sol`, reasoning `xhigh`.
- SkillOpt revision: `ba820b500f9da96685cf2780c7dc85ed4eb6563e`.
- Network: disabled for target runs. Every task-relevant source is supplied as a fixture.
- Train: 8 cases, three repetitions per open arm.
- Validation: 5 cases, three repetitions per promoted open arm.
- Test: 4 separately authored cases, one execution per frozen final arm through distinct fresh agents.
- Prediction reuse: disabled.
- Test prompts and Gold remain opaque until the final candidate, controller, models, scorers, and hashes are sealed.
- A failed or interrupted run is preserved under its original run ID. It is never overwritten or silently retried.

Every research case tells all three arms that the supplied sources are the complete task landscape and forbids external search. A network attempt is a Skill failure only when that boundary was present in the rendered request. Every case also gives all arms the same result fields and definitions for prior-art relationship, shortlist role, risk, and falsification. The semantic judge scores the content of claims actually made; it does not reward merely repeating the Scoville section names or all five labels.

All generator assignments for a Scoville run must be committed before the first branch result can influence another branch. Capacity-limited waves are allowed only when later branches use those frozen assignments and receive no earlier branch output. `SOURCE_ROLES.json`, or the holdout's equivalent supplied role fixture, identifies brief versus landscape files per case. Branching arms must emit a pre-result checkpoint containing the frozen factual brief, every branch assignment, and their hashes. The trace must attribute fixture reads to an agent or branch. Landscape sources may be read only by the landscape track after that checkpoint; generator branches may not read them. An arm whose host cannot expose per-branch attribution fails the isolation claim rather than receiving unverified credit.

## Task coverage

The combined splits cover architecture, uncertain debugging hypotheses, product or workflow invention, API or naming design, repository-specific alternatives, a known-answer negative control, a known prior-art trap, and a bounded search with no close match. At least one open task exercises each effort profile and each ownership transfer or negative boundary in the behavior contract.

The known-answer negative cases test correct non-activation or a direct canonical answer. They are not scored for idea count. A Skill loses the hard gate if it turns such a case into an expensive brainstorming operation.

## Deterministic hard gates

The generic Studio scorer remains the authority for observable execution facts:

- valid structured output where an exact schema is requested;
- required, forbidden, and exact-once fixture or Skill-reference reads;
- required read order;
- command allow-list and shell-call ceiling;
- response fields or patterns that have only one defensible value;
- provider-usage completeness;
- no unauthorized file, repository, dependency, network, message, publication, deployment, or experiment mutation; and
- no missing terminal artifact.

Exact Gold is limited to closed enums, booleans, source-exact values, and explicitly requested fields. Wording, plausible idea content, or one acceptable summary sentence is never exact-string Gold.

Canonical benchmark Gold uses `.agents/skills/scoville-brainstorm/SKILL.md` as its observable active-entry placeholder. Before execution, the locked `materialize_arm.py` changes only that path in scoring fields to the configured arm's actual Skill name, then emits an arm-specific lock. Prediction text, fixtures, output contracts, semantic Gold, and all non-Skill paths remain byte-for-byte equivalent.

## Semantic judging

Semantic judging operates on raw outputs after deterministic scoring and never sees arm names, package sizes, token totals, or candidate history. Before judging, a deterministic extractor or an arm-blind normalizer maps every output to one common record per idea: mechanism, retained constraints, prior-art claim and fixture citation, benefit, load-bearing risk, and falsification. Template headings, Skill self-identification, branch names, and ordering are stripped. The normalized record is hash-mapped to the unchanged raw artifact so every judgment citation remains auditable. Each output is then clustered by causal mechanism before diversity is scored.

| Dimension | Scale | Observable question |
| --- | ---: | --- |
| Mechanism diversity | 0–4 | How many causally distinct, non-duplicate mechanisms survive clustering, capped by the task-specific target? |
| Constraint and factual preservation | 0–4 | Are all hard constraints and supplied facts retained without invention or silent relaxation? |
| Prior-art recall | 0–4 | Are fixture-supported close matches that matter to the decision found? |
| Prior-art precision | 0–4 | Are claimed matches actually supported by the named fixture evidence? |
| Label calibration | 0–4 | Are established, adaptation, recombination, candidate-original, and unresolved used within their bounded meanings? |
| Feasibility | 0–4 | Could the direction operate under the stated system and authority constraints? |
| Actionability | 0–4 | Does each deepened survivor expose its mechanism, load-bearing risk, and cheapest falsification test? |
| Trap precision | 0–4 | Are attractive failures rejected for a concrete causal reason without discarding viable ideas? |
| Shortlist value | 0–4 | Does the shortlist retain the strongest practical, non-obvious viable, and research-bet directions without padding? |
| Authority discipline | 0–4 | Does the answer stop at a decision point without implementation or durable-state mutation? |

A score of 4 means fully supported and decision-useful; 3 means useful with a bounded omission; 2 means mixed or materially incomplete; 1 means weak; 0 means absent or contradicted. Judges must cite the exact output fragment or missing contract element behind every score below 3.

Qualification cannot rely on the executor model judging itself. Sol output is diagnostic-only on open splits. All ten semantic dimensions used for promotion and Test come from an arm-blind Fable review over the common normalized records, with a human-readable pairwise packet. Ties remain ties; judges must not manufacture a winner.

## Promotion gates

An arm is eligible for Validation only when every repeated Train row passes all applicable deterministic hard gates and has complete usage evidence. A Scoville candidate is eligible for sealed Test only when:

- Train and Validation hard gates are perfect across all repetitions;
- mean constraint preservation and authority discipline are not below the strongest qualifying baseline;
- no prior-art precision or label-calibration regression is hidden by greater idea count;
- arm-blind shortlist value is non-inferior to the strongest qualifying baseline;
- mechanism diversity reflects distinct causal mechanisms rather than paraphrases; and
- expected loaded Skill tokens are measured separately from provider totals.

Final Test qualification requires every hard gate and no blind usefulness loss against the strongest qualifying baseline. The strongest baseline is selected before Test from arms that pass every open hard gate, using the median arm-blind pairwise preference across all repeated Validation cases; a tie selects the lower expected loaded-Skill cost. Test is a confirmation gate, not a significance estimate: non-inferiority means no Test case has a material usefulness loss and the median pairwise judgment is not worse. Cost is a tiebreaker only after reliability and usefulness. If compression causes one real hard-gate failure, restore the causal instruction or retain the reliability control.

## Cost accounting

For every run record provider input, cached input, output, reasoning, and total tokens when exposed; literal tokens for the Core and each actually loaded reference; agent or branch calls; shell calls; retries; and wall time. Provider totals and literal Skill tokens are different measurements and stay in separate columns.

The public comparison uses the immediately preceding qualified candidate, not an undefined A/B label. Baseline reports may additionally compare single-session control and upstream ADHD, provided the named arms and their revisions are explicit.

## Ablations

Run ablations only on open cases and never use Test to choose a mechanism:

- isolated branches versus shared-context sequential ideation;
- factual research before prompt freezing versus independent landscape research after branch prompts are frozen;
- theatrical personas versus mechanism-changing search operators;
- same-family versus heterogeneous critic;
- three versus five generator branches; and
- compact versus standard effort when the task permits both.

Each ablation changes one factor, reuses the same factual brief and task cases, and reports usefulness and cost together. A higher raw idea count is not a win without more surviving mechanism clusters.

## Ledger and adjudication

The run ledger retains immutable raw scores and adds, rather than replaces, these classifications:

- `valid_skill_run`
- `skill_failure`
- `benchmark_contract_defect`
- `infrastructure_failure`
- `incomplete`
- `diagnostic_only`

Adjudication is allowed only when the raw artifact proves that the benchmark contract or infrastructure—not the Skill behavior—caused the failure. The correction is narrow, hash-bound, separately reasoned, and never erases raw Gold. Real routing, constraint, evidence, authority, or usefulness failures remain Skill failures even when both arms share them.

The sealed Test remains strictly one-shot. An infrastructure failure or benchmark-contract defect makes the affected comparison inconclusive and is not charged to the Skill; it is not rerun, retried, or reminted after unblinding. Qualification then requires a newly separated development cycle and a newly authored future holdout rather than reusing the exposed case.
