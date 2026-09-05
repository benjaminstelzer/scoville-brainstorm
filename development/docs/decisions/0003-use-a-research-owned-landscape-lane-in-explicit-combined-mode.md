---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-08-19
accepted: 2026-08-19
scope: skill/research-composition
transition_batch: b130fa9bd375c28ee18755ad3a38d9db9592f1d7fc9d5e5e5fa0be2456cb147e
transition_batch_members: [ADR-0003]
---

# Use a Research-owned landscape lane in explicit combined mode

## Decision

In an explicitly combined Scoville Research and Scoville Brainstorm run, substitute one Research-owned landscape lane for Brainstorm's native landscape agent. Preserve frozen isolated generators, use the Research lane as the sole landscape input to convergence, and keep both Skills independent outside that explicit mode.

## Problem

Standalone Brainstorm owns bounded prior-art comparison because divergence needs a landscape before originality labels can be calibrated. Research owns the stronger source contract: private-query sanitization, untrusted-content handling, actual-source inspection, source independence, contradictions, and claim-to-evidence traceability. Running both native landscape mechanisms in a combined task duplicates retrieval, makes reconciliation ownership ambiguous, and can anchor generators if either result becomes visible too early.

## Drivers

- One mechanism needs one canonical owner in combined mode.
- Brainstorm generators must remain prompt-frozen and isolated from landscape evidence until convergence.
- Retrieved content must stay untrusted and private identifiers must not enter external queries without explicit direction.
- Brainstorm must remain fully useful without Research, and Research must never become an automatic dependency.
- Bounded search can calibrate an originality label but cannot establish global novelty.

## Considered alternatives

- Run both landscape agents and merge them. This preserves each standalone pipeline literally, but duplicates work and creates two competing evidence owners.
- Let Brainstorm consume Research output before generation. This may inspire ideas, but it breaks the isolation mechanism meant to reduce anchoring.
- Make Research mandatory for every Brainstorm run. This improves the evidence floor but broadens activation, cost, artifact, and host dependencies for ordinary ideation.
- Substitute the Research lane only in explicit combined mode. This preserves one evidence owner while leaving both standalone contracts intact.

## Consequences

- Brainstorm loads a composition reference only for an explicit combined request when Research is independently available and applicable.
- The coordinator freezes the factual frame, generator prompts, and Research lane prompt before dispatch.
- Brainstorm does not launch its native landscape agent in combined mode.
- The completed Research lane enters convergence only after generator collection and is the only landscape input.
- Research owns source retrieval and evidence limits; Brainstorm owns divergent mechanisms, convergence, calibrated originality labels, and the shortlist.
- Trace evidence, not coordinator prose, owns claims about isolation and visibility.
- Standalone Brainstorm keeps its native landscape agent and gains no Research dependency.

## Confirmation

Freeze standalone and combined topology cases before implementation. Qualification requires exact reference routing, no duplicate landscape call, no pre-convergence landscape visibility, one Research landscape handoff, preserved standalone behavior, prompt-injection and private-query safety, Agent Skill validation, and an exact candidate hash reviewed by Fable.

## Revisit when

Revisit if the hosts provide a native typed composition primitive, if Research and Brainstorm adopt a shared evidence protocol without activation coupling, or if observed combined runs cannot preserve generator isolation while handing one Research lane to convergence.
