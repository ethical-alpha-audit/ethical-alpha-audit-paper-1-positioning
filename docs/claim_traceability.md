# Claim Traceability Matrix

**Repo:** ethical-alpha-audit-paper-1-positioning  
**Updated:** 2026-04-19  
**Claims:** 22 (see `config/p1_claims.json`)  
**TRACEABILITY STATUS: VERIFIED** — 22/22 claim IDs enumerated with explicit coverage class per row; no claim omitted from the matrix.

**Compensatory anchoring (EXTERNAL empirical claims):** P1-C06, P1-C07, and P1-C19 are anchored to companion manuscripts / supplementary materials named in `docs/cross_study_reference.md` and flagged **EXTERNAL** here so they are not treated as silent gaps in this Viewpoint-only harness.

Per-row **Status** values below record how each claim is evidenced in-repo (TRACEABLE / NARRATIVE / EXTERNAL / PARTIAL).

## CLAIM EXTRACTION COMPLETE: 22 claims identified for P1

| Claim ID | Claim (summary) | Code / data | Notebook | Output | Status |
|----------|-----------------|-------------|----------|--------|--------|
| P1-C01 | Governance instruments underspecify binary deployment activation logic | — | 01 | `outputs/tables/table1_rendered.csv` (context) | PARTIAL (narrative + audit motivation) |
| P1-C02 | Compensatory aggregation permits cross-domain offsetting | — | 01 | — | NARRATIVE |
| P1-C03 | Audit: no reviewed instrument specifies full threshold + non-compensatory + constrained override rule | `data/table1_gap_audit.json` | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C04 | Proposed conjunctive five-domain gate architecture | `data/gates_specification.json` | 02 | `outputs/tables/gates_summary.csv` | TRACEABLE |
| P1-C05 | Risk-tiered floors; override for G2–4; shared service model | `data/table2_risk_tiers.json`, `data/override_specification.json` | 02, 03 | `outputs/tables/table2_rendered.csv`, `outputs/tables/override_summary.csv` | TRACEABLE |
| P1-C06 | Companion simulation: gate vs composite under heterogeneous evidence | — | — | — | EXTERNAL (companion manuscript [25]) |
| P1-C07 | Historical replay: preliminary convergent evidence | — | — | — | EXTERNAL (companion manuscript) |
| P1-C08 | Four audit coding dimensions (MA4) | `data/table1_gap_audit.json` (column schema) | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C09 | Conservative operational coding rule | `data/table1_gap_audit.json` (`metadata.note`) | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C10 | Table 1 characterisations for seven frameworks | `data/table1_gap_audit.json` | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C11 | Dominant pattern: lifecycle / evidence expectations vs binding combination rule | `data/table1_gap_audit.json` | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C12 | No reviewed instrument combines all three structural elements | `data/table1_gap_audit.json` | 01 | `outputs/tables/table1_rendered.csv` | TRACEABLE |
| P1-C13 | Conjunctive decision-theoretic rationale | — | 02 | — | NARRATIVE |
| P1-C14 | Gate roles; G1/G5 non-overridable; G2–4 overridable | `data/gates_specification.json`, `data/override_specification.json` | 02, 03 | `outputs/tables/gates_summary.csv`, `outputs/tables/override_summary.csv` | TRACEABLE |
| P1-C15 | Table 2 risk-tiered thresholds | `data/table2_risk_tiers.json` | 02 | `outputs/tables/table2_rendered.csv` | TRACEABLE |
| P1-C16 | Four override criteria; three accumulation safeguards | `data/override_specification.json` | 03 | `outputs/tables/override_summary.csv` | TRACEABLE |
| P1-C17 | Epic Sepsis illustration mapping | `data/epic_sepsis_illustration.json` | 03 | (narrative cells) | TRACEABLE |
| P1-C18 | FUTURE-AI ↔ five gates mapping | `data/futureai_mapping.json` | 02 | `outputs/tables/futureai_alignment.csv` | TRACEABLE |
| P1-C19 | PhysioNet preliminary validation narrative | — | — | — | EXTERNAL / SUPPLEMENT (not reproduced in this repo) |
| P1-C20 | Scope boundaries (necessary not sufficient) | — | — | — | NARRATIVE |
| P1-C21 | Pilot endpoints | — | — | — | NARRATIVE |
| P1-C22 | Limitations (single auditor, provisional defaults, etc.) | `data/table1_gap_audit.json` (`metadata`) | 01 | — | PARTIAL |

### Legend

- **TRACEABLE**: Structured JSON in `data/` plus notebook pipeline produces cited tables/artefacts.
- **PARTIAL**: Some grounding in repo metadata or outputs; remainder is manuscript-only.
- **NARRATIVE**: Stated in manuscript; not isolated as a separate computational artefact in this repository.
- **EXTERNAL**: Empirical or extended evidence in companion papers or appendices outside this repo’s harness.

### STM / output cross-reference

See `config/trace_map.json` for STM-target tags on committed outputs (`outputs/tables/*.csv`, `outputs/figures/*.png`, `outputs/logs/notebook_run_log.txt`).
