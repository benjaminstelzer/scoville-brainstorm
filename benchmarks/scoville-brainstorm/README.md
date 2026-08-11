# Scoville Brainstorm benchmark

This benchmark compares an ordinary single-session control, the unchanged upstream ADHD Skill, and a future frozen Scoville Brainstorm candidate. It is authored before candidate generation and keeps exact execution gates separate from blind usefulness judgment.

- `PROTOCOL.md` defines models, splits, metrics, promotion gates, ablations, cost accounting, and adjudication.
- `BASELINE_MANIFEST.json` pins upstream source and tool revisions.
- `train/items.json` and `val/items.json` are open development cases.
- `test/items.json` is an opaque one-shot holdout. Development agents may verify only its seal, byte count, case count, and hash.
- `COVERAGE_MATRIX.md` maps behavior-contract requirements to open cases.
- `SOURCE_ROLES.json` distinguishes factual-brief fixtures from landscape evidence for machine-checkable branch isolation.
- `packages/brainstorm-single-session-control` is a benchmark-only one-context comparison arm.
- `packages/upstream-adhd` contains the byte-exact pinned upstream Skill and license after provenance verification.
- `scripts/materialize_arm.py` adapts only the observable active-Skill path and creates a separately locked execution copy.
- `scripts/normalize_output.py` removes arm-identifying templates and maps raw answers to one common judging record while preserving a raw-artifact hash.

No Test result may select or repair a candidate. Raw benchmark, infrastructure, and adjudicated Skill outcomes remain separately reproducible.
