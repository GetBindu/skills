# Monarch Initiative API v3 Reference

## Base URL
`https://api.monarchinitiative.org/v3/api`

## No API key required — free public API.

## Key Endpoints

| Endpoint | Purpose |
|----------|---------|
| GET /search?q={term} | Search entities by name/ID |
| GET /entity/{id} | Get entity details |
| GET /entity/{id}/associations | Get disease-gene-phenotype links |

## Entity Categories
- `biolink:Disease` — MONDO IDs (e.g., MONDO:0007947)
- `biolink:Gene` — HGNC symbols (e.g., BRCA1)
- `biolink:PhenotypicFeature` — HPO terms (e.g., HP:0001166)

## Data Sources
OMIM, ORPHANET, HPO, ClinVar, MGI (Mouse), ZFIN (Zebrafish), RGD (Rat), FlyBase, WormBase

## Common Use Cases
1. Phenotype-to-gene mapping (patient HPO terms → candidate genes)
2. Disease-gene associations (MONDO ID → causal genes)
3. Cross-species ortholog discovery
4. Rare disease gene discovery
