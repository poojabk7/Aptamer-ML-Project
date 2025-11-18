"""
numpy_array_conversion.py

Converts an Excel sheet of aptamer-related data into a NumPy array format for
use in machine learning workflows.

Input:  Excel file (.xlsx) containing structured tabular data
Output: NumPy (.npy) file containing the full dataset

Note:
    Update 'file_path' and 'output_file' based on your directory structure.
"""

import numpy as np
import openpyxl


def excel_to_numpy(file_path, output_path):
    """
    Load an Excel file and convert its contents (excluding header) to a NumPy array.
    """
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header row
        data.append(row)

    data_array = np.array(data, dtype=object)
    np.save(output_path, data_array)

    return data_array


def main():
    # Modify these paths before running
    file_path = "/content/xlfornumpy.xlsx"                    # Input Excel file
    output_file = "/content/finalexcelsheetapta_output.npy"   # Output NumPy file

    data_array = excel_to_numpy(file_path, output_file)
    print(f"Data saved to {output_file}")
    print("Array shape:", data_array.shape)
    print("Preview:")
    print(data_array[:5])


if __name__ == "__main__":
    main()
