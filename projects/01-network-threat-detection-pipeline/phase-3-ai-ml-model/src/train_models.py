"""
Model Training Module
=====================
Train multiple ML models for network intrusion detection.

YOUR TASKS:
1. Implement prepare_data() to split features and labels
2. Implement train_logistic_regression()
3. Implement train_decision_tree()
4. Implement train_random_forest()
5. Implement evaluate_model() to compute metrics
6. Implement compare_models() to rank all models
7. Save the best model to the models/ directory
"""

import pandas as pd
import numpy as np
import os
import time
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

import matplotlib.pyplot as plt
import seaborn as sns


LABEL_COLUMNS = ['label', 'attack_category', 'is_attack']
RESULTS_DIR = 'results'
MODELS_DIR = 'models'

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)


def prepare_data(df):
    """
    Split DataFrame into features (X) and label (y), then into train/test sets.

    Steps:
    1. X = all columns except LABEL_COLUMNS (drop them)
    2. y = df['is_attack']
    3. Split 80/20 with stratify=y and random_state=42
    4. Print shapes and class distributions

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # TODO: Implement
    pass


def train_logistic_regression(X_train, y_train):
    """
    Train a Logistic Regression baseline model.

    Config: max_iter=1000, random_state=42

    Returns:
        trained model
    """
    # TODO: Implement
    pass


def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree classifier.

    Config: max_depth=10, random_state=42

    Returns:
        trained model
    """
    # TODO: Implement
    pass


def train_random_forest(X_train, y_train):
    """
    Train a Random Forest classifier.

    Config: n_estimators=100, max_depth=15, random_state=42, n_jobs=-1

    Returns:
        trained model
    """
    # TODO: Implement
    pass


def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a model and generate metrics + confusion matrix plot.

    Steps:
    1. Predict on X_test
    2. Calculate accuracy, precision, recall, f1
    3. Print classification report
    4. Plot and save confusion matrix
    5. Return dict of metrics

    Returns:
        dict: {accuracy, precision, recall, f1}
    """
    # TODO: Implement
    pass


def plot_feature_importance(model, feature_names, top_n=20):
    """
    Plot top N most important features from a tree-based model.

    Save to results/feature_importance.png
    """
    # TODO: Implement
    pass


def compare_models(results):
    """
    Create a comparison table and bar chart of all models.

    Args:
        results: dict of {model_name: {accuracy, precision, recall, f1}}
    """
    # TODO: Implement
    pass


def save_best_model(model, name):
    """
    Save the trained model using joblib.

    Args:
        model: trained sklearn model
        name: filename (e.g., 'best_random_forest.joblib')
    """
    # TODO: Implement
    pass


if __name__ == '__main__':
    print("=" * 60)
    print("  NETWORK THREAT DETECTION — MODEL TRAINING")
    print("=" * 60)

    # Load data
    data_path = '../phase-1-data-engineering/data/features/train_features.parquet'
    if not os.path.exists(data_path):
        data_path = '../phase-1-data-engineering/data/processed/train_clean.csv'

    print(f"\nLoading data from: {data_path}")
    df = pd.read_parquet(data_path) if data_path.endswith('.parquet') else pd.read_csv(data_path)
    print(f"Loaded: {df.shape}")

    # Prepare
    X_train, X_test, y_train, y_test = prepare_data(df)

    # Train models
    models = {}

    print("\n[1/3] Training Logistic Regression...")
    start = time.time()
    models['Logistic Regression'] = train_logistic_regression(X_train, y_train)
    print(f"       Done in {time.time() - start:.1f}s")

    print("\n[2/3] Training Decision Tree...")
    start = time.time()
    models['Decision Tree'] = train_decision_tree(X_train, y_train)
    print(f"       Done in {time.time() - start:.1f}s")

    print("\n[3/3] Training Random Forest...")
    start = time.time()
    models['Random Forest'] = train_random_forest(X_train, y_train)
    print(f"       Done in {time.time() - start:.1f}s")

    # Evaluate all models
    print("\n" + "=" * 60)
    print("  EVALUATION RESULTS")
    print("=" * 60)

    results = {}
    for name, model in models.items():
        print(f"\n--- {name} ---")
        results[name] = evaluate_model(model, X_test, y_test, name)

    # Compare
    compare_models(results)

    # Feature importance for best tree model
    print("\nGenerating feature importance plot...")
    feature_names = [c for c in df.columns if c not in LABEL_COLUMNS]
    plot_feature_importance(models['Random Forest'], feature_names)

    # Save best model
    print("\nSaving best model...")
    save_best_model(models['Random Forest'], 'best_random_forest.joblib')

    print("\nDone! Check the 'results/' and 'models/' directories.")
