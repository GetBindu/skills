#!/usr/bin/env python3
"""
EPA CompTox Dashboard Query Script

Query chemical toxicity data from EPA CompTox Chemicals Dashboard.

Usage:
    python query.py --chemical "glyphosate" --data-type toxicity
    python query.py --chemical "atrazine" --format json
"""

import argparse
import json
import sys
from typing import Dict, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

COMPTOX_API = "https://comptox.epa.gov/dashboard-api"


def query_comptox(chemical_identifier: str, data_type: Optional[str] = None) -> Dict:
    """
    Query EPA CompTox Dashboard API.

    Args:
        chemical_identifier: Chemical name, CAS number, or DTXSID
        data_type: Type of data ('toxicity', 'properties', 'bioactivity')

    Returns:
        Dictionary with chemical data
    """
    # Search for chemical by name first
    search_url = f"{COMPTOX_API}/chemical/search/by-name/{chemical_identifier}"

    try:
        response = requests.get(search_url, timeout=30)
        response.raise_for_status()
        search_data = response.json()

        if not search_data:
            return {"query": chemical_identifier, "error": "Chemical not found", "total": 0}

        # Get first match
        dtxsid = search_data[0].get("dtxsid")

        # Fetch detailed data
        detail_url = f"{COMPTOX_API}/chemical/detail/search/by-dtxsid/{dtxsid}"
        detail_response = requests.get(detail_url, timeout=30)
        detail_response.raise_for_status()
        detail_data = detail_response.json()

        chemical_data = {
            "query": chemical_identifier,
            "dtxsid": dtxsid,
            "preferred_name": detail_data.get("preferredName", ""),
            "cas_rn": detail_data.get("casrn", ""),
            "molecular_formula": detail_data.get("molecularFormula", ""),
            "molecular_weight": detail_data.get("molecularWeight", ""),
            "smiles": detail_data.get("smiles", ""),
            "source": "EPA CompTox Dashboard",
        }

        # Add toxicity data if requested
        if not data_type or data_type == "toxicity":
            tox_url = f"{COMPTOX_API}/chemical/toxicity/search/by-dtxsid/{dtxsid}"
            try:
                tox_response = requests.get(tox_url, timeout=30)
                if tox_response.status_code == 200:
                    chemical_data["toxicity"] = tox_response.json()
            except Exception:
                chemical_data["toxicity"] = "Not available"

        return chemical_data

    except requests.RequestException as e:
        print(f"Error querying CompTox API: {e}", file=sys.stderr)
        return {"query": chemical_identifier, "error": str(e)}


def format_summary(chemical_data: Dict) -> str:
    """Format chemical data as summary."""
    if "error" in chemical_data:
        return f"Error: {chemical_data['error']}"

    lines = [f"\nEPA CompTox Data for: {chemical_data['query']}\n"]
    lines.append("-" * 80)
    lines.append(f"\nPreferred Name: {chemical_data.get('preferred_name', 'N/A')}")
    lines.append(f"DTXSID: {chemical_data.get('dtxsid', 'N/A')}")
    lines.append(f"CAS RN: {chemical_data.get('cas_rn', 'N/A')}")
    lines.append(f"Molecular Formula: {chemical_data.get('molecular_formula', 'N/A')}")
    lines.append(f"Molecular Weight: {chemical_data.get('molecular_weight', 'N/A')}")

    if "toxicity" in chemical_data:
        lines.append("\nToxicity Data: Available")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query EPA CompTox Chemicals Dashboard",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --chemical "glyphosate" --data-type toxicity
  %(prog)s --chemical "atrazine" --format json
  %(prog)s --chemical "2,4-D"
        """,
    )

    parser.add_argument("--chemical", "-c", required=True, help="Chemical name, CAS number, or DTXSID")
    parser.add_argument(
        "--data-type", "-d", choices=["toxicity", "properties", "bioactivity"], help="Type of data to retrieve"
    )
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        chemical_data = query_comptox(chemical_identifier=args.chemical, data_type=args.data_type)

        if args.format == "json":
            print(json.dumps(chemical_data, indent=2))
        else:
            print(format_summary(chemical_data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
