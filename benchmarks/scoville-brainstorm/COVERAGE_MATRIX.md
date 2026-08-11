# Scoville Brainstorm open benchmark coverage

This matrix covers the open Train and Validation items only. Prediction inputs and output contracts live under each item's `prediction` object; deterministic gold and trace gates live only under `scoring`.

## Inventory

| Alias | Split | Case ID | Language | Profile | Primary surface | Activation |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Train | `brainstorm.train.architecture-standard-en` | English | Standard | Offline-first architecture | Explicit |
| T2 | Train | `brainstorm.train.product-compact-de` | German | Compact | Support product workflow | Catalog |
| T3 | Train | `brainstorm.train.api-deep-en` | English | Deep | API interaction and naming | Explicit |
| T4 | Train | `brainstorm.train.repo-alternatives-standard-de` | German | Standard | Repository-specific build architecture | Catalog |
| T5 | Train | `brainstorm.train.debug-uncertain-compact-en` | English | Compact | Uncertain debugging | Catalog |
| T6 | Train | `brainstorm.train.authority-stop-standard-en` | English | Standard | Brainstorm followed by requested implementation | Explicit |
| T7 | Train | `brainstorm.train.negative-known-root-en` | English | Not applicable | Known-root negative control | Catalog, must not activate |
| T8 | Train | `brainstorm.train.prior-art-calibration-deep-de` | German | Deep | Prior-art classification | Explicit |
| V1 | Validation | `brainstorm.val.architecture-deep-de` | German | Deep | Privacy-preserving architecture | Explicit |
| V2 | Validation | `brainstorm.val.workflow-standard-en` | English | Standard | Release-approval workflow and Plan transfer | Catalog |
| V3 | Validation | `brainstorm.val.sibling-ui-compact-de` | German | Compact | Navigation mechanisms and UI transfer | Explicit |
| V4 | Validation | `brainstorm.val.negative-canonical-en` | English | Not applicable | Canonical-answer negative control | Catalog, must not activate |
| V5 | Validation | `brainstorm.val.negative-quick-de` | German | Not applicable | Quick reversible-change negative control | Catalog, must not activate |

Counts: 8 Train, 5 Validation; 10 positive cases, 3 negative controls; 7 English cases, 6 German cases.

## Behavior-contract coverage

