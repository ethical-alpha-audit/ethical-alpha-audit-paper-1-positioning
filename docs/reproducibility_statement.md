# Reproducibility Statement

## What IS Reproducible From This Repository

Running `python reproduce_all.py` deterministically produces:

- 5 CSV table files rendered from structured manuscript data
- 1 illustrative comparison chart from synthetic data
- 1 validation log
- 4 HTML notebook exports for code-free reading
- SHA-256 manifest of all outputs

A second clean run (after clearing `outputs/`) produces byte-identical results when executed with the same Python version and dependencies specified in `requirements.txt`.

### Determinism Verification Protocol

```bash
# Run 1
python reproduce_all.py
cp MANIFEST.sha256 MANIFEST_run1.sha256

# Run 2 (clean)
rm -rf outputs/figures/* outputs/tables/* outputs/logs/*
python reproduce_all.py

# Verify
diff MANIFEST_run1.sha256 MANIFEST.sha256
# Expected: no differences

python scripts/validate_outputs.py
# Expected: VALIDATION PASSED
```

## What is NOT Reproducible From This Repository

**Scientific claims are not computational outputs.** Paper 1 is a Viewpoint paper. Its claims are conceptual arguments, decision-theoretic reasoning, and interpretive assessments of a targeted document audit. These are not the product of code execution and cannot be "reproduced" by running notebooks.

**Companion study results are not reproduced here.** The manuscript references:
- A simulation study [25] with quantitative findings (zero unsafe deployments under gates vs 0.9% under composite scoring)
- A historical replay evaluation (60/61 failure cases rejected, 30/30 controls approved)
- PhysioNet clinical benchmark validation

These results are reproduced in companion paper repositories, not in this repository. See `docs/cross_study_reference.md` for details.

**The governance engine is not executed here.** The engine (`corrected_public_engine_v1_1.py`) lives in the Paper 4 repository.
