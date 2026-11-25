"""
Feature Engineering Module
==========================
Transforms cleaned data into ML-ready features: encoding, normalization,
and creation of new derived features.

YOUR TASKS:
1. Implement encode_categorical()
2. Implement create_derived_features()
3. Implement normalize_numeric()
4. Implement engineer_features() to chain all steps
5. Save fitted encoders and scaler using joblib for reuse in Phase 4
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import os

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
DERIVED_COLUMNS = ['bytes_ratio', 'error_rate', 'is_privileged', 'traffic_intensity']


def encode_categorical(df):
    """Convert text columns to numbers with LabelEncoder."""
    df = df.copy()
    encoders = {}

    for col in CATEGORICAL_COLUMNS:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

        mapping = {name: code for code, name in enumerate(encoder.classes_)}
        if len(mapping) <= 15:
            print(f"{col} mapping: {mapping}")
        else:
            print(f"{col}: {len(mapping)} unique values encoded")

    return df, encoders


def create_derived_features(df):
    """Add 4 new features. Must run BEFORE normalization."""
    df = df.copy()

    df['bytes_ratio'] = df['src_bytes'] / (df['dst_bytes'] + 1)
    df['error_rate'] = (df['serror_rate'] + df['rerror_rate']) / 2
    df['is_privileged'] = (
        (df['root_shell'] == 1) | (df['su_attempted'] >= 1)
    ).astype(int)
    df['traffic_intensity'] = df['count'] * df['srv_count']

    print("Derived feature summary:")
    print(df[DERIVED_COLUMNS].describe().round(3).to_string())
    return df


def normalize_numeric(df):
    """Scale numeric and derived columns into the range 0 to 1."""
    df = df.copy()
    columns = [c for c in NUMERIC_COLUMNS + DERIVED_COLUMNS if c in df.columns]

    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])

    print(f"Normalized {len(columns)} columns to the 0-1 range")
    return df, scaler


def engineer_features(df):
    """Full pipeline: encode -> derive -> normalize -> save."""
    print("\n--- Feature Engineering Pipeline ---")

    df, encoders = encode_categorical(df)
    df = create_derived_features(df)
    df, scaler = normalize_numeric(df)

    os.makedirs('data/features', exist_ok=True)
    joblib.dump(encoders, 'data/features/label_encoders.joblib')
    joblib.dump(scaler, 'data/features/scaler.joblib')
    print("Saved encoders and scaler to data/features/")

    label_columns = ['label', 'attack_category', 'is_attack']
    n_features = len([c for c in df.columns if c not in label_columns])
    print(f"Feature columns: {n_features}")
    return df

if __name__ == '__main__':
    from ingest import load_data
    from clean import clean_data

    df = clean_data(load_data('data/raw/KDDTrain+.txt'))
    features = engineer_features(df)

    print(features.head())
    print(features[NUMERIC_COLUMNS + DERIVED_COLUMNS].agg(['min', 'max']).T.head(8))