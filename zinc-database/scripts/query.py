#!/usr/bin/env python3
"""
ZINC Database Compound Lookup

Search for purchasable compounds by name, SMILES, or ZINC ID.
Uses PubChem for compound resolution and provides ZINC database links.

Note: The CartBlanche22 REST API is no longer publicly available (returns HTML).
This script uses PubChem as the primary data source for compound lookup and
generates direct ZINC URLs for web-based access.

Usage:
    python query.py --query "aspirin" --format json
    python query.py --query "erlotinib" --limit 5
    python query.py --query "c1ccccc1" --smiles
    python query.py --query "ZINC000000000001"
"""

import argparse
import json
import re
import sys

try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests is required. Install with: uv pip install requests"}))
    sys.exit(1)


PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
ZINC_WEB = "https://cartblanche22.docking.org"


def is_smiles(query):
    """Heuristic: does the query look like a SMILES string?"""
    smiles_chars = set("CNOPSFClBrI[]()=#@+\\/-.")
    return len(query) > 4 and sum(c in smiles_chars for c in query) / len(query) > 0.6


def is_zinc_id(query):
    """Check if query is a ZINC ID."""
    return re.match(r"^ZINC\d+$", query.strip(), re.IGNORECASE) is not None


def pubchem_by_name(name, limit=10):
    """Look up a compound by name via PubChem and return properties + similar compounds."""
    try:
        # Resolve name to CID
        r = requests.get(
            f"{PUBCHEM_BASE}/compound/name/{requests.utils.quote(name)}/property/"
            "IsomericSMILES,CanonicalSMILES,IUPACName,MolecularFormula,MolecularWeight/JSON",
            timeout=15,
        )
        if r.status_code != 200:
            return None, []

        data = r.json()
        props = data.get("PropertyTable", {}).get("Properties", [{}])[0]
        cid = props.get("CID")
        smiles = (
            props.get("IsomericSMILES")
            or props.get("CanonicalSMILES")
            or props.get("SMILES")
            or props.get("ConnectivitySMILES")
        )

        compound = {
            "cid": cid,
            "name": name,
            "iupac_name": props.get("IUPACName"),
            "smiles": smiles,
            "formula": props.get("MolecularFormula"),
            "molecular_weight": props.get("MolecularWeight"),
            "pubchem_url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}" if cid else None,
            "zinc_search_url": f"{ZINC_WEB}/search/smiles?smiles={smiles}" if smiles else None,
        }

        # Get similar compounds from PubChem
        similar = []
        if cid and limit > 1:
            try:
                r2 = requests.get(
                    f"{PUBCHEM_BASE}/compound/fastsimilarity_2d/cid/{cid}/property/"
                    f"IsomericSMILES,IUPACName,MolecularFormula,MolecularWeight/JSON"
                    f"?MaxRecords={limit}",
                    timeout=30,
                )
                if r2.status_code == 200:
                    sim_data = r2.json()
                    for sp in sim_data.get("PropertyTable", {}).get("Properties", []):
                        if sp.get("CID") != cid:
                            similar.append(
                                {
                                    "cid": sp.get("CID"),
                                    "iupac_name": sp.get("IUPACName"),
                                    "smiles": sp.get("IsomericSMILES") or sp.get("CanonicalSMILES") or sp.get("SMILES"),
                                    "formula": sp.get("MolecularFormula"),
                                    "molecular_weight": sp.get("MolecularWeight"),
                                    "pubchem_url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{sp.get('CID')}",
                                }
                            )
            except Exception:
                pass

        return compound, similar

    except Exception as e:
        return {"error": f"PubChem lookup failed: {e!s}"}, []


def pubchem_by_smiles(smiles, limit=10):
    """Look up compound by SMILES via PubChem."""
    try:
        r = requests.get(
            f"{PUBCHEM_BASE}/compound/smiles/{requests.utils.quote(smiles, safe='')}/property/"
            "IsomericSMILES,CanonicalSMILES,IUPACName,MolecularFormula,MolecularWeight/JSON",
            timeout=15,
        )
        if r.status_code != 200:
            return None, []

        data = r.json()
        props = data.get("PropertyTable", {}).get("Properties", [{}])[0]
        cid = props.get("CID")

        compound = {
            "cid": cid,
            "smiles": props.get("IsomericSMILES") or props.get("CanonicalSMILES"),
            "iupac_name": props.get("IUPACName"),
            "formula": props.get("MolecularFormula"),
            "molecular_weight": props.get("MolecularWeight"),
            "pubchem_url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}" if cid else None,
            "zinc_search_url": f"{ZINC_WEB}/search/smiles?smiles={smiles}",
        }

        # Get similar compounds
        similar = []
        if cid and limit > 1:
            try:
                r2 = requests.get(
                    f"{PUBCHEM_BASE}/compound/fastsimilarity_2d/cid/{cid}/property/"
                    f"IsomericSMILES,IUPACName,MolecularFormula,MolecularWeight/JSON"
                    f"?MaxRecords={limit}",
                    timeout=30,
                )
                if r2.status_code == 200:
                    sim_data = r2.json()
                    for sp in sim_data.get("PropertyTable", {}).get("Properties", []):
                        if sp.get("CID") != cid:
                            similar.append(
                                {
                                    "cid": sp.get("CID"),
                                    "iupac_name": sp.get("IUPACName"),
                                    "smiles": sp.get("IsomericSMILES") or sp.get("CanonicalSMILES") or sp.get("SMILES"),
                                    "formula": sp.get("MolecularFormula"),
                                    "molecular_weight": sp.get("MolecularWeight"),
                                    "pubchem_url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{sp.get('CID')}",
                                }
                            )
            except Exception:
                pass

        return compound, similar

    except Exception as e:
        return {"error": f"PubChem SMILES lookup failed: {e!s}"}, []


def lookup_zinc_id(zinc_id):
    """Generate ZINC web URL for a ZINC ID (direct API no longer available)."""
    zinc_id = zinc_id.upper()
    if not zinc_id.startswith("ZINC"):
        zinc_id = f"ZINC{zinc_id}"
    return {
        "zinc_id": zinc_id,
        "zinc_url": f"{ZINC_WEB}/?zinc_id={zinc_id}",
        "note": "Use the web URL to look up this compound on CartBlanche22.",
    }


def main():
    parser = argparse.ArgumentParser(description="Search for purchasable compounds by name, SMILES, or ZINC ID")
    parser.add_argument(
        "--query",
        "--search",
        "-q",
        dest="query",
        required=True,
        help="Compound name, ZINC ID, or SMILES string",
    )
    parser.add_argument("--limit", "-l", type=int, default=10, help="Max similar compounds (default: 10)")
    parser.add_argument("--max-results", type=int, default=None, help="Alias for --limit")
    parser.add_argument(
        "--format",
        "-f",
        default="json",
        choices=["summary", "json"],
        help="Output format (default: json)",
    )
    parser.add_argument("--smiles", action="store_true", help="Force treating query as SMILES")

    args = parser.parse_args()
    limit = args.max_results if args.max_results is not None else args.limit
    query = args.query.strip()

    result = {"query": query, "method": None}

    if is_zinc_id(query):
        result["method"] = "zinc_id"
        result["compound"] = lookup_zinc_id(query)

    elif args.smiles or is_smiles(query):
        result["method"] = "smiles_lookup"
        compound, similar = pubchem_by_smiles(query, limit)
        if compound and "error" not in compound:
            result["compound"] = compound
            result["similar_compounds"] = similar
            result["total_similar"] = len(similar)
        else:
            result["error"] = compound.get("error", "SMILES not found") if compound else "SMILES not found in PubChem"

    else:
        compound, similar = pubchem_by_name(query, limit)
        if compound and "error" not in compound:
            result["method"] = "name_lookup"
            result["compound"] = compound
            result["similar_compounds"] = similar
            result["total_similar"] = len(similar)
        else:
            result["method"] = "not_found"
            result["error"] = (
                compound.get("error", f"Could not resolve '{query}'") if compound else f"'{query}' not found"
            )

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"Compound search for '{query}' ({result.get('method', 'unknown')})")
        c = result.get("compound", {})
        if c:
            print(f"  Name: {c.get('iupac_name', 'N/A')}")
            print(f"  SMILES: {c.get('smiles', 'N/A')}")
            print(f"  Formula: {c.get('formula', 'N/A')}")
            print(f"  MW: {c.get('molecular_weight', 'N/A')}")
            if c.get("pubchem_url"):
                print(f"  PubChem: {c['pubchem_url']}")
            if c.get("zinc_search_url"):
                print(f"  ZINC search: {c['zinc_search_url']}")
        similar = result.get("similar_compounds", [])
        if similar:
            print(f"\n  Similar compounds ({len(similar)}):")
            for s in similar[:5]:
                print(f"    {s.get('iupac_name', 'N/A')[:50]} | {s.get('smiles', '')[:40]}")
        if result.get("error"):
            print(f"  Error: {result['error']}")


if __name__ == "__main__":
    main()
