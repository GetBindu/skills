#!/usr/bin/env python3
"""
USDA NASS Agricultural Statistics Query Script

Query US crop production, acreage, yields, and prices from USDA NASS QuickStats API.

Usage:
    python query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --year 2023
    python query.py --commodity "SOYBEANS" --data-item "PRODUCTION" --format json
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

NASS_API = "https://quickstats.nass.usda.gov/api/api_GET/"


def query_nass(
    commodity: str,
    data_item: str,
    state: Optional[str] = None,
    year: Optional[int] = None,
    api_key: Optional[str] = None,
) -> List[Dict]:
    """
    Query USDA NASS QuickStats API.

    Args:
        commodity: Crop or livestock commodity (e.g., 'CORN', 'SOYBEANS')
        data_item: Statistic type (e.g., 'YIELD', 'PRODUCTION', 'ACRES PLANTED')
        state: US state name (optional)
        year: Year for data (optional)
        api_key: NASS API key (or set NASS_API_KEY env var)

    Returns:
        List of statistics dictionaries
    """
    if not api_key:
        api_key = os.environ.get("NASS_API_KEY")

    if not api_key:
        raise ValueError("NASS API key required. Set NASS_API_KEY environment variable or pass --api-key")

    params = {
        "key": api_key,
        "commodity_desc": commodity.upper(),
        "statisticcat_desc": data_item.upper(),
        "format": "JSON",
    }

    if state:
        params["state_name"] = state.upper()

    if year:
        params["year"] = year

    try:
        response = requests.get(NASS_API, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "data" not in data:
            return []

        # Parse and format results
        statistics = []
        for item in data["data"]:
            statistics.append(
                {
                    "commodity": item.get("commodity_desc", ""),
                    "data_item": item.get("statisticcat_desc", ""),
                    "value": item.get("Value", ""),
                    "unit": item.get("unit_desc", ""),
                    "state": item.get("state_name", ""),
                    "county": item.get("county_name", ""),
                    "year": item.get("year", ""),
                    "period": item.get("reference_period_desc", ""),
                    "source": "USDA NASS QuickStats",
                }
            )

        return statistics

    except requests.RequestException as e:
        print(f"Error querying NASS API: {e}", file=sys.stderr)
        return []


def format_summary(statistics: List[Dict]) -> str:
    """Format statistics as summary."""
    if not statistics:
        return "No data found."

    lines = [f"\nFound {len(statistics)} records:\n"]
    lines.append("-" * 80)

    for i, stat in enumerate(statistics[:10], 1):
        lines.append(f"\n{i}. {stat['commodity']} - {stat['data_item']}")
        lines.append(f"   Value: {stat['value']} {stat['unit']}")
        lines.append(f"   Location: {stat['county'] or stat['state']}, Year: {stat['year']}")

    if len(statistics) > 10:
        lines.append(f"\n... and {len(statistics) - 10} more records")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query USDA NASS agricultural statistics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --commodity "CORN" --data-item "YIELD" --state "IOWA" --year 2023
  %(prog)s --commodity "SOYBEANS" --data-item "PRODUCTION" --format json
  %(prog)s --commodity "WHEAT" --data-item "PRICE RECEIVED" --state "KANSAS"
        """,
    )

    parser.add_argument("--commodity", "-c", required=True, help="Commodity name (e.g., CORN, SOYBEANS, WHEAT)")
    parser.add_argument(
        "--data-item", "-d", required=True, help="Data item (e.g., YIELD, PRODUCTION, ACRES PLANTED, PRICE RECEIVED)"
    )
    parser.add_argument("--state", "-s", help="State name (optional)")
    parser.add_argument("--year", "-y", type=int, help="Year (optional)")
    parser.add_argument("--api-key", "-k", help="NASS API key (or set NASS_API_KEY env var)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        statistics = query_nass(
            commodity=args.commodity, data_item=args.data_item, state=args.state, year=args.year, api_key=args.api_key
        )

        if args.format == "json":
            result = {
                "query": {
                    "commodity": args.commodity,
                    "data_item": args.data_item,
                    "state": args.state,
                    "year": args.year,
                },
                "statistics": statistics,
                "total": len(statistics),
            }
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(statistics))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
