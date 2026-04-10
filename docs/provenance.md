# Provenance

## Manuscript Bundle

- **Source:** `Paper_1_CORRECTED.zip` (author's corrected submission bundle)
- **Contents:** Manuscript docx, supplementary materials docx, 2 main figures (PNG), 6 multimedia appendices (3 PNG + 3 DOCX), 4 QA audit logs (MD)
- **Integrity:** All files copied verbatim. SHA-256 hashes recorded in MANIFEST.sha256.

## Structured Data Files

All JSON files in `data/` were extracted from the manuscript by manual transcription:

- `table1_gap_audit.json` — from the formal Word table (Table 1) in Paper1_Manuscript.docx
- `table2_risk_tiers.json` — from paragraph text in the "Risk-Tiered Thresholds" section
- `gates_specification.json` — from the five gate description paragraphs
- `override_specification.json` — from the "Override Pathway" and "Preventing Override Accumulation" sections
- `futureai_mapping.json` — from the "Relationship to FUTURE-AI" discussion paragraph
- `glossary.json` — from the "Abbreviations" section
- `epic_sepsis_illustration.json` — from the "Illustrative Application" section

Each file includes a `metadata.source` field identifying its exact manuscript origin.

## Figures

- **Figure 1 and Figure 2:** Author-created schematic design artifacts. Not computationally generated.
- **Multimedia Appendices 1–3:** Author-created visual mockups and templates.
- **illustrative_compensation_example.png:** Computationally generated from synthetic data in NB-02.

## Execution Infrastructure

- **Scripts:** Adapted from the Deterministic Notebook Execution Harness (I2)
- **Structural patterns:** Based on the Paper 4 golden exemplar (I5) floor standard
- **Metadata templates:** Based on the EAA Repo Starter Pack (I3) Paper 1 template

## QA Provenance

Four audit log files in `provenance/audit_logs/` document the correction, QA disposition, quality improvement, and fallacy audit processes applied to the manuscript.
