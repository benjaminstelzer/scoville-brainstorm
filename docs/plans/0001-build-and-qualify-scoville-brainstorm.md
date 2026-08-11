---
format_version: 1
id: PLAN-0001
status: active
created: 2026-08-11
updated: 2026-08-11
current_item: W-007
---

# Build and qualify Scoville Brainstorm

## Goal

Create a portable, token-conscious Scoville Skill that deliberately broadens the solution space before a decision: independently explore materially different mechanisms, research bounded prior art without anchoring generators, distinguish established approaches from adaptations, recombinations, and candidate-original directions, and return a compact evidence-linked shortlist for human selection before Code or Plan takes ownership.

## Non-goals

- Do not turn ordinary implementation, review, debugging with a known root cause, or small reversible work into a brainstorming exercise.
- Do not replace Scoville Code's engineering ownership, Scoville Plan's durable decisions, Scoville Scribe's wording ownership, Scoville UI's interface ownership, or Scoville Handoff's transfer ownership.
- Do not claim patent novelty, scientific originality, or exhaustive prior-art coverage from a bounded search.
- Do not edit project files, run proposed experiments, publish results, or perform other side effects as part of brainstorming alone.
- Do not maximize raw idea count at the expense of factual correctness, constraint preservation, mechanism diversity, usefulness, or token cost.
- Do not hard-code one provider, one fixed agent count, or one host-specific orchestration path into the portable behavior contract.

## Work items

### W-001 Establish the behavior, activation, and suite-ownership contract
Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001]
Outcome: One reviewable contract defines when Scoville Brainstorm activates, what remains fixed during divergence, how isolated research and idea generation interact, how candidate originality is described, what the final shortlist contains, and where ownership transfers to other Scoville Skills.
Acceptance: The contract covers explicit English and German positive requests, ordinary-work negative cases, read-only and authority boundaries, prompt freezing before isolated branches run, compact/standard/deep effort profiles, mechanism-based search operators, bounded prior-art categories, clustering, independent criticism, seductive-trap handling, the three-direction shortlist, cheapest falsification tests, and the exact stop before implementation; every claimed ADHD, research, or suite behavior is linked to a primary or inspectable source; no unresolved implementation choice is presented as accepted.
Steps:
1. Freeze the current Scoville sibling ownership and the inspected upstream ADHD behavior as source evidence.
2. Write concrete positive, negative, ambiguous, and composition examples for the behavior contract.
3. Specify the frame, isolated landscape and divergence tracks, clustering, comparison, selection, deepening, and decision handoff.
4. Define host-capacity adaptation and the compact, standard, and deep cost profiles without weakening branch isolation.
5. Review the complete contract for activation overlap, unsupported novelty claims, authority leakage, and unnecessary loaded instructions.
Evidence: [behavior contract SHA256 0A08127BC4A7766DE0BA701370ECC58C2F9D50F52EBEC59C51A15D8659EB59AA covers all 11 required sections, source map SHA256 B618BA882A10F6D3612DCBA968F34434090703404FA4204356DB5772CEDB4ADB pins ADHD and five siblings, five indexed research PDFs passed PDF signature and SHA256 checks]

