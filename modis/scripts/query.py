#!/usr/bin/env python3
"""
MODIS Satellite Data Query Script

Query daily global vegetation indices and land surface data from NASA MODIS.

Usage:
    python query.py --product MOD13Q1 --lat 42.0 --lon -93.6 --start 2023-04-01 --end 2023-10-31
    python query.py --product MOD11A1 --lat 28.5 --lon 77.2 --start 2023-01-01 --end 2023-12-31
"""

import argparse
import json
import sys
from typing import Dict

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

MODIS_API = "https://modis.ornl.gov/rst/api/v1"


def query_modis(product: str, latitude: float, longitude: float, start_date: str, end_date: str) -> Dict:
    """
    Query MODIS data via ORNL DAAC MODIS Web Service.

    Args:
        product: MODIS product (e.g., 'MOD13Q1', 'MOD11A1', 'MCD43A4')
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)

    Returns:
        Dictionary with MODIS data
    """
    # Common MODIS products
    products_info = {
        "MOD13Q1": "Vegetation Indices 16-Day 250m",
        "MOD11A1": "Land Surface Temperature Daily 1km",
        "MCD43A4": "Nadir BRDF-Adjusted Reflectance Daily 500m",
        "MOD09A1": "Surface Reflectance 8-Day 500m",
        "MCD15A2H": "Leaf Area Index 8-Day 500m",
    }

    url = f"{MODIS_API}/{product}/subset"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "startDate": start_date.replace("-", ""),  # MODIS API uses YYYYMMDD
        "endDate": end_date.replace("-", ""),
        "kmAboveBelow": 0,
        "kmLeftRight": 0,
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Parse results
        modis_data = {
            "query": {
                "product": product,
                "product_name": products_info.get(product, "Unknown product"),
                "location": {"latitude": latitude, "longitude": longitude},
                "start_date": start_date,
                "end_date": end_date,
            },
            "data": [],
            "source": "MODIS (NASA)",
        }

        if "subset" in data:
            for record in data["subset"]:
                modis_data["data"].append(
                    {
                        "date": record.get("calendar_date", ""),
                        "modis_date": record.get("modis_date", ""),
                        "band": record.get("band", ""),
                        "value": record.get("value", ""),
                        "scale": record.get("scale", ""),
                        "units": record.get("units", ""),
                    }
                )

        modis_data["total"] = len(modis_data["data"])

        return modis_data

    except requests.RequestException as e:
        print(f"Error querying MODIS API: {e}", file=sys.stderr)
        return {"error": str(e)}


def format_summary(modis_data: Dict) -> str:
    """Format MODIS data as summary."""
    if "error" in modis_data:
        return f"Error: {modis_data['error']}"

    lines = ["\nMODIS Data Query"]
    lines.append(f"Product: {modis_data['query']['product']} - {modis_data['query']['product_name']}")
    loc = modis_data["query"]["location"]
    lines.append(f"Location: ({loc['latitude']}, {loc['longitude']})")
    lines.append(f"Period: {modis_data['query']['start_date']} to {modis_data['query']['end_date']}")
    lines.append(f"\nFound {modis_data['total']} records\n")
    lines.append("-" * 80)

    if modis_data.get("data"):
        lines.append("\nSample data (first 10 records):")
        for i, record in enumerate(modis_data["data"][:10], 1):
            lines.append(f"\n{i}. Date: {record['date']}")
            lines.append(f"   Band: {record['band']}, Value: {record['value']} {record.get('units', '')}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query MODIS satellite data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --product MOD13Q1 --lat 42.0 --lon -93.6 --start 2023-04-01 --end 2023-10-31
  %(prog)s --product MOD11A1 --lat 28.5 --lon 77.2 --start 2023-01-01 --end 2023-12-31
  
Common products:
  MOD13Q1  - Vegetation Indices 16-Day 250m (NDVI, EVI)
  MOD11A1  - Land Surface Temperature Daily 1km
  MCD43A4  - Nadir BRDF-Adjusted Reflectance Daily 500m
  MOD09A1  - Surface Reflectance 8-Day 500m
  MCD15A2H - Leaf Area Index 8-Day 500m
        """,
    )

    parser.add_argument("--product", "-p", required=True, help="MODIS product (e.g., MOD13Q1, MOD11A1)")
    parser.add_argument("--lat", "--latitude", type=float, required=True, help="Latitude coordinate")
    parser.add_argument("--lon", "--longitude", type=float, required=True, help="Longitude coordinate")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        modis_data = query_modis(
            product=args.product, latitude=args.lat, longitude=args.lon, start_date=args.start, end_date=args.end
        )

        if args.format == "json":
            print(json.dumps(modis_data, indent=2))
        else:
            print(format_summary(modis_data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
