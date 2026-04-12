# Cross-Study Reference

## Purpose

This document explicitly defines the boundary between this repository (Paper 1) and companion study repositories. This is critical because the Paper 1 manuscript references several companion study findings that are NOT reproduced in this repository.

## Companion Studies Referenced in Paper 1

| Reference | Study | Repository |
|-----------|-------|------------|
| [25] | Brown W. "Operationalizing non-compensatory governance gates: a theory-testing simulation study." JMIR Med Inform 2026. | https://github.com/ethical-alpha-audit/ethical-alpha-audit-paper-2-governance-gates-simulation |
| Paper 4 | Historical replay evaluation of non-compensatory AI governance | https://github.com/ethical-alpha-audit/ethical-alpha-audit-paper-4-historical-replay |

## What This Repository Does NOT Reproduce

| Companion Result | Where It Lives | NOT Here Because |
|------------------|----------------|-----------------|
| Simulation: gates achieved zero unsafe deployments vs 0.9% for composite scoring | Paper 2 repo | Computational experiment belongs to companion study |
| Historical replay: 60/61 failure cases rejected, 30/30 controls approved | Paper 4 repo | Benchmark dataset and engine execution belong to companion study |
| PhysioNet clinical benchmark validation (2 sepsis models, 5000 patients) | Paper 4 repo | Clinical data processing belongs to companion study |
| Monte Carlo stability (12/12 stable, 200 iterations) | Paper 4 repo | Stochastic analysis belongs to companion study |
| Perturbation robustness (46/48 stable) | Paper 4 repo | Robustness testing belongs to companion study |
| Gate ablation analysis | Paper 4 repo | Ablation analysis belongs to companion study |

## The Governance Engine

The governance engine (`corrected_public_engine_v1_1.py`) is referenced in Paper 1's Data Availability section. This engine:

- Lives in the Paper 4 repository
- Is NOT included in this repository
- Is NOT executed by any notebook in this repository

## Why This Boundary Matters

Paper 1 is a Viewpoint paper proposing a governance architecture. Its contribution is conceptual and decision-theoretic. The companion studies provide empirical characterisation. Importing companion study computations into this repository would falsely imply that Paper 1 independently validates its claims through computation, which it does not.
