"""
plot_results.py

Generates graphs from CSV data using matplotlib. Designed for visualization of
machine learning results such as binding affinity, feature distributions, and
model predictions.

Input:
    A CSV file containing:
        - true values column (e.g., "Binding Affinity")
        - predicted values column (optional)
        - numerical features for distribution plots

Example:
    python plot_results.py --file results.csv --true "Binding Affinity" --pred "Predicted"
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt


def plot_true_vs_pred(df, true_col, pred_col):
    plt.scatter(df[true_col], df[pred_col])
    plt.xlabel("True Values")
    plt.ylabel("Predicted Values")
    plt.title("True vs Predicted Values")
    plt.grid(True)
    plt.show()


def plot_distribution(df, col):
    plt.hist(df[col], bins=20)
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.title(f"Distribution of {col}")
    plt.grid(True)
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Input CSV file")
    parser.add_argument("--true", help="Column name for true values")
    parser.add_argument("--pred", help="Column name for predicted values")
    parser.add_argument("--dist", help="Column name for distribution visualization")
    args = parser.parse_args()

    df = pd.read_csv(args.file)

    # Plot true vs predicted
    if args.true and args.pred:
        plot_true_vs_pred(df, args.true, args.pred)

    # Plot distribution of any numeric column
    if args.dist:
        plot_distribution(df, args.dist)


if __name__ == "__main__":
    main()
