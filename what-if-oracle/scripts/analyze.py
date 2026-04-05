#!/usr/bin/env python3
"""
What-If Oracle — Structured Scenario Analysis Generator

Takes a speculative question and generates a structured multi-branch
scenario analysis using the 0·IF·1 framework.

Usage:
    python analyze.py --question "What if oil prices double in 6 months?"
    python analyze.py --question "What if our competitor launches first?" --mode deep
    python analyze.py --question "What if interest rates hit 8%?" --format json
"""

import argparse
import json

SCENARIO_BRANCHES = {
    "best_case": {"symbol": "Ω", "label": "Best Case", "desc": "Maximum upside scenario"},
    "likely_case": {"symbol": "α", "label": "Likely Case", "desc": "Most probable path"},
    "worst_case": {"symbol": "Δ", "label": "Worst Case", "desc": "Maximum downside scenario"},
    "wild_card": {"symbol": "Ψ", "label": "Wild Card", "desc": "Black swan territory"},
    "contrarian": {"symbol": "Φ", "label": "Contrarian", "desc": "Opposite of consensus"},
    "second_order": {"symbol": "∞", "label": "Second Order", "desc": "Cascading ripple effects"},
}

MODES = {
    "quick": {
        "branches": ["best_case", "likely_case", "worst_case"],
        "description": "3-branch fast analysis",
    },
    "deep": {
        "branches": list(SCENARIO_BRANCHES.keys()),
        "description": "Full 6-branch comprehensive analysis",
    },
    "reverse": {
        "branches": ["likely_case", "best_case", "contrarian"],
        "description": "Backward mapping from desired outcome",
    },
}


def decompose_question(question: str) -> dict:
    """Phase 1: Frame — decompose the what-if into structured components."""
    return {
        "original_question": question,
        "variable": "[Identify the key variable being changed]",
        "magnitude": "[Quantify the change if possible]",
        "timeframe": "[Extract or estimate timeframe]",
        "context": "[Relevant background context]",
        "refined_question": f"Refined: {question}",
        "note": "An LLM agent should fill in these fields by analyzing the question.",
    }


def generate_branch_template(branch_key: str) -> dict:
    """Generate a template for one scenario branch."""
    branch = SCENARIO_BRANCHES[branch_key]
    return {
        "symbol": branch["symbol"],
        "label": branch["label"],
        "description": branch["desc"],
        "probability": "[Estimate 0-100%]",
        "narrative": "[Describe what happens in this scenario]",
        "key_assumptions": ["[Assumption 1]", "[Assumption 2]"],
        "trigger_conditions": ["[What would make this scenario occur]"],
        "consequences_timeline": {
            "immediate": "[0-30 days]",
            "short_term": "[1-6 months]",
            "long_term": "[6-24 months]",
        },
        "required_responses": ["[Action to take if this scenario emerges]"],
        "overlooked_insight": "[The thing most people would miss]",
    }


def generate_analysis(question: str, mode: str = "quick") -> dict:
    """Generate the full scenario analysis structure."""
    mode_config = MODES.get(mode, MODES["quick"])

    analysis = {
        "framework": "0·IF·1",
        "mode": mode,
        "mode_description": mode_config["description"],
        "phase_1_frame": decompose_question(question),
        "phase_2_map": {"branches": {key: generate_branch_template(key) for key in mode_config["branches"]}},
        "phase_3_analyze": {
            "note": "Each branch above contains analysis fields to be filled by an LLM agent.",
            "golden_ratio": "Allocate 61.8% attention to primary scenario, 38.2% to alternatives.",
        },
        "phase_4_synthesize": {
            "probability_distribution": "[Summarize probabilities across branches]",
            "robust_actions": ["[Actions that work across multiple scenarios]"],
            "decision_triggers": ["[Observable signals that indicate which scenario is emerging]"],
            "one_percent_insight": "[The insight most analysis overlooks]",
        },
    }
    return analysis


def main():
    parser = argparse.ArgumentParser(description="What-If Oracle — Structured Scenario Analysis")
    parser.add_argument(
        "--question", "-q", required=True, help='The what-if question to analyze (e.g., "What if oil prices double?")'
    )
    parser.add_argument(
        "--mode",
        "-m",
        default="quick",
        choices=["quick", "deep", "reverse"],
        help="Analysis mode: quick (3 branches), deep (6 branches), reverse (backward mapping)",
    )
    parser.add_argument(
        "--format", "-f", default="json", choices=["json", "summary"], help="Output format (default: json)"
    )
    args = parser.parse_args()

    result = generate_analysis(args.question, args.mode)

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"{'=' * 70}")
        print(f"WHAT-IF ORACLE — {args.mode.upper()} MODE")
        print(f"{'=' * 70}")
        print(f"Question: {args.question}")
        print("Framework: 0·IF·1")
        print(f"Branches: {len(result['phase_2_map']['branches'])}")
        print()
        for key, branch in result["phase_2_map"]["branches"].items():
            print(f"  {branch['symbol']} {branch['label']}: {branch['description']}")
        print()
        print("Run with --format json for full structured template.")
        print("Feed the JSON to an LLM agent to fill in the analysis fields.")


if __name__ == "__main__":
    main()
