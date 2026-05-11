# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is (and is not)

This is the publication-grade reproducibility package for **Paper 1** ("Non-Compensatory Governance Gates for Clinical AI Deployment") of the Ethical Alpha Audit five-paper bundle. Paper 1 is a **Viewpoint paper**: its claims are conceptual, decision-theoretic, and based on a targeted document audit — **not computational findings**.

This shapes every change you'll be asked to make:

- The notebooks **render and explain** structured manuscript content; they do not analyse data. The only computationally generated figure (`outputs/figures/illustrative_compensation_example.png`) uses five synthetic numbers to illustrate compensatory vs. non-compensatory logic.
- The governance engine (`corrected_public_engine_v1_1.py`) lives in **Paper 4's repo**, not here. Two structural tests (`test_no_engine_present`, `test_no_benchmark_data` in [tests/test_harness_structure.py](tests/test_harness_structure.py)) enforce that boundary — if you're tempted to add engine code or benchmark datasets, you're in the wrong repo. See [docs/cross_study_reference.md](docs/cross_study_reference.md) for the full companion-study boundary.
- Empirical results referenced in the manuscript (simulation, historical replay, PhysioNet) belong to companion repositories and must not be imported here.

## Commands

All commands run from the repo root.

| Command | Purpose |
|---|---|
| `python scripts/validate_outputs.py` | Reviewer quick-validation. Zero deps (stdlib only). Compares output files against pinned SHA-256 in `config/expected_outputs.json`. Expected: `VALIDATION PASSED`. |
| `python reproduce_all.py` | Full pipeline: set `PYTHONHASHSEED=42`, execute all 4 notebooks in order, regenerate `MANIFEST.sha256`, validate hashes, export notebooks → `docs/html/`. |
| `python reproduce_all.py --update-expected` | Refresh `config/expected_outputs.json` from current outputs (use only when an intentional output change is being baselined). |
| `python -m pytest tests/ -v` | Structural + schema tests (no notebook execution). |
| `python -m pytest tests/test_reproducibility.py::test_table1_schema -v` | Run a single test by path::name. |
| `python scripts/notebook_runner.py` | Execute notebooks only (skips manifest/validation/export). |
| `python scripts/hash_manifest.py` | Regenerate `MANIFEST.sha256` only. |
| `python scripts/export_html.py` | Re-export notebooks to `docs/html/` only. |

Pin: pip install with the exact versions in [requirements.txt](requirements.txt) — `requirements.lock.txt` and `environment.lock` capture the full resolved environment.

## Architecture

### Determinism contract

The whole repo is built around **byte-identical reproducibility**. Three artifacts hold it together:

- [config/harness_settings.json](config/harness_settings.json) sets `PYTHONHASHSEED=42` (loaded by `reproduce_all.py` before any notebook runs).
- [config/notebook_plan.json](config/notebook_plan.json) declares notebook execution order and each notebook's expected outputs.
- [config/expected_outputs.json](config/expected_outputs.json) pins SHA-256 for every output file. `outputs/logs/notebook_run_log.txt` is the only intentionally excluded non-deterministic output (see `EXCLUDED_PATHS` in [scripts/validate_outputs.py](scripts/validate_outputs.py:24)).

The two-run determinism protocol (clear outputs, re-run, diff manifests) is documented in [docs/reproducibility_statement.md](docs/reproducibility_statement.md).

### Notebook flow

Notebooks execute in declared order; outputs are cleared before each run to enforce fresh execution ([scripts/notebook_runner.py:25](scripts/notebook_runner.py:25)). `nbclient.NotebookClient` runs each notebook from the **repo root** as its working directory.

| # | Notebook | Outputs |
|---|---|---|
| 01 | `01_claim_traceability.ipynb` | `outputs/tables/table1_rendered.csv` |
| 02 | `02_framework_and_specification.ipynb` | `table2_rendered.csv`, `gates_summary.csv`, `futureai_alignment.csv`, `illustrative_compensation_example.png` |
| 03 | `03_override_and_illustration.ipynb` | `override_summary.csv` |
| 04 | `04_release_validation.ipynb` | `notebook_run_log.txt` (excluded from hash check) |

Notebooks pull from structured JSON in `data/` (manuscript extractions) and may import the `p1_harness` package — only `src/p1_harness/table1_gap_audit.py` exists today; add new modules there if a notebook accretes non-trivial logic.

### Traceability layer

Each output is mapped to the notebook that produced it and to STM ("structured-traceability-map") targets in [config/trace_map.json](config/trace_map.json). The 22 manuscript claims live in [config/p1_claims.json](config/p1_claims.json) and are verified by [tests/test_claims_traceability.py](tests/test_claims_traceability.py). When you add or rename an output, update both `expected_outputs.json` and `trace_map.json`.

### Canonical document tracking

[canonical_documents.yaml](canonical_documents.yaml) is the WS-CANONICAL-SOURCE-AUTOMATION schema (v1.0) tracking the authoritative manuscript, supplementary, notebook, and multimedia files with SHA-256, sizes, and drift status across the bundle's four axes. Don't hand-edit lightly — it carries audit basis and editorial commitments (target journal, variant lock history). If you change a tracked file, you may also need to update its `canonical_sha256` here.

## Repo conventions

- **No-commit-manuscripts policy**: `inputs/*.docx` and `inputs/*.pdf` are working-tree-only — required on disk for PowerShell readiness gates and notebooks, but never committed (see `.gitignore` lines 34–41). The manuscript snapshot used for citation lives in [manuscript/Paper1_Manuscript.docx](manuscript/Paper1_Manuscript.docx); the working copy is `inputs/manuscript.docx`.
- **Pre-submission checklist** is at [docs/repo_integration_checklist.md](docs/repo_integration_checklist.md). It includes verifying determinism with a second clean run.
- **Audit logs** under `provenance/audit_logs/` (correction, disposition, quality, fallacy registers) are part of the publication-grade record — don't delete them when cleaning up, even if they look like agent scratch.
- **Hash dirs** for `MANIFEST.sha256` are listed at [scripts/hash_manifest.py:14](scripts/hash_manifest.py:14). If you add a new top-level directory whose contents should be in the manifest, append it there.