### W-002 Build a contamination-resistant benchmark and compare baselines
Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0001]
Outcome: A frozen benchmark compares an ordinary single-session brainstorm, upstream ADHD, and the Scoville contract across representative creative and negative-control tasks without leaking cases or intended answers into later candidates.
Acceptance: Before model calls, the benchmark freezes Train, Validation, and opaque one-shot Test splits; task domains include architecture, uncertain debugging hypotheses, product or workflow invention, API or naming design, repository-specific alternatives, a known-answer negative control, a known prior-art trap, and a case with no close match in bounded sources; repeated open runs measure mechanism diversity after semantic clustering, constraint and factual preservation, source-backed prior-art recall and precision, novelty-label calibration, feasibility, actionability, trap precision, shortlist value, unauthorized side effects, provider tokens, loaded Skill tokens, agent calls, and wall time; deterministic checks and blind human or heterogeneous-model judgments are separated; same-model judging alone cannot qualify the Skill; isolation, research timing, search-operator, critic-family, and branch-count ablations are specified; every run, exclusion, infrastructure defect, and adjudication is retained in a reproducible ledger.
Steps:
1. Derive a coverage matrix from the behavior contract and define exact scored and judgment-based fields.
2. Author open Train and Validation cases plus a separately authored opaque Test split with immutable hashes.
3. Freeze models, effort, branch prompts, source access, execution order, scorers, repetition counts, cost accounting, and promotion gates.
4. Run the no-Skill and upstream ADHD baselines without exposing Test content to candidate development.
5. Publish the raw baseline report and the evidence needed to decide the implementation basis in ADR-0002.
Evidence: [benchmark lock SHA256 EFF995DD8637295A9530EF6F84B0D72A14767EF86EBEF6FBB227D1C1F185E9A1, opaque Test SHA256 9DA814D4C998A4C0D14B4FD7ED7CD51C43E42954422987E7379A2073CE4B7FBB remained unopened and unexecuted, formal Terra 5.6 Medium baselines completed 24 Train cases per arm, control passed 6 of 24 hard cases, host-normalized ADHD passed 9 of 24 hard cases, neither arm reached Validation or Test, raw aggregate SHA256 6FAACF4520599D3AE6CF30F65529F61B773635D8C2F2AB95A825AC0E338F019C, report docs/evidence/w002-baseline-report.md, ADR-0002 accepted the host-portable native basis]

### W-003 Implement the first portable Scoville Brainstorm candidate
Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: One installable `scoville-brainstorm` package implements the selected orchestration basis, preserves isolated divergence and evidence boundaries across host capacities, and composes with every sibling without depending on one.
Acceptance: The package directory and frontmatter name are `scoville-brainstorm`; Skill metadata distinguishes explicit creative exploration from ordinary coding and prose tasks; the core contains only activation, fixed constraints, routing, authority, isolation, novelty-language, and output invariants; optional references are routed only when required; all branch prompts are frozen before outputs can influence later branches, including wave-based execution; research content is treated as data and cannot issue instructions; the package attributes adapted MIT-licensed ADHD ideas where applicable; no runtime dependency, script, reference, or provider requirement is added without a demonstrated recurring need; `agents/openai.yaml` matches the final Skill; Skill validation and static contract checks pass.
Steps:
1. Resolve ADR-0002 from W-002 evidence before selecting or adding a runtime dependency.
2. Initialize the package with the canonical Skill Creator tooling and only the resource directories justified by the contract.
3. Implement the smallest behavior-complete Core and any conditionally loaded references.
4. Generate matching OpenAI metadata and add attribution required by the selected basis.
5. Run Skill validation and inspect activation, routing, isolation, output, and sibling-composition contracts.
Evidence: [Skill Creator validation passed, package Core SHA256 86D3B8EE20D04913224A74AC9AB046837CD1CF5DC8E3835BD33B5CB584B05C11, orchestration reference SHA256 E80D6F7815CC0E16F224EB04702F4A3313B16DDBB768DF580F899809A0FFFF0D, evidence and output reference SHA256 C4D349F728697B01CAD2227155FDF65A7FFBC560CE288805C79C35D13F5C186C, MIT license SHA256 3F08D24B5561FC516B262351CB8E0302D30E7D9139F01B4A637E4BF3B5AB0938, Fable final regression review READY, every open Train case demonstrated at least one hard pass, Validation Deep smoke passed 1 of 1, report docs/evidence/w003-candidate-report.md, opaque Test remained unexecuted]

