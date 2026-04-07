#!/usr/bin/env python3
"""
IUCN Red List Database Query Script

Query species conservation status from IUCN Red List of Threatened Species.

Usage:
    python query.py --species "Bombus affinis"
    python query.py --category "CR" --region "North America"
"""

import argparse
import json
import os
import sys
from typing import Dict, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

IUCN_API = "https://apiv3.iucnredlist.org/api/v3"


def query_iucn(
    species_name: Optional[str] = None,
    category: Optional[str] = None,
    region: Optional[str] = None,
    api_key: Optional[str] = None,
) -> Dict:
    """
    Query IUCN Red List API.

    Args:
        species_name: Species scientific name
        category: Conservation category (CR, EN, VU, NT, LC, DD)
        region: Geographic region
        api_key: IUCN API key (or set IUCN_API_KEY env var)

    Returns:
        Dictionary with species conservation data
    """
    if not api_key:
        api_key = os.environ.get("IUCN_API_KEY")

    if not api_key:
        raise ValueError("IUCN API key required. Set IUCN_API_KEY environment variable or pass --api-key")

    params = {"token": api_key}

    try:
        if species_name:
            # Search for specific species
            search_url = f"{IUCN_API}/species/{species_name}"
            response = requests.get(search_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            if data.get("result"):
                species_data = data["result"][0]
                return {
                    "query": species_name,
                    "species": {
                        "scientific_name": species_data.get("scientific_name", ""),
                        "category": species_data.get("category", ""),
                        "population_trend": species_data.get("population_trend", ""),
                        "main_common_name": species_data.get("main_common_name", ""),
                        "kingdom": species_data.get("kingdom_name", ""),
                        "phylum": species_data.get("phylum_name", ""),
                        "class": species_data.get("class_name", ""),
                        "order": species_data.get("order_name", ""),
                        "family": species_data.get("family_name", ""),
                    },
                    "source": "IUCN Red List of Threatened Species",
                }
            else:
                return {"query": species_name, "error": "Species not found"}

        else:
            # List species by category
            return {
                "note": "Category-based search requires additional implementation",
                "category": category,
                "region": region,
                "source": "IUCN Red List of Threatened Species",
            }

    except requests.RequestException as e:
        print(f"Error querying IUCN API: {e}", file=sys.stderr)
        return {"error": str(e)}


def format_summary(result: Dict) -> str:
    """Format IUCN data as summary."""
    if "error" in result:
        return f"Error: {result['error']}"

    if "note" in result:
        return f"\n{result['note']}"

    lines = ["\nIUCN Red List Assessment"]
    lines.append(f"Species: {result['query']}\n")
    lines.append("-" * 80)

    if "species" in result:
        sp = result["species"]
        lines.append(f"\nScientific Name: {sp['scientific_name']}")
        if sp.get("main_common_name"):
            lines.append(f"Common Name: {sp['main_common_name']}")
        lines.append(f"\nConservation Status: {sp['category']}")
        lines.append(f"Population Trend: {sp['population_trend']}")
        lines.append("\nTaxonomy:")
        lines.append(f"  Kingdom: {sp.get('kingdom', '')}")
        lines.append(f"  Phylum: {sp.get('phylum', '')}")
        lines.append(f"  Class: {sp.get('class', '')}")
        lines.append(f"  Order: {sp.get('order', '')}")
        lines.append(f"  Family: {sp.get('family', '')}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query IUCN Red List database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --species "Bombus affinis"
  %(prog)s --species "Panthera tigris"
  %(prog)s --category "CR" --region "North America"
  
Conservation Categories:
  CR - Critically Endangered
  EN - Endangered
  VU - Vulnerable
  NT - Near Threatened
  LC - Least Concern
  DD - Data Deficient
        """,
    )

    parser.add_argument("--species", "-s", help="Species scientific name")
    parser.add_argument("--category", "-c", choices=["CR", "EN", "VU", "NT", "LC", "DD"], help="Conservation category")
    parser.add_argument("--region", "-r", help="Geographic region")
    parser.add_argument("--api-key", "-k", help="IUCN API key (or set IUCN_API_KEY env var)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        result = query_iucn(species_name=args.species, category=args.category, region=args.region, api_key=args.api_key)

        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(result))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
