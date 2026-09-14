"""
Feature Engineering Module
==========================
Transforms cleaned data into ML-ready features: encoding, normalization,
and creation of new derived features.

YOUR TASKS:
1. Implement encode_categorical()
2. Implement normalize_numeric()
3. Implement create_derived_features()
4. Implement engineer_features() to chain all steps
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

CATEGORICAL_COLUMNS = ['protocol_type', 'service', 'flag']

NUMERIC_COLUMNS = [
    'duration', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
    'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
    'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
    'num_shells', 'num_access_files', 'num_outbound_cmds',
    'is_host_login', 'is_guest_login', 'count', 'srv_count',
    'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
]


def encode_categorical(df):
    """
    Convert categorical text columns to numeric using Label Encoding.

    The NSL-KDD dataset has 3 categorical columns:
    - protocol_type: tcp, udp, icmp
    - service: http, ftp, smtp, etc. (~70 unique values)
    - flag: SF, S0, REJ, etc. (~11 unique values)

    Steps:
    1. For each column in CATEGORICAL_COLUMNS:
       a. Create a LabelEncoder instance
       b. Fit and transform the column
       c. Print the mapping (original value -> encoded value)
    2. Return the modified DataFrame and a dict of encoders (for later use)

    Args:
        df (pd.DataFrame): DataFrame with categorical columns

    Returns:
        tuple: (modified DataFrame, dict of {column_name: LabelEncoder})
    """
    # TODO: Implement this function
    pass


def normalize_numeric(df):
    """
    Normalize numeric features to the range [0, 1] using Min-Max scaling.

    Why normalize?
    - Features like 'src_bytes' can be in millions, while 'land' is 0 or 1
    - ML algorithms perform better when features are on similar scales

    Steps:
    1. Create a MinMaxScaler instance
    2. Fit and transform all NUMERIC_COLUMNS
    3. Replace the original columns with normalized values
    4. Return the modified DataFrame and the fitted scaler

    Args:
        df (pd.DataFrame): DataFrame with numeric columns

    Returns:
        tuple: (modified DataFrame, fitted MinMaxScaler)
    """
    # TODO: Implement this function
    pass


def create_derived_features(df):
    """
    Create new features from existing ones that may help the ML model.

    New features to create:
    1. bytes_ratio: src_bytes / (dst_bytes + 1)
       - High ratio = sending much more than receiving (possible data exfiltration)
       - Adding 1 to denominator avoids division by zero

    2. error_rate: (serror_rate + rerror_rate) / 2
       - Combined error rate — high values suggest scanning/probing activity

    3. is_privileged: 1 if root_shell == 1 OR su_attempted >= 1, else 0
       - Indicates privilege escalation attempts

    4. traffic_intensity: count * srv_count
       - Measures how busy this connection's host/service pair is

    Steps:
    1. Create each derived feature as a new column
    2. Print summary statistics for the new features
    3. Return the modified DataFrame

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: DataFrame with new feature columns added
    """
    # TODO: Implement this function
    pass


def engineer_features(df):
    """
    Run the full feature engineering pipeline.

    Steps:
    1. Encode categorical columns
    2. Normalize numeric columns
    3. Create derived features
    4. Print final feature count
    5. Return the feature-engineered DataFrame

    Args:
        df (pd.DataFrame): Cleaned DataFrame from Phase 1

    Returns:
        pd.DataFrame: ML-ready DataFrame with all features engineered
    """
    print("\n--- Feature Engineering Pipeline ---")

    # TODO: Implement this function by calling the functions above
    pass


if __name__ == '__main__':
    print("Run this module through pipeline.py, or test individual functions.")
