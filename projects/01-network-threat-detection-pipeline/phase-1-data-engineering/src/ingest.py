"""
Data Ingestion Module
=====================
Loads raw NSL-KDD network traffic data from text files into Pandas DataFrames.

YOUR TASKS:
1. Review the COLUMN_NAMES list — verify it has all 43 column names matching the dataset
2. Implement the load_data() function
3. Implement the validate_data() function
"""

import pandas as pd
import os
import time

COLUMN_NAMES = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes',
    'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
    'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'label', 'difficulty_level'
]


def load_data(filepath):
    """
    Load raw NSL-KDD data from a text file.

    The NSL-KDD files are comma-separated with NO header row.
    You need to:
    1. Check if the file exists — raise FileNotFoundError if not
    2. Use pd.read_csv() with header=None and names=COLUMN_NAMES
    3. Print the shape of the loaded data
    4. Return the DataFrame

    Args:
        filepath (str): Path to the raw data file (e.g., 'data/raw/KDDTrain+.txt')

    Returns:
        pd.DataFrame: Loaded raw data
    """
    # TODO: Implement this function
    # Your code here
    pass


def validate_data(df, expected_columns=43):
    """
    Run basic validation checks on the loaded data.

    Checks to implement:
    1. Verify the DataFrame is not empty
    2. Verify the number of columns matches expected_columns
    3. Print data types summary
    4. Print first 5 rows
    5. Return True if all checks pass, False otherwise

    Args:
        df (pd.DataFrame): The loaded DataFrame
        expected_columns (int): Expected number of columns

    Returns:
        bool: True if validation passes
    """
    # TODO: Implement this function
    # Your code here
    pass


if __name__ == '__main__':
    print("=" * 60)
    print("NSL-KDD Data Ingestion")
    print("=" * 60)

    train_path = os.path.join('data', 'raw', 'KDDTrain+.txt')
    test_path = os.path.join('data', 'raw', 'KDDTest+.txt')

    # Load training data
    print("\n[1] Loading training data...")
    start = time.time()
    train_df = load_data(train_path)
    print(f"    Done in {time.time() - start:.2f}s")

    # Validate training data
    print("\n[2] Validating training data...")
    is_valid = validate_data(train_df)
    print(f"    Validation: {'PASSED' if is_valid else 'FAILED'}")

    # Load test data
    print("\n[3] Loading test data...")
    start = time.time()
    test_df = load_data(test_path)
    print(f"    Done in {time.time() - start:.2f}s")

    print("\n" + "=" * 60)
    print(f"Training set: {train_df.shape[0]} rows, {train_df.shape[1]} columns")
    print(f"Test set:     {test_df.shape[0]} rows, {test_df.shape[1]} columns")
    print("=" * 60)
