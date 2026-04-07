#!/usr/bin/env python3
"""
SolubleMPNN — Solubility-optimized protein sequence design.

Reports environment status and provides setup instructions.
The actual model runs require cloning the upstream LigandMPNN repo.

Usage:
    python info.py --help
    python info.py --info
    python info.py --check-deps
"""

import argparse
import json
import shutil
import sys

UPSTREAM_REPO = "https://github.com/dauparas/LigandMPNN"


def check_environment():
    """Check if required tools and dependencies are available."""
    checks = {
        "python": sys.version.split()[0],
        "git": shutil.which("git") is not None,
        "conda": shutil.which("conda") is not None,
    }

    # Check for key Python packages
    for pkg in ["torch", "numpy", "prody"]:
        try:
            __import__(pkg)
            checks[pkg] = True
        except ImportError:
            checks[pkg] = False

    return checks


def main():
    parser = argparse.ArgumentParser(
        description="SolubleMPNN — solubility-optimized protein sequence design",
    )
    parser.add_argument("--info", action="store_true", help="Show skill info and setup instructions")
    parser.add_argument("--check-deps", action="store_true", help="Check required dependencies")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="summary")
    args = parser.parse_args()

    if args.check_deps:
        checks = check_environment()
        if args.format == "json":
            print(json.dumps(checks, indent=2))
        else:
            print("SolubleMPNN Dependency Check")
            print("=" * 40)
            for k, v in checks.items():
                status = "✓" if v and v is not True else ("✓ " + str(v) if v else "✗")
                print(f"  {k:<15} {status}")
            if not checks.get("torch"):
                print("\n  PyTorch required. Install: conda install pytorch -c pytorch")
            if not checks.get("prody"):
                print("  ProDy required. Install: pip install prody")
        return

    # Default: show info
    info = {
        "skill": "solublempnn",
        "upstream_repo": UPSTREAM_REPO,
        "description": "Solubility-optimized protein sequence design using SolubleMPNN (ProteinMPNN variant from LigandMPNN)",
        "requires": {
            "gpu": "NVIDIA GPU with CUDA (recommended for production; CPU works for small designs)",
            "software": ["git", "conda or pip", "Python 3.9+", "PyTorch", "NumPy", "ProDy"],
        },
        "setup_steps": [
            f"git clone {UPSTREAM_REPO}.git",
            "cd LigandMPNN",
            "conda create -n solublempnn python=3.9 pytorch -c pytorch",
            "conda activate solublempnn",
            "pip install prody numpy",
            "bash get_model_params.sh",
        ],
        "run_example": "python run.py --model_type soluble_mpnn --pdb_path input.pdb --out_folder output/",
    }

    if args.format == "json":
        print(json.dumps(info, indent=2))
    else:
        print("SolubleMPNN — Solubility-Optimized Protein Sequence Design")
        print("=" * 60)
        print(f"  Upstream: {info['upstream_repo']}")
        print(f"  GPU: {info['requires']['gpu']}")
        print()
        print("  Setup:")
        for i, step in enumerate(info["setup_steps"], 1):
            print(f"    {i}. {step}")
        print()
        print(f"  Run: {info['run_example']}")


if __name__ == "__main__":
    main()
