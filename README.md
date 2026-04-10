# Non-Compensatory Governance Gates for Clinical AI Deployment

[![DOI](https://zenodo.org/badge/1194627228.svg)](https://doi.org/10.5281/zenodo.19499782)

> **Paper 1** of the Ethical Alpha Audit five-paper bundle
>
> Author: Walter Brown, MSc, MA — Ethical Alpha Audit
> ORCID: [0000-0002-6050-8522](https://orcid.org/0000-0002-6050-8522)

## Reviewer quick validation (no execution required)

```bash
python scripts/validate_outputs.py
```

**Expected result:** `VALIDATION PASSED`

This checks every output file against its pinned SHA-256 digest. No notebook execution, no dependencies beyond Python stdlib.

**To re-execute the full pipeline** (requires dependencies):

```bash
pip install -r requirements.txt
python reproduce_all.py
```

## What this repository supports

This repository is the publication-grade companion to Paper 1, a Viewpoint paper proposing a non-compensatory governance gate architecture for clinical AI deployment. It provides:

1. The complete manuscript bundle (manuscript, supplementary materials, figures)
2. A structured walkthrough of the decision-rule gap audit (Table 1)
3. Rendered specifications of the five-gate architecture, risk-tiered thresholds, and FUTURE-AI alignment
4. An illustrative worked example comparing compensatory and non-compensatory logic (synthetic data)
5. A walkthrough of the override pathway and the Epic Sepsis Model illustrative application
6. Full QA provenance trail (correction logs, fallacy register, disposition log)

## What this repository does NOT do

- **Does not execute the governance engine.** The engine (`corrected_public_engine_v1_1.py`) lives in the Paper 4 companion repository.
- **Does not replay benchmark datasets.** Case files and benchmark data belong to companion studies.
- **Does not reproduce companion study results.** Simulation findings, historical replay results, and PhysioNet validation are produced in companion repositories.
- **Does not perform empirical analysis.** Paper 1 is a Viewpoint paper. Its claims are conceptual, not computational.

See `docs/cross_study_reference.md` for the full companion study boundary specification.

## Repository structure

```
manuscript/         Authoritative manuscript bundle (docx + supplementary)
figures/            Main figures (static schematic design artifacts)
supplementary/      Multimedia appendices (PNG + DOCX)
data/               Structured manuscript extractions (JSON) for notebook rendering
notebooks/          4 Jupyter notebooks (explanatory, not analytical)
scripts/            Execution harness (notebook runner, hash validator, HTML export)
config/             Determinism settings, notebook plan, trace map, expected outputs
outputs/            Generated tables, figures, and logs (hash-locked)
provenance/         QA audit logs (correction, disposition, quality, fallacy)
docs/               Methods note, provenance, reproducibility statement, cross-study reference
docs/html/          Static HTML exports for reading without Jupyter
tests/              Structural and reproducibility tests
```

## Notebooks

| # | Notebook | Purpose | Epistemic Status |
|---|----------|---------|-----------------|
| 01 | Claim Traceability | Decision-rule gap audit walkthrough (Table 1) | EXPLANATORY |
| 02 | Framework and Specification | Gate architecture, risk tiers, FUTURE-AI, worked example | EXPLANATORY + ILLUSTRATIVE |
| 03 | Override and Illustration | Override pathway logic, Epic Sepsis case | EXPLANATORY + ILLUSTRATIVE |
| 04 | Release Validation | Bundle integrity, hash checks, trace map | VALIDATION |

For code-free reading, see `docs/html/`.

## Figures

Both main figures are **static schematic design artifacts**, not computationally generated:
- `figures/Figure1_GovernanceGates.png` — Governance gate architecture diagram
- `figures/Figure2_OverrideRequestForm.png` — Structured override request form

The only computationally generated figure is `outputs/figures/illustrative_compensation_example.png`, which uses synthetic data and is clearly labeled as illustrative.

## How to cite

See `CITATION.cff` for structured citation metadata. If using this repository, please cite both the manuscript and this reproducibility package.

## License

MIT. See `LICENSE`.
