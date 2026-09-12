# Scoville Brainstorm

Three versions of the same idea do not give you three useful choices. A queue,
an event queue and a queue with different arrows may still solve the problem
in exactly the same way.

Scoville Brainstorm explores alternatives by how they work. It compares them
against the fixed constraints and existing approaches, challenges their weak
assumptions and returns a shortlist you can make a decision from. It stops
before choosing or implementing a direction.

Use it for architecture, product, workflow or research questions that need
materially different approaches, including competing explanations for an unknown
cause. A known fix, ordinary review or wording question does not need this process.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
Here, that signal is the difference between approaches after constraints and criticism have been applied.

## How to use

Name Scoville Brainstorm and an effort profile in the request. Compact targets
up to three generator branches, Standard up to five, and Deep six to eight when
host capacity permits. Weak ideas are never added merely to reach a count.

**Compact** - a quick check before choosing between a few plausible directions:

```text
Use Scoville Brainstorm in Compact mode. Find materially different mechanisms for reducing checkout abandonment without changing the payment provider. Preserve the stated constraints, return a short decision-ready comparison, and do not choose or implement a direction.
```

**Standard** - broader exploration with prior-art separation:

```text
Use Scoville Brainstorm in Standard mode. Explore materially different architectures for offline-first collaboration. Separate established approaches from adaptations or candidate-original directions, identify attractive traps, and stop at a shortlist with the cheapest falsifier for each direction.
```

**Deep** - a material, uncertain choice worth a wider search:

```text
Use Scoville Brainstorm in Deep mode. Investigate fundamentally different mechanisms for recovering from intermittent data corruption with an unknown root cause. Include a load-bearing-assumption challenge, a practical comparator, bounded prior-art research, and falsifiable hypotheses. Do not diagnose, plan, or implement the winner.
```

**Combined with Research** - keep evidence depth without anchoring the idea
generators:

```text
Use Scoville Brainstorm together with Scoville Research. Freeze the factual frame and generator prompts first. Let Research own one inspected prior-art landscape lane, keep that lane invisible to Brainstorm generators until convergence, and return a mechanism-level shortlist without implementing it.
```

Explicit `$scoville-brainstorm` invocation also works on hosts that support
named Skill invocation.

## Compatibility

Any Agent Skills host that can read references/. Isolated generators, a landscape agent and an independent critic need subagent spawning; without it the Skill uses its documented solo fallback. Web search improves the landscape pass. No scripts, no network service. Developed for Codex and Claude Code; other hosts untested.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

```text
Install the complete Scoville Skill suite for all my projects. Fetch and install every exact package directory below:

https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
https://github.com/benjaminstelzer/scoville-research/tree/main/scoville-research
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/tree/main/scoville-design-anti-ai-slop
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
https://github.com/benjaminstelzer/scoville-plan/tree/main/scoville-plan
https://github.com/benjaminstelzer/scoville-handoff/tree/main/scoville-handoff

Preserve existing customizations and ask before overwriting conflicting files. Report every installed location and whether the host discovers each Skill.
```

## What it enforces

- **Decision-shaped activation.** Difficulty alone does not trigger an idea
  search. The request must need materially different mechanisms.
- **One factual frame.** Facts, authority, fixed constraints, assumptions,
  source scope, and effort profile are frozen before divergence.
- **Independent generation when available.** Generators do not see sibling or
  landscape output. A single-agent fallback is labeled by its real capacity.
- **One landscape owner in combined mode.** Research replaces the native
  Brainstorm landscape agent when both Skills are explicitly requested. It
  never becomes a standalone dependency.
- **Mechanisms over paraphrases.** Convergence merges surface variants and
  rejects unsupported or constraint-breaking directions.
- **Calibrated originality.** Evidence labels describe only the documented,
  bounded comparison and never claim objective novelty or patentability.
- **A hard decision stop.** The result gives benefits, risks, and cheapest
  falsifiers, then waits for human selection.

The complete contract is in [SKILL.md](scoville-brainstorm/SKILL.md).

## How it works

A request is routed as `NO`, `ASK`, or `YES`. A positive run freezes one brief,
uses isolated generators and a separate landscape pass when the host supports
them, clusters ideas by mechanism, applies independent criticism, and returns
at most three distinct directions (two in Compact). With no agent delegation,
one consolidated generation pass is followed by exactly one landscape pass,
without claiming isolation or independent criticism. Truncated sources have a
targeted recovery path before the frame is frozen. Observation labels remain
facts, not automatic constraints. A known material source change after freezing
requires visible reconciliation instead of silently mixing revisions.

In explicit combined mode, Research owns the only landscape lane. Brainstorm
freezes and runs its generators without that result, receives the inspected
landscape only after collection, and then converges by mechanism. Outside that
mode the native Brainstorm landscape remains unchanged. Research can require browsing, and parallel branches use additional context.
The Skill installs no executable software or dedicated network service.

## How it was developed

I developed Brainstorm around a recurring problem: asking for different ideas
often produces different descriptions of the same idea. The instructions keep
generation separate from criticism and compare alternatives by how they work.
That distinction matters more than the number of proposals.

I use it in real tasks and read the complete histories to see where alternatives
collapse into one another, constraints get lost or the search continues after
it has enough useful directions. I have also used SkillOpt to try instruction
changes. An [early optimization run](https://github.com/benjaminstelzer/scoville-brainstorm/blob/1ca176c9a6ec85188a2cd50feebd579f35991247/CHANGELOG.md)
did not produce a change worth keeping. The existing instructions stayed.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web,
  GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns
  visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  framework-aligned implementation, interface mechanics, accessibility, and
  rendered evidence, with a standalone design fallback.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Current Codex lifecycle limitation

On 2026-09-09, the tested Codex Desktop tool surface exposed no control whose
documented semantics close a completed subagent thread and free its slot. Other
Codex hosts may expose an equivalent control under a different name. Brainstorm
therefore discovers lifecycle controls by documented behavior, reports unavailable
cleanup before isolated generation, and keeps generators, landscape work, and any
critic within observable capacity. Interrupting, archiving, deleting a task, or
killing a process is not assumed to free a subagent slot.

## Sources

- [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd/tree/3d9dc487bc2eba4449742e2db0d92be9ebdf95b6)
  for isolated ideation, delayed criticism, and convergence after divergence.
- [SkillReducer](https://arxiv.org/abs/2603.29919v2) for semantic-unit analysis
  and progressive disclosure.
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601v2) and
  [Brainstorm then Select](https://openreview.net/forum?id=8HwKaJ1wvl) for
  separating candidate generation from evaluation and selection.
- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package contract.

## License

MIT. See [LICENSE](LICENSE).
