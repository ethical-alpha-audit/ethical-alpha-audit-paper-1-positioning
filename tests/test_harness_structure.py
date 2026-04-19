"""
test_harness_structure.py — Verify repository directory structure and key files.
Adapted from I2 and I5 test patterns.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DIRS = [
    "manuscript",
    "figures",
    "supplementary",
    "data",
    "notebooks",
    "scripts",
    "src",
    "src/p1_harness",
    "config",
    "outputs",
    "outputs/figures",
    "outputs/tables",
    "outputs/logs",
    "provenance",
    "provenance/audit_logs",
    "docs",
    "docs/html",
    "html",
    "tests",
]

EXPECTED_ROOT_FILES = [
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    "VERSION",
    "RELEASE_NOTES_v1.0.0.md",
    "reproduce_all.py",
    "requirements.txt",
    "environment.yml",
    "runtime.txt",
]

EXPECTED_DATA_FILES = [
    "data/table1_gap_audit.json",
    "data/table2_risk_tiers.json",
    "data/gates_specification.json",
    "data/override_specification.json",
    "data/futureai_mapping.json",
    "data/glossary.json",
    "data/epic_sepsis_illustration.json",
    "data/README.md",
]

EXPECTED_NOTEBOOKS = [
    "notebooks/01_claim_traceability.ipynb",
    "notebooks/02_framework_and_specification.ipynb",
    "notebooks/03_override_and_illustration.ipynb",
    "notebooks/04_release_validation.ipynb",
]

EXPECTED_SCRIPTS = [
    "scripts/notebook_runner.py",
    "scripts/hash_manifest.py",
    "scripts/validate_outputs.py",
    "scripts/export_html.py",
]

EXPECTED_CONFIGS = [
    "config/harness_settings.json",
    "config/notebook_plan.json",
    "config/expected_outputs.json",
    "config/trace_map.json",
    "config/p1_claims.json",
    "config/portfolio_dependency_lock.json",
]


def test_directories_exist():
    for d in EXPECTED_DIRS:
        assert (REPO_ROOT / d).is_dir(), f"Missing directory: {d}"


def test_root_files_exist():
    for f in EXPECTED_ROOT_FILES:
        assert (REPO_ROOT / f).is_file(), f"Missing root file: {f}"


def test_data_files_exist():
    for f in EXPECTED_DATA_FILES:
        assert (REPO_ROOT / f).is_file(), f"Missing data file: {f}"


def test_notebooks_exist():
    for f in EXPECTED_NOTEBOOKS:
        assert (REPO_ROOT / f).is_file(), f"Missing notebook: {f}"


def test_scripts_exist():
    for f in EXPECTED_SCRIPTS:
        assert (REPO_ROOT / f).is_file(), f"Missing script: {f}"


def test_configs_exist():
    for f in EXPECTED_CONFIGS:
        assert (REPO_ROOT / f).is_file(), f"Missing config: {f}"


def test_manuscript_files():
    assert (REPO_ROOT / "manuscript" / "Paper1_Manuscript.docx").is_file()
    assert (REPO_ROOT / "manuscript" / "Paper1_Supplementary_Materials.docx").is_file()


def test_inputs_attachment_requirements():
    """Portfolio attachment_requirements.json for paper-1 (manuscript + supplementary.pdf)."""
    assert (REPO_ROOT / "inputs" / "supplementary.pdf").is_file()
    docx = REPO_ROOT / "inputs" / "manuscript.docx"
    pdf = REPO_ROOT / "inputs" / "manuscript.pdf"
    assert docx.is_file() or pdf.is_file(), "Expected manuscript.docx or manuscript.pdf under inputs/"


def test_src_table1_module_importable():
    import sys

    sys.path.insert(0, str(REPO_ROOT / "src"))
    from p1_harness.table1_gap_audit import load_table1_data, validate_table1_schema

    data = load_table1_data(REPO_ROOT)
    validate_table1_schema(data)


def test_figures():
    assert (REPO_ROOT / "figures" / "Figure1_GovernanceGates.png").is_file()
    assert (REPO_ROOT / "figures" / "Figure2_OverrideRequestForm.png").is_file()


def test_audit_logs():
    logs = [
        "Paper1_Correction_Log.md",
        "Paper1_QA_Disposition_Log.md",
        "Paper1_Quality_Improvements_Log.md",
        "Paper1_Fallacy_Register.md",
    ]
    for log_file in logs:
        assert (REPO_ROOT / "provenance" / "audit_logs" / log_file).is_file(), f"Missing: {log_file}"


def _iter_repo_paths(pattern: str):
    """Yield paths under the repo root, excluding virtualenvs and caches."""
    skip_parts = {".venv", "venv", "env", ".git", "__pycache__", "node_modules"}
    for path in REPO_ROOT.rglob(pattern):
        if any(part in skip_parts for part in path.parts):
            continue
        yield path


def test_no_engine_present():
    """Paper 1 must NOT contain the governance engine."""
    for f in _iter_repo_paths("*engine*"):
        assert False, f"Engine file found (should not be present): {f}"


def test_no_benchmark_data():
    """Paper 1 must NOT contain Paper 4 benchmark data."""
    benchmark_dir = REPO_ROOT / "data" / "benchmark"
    assert not benchmark_dir.exists(), "benchmark/ directory should not exist in Paper 1"
