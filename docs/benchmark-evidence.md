# Benchmark evidence

Scoville Brainstorm was developed reliability-first. The frozen open benchmark
contains eight Train and five Validation cases; the independently authored
holdout contains four cases. Terra 5.6 Medium executed the Skill. Sol 5.6 xhigh
performed diagnosis and the final conservative SkillOpt analysis.

## v1.1.0 composition qualification

The v1.1.0 package adds one conditionally loaded Research-composition reference
without changing standalone landscape behavior. The evaluated Windows-worktree
package SHA-256 is
`FC204947ED837424B24EB2067491D2DED3126381D952EBDEAED55D3765B06D2A`.
The canonical five-file GitHub tag package SHA-256 is
`A315FD4E93BB1453E9104E9BD367AD52AB8803BF4F67C23B2936235E1088A487`.
The sole raw difference is CRLF versus LF in the unchanged
`agents/openai.yaml`; `SKILL.md` and the composition reference are raw
byte-identical. v1.1.1 records that boundary and adds LF normalization without
changing Skill behavior.

The candidate passed 6/6 open Validation cases: the new explicit-combined
topology plus five historical standalone, activation, constraint, and stop
gates. The combined case observed exactly two package reads, suppressed the
native Brainstorm landscape agent, kept Research content untrusted, preserved
private-query and visibility boundaries, and retained both standalone modes.

The fresh three-case Test ran once with no retry, remint, Gold change, or
post-Test candidate edit. Raw score was 1/3. The combined topology passed every
invariant. Two other rows contained frozen contract defects:

- the neutral executor required an activation object while the row contract
  and Gold required a Boolean;
- the standalone row required an undisclosed `mode` string and exactly two
  mechanisms even though neither its task nor the Skill fixed that count.

All governed Skill behavior passed those rows, producing an adjudicated 3/3
Skill score. Fable 5 High independently confirmed both defects and returned
`READY` on the joint Research and Brainstorm implementation review. The exact
hashes and results are preserved in the
[v1.1 qualification manifest](evidence/w003-research-composition-qualification.json).

## Final qualification

| Gate | Repetitions | Result | What it checks |
| --- | ---: | ---: | --- |
| Open Train | 3 x 8 | 24/24 | positive and negative routing, source discipline, constraints, authority, prior art, useful shortlist |
| Open Validation | 3 x 5 | 15/15 | new domains, both languages, all effort profiles, sibling boundary, direct-answer negatives |
| Description-only activation | 3 x 12 | 36/36 | discovery metadata only; four positive and eight negative activation decisions; zero tools |
| One-shot sealed holdout | 1 x 4 | 4/4 Skill score | unseen architecture, uncertain-root debugging, direct-answer negative, and prior-art trap |

The exact final `SKILL.md` is 8,060 bytes, 1,712 loaded Skill tokens, and has
SHA-256
`144590B8D3804945D9181C08DBEB5F71286CF76896415FA2AECC687560EAD40B`.
It passed 43/43 semantic qualification cases plus 36/36 metadata-only
activation cases.

The repeated open semantic gate used 66,768 loaded Skill tokens and 1,466,321
provider tokens across 39 cases. The sealed holdout used 6,848 loaded Skill
tokens and 180,291 provider tokens across four cases. The activation gate used
only discovery metadata and 387,821 provider tokens across 36 cases. Provider
usage includes the host and conversation context and is not the same measure as
literal loaded Skill instructions.

## Holdout integrity and scoring

The final package, Microsoft SkillOpt commit, Studio harness, model roles,
configuration, scorer, and opaque Test seal were hash-bound before execution.
A fresh Terra 5.6 Medium agent consumed the gate once. There was no retry,
prediction reuse, remint, or post-Test Skill edit.

The raw holdout score is preserved as 2/4. Two rows exposed contradictions in
the frozen benchmark contract and are separately adjudicated as Skill passes:

- one task required exactly one fixture read while its scorer allowed zero
  shell calls;
- one output contract allowed any string for a bounded-evidence limitation
  while hidden Gold required one exact phrase, rejecting a more specific
  meaning-preserving answer.

The other behavior, source, authority, constraint, and efficiency gates passed.
The adjudicated Skill score is therefore 4/4, with zero Skill failures. The raw
files and Gold were not changed. The outer observer timed out after 60 seconds,
but the original process remained alive and wrote all four results plus its
terminal summary; this changed neither execution nor scoring.

Key Test evidence:

- one-shot gate SHA-256:
  `74CA91225D69E66B781F8399AF4DEE21ABE163540E536E8C269D7375A3BB8149`;
- raw summary SHA-256:
  `A79DB0CC2524ACF004362E8473C7A7B36D592EBF61663E6FDE7DECE5437458B5`;
- adjudication SHA-256:
  `673C212C6D47E4C927D365DCA9BADC5F7BD82B2A30F8C340B1C8A83DB61304C6`.

## Optimization decision

The final reliability control already used one Core and no conditional
references. Microsoft SkillOpt at commit
`ba820b500f9da96685cf2780c7dc85ed4eb6563e` ran one conservative optimization
step. Its eight-case Train rollout passed 8/8; SkillOpt rejected the proposed
step and retained the initial Skill byte-for-byte. Loaded instructions therefore
changed by 0% against the immediately preceding reliability candidate. Because
this is the first release, no release-to-release token percentage is
claimed.

## Installed-host checks

The qualified four-file package was copied byte-for-byte to the Codex and
Claude global Skill directories. Each host contains exactly one
`scoville-brainstorm` identity, and each installed `SKILL.md` retains the
qualified SHA-256. The Codex execution evidence above used the same exact Skill
bytes. Claude Code 2.1.220 completed an explicit Compact positive check with a
decision point and no implementation, then answered a canonical React negative
directly without Brainstorm sections. The configured `opus` alias resolved to
Claude Opus 5 for these checks, which is above the documented comparable-model
floor.

## Limits

- Qualification establishes behavior on the frozen cases and models, not
  deterministic behavior on every future prompt or host.
- The description-only gate isolates metadata discriminability; it does not
  replace the semantic and live orchestration checks.
- Prior-art labels remain bounded by the searched or supplied sources. They do
  not establish objective originality, novelty, or patentability.
- Multi-agent cost and quality depend on host capacity. The single-coordinator
  fallback is intentionally reported as degraded rather than independent.
- Human selection remains outside the Skill. The benchmark evaluates the
  shortlist and decision boundary, not whether one direction is universally
  best.
