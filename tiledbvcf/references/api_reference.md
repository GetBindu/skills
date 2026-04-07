# TileDB-VCF Quick Reference

## Key Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| sample_name | str | Sample identifier |
| contig | str | Chromosome |
| pos_start | int | Variant start (1-based) |
| pos_end | int | Variant end |
| alleles | list[str] | REF + ALT alleles |
| id | str | Variant ID (rsID) |
| fmt_GT | str | Genotype (0/1, 1/1) |
| fmt_GQ | int | Genotype quality |
| fmt_DP | int | Read depth |
| fmt_AF | float | Allele frequency |
| info_* | varies | Any INFO field |
| fmt_* | varies | Any FORMAT field |

## Performance
- Ingestion: ~500 samples/hour
- Query: 10-100x faster than tabix on large cohorts
- Storage: ~3-5x compression vs gzipped VCF
- Incremental: Add samples without reprocessing

## Cloud Config (S3)
```python
import tiledb
tiledb.Config({
    "vfs.s3.aws_access_key_id": "KEY",
    "vfs.s3.aws_secret_access_key": "SECRET",
    "vfs.s3.region": "us-east-1"
})
```
