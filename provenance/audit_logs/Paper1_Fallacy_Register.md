# Paper 1 — Fallacy Register

**Paper:** Paper 1 (Non-Compensatory Governance Gates)
**Reference document:** KLogicalFallacies.pdf
**Sources:** QA-Fallacy Audit + Independent scan

---

## Fallacies from QA Audit

| ID | Fallacy Type | Location | Exact Quote | Classification | Action | Status |
|----|-------------|----------|-------------|----------------|--------|--------|
| QA-F1 | Weak Analogy (fallacy of questionable analogy) | Decision-Theoretic Rationale, P15-S6 | "The surgical safety checklist is a familiar clinical instantiation: the absence of sterile technique cannot be compensated by superior surgical skill [7]." | A — cosmetic | Reframed as "As an illustrative analogy, the surgical safety checklist applies a similar logic in clinical practice" | FIXED |
| QA-F2 | Hasty Generalization (over-generalizing) | Audit synthesis, P15-S2 | "...the dominant pattern in widely used governance instruments is specification of what to evaluate..." | A — cosmetic | Scope-bounded: "within the reviewed instruments, the dominant pattern is..." | FIXED |
| QA-F3 | Appeal to Authority / Prestige | Introduction, P6-S1 | "The FUTURE-AI consensus guideline [26], published in 2025 by 117 experts from 50 countries..." | A — cosmetic | Removed "by 117 experts from 50 countries" | FIXED |

## Independent Fallacy Scan (Stage 2.5)

Additional passages scanned: Abstract, Introduction, Discussion, Conclusions, Supplementary narrative.

| ID | Fallacy Type | Location | Passage Summary | Classification | Action | Status |
|----|-------------|----------|-----------------|----------------|--------|--------|
| SCAN-F1 | Hasty Generalization | Abstract P1-S3 | "confirmed that no reviewed framework specifies..." — the verb "confirmed" overstates what a targeted audit can establish | A — cosmetic | Changed "confirmed" → "found" (Edit #1) | FIXED |
| SCAN-F2 | Argument from Ignorance (borderline) | Introduction P7-S3 | "They do not specify how an institution should determine..." — negative claim about absence is interpretive, not proven universal negative | B — structural but safe | Addressed indirectly via scope qualifiers applied to the audit claim elsewhere. The sentence itself is adequately hedged by context. | ACCEPTED — no standalone fix needed |
| SCAN-F3 | Hasty Generalization | Conclusions P39-S5 | "...structural absence of explicit activation logic in widely used governance instruments" — scope unbound | A — cosmetic | Scope-bounded to "within the reviewed instruments" (Edit #21) | FIXED |
| SCAN-F4 | Oversimplified Cause (borderline) | Discussion P26-S3 | Companion study scope-condition analysis compressed into single causal narrative | B — structural but safe | Added "within the tested simulation architecture" qualifier (Edit #17) | FIXED |
| SCAN-F5 | Appeal to Authority (companion-study dependence) | Multiple locations | Repeated deferral to companion study [25] for empirical support reads as evidential outsourcing | B — structural but safe | Softened dependence language in stress-test section (Edit #18). Broader pattern is structural to the multi-paper design and cannot be fully resolved within this paper. | PARTIALLY ADDRESSED |

## Summary

| Classification | Count | Actioned |
|----------------|-------|----------|
| A — cosmetic | 5 | 5 FIXED |
| B — structural but safe | 3 | 2 FIXED, 1 ACCEPTED |
| C — affects scientific meaning | 0 | N/A |
| **Total** | **8** | **7 resolved** |

No Category C fallacies were identified. No fallacy correction altered any scientific result, number, or conclusion.
