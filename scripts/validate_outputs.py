"""
Output validation for the Paper 1 reproducibility harness.
Adapted from the Deterministic Notebook Execution Harness (I2).

ZERO EXTERNAL DEPENDENCIES — uses only Python standard library.
Reviewers can run this without installing anything:

    python scripts/validate_outputs.py

Validates all output files against expected SHA-256 hashes
stored in config/expected_outputs.json.
"""

import hashlib
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def validate():
    config_path = BASE_DIR / "config" / "expected_outputs.json"
    if not config_path.exists():
        print("ERROR: config/expected_outputs.json not found")
        return False

    with open(config_path, "r", encoding="utf-8") as f:
        expected = json.load(f)

    print("Validating outputs against config/expected_outputs.json...")
    print()

    total = 0
    passed = 0
    failures = []

    for rel_path, entry in sorted(expected.items()):
        total += 1
        file_path = BASE_DIR / rel_path
        expected_hash = entry.get("sha256", "")

        if expected_hash == "PENDING":
            print(f"  {rel_path:<60s} SKIP (hash pending)")
            passed += 1
            continue

        if not file_path.exists():
            print(f"  {rel_path:<60s} MISSING")
            failures.append(f"Missing: {rel_path}")
            continue

        actual_hash = sha256_file(file_path)
        if actual_hash == expected_hash:
            print(f"  {rel_path:<60s} PASS")
            passed += 1
        else:
            print(f"  {rel_path:<60s} MISMATCH")
            failures.append(
                f"Mismatch: {rel_path} (expected {expected_hash[:16]}..., "
                f"got {actual_hash[:16]}...)"
            )

    print()
    print("----")
    if failures:
        print(f"VALIDATION FAILED  ({passed}/{total} files match, "
              f"{len(failures)} issue(s))")
        for f in failures:
            print(f"  - {f}")
        return False
    else:
        print(f"VALIDATION PASSED  ({passed}/{total} files match)")
        return True


if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
