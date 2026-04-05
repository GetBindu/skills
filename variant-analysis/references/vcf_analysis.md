# VCF Analysis & Variant Annotation Reference

## What this skill delegates to

Thin CLI wrapper for the [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse) `tooluniverse-variant-analysis` agentic workflow. The local script is stdlib-only; all analysis happens upstream.

## Mutation type classification

| Type | Meaning | Typical impact |
|------|---------|---------------|
| **Missense** | Single AA change | Variable; often VUS |
| **Nonsense** | Premature stop codon | Usually loss-of-function |
| **Synonymous** | Same AA encoded | Usually benign (splicing exceptions) |
| **Frameshift** | Indel not multiple of 3 | Usually LoF |
| **Splice** | Disrupts splice site | Often LoF |
| **Intronic** | In intron | Mostly benign (deep intron exceptions) |
| **Intergenic** | Between genes | Mostly benign |
| **5'/3' UTR** | In untranslated region | Variable |

## Structural variants (SV) / Copy number variants (CNV)

| Type | Size | Detection |
|------|------|-----------|
| **Deletion** | >50bp | VCF SVTYPE=DEL |
| **Duplication** | >50bp | VCF SVTYPE=DUP |
| **Inversion** | any | VCF SVTYPE=INV |
| **Translocation** | n/a | VCF SVTYPE=BND |
| **Insertion** | >50bp | VCF SVTYPE=INS |

### Clinical significance of SV/CNV

Uses **ClinGen dosage sensitivity** scores:
- **Haploinsufficiency (HI)**: 3 = sufficient evidence (1 copy loss → disease), 2 = emerging, 1 = minimal, 0 = no evidence
- **Triplosensitivity (TS)**: same scale for copy gain → disease
- CNVs overlapping HI/TS genes with score 3 are clinically actionable

## Common filter criteria

| Filter | Typical threshold | Purpose |
|--------|-------------------|---------|
| **VAF** (variant allele freq) | ≥0.25 (germline), variable (somatic) | Exclude sequencing noise |
| **DP** (total depth) | ≥10 | Require adequate coverage |
| **GQ** (genotype quality) | ≥20 | High-confidence genotype calls |
| **QUAL** | ≥30 (Phred) | Variant call confidence |
| **FILTER** field | PASS | Excludes flagged variants |

## Annotation sources (upstream workflow aggregates)

- **ClinVar**: Clinical significance assertions
- **dbSNP**: Variant IDs and population data
- **gnomAD**: Population allele frequencies (ancestry-stratified)
- **CADD**: Combined deleteriousness score
- **ClinGen**: Dosage sensitivity for SV/CNV interpretation

## Local script usage

```bash
# Report tool count + workflow availability
python3 scripts/run.py --list-workflows

# Attempt a query (returns gap message until upstream skill is published to PyPI)
python3 scripts/run.py --query "What fraction of variants with VAF < 0.3 in /path/file.vcf are missense?"
python3 scripts/run.py --query "Classify structural variants in /path/file.vcf" --format summary
```
