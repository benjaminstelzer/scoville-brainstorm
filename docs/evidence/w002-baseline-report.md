# W-002 baseline report

## Result

Neither baseline qualified on the frozen Train split. The host-normalized upstream ADHD arm improved the hard pass rate by 12.5 percentage points over the single-session control, but still failed 15 of 24 cases and used substantially more time and tokens. Validation and Test were therefore not executed.

| Arm | Train hard pass | Provider tokens | Loaded Skill tokens | Wall time |
| --- | ---: | ---: | ---: | ---: |
| Single-session control | 6/24 (25.0%) | 901,926 | 3,325 | 1,194.8 s |
| Host-normalized upstream ADHD | 9/24 (37.5%) | 4,823,494 | 57,603 | 2,686.8 s |

Relative to the control, the ADHD arm used 5.35 times the provider tokens (+434.8%), 17.32 times the loaded Skill tokens (+1,632.4%), and 2.25 times the wall time (+124.9%). The Studio `soft` value is a cost-weighted execution score and is not treated as a semantic-quality judgment.

## Scope and provenance

- Benchmark: `benchmarks/scoville-brainstorm-v2`, frozen lock SHA-256 `EFF995DD8637295A9530EF6F84B0D72A14767EF86EBEF6FBB227D1C1F185E9A1`.
- Executor: Terra 5.6 Medium; three Train repetitions per arm; eight cases per repetition.
- Upstream ADHD source: commit `3d9dc487bc2eba4449742e2db0d92be9ebdf95b6` under the MIT license.
- The ADHD execution copy removed only the unsupported frontmatter field `license: MIT`; its instruction body remained byte-identical, SHA-256 `33D766647CA884F88172E81960A9DBB926EB234B68787E4E3767087BE383C52F`.
- Raw aggregate: `docs/evidence/w002-baseline-metrics.json`, SHA-256 `6FAACF4520599D3AE6CF30F65529F61B773635D8C2F2AB95A825AC0E338F019C`.
- Blind-judgment packet: `docs/evidence/w002-baseline-blind-packet.json`, SHA-256 `567A9910CCC8225D5162A69B5A4A00ECE1ECCE4242CE224269F042320C51C7D8`.

## Isolation limit

The ADHD outputs self-reported 57 generator branches, while the runtime trace recorded 84 completed collaboration waits but no completed spawn calls and no receiver identities. The present trace therefore cannot prove that those branches were independently created or isolated. The control also self-reported 14 generators although its instructions prohibited spawning, so self-report is not accepted as provenance evidence.

## Exclusions and gates

Earlier v1 and v2 development runs exposed benchmark-contract and runtime defects and are retained as diagnostics, not merged into these formal rates. A later blind semantic-judge request timed out before returning a judgment; it was not retried and contributes no score. Because both formal arms failed Train, no Validation or opaque Test case was read or executed.

## Decision consequence

Upstream ADHD does not justify a runtime dependency or wrapper: its modest reliability gain does not offset the failed gate, the measured cost, the missing Scoville prior-art and authority contract, or the unverified isolation provenance. Scoville Brainstorm will therefore implement a host-portable Scoville-native Skill. It may adapt useful MIT-licensed ADHD concepts with attribution, but it will not require ADHD at runtime.
