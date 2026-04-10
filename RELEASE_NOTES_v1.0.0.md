# Release Notes — v1.0.0

## Release: v1.0.0-submission

**Date:** REPLACE_WITH_RELEASE_DATE
**Paper:** Non-Compensatory Governance Gates for Clinical Artificial Intelligence Deployment
**Target journal:** JMIR Medical Informatics

## What This Release Contains

- Complete manuscript bundle (manuscript + supplementary materials + 2 figures + 6 multimedia appendices)
- 4 explanatory Jupyter notebooks with deterministic execution
- 7 structured data files extracted from manuscript content
- 4 QA audit logs documenting correction, disposition, quality improvement, and fallacy audit
- Full reproducibility infrastructure: hash-locked outputs, trace map, validation scripts, HTML exports
- Publication metadata: CITATION.cff, .zenodo.json, LICENSE (MIT)

## Known Limitations

- Table 2 (risk-tiered thresholds) was manually extracted from manuscript paragraph text, not from a formal Word table. Transcription has been verified against the manuscript but is inherently manual.
- The decision-rule gap audit was conducted by a single author. Whether other analysts would derive the same coding is an empirical question (acknowledged in the manuscript).
- Provisional default values (90-day override, 30% escalation trigger, concurrent override limit) are proposed for pilot testing, not empirically validated (acknowledged in the manuscript).
- Multimedia Appendix 4 may contain text duplicated from the manuscript body (flagged in QA log, item SELF-004). Included as-is pending author review.
- Reference [28] TEHAI/WHO citation requires author verification (flagged in QA log, item B4).

## Unresolved REPLACE Markers

The following markers require population at release time:

- `REPLACE_WITH_ZENODO_DOI` — in README.md
- `REPLACE_WITH_RELEASE_DATE` — in CITATION.cff and this file
- `REPLACE_WITH_ORG` — in CITATION.cff (GitHub organisation)
- `REPLACE_WITH_PAPER2_REPO_URL` — in docs/cross_study_reference.md

## Companion Repositories

- Paper 4 (Historical Replay): https://github.com/REPLACE_WITH_ORG/ethical-alpha-audit-paper-4-historical-replay
- Paper 2 (Simulation): REPLACE_WITH_PAPER2_REPO_URL
