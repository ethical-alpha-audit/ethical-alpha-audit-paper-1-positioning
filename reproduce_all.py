"""
reproduce_all.py — Single-command reproducibility orchestrator for Paper 1.

Usage:
    python reproduce_all.py

Steps:
    1. Set PYTHONHASHSEED for deterministic execution
    2. Execute all notebooks in order (clears outputs first)
    3. Generate SHA-256 manifest
    4. Validate outputs against expected hashes
    5. Export notebooks to HTML for code-free reading
"""

import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def run_step(label, cmd):
    print(f"=== {label} ===")
    result = subprocess.run(cmd, cwd=BASE_DIR, text=True)
    if result.returncode != 0:
        print(f"FAIL: {label}")
        sys.exit(result.returncode)
    print(f"OK: {label}")
    print()


def main():
    # Step 0: Set deterministic hash seed
    settings = json.loads(
        (BASE_DIR / "config" / "harness_settings.json").read_text(encoding="utf-8")
    )
    os.environ["PYTHONHASHSEED"] = str(settings["python_hash_seed"])
    print(f"PYTHONHASHSEED={os.environ['PYTHONHASHSEED']}")
    print()

    # Step 1: Execute notebooks
    run_step(
        "Notebook execution",
        [sys.executable, "scripts/notebook_runner.py"],
    )

    # Step 2: Generate manifest
    run_step(
        "Manifest generation",
        [sys.executable, "scripts/hash_manifest.py"],
    )

    # Step 3: Validate outputs
    run_step(
        "Output validation",
        [sys.executable, "scripts/validate_outputs.py"],
    )

    # Step 4: Export HTML
    run_step(
        "HTML export",
        [sys.executable, "scripts/export_html.py"],
    )

    print("=" * 40)
    print("ALL STEPS PASSED")
    print("=" * 40)


if __name__ == "__main__":
    main()
