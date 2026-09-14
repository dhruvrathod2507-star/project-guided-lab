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
}


def check_missing_values(df):
    """
    Check for missing values in each column.

    Steps:
    1. Use df.isnull().sum() to count missing values per column
    2. Print columns that have missing values (if any)
    3. Print total missing values
    4. Return the count of total missing values

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        int: Total number of missing values
    """
    # TODO: Implement this function
    pass


def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.

    Steps:
    1. Count duplicates using df.duplicated().sum()
    2. Remove duplicates using df.drop_duplicates()
    3. Print how many rows were removed
    4. Return the cleaned DataFrame

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: DataFrame with duplicates removed
    """
    # TODO: Implement this function
    pass


def map_attack_categories(df):
    """
    Map specific attack type labels to their broader categories.

    The 'label' column contains specific attack names (e.g., 'neptune', 'smurf').
    Map these to categories: Normal, DoS, Probe, R2L, U2R.

    Steps:
    1. Strip any trailing '.' from the label column (some versions have this)
    2. Use the ATTACK_CATEGORY_MAP dictionary to create a new 'attack_category' column
    3. Handle unknown attack types by mapping them to 'Unknown'
    4. Print the value counts of attack categories
    5. Return the DataFrame with the new column

    Args:
        df (pd.DataFrame): Input DataFrame with 'label' column

    Returns:
        pd.DataFrame: DataFrame with new 'attack_category' column
    """
    # TODO: Implement this function
    pass


def create_binary_label(df):
    """
    Create a binary classification label: normal (0) vs attack (1).

    Steps:
    1. Create new column 'is_attack': 0 if attack_category == 'Normal', else 1
    2. Print the distribution of binary labels
    3. Return the DataFrame

    Args:
        df (pd.DataFrame): Input DataFrame with 'attack_category' column

    Returns:
        pd.DataFrame: DataFrame with new 'is_attack' column
    """
    # TODO: Implement this function
    pass


def clean_data(df):
    """
    Run the full cleaning pipeline.

    Chain all cleaning steps in order:
    1. Check missing values
    2. Remove duplicates
    3. Drop the 'difficulty_level' column (not needed for modeling)
    4. Map attack categories
    5. Create binary label
    6. Return the cleaned DataFrame

    Args:
        df (pd.DataFrame): Raw input DataFrame

    Returns:
        pd.DataFrame: Fully cleaned DataFrame
    """
    print("\n--- Data Cleaning Pipeline ---")

    # TODO: Implement this function by calling the functions above in order
    pass


if __name__ == '__main__':
    print("Run this module through pipeline.py, or test individual functions here.")
    print("Example:")
    print("  from ingest import load_data")
    print("  df = load_data('data/raw/KDDTrain+.txt')")
    print("  cleaned = clean_data(df)")
