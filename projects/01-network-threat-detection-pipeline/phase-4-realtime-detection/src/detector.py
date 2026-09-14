"""
Threat Detector
===============
Loads the trained ML model and classifies network connections.

YOUR TASKS:
1. Implement load_model() to load the saved joblib model
2. Implement classify() to predict on a batch of connections
3. Implement get_threat_level() to categorize the severity
"""

import joblib
import numpy as np
from pathlib import Path

DEFAULT_MODEL_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / 'phase-3-ai-ml-model' / 'models' / 'best_random_forest.joblib'
)


def load_model(model_path=None):
    """
    Load the trained model from disk.

    Steps:
    1. Use the provided model_path, or fall back to DEFAULT_MODEL_PATH
    2. Use joblib.load() to load the model
    3. Print model type and key configuration (e.g., n_estimators for RF)
    4. Return the model

    Args:
        model_path (str or Path, optional): Path to the .joblib model file

    Returns:
        trained sklearn model
    """
    # TODO: Implement this function
    pass


def classify(model, X_batch):
    """
    Classify a batch of network connections.

    The model outputs both a binary label (0=normal, 1=attack) and a
    probability score. Use the probability to assign threat levels and
    to compare against ALERT_THRESHOLD from config.py — only connections
    whose attack probability exceeds the threshold should trigger alerts.

    Steps:
    1. Use model.predict(X_batch) to get class labels (0 or 1)
    2. Use model.predict_proba(X_batch) to get probability scores
       - predict_proba returns [[prob_normal, prob_attack], ...]
       - Extract the attack probability (column index 1)
    3. Return both predictions and attack probabilities

    Args:
        model: trained sklearn model
        X_batch (pd.DataFrame or np.ndarray): Feature matrix for the batch

    Returns:
        tuple: (predictions np.ndarray of 0/1, probabilities np.ndarray of floats)
    """
    # TODO: Implement this function
    pass


def get_threat_level(probability):
    """
    Map a single prediction probability to a human-readable threat level.

    Levels:
    - probability < 0.3:   "LOW"      (likely normal traffic)
    - probability < 0.6:   "MEDIUM"   (suspicious, worth watching)
    - probability < 0.85:  "HIGH"     (likely an attack)
    - probability >= 0.85: "CRITICAL" (almost certain attack)

    Args:
        probability (float): Attack probability from predict_proba (0.0 to 1.0)

    Returns:
        str: One of "LOW", "MEDIUM", "HIGH", "CRITICAL"
    """
    # TODO: Implement this function
    pass


if __name__ == '__main__':
    print("Loading model...")
    model = load_model()
    print(f"Model type: {type(model).__name__}")
    print("Detector ready.")
