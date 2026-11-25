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


def _size_mb(filepath):
    """Return a file's size in megabytes."""
    return os.path.getsize(filepath) / (1024 * 1024)


def save_to_csv(df, filepath):
    """Save DataFrame to CSV without the index column."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"CSV saved: {filepath} ({_size_mb(filepath):.1f} MB)")
    return filepath


def save_to_parquet(df, filepath, csv_path=None):
    """Save DataFrame to compressed Parquet."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_parquet(filepath, engine='pyarrow', compression='snappy', index=False)

    size = _size_mb(filepath)
    print(f"Parquet saved: {filepath} ({size:.1f} MB)")
    if csv_path and os.path.exists(csv_path):
        print(f"  CSV is {_size_mb(csv_path) / size:.1f}x the size of the Parquet file")
    return filepath


def save_to_sqlite(df, db_path, table_name='network_traffic'):
    """Save DataFrame to a SQLite table and verify the row count."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False, chunksize=10000)
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"SQLite saved: {db_path} ({_size_mb(db_path):.1f} MB, {count} rows in '{table_name}')")
    finally:
        conn.close()

    return db_path


def store_data(df, output_dir='data', clean_df=None):
    """Save data in all three formats."""
    print("\n--- Storing Data ---")

    paths = {}

    csv_path = os.path.join(output_dir, 'processed', 'train_clean.csv')
    parquet_path = os.path.join(output_dir, 'features', 'train_features.parquet')
    db_path = os.path.join(output_dir, 'processed', 'network_traffic.db')

    csv_source = clean_df if clean_df is not None else df
    paths['csv'] = save_to_csv(csv_source, csv_path)
    paths['parquet'] = save_to_parquet(df, parquet_path, csv_path)
    paths['sqlite'] = save_to_sqlite(df, db_path)

    return paths

if __name__ == '__main__':
    from ingest import load_data
    from clean import clean_data
    from features import engineer_features

    cleaned = clean_data(load_data('data/raw/KDDTrain+.txt'))
    features = engineer_features(cleaned)
    paths = store_data(features, clean_df=cleaned)

    conn = sqlite3.connect(paths['sqlite'])
    query = """
        SELECT attack_category, COUNT(*) AS n
        FROM network_traffic
        GROUP BY attack_category
        ORDER BY n DESC
    """
    print("\nSQL check:")
    print(pd.read_sql(query, conn))
    conn.close()