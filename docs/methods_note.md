# Methods Note

## Paper Character

Paper 1 ("Non-Compensatory Governance Gates for Clinical Artificial Intelligence Deployment") is a **Viewpoint** paper published in JMIR Medical Informatics. It proposes a governance architecture through conceptual argument, decision-theoretic reasoning, and a targeted document audit. It is not a computational experiment paper.

## What the Notebooks Do

The four notebooks in this repository:

1. **Render and explain** structured manuscript content (tables, gate specifications, mappings)
2. **Provide one illustrative worked example** using entirely synthetic data to demonstrate compensatory vs non-compensatory logic
3. **Validate** repository bundle integrity

No notebook executes a governance engine, processes real patient data, or reproduces companion study results.

## Data Provenance

All data files in `data/` are structured extractions of manuscript content — they contain only information explicitly present in the manuscript text. They are not independently generated research datasets.

## Single Generated Figure

Only one figure is computationally generated: `outputs/figures/illustrative_compensation_example.png`. This uses five synthetic numbers to illustrate a concept. All other figures in the repository are static schematic design artifacts created by the author.
