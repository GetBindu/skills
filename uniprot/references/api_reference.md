# UniProt API Reference

## Backend
[UniProt REST API](https://www.uniprot.org/help/api) — `https://rest.uniprot.org/uniprotkb`. Free, no authentication required.

## Query best practices

The `--query` argument should be a **bare gene symbol or protein name** (1–3 words). Strip drug names, mutation labels, and mechanism words.

| Original topic | Correct `--query` |
|---------------|-------------------|
| sotorasib KRAS G12C | `KRAS` |
| imatinib BCR-ABL resistance | `BCR-ABL` |
| trastuzumab HER2+ breast cancer | `HER2` |
| Bruton tyrosine kinase inhibitor | `BTK` or `Bruton tyrosine kinase` |
| P01116 | `P01116` (UniProt accession) |

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query` / `-q` | Gene symbol, protein name, or UniProt accession | required |
| `--organism` | Organism filter (e.g., `human`, `mouse`, `rat`, or NCBI taxonomy ID `9606`) | all |
| `--reviewed` | Only return SwissProt reviewed entries | false |
| `--max-results` | Maximum results to return | 10 |
| `--format` | `summary`, `detailed`, or `json` | `summary` |

## Returned fields

Per-protein record includes:
- **accession** — UniProt primary accession (e.g., `P01116`)
- **id** — UniProt entry name (e.g., `RASK_HUMAN`)
- **protein_name** — Recommended protein name
- **gene_name** — Primary gene symbol
- **organism** — Scientific name
- **sequence_length** — Number of amino acids
- **function** — Free-text functional description
- **reviewed** — Whether entry is in SwissProt (reviewed) or TrEMBL (unreviewed)
- **url** — Link to UniProt entry web page

## Common uses

- **Drug target annotation**: Look up protein function before literature review
- **Ortholog lookup**: Compare same protein across organisms (`--organism human` then `--organism mouse`)
- **Sequence retrieval**: Get canonical sequence length + variants
- **Accession resolution**: Convert gene symbol → UniProt ID for downstream tools (AlphaFold DB, PDB)

## Rate limiting

UniProt REST API does not require authentication and has no hard rate limits, but requests are throttled at ~1 request/second for unauthenticated clients. The script handles this naturally through sequential request patterns.
