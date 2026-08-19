# Scoville Brainstorm

More ideas are easy. More genuinely different mechanisms are not.

It usually looks harmless:

- You ask for three different architectures and receive a queue, a queue with
  events, and a queue whose arrows point the other way.
- One direction ignores the fixed offline constraint but survives because it
  is, admittedly, the exciting one.
- A familiar pattern is presented as original after the prior-art search stops
  precisely where recognition begins.
- The eighth idea exists because eight ideas were requested. Its main mechanism
  is being number eight.

That is brainstorming slop: surface variety without causal variety. Plenty of
ideas, very little new decision space.

Scoville Brainstorm is a read-only Agent Skill for material architecture,
product, workflow, research, and unknown-root choices. It explores causally
different mechanisms, tests them against fixed constraints and bounded prior
art, and returns a decision-ready shortlist. Then it stops. Selection,
implementation, durable planning, and publication belong to the work that
comes after brainstorming, however eager the brainstorm may be to get promoted.

Do not use it for one canonical answer, a known-root fix, ordinary review or
wording, or one small reversible change.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
Brainstorming produces words easily. Its useful heat is the smaller set of
distinct mechanisms that survives constraints, prior-art comparison, and
criticism.

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

## Install

Use an Agent Skills-compatible host and Terra 5.6 Medium or a comparably
capable executor such as Opus 4.8. Ask the agent to install:

```text
Install this Agent Skill and refresh the available Skill list:
https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
Keep the installed directory name scoville-brainstorm. Use Terra 5.6 Medium or a comparably capable executor such as Opus 4.8.
```

The final path must end in
`<skills-dir>/scoville-brainstorm/SKILL.md`. For Claude Code, use
`~/.claude/skills/` globally or `.claude/skills/` inside one project. Other
hosts use their supported Skills directory.

**What it costs.** Brainstorm loads a 1,977-token Core, then generator,
landscape, and critic passes can use materially more tokens than working
without the Skill. That cost buys broader mechanism coverage and a constrained,
decision-ready shortlist. Use it for material or uncertain choices. Skip it for
known answers and small vibe-coding tasks. See
[benchmark evidence](docs/benchmark-evidence.md).

## What it enforces

- **Decision-shaped activation.** Difficulty alone does not trigger an idea
  search. The request must need materially different mechanisms.
- **One factual frame.** Facts, authority, fixed constraints, assumptions,
  source scope, and effort profile are frozen before divergence.
- **Independent generation when available.** Generators do not see sibling or
  landscape output. A single-agent fallback is labeled by its real capacity.
- **One landscape owner in combined mode.** Research replaces the native
  Brainstorm landscape agent when both Skills are explicitly requested; it
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
one consolidated pass follows the same constraints without claiming isolation.

In explicit combined mode, Research owns the only landscape lane. Brainstorm
freezes and runs its generators without that result, receives the inspected
landscape only after collection, and then converges by mechanism. Outside that
mode the native Brainstorm landscape remains unchanged. The Skill installs no
executable software and requires no network service.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web,
  GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  interface hierarchy, framework fit, accessibility, and rendered evidence.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

The v1.1.0 candidate passed **6/6 open Validation cases**: one new combined
Research topology and five released standalone retention gates. Its fresh
three-case holdout produced **1/3 raw** and **3/3 adjudicated Skill** results.
The two raw failures were frozen benchmark-contract defects - one contradicted
its own Boolean output type, the other required an undisclosed mode string and
exact idea count. Neither justified changing the candidate, retrying the run,
or rewriting Gold.

The earlier qualification history remains intact: 182 optimization and
evaluation runs, 584 benchmark case executions, 43/43 semantic cases, 36/36
activation cases, and 4/4 v1.0 holdout cases. See the
[v1.1 qualification manifest](docs/evidence/w003-research-composition-qualification.json),
[benchmark evidence](docs/benchmark-evidence.md), and
[family run ledger](docs/optimization-history.md).

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

Research scope and pinned sources are listed in
[the source map](docs/research/source-map.md).

## License

MIT - see [LICENSE](LICENSE).
