#!/usr/bin/env python3
"""
Chai-1 Structure Prediction Client

Submits protein/complex structure prediction jobs to the Chai Discovery API
or runs local inference with chai-lab.

Usage:
    python predict.py --sequence "MTEYKLVVVGAGGVGKS..." --api-key YOUR_KEY
    python predict.py --fasta input.fasta --api-key YOUR_KEY
    python predict.py --fasta input.fasta --local --output-dir results/
"""

import argparse
import json
import sys
import time

try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests required. Install: pip install requests"}))
    sys.exit(1)

CHAI_API_URL = "https://api.chaidiscovery.com/v1/predictions"


def predict_api(sequences: list, api_key: str, num_timesteps: int = 200) -> dict:
    """Submit prediction to Chai Discovery API."""
    payload = {
        "sequences": sequences,
        "num_diffn_timesteps": num_timesteps,
        "num_trunk_recycles": 3,
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    try:
        resp = requests.post(CHAI_API_URL, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        job = resp.json()
        job_id = job.get("job_id")

        # Poll for results
        for _ in range(120):  # Max 60 min
            status_resp = requests.get(f"{CHAI_API_URL}/{job_id}", headers=headers, timeout=15)
            status = status_resp.json()
            if status.get("status") == "completed":
                return {"status": "completed", "job_id": job_id, "results": status.get("results")}
            elif status.get("status") == "failed":
                return {"status": "failed", "job_id": job_id, "error": status.get("error")}
            time.sleep(30)

        return {"status": "timeout", "job_id": job_id}
    except requests.exceptions.HTTPError as e:
        return {"error": f"API error: {e}", "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def predict_local(fasta_path: str, output_dir: str) -> dict:
    """Run local inference with chai-lab."""
    try:
        from pathlib import Path

        import torch
        from chai_lab.chai1 import run_inference

        results = run_inference(
            fasta_file=Path(fasta_path),
            output_dir=Path(output_dir),
            num_trunk_recycles=3,
            num_diffn_timesteps=200,
            seed=42,
            device=torch.device("cuda:0"),
            use_esm_embeddings=True,
        )
        return {
            "status": "completed",
            "output_dir": output_dir,
            "models": [{"index": i, "ptm": float(r.ptm), "iptm": float(r.iptm)} for i, r in enumerate(results)],
        }
    except ImportError:
        return {
            "error": "chai-lab not installed. Install: pip install chai-lab",
            "note": "Requires 16GB GPU VRAM. Use --api-key for cloud inference instead.",
        }
    except Exception as e:
        return {"error": str(e)}


def parse_fasta(fasta_path: str) -> list:
    """Parse FASTA file into Chai API sequence format."""
    sequences = []
    current_header = None
    current_seq = []

    with open(fasta_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_header and current_seq:
                    seq_type, chain_id = parse_header(current_header)
                    sequences.append(
                        {
                            "type": seq_type,
                            "chain_id": chain_id,
                            "sequence": "".join(current_seq),
                        }
                    )
                current_header = line[1:]
                current_seq = []
            elif line:
                current_seq.append(line)
    if current_header and current_seq:
        seq_type, chain_id = parse_header(current_header)
        sequences.append(
            {
                "type": seq_type,
                "chain_id": chain_id,
                "sequence": "".join(current_seq),
            }
        )
    return sequences


def parse_header(header: str) -> tuple:
    """Parse FASTA header like 'protein|A' or 'ligand|L'."""
    parts = header.split("|")
    seq_type = parts[0].strip().lower() if parts else "protein"
    chain_id = parts[1].strip() if len(parts) > 1 else "A"
    return seq_type, chain_id


def main():
    parser = argparse.ArgumentParser(description="Chai-1 Structure Prediction")
    parser.add_argument("--sequence", "-s", help="Single protein sequence")
    parser.add_argument("--fasta", help="Path to FASTA file (multi-chain supported)")
    parser.add_argument("--api-key", help="Chai Discovery API key (for cloud inference)")
    parser.add_argument("--local", action="store_true", help="Run local inference (requires GPU + chai-lab)")
    parser.add_argument("--output-dir", default="./chai_results", help="Output directory for local inference")
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    if not args.sequence and not args.fasta:
        parser.error("Provide --sequence or --fasta")

    if args.sequence:
        sequences = [{"type": "protein", "chain_id": "A", "sequence": args.sequence}]
    else:
        sequences = parse_fasta(args.fasta)

    if args.local:
        if not args.fasta:
            print(json.dumps({"error": "Local inference requires --fasta input file"}))
            sys.exit(1)
        result = predict_local(args.fasta, args.output_dir)
    elif args.api_key:
        result = predict_api(sequences, args.api_key)
    else:
        result = {
            "status": "info",
            "sequences_parsed": len(sequences),
            "sequences": sequences,
            "note": "Provide --api-key for Chai Discovery API or --local for local GPU inference.",
            "api_url": CHAI_API_URL,
        }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
