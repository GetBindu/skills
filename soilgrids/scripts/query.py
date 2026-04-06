#!/usr/bin/env python3
"""
SoilGrids Global Soil Data Query Script

Query ML-predicted global soil properties at 250m resolution from ISRIC.

Usage:
    python query.py --lat 42.0308 --lon -93.6319 --properties phh2o soc clay
    python query.py --lat 28.5 --lon 77.2 --depths "0-5" "5-15" --format json
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

SOILGRIDS_API = "https://rest.isric.org/soilgrids/v2.0/properties/query"

PROPERTY_NAMES = {
    "phh2o": "Soil pH (H2O)",
    "soc": "Soil Organic Carbon",
    "clay": "Clay content",
    "sand": "Sand content",
    "silt": "Silt content",
    "bdod": "Bulk density",
    "cec": "Cation Exchange Capacity",
    "nitrogen": "Nitrogen content",
    "cfvo": "Coarse fragments",
}


def query_soilgrids(
    latitude: float, longitude: float, properties: Optional[List[str]] = None, depths: Optional[List[str]] = None
) -> Dict:
    """
    Query SoilGrids API for soil properties.

    Args:
        latitude: Latitude coordinate (-90 to 90)
        longitude: Longitude coordinate (-180 to 180)
        properties: List of soil properties (e.g., ['phh2o', 'soc', 'clay'])
        depths: List of depth layers (e.g., ['0-5', '5-15', '15-30'])

    Returns:
        Dictionary with soil data by property and depth
    """
    if not properties:
        properties = ["phh2o", "soc", "clay"]

    params = {"lon": longitude, "lat": latitude, "property": properties}

    if depths:
        params["depth"] = depths

    try:
        response = requests.get(SOILGRIDS_API, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Parse and format results
        soil_data = {
            "location": {"latitude": latitude, "longitude": longitude},
            "properties": {},
            "source": "ISRIC SoilGrids v2.0",
            "resolution": "250m",
            "method": "Machine Learning Prediction",
        }

        if "properties" in data:
            for prop in data["properties"]["layers"]:
                prop_name = prop["name"]
                unit = prop.get("unit_measure", {}).get("mapped_units", "")

                soil_data["properties"][prop_name] = {
                    "name": PROPERTY_NAMES.get(prop_name, prop_name),
                    "unit": unit,
                    "depths": {},
                }

                for depth in prop.get("depths", []):
                    depth_label = depth["label"]
                    values = depth.get("values", {})

                    soil_data["properties"][prop_name]["depths"][depth_label] = {
                        "mean": values.get("mean"),
                        "uncertainty": values.get("uncertainty"),
                        "depth_cm": depth.get("range", {}),
                    }

        return soil_data

    except requests.RequestException as e:
        print(f"Error querying SoilGrids API: {e}", file=sys.stderr)
        return {}


def format_summary(soil_data: Dict) -> str:
    """Format soil data as summary."""
    if not soil_data or "properties" not in soil_data:
        return "No data found."

    loc = soil_data["location"]
    lines = [f"\nSoilGrids Data for ({loc['latitude']}, {loc['longitude']})"]
    lines.append(f"Source: {soil_data['source']}, Resolution: {soil_data['resolution']}\n")
    lines.append("-" * 80)

    for prop_key, prop_data in soil_data["properties"].items():
        lines.append(f"\n{prop_data['name']} ({prop_data['unit']}):")

        for depth, values in prop_data["depths"].items():
            mean = values.get("mean", "N/A")
            unc = values.get("uncertainty", "N/A")
            lines.append(f"  {depth}cm: {mean} ± {unc}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query SoilGrids global soil database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 42.0308 --lon -93.6319 --properties phh2o soc clay
  %(prog)s --lat 28.5 --lon 77.2 --depths "0-5" "5-15" "15-30"
  %(prog)s --lat -23.5 --lon -46.6 --properties phh2o bdod cec --format json
  
Available properties: phh2o, soc, clay, sand, silt, bdod, cec, nitrogen, cfvo
        """,
    )

    parser.add_argument("--lat", "--latitude", type=float, required=True, help="Latitude (-90 to 90)")
    parser.add_argument("--lon", "--longitude", type=float, required=True, help="Longitude (-180 to 180)")
    parser.add_argument(
        "--properties",
        "-p",
        nargs="+",
        default=["phh2o", "soc", "clay"],
        help="Soil properties to query (default: phh2o soc clay)",
    )
    parser.add_argument("--depths", "-d", nargs="+", help="Depth layers in cm (e.g., 0-5 5-15 15-30)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        soil_data = query_soilgrids(
            latitude=args.lat, longitude=args.lon, properties=args.properties, depths=args.depths
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