### W-004 Improve reliability first, then reduce expected loaded tokens
Status: done
Depends on: [W-003]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: Repeated open evaluation produces a reliability-qualified candidate, after which the current Microsoft SkillOpt base and a SkillReducer-style reduction minimize expected loaded instructions without weakening any behavior or useful creative outcome.
Acceptance: Terra 5.6 Medium or a documented comparable model executes the representative tasks and Sol 5.6 xhigh or a documented comparable analyzer diagnoses failures; genuine reliability, factuality, activation, isolation, novelty-classification, shortlist, or authority failures are corrected before token reduction; benchmark and harness defects remain raw evidence but do not become Skill failures; candidate revisions never read opaque Test content; the reliability control passes every hard open gate before reduction; SkillOpt optimization uses current upstream source and records its exact revision; reduction classifies essential, route-specific, redundant, and harmful instructions, measures Core plus actually loaded references, selectively restores instructions when behavior regresses, and promotes only a candidate that preserves every hard gate and does not reduce blind usefulness while lowering expected loaded Skill tokens.
Steps:
1. Run repeated open candidate evaluations against the frozen baselines and diagnose only evidenced failures.
2. Repair the smallest causal instruction, routing rule, or evaluation contract and rerun every affected open case.
3. Freeze the perfect open candidate as the uncompressed reliability control.
4. Optimize with current SkillOpt and the local reducer method while preserving raw A/B evidence and contamination boundaries.
5. Select the lowest-cost candidate that passes every reliability and usefulness gate, or retain the qualified control when no reduction qualifies.
Evidence: [docs/evidence/w004-open-diagnostics.md records the reliability and harness corrections; exact final bytes passed 39/39 repeated open semantic cases and 36/36 description-only activation cases; the live multi-agent integration preserved isolated generators, landscape, and independent criticism; Microsoft SkillOpt ba820b500f9da96685cf2780c7dc85ed4eb6563e ran one conservative Sol 5.6 xhigh/Terra 5.6 Medium reduction step, rejected its proposed step, and retained the 1,712-token reliability control byte-for-byte; the opaque Test remained unopened and unexecuted]
Next action: Seal and execute the one-shot opaque Test against the unchanged reliability control.

### W-005 Qualify the frozen candidate on unseen tasks
Status: done
Depends on: [W-004]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: A one-shot opaque evaluation establishes whether the frozen candidate preserves constraints, produces genuinely distinct and useful mechanisms, separates prior art honestly, and stops before implementation on unseen tasks.
Acceptance: The final package, controller, models, prompts, sources, scorers, and opaque split hashes are sealed before any Test execution; independent fresh agents execute each bound arm once with no memory, prediction reuse, retry, remint, or post-Test candidate edit; the candidate passes every exact safety, authority, source, constraint, activation, and output-contract gate; blind judgment finds no loss of practical shortlist value against the strongest qualified baseline and confirms mechanism diversity rather than surface variation; novelty labels remain within the bounded-search language; provider usage and literal loaded instructions are complete and reported separately; raw scores, semantic Skill scores, infrastructure failures, benchmark-contract defects, exclusions, total runs, total cases, and token deltas remain separately reproducible.
Steps:
1. Seal the final candidate and complete open-gate evidence without inspecting opaque Test content.
2. Mint one execution gate bound to exact package, benchmark, controller, model, and scorer hashes.
3. Run every Test arm once through distinct fresh agents and inspect results only after terminal completion.
4. Adjudicate only documented benchmark or infrastructure defects without changing raw results or relabeling real Skill failures.
5. Produce the qualification report and either retain the qualified package or return to a newly separated development cycle with an entirely new future Test split.
Evidence: [one-shot gate SHA256 74CA91225D69E66B781F8399AF4DEE21ABE163540E536E8C269D7375A3BB8149 and preflight SHA256 C68BD31B5679FC6F2E452D899A88BF72AD279F5FBF81D6D5275F6546D9E8CBA1 bound the exact 144590B8D3804945D9181C08DBEB5F71286CF76896415FA2AECC687560EAD40B Skill; one fresh Terra 5.6 Medium agent consumed the gate once with no retry or remint; the outer observer timed out with exit 124 while the original process remained alive and completed all four cases plus its terminal summary; raw score 2/4 preserved; two benchmark-contract contradictions were hash-bound and adjudicated without changing Gold or results; Skill score 4/4 with zero Skill failures; TEST_ADJUDICATED_RESULT.json SHA256 673C212C6D47E4C927D365DCA9BADC5F7BD82B2A30F8C340B1C8A83DB61304C6]
Next action: Build factual public documentation and install the unchanged qualified package locally.

