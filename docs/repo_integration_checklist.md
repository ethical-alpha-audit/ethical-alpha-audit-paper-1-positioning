# Pre-Submission Checklist

1. [ ] `python -m pytest tests/ -v` — all structural tests pass
2. [ ] `python reproduce_all.py` — ALL STEPS PASSED
3. [ ] Second clean run produces identical hashes (determinism verified)
4. [ ] README reviewer quick-start works (`python scripts/validate_outputs.py` → VALIDATION PASSED)
5. [ ] `docs/html/` contains 4 HTML files (code-free notebook exports)
6. [ ] CITATION.cff DOI field populated with Zenodo DOI
7. [ ] .zenodo.json metadata complete
8. [ ] VERSION matches across VERSION, CITATION.cff, .zenodo.json, and RELEASE_NOTES
9. [ ] `docs/cross_study_reference.md` companion repo URLs populated
10. [ ] All REPLACE markers resolved (search for "REPLACE" across all files)
