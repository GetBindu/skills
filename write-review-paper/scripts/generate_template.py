#!/usr/bin/env python3
"""
Literature Review Writing — Template Generator

Generates structured templates for literature review papers, including
reading plans, comparison matrices, and writing outlines.

Usage:
    python generate_template.py --type reading-plan --papers 20
    python generate_template.py --type comparison-matrix --topic "CRISPR delivery"
    python generate_template.py --type writing-outline --format survey
    python generate_template.py --type all --topic "protein folding" --output-dir ./review
"""

import argparse
import json
import os


def reading_plan_template(num_papers: int = 20) -> dict:
    """Phase 1: Generate a reading plan with paper triage template."""
    return {
        "phase": "1_reading_strategy",
        "triage_levels": {
            "P1_must_read": {
                "count": max(1, num_papers // 4),
                "criteria": "Foundational papers, highly cited, directly relevant",
                "action": "Full read with detailed notes",
            },
            "P2_should_read": {
                "count": max(1, num_papers // 2),
                "criteria": "Important context, methodological contributions",
                "action": "Abstract + key sections + notes",
            },
            "P3_skim": {
                "count": max(1, num_papers // 4),
                "criteria": "Peripheral relevance, background context",
                "action": "Abstract + conclusions only",
            },
        },
        "note_template": {
            "paper_id": "[BibTeX key]",
            "title": "",
            "authors_year": "",
            "main_contribution": "",
            "methodology": "",
            "key_findings": [],
            "limitations": "",
            "relevance_to_review": "",
            "connections_to_other_papers": [],
        },
        "total_papers": num_papers,
    }


def comparison_matrix_template(topic: str) -> dict:
    """Phase 2: Generate a comparison matrix template."""
    return {
        "phase": "2_synthesis",
        "topic": topic,
        "comparison_dimensions": [
            "Method/Approach",
            "Dataset/Scale",
            "Key Results",
            "Strengths",
            "Limitations",
            "Year",
        ],
        "matrix": [
            {
                "paper": "[Paper 1]",
                "values": {
                    d: ""
                    for d in ["Method/Approach", "Dataset/Scale", "Key Results", "Strengths", "Limitations", "Year"]
                },
            },
            {
                "paper": "[Paper 2]",
                "values": {
                    d: ""
                    for d in ["Method/Approach", "Dataset/Scale", "Key Results", "Strengths", "Limitations", "Year"]
                },
            },
        ],
        "timeline_analysis": {
            "note": "Track how the field evolved over time",
            "periods": [
                {"era": "Early Work", "years": "[Start-Year]", "key_developments": []},
                {"era": "Current State", "years": "[Current]", "key_developments": []},
            ],
        },
        "taxonomy": {
            "note": "Categorize approaches by multiple dimensions",
            "dimension_1": {"name": "[e.g., Method Type]", "categories": []},
            "dimension_2": {"name": "[e.g., Application Domain]", "categories": []},
        },
    }


def writing_outline_template(fmt: str = "survey") -> dict:
    """Phase 3: Generate a writing structure template."""
    if fmt == "survey":
        return {
            "phase": "3_writing",
            "format": "survey_paper",
            "sections": [
                {"name": "Abstract", "target_words": 250, "citation_density": "2-5"},
                {"name": "Introduction", "target_words": 1500, "citation_density": "10-20"},
                {"name": "Background & Problem Definition", "target_words": 1000, "citation_density": "10-15"},
                {"name": "Taxonomy / Classification", "target_words": 2000, "citation_density": "20-30"},
                {"name": "Detailed Analysis", "target_words": 4000, "citation_density": "30-50"},
                {"name": "Comparison & Discussion", "target_words": 1500, "citation_density": "10-20"},
                {"name": "Open Problems & Future Directions", "target_words": 1000, "citation_density": "5-10"},
                {"name": "Conclusion", "target_words": 500, "citation_density": "3-5"},
            ],
        }
    else:
        return {
            "phase": "3_writing",
            "format": "thesis_chapter",
            "sections": [
                {"name": "Introduction to Topic", "target_words": 1000},
                {"name": "Literature Review", "target_words": 5000, "citation_density": "50-100+"},
                {"name": "Critical Analysis", "target_words": 2000},
                {"name": "Research Gaps", "target_words": 1000},
                {"name": "Summary", "target_words": 500},
            ],
        }


def main():
    parser = argparse.ArgumentParser(description="Literature Review Template Generator")
    parser.add_argument(
        "--type",
        "-t",
        required=True,
        choices=["reading-plan", "comparison-matrix", "writing-outline", "all"],
        help="Template type to generate",
    )
    parser.add_argument("--topic", default="[Your Topic]", help="Research topic")
    parser.add_argument("--papers", type=int, default=20, help="Number of papers (for reading plan)")
    parser.add_argument("--format", "-f", default="survey", choices=["survey", "thesis"])
    parser.add_argument("--output-dir", help="Directory to save templates (optional)")
    args = parser.parse_args()

    templates = {}
    if args.type in ("reading-plan", "all"):
        templates["reading_plan"] = reading_plan_template(args.papers)
    if args.type in ("comparison-matrix", "all"):
        templates["comparison_matrix"] = comparison_matrix_template(args.topic)
    if args.type in ("writing-outline", "all"):
        templates["writing_outline"] = writing_outline_template(args.format)

    result = {"topic": args.topic, "templates": templates}

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        for name, tmpl in templates.items():
            path = os.path.join(args.output_dir, f"{name}.json")
            with open(path, "w") as f:
                json.dump(tmpl, f, indent=2)
            print(f"Saved: {path}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
