"""
loop_count.py

Counts loop regions in aptamer secondary structures represented in dot-bracket
notation. A loop is defined as a region of unpaired bases ('.') occurring within
paired sections.

Input:  CSV file containing aptamer sequence, secondary structure, and MFE
Output: CSV file with additional columns: Loop Count, Nucleotides in Loops

Example:
    python loop_count.py --input Final_Results.csv --output Loop_Results.csv
"""

import argparse
import csv


def count_loops_and_nucleotides(dot_bracket):
    """
    Count loops and nucleotides within loops based on dot-bracket notation.
    Returns: (loop_count, nucleotide_count)
    """
    stack = []
    loop_count = 0
    nucleotide_count = 0
    in_loop = False

    for char in dot_bracket:
        if char == "(":
            stack.append("(")
            in_loop = False
        elif char == ")":
            if stack:
                stack.pop()
            in_loop = False
        elif char == ".":
            if stack:  # inside structured region
                nucleotide_count += 1
                if not in_loop:
                    loop_count += 1
                    in_loop = True
        else:
            in_loop = False

    return loop_count, nucleotide_count


def process_file(input_path, output_path):
    """
    Read input CSV and write loop statistics to output CSV.
    """
    with open(input_path, "r", encoding="utf-8") as f_in, \
            open(output_path, "w", newline="", encoding="utf-8") as f_out:

        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        # Write header
        writer.writerow(["Aptamer", "Secondary Structure", "MFE",
                         "Loop Count", "Nucleotides in Loops"])

        next(reader)  # skip input header

        for row in reader:
            if len(row) < 3:
                continue

            aptamer = row[0]
            structure = row[1]
            mfe = row[2]

            loops, nucleotides = count_loops_and_nucleotides(structure)
            writer.writerow([aptamer, structure, mfe, loops, nucleotides])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV file with secondary structures")
    parser.add_argument("--output", required=True, help="Output CSV file to save loop statistics")
    args = parser.parse_args()

    process_file(args.input, args.output)


if __name__ == "__main__":
    main()
