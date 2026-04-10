# Paper 1 — QA Disposition Log

**Paper:** Paper 1 (Non-Compensatory Governance Gates)
**QA File 1:** Paper1_Forensic_Claim_Audit_Report.docx
**QA File 2:** Paper1_Fallacy_Audit_Report.docx

---

## Forensic Claim Audit Dispositions

### Critical Blockers

| ID | Blocker | Severity | Disposition | Action Taken |
|----|---------|----------|-------------|--------------|
| B1 | Formatting integrity (section hierarchy, table rendering) | High | PARTIALLY ADDRESSED | Manuscript repacked with validated XML. Table 2 structural rendering is a Word formatting issue that may require manual style pass. Flagged for author attention. |
| B2 | Abstract claim density | High | APPLIED | Abstract simplified — removed detailed 91.7%/1.000/replay numbers. Retained one concise simulation result. (Edit #2) |
| B3 | Unqualified cross-paper comparative claim | High | APPLIED | Added explicit scope/denominator to zero-unsafe claim (Edit #7). Abstract simplified (Edit #2). |
| B4 | Citation/reference mismatch (TEHAI [28] vs WHO guidance) | High | FLAGGED — DO NOT APPLY (Category C) | The forensic audit identifies that reference [28] appears to be a WHO guidance document, while the text names it as TEHAI. Changing reference numbering or citation targets could affect scientific claim chains. **Author action required**: verify whether [28] correctly points to the TEHAI source or whether the reference entry needs correction. |
| B5 | Supplement naming inconsistency | Medium | FLAGGED FOR AUTHOR | The manuscript uses "Supplementary Appendix A–E" for sections within Paper1_Supplementary_Materials.docx and "Multimedia Appendix 1–6" for standalone files. These appear to be intentionally different naming conventions for different content types. JMIR may require harmonisation. **Author action required**: confirm JMIR-compliant naming convention and apply consistently. |
| B6 | Overstrong reproducibility statements | High | APPLIED | Softened "bit-identical" language to "designed as deterministic...intended to produce identical results" (Edit #10). |

### High-Risk Claim Units

| Loc. | Claim | Disposition | Action |
|------|-------|-------------|--------|
| P1-S3 | Audit confirmed no framework specifies... | APPLIED | Scope-bounded + appendix anchor (Edit #1) |
| P2-S3 | Dense companion-study results | APPLIED | Simplified (Edit #2) |
| P7-S6 | Novelty lies in three elements | ACCEPTED AS-IS | This is a design proposal statement; normative framing is appropriate. No citation needed for a proposal's own specification. |
| P8-S2 | Zero unsafe deployments | APPLIED | Added denominator + explicit scope (Edit #7) |
| P9-S3 | Audit method description | APPLIED | Added coding frame anchor (Edit #12) |
| P15-S3 | No reviewed framework combined... | APPLIED | Scope-bounded + anchored (Edit #5) |
| P17-S1 | Three pathway outcomes | ACCEPTED AS-IS | This describes the paper's own proposed architecture. No external citation required for a design specification. |
| P17-S5 | Gate 1 non-overridable rationale | ACCEPTED AS-IS | Normative design rationale. Appropriate without external citation. |
| P18-S2 | Gate 2 subpopulation risk | ACCEPTED AS-IS | Standard risk description for equity gate. |
| P18-S4 | Gate 2 override criteria | ACCEPTED AS-IS | Design specification. |
| P18-S6 | Gate 3 documentation functions | ACCEPTED AS-IS | Normative description. |
| P19-S3 | Gate 4 moral hazard | ACCEPTED AS-IS | Established concept in governance literature. |
| P19-S7 | Gate 5 non-overridable rationale | ACCEPTED AS-IS | Normative design rationale. |
| P20-S6 | Table 2 risk-tiered thresholds | ACCEPTED AS-IS | These are proposed design parameters, not empirical claims. |
| P22-S1/S2 | Override pathway description | ACCEPTED AS-IS | Design specification. |
| P24-S1 | Shared service model | ACCEPTED AS-IS | Proposal. |
| P25-S6 | Gate 3/5 false-negative resolution | ACCEPTED AS-IS | Logical inference from the proposed architecture. |
| P28-S1 | PhysioNet validation claim | APPLIED | Added appendix anchor + softened (Edit #8) |
| P28-S2–S5 | PhysioNet benchmark details | PARTIALLY ADDRESSED | Appendix C anchor added at section level (Edit #8, #14). Individual sentence-level anchors not added to avoid over-cluttering. |
| P28-S6 | PhysioNet conclusion | APPLIED | Softened "indicates" → "is consistent with" (Edit #9) |
| P29-S2 | 60/61 failure cases | APPLIED | Appendix C anchor added (Edit #14) |
| P36-S3 | Companion dataset claim | APPLIED | Added [25] citation anchor (Edit #19) |
| P40-S2 | Override pathway in conclusion | ACCEPTED AS-IS | Summary of architecture already described. |
| P88-S1 | AI disclosure | ACCEPTED AS-IS | Administrative statement. |
| P90-S1 | Supplementary Appendix A reference | VERIFIED | Appendix A exists in Paper1_Supplementary_Materials.docx. |
| P91-S1 | Re-execution identical outputs | APPLIED via Edit #10 | Softened overall reproducibility language. |
| P91-S2 | Corrected engine bit-identical | APPLIED | Edit #10. |
| P91-S3/S4 | Engine drift correction claims | FLAGGED FOR AUTHOR | These are technical provenance claims that cannot be verified from the manuscript alone. Author should ensure repository/hash support exists before submission. |
| P93-S1 | Data availability | APPLIED | Clarified secondary data usage (Edit #15) |
| P101-S1 | Supplementary Appendix D reference | VERIFIED | Appendix D exists in Paper1_Supplementary_Materials.docx. |

### DOI/Repository References

| Item | Location | Disposition |
|------|----------|-------------|
| Zenodo DOI: "to be provided upon publication" | Supplementary Materials (Appendix A) | **IGNORED — MANUAL POST-PUBLICATION STEP** |
| Public repository/hash references | Reproducibility section | **IGNORED — MANUAL POST-PUBLICATION STEP** (per governance rule: no fabrication of DOI/repository links) |
| Reproducibility artefact reference | P91-S4 | **IGNORED — MANUAL POST-PUBLICATION STEP** |

---

## Fallacy Audit Dispositions

| Fallacy ID | Type | Location | Confidence | Classification | Disposition | Action |
|------------|------|----------|------------|----------------|-------------|--------|
| F1 | Weak Analogy | P15-S6 (surgical checklist) | Medium | A — cosmetic | APPLIED | Reframed as "illustrative analogy" (Edit #6) |
| F2 | Hasty Generalization | P15-S2 ("dominant pattern") | Medium | A — cosmetic | APPLIED | Scope-bounded to reviewed instruments (Edit #4) |
| F3 | Appeal to Authority/Prestige | P6-S1 (FUTURE-AI "117 experts") | Low | A — cosmetic | APPLIED | Removed "117 experts from 50 countries" (Edit #3) |

All three fallacy instances were Category A (cosmetic) — wording adjustments that do not affect scientific meaning.
