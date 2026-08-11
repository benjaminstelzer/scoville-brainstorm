# Changelog

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
