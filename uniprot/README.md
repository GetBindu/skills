# uniprot

Look up proteins in UniProt by accession, entry name, or keyword search — returns sequences, functional annotations, cross-references, and features.

## What it does

Queries the [UniProt REST API](https://www.uniprot.org/help/api) (`rest.uniprot.org/uniprotkb`) to retrieve:

- Protein sequences (FASTA)
- Functional descriptions and GO terms
- Domain and feature annotations (Pfam, InterPro, active sites, PTMs)
- Cross-references to PDB, AlphaFold DB, and ~170 other databases
- Organism, gene name, sequence length, review status (SwissProt vs TrEMBL)

## Setup

```bash
cd uniprot
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None. Free public REST API, no authentication.

## Usage

### Input — fetch by accession (most reliable)
```bash
python3 scripts/uniprot_fetch.py --accession P01116 --format summary
```

### Output
```
Found 1 proteins:

----------------------------------------------------------------------------------------------------
Accession    Entry           Gene         Length   Reviewed   Protein Name
----------------------------------------------------------------------------------------------------
P01116       RASK_HUMAN      KRAS         189      Yes        GTPase KRas
----------------------------------------------------------------------------------------------------
```

### Other input modes
```bash
# Fetch by entry name
python3 scripts/uniprot_fetch.py --accession P53_HUMAN

# Multiple accessions (comma-separated, FASTA output)
python3 scripts/uniprot_fetch.py --accession "P53_HUMAN,BRCA1_HUMAN,EGFR_HUMAN" --format fasta

# Search by gene name + organism (note: may return fuzzy matches for short gene symbols)
python3 scripts/uniprot_fetch.py --search "insulin human"

# Detailed view with features and cross-references
python3 scripts/uniprot_fetch.py --accession P04637 --format detailed --include-features --include-xrefs

# Advanced UniProt query syntax
python3 scripts/uniprot_fetch.py --search "gene:TP53 AND organism_id:9606"
```

## ⚠️ Query best practices

UniProt is a **protein database**, not a drug/chemistry database. The `--search` and frontmatter instructions emphasize:

**Pass only the bare gene symbol, protein name, or accession — 1 to 3 words max.** Strip drug names, mutation labels, and mechanism words.

| Original topic | Correct query |
|---------------|---------------|
| sotorasib KRAS G12C | `KRAS` or `P01116` |
| imatinib BCR-ABL resistance | `BCR-ABL` |
| trastuzumab HER2+ breast cancer | `HER2` or `ERBB2` |
| Bruton tyrosine kinase inhibitor | `BTK` |
| TP53 tumor suppressor | `TP53` or `P04637` |

For drug/chemistry queries, use PubChem or ChEMBL skills instead.

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--accession` | UniProt accession or entry name (comma-separated list OK) | — |
| `--search` | Keyword or advanced query string | — |
| `--organism` | Organism filter (`human`, `mouse`, or NCBI taxonomy ID) | all |
| `--reviewed` | Only SwissProt reviewed entries | false |
| `--max-results` | Max results for search | 10 |
| `--format` | `summary`, `detailed`, `fasta`, or `json` | `summary` |
| `--include-features` | Include feature annotations (domains, sites, PTMs) | false |
| `--include-xrefs` | Include cross-references (PDB, Pfam, etc.) | false |

## Dependencies

- `requests`

## Tested with

- **Direct script run (`--accession P01116`):** ✅ Returns KRAS (RASK_HUMAN, 189 aa, GTPase KRas, SwissProt reviewed)
- **Fuzzy search (`--search "KRAS"`):** ⚠️ Can return unrelated matches (MAPKAP1 appeared in one test) — prefer `--accession` for deterministic lookup
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed `--accession P01116 --format summary`, got correct KRAS result, and extracted the full "valid/invalid query" policy from the frontmatter

### Agno agent verdict (excerpt)
> The UniProt skill provides access to the world's most comprehensive protein sequence and functional annotation database. Queries MUST be protein-centric (bare gene symbol, protein name, or accession — 1-3 words max). Valid: 'KRAS', 'EGFR', 'P01116', 'Bruton tyrosine kinase'. Invalid: 'KRAS G12C inhibitor', 'sotorasib KRAS'. Strip drug names, mutation labels, and mechanism words. Use UniProt for protein info, not drug/chemistry — for those, use PubChem or ChEMBL instead.

## See also

- [`references/api_reference.md`](references/api_reference.md) — CLI flag reference + UniProt API details

## Fix notes

- Added missing `references/` directory with `api_reference.md`
- Removed stray `__pycache__/`
- No script changes needed
