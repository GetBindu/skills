# uniprot-database

Direct low-level REST API client for UniProt. Protein searches, FASTA retrieval, ID mapping across 40+ databases, streaming large result sets, and advanced query syntax.

## What it does

Thin Python client over the [UniProt REST API](https://www.uniprot.org/help/api) (`https://rest.uniprot.org`). Unlike the higher-level `uniprot` skill which focuses on simple name/accession lookups with a summary output, this skill gives you:

- **Direct HTTP/REST control** — all endpoints (`/uniprotkb/search`, `/uniprotkb/{id}`, `/idmapping`, `/uniprotkb/stream`)
- **All output formats** — json, tsv, xlsx, xml, fasta, txt, rdf
- **Custom field selection** via `--fields` to retrieve only what you need
- **ID mapping** across PDB, Ensembl, RefSeq, KEGG, InterPro, Pfam, and 40+ other databases
- **Streaming** for large result sets (millions of entries)
- **Full query syntax** access (advanced boolean queries, organism + reviewed + date filters)

## When to use this vs. `uniprot`

| Use case | Recommended skill |
|---------|-------------------|
| Quick gene lookup, single protein | `uniprot` |
| Getting FASTA for one accession | either (this one is lighter) |
| Large batch export | `uniprot-database` (streaming) |
| ID mapping (e.g., UniProt → PDB) | `uniprot-database` |
| Custom field selection | `uniprot-database` |
| Multi-database workflow | Use `bioservices` skill (unified 40+ service interface) |

## Setup

```bash
cd uniprot-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None. Free public REST API.

## Usage

### Input — retrieve a single protein as FASTA
```bash
python3 scripts/uniprot_client.py --get P01116 --format fasta
```

### Output
```
>sp|P01116|RASK_HUMAN GTPase KRas OS=Homo sapiens OX=9606 GN=KRAS PE=1 SV=1
MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAG
QEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDL
PSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGC
VKIKKCIIM
```

### Other input modes
```bash
# Search for proteins (tsv output with custom fields)
python3 scripts/uniprot_client.py --query "insulin AND organism_name:human AND reviewed:true" \
  --fields "accession,id,gene_names,length" --format tsv

# ID mapping: UniProt → PDB
python3 scripts/uniprot_client.py --map P01116,P04637 --from UniProtKB_AC-ID --to PDB

# Stream a large result set (returns data in chunks)
python3 scripts/uniprot_client.py --stream "taxonomy_id:9606 AND reviewed:true" --format fasta

# List all available query fields
python3 scripts/uniprot_client.py --list-fields

# List all ID mapping databases
python3 scripts/uniprot_client.py --list-databases
```

## CLI flags

| Flag | Description |
|------|-------------|
| `--query` / `--search` / `-s` | Search query string (full UniProt syntax) |
| `--get` / `-g` | Get a single protein by accession |
| `--map` / `-m` | Map IDs (comma-separated) from one database to another |
| `--stream` | Stream large result sets |
| `--list-fields` | List all available query and output fields |
| `--list-databases` | List all ID mapping target databases |
| `--format` / `-f` | `json`, `tsv`, `xlsx`, `xml`, `fasta`, `txt`, `rdf` |
| `--fields` | Comma-separated field list to return (for `--query`) |
| `--size` | Result page size |
| `--from` | Source database for ID mapping |
| `--to` | Target database for ID mapping |

## Dependencies

- `requests`

## Tested with

- **Direct script run (`--get P01116 --format fasta`):** ✅ Returns KRAS FASTA (189 aa, GN=KRAS, Homo sapiens)
- **`--help`:** ✅ All 11 flags documented
- **`--map`:** ⚠️ Works but uses UniProt's async polling endpoint — can take 30-60s for large jobs (normal)
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent retrieved KRAS FASTA, explained the direct-REST positioning vs. the generic `uniprot` skill, surfaced the `bioservices` recommendation for multi-database workflows

### Agno agent verdict (excerpt)
> The uniprot-database skill provides direct REST API access for low-level HTTP/REST control over UniProt endpoints. Optimized for: field customization, ID mapping across 40+ external databases, streaming large datasets, Swiss-Prot vs TrEMBL distinction. For multi-database Python workflows, prefer the bioservices skill (unified interface to 40+ services); use uniprot-database when you specifically need UniProt control or REST/HTTP work.

## See also

Reference docs (4 files, 1229 lines total):
- `references/api_examples.md` — complete API call examples
- `references/api_fields.md` — all available query/return fields
- `references/id_mapping_databases.md` — list of 40+ supported target databases
- `references/query_syntax.md` — UniProt advanced query syntax

## Fix notes

- Removed stray `__pycache__/`
- Script was already functional (341 lines) — no code changes
- Noted async-polling behavior for `--map` (normal UniProt API behavior, not a bug)
