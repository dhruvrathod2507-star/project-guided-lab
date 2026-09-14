"""
Data Storage Module
===================
Stores processed data in multiple formats: CSV, Parquet, and SQLite.

YOUR TASKS:
1. Implement save_to_csv()
2. Implement save_to_parquet()
3. Implement save_to_sqlite()
4. Implement store_data() to save in all formats
"""

import pandas as pd
import sqlite3
import os


def save_to_csv(df, filepath):
    """
    Save DataFrame to a CSV file.

    CSV is human-readable and universally supported, but large and slow for big data.

    Steps:
    1. Create the output directory if it doesn't exist
    2. Save the DataFrame to CSV (without the default index column)
    3. Print the file size
    4. Return the filepath

    Args:
        df (pd.DataFrame): DataFrame to save
        filepath (str): Output file path (e.g., 'data/processed/train_clean.csv')

    Returns:
        str: Path to the saved file
    """
    # TODO: Implement this function
    pass


def save_to_parquet(df, filepath):
    """
    Save DataFrame to a Parquet file.

    Parquet is a columnar storage format that is:
    - Much smaller than CSV (compressed)
    - Much faster to read for analytics queries
    - Preserves data types (no type guessing on reload)

    Steps:
    1. Create the output directory if it doesn't exist
    2. Save using df.to_parquet() with snappy compression
    3. Print the file size and compare with CSV size
    4. Return the filepath

    Args:
        df (pd.DataFrame): DataFrame to save
        filepath (str): Output file path (e.g., 'data/features/train_features.parquet')

    Returns:
        str: Path to the saved file
    """
    # TODO: Implement this function
    pass


def save_to_sqlite(df, db_path, table_name='network_traffic'):
    """
    Save DataFrame to a SQLite database.

    SQLite is useful because:
    - You can run SQL queries on your data
    - It's a single file (no server needed)
    - Great for the dashboard in Phase 5

    Steps:
    1. Create the output directory if it doesn't exist
    2. Connect to SQLite database (creates file if it doesn't exist)
    3. Write the DataFrame to a table using df.to_sql()
       - Use if_exists='replace' to overwrite existing data
       - Set index=False to avoid writing the DataFrame index
    4. Verify by running a SELECT COUNT(*) query
    5. Close the connection
    6. Return the database path

    Args:
        df (pd.DataFrame): DataFrame to save
        db_path (str): Path to SQLite database file
        table_name (str): Name of the table to create

    Returns:
        str: Path to the database file
    """
    # TODO: Implement this function
    pass


def store_data(df, output_dir='data'):
    """
    Save data in all three formats.

    Args:
        df (pd.DataFrame): DataFrame to store
        output_dir (str): Base output directory

    Returns:
        dict: Paths to all saved files
    """
    print("\n--- Storing Data ---")

    paths = {}

    csv_path = os.path.join(output_dir, 'processed', 'train_clean.csv')
    parquet_path = os.path.join(output_dir, 'features', 'train_features.parquet')
    db_path = os.path.join(output_dir, 'processed', 'network_traffic.db')

    # TODO: Call each save function and store the returned paths
    # paths['csv'] = save_to_csv(df, csv_path)
    # paths['parquet'] = save_to_parquet(df, parquet_path)
    # paths['sqlite'] = save_to_sqlite(df, db_path)

    return paths


if __name__ == '__main__':
    print("Run this module through pipeline.py, or test individual functions.")
