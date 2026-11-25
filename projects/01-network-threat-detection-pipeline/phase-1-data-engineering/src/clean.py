"""
Data Cleaning Module
====================
Cleans raw NSL-KDD data: handles missing values, removes duplicates,
fixes data types, and maps attack labels to categories.

YOUR TASKS:
1. Implement check_missing_values()
2. Implement remove_duplicates()
3. Implement map_attack_categories()
4. Implement create_binary_label()
5. Implement clean_data() to chain all steps
"""

import pandas as pd

ATTACK_CATEGORY_MAP = {
    'normal': 'Normal',

    # DoS — Denial of Service attacks
    'back': 'DoS', 'land': 'DoS', 'neptune': 'DoS', 'pod': 'DoS',
    'smurf': 'DoS', 'teardrop': 'DoS', 'apache2': 'DoS',
    'udpstorm': 'DoS', 'processtable': 'DoS', 'mailbomb': 'DoS',

    # Probe — Surveillance/Scanning attacks
    'ipsweep': 'Probe', 'nmap': 'Probe', 'portsweep': 'Probe',
    'satan': 'Probe', 'mscan': 'Probe', 'saint': 'Probe',

    # R2L — Remote to Local attacks
    'ftp_write': 'R2L', 'guess_passwd': 'R2L', 'imap': 'R2L',
    'multihop': 'R2L', 'phf': 'R2L', 'spy': 'R2L',
    'warezclient': 'R2L', 'warezmaster': 'R2L',
    'snmpgetattack': 'R2L', 'named': 'R2L', 'xlock': 'R2L',
    'xsnoop': 'R2L', 'sendmail': 'R2L', 'httptunnel': 'R2L',

    # U2R — User to Root attacks
    'buffer_overflow': 'U2R', 'loadmodule': 'U2R', 'perl': 'U2R',
    'rootkit': 'U2R', 'sqlattack': 'U2R', 'xterm': 'U2R', 'ps': 'U2R',

    # Additional attack types found in KDDTest+ (not in KDDTrain+)
    'snmpguess': 'R2L', 'worm': 'R2L',
}


def check_missing_values(df):
    """Count missing values per column and in total."""
    missing = df.isnull().sum()
    total = int(missing.sum())

    columns_with_missing = missing[missing > 0]
    if total > 0:
        print("Columns with missing values:")
        print(columns_with_missing.to_string())

    print(f"Missing values: {total}")
    return total


def remove_duplicates(df):
    """Drop duplicate rows and report how many were removed."""
    duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates()
    print(f"Duplicates removed: {duplicates}")
    return df


def map_attack_categories(df):
    """Group specific attack names into 5 categories."""
    df = df.copy()
    df['label'] = df['label'].str.strip().str.rstrip('.')
    df['attack_category'] = df['label'].map(ATTACK_CATEGORY_MAP)

    unknown = df.loc[df['attack_category'].isnull(), 'label'].unique()
    if len(unknown) > 0:
        print(f"Unknown attack types: {list(unknown)}")
    df['attack_category'] = df['attack_category'].fillna('Unknown')

    print("Attack categories:")
    print(df['attack_category'].value_counts().to_string())
    return df


def create_binary_label(df):
    """Add is_attack: 0 = Normal, 1 = any attack."""
    df = df.copy()
    df['is_attack'] = (df['attack_category'] != 'Normal').astype(int)

    counts = df['is_attack'].value_counts()
    print(f"Binary labels - Normal: {counts.get(0, 0)}, Attack: {counts.get(1, 0)}")
    return df


def clean_data(df):
    """Run the full cleaning pipeline."""
    print("\n--- Data Cleaning Pipeline ---")

    check_missing_values(df)
    df = remove_duplicates(df)
    df = df.drop(columns=['difficulty_level'])
    df = map_attack_categories(df)
    df = create_binary_label(df)

    print(f"Columns after cleaning: {df.shape[1]}")
    return df


if __name__ == '__main__':
    from ingest import load_data

    df = load_data('data/raw/KDDTrain+.txt')
    cleaned = clean_data(df)
    print(cleaned[['label', 'attack_category', 'is_attack']].head())