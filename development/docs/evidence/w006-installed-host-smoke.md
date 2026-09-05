# W-006 installed-host smoke evidence

Date: 2026-08-11

The installable four-file package was copied to:

- `C:\Users\benja\.codex\skills\scoville-brainstorm`
- `C:\Users\benja\.claude\skills\scoville-brainstorm`

Both trees are byte-identical to the repository package. Each host contains
exactly one `SKILL.md` whose frontmatter name is `scoville-brainstorm`. The
installed Skill SHA-256 is
`144590B8D3804945D9181C08DBEB5F71286CF76896415FA2AECC687560EAD40B`.

Codex CLI `0.146.0-alpha.9.2` produced the complete 39/39 open semantic,
36/36 metadata-only activation, and 4/4 adjudicated sealed qualification
evidence against those exact Skill bytes before installation.

Claude Code `2.1.220` then ran two read-only installed-host checks:

1. Explicit Compact activation returned a 6,746-character Brainstorm artifact
   with mechanism exploration, a decision point, and an explicit no-
   implementation boundary. The `opus` alias resolved to `claude-opus-5`.
2. A canonical React controlled-input request returned a 312-character direct
   answer with `useState` and `onChange` and no Idea map, Landscape, Shortlist,
   or Deepened-directions shape.

The two successful checks cost USD 0.2198635 and USD 0.045327 according to the
Claude CLI result envelopes. Tools capable of shell, edit, write, web, or task
delegation were disabled. An earlier command-line attempt supplied no prompt
because of argument parsing and exited before a provider call; it is an
infrastructure invocation, not an evaluation run.
