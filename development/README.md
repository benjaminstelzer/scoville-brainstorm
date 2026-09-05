# Development

The only installable Skill source is [`scoville-brainstorm/`](../scoville-brainstorm/).
This directory owns repository development and is not an installation package.

## Current layout

Paths recorded before the 2026-09-05 structure change are historical. Use this mapping
for current local files; frozen evidence retains its original contents and hashes.

| Former repository path | Current repository path |
| --- | --- |
| `docs` | `development/docs` |
| `tests` | `development/tests` |
| `scripts` | `development/scripts` |
| `benchmarks` | `development/benchmarks` |
| `PROJECT_INDEX.md` | `development/PROJECT_INDEX.md` |

Run development commands from this directory unless the command specifies otherwise.
The installable package is one directory above. Tests, when present, run with
`python -B -m unittest discover -s tests` in the existing development environment.
This move does not add dependencies or establish new model or host qualification.

The native planning root is this directory: [`PROJECT_INDEX.md`](PROJECT_INDEX.md),
`docs/plans/` and `docs/decisions/` moved together.

## Frozen control texts

These files are evaluation inputs, not additional installable Skills. Their bytes
are unchanged. A new evaluation must copy the chosen control into its isolated
run directory as `SKILL.md`; never restore that name in this repository.

| Former path after directory move | Stored fixture path |
| --- | --- |
| `development/benchmarks/scoville-brainstorm/packages/brainstorm-single-session-control/SKILL.md` | `development/benchmarks/scoville-brainstorm/packages/brainstorm-single-session-control/SKILL.fixture.md` |
| `development/benchmarks/scoville-brainstorm/packages/upstream-adhd/SKILL.md` | `development/benchmarks/scoville-brainstorm/packages/upstream-adhd/SKILL.fixture.md` |
| `development/benchmarks/scoville-brainstorm-v2/packages/brainstorm-single-session-control/SKILL.md` | `development/benchmarks/scoville-brainstorm-v2/packages/brainstorm-single-session-control/SKILL.fixture.md` |
| `development/benchmarks/scoville-brainstorm-v2/packages/upstream-adhd/SKILL.md` | `development/benchmarks/scoville-brainstorm-v2/packages/upstream-adhd/SKILL.fixture.md` |
