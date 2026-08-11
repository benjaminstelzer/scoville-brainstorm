"""Aggregate formal W-002 baselines and build an arm-blind semantic packet."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from statistics import mean
from types import ModuleType
from typing import Any


PROJECT = Path(r"Z:\Projekts\AI\scoville-brainstorm")
STUDIO = Path(r"C:\Users\benja\Desktop\kompressidee\skillopt-studio")
BENCHMARK = PROJECT / "benchmarks" / "scoville-brainstorm-v2"
RUNS = STUDIO / "runs" / "scoville-brainstorm-v2-baselines"
OUT = PROJECT / "docs" / "evidence"

RUN_IDS = {
    "single_session_control": [f"brainstorm-v2-rev2-control-train-r{rep}" for rep in range(1, 4)],
    "upstream_adhd_host_normalized": [f"brainstorm-v2-rev2-adhd-train-r{rep}" for rep in range(1, 4)],
}

ARM_WALL_SECONDS = {
    "single_session_control": [394.5, 386.1, 414.2],
    "upstream_adhd_host_normalized": [751.3, 988.2, 947.3],
}

BLIND_SAMPLE = (
    (1, "brainstorm.train.architecture-standard-en"),
    (1, "brainstorm.train.product-compact-de"),
    (2, "brainstorm.train.debug-uncertain-compact-en"),
    (2, "brainstorm.train.prior-art-calibration-deep-de"),
    (3, "brainstorm.train.authority-stop-standard-en"),
    (3, "brainstorm.train.negative-known-root-en"),
)


def load_normalizer() -> ModuleType:
    path = BENCHMARK / "scripts" / "normalize_output.py"
    spec = importlib.util.spec_from_file_location("brainstorm_normalizer", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import normalizer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_result(run_id: str, item_id: str) -> dict[str, Any]:
    path = RUNS / run_id / "predictions" / item_id / "result.json"
    return json.loads(path.read_text(encoding="utf-8"))


def trace_counts(run_id: str, item_id: str) -> dict[str, int]:
    path = RUNS / run_id / "predictions" / item_id / "stdout.jsonl"
    counts = {"collab_calls": 0, "spawn_calls": 0, "wait_calls": 0, "trace_errors": 0}
    for line in path.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        item = event.get("item") if isinstance(event.get("item"), dict) else {}
        if item.get("type") == "error":
            counts["trace_errors"] += 1
        if item.get("type") == "collab_tool_call" and event.get("type") == "item.completed":
            counts["collab_calls"] += 1
            if item.get("tool") == "spawn_agent":
                counts["spawn_calls"] += 1
            if item.get("tool") == "wait":
                counts["wait_calls"] += 1
    return counts


def aggregate_arm(arm: str, run_ids: list[str]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for repetition, run_id in enumerate(run_ids, start=1):
        predictions = RUNS / run_id / "predictions"
        for directory in sorted(path for path in predictions.iterdir() if path.is_dir()):
            result = load_result(run_id, directory.name)
            trace = trace_counts(run_id, directory.name)
            process = result.get("predicted_answer", {}).get("process", {})
            rows.append(
                {
                    "repetition": repetition,
                    "run_id": run_id,
                    "item_id": result["id"],
                    "hard": int(result["hard"]),
                    "soft": float(result["soft"]),
                    "fail_reason": result.get("fail_reason", ""),
                    "provider_total_tokens": int(result["tokens"]["total"]),
                    "provider_input_tokens": int(result["tokens"]["input"]),
                    "provider_cached_input_tokens": int(result["tokens"]["cached_input"]),
                    "provider_output_tokens": int(result["tokens"]["output"]),
                    "loaded_skill_tokens": int(result["loaded_skill_tokens"]),
                    "shell_calls": int(result["shell_call_count"]),
                    "self_reported_generators": process.get("actual_generators"),
                    "self_reported_isolation": process.get("generator_isolation_preserved"),
                    **trace,
                }
            )
    total = len(rows)
    hard = sum(row["hard"] for row in rows)
    return {
        "rows": rows,
        "summary": {
            "runs": len(run_ids),
            "cases": total,
            "hard_passes": hard,
            "hard_rate": hard / total,
            "mean_soft": mean(row["soft"] for row in rows),
            "provider_total_tokens": sum(row["provider_total_tokens"] for row in rows),
            "provider_input_tokens": sum(row["provider_input_tokens"] for row in rows),
            "provider_cached_input_tokens": sum(row["provider_cached_input_tokens"] for row in rows),
            "provider_output_tokens": sum(row["provider_output_tokens"] for row in rows),
            "loaded_skill_tokens": sum(row["loaded_skill_tokens"] for row in rows),
            "shell_calls": sum(row["shell_calls"] for row in rows),
            "trace_spawn_calls": sum(row["spawn_calls"] for row in rows),
            "trace_wait_calls": sum(row["wait_calls"] for row in rows),
            "trace_errors": sum(row["trace_errors"] for row in rows),
            "self_reported_generators": sum(
                value for value in (row["self_reported_generators"] for row in rows) if isinstance(value, int)
            ),
            "wall_seconds": sum(ARM_WALL_SECONDS[arm]),
            "mean_run_wall_seconds": mean(ARM_WALL_SECONDS[arm]),
            "validation_executed": False,
            "test_executed": False,
        },
    }


def is_single_json_object(response: str) -> bool:
    try:
        value = json.loads(response)
    except json.JSONDecodeError:
        return False
    return isinstance(value, dict)


def build_blind_packet(normalizer: ModuleType) -> tuple[dict[str, Any], dict[str, Any]]:
    items = {item["id"]: item for item in json.loads((BENCHMARK / "train" / "items.json").read_text(encoding="utf-8"))}
    packet: dict[str, Any] = {
        "schema_version": 1,
        "judge_instructions": {
            "arms_are_anonymous": True,
            "dimensions": [
                "mechanism_diversity",
                "constraint_and_factual_preservation",
                "prior_art_recall",
                "prior_art_precision",
                "label_calibration",
                "feasibility",
                "actionability",
                "trap_precision",
                "shortlist_value",
                "authority_discipline",
            ],
            "scale": "0-4 per applicable dimension",
            "pairwise": "prefer_a, prefer_b, or tie",
        },
        "pairs": [],
    }
    mapping: dict[str, Any] = {"schema_version": 1, "pairs": {}}
    for repetition, item_id in BLIND_SAMPLE:
        pair_id = f"r{repetition}-{item_id}"
        arm_results: dict[str, dict[str, Any]] = {}
        for arm, run_ids in RUN_IDS.items():
            result = load_result(run_ids[repetition - 1], item_id)
            response = str(result["response"])
            raw_hash = hashlib.sha256(response.encode("utf-8")).hexdigest().upper()
            normalized = normalizer.normalize(result["predicted_answer"], raw_hash)
            normalized["single_json_object"] = is_single_json_object(response)
            arm_results[arm] = normalized
        control_first = int(hashlib.sha256(pair_id.encode("utf-8")).hexdigest(), 16) % 2 == 0
        a_arm = "single_session_control" if control_first else "upstream_adhd_host_normalized"
        b_arm = "upstream_adhd_host_normalized" if control_first else "single_session_control"
        item = items[item_id]
        packet["pairs"].append(
            {
                "pair_id": pair_id,
                "task_type": item["task_type"],
                "task_text": item["prediction"]["task_text"],
                "output_contract": item["prediction"]["output_contract"],
                "fixtures": item["prediction"]["files"],
                "variant_a": arm_results[a_arm],
                "variant_b": arm_results[b_arm],
            }
        )
        mapping["pairs"][pair_id] = {"variant_a": a_arm, "variant_b": b_arm}
    return packet, mapping


def main() -> int:
    normalizer = load_normalizer()
    arms = {arm: aggregate_arm(arm, run_ids) for arm, run_ids in RUN_IDS.items()}
    packet, mapping = build_blind_packet(normalizer)
    OUT.mkdir(parents=True, exist_ok=True)
    metrics = {
        "schema_version": 1,
        "benchmark_lock_sha256": "EFF995DD8637295A9530EF6F84B0D72A14767EF86EBEF6FBB227D1C1F185E9A1",
        "runtime_binding": "BASELINE_BINDING_REV2.json",
        "arms": arms,
        "promotion": {
            "single_session_control": "train_gate_failed_no_validation",
            "upstream_adhd_host_normalized": "train_gate_failed_no_validation",
        },
    }
    metrics_path = OUT / "w002-baseline-metrics.json"
    packet_path = OUT / "w002-baseline-blind-packet.json"
    map_path = RUNS / "W002_BLIND_MAP.json"
    metrics_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    map_path.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "metrics": str(metrics_path),
                "packet": str(packet_path),
                "blind_map": str(map_path),
                "hard": {arm: data["summary"]["hard_passes"] for arm, data in arms.items()},
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
