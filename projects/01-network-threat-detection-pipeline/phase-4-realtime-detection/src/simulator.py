"""
Network Traffic Simulator
=========================
Reads processed test data and yields records in batches to simulate
real-time network traffic arriving at the detector.

We load the ALREADY PROCESSED Parquet file from Phase 1 instead of
re-processing raw data. This avoids encoder/scaler mismatch — if you
fit a new LabelEncoder on test data, categories get different integer
mappings and the model produces garbage predictions.

YOUR TASKS:
1. Implement load_test_data() to load the feature-engineered data
2. Implement stream_connections() as a generator that yields batches
3. Add timing between batches to simulate realistic traffic

BACKGROUND — Python Generators:
    A generator is a special function that uses 'yield' instead of 'return'.
    When you call next() on it, it runs until it hits 'yield', hands you
    the value, then *pauses*. The next call to next() resumes from where
    it left off. This lets you process huge datasets piece by piece
    without loading everything into memory at once.

    Example:
        def count_up(n):
            for i in range(n):
                yield i          # pauses here each iteration

        gen = count_up(3)
        print(next(gen))  # 0
        print(next(gen))  # 1
        print(next(gen))  # 2

    Learn more: https://docs.python.org/3/howto/functional.html#generators
"""

import pandas as pd
import numpy as np
import time
from pathlib import Path

PHASE1_DIR = Path(__file__).resolve().parent.parent.parent / 'phase-1-data-engineering'
LABEL_COLUMNS = ['label', 'attack_category', 'is_attack']


def load_test_data():
    """
    Load the feature-engineered dataset from Phase 1.

    We use the already-processed data to avoid re-fitting encoders/scalers.
    The Parquet file preserves data types and is fast to read.

    Steps:
    1. Build the path to Phase 1's Parquet file using PHASE1_DIR
       (fall back to the CSV if Parquet doesn't exist)
    2. Load the DataFrame
    3. Separate features (X) from labels:
       - X = all columns EXCEPT LABEL_COLUMNS
       - y = the 'is_attack' column
    4. Print the shape and class distribution
    5. Return (X, y, full_df)

    Returns:
        tuple: (X features DataFrame, y true labels Series, raw DataFrame)
    """
    # TODO: Implement this function
    pass


def stream_connections(X, y, batch_size=10, delay=1.0):
    """
    Generator that yields batches of connections, simulating real-time traffic.

    This is a Python generator — it uses 'yield' instead of 'return'.
    See the module docstring above for an explanation of how generators work.

    Steps:
    1. Calculate the total number of batches
    2. Loop through the dataset in chunks of batch_size:
       a. Slice X and y for the current batch
       b. yield (X_batch, y_batch, batch_number)
       c. Sleep for 'delay' seconds between batches (simulates real-time)
       d. Print a status update every 10 batches
    3. After the loop, the generator is exhausted — no more data

    Args:
        X (pd.DataFrame): Feature matrix
        y (pd.Series): True labels
        batch_size (int): Number of connections per batch
        delay (float): Seconds to sleep between batches

    Yields:
        tuple: (X_batch DataFrame, y_batch Series, batch_number int)
    """
    # TODO: Implement this function
    pass


if __name__ == '__main__':
    print("Loading test data from Phase 1...")
    X, y, df = load_test_data()
    print(f"\nStreaming first 5 batches:")
    for X_batch, y_batch, batch_num in stream_connections(X, y, batch_size=10, delay=0.5):
        threats = y_batch.sum()
        print(f"  Batch {batch_num}: {len(X_batch)} connections, {threats} threats")
        if batch_num >= 5:
            break
