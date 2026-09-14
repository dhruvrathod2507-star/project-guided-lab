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
    """
    Execute the full ETL pipeline.

    Steps:
    1. INGEST — Load raw data files
    2. CLEAN — Handle missing values, duplicates, fix types, map labels
    3. FEATURES — Encode, normalize, create derived features
    4. STORE — Save to CSV, Parquet, and SQLite

    For each step:
    - Print the step name and number
    - Record the start time
    - Execute the step
    - Print the elapsed time and a summary

    Args:
        train_path (str): Path to KDDTrain+.txt
        test_path (str, optional): Path to KDDTest+.txt
    """
    print("=" * 60)
    print("  NETWORK TRAFFIC ETL PIPELINE")
    print("=" * 60)

    pipeline_start = time.time()

    # ── Step 1: Ingest ──────────────────────────────────────
    # TODO: Load the training data using load_data()
    # TODO: Validate it using validate_data()
    # TODO: Print how many rows were loaded and how long it took

    # ── Step 2: Clean ───────────────────────────────────────
    # TODO: Clean the data using clean_data()
    # TODO: Print how many rows remain after cleaning

    # ── Step 3: Feature Engineering ─────────────────────────
    # TODO: Engineer features using engineer_features()
    # TODO: Print the final number of columns/features

    # ── Step 4: Store ───────────────────────────────────────
    # TODO: Store the data using store_data()
    # TODO: Print the paths to all saved files

    # ── Summary ─────────────────────────────────────────────
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
