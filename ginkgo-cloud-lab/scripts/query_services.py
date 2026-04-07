#!/usr/bin/env python3
"""
Ginkgo Cloud Lab — Service Query Tool

Lists available Ginkgo Cloud Lab services with pricing, turnaround, and
requirements. Can also generate a protocol submission template.

Usage:
    python query_services.py --list
    python query_services.py --service "protein-expression"
    python query_services.py --template --service "protein-expression" --format json
"""

import argparse
import json

SERVICES = {
    "protein-expression-validation": {
        "name": "Cell-Free Protein Expression Validation",
        "price_per_sample": "$39",
        "turnaround_days": "5-10",
        "description": "Screens protein sequences (up to 1800 bp) for expression feasibility using cell-free systems.",
        "max_sequence_length_bp": 1800,
        "input_format": "FASTA or CSV with protein/DNA sequences",
        "url": "https://cloud.ginkgo.bio",
    },
    "protein-expression-optimization": {
        "name": "Cell-Free Protein Expression Optimization",
        "price_per_sample": "$199",
        "turnaround_days": "6-11",
        "description": "Uses Design of Experiments across up to 24 conditions for challenging proteins.",
        "max_conditions": 24,
        "input_format": "FASTA or CSV with protein/DNA sequences",
        "url": "https://cloud.ginkgo.bio",
    },
    "pixel-art": {
        "name": "Fluorescent Pixel Art Generation (Beta)",
        "price_per_plate": "$25",
        "turnaround_days": "5-7",
        "description": "Converts digital images into bacterial artwork using up to 11 E. coli strains.",
        "max_strains": 11,
        "input_format": "PNG/JPG image",
        "url": "https://cloud.ginkgo.bio",
    },
}


def generate_submission_template(service_key: str) -> dict:
    """Generate a protocol submission template for a service."""
    service = SERVICES.get(service_key)
    if not service:
        return {"error": f"Unknown service: {service_key}", "available": list(SERVICES.keys())}

    return {
        "service": service["name"],
        "submission_template": {
            "project_name": "[Your project name]",
            "sequences": [{"id": "seq_001", "sequence": "[DNA or protein sequence]", "name": "[Optional name]"}],
            "parameters": {
                "note": "Configure based on service requirements",
            },
            "contact_email": "[Your email]",
        },
        "pricing": service.get("price_per_sample", service.get("price_per_plate", "Contact")),
        "turnaround": service["turnaround_days"] + " days",
        "submit_at": service["url"],
        "auth_contact": "cloud@ginkgo.bio",
    }


def main():
    parser = argparse.ArgumentParser(description="Ginkgo Cloud Lab Service Query")
    parser.add_argument("--list", action="store_true", help="List all available services")
    parser.add_argument("--service", "-s", help="Service key to query or get template for")
    parser.add_argument("--template", "-t", action="store_true", help="Generate submission template")
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    if args.list or (not args.service and not args.template):
        result = {"services": SERVICES, "platform_url": "https://cloud.ginkgo.bio"}
    elif args.template and args.service:
        result = generate_submission_template(args.service)
    elif args.service:
        svc = SERVICES.get(args.service)
        if svc:
            result = svc
        else:
            result = {"error": f"Unknown service '{args.service}'", "available": list(SERVICES.keys())}
    else:
        result = {"error": "Provide --list, --service, or --template --service"}

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        if "services" in result:
            print("Ginkgo Cloud Lab — Available Services")
            print("=" * 50)
            for key, svc in result["services"].items():
                price = svc.get("price_per_sample", svc.get("price_per_plate", "N/A"))
                print(f"\n  [{key}]")
                print(f"  {svc['name']}")
                print(f"  Price: {price} | Turnaround: {svc['turnaround_days']} days")
            print("\nPlatform: https://cloud.ginkgo.bio")
        else:
            print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
