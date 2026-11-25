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
    """Load raw NSL-KDD data from a text file (no header row)."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath, header=None, names=COLUMN_NAMES)

    print(f"    Loaded {os.path.basename(filepath)}: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"    Columns: {list(df.columns)}")
    return df


def validate_data(df, expected_columns=43):
    """Run basic validation checks on the loaded data."""
    passed = True

    if df.empty:
        print("    CHECK FAILED: DataFrame is empty")
        passed = False

    if df.shape[1] != expected_columns:
        print(f"    CHECK FAILED: expected {expected_columns} columns, got {df.shape[1]}")
        passed = False

    print("    Data types summary:")
    print(df.dtypes.value_counts().to_string())

    print("    First 5 rows:")
    print(df.head())

    return passed

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
