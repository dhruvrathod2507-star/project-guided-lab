"""
Exploratory Data Analysis — Starter Code
=========================================
Use this as a reference for building your EDA Jupyter notebook.
Each function produces one analysis or visualization.

YOUR TASKS:
1. Implement each function
2. Call them from your Jupyter notebook (or run this script directly)
3. Save all generated plots to a 'plots/' directory
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

PLOT_DIR = 'plots'
os.makedirs(PLOT_DIR, exist_ok=True)

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12


def load_cleaned_data():
    """
    Load the cleaned (pre-encoded) data from Phase 1.

    IMPORTANT: We load the CSV (pre-encoding), NOT the Parquet (post-encoding).
    The Parquet file has categorical columns label-encoded to integers
    (e.g., protocol_type: tcp=2, udp=1, icmp=0) which makes categorical
    analysis like "What percentage uses TCP vs UDP?" impossible to interpret.
    """
    csv_path = '../phase-1-data-engineering/data/processed/train_clean.csv'

    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        raise FileNotFoundError(
            "No cleaned data found at '{}'. Complete Phase 1 first.".format(csv_path)
        )


def plot_attack_distribution(df):
    """
    Create a bar chart showing count of each attack category.

    TODO:
    1. Count records per attack_category
    2. Create a bar chart with counts on y-axis, categories on x-axis
    3. Annotate each bar with the exact count
    4. Use green for Normal, red shades for attacks
    5. Save to plots/attack_distribution.png
    """
    # TODO: Implement
    pass


def plot_binary_distribution(df):
    """
    Create a pie chart of Normal vs Attack traffic.

    TODO:
    1. Count normal vs attack using the 'is_attack' column
    2. Create a pie chart with percentages
    3. Save to plots/binary_distribution.png
    """
    # TODO: Implement
    pass


def plot_protocol_distribution(df):
    """
    Show protocol usage across attack categories.

    TODO:
    1. Create a grouped/stacked bar chart
    2. x-axis: attack categories, bars: protocol types
    3. Save to plots/protocol_by_attack.png
    """
    # TODO: Implement
    pass


def plot_feature_comparison(df):
    """
    Box plots comparing key features across attack categories.

    TODO:
    1. Create box plots for: duration, src_bytes, dst_bytes
    2. Group by attack_category
    3. Use log scale if values vary widely
    4. Save to plots/feature_comparison.png
    """
    # TODO: Implement
    pass


def plot_correlation_heatmap(df):
    """
    Create a correlation heatmap of numeric features.

    TODO:
    1. Select only numeric columns
    2. Compute the correlation matrix
    3. Create a heatmap using seaborn
    4. Save to plots/correlation_heatmap.png
    """
    # TODO: Implement
    pass


def find_top_correlated_features(df, threshold=0.9):
    """
    Find pairs of features with correlation above the threshold.

    TODO:
    1. Compute correlation matrix
    2. Find pairs where abs(correlation) > threshold
    3. Exclude self-correlations (feature with itself)
    4. Print and return the list of pairs

    Returns:
        list of tuples: (feature1, feature2, correlation_value)
    """
    # TODO: Implement
    pass


def plot_error_rates(df):
    """
    Compare error rates across attack categories.

    TODO:
    1. Group by attack_category
    2. Calculate mean serror_rate and rerror_rate per category
    3. Create a grouped bar chart
    4. Save to plots/error_rates.png
    """
    # TODO: Implement
    pass


def generate_summary_stats(df):
    """
    Print a summary of key statistics.

    TODO:
    1. Total records, feature count
    2. Class distribution (counts and percentages)
    3. Top 5 features correlated with is_attack
    4. Most targeted services per attack category
    """
    # TODO: Implement
    pass


if __name__ == '__main__':
    print("Loading cleaned data from Phase 1...")
    df = load_cleaned_data()
    print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

    print("Generating visualizations...")
    plot_attack_distribution(df)
    plot_binary_distribution(df)
    plot_protocol_distribution(df)
    plot_feature_comparison(df)
    plot_correlation_heatmap(df)
    plot_error_rates(df)

    print("\nFinding highly correlated features...")
    find_top_correlated_features(df)

    print("\nGenerating summary statistics...")
    generate_summary_stats(df)

    print(f"\nAll plots saved to '{PLOT_DIR}/' directory.")