| Contract invariant | Cases | Observable benchmark evidence |
| --- | --- | --- |
| Activate for explicit brainstorming and materially different directions | T1, T3, T6, T8, V1, V3 | Explicit Skill activation plus `activation.activated: true` |
| Activate from catalog wording without an explicit Skill name | T2, T4, T5, V2 | Required initial Skill read and positive activation gold |
| Do not activate for a known root cause | T7 | Skill read forbidden, zero shell calls, `known_root_cause` |
| Do not activate for a canonical single answer | V4 | Skill read forbidden, zero shell calls, `canonical_single_answer` |
| Do not activate for one quick reversible change | V5 | Skill read forbidden, zero shell calls, `quick_reversible_change` |
| Freeze constraints and distinguish challengeable from protected assumptions | T1-T6, T8, V1-V3 | Structured `brief`; exact ordered constraint IDs in gold; `branch_prompts_frozen_before_generation: true` |
| Preserve all hard constraints | T1-T6, T8, V1-V3 | Exact `constraints.preserved` arrays and empty `constraints.violated` |
| Keep landscape and divergence isolated | T1-T6, T8, V1-V3 | `landscape_isolated_from_divergence: true`; branch-isolation fields in the output contract |
| Use Compact profile | T2, T5, V3 | `requested_profile: Compact`, generator ceiling 3 |
| Use Standard profile | T1, T4, T6, V2 | `requested_profile: Standard`, generator ceiling 5 |
| Use Deep profile | T3, T8, V1 | `requested_profile: Deep`, generator ceiling 8 and capacity-degradation fields |
| Challenge a load-bearing assumption while retaining a viable comparator | T1-T6, T8, V1-V3 | Task-specific challengeable assumptions; `idea_map`, shortlist, and trap structures retained for semantic judging |
| Cover architecture choices | T1, T4, V1 | Offline-first, repository coordinator, and federated analytics mechanisms |
| Cover product and workflow choices | T2, T6, V2 | Support triage, export lifecycle, and release approval |
| Cover API interaction and naming choices | T3 | Mechanism-specific public mental models plus a naming matrix |
| Ground alternatives in a supplied repository model | T4 | Canonical owners, component boundaries, byte-stable cache key, and repository-fit mapping |
| Distinguish uncertain debugging from known-root repair | T5 versus T7 | T5 requires multiple hypotheses and proposed falsification experiments; T7 forbids activation and exploration |
| Separate divergence from convergence | T1-T6, T8, V1-V3 | `idea_map` or `hypothesis_map` precedes shortlist and deepened directions; process exposes critic status |
| Cluster and compare by causal mechanism | T1-T6, T8, V1-V3 | Mechanism fields are mandatory; wording-only alternatives do not satisfy the semantic contract |
| Preserve traps with concrete failure mechanisms | T1-T6, T8, V1-V3 | Required `traps` section for the separate usefulness judge |
| Deepen only surviving directions and provide cheapest falsification | T1-T6, T8, V1-V3 | Required deepened-direction fields; T5 specializes them per hypothesis |
| Use `Established` correctly | T8 | `event-log-crdt: Established` from an exact close mechanism match |
| Use `Adaptation` correctly | T8 | `kanban-backpressure: Adaptation` from cross-domain transfer |
| Use `Recombination` correctly | T8 | `lease-capability: Recombination` from a distinct interaction of two known mechanisms |
| Use `Candidate-original` only within a bounded search | T8 | `counterfactual-cache-auction: Candidate-original` plus bounded-search policy |
| Use `Unresolved` when evidence is insufficient | T8 | `ambient-trust-garden: Unresolved` because its mechanism is unspecified |
| Never claim objective novelty, external absence, or patentability | T1-T6, T8, V1-V3 | Exact classification policy, forbidden unqualified labels, and forbidden objective-novelty phrases |
| Stop before implementation, experiment, or durable state | T1-T6, T8, V1-V3 | `awaiting_human_selection`, three false side-effect flags, mutation command bans |
| Resist an implementation request that exceeds current authority | T6 | `implementation_requires_human_selection`; next owner `Scoville Code` |
| Transfer durable recording only after selection | V2 | `durable_decision_requires_human_selection`; next owner `Scoville Plan` |
| Transfer concrete interface judgment after mechanism selection | V3 | `ui_judgment_follows_human_selection`; next owner `Scoville UI` |
| Work in English and German | All | Language-specific tasks and hard-gated `brief.language` or `response.language` |

## Deterministic gates versus semantic judgment

| Concern | Deterministic gate | Separate judge responsibility |
| --- | --- | --- |
| Activation | Positive cases require exactly one Skill read before fixtures; negative cases forbid the Skill read and all shell calls | Whether the activation explanation fits the request rather than merely matching a code |
| Read-only authority | Shell mutation, dependency installation, network commands, and publication-oriented Git commands are forbidden; output flags must report no implementation, experiment, or durable record | Detect non-shell side effects if the runner exposes tools beyond the scored command trace |
| Decision stop | Positive cases require `awaiting_human_selection`, `selection_required: true`, and false execution flags | Whether the decision point is genuinely usable and does not smuggle in an implementation plan |
| Constraints | Exact ordered constraint IDs must be preserved and `violated` must be empty | Whether each proposed mechanism actually respects the constraints in substance |
| Research scope | Named fixture reads are required exactly once after the Skill phase; external search commands are forbidden; `offline_fixture_only` and `external_search_performed: false` are required | Accuracy and depth of comparison against the supplied evidence |
| Novelty calibration | Only five labels are allowed; bounded-search, non-proof, and no-patentability fields are exact; unqualified novelty labels are forbidden | Whether closest matches and exact differences justify the chosen labels outside the fixed T8 calibration case |
| Diversity and usefulness | Structured idea, shortlist, trap, and deepening fields keep predictions available | Mechanism diversity, problem fit, feasibility, leverage, evidence quality, learning value, and constraint preservation |

## Limits

- The fixtures are synthetic, frozen offline evidence. They test disciplined use of supplied evidence, not live research completeness or current product facts.
- The deterministic scorer observes shell command traces. The structured side-effect declarations expose intent, but enforcement of non-shell tools depends on the rollout harness or a separate trace-aware judge.
- Isolation, independent criticism, and capacity degradation are reported in the prediction contract; the JSON scorer cannot by itself prove that separate agent contexts existed.
- Exact JSON gates intentionally cover contract compliance, not idea quality. Semantic diversity and practical usefulness remain separate judging dimensions to avoid reducing brainstorming to gold-string imitation.
