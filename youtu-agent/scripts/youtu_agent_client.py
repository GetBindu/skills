#!/usr/bin/env python3
"""
youtu_agent bootstrapper.

Clones the TencentCloudADP/youtu-agent repo into ./upstream (if missing),
sets up its .venv with uv, and runs the specified CLI command.

Usage:
    # Bootstrap only (clone + install, no run)
    python youtu_agent_client.py --setup

    # Run CLI chat
    python youtu_agent_client.py --config simple/base
    python youtu_agent_client.py --config simple/base_search

    # Check status
    python youtu_agent_client.py --info

Environment variables required for actual agent execution:
    UTU_LLM_API_KEY     LLM provider key (DeepSeek, OpenAI, etc.)
    UTU_LLM_MODEL       e.g. deepseek-chat
    UTU_LLM_BASE_URL    e.g. https://api.deepseek.com/v1
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/TencentCloudADP/youtu-agent.git"
REPO_NAME = "youtu-agent"
PAPER_URL = "https://arxiv.org/abs/2512.24615"

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
UPSTREAM_DIR = SKILL_DIR / "upstream" / REPO_NAME


def have(cmd):
    return shutil.which(cmd) is not None


def check_environment():
    """Return status of required tools and env vars."""
    return {
        "python": sys.version.split()[0],
        "git": have("git"),
        "uv": have("uv"),
        "upstream_cloned": UPSTREAM_DIR.exists(),
        "upstream_venv": (UPSTREAM_DIR / ".venv").exists() if UPSTREAM_DIR.exists() else False,
        "env_vars": {
            "UTU_LLM_API_KEY": bool(os.environ.get("UTU_LLM_API_KEY")),
            "UTU_LLM_MODEL": os.environ.get("UTU_LLM_MODEL", "not set"),
            "UTU_LLM_BASE_URL": os.environ.get("UTU_LLM_BASE_URL", "not set"),
            "SERPER_API_KEY": bool(os.environ.get("SERPER_API_KEY")),
            "JINA_API_KEY": bool(os.environ.get("JINA_API_KEY")),
        },
    }


def clone_repo():
    """Clone the upstream repo if it doesn't exist."""
    if UPSTREAM_DIR.exists():
        return {"status": "already_cloned", "path": str(UPSTREAM_DIR)}

    if not have("git"):
        return {"status": "error", "message": "git not found in PATH"}

    UPSTREAM_DIR.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["git", "clone", "--depth=1", REPO_URL, str(UPSTREAM_DIR)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {"status": "error", "message": result.stderr.strip()}

    return {"status": "cloned", "path": str(UPSTREAM_DIR)}


def install_deps():
    """Run uv sync in the upstream repo."""
    if not UPSTREAM_DIR.exists():
        return {"status": "error", "message": "Repo not cloned yet. Run --setup first."}

    if not have("uv"):
        return {"status": "error", "message": "uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh"}

    result = subprocess.run(
        ["uv", "sync"],
        cwd=str(UPSTREAM_DIR),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {"status": "error", "message": result.stderr.strip()[-500:]}

    return {"status": "installed", "path": str(UPSTREAM_DIR / ".venv")}


def run_cli(config):
    """Run the youtu-agent cli_chat.py with given config."""
    cli_script = UPSTREAM_DIR / "scripts" / "cli_chat.py"
    if not cli_script.exists():
        return {"status": "error", "message": f"cli_chat.py not found at {cli_script}. Run --setup first."}

    if not os.environ.get("UTU_LLM_API_KEY"):
        return {
            "status": "error",
            "message": "UTU_LLM_API_KEY env var not set. Required to run the agent.",
            "hint": "export UTU_LLM_API_KEY=sk-... UTU_LLM_MODEL=deepseek-chat UTU_LLM_BASE_URL=https://api.deepseek.com/v1",
        }

    venv_python = UPSTREAM_DIR / ".venv" / "bin" / "python"
    python = str(venv_python) if venv_python.exists() else sys.executable

    try:
        subprocess.run(
            [python, str(cli_script), "--config", config],
            cwd=str(UPSTREAM_DIR),
        )
        return {"status": "ok"}
    except KeyboardInterrupt:
        return {"status": "interrupted"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def main():
    parser = argparse.ArgumentParser(description="youtu_agent bootstrapper & runner")
    parser.add_argument("--setup", action="store_true", help="Clone repo and install dependencies")
    parser.add_argument("--info", action="store_true", help="Show environment and setup status")
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Agent config to run (e.g., 'simple/base', 'simple/base_search')",
    )
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    result = {
        "skill": "youtu_agent",
        "repository": REPO_URL,
        "paper": PAPER_URL,
    }

    if args.info or (not args.setup and not args.config):
        result["environment"] = check_environment()
        result["next_steps"] = []
        env = result["environment"]
        if not env["upstream_cloned"] or not env["upstream_venv"]:
            result["next_steps"].append("Run: python youtu_agent_client.py --setup")
        elif not env["env_vars"]["UTU_LLM_API_KEY"]:
            result["next_steps"].append("Set UTU_LLM_API_KEY, UTU_LLM_MODEL, UTU_LLM_BASE_URL env vars")
        else:
            result["next_steps"].append("Run: python youtu_agent_client.py --config simple/base")

    elif args.setup:
        result["clone"] = clone_repo()
        if result["clone"]["status"] in ("cloned", "already_cloned"):
            result["install"] = install_deps()

    elif args.config:
        if not UPSTREAM_DIR.exists():
            result["bootstrap"] = clone_repo()
            if result["bootstrap"]["status"] in ("cloned", "already_cloned"):
                result["install"] = install_deps()
        result["run"] = run_cli(args.config)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"youtu_agent — {REPO_URL}")
        for k, v in result.items():
            if k == "skill":
                continue
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
