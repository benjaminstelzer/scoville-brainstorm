# W-003 candidate report

## Result

The first host-portable `scoville-brainstorm` package is implemented and structurally valid. It has no ADHD runtime dependency. The package contains one Core, two routed references, OpenAI interface metadata, the upstream notice, and a byte-exact copy of the upstream MIT license.

Skill Creator validation and the Scoville Plan profile validator pass. Fable's final read-only regression review returned `READY` after checking activation, host-conditional batching, truthful isolation degradation, exact labeled-ID carryover, process-versus-task violations, coordinator-owned JSON serialization, sibling ownership, and attribution.

## Current package

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `SKILL.md` | 5,491 | `86D3B8EE20D04913224A74AC9AB046837CD1CF5DC8E3835BD33B5CB584B05C11` |
| `references/orchestration.md` | 4,380 | `E80D6F7815CC0E16F224EB04702F4A3313B16DDBB768DF580F899809A0FFFF0D` |
| `references/evidence-and-output.md` | 3,193 | `C4D349F728697B01CAD2227155FDF65A7FFBC560CE288805C79C35D13F5C186C` |
| `agents/openai.yaml` | 285 | `074DE076969037FEC130689FA84B1CF7736A177F0ECFF0E7247D086C3F3FFE40` |
| `THIRD_PARTY_NOTICES.md` | 700 | `21E292299CF6DA733C4C5F8B4FD542CA5FDF90602D80A43EE6A57BD165CFD737` |
| `LICENSES/ADHD-MIT.txt` | 1,074 | `3F08D24B5561FC516B262351CB8E0302D30E7D9139F01B4A637E4BF3B5AB0938` |

## Open development evidence

The first full Train development run passed 5/8 hard cases. Its three failures exposed distinct causes rather than one aggregate score:

- Debug replaced supplied IDs with descriptions.
- Product emitted one malformed JSON delimiter while preserving the requested semantics in the raw response.
- Repository omitted required references, reread the Core, and ran a dummy command.

The smallest causal rules were added. Targeted fresh Terra 5.6 Medium reruns then passed the affected cases:

| Case | Passing run | Hard | Shell calls | Result SHA-256 |
| --- | --- | ---: | ---: | --- |
| Product Compact | `brainstorm-candidate-v1-fix-product-r1` | 1/1 | 2 | `7ABF71A029358E0892432E9AB48F5EF97BC655D32C7FA4C591282395145912AD` |
| Repository Standard | `brainstorm-candidate-v1-fix-repo-r2` | 1/1 | 2 | `B3CE9C61DDD59B3FED4D0E1031E8389DAF7D1326CFD240A45082F7C6990A21FC` |
| Debug Compact | `brainstorm-candidate-v1-fix-debug-r4` | 1/1 | 2 | `91990ABB492B95A569BF706597E2791A5D575693FF87843830F264DDAF9D4609` |

A Validation Deep smoke also passed 1/1 hard under `brainstorm-candidate-v1-smoke-valid-seen-r3`, result SHA-256 `2DF3B6AC07C7D6BA1608EDFC8FD7677265B1C0B2AC3CF3EC6D807D4317E8422D`.

Every Train case has therefore demonstrated at least one hard pass during open development. This is W-003 direction evidence, not qualification: the current exact package hash has not yet completed repeated full Train and Validation runs. W-004 owns that reliability gate and later token reduction. The opaque Test split remains unexecuted.
