"""Create a hash-bound arm copy with only observable Skill paths adapted."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


PATH_KEYS = ("required_file_reads", "forbidden_file_reads", "exact_once_file_reads")


def digest(path: Path) -> dict[str, object]:
    payload = path.read_bytes()
    return {"bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest().upper()}


def replace_path(value: str, skill_name: str) -> str:
    prefix = ".agents/skills/scoville-brainstorm/"
    if value.startswith(prefix):
        return f".agents/skills/{skill_name}/" + value[len(prefix) :]
    return value


def transform_items(path: Path, skill_name: str) -> None:
    items = json.loads(path.read_text(encoding="utf-8"))
    for item in items:
        scoring = item["scoring"]
        for key in PATH_KEYS:
            scoring[key] = [replace_path(str(value), skill_name) for value in scoring.get(key, [])]
        scoring["required_read_phases"] = [
            [replace_path(str(value), skill_name) for value in phase]
            for phase in scoring.get("required_read_phases", [])
        ]
    path.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def verify_canonical(root: Path) -> dict[str, object]:
    lock_path = root / "BENCHMARK_LOCK.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    for relative, expected in lock["files"].items():
        actual = digest(root / relative)
        if actual != expected:
            raise ValueError(f"canonical lock mismatch: {relative}")
    return lock


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--arm", required=True)
    parser.add_argument("--skill-name", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    canonical_lock = verify_canonical(root)
    if output.exists():
        raise FileExistsError(f"refusing to overwrite arm copy: {output}")
    shutil.copytree(root, output)
    for split in ("train", "val", "test"):
        transform_items(output / split / "items.json", args.skill_name)
    (output / "BENCHMARK_LOCK.json").unlink()
    binding = {
        "schema_version": 1,
        "arm": args.arm,
        "skill_name": args.skill_name,
        "canonical_lock_sha256": digest(root / "BENCHMARK_LOCK.json")["sha256"],
        "allowed_transformation": "observable_skill_path_only",
    }
    binding_path = output / "ARM_BINDING.json"
    binding_path.write_text(json.dumps(binding, indent=2) + "\n", encoding="utf-8", newline="\n")
    files = dict(canonical_lock["files"])
    for split in ("train", "val", "test"):
        files[f"{split}/items.json"] = digest(output / split / "items.json")
    files["ARM_BINDING.json"] = digest(binding_path)
    arm_lock = dict(canonical_lock)
    arm_lock["derived_arm"] = args.arm
    arm_lock["skill_name"] = args.skill_name
    arm_lock["files"] = files
    lock_path = output / "BENCHMARK_LOCK.json"
    lock_path.write_text(json.dumps(arm_lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"output": str(output), "arm": args.arm, "files": len(files)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

