#!/usr/bin/env python3
"""
ERA5 Climate Reanalysis Query Script

Query global atmospheric reanalysis data from ECMWF/Copernicus.

Usage:
    python query.py --variable "soil_moisture" --north 43 --south 41 --east -93 --west -95 --start 2023-04-01 --end 2023-10-31
    python query.py --variable "temperature" --north 30 --south 28 --east 78 --west 76 --start 2023-01-01 --end 2023-12-31
"""

import argparse
import json
import os
import sys
from typing import Dict

try:
    import cdsapi
except ImportError:
    print("Error: cdsapi is required. Install with: pip install cdsapi")
    sys.exit(1)


def query_era5(
    variable: str,
    north: float,
    south: float,
    east: float,
    west: float,
    start_date: str,
    end_date: str,
    time_resolution: str = "monthly",
) -> Dict:
    """
    Query ERA5 reanalysis data via Copernicus Climate Data Store.

    Args:
        variable: Climate variable (e.g., 'temperature', 'precipitation', 'soil_moisture')
        north: Northern latitude
        south: Southern latitude
        east: Eastern longitude
        west: Western longitude
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        time_resolution: 'hourly' or 'monthly'

    Returns:
        Dictionary with query status and file information
    """
    # Check for CDS API key
    api_key = os.environ.get("CDS_API_KEY")
    if not api_key:
        return {
            "error": "CDS API key required",
            "note": "Register at https://cds.climate.copernicus.eu/ and set CDS_API_KEY environment variable",
        }

    # Map variable names to ERA5 parameter names
    variable_map = {
        "temperature": "2m_temperature",
        "precipitation": "total_precipitation",
        "soil_moisture": "volumetric_soil_water_layer_1",
        "wind": "10m_wind_speed",
    }

    era5_variable = variable_map.get(variable, variable)

    # Determine dataset
    if time_resolution == "hourly":
        dataset = "reanalysis-era5-single-levels"
    else:
        dataset = "reanalysis-era5-single-levels-monthly-means"

    # Parse dates
    start_year, start_month = start_date[:7].split("-")
    end_year, end_month = end_date[:7].split("-")

    request_params = {
        "product_type": "reanalysis",
        "variable": era5_variable,
        "year": [str(y) for y in range(int(start_year), int(end_year) + 1)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "area": [north, west, south, east],
        "format": "netcdf",
    }

    if time_resolution == "hourly":
        request_params["time"] = [f"{h:02d}:00" for h in range(24)]
        request_params["day"] = [f"{d:02d}" for d in range(1, 32)]

    result = {
        "query": {
            "variable": variable,
            "area": {"north": north, "south": south, "east": east, "west": west},
            "start_date": start_date,
            "end_date": end_date,
            "time_resolution": time_resolution,
        },
        "dataset": dataset,
        "era5_variable": era5_variable,
        "status": "Query prepared",
        "note": "ERA5 data download requires CDS API client and can take several minutes",
        "source": "ECMWF/Copernicus Climate Data Store",
    }

    # Note: Actual download would be done here
    # c = cdsapi.Client()
    # c.retrieve(dataset, request_params, 'download.nc')

    result["download_command"] = f"Use cdsapi.Client().retrieve('{dataset}', request_params, 'output.nc')"

    return result


def format_summary(result: Dict) -> str:
    """Format ERA5 query as summary."""
    if "error" in result:
        return f"Error: {result['error']}\n{result.get('note', '')}"

    lines = ["\nERA5 Reanalysis Query"]
    lines.append(f"Variable: {result['query']['variable']}")
    lines.append(f"Area: {result['query']['area']}")
    lines.append(f"Period: {result['query']['start_date']} to {result['query']['end_date']}")
    lines.append(f"Resolution: {result['query']['time_resolution']}\n")
    lines.append("-" * 80)
    lines.append(f"\nDataset: {result['dataset']}")
    lines.append(f"ERA5 Variable: {result['era5_variable']}")
    lines.append(f"\nStatus: {result['status']}")
    lines.append(f"\n{result.get('note', '')}")
    lines.append(f"\nDownload: {result.get('download_command', '')}")
    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query ERA5 climate reanalysis data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --variable "soil_moisture" --north 43 --south 41 --east -93 --west -95 --start 2023-04-01 --end 2023-10-31
  %(prog)s --variable "temperature" --north 30 --south 28 --east 78 --west 76 --start 2023-01-01 --end 2023-12-31
  
Available variables: temperature, precipitation, soil_moisture, wind
Register for CDS API key at: https://cds.climate.copernicus.eu/
        """,
    )

    parser.add_argument(
        "--variable", "-v", required=True, help="Climate variable (temperature, precipitation, soil_moisture, wind)"
    )
    parser.add_argument("--north", type=float, required=True, help="Northern latitude")
    parser.add_argument("--south", type=float, required=True, help="Southern latitude")
    parser.add_argument("--east", type=float, required=True, help="Eastern longitude")
    parser.add_argument("--west", type=float, required=True, help="Western longitude")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument(
        "--time-resolution",
        default="monthly",
        choices=["hourly", "monthly"],
        help="Temporal resolution (default: monthly)",
    )
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        result = query_era5(
            variable=args.variable,
            north=args.north,
            south=args.south,
            east=args.east,
            west=args.west,
            start_date=args.start,
            end_date=args.end,
            time_resolution=args.time_resolution,
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
