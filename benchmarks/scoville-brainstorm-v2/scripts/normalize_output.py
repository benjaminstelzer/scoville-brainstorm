"""Normalize one raw brainstorm JSON answer for arm-blind semantic judging."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable


SKILL_SIGNATURE_PATTERNS = (
    r"\bscoville(?:[- ](?:brainstorm|code|plan|ui|scribe|handoff))?\b",
    r"\badhd(?: skill)?\b",
    r"\bbrainstorm-single-session-control\b",
)


def first(mapping: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = mapping.get(key)
        if value not in (None, "", [], {}):
            return value
    return None


def flatten_candidates(answer: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for container_key in ("idea_map", "hypothesis_map"):
        container = answer.get(container_key, [])
        if not isinstance(container, list):
            continue
        for entry in container:
            if not isinstance(entry, dict):
                continue
            nested = first(entry, "candidates", "ideas", "hypotheses")
            if isinstance(nested, list):
                for candidate in nested:
                    if isinstance(candidate, dict):
                        yield candidate
            else:
                yield entry


def normalize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    prior = candidate.get("prior_art")
    if not isinstance(prior, dict):
        prior = {}
    return {
        "id": first(candidate, "id", "candidate_id"),
        "title": first(candidate, "title", "name"),
        "mechanism": first(candidate, "mechanism", "navigation_mechanism", "failure_mechanism"),
        "benefit": first(candidate, "benefit", "expected_benefit", "leverage"),
        "closest_match": first(prior, "closest_match", "closest_analogue"),
        "prior_art_label": first(prior, "label"),
        "exact_difference": first(prior, "exact_difference"),
        "search_scope": first(prior, "search_scope"),
        "confidence": first(prior, "confidence"),
        "load_bearing_risk": first(candidate, "load_bearing_risk", "risk"),
        "falsification": first(
            candidate,
            "cheapest_falsification_experiment",
            "disconfirming_observation",
            "falsification",
        ),
    }


def normalize_direction(direction: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": first(direction, "id", "candidate_id"),
        "mechanism": first(direction, "mechanism", "navigation_mechanism"),
        "closest_match": first(direction, "closest_analogue", "closest_match"),
        "exact_difference": first(direction, "exact_difference"),
        "benefit": first(direction, "benefit", "expected_benefit"),
        "load_bearing_risk": first(direction, "load_bearing_risk", "risk"),
        "falsification": first(direction, "cheapest_falsification_experiment", "falsification"),
    }


def scrub_signature(value: Any) -> Any:
    if isinstance(value, str):
        result = value
        for pattern in SKILL_SIGNATURE_PATTERNS:
            result = re.sub(pattern, "[skill]", result, flags=re.IGNORECASE)
        return result
    if isinstance(value, list):
        return [scrub_signature(item) for item in value]
    if isinstance(value, dict):
        return {key: scrub_signature(item) for key, item in value.items()}
    return value


def normalize(answer: dict[str, Any], raw_hash: str) -> dict[str, Any]:
    activation = answer.get("activation") if isinstance(answer.get("activation"), dict) else {}
    if activation.get("activated") is False:
        return scrub_signature({
            "raw_sha256": raw_hash,
            "activation": False,
            "reason_code": activation.get("reason_code"),
            "direct_response": answer.get("response"),
            "side_effects": answer.get("side_effects"),
        })
    constraints = answer.get("constraints") if isinstance(answer.get("constraints"), dict) else {}
    research = answer.get("research") if isinstance(answer.get("research"), dict) else {}
    return scrub_signature({
        "raw_sha256": raw_hash,
        "activation": activation.get("activated"),
        "constraints_preserved": constraints.get("preserved"),
        "constraints_violated": constraints.get("violated"),
        "research_scope": scrub_signature(first(research, "scope_statement", "limitations")),
        "sources": first(research, "sources_read"),
        "close_matches": scrub_signature(research.get("close_matches")),
        "ideas": [normalize_candidate(candidate) for candidate in flatten_candidates(answer)],
        "deepened_directions": [
            normalize_direction(direction)
            for direction in answer.get("deepened_directions", [])
            if isinstance(direction, dict)
        ],
        "shortlist": scrub_signature(answer.get("shortlist")),
        "traps": scrub_signature(answer.get("traps")),
        "decision_point": scrub_signature(answer.get("decision_point")),
    })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = args.input.read_bytes()
    answer = json.loads(payload.decode("utf-8"))
    if not isinstance(answer, dict):
        raise ValueError("raw answer must be one JSON object")
    normalized = normalize(answer, hashlib.sha256(payload).hexdigest().upper())
    args.output.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
