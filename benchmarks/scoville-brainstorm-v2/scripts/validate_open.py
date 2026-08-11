"""Validate open Scoville Brainstorm benchmark files without parsing Test."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType


EXPECTED_ADHD = {
    "packages/upstream-adhd/SKILL.md": (
        11118,
        "06DEBE68A370206ACD93E0B2EE54D6395BC367FDFBC079F2348E3CE2966DAC0A",
    ),
    "packages/upstream-adhd/LICENSE": (
        1074,
        "3F08D24B5561FC516B262351CB8E0302D30E7D9139F01B4A637E4BF3B5AB0938",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_benchmark_module(studio_root: Path) -> ModuleType:
    source = studio_root / "skillopt_studio" / "benchmark.py"
    spec = importlib.util.spec_from_file_location("frozen_studio_benchmark", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import Studio benchmark module: {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_split(root: Path, name: str, expected_count: int, module: ModuleType) -> list[str]:
    path = root / name / "items.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list) or len(payload) != expected_count:
        raise ValueError(f"{name} requires exactly {expected_count} items")
    ids: list[str] = []
    for item in payload:
        module.validate_item(item, source=path)
        ids.append(str(item["id"]))
    if len(ids) != len(set(ids)):
        raise ValueError(f"duplicate ids within {name}")
    return ids


def verify_test_seal(root: Path) -> dict[str, object]:
    seal_path = root / "TEST_SEAL.json"
    test_path = root / "test" / "items.json"
    seal = json.loads(seal_path.read_text(encoding="utf-8"))
    record = seal.get("files", {}).get("test/items.json", {})
    expected_hash = str(record.get("sha256", "")).upper()
    expected_bytes = int(record.get("bytes", -1))
    expected_count = int(seal.get("item_count", -1))
    actual_hash = sha256(test_path)
    actual_bytes = test_path.stat().st_size
    if expected_hash != actual_hash or expected_bytes != actual_bytes or expected_count != 4:
        raise ValueError("opaque Test seal mismatch")
    return {"count": expected_count, "bytes": actual_bytes, "sha256": actual_hash}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--studio", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    module = load_benchmark_module(args.studio.resolve())

    train_ids = validate_split(root, "train", 8, module)
    val_ids = validate_split(root, "val", 5, module)
    if set(train_ids) & set(val_ids):
        raise ValueError("Train and Validation ids overlap")

    source_roles = json.loads((root / "SOURCE_ROLES.json").read_text(encoding="utf-8"))["items"]
    if set(source_roles) != set(train_ids + val_ids):
        raise ValueError("SOURCE_ROLES ids must exactly cover open items")
    for item_id, roles in source_roles.items():
        if set(roles) != {"brief_fixtures", "landscape_fixtures"}:
            raise ValueError(f"invalid source role keys: {item_id}")
        if set(roles["brief_fixtures"]) & set(roles["landscape_fixtures"]):
            raise ValueError(f"fixture cannot have two roles: {item_id}")

    manifest = json.loads((root / "BASELINE_MANIFEST.json").read_text(encoding="utf-8"))
    expected_commit = manifest["skillopt"]["commit"]
    for relative, (expected_bytes, expected_hash) in EXPECTED_ADHD.items():
        path = root / relative
        if path.stat().st_size != expected_bytes or sha256(path) != expected_hash:
            raise ValueError(f"upstream baseline mismatch: {relative}")

    result = {
        "valid": True,
        "train": len(train_ids),
        "val": len(val_ids),
        "test_seal": verify_test_seal(root),
        "skillopt_commit": expected_commit,
        "upstream_adhd_verified": True,
        "source_roles_verified": True,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
