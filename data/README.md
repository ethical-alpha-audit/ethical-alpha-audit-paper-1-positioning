# Data Directory

## Purpose

This directory contains **structured extractions of manuscript content** for deterministic notebook rendering. These are NOT research datasets. They contain only information explicitly present in the manuscript text.

## Files

| File | Source | Description |
|------|--------|-------------|
| `table1_gap_audit.json` | Table 1, Paper1_Manuscript.docx | Decision-rule gap audit: 7 frameworks × 4 audit dimensions |
| `table2_risk_tiers.json` | Table 2 text, Paper1_Manuscript.docx | Risk-tiered minimum evidence thresholds: 5 domains × 2 tiers |
| `gates_specification.json` | Five Governance Gates section | Gate definitions: number, domain, overridable status, evidence floors |
| `override_specification.json` | Override Pathway sections | 4 operative criteria, 3 accumulation safeguards, provisional defaults |
| `futureai_mapping.json` | Discussion section | FUTURE-AI 6-principle → gate domain alignment (author's interpretive mapping) |
| `glossary.json` | Abbreviations section | ~14 abbreviations used in the manuscript |
| `epic_sepsis_illustration.json` | Illustrative Application section | Epic Sepsis Model gate-mapping with epistemic caveat |

## Provenance

Every JSON file includes a `metadata.source` field identifying the exact manuscript section from which it was extracted. Extraction was performed by manual transcription from the manuscript docx, verified against the rendered text.

## Epistemic Note

These files are structured renderings of manuscript content, not independently generated research data. They exist solely to enable deterministic notebook rendering of manuscript tables and specifications.
