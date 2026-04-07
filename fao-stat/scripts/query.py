#!/usr/bin/env python3
"""
FAO STAT Global Agriculture Database Query Script

Query global food and agriculture statistics from UN FAO.

Usage:
    python query.py --domain "Production" --country "India" --item "Wheat" --element "Production"
    python query.py --domain "Trade" --country "Brazil" --item "Soybeans" --year-start 2020 --year-end 2023
"""

import argparse
import json
import sys
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

FAOSTAT_API = "https://fenixservices.fao.org/faostat/api/v1/en/data"


def query_faostat(
    domain: str,
    country: str,
    item: str,
    element: Optional[str] = None,
    year_start: Optional[int] = None,
    year_end: Optional[int] = None,
) -> List[Dict]:
    """
    Query FAO STAT API.

    Args:
        domain: Data domain (e.g., 'Production', 'Trade', 'Prices')
        country: Country name or ISO code
        item: Commodity or item name
        element: Data element (e.g., 'Production', 'Yield', 'Area harvested')
        year_start: Start year (optional)
        year_end: End year (optional)

    Returns:
        List of data dictionaries
    """
    # Build query parameters
    params = {"domain_code": domain, "area": country, "item": item}

    if element:
        params["element"] = element

    if year_start and year_end:
        params["year"] = f"{year_start}:{year_end}"
    elif year_start:
        params["year"] = year_start

    try:
        response = requests.get(FAOSTAT_API, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "data" not in data:
            return []

        # Parse and format results
        results = []
        for record in data["data"]:
            results.append(
                {
                    "country": record.get("Area", ""),
                    "item": record.get("Item", ""),
                    "element": record.get("Element", ""),
                    "year": record.get("Year", ""),
                    "value": record.get("Value", ""),
                    "unit": record.get("Unit", ""),
                    "flag": record.get("Flag", ""),
                    "source": "FAO STAT",
                }
            )

        return results

    except requests.RequestException as e:
        print(f"Error querying FAO STAT API: {e}", file=sys.stderr)
        return []


def format_summary(data: List[Dict]) -> str:
    """Format data as summary."""
    if not data:
        return "No data found."

    lines = [f"\nFound {len(data)} records:\n"]
    lines.append("-" * 80)

    for i, record in enumerate(data[:10], 1):
        lines.append(f"\n{i}. {record['country']} - {record['item']}")
        lines.append(f"   {record['element']}: {record['value']} {record['unit']}")
        lines.append(f"   Year: {record['year']}")

    if len(data) > 10:
        lines.append(f"\n... and {len(data) - 10} more records")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query FAO STAT global agriculture database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --domain "Production" --country "India" --item "Wheat" --element "Production"
  %(prog)s --domain "Trade" --country "Brazil" --item "Soybeans" --year-start 2020 --year-end 2023
  %(prog)s --domain "Prices" --country "United States" --item "Maize"
        """,
    )

    parser.add_argument(
        "--domain", "-d", required=True, help="Data domain (e.g., Production, Trade, Prices, Food Balance)"
    )
    parser.add_argument("--country", "-c", required=True, help="Country name or ISO code")
    parser.add_argument("--item", "-i", required=True, help="Commodity or item name (e.g., Wheat, Rice, Cattle)")
    parser.add_argument("--element", "-e", help="Data element (e.g., Production, Yield, Area harvested)")
    parser.add_argument("--year-start", type=int, help="Start year for time series")
    parser.add_argument("--year-end", type=int, help="End year for time series")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        data = query_faostat(
            domain=args.domain,
            country=args.country,
            item=args.item,
            element=args.element,
            year_start=args.year_start,
            year_end=args.year_end,
        )

        if args.format == "json":
            result = {
                "query": {"domain": args.domain, "country": args.country, "item": args.item, "element": args.element},
                "data": data,
                "total": len(data),
            }
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
