---
format_version: 1
id: ADR-0002
status: accepted
created: 2026-08-11
accepted: 2026-08-11
scope: project/orchestration
---

# Select the runtime basis after baseline evidence

## Decision

Use a host-portable Scoville-native Skill adapted from useful MIT-licensed ADHD concepts, with attribution. Do not depend on, wrap, or fork upstream ADHD at runtime.

## Problem

Upstream ADHD already implements isolated parallel ideation and separate criticism, but Scoville Brainstorm additionally requires bounded prior-art research, calibrated originality language, Scoville ownership boundaries, host-capacity adaptation, and qualification across Codex and Claude. Reimplementing proven orchestration unnecessarily would add maintenance; depending on a host-specific runtime unnecessarily would reduce portability and control.

## Drivers

- Reuse working open-source mechanisms instead of rebuilding them without evidence.
- Avoid a mandatory runtime or provider dependency when portable Skill instructions suffice.
- Preserve frozen branch prompts, isolation, bounded research, and independent criticism across hosts.
- Attribute adapted MIT-licensed material accurately.
- Choose from measured behavior, usefulness, portability, and cost rather than architectural preference.

## Considered alternatives

- Depend on upstream ADHD directly: minimizes new orchestration work but may not provide the required novelty reconciliation, Scoville composition, or cross-host contract.
- Fork ADHD as the complete runtime: permits modification but creates a larger maintenance and release surface.
- Implement a host-native Skill without an upstream baseline: maximizes control but may duplicate working mechanisms without proof.
- Benchmark upstream first and select the smallest qualifying basis: delays implementation slightly but makes dependency and portability costs observable.

## Consequences

The installable package remains host-portable and owns its activation, isolation, research, originality, authority, and output contracts. Adapted ADHD concepts retain attribution, but the package adds no ADHD runtime dependency or maintenance surface.

## Confirmation

Across three frozen Train repetitions per arm, the single-session control passed 6/24 hard cases (25.0%) and the host-normalized upstream ADHD arm passed 9/24 (37.5%). ADHD used 4,823,494 provider tokens versus 901,926 (5.35x), 57,603 loaded Skill tokens versus 3,325 (17.32x), and 2,686.8 seconds versus 1,194.8 (2.25x). Neither arm reached Validation. The trace recorded no completed generator spawn calls, so the ADHD arm's 57 self-reported generators do not establish auditable branch isolation. See `docs/evidence/w002-baseline-report.md` and the frozen raw aggregate it identifies.

## Revisit when

Upstream ADHD changes its license, runtime, host support, orchestration contract, or measured performance, or a supported host gains a portable native primitive that replaces custom branch orchestration.
