#!/usr/bin/env python3
"""
ToolUniverse workflow: tooluniverse-sequence-retrieval

CLI wrapper for the biological sequence retrieval agentic workflow.
See: https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-sequence-retrieval

Usage:
    python3 run.py --query "Retrieve BRCA1 mRNA sequence from NCBI"
    python3 run.py --list-workflows
"""

import argparse
import json
import sys

WORKFLOW = "tooluniverse-sequence-retrieval"
UPSTREAM_REPO = "https://github.com/mims-harvard/ToolUniverse"
UPSTREAM_SKILL = f"{UPSTREAM_REPO}/tree/main/skills/{WORKFLOW}"


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
            "install": "pip install tooluniverse pyyaml",
            "upstream": UPSTREAM_REPO,
        }
    tu = ToolUniverse()
    tu.load_tools()
    return tu, None


def main():
    parser = argparse.ArgumentParser(
        description=f"Run the ToolUniverse '{WORKFLOW}' sequence retrieval workflow.",
    )
    parser.add_argument("--query", "-q", help="Sequence retrieval query")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json", help="Output format")
    parser.add_argument("--no-cache", action="store_true", help="Disable result caching")
    parser.add_argument("--list-workflows", action="store_true", help="List available workflows and exit")
    args = parser.parse_args()

    tu, err = load_tooluniverse()
    if err:
        print(json.dumps(err, indent=2), file=sys.stderr)
        sys.exit(1)

    available = list(tu.all_tool_dict.keys())

    if args.list_workflows:
        print(
            json.dumps(
                {
                    "total_tools_loaded": len(available),
                    "upstream_repo": UPSTREAM_REPO,
                    "target_workflow": WORKFLOW,
                    "target_workflow_available": WORKFLOW in available,
                    "sample_tools": sorted(available)[:20],
                },
                indent=2,
            )
        )
        return

    if not args.query:
        parser.error("--query is required (or use --list-workflows)")

    if WORKFLOW not in available:
        print(
            json.dumps(
                {
                    "error": f"Workflow '{WORKFLOW}' not available in current tooluniverse install",
                    "reason": "The pip-published tooluniverse package bundles data-source tool clients but not the agentic skill workflows.",
                    "upstream_skill_definition": UPSTREAM_SKILL,
                    "workaround": "Clone the upstream repo and load skills from skills/ directory.",
                    "tools_loaded": len(available),
                    "query": args.query,
                },
                indent=2,
            )
        )
        sys.exit(2)

    try:
        run_kwargs = {}
        try:
            import inspect

            if "use_cache" in inspect.signature(tu.run).parameters:
                run_kwargs["use_cache"] = not args.no_cache
        except Exception:
            pass
        result = tu.run({"name": WORKFLOW, "arguments": {"query": args.query}}, **run_kwargs)
    except Exception as exc:
        print(json.dumps({"error": str(exc), "workflow": WORKFLOW, "query": args.query}, indent=2))
        sys.exit(1)

    safe = to_serializable(result)
    if args.format == "summary":
        text = safe if isinstance(safe, str) else json.dumps(safe, indent=2)
        print(text[:3000])
    else:
        print(json.dumps(safe, indent=2))


if __name__ == "__main__":
    main()
