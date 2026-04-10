# Cover Note for Reviewers

## Quick Validation (No Installation Required)

```bash
python scripts/validate_outputs.py
```

**Expected result:** `VALIDATION PASSED`

This checks every committed output file against its pinned SHA-256 digest using only the Python standard library. A passing result confirms the checked-in outputs are byte-identical to those produced by the deterministic pipeline.

## Code-Free Notebook Reading

Pre-rendered HTML versions of all notebooks are available in `docs/html/`. These can be opened in any web browser without installing Jupyter or any dependencies.

## Full Re-Execution

```bash
pip install -r requirements.txt
python reproduce_all.py
```

This clears all notebook outputs, re-executes all four notebooks, regenerates the SHA-256 manifest, validates outputs, and exports HTML.

## What This Repository Contains

- The complete manuscript bundle (manuscript, figures, supplementary materials)
- Four explanatory notebooks that render and walk through the manuscript's key structures
- One illustrative worked example using synthetic data
- QA provenance trail (correction logs, fallacy register, disposition log)
- Full reproducibility infrastructure (hash-locked outputs, trace map, validation scripts)

## What This Repository Does NOT Contain

- The governance engine (`corrected_public_engine_v1_1.py`) — this lives in the Paper 4 companion repository
- Benchmark datasets or case files — these belong to companion studies
- Any computation that reproduces companion study results
- Any empirical analysis — Paper 1 is a Viewpoint paper

See `docs/cross_study_reference.md` for the full boundary specification.
