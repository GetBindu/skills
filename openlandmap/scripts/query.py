#!/usr/bin/env python3
"""
OpenLandMap Soil Properties Query Script

Query ML-predicted global soil properties from EnvirometriX.

Usage:
    python query.py --lat 42.0308 --lon -93.6319 --properties ph soc clay
    python query.py --lat 28.5 --lon 77.2 --depth "0-5cm" --format json
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

OPENLANDMAP_API = "https://rest.opengeohub.org/query"


def query_openlandmap(
    latitude: float, longitude: float, properties: Optional[List[str]] = None, depth: str = "0-5cm"
) -> Dict:
    """
    Query OpenLandMap API for soil properties.

    Args:
        latitude: Latitude coordinate (-90 to 90)
        longitude: Longitude coordinate (-180 to 180)
        properties: List of soil properties (e.g., ['ph', 'soc', 'clay'])
        depth: Depth layer (e.g., '0-5cm', '5-15cm')

    Returns:
        Dictionary with soil data
    """
    if not properties:
        properties = ["ph", "soc", "clay"]

    # OpenLandMap uses WCS (Web Coverage Service) protocol
    # This is a simplified query - actual implementation may vary

    soil_data = {
        "location": {"latitude": latitude, "longitude": longitude},
        "depth": depth,
        "properties": {},
        "source": "OpenLandMap (EnvirometriX)",
        "resolution": "250m",
        "method": "Machine Learning Prediction (alternative to SoilGrids)",
    }

    # Note: OpenLandMap API access may require specific authentication
    # This is a placeholder implementation
    try:
        params = {"lon": longitude, "lat": latitude, "depth": depth}

        # Simulated response structure
        # In production, this would make actual API calls
        for prop in properties:
            soil_data["properties"][prop] = {
                "value": None,
                "uncertainty": None,
                "note": "OpenLandMap API integration pending - requires WCS protocol",
            }

        return soil_data

    except Exception as e:
        print(f"Error querying OpenLandMap: {e}", file=sys.stderr)
        return soil_data


def format_summary(soil_data: Dict) -> str:
    """Format soil data as summary."""
    if not soil_data:
        return "No data found."

    loc = soil_data["location"]
    lines = [f"\nOpenLandMap Data for ({loc['latitude']}, {loc['longitude']})"]
    lines.append(f"Depth: {soil_data['depth']}")
    lines.append(f"Source: {soil_data['source']}\n")
    lines.append("-" * 80)

    for prop_key, prop_data in soil_data["properties"].items():
        lines.append(f"\n{prop_key}:")
        if "note" in prop_data:
            lines.append(f"  {prop_data['note']}")
        else:
            lines.append(f"  Value: {prop_data.get('value', 'N/A')}")
            lines.append(f"  Uncertainty: {prop_data.get('uncertainty', 'N/A')}")

    lines.append("\n" + "-" * 80)
    lines.append("\nNote: Full OpenLandMap integration requires WCS protocol implementation")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query OpenLandMap global soil database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 42.0308 --lon -93.6319 --properties ph soc clay
  %(prog)s --lat 28.5 --lon 77.2 --depth "0-5cm" --format json
  
Note: OpenLandMap uses WCS protocol - full implementation pending
        """,
    )

    parser.add_argument("--lat", "--latitude", type=float, required=True, help="Latitude (-90 to 90)")
    parser.add_argument("--lon", "--longitude", type=float, required=True, help="Longitude (-180 to 180)")
    parser.add_argument(
        "--properties",
        "-p",
        nargs="+",
        default=["ph", "soc", "clay"],
        help="Soil properties to query (default: ph soc clay)",
    )
    parser.add_argument("--depth", "-d", default="0-5cm", help="Depth layer (default: 0-5cm)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        soil_data = query_openlandmap(
            latitude=args.lat, longitude=args.lon, properties=args.properties, depth=args.depth
        )

        if args.format == "json":
            print(json.dumps(soil_data, indent=2))
        else:
            print(format_summary(soil_data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