### W-006 Align documentation, local installations, and release readiness
Status: done
Depends on: [W-005]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: The qualified Skill has factual Scoville-family documentation, byte-identical Codex and Claude installations, and a reviewed release candidate without publishing or changing sibling repositories prematurely.
Acceptance: README structure and terminology match the current Scoville family; installation identifies Terra 5.6 Medium or comparable such as Opus 4.8 as the minimum qualified executor; cost guidance explains when divergent research is worth the additional tokens and calls; Status reports the exact qualified cases, total optimization runs, and loaded-token change against the immediately preceding candidate; sources distinguish inspiration, adapted licensed material, and original Scoville mechanisms; sibling ownership and links are correct; Codex and Claude installations are byte-identical to the qualified package and contain no conflicting Brainstorm identity; validators, local links, package inventories, representative activation and negative checks, and the full scoped diff pass; no commit, push, tag, GitHub release, profile pin, or sibling-repository edit occurs without a later explicit publication request.
Steps:
1. Build the root documentation and benchmark evidence from the final qualification artifacts.
2. Verify every public claim, source, link, version comparison, run count, and token figure against the repository tree and raw evidence.
3. Stage and validate the exact package before updating Codex and Claude installations without duplicate discovery.
4. Run isolated activation, negative, cost-profile, and sibling-composition checks on both hosts.
5. Prepare the clean release diff and report the remaining external publication actions for explicit authorization.
Evidence: [README SHA256 6D2CA2EEEFB3DE73A286CF29093F7B99DD2C579CC2471D6B15624B9076BD995B contains the minimum executor, cost boundary, concise Status, family ownership, and no Verify-it-works section; docs/benchmark-evidence.md SHA256 B546C3B5BD9B8CCF0074F5A836C3E5C2C9F3584DC0F01B8A120F4E0501CF81B8 preserves raw and Skill scores, token measures, hashes, and limits; docs/optimization-runs.md SHA256 C04404F3F9EB5D9EAB4F03D7DB2FBE828D83814589672AD3484CE2BA42E76538 records 182 runs and 584 benchmark case executions; docs/evidence/w006-installed-host-smoke.md SHA256 2BF8821AD2FE1512F3A8D59B6220D89166D2FCD0741E1FFDE1E6166B55803BDD records the local copies and Claude checks; Skill Creator validation passed; 27 Markdown files have zero broken relative links; Codex and Claude each contain exactly one four-file scoville-brainstorm package byte-identical to Skill SHA256 144590B8D3804945D9181C08DBEB5F71286CF76896415FA2AECC687560EAD40B; Claude Code 2.1.220 passed one explicit Compact positive and one canonical-answer negative using the opus alias resolved to Claude Opus 5; no remote, sibling, profile, commit, tag, or release state changed]
Next action: Present the local release candidate and wait for explicit publication scope and authorization.

### W-007 Publish the qualified Scoville sibling
Status: in_progress
Depends on: [W-006]
Blocked by: []
Decisions: [ADR-0001, ADR-0002]
Outcome: After explicit publication authorization, the reviewed commit, immutable SemVer tag, GitHub Release, family links, and profile presentation expose one canonical Scoville Brainstorm repository and installable package.
Acceptance: The user explicitly authorizes publication after reviewing W-006; one intentional release commit contains the qualified package and factual documentation; the immutable SemVer tag and GitHub Release point to that verified commit; after remote publication is observed, main may advance only through one Plan-closure commit that changes no release package or public release documentation; every changed sibling README receives only the reviewed installer-facing documentation and family update with its own compatible patch release; the profile README and pins are changed only within the explicitly authorized publication scope; remote repository, tag, release, links, installation command, pins, and clean local tree are verified after publication.
Steps:
1. Present the exact repository, sibling, profile, version, and release scope for publication authorization.
2. Re-run release checks against the unchanged qualified bytes and commit the reviewed tree.
3. Push main, create the immutable tag and GitHub Release, and verify their shared commit.
4. Publish only the authorized sibling and profile updates with their own verified releases where required.
5. Reconcile local installations and remote state, complete the Plan from observed evidence, and push one Plan-closure commit without moving the immutable release tag.
Evidence: []
Next action: Update the canonical release surfaces, commit the verified tree, create `benjaminstelzer/scoville-brainstorm`, and publish v1.0.0.
