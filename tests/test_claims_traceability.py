"""Claim registry integrity for Paper 1."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_p1_claims_count_and_ids():
    path = REPO_ROOT / "config" / "p1_claims.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    claims = data["claims"]
    assert len(claims) == 22
    ids = [c["id"] for c in claims]
    for i in range(1, 23):
        assert f"P1-C{i:02d}" in ids, f"Missing claim id P1-C{i:02d}"
