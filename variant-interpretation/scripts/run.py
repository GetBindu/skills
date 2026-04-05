#!/usr/bin/env python3
"""
ToolUniverse workflow: tooluniverse-variant-interpretation

CLI wrapper for the ACMG clinical variant interpretation agentic workflow
from https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-interpretation

NOTE: The pip-published `tooluniverse` package bundles ~214 OpenTargets/FDA/
Monarch tool clients but does NOT include the agentic skill workflows from
the upstream repo's `skills/` directory. To actually run this workflow, you
need either:

  1. A ToolUniverse checkout with skills loaded: clone the repo and set
     TOOLUNIVERSE_SKILLS_DIR to the skills/ path, OR
  2. A custom build that registers the workflow explicitly.

The script will:
  - Install check: report if tooluniverse is not installed
  - Workflow check: load ToolUniverse tools and verify the workflow exists
  - Fall back: if the workflow is missing, list available workflows and
    point at the upstream repo for the definition

Usage:
    python3 run.py --query "BRCA1 c.5266dupC in Ashkenazi Jewish patient"
    python3 run.py --query "TP53 R175H" --format summary
    python3 run.py --list-workflows
"""

import argparse
import json
import sys

WORKFLOW = "tooluniverse-variant-interpretation"
UPSTREAM_REPO = "https://github.com/mims-harvard/ToolUniverse"
UPSTREAM_SKILL = f"{UPSTREAM_REPO}/tree/main/skills/{WORKFLOW}"


def build_parser():
    parser = argparse.ArgumentParser(
        description=f"Run the ToolUniverse '{WORKFLOW}' clinical variant interpretation workflow.",
    )
    parser.add_argument("--query", "-q", help="Variant description, gene + variant, or clinical question")
    parser.add_argument(
        "--format",
        "-f",
        choices=["json", "summary"],
        default="json",
        help="Output format",
    )
    parser.add_argument("--no-cache", action="store_true", help="Disable result caching")
    parser.add_argument(
        "--list-workflows",
        action="store_true",
        help="List available ToolUniverse workflows and exit (no query required)",
    )
    return parser


def to_serializable(obj):
    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_serializable(v) for v in obj]
    try:
        json.dumps(obj)
        return obj
    except (TypeError, ValueError):
        return str(obj)


def load_tooluniverse():
    try:
        from tooluniverse import ToolUniverse
    except ImportError:
        return None, {
            "error": "tooluniverse is not installed",
            "install": "pip install tooluniverse",
            "upstream": UPSTREAM_REPO,
        }
    tu = ToolUniverse()
    tu.load_tools()
    return tu, None


def main():
    parser = build_parser()
    args = parser.parse_args()

    tu, err = load_tooluniverse()
    if err:
        print(json.dumps(err, indent=2), file=sys.stderr)
        sys.exit(1)

    available = list(tu.all_tool_dict.keys())

    if args.list_workflows:
        result = {
            "total_tools_loaded": len(available),
            "upstream_repo": UPSTREAM_REPO,
            "target_workflow": WORKFLOW,
            "target_workflow_available": WORKFLOW in available,
            "sample_tools": sorted(available)[:20],
        }
        print(json.dumps(result, indent=2))
        return

    if not args.query:
        parser.error("--query is required (or use --list-workflows)")

    if WORKFLOW not in available:
        result = {
            "error": f"Workflow '{WORKFLOW}' not available in current tooluniverse install",
            "reason": (
                "The pip-published tooluniverse package bundles data-source tool clients "
                "but not the agentic skill workflows from the upstream repo's skills/ directory."
            ),
            "upstream_skill_definition": UPSTREAM_SKILL,
            "workaround": (
                "Clone the upstream repo and load skills from skills/ directory, or wait for "
                "the skill workflow to be published to PyPI."
            ),
            "tools_loaded": len(available),
            "query": args.query,
        }
        print(json.dumps(result, indent=2))
        sys.exit(2)

    try:
        run_kwargs = {}
        try:
            import inspect

            if "use_cache" in inspect.signature(tu.run).parameters:
                run_kwargs["use_cache"] = not args.no_cache
        except Exception:
            pass
        result = tu.run(
            {"name": WORKFLOW, "arguments": {"query": args.query}},
            **run_kwargs,
        )
    except Exception as exc:
        error = {"error": str(exc), "workflow": WORKFLOW, "query": args.query}
        print(json.dumps(error, indent=2))
        sys.exit(1)

    safe = to_serializable(result)
    if args.format == "summary":
        text = safe if isinstance(safe, str) else json.dumps(safe, indent=2)
        print(text[:3000])
    else:
        print(json.dumps(safe, indent=2))


if __name__ == "__main__":
    main()
