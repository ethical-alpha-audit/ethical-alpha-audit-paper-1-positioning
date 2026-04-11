"""
Output validation for the Paper 1 reproducibility harness.
Adapted from the Deterministic Notebook Execution Harness (I2).

ZERO EXTERNAL DEPENDENCIES — uses only Python standard library.
Reviewers can run this without installing anything:

    python scripts/validate_outputs.py
    python scripts/validate_outputs.py --update-expected

Validates all output files against expected SHA-256 hashes
stored in config/expected_outputs.json.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

# Non-deterministic outputs: excluded from hashing, comparison, and counts.
EXCLUDED_PATHS = frozenset(
    {
        "outputs/logs/notebook_run_log.txt",
    }
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def validate(*, update_expected: bool) -> bool:
    config_path = BASE_DIR / "config" / "expected_outputs.json"
    if not config_path.exists():
        print("ERROR: config/expected_outputs.json not found")
        return False

    with open(config_path, "r", encoding="utf-8") as f:
        expected = json.load(f)

    if update_expected:
        print("Updating config/expected_outputs.json from current outputs...")
        print()
        new_data: dict = {}
        for rel_path, entry in expected.items():
            if rel_path in EXCLUDED_PATHS:
                print(f"Skipping non-deterministic output: {rel_path}")
                continue
            new_entry = dict(entry)
            if new_entry.get("sha256") == "PENDING":
                new_data[rel_path] = new_entry
                continue
            file_path = BASE_DIR / rel_path
            if file_path.exists():
                new_entry["sha256"] = sha256_file(file_path)
            new_data[rel_path] = new_entry

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print()
        print("Expected outputs updated successfully")
        return True

    print("Validating outputs against config/expected_outputs.json...")
    print()

    total = 0
    passed = 0
    failures = []

    for rel_path, entry in sorted(expected.items()):
        if rel_path in EXCLUDED_PATHS:
            print(f"Skipping non-deterministic output: {rel_path}")
            continue

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


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate or refresh expected output hashes.")
    parser.add_argument(
        "--update-expected",
        action="store_true",
        help="Rewrite config/expected_outputs.json with newly computed hashes (non-excluded paths only).",
    )
    args = parser.parse_args()
    success = validate(update_expected=args.update_expected)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
