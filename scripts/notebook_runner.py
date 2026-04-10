"""
Notebook execution runner for the Paper 1 reproducibility harness.
Adapted from the Deterministic Notebook Execution Harness (I2).

Reads config/notebook_plan.json and executes each notebook in order,
clearing outputs before re-execution to enforce fresh-run discipline.
"""

import json
import os
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

BASE_DIR = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def clear_notebook_outputs(nb):
    """Clear all code cell outputs to enforce fresh execution."""
    for cell in nb.cells:
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    return nb


def run_notebook(notebook_path: Path, timeout: int = 300):
    """Execute a single notebook, returning status dict."""
    if not notebook_path.exists():
        return {"status": "error", "message": f"Notebook missing: {notebook_path}"}

    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    nb = clear_notebook_outputs(nb)

    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(BASE_DIR)}},
    )

    start = time.time()
    try:
        executed = client.execute()
        duration = round(time.time() - start, 3)
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(executed, f)
        return {
            "status": "ok",
            "message": f"Executed {notebook_path.name}",
            "duration_seconds": duration,
        }
    except Exception as exc:
        duration = round(time.time() - start, 3)
        return {
            "status": "error",
            "message": str(exc),
            "duration_seconds": duration,
        }


def execute_all():
    """Execute all notebooks in plan order. Fail-fast on error."""
    plan = load_json(BASE_DIR / "config" / "notebook_plan.json")
    results = []

    for item in plan["execution_order"]:
        path = BASE_DIR / item["path"]
        print(f"  Running {item['name']}...", end=" ", flush=True)
        result = run_notebook(path)
        result["notebook"] = item["path"]
        results.append(result)
        if result["status"] == "ok":
            print(f"OK ({result['duration_seconds']}s)")
        else:
            print(f"FAIL: {result['message']}")
            break  # fail-fast

    return results


if __name__ == "__main__":
    results = execute_all()
    failed = [r for r in results if r["status"] != "ok"]
    if failed:
        raise SystemExit(1)
