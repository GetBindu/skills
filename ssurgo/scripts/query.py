#!/usr/bin/env python3
"""
USDA SSURGO Soil Survey Query Script

Query detailed US soil survey data from USDA NRCS.

Usage:
    python query.py --lat 42.0308 --lon -93.6319 --properties ph om clay
    python query.py --lat 36.1 --lon -95.9 --format json
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

SSURGO_API = "https://sdmdataaccess.nrcs.usda.gov/Tabular/post.rest"


def query_ssurgo(latitude: float, longitude: float, properties: Optional[List[str]] = None) -> Dict:
    """
    Query USDA SSURGO soil survey data.

    Args:
        latitude: Latitude coordinate (US only)
        longitude: Longitude coordinate (US only)
        properties: List of soil properties (e.g., ['ph', 'om', 'clay'])

    Returns:
        Dictionary with soil data
    """
    if not properties:
        properties = ["ph", "om", "clay"]

    # SQL query to get map unit at location
    query = f"""
    SELECT mukey, muname
    FROM mapunit
    WHERE mukey IN (
        SELECT * FROM SDA_Get_Mukey_from_intersection_with_WktWgs84(
            'point({longitude} {latitude})'
        )
    )
    """

    try:
        response = requests.post(SSURGO_API, data={"query": query, "format": "JSON"}, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data.get("Table"):
            return {
                "location": {"latitude": latitude, "longitude": longitude},
                "error": "No SSURGO data found for this location",
                "note": "Location may be outside US or in unsurveyed area",
            }

        # Get map unit info
        mukey = data["Table"][0][0]
        muname = data["Table"][0][1]

        # Query soil properties for this map unit
        prop_query = f"""
        SELECT
            chorizon.hzdept_r,
            chorizon.hzdepb_r,
            chorizon.ph1to1h2o_r,
            chorizon.om_r,
            chorizon.claytotal_r,
            chorizon.sandtotal_r,
            chorizon.awc_r
        FROM component
        INNER JOIN chorizon ON component.cokey = chorizon.cokey
        WHERE component.mukey = {mukey}
        AND component.compkind = 'Series'
        ORDER BY chorizon.hzdept_r
        """

        prop_response = requests.post(SSURGO_API, data={"query": prop_query, "format": "JSON"}, timeout=30)
        prop_response.raise_for_status()
        prop_data = prop_response.json()

        # Format results
        soil_data = {
            "location": {"latitude": latitude, "longitude": longitude},
            "map_unit": muname,
            "map_unit_key": mukey,
            "horizons": [],
            "source": "USDA NRCS SSURGO",
            "method": "Ground Survey",
        }

        if prop_data.get("Table"):
            for row in prop_data["Table"]:
                soil_data["horizons"].append(
                    {
                        "depth_top_cm": row[0],
                        "depth_bottom_cm": row[1],
                        "ph": row[2],
                        "organic_matter_pct": row[3],
                        "clay_pct": row[4],
                        "sand_pct": row[5],
                        "available_water_capacity": row[6],
                    }
                )

        return soil_data

    except requests.RequestException as e:
        print(f"Error querying SSURGO API: {e}", file=sys.stderr)
        return {}


def format_summary(soil_data: Dict) -> str:
    """Format soil data as summary."""
    if not soil_data:
        return "No data found."

    if "error" in soil_data:
        return f"Error: {soil_data['error']}\n{soil_data.get('note', '')}"

    loc = soil_data["location"]
    lines = [f"\nSSURGO Data for ({loc['latitude']}, {loc['longitude']})"]
    lines.append(f"Map Unit: {soil_data['map_unit']}")
    lines.append(f"Source: {soil_data['source']}\n")
    lines.append("-" * 80)

    if soil_data.get("horizons"):
        lines.append("\nSoil Horizons:")
        for i, horizon in enumerate(soil_data["horizons"], 1):
            depth = f"{horizon['depth_top_cm']}-{horizon['depth_bottom_cm']}cm"
            lines.append(f"\n  Horizon {i} ({depth}):")
            lines.append(f"    pH: {horizon.get('ph', 'N/A')}")
            lines.append(f"    Organic Matter: {horizon.get('organic_matter_pct', 'N/A')}%")
            lines.append(f"    Clay: {horizon.get('clay_pct', 'N/A')}%")
            lines.append(f"    Sand: {horizon.get('sand_pct', 'N/A')}%")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query USDA SSURGO soil survey database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 42.0308 --lon -93.6319 --properties ph om clay
  %(prog)s --lat 36.1 --lon -95.9 --format json
  %(prog)s --lat 39.7 --lon -104.9
  
Note: SSURGO only covers the United States
        """,
    )

    parser.add_argument("--lat", "--latitude", type=float, required=True, help="Latitude (US locations only)")
    parser.add_argument("--lon", "--longitude", type=float, required=True, help="Longitude (US locations only)")
    parser.add_argument(
        "--properties",
        "-p",
        nargs="+",
        default=["ph", "om", "clay"],
        help="Soil properties to query (default: ph om clay)",
    )
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        soil_data = query_ssurgo(latitude=args.lat, longitude=args.lon, properties=args.properties)

        if args.format == "json":
            print(json.dumps(soil_data, indent=2))
        else:
            print(format_summary(soil_data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
