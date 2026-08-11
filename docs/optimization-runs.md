# Optimization and evaluation runs

The development ledger records every retained Scoville Brainstorm Studio
invocation, including incomplete diagnostic runs, plus the separate activation
and live-orchestration runs. A "run" is one evaluation, optimization, activation
repetition, or live integration invocation. A case execution is one target-model
benchmark row; optimizer analysis calls and live branch calls are reported
separately.

## Totals

| Measure | Count |
| --- | ---: |
| Optimization and evaluation runs | 182 |
| Benchmark case executions | 584 |
| Optimizer-only analysis, merge, and ranking calls | 6 |
| Live integration branch calls | 4 |
| Installed-host smoke invocations | 2 |
| Total retained model invocations represented by those categories | 596 |

The 182 runs comprise 173 Studio invocations, six description-only activation
repetitions, one live multi-agent integration, and two installed-host smoke
checks. The Studio invocations include the one conservative SkillOpt run and
the one-shot sealed Test.

## Studio history by evidence root

| Evidence root | Runs | Case executions |
| --- | ---: | ---: |
| `scoville-brainstorm-baselines` | 2 | 16 |
| `scoville-brainstorm-v2-baselines` | 9 | 58 |
| `scoville-brainstorm-v2-reliability` | 6 | 48 |
| `scoville-brainstorm-v2-candidate-development` | 71 | 120 |
| `scoville-brainstorm-v3-source-mirror-development` | 1 | 3 |
| `scoville-brainstorm-v4-injected-core-development` | 1 | 3 |
| `scoville-brainstorm-v5-host-activation-development` | 1 | 2 |
| `scoville-brainstorm-v6-single-core-source-development` | 1 | 8 |
| `scoville-brainstorm-v7-process-gold-development` | 3 | 4 |
| `scoville-brainstorm-v8-observable-process-development` | 1 | 1 |
| `scoville-brainstorm-v9-observable-agent-evidence-development` | 1 | 1 |
| `scoville-brainstorm-v10-unambiguous-process-development` | 5 | 5 |
| `scoville-brainstorm-v11-trace-owned-process-development` | 8 | 15 |
| `scoville-brainstorm-v12-semantic-trace-separation-development` | 32 | 95 |
| `scoville-brainstorm-v13-explicit-constraint-schema-development` | 31 | 133 |
| **Studio subtotal** | **173** | **512** |
| Description-only activation | 6 | 72 |
| **Benchmark subtotal** | **179** | **584** |
| Live multi-agent integration | 1 | not a benchmark row |
| Installed-host positive and negative smoke | 2 | not a benchmark row |
| **Development total** | **182** | **584** |

Counts come from terminal and partial Studio run markers plus retained result
artifacts. They are execution-history totals, not an attempt to make diagnostic
or superseded candidates look like qualification evidence. Final qualification
uses only the exact-byte gates documented in
[benchmark evidence](benchmark-evidence.md).
