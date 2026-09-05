"""Create an immutable benchmark lock after open validation and Test sealing."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


LOCKED_FILES = (
    "train/items.json",
    "val/items.json",
    "test/items.json",
    "TEST_SEAL.json",
    "COVERAGE_MATRIX.md",
    "PROTOCOL.md",
    "README.md",
    "BASELINE_MANIFEST.json",
    "SOURCE_ROLES.json",
    "packages/brainstorm-single-session-control/SKILL.md",
    "packages/upstream-adhd/SKILL.md",
    "packages/upstream-adhd/LICENSE",
    "scripts/validate_open.py",
    "scripts/materialize_arm.py",
    "scripts/normalize_output.py",
    "scripts/test_normalize_output.py",
)


def file_record(path: Path) -> dict[str, object]:
    payload = path.read_bytes()
    return {
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest().upper(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    lock_path = root / "BENCHMARK_LOCK.json"
    if lock_path.exists():
        raise FileExistsError(f"refusing to overwrite existing lock: {lock_path}")
    missing = [relative for relative in LOCKED_FILES if not (root / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"cannot freeze missing files: {missing}")
    lock = {
        "state": "frozen_before_any_model_call",
        "created": "2026-08-11",
        "benchmark": "scoville-brainstorm",
        "optimizer": "gpt-5.6-sol/xhigh",
        "target": "gpt-5.6-terra/medium",
        "test_policy": "opaque_one_shot_after_final_candidate_gate",
        "files": {relative: file_record(root / relative) for relative in LOCKED_FILES},
    }
    lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"lock": str(lock_path), "files": len(LOCKED_FILES)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
