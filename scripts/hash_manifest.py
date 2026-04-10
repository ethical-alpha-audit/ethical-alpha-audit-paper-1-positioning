"""
SHA-256 manifest generator for the Paper 1 reproducibility harness.
Adapted from the Deterministic Notebook Execution Harness (I2).

Generates MANIFEST.sha256 covering all source and output files.
"""

import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

# Directories to hash (relative to repo root)
HASH_DIRS = [
    "manuscript",
    "figures",
    "supplementary",
    "data",
    "config",
    "provenance",
    "docs",
    "outputs",
]

# Individual root files to hash
HASH_ROOT_FILES = [
    "reproduce_all.py",
    "requirements.txt",
    "environment.yml",
    "environment.lock",
    "runtime.txt",
    "VERSION",
]

SKIP_EXTENSIONS = {".pyc"}
SKIP_DIRS = {"__pycache__", ".ipynb_checkpoints"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_files():
    """Collect all files to hash, sorted lexicographically."""
    files = []

    for dir_name in HASH_DIRS:
        dir_path = BASE_DIR / dir_name
        if dir_path.exists():
            for fpath in sorted(dir_path.rglob("*")):
                if fpath.is_file() and fpath.suffix not in SKIP_EXTENSIONS:
                    if not any(part in SKIP_DIRS for part in fpath.parts):
                        files.append(fpath)

    for fname in HASH_ROOT_FILES:
        fpath = BASE_DIR / fname
        if fpath.exists():
            files.append(fpath)

    return sorted(files, key=lambda p: str(p.relative_to(BASE_DIR)))


def build_manifest():
    """Generate MANIFEST.sha256."""
    files = collect_files()
    lines = []
    for fpath in files:
        rel = fpath.relative_to(BASE_DIR)
        digest = sha256_file(fpath)
        lines.append(f"{digest}  {rel}")

    manifest_path = BASE_DIR / "MANIFEST.sha256"
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  MANIFEST.sha256: {len(lines)} files hashed")
    return manifest_path


if __name__ == "__main__":
    build_manifest()
