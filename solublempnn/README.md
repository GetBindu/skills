# solublempnn

Solubility-optimized protein sequence design using SolubleMPNN, a ProteinMPNN variant from the LigandMPNN suite.

## What it does

This is a prompt-only skill (no scripts) that provides LLM instructions for designing protein sequences with higher aqueous solubility using SolubleMPNN. The skill covers:

- Running SolubleMPNN on PDB structures (single-chain and multi-chain complexes)
- Post-design biophysical filtering (GRAVY, instability index, cysteine clustering)
- Sequence liability scanning (N-glycosylation, deamidation, polybasic clusters)
- Decision guide: when to use SolubleMPNN vs ProteinMPNN vs LigandMPNN
- Full E. coli expression workflow (backbone generation through gene synthesis)

Published benchmark: SolubleMPNN achieves 72% soluble expression rate in E. coli vs 54% for standard ProteinMPNN.

## Setup

Requires LigandMPNN installed locally:

```bash
git clone https://github.com/dauparas/LigandMPNN
cd LigandMPNN
pip install -e .
bash get_model_params.sh
```

## Environment variables

None required (LigandMPNN runs locally with downloaded model weights).

## Usage

This skill is used by an LLM agent — no standalone CLI. The SKILL.md contains code examples the agent executes:

```bash
# Basic soluble sequence design
python3 LigandMPNN/run.py \
    --model_type "soluble_mpnn" \
    --checkpoint_path "model_params/solublempnn_v_48_002.pt" \
    --pdb_path structure.pdb \
    --out_folder output/ \
    --number_of_batches 8 \
    --batch_size 4 \
    --temperature 0.1
```

## Dependencies

- `LigandMPNN` (includes SolubleMPNN model)
- `biopython` (for post-design analysis)

## Tested with

- **Direct script run:** N/A (prompt-only skill)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent loaded the solublempnn skill and provided a comprehensive explanation of SolubleMPNN vs ProteinMPNN tradeoffs, the 72% vs 54% soluble expression benchmark, and the full 6-step E. coli expression workflow including post-design filtering criteria.

## Fix notes

- Enhanced description from one-liner to full capability summary
- Added `source:` URL under `metadata:`
