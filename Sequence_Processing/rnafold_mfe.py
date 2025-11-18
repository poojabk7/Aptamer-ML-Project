"""
rnafold_mfe.py

Computes secondary structures and Minimum Free Energy (MFE) values for aptamer
sequences using RNAfold from the ViennaRNA package.

Input:  FASTA file containing sequences
Output: CSV file with sequence ID, sequence, predicted structure, and MFE

Example:
    python rnafold_mfe.py --input input.fasta --output results.csv
"""

import argparse
import csv
import subprocess
import shlex


def read_fasta(filepath):
    """
    Read a FASTA file and return a list of (header, sequence) tuples.
    """
    records = []
    header = None
    seq = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    records.append((header, "".join(seq)))
                header = line[1:]
                seq = []
            else:
                seq.append(line)

    if header is not None:
        records.append((header, "".join(seq)))

    return records


def run_rnafold(sequence):
    """
    Execute RNAfold on a sequence using subprocess.
    Returns: (structure, mfe)
    """
    try:
        cmd = f"echo {shlex.quote(sequence)} | RNAfold --noPS"
        result = subprocess.run(
            ["bash", "-lc", cmd],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().splitlines()

        if len(lines) >= 2:
            structure_line = lines[1].strip()
            structure_part, mfe_part = structure_line.rsplit(" ", 1)
            structure = structure_part
            mfe = float(mfe_part.strip("()"))
            return structure, mfe

    except Exception:
        pass

    return "", 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input FASTA file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    records = read_fasta(args.input)
    results = []

    for header, seq in records:
        structure, mfe = run_rnafold(seq)
        results.append((header, seq, structure, mfe))

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Aptamer", "Sequence", "Secondary Structure", "MFE"])
        for header, seq, struct, mfe in results:
            writer.writerow([header, seq, struct, f"{mfe:.2f}"])


if __name__ == "__main__":
    main()
