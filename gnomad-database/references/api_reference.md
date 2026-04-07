# gnomAD API Reference

## Endpoint
- **GraphQL API**: `https://gnomad.broadinstitute.org/api`
- **No API key required**
- **License**: CC0-1.0 (public domain)

## Datasets
| Dataset | Description |
|---------|-------------|
| gnomad_r4 | v4 (730K exomes, 76K genomes) |
| gnomad_r3 | v3 (genomes only) |
| gnomad_r2_1 | v2.1.1 (legacy) |

## Reference Genomes
- GRCh38 (default for v4)
- GRCh37 (legacy)

## Constraint Metrics
| Metric | Interpretation |
|--------|---------------|
| pLI | Probability of loss-of-function intolerance (>0.9 = constrained) |
| LOEUF | Loss-of-function observed/expected upper bound (<0.35 = constrained) |
| oe_lof | Observed/expected LoF ratio |
| oe_mis | Observed/expected missense ratio |

## Variant ID Format
`chromosome-position-reference-alternate` (e.g., `1-55051215-G-A`)

## Population IDs
afr (African), amr (Latino), asj (Ashkenazi), eas (East Asian), fin (Finnish), nfe (Non-Finnish European), sas (South Asian)
