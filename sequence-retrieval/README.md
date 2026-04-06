# sequence-retrieval

Retrieve biological sequences (DNA, RNA, protein) from NCBI and ENA via ToolUniverse with gene disambiguation and accession handling.

## What it does

Wraps the `tooluniverse-sequence-retrieval` agentic workflow for retrieving sequences from NCBI and ENA databases. Handles gene disambiguation, accession type detection (GenBank, RefSeq, EMBL), and generates detailed sequence profiles with metadata, cross-database references, and download options.

**Note**: The pip-published `tooluniverse` package bundles ~214 data-source tool clients but does not include the agentic skill workflow definitions. The script detects this gap and provides a structured error pointing to the upstream repo.

## Setup

```bash
cd sequence-retrieval
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/run.py --list-workflows
python3 scripts/run.py --query "Retrieve BRCA1 mRNA sequence from NCBI"
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Sequence retrieval query | (required unless `--list-workflows`) |
| `--format`, `-f` | Output format (json/summary) | `json` |
| `--no-cache` | Disable caching | off |
| `--list-workflows` | List available tools and exit | off |

## Dependencies

- `tooluniverse`, `pyyaml`

## Tested with

- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described NCBI/ENA sequence retrieval, accession handling, and the pip vs upstream gap.

## Fix notes

- Merged duplicate YAML frontmatter blocks
- Upgraded description, added source URL under metadata
- Rewrote run.py with --list-workflows, gap detection, use_cache compat
- Cleaned `__pycache__/`
