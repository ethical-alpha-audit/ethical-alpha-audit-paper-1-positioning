"""Table 1 (decision-rule gap audit) load, validation, and CSV rendering."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import pandas as pd


def load_table1_data(repo_root: Path) -> Dict[str, Any]:
    path = repo_root / "data" / "table1_gap_audit.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_table1_schema(table1_data: Dict[str, Any]) -> None:
    assert "columns" in table1_data, "Missing 'columns' key"
    assert "rows" in table1_data, "Missing 'rows' key"
    assert len(table1_data["rows"]) == 7, f"Expected 7 rows, got {len(table1_data['rows'])}"
    for row in table1_data["rows"]:
        for col in table1_data["columns"]:
            assert col in row, f"Missing column '{col}' in row: {row.get('Framework', '?')}"


def render_table1_dataframe(table1_data: Dict[str, Any]) -> pd.DataFrame:
    return pd.DataFrame(table1_data["rows"], columns=table1_data["columns"])


def write_table1_csv(repo_root: Path, df: pd.DataFrame) -> Path:
    output_path = repo_root / "outputs" / "tables" / "table1_rendered.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
