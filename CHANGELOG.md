# Changelog

## 2026-08-19: Public validation wording (v1.1.2)

### Changed

- Removed external model-review approval from the public Status and release
  history.
- Kept the measured qualification results, evidence links, Skill package, and
  behavior unchanged.

### Validation

- README and Changelog no longer publish external approval as completion
  evidence.
- The unchanged Agent Skill package passes canonical validation.

## 2026-08-19: Release-package provenance (v1.1.1)

### Fixed

- Distinguished the evaluated Windows-worktree package hash from the canonical
  GitHub tag-package hash after Git normalized three CRLF line endings in the
  unchanged `agents/openai.yaml` metadata file.
- Added repository-wide LF normalization for future release checkouts.
- Kept `SKILL.md`, the Research-composition reference, behavior, and qualified
  results unchanged.

### Validation

- Both the evaluated worktree and downloaded tag package passed Agent Skill
  validation.
- `SKILL.md`, `THIRD_PARTY_NOTICES.md`, `LICENSES/ADHD-MIT.txt`, and
  `references/research-composition.md` were raw byte-identical.
- The downloaded five-file tag package has canonical SHA-256
  `a315fd4e93bb1453e9104e9bd367ad52ab8803bf4f67c23b2936235e1088a487`.
- No model-behavior test was repeated because no Skill instruction or metadata
  value changed.

## 2026-08-19: Scoville Brainstorm v1.1.0

### Added

- Added an explicit combined mode in which Scoville Research owns the sole
  inspected prior-art landscape lane.
- Added a conditionally loaded composition reference for untrusted retrieved
  content, private-query sanitization, actual-source inspection, source-origin
  collapse, and bounded originality language.
- Added the Research-lane substitution rule: Brainstorm does not dispatch its
  native landscape agent in combined mode, and generators see no landscape or
  sibling output before convergence.
- Added Brainstorm-native Decision, Plan, and qualification evidence for the
  sibling boundary without creating a standalone Research dependency.

### Validation

- Agent Skill package and native Scoville Plan validation passed.
- The exact candidate passed 6/6 open Validation cases including five released
  standalone retention gates.
- The fresh three-case holdout produced 1/3 raw and 3/3 adjudicated Skill
  results; two frozen benchmark-contract defects were retained without retry,
  Gold changes, or candidate changes.

## 2026-08-11: Concrete slop examples (v1.0.3)

### Changed

- Restored the concrete problem-first opening used by the earlier Scoville Code
  README and adapted it to this Skill's actual failure modes.
- Added four visible slop symptoms, their consequence, and dry humor without
  changing the Skill contract or its measured claims.
- Kept the shared README section order and family copy aligned across all six
  Scoville repositories.

### Validation

- Agent Skill package, README structure, shared-copy, internal-link, and
  Markdown whitespace checks passed.
- No model-behavior benchmark was run because the Skill instructions did not
  change.

## 2026-08-11: README voice and structure (v1.0.2)

### Changed

- Reworked the public README opening in Benjamin's voice while preserving the
  Skill's activation boundary, mechanism, evidence, sources, and measured
  status.
- Kept the shared Scoville section order and family copy aligned across all six
  project READMEs.
- Updated the Codex Skill-list description to use the same public voice.

### Validation

- Agent Skill package, README structure, shared-copy, internal-link, and
  Markdown whitespace checks passed.
- No model-behavior benchmark was run because the Skill instructions did not
  change.

## 2026-08-11: Standalone family contract (v1.0.1)

### Changed

- Clarified that every Scoville Skill works independently and that family
  discovery does not imply installation, activation, applicability, or a
  dependency.
- Added all five current siblings with scoped ownership and kept sibling
  opt-out local to that sibling.
- Reduced repeated Core wording while retaining the existing activation
  metadata, domain ownership, decision stop, and output contract.

### Validation

- The central family-contract test passed all six packages and rejected all
  five synthetic drift cases; Agent Skill package validation also passed.
- No new model-behavior benchmark was run for this patch release.

## 2026-08-11: Scoville Brainstorm v1.0.0

### Added

- Added the first installable `scoville-brainstorm` package for read-only,
  decision-shaped divergence before implementation or durable planning.
- Added isolated generator, bounded landscape, mechanism clustering,
  calibrated prior-art labeling, independent criticism, constraint checking,
  and decision-stop contracts.
- Added Compact, Standard, and Deep effort profiles with a truthful
  single-coordinator fallback when fresh agents are unavailable.
- Added copy-ready Compact, Standard, and Deep usage examples to the README.
- Reduced the README to install-decision content while retaining the Scoville
  name rationale, implementation overview, sources, and qualification evidence.
- Added the six-Skill optimization-history ledger under `docs/`.
- Added MIT attribution for ideas adapted from `UditAkhourii/adhd` without a
  runtime dependency.

### Validation

- Qualified the exact package with Terra 5.6 Medium on 39/39 repeated open
  semantic cases, 36/36 description-only activation cases, and 4/4 one-shot
  sealed holdout cases.
- Ran one conservative Microsoft SkillOpt step with Sol 5.6 xhigh analysis;
  the optimizer rejected its proposed step and retained the 1,712-token
  reliability control unchanged.
- Confirmed actual isolated generator, separate landscape, and independent
  critic orchestration in a live multi-agent integration check.
