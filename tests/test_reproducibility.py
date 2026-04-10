"""
test_reproducibility.py — Verify data file schemas and config validity.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_json(rel_path):
    with open(REPO_ROOT / rel_path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_table1_schema():
    d = _load_json("data/table1_gap_audit.json")
    assert "metadata" in d
    assert "columns" in d
    assert "rows" in d
    assert len(d["rows"]) == 7
    for row in d["rows"]:
        assert "Framework" in row


def test_table2_schema():
    d = _load_json("data/table2_risk_tiers.json")
    assert "metadata" in d
    assert "domains" in d
    assert len(d["domains"]) == 5
    for dom in d["domains"]:
        assert "gate" in dom
        assert "standard_risk_floor" in dom
        assert "higher_risk_floor" in dom


def test_gates_schema():
    d = _load_json("data/gates_specification.json")
    assert "gates" in d
    assert len(d["gates"]) == 5
    for g in d["gates"]:
        assert "number" in g
        assert "domain" in g
        assert "overridable" in g
        assert "minimum_evidence_floor" in g


def test_override_schema():
    d = _load_json("data/override_specification.json")
    assert "operative_criteria" in d
    assert len(d["operative_criteria"]) == 4
    assert "accumulation_safeguards" in d
    assert len(d["accumulation_safeguards"]) == 3


def test_futureai_schema():
    d = _load_json("data/futureai_mapping.json")
    assert "mappings" in d
    assert len(d["mappings"]) == 6


def test_glossary_schema():
    d = _load_json("data/glossary.json")
    assert "terms" in d
    assert len(d["terms"]) >= 10


def test_epic_sepsis_schema():
    d = _load_json("data/epic_sepsis_illustration.json")
    assert "case" in d
    assert "gate_mapping" in d
    assert len(d["gate_mapping"]) == 5


def test_config_valid_json():
    for cfg in ["harness_settings.json", "notebook_plan.json", "expected_outputs.json", "trace_map.json"]:
        _load_json(f"config/{cfg}")


def test_notebook_plan_has_four_entries():
    d = _load_json("config/notebook_plan.json")
    assert len(d["execution_order"]) == 4


def test_trace_map_has_seven_entries():
    d = _load_json("config/trace_map.json")
    assert len(d) == 7


def test_all_data_files_have_metadata():
    data_dir = REPO_ROOT / "data"
    for jf in data_dir.glob("*.json"):
        d = json.loads(jf.read_text(encoding="utf-8"))
        assert "metadata" in d, f"Missing metadata in {jf.name}"
