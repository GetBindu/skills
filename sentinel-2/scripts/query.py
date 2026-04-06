#!/usr/bin/env python3
"""
Sentinel-2 Satellite Imagery Query Script

Query Sentinel-2 multispectral imagery from ESA Copernicus program.

Usage:
    python query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
    python query.py --north 28.6 --south 28.4 --east 77.3 --west 77.1 --start 2023-01-01 --end 2023-12-31
"""

import argparse
import json
import os
import sys
from typing import Dict

try:
    from sentinelsat import SentinelAPI
except ImportError:
    print("Error: sentinelsat is required. Install with: pip install sentinelsat")
    sys.exit(1)


def query_sentinel2(
    north: float,
    south: float,
    east: float,
    west: float,
    start_date: str,
    end_date: str,
    cloud_cover_max: int = 20,
    username: str = None,
    password: str = None,
) -> Dict:
    """
    Query Sentinel-2 imagery via Copernicus Open Access Hub.

    Args:
        north: Northern latitude
        south: Southern latitude
        east: Eastern longitude
        west: Western longitude
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        cloud_cover_max: Maximum cloud cover percentage
        username: Copernicus username (or set COPERNICUS_USER env var)
        password: Copernicus password (or set COPERNICUS_PASSWORD env var)

    Returns:
        Dictionary with imagery metadata
    """
    if not username:
        username = os.environ.get("COPERNICUS_USER")
    if not password:
        password = os.environ.get("COPERNICUS_PASSWORD")

    if not username or not password:
        return {
            "error": "Copernicus credentials required",
            "note": "Register at https://scihub.copernicus.eu/ and set COPERNICUS_USER and COPERNICUS_PASSWORD",
        }

    try:
        # Connect to Copernicus Open Access Hub
        api = SentinelAPI(username, password, "https://scihub.copernicus.eu/dhus")

        # Define area of interest
        footprint = f"POLYGON(({west} {south},{east} {south},{east} {north},{west} {north},{west} {south}))"

        # Query products
        products = api.query(
            footprint, date=(start_date, end_date), platformname="Sentinel-2", cloudcoverpercentage=(0, cloud_cover_max)
        )

        # Format results
        imagery_list = []
        for product_id, product_info in products.items():
            imagery_list.append(
                {
                    "product_id": product_id,
                    "title": product_info.get("title", ""),
                    "date": product_info.get("beginposition", "").split("T")[0]
                    if product_info.get("beginposition")
                    else "",
                    "cloud_cover": product_info.get("cloudcoverpercentage", ""),
                    "size_mb": product_info.get("size", ""),
                    "product_type": product_info.get("producttype", ""),
                    "download_url": product_info.get("link", ""),
                }
            )

        return {
            "query": {
                "area": {"north": north, "south": south, "east": east, "west": west},
                "start_date": start_date,
                "end_date": end_date,
                "cloud_cover_max": cloud_cover_max,
            },
            "imagery": imagery_list,
            "total": len(imagery_list),
            "source": "Sentinel-2 (ESA Copernicus)",
        }

    except Exception as e:
        return {"error": str(e)}


def format_summary(result: Dict) -> str:
    """Format Sentinel-2 query as summary."""
    if "error" in result:
        return f"Error: {result['error']}\n{result.get('note', '')}"

    lines = ["\nSentinel-2 Imagery Query"]
    area = result["query"]["area"]
    lines.append(f"Area: ({area['south']}, {area['west']}) to ({area['north']}, {area['east']})")
    lines.append(f"Period: {result['query']['start_date']} to {result['query']['end_date']}")
    lines.append(f"Cloud cover: ≤{result['query']['cloud_cover_max']}%")
    lines.append(f"\nFound {result['total']} scenes\n")
    lines.append("-" * 80)

    if result.get("imagery"):
        lines.append("\nAvailable scenes:")
        for i, img in enumerate(result["imagery"][:10], 1):
            lines.append(f"\n{i}. {img['title']}")
            lines.append(f"   Date: {img['date']}, Cloud cover: {img['cloud_cover']}%")
            lines.append(f"   Size: {img['size_mb']}, Type: {img['product_type']}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query Sentinel-2 satellite imagery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
  %(prog)s --north 28.6 --south 28.4 --east 77.3 --west 77.1 --start 2023-01-01 --end 2023-12-31 --cloud-max 10
  
Register for free at: https://scihub.copernicus.eu/
        """,
    )

    parser.add_argument("--north", type=float, required=True, help="Northern latitude")
    parser.add_argument("--south", type=float, required=True, help="Southern latitude")
    parser.add_argument("--east", type=float, required=True, help="Eastern longitude")
    parser.add_argument("--west", type=float, required=True, help="Western longitude")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--cloud-max", type=int, default=20, help="Max cloud cover %% (default: 20)")
    parser.add_argument("--username", help="Copernicus username (or set COPERNICUS_USER)")
    parser.add_argument("--password", help="Copernicus password (or set COPERNICUS_PASSWORD)")
    parser.add_argument("--format", "-f", default="json", choices=["summary", "json"], help="Output format")

    args = parser.parse_args()

    try:
        result = query_sentinel2(
            north=args.north,
            south=args.south,
            east=args.east,
            west=args.west,
            start_date=args.start,
            end_date=args.end,
            cloud_cover_max=args.cloud_max,
            username=args.username,
            password=args.password,
        )

        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(result))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
