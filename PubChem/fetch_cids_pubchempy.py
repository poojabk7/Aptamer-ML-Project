"""
fetch_cids_pubchempy.py

Retrieves PubChem Compound IDs (CIDs) for a list of chemical names using the
PubChemPy API.

Input:  Text file containing one compound name per line
Output: Text file mapping each compound name to its corresponding CID

Example:
    python fetch_cids_pubchempy.py --input compound_names.txt --output cids_output.txt
"""

import argparse
import pubchempy as pcp


def fetch_cid(name):
    """
    Query PubChem API and retrieve the first CID match for a chemical name.
    Returns an integer CID or None if not found.
    """
    try:
        compounds = pcp.get_compounds(name, 'name')
        if compounds:
            return compounds[0].cid
    except Exception:
        pass
    return None


def process_file(input_path, output_path):
    """
    Read compound names and write CID results to output text file.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f.readlines() if line.strip()]

    with open(output_path, "w", encoding="utf-8") as out:
        for name in names:
            cid = fetch_cid(name)
            if cid:
                out.write(f"{name} -> CID: {cid}\n")
            else:
                out.write(f"{name} -> CID: Not found\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input text file containing chemical names")
    parser.add_argument("--output", required=True, help="Output text file for CIDs")
    args = parser.parse_args()

    process_file(args.input, args.output)


if __name__ == "__main__":
    main()
