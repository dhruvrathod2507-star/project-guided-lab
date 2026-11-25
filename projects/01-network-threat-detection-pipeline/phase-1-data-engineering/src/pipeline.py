"""
ETL Pipeline
=============
Orchestrates the full data pipeline: Ingest → Clean → Feature Engineer → Store.

YOUR TASKS:
1. Import functions from the other modules
2. Chain them together in run_pipeline()
3. Add timing for each step
4. Make this script runnable from the command line
"""

import time
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from ingest import load_data, validate_data
from clean import clean_data
from features import engineer_features
from store import store_data


def run_pipeline(train_path, test_path=None):
    """Execute the full ETL pipeline: ingest -> clean -> features -> store."""
    print("=" * 60)
    print("  NETWORK TRAFFIC ETL PIPELINE")
    print("=" * 60)

    pipeline_start = time.time()

    # Step 1: Ingest
    print("\n[Step 1/4] Ingesting data...")
    step_start = time.time()
    raw_df = load_data(train_path)
    if not validate_data(raw_df):
        raise ValueError("Validation failed - check the raw data file")
    print(f"[Step 1/4] Done ({time.time() - step_start:.1f}s) - {len(raw_df)} rows loaded")

    if test_path and os.path.exists(test_path):
        test_df = load_data(test_path)
        print(f"           Test file checked: {len(test_df)} rows (features are built in Phase 3)")

    # Step 2: Clean
    print("\n[Step 2/4] Cleaning data...")
    step_start = time.time()
    clean_df = clean_data(raw_df)
    dropped = len(raw_df) - len(clean_df)
    print(f"[Step 2/4] Done ({time.time() - step_start:.1f}s) - {len(clean_df)} rows, {dropped} dropped")

    # Step 3: Feature engineering
    print("\n[Step 3/4] Engineering features...")
    step_start = time.time()
    features_df = engineer_features(clean_df)
    label_columns = ['label', 'attack_category', 'is_attack']
    n_features = len([c for c in features_df.columns if c not in label_columns])
    print(f"[Step 3/4] Done ({time.time() - step_start:.1f}s) - {n_features} feature columns")

    # Step 4: Store
    print("\n[Step 4/4] Storing data...")
    step_start = time.time()
    paths = store_data(features_df, clean_df=clean_df)
    print(f"[Step 4/4] Done ({time.time() - step_start:.1f}s)")
    for name, path in paths.items():
        print(f"  -> {name}: {path}")

    # Summary
    total_time = time.time() - pipeline_start
    print("\n" + "=" * 60)
    print(f"  Pipeline complete! Total time: {total_time:.2f}s")
    print("=" * 60)

if __name__ == '__main__':
    train_file = os.path.join('data', 'raw', 'KDDTrain+.txt')
    test_file = os.path.join('data', 'raw', 'KDDTest+.txt')

    if not os.path.exists(train_file):
        print(f"ERROR: Training data not found at '{train_file}'")
        print("Please download the NSL-KDD dataset first.")
        print("See: datasets/README.md for download instructions.")
        sys.exit(1)

    run_pipeline(train_file, test_file)
