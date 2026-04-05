# zinc-database

Look up purchasable compounds by name, SMILES, or ZINC ID, and find structural analogs.

## What it does

Given a compound name (e.g. "aspirin"), a SMILES string, or a ZINC ID, the skill returns the canonical compound info and a list of structurally similar compounds. Uses the PubChem REST API for resolution and similarity search, and generates direct search URLs to ZINC CartBlanche22 for web-based follow-up. The original ZINC22 `.txt` API is no longer publicly accessible (returns HTML only), so this script pivots to PubChem for all data.

## Setup

```bash
cd zinc-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None. Uses free public PubChem REST API — no authentication required.

## Usage

### Input — by compound name
```bash
python3 scripts/query.py --query "aspirin" --limit 3 --format json
```

### Output
```json
{
  "query": "aspirin",
  "method": "name_lookup",
  "compound": {
    "cid": 2244,
    "name": "aspirin",
    "iupac_name": "2-acetyloxybenzoic acid",
    "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "formula": "C9H8O4",
    "molecular_weight": "180.16",
    "pubchem_url": "https://pubchem.ncbi.nlm.nih.gov/compound/2244",
    "zinc_search_url": "https://cartblanche22.docking.org/search/smiles?smiles=CC(=O)OC1=CC=CC=C1C(=O)O"
  },
  "similar_compounds": [
    {
      "cid": 4133,
      "iupac_name": "methyl 2-hydroxybenzoate",
      "smiles": "COC(=O)C1=CC=CC=C1O",
      "formula": "C8H8O3",
      "molecular_weight": "152.15",
      "pubchem_url": "https://pubchem.ncbi.nlm.nih.gov/compound/4133"
    }
  ],
  "total_similar": 2
}
```

### Other input modes
```bash
# By SMILES (direct structure)
python3 scripts/query.py --query "c1ccccc1" --smiles --limit 5

# By ZINC ID
python3 scripts/query.py --query "ZINC000000000001" --format json

# Human-readable summary
python3 scripts/query.py --query "ibuprofen" --format summary
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query` / `-q` | Compound name, SMILES, or ZINC ID (required) | — |
| `--smiles` | Force treating query as SMILES | auto-detect |
| `--limit` / `-l` | Max similar compounds to return | 10 |
| `--format` / `-f` | `json` or `summary` | `json` |

## Dependencies

- `requests`

## Tested with

- **Direct script run:** ✅ `python3 scripts/query.py --query "aspirin"` returns compound + 2 analogs
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent successfully calls `get_skill_instructions`, sets up venv, and executes two examples (name lookup + SMILES lookup)

### Agno agent verdict (excerpt)
> I executed two examples of the `query.py` script. Example 1: Resolved "aspirin" to CID 2244, extracted SMILES/formula/MW/IUPAC, found similar compounds. Example 2: Recognized benzene SMILES, resolved to CID 241, retrieved properties. Key capabilities: search by name/SMILES/ZINC ID, uses PubChem for resolution, outputs JSON or summary with links to PubChem and ZINC CartBlanche22.
