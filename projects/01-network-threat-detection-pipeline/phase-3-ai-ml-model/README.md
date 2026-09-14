# Phase 3: AI/ML Model Training

**Duration:** 2 weeks
**Objective:** Train machine learning models to classify network traffic as normal or malicious, evaluate their performance, and select the best model.

**Prerequisite:** Complete Phase 1 (cleaned data) and Phase 2 (understanding of the data).

---

## What You Will Learn

- Preparing data for machine learning
- Training classification models (Logistic Regression, Decision Tree, Random Forest)
- Evaluating ML models (accuracy, precision, recall, F1-score, confusion matrix)
- Hyperparameter tuning with Grid Search
- Saving and loading trained models
- Understanding model performance in a cybersecurity context

---

## Why These Metrics Matter in Cyber Security

In intrusion detection, not all errors are equal:

| Metric | Meaning | Cyber Security Impact |
|--------|---------|----------------------|
| **Precision** | Of all predicted attacks, how many were real? | Low precision = too many false alarms, analysts waste time |
| **Recall** | Of all real attacks, how many did we catch? | Low recall = missed attacks, breaches go undetected |
| **F1-Score** | Balance of precision and recall | Best single metric for IDS performance |

**In security, recall is usually more important than precision** — it's better to investigate a false alarm than to miss a real attack.

---

## Step-by-Step Guide

### Step 1: Set Up

```
phase-3-ai-ml-model/
├── src/
│   ├── prepare_data.py    <- Split and prepare data for ML
│   ├── train_models.py    <- Train multiple models
│   ├── evaluate.py        <- Evaluate and compare models
│   └── tune.py            <- Hyperparameter tuning
├── models/                <- Saved trained models
├── results/               <- Evaluation reports and plots
└── notebooks/
    └── 03_model_training.ipynb
```

```bash
mkdir -p src models results notebooks
```

### Step 2: Prepare Data for ML (`src/prepare_data.py`)

**TODO:** Split data into features (X) and labels (y), then into train/test sets.

```python
# What you need to implement:

def prepare_data(df):
    """
    Prepare the DataFrame for ML training.

    Steps:
    1. Separate features (X) from labels (y)
       - X = all columns EXCEPT 'label', 'attack_category', 'is_attack'
       - y = 'is_attack' column (binary: 0 or 1)
    2. Split into training and test sets (80/20 split)
       - Use sklearn.model_selection.train_test_split
       - Set random_state=42 for reproducibility
       - Use stratify=y to maintain class balance
    3. Print the shapes and class distribution of each split
    4. Return X_train, X_test, y_train, y_test
    """
    pass
```

**Key concept: Stratified Split**
- Without stratification, rare attack types (U2R, R2L) might end up entirely in one split
- `stratify=y` ensures both train and test have the same class ratio

### Step 3: Train Multiple Models (`src/train_models.py`)

**TODO:** Train 3 different models and compare their performance.

#### Model 1: Logistic Regression (Baseline)

```python
from sklearn.linear_model import LogisticRegression

def train_logistic_regression(X_train, y_train):
    """
    Train a Logistic Regression model.

    This is your BASELINE model — simple but interpretable.
    All other models should beat this.

    Steps:
    1. Create LogisticRegression(max_iter=1000, random_state=42)
    2. Fit on training data
    3. Print training accuracy
    4. Return the trained model
    """
    # TODO: Implement
    pass
```

#### Model 2: Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier

def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree classifier.

    Decision Trees are great for cybersecurity because:
    - They produce interpretable rules ("IF src_bytes > 1000 AND serror_rate > 0.5 THEN attack")
    - They handle both numeric and categorical features
    - They capture non-linear patterns

    Steps:
    1. Create DecisionTreeClassifier(max_depth=10, random_state=42)
    2. Fit on training data
    3. Print training accuracy
    4. Return the trained model
    """
    # TODO: Implement
    pass
```

#### Model 3: Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):
    """
    Train a Random Forest classifier.

    Random Forest = many Decision Trees voting together.
    Usually the best performer for tabular security data.

    Steps:
    1. Create RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
    2. Fit on training data
    3. Print training accuracy
    4. Return the trained model
    """
    # TODO: Implement
    pass
```

### Step 4: Evaluate Models (`src/evaluate.py`)

**TODO:** Compare all models using multiple metrics.

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a trained model on the test set.

    Steps:
    1. Generate predictions: y_pred = model.predict(X_test)
    2. Calculate metrics:
       - Accuracy
       - Precision (weighted average)
       - Recall (weighted average)
       - F1-score (weighted average)
    3. Print the full classification report
    4. Generate and plot the confusion matrix
    5. Save the confusion matrix plot to results/
    6. Return a dict of all metrics

    Returns:
        dict: {'accuracy': ..., 'precision': ..., 'recall': ..., 'f1': ...}
    """
    # TODO: Implement
    pass


def plot_confusion_matrix(y_test, y_pred, model_name):
    """
    Create a visual confusion matrix.

    TODO:
    1. Compute confusion matrix
    2. Plot as a heatmap with annotations
    3. Label axes: "Predicted" and "Actual"
    4. Show: True Negatives, False Positives, False Negatives, True Positives
    5. Save to results/{model_name}_confusion_matrix.png
    """
    # TODO: Implement
    pass


def compare_models(results_dict):
    """
    Create a comparison table and bar chart of all models.

    TODO:
    1. Create a DataFrame from the results dictionary
    2. Print a formatted comparison table
    3. Create a grouped bar chart comparing all metrics across models
    4. Highlight the best model for each metric
    5. Save to results/model_comparison.png

    Args:
        results_dict: {'ModelName': {'accuracy': ..., 'precision': ..., ...}, ...}
    """
    # TODO: Implement
    pass
```

### Step 5: Feature Importance (`src/evaluate.py`)

**TODO:** Find which features matter most for detection.

```python
def plot_feature_importance(model, feature_names, top_n=20):
    """
    Plot the most important features from a tree-based model.

    Why this matters in cybersecurity:
    - Tells analysts which network features to monitor
    - Helps optimize real-time detection (fewer features = faster)
    - Validates security intuition (are the right features important?)

    Steps:
    1. Get feature importances from model.feature_importances_
    2. Sort by importance (descending)
    3. Plot top N features as a horizontal bar chart
    4. Save to results/feature_importance.png
    """
    # TODO: Implement
    pass
```

### Step 6: Hyperparameter Tuning (`src/tune.py`)

**TODO:** Optimize the best model's parameters.

```python
from sklearn.model_selection import GridSearchCV

def tune_random_forest(X_train, y_train):
    """
    Use Grid Search to find the best hyperparameters for Random Forest.

    Parameter grid to search:
    - n_estimators: [50, 100, 200]
    - max_depth: [10, 15, 20, None]
    - min_samples_split: [2, 5, 10]

    Steps:
    1. Define the parameter grid
    2. Create GridSearchCV with:
       - cv=5 (5-fold cross-validation)
       - scoring='f1_weighted' (optimize for F1-score)
       - n_jobs=-1 (use all CPU cores)
    3. Fit on training data
    4. Print best parameters and best score
    5. Return the best model

    Note: This will take several minutes to run. That's normal.
    """
    # TODO: Implement
    pass
```

### Step 7: Save the Best Model

```python
import joblib

def save_model(model, filepath):
    """
    Save a trained model to disk using joblib.

    TODO:
    1. Save using joblib.dump(model, filepath)
    2. Print the file size
    3. Verify by loading it back and checking predictions match
    """
    # TODO: Implement
    pass

# Save your best model
# save_model(best_model, 'models/best_random_forest.joblib')
```

---

## Checkpoint: How to Know You're Done

- [ ] At least 3 models trained (Logistic Regression, Decision Tree, Random Forest)
- [ ] Each model evaluated with accuracy, precision, recall, F1-score
- [ ] Confusion matrices generated for all models
- [ ] Model comparison table and chart created
- [ ] Feature importance analysis completed
- [ ] Hyperparameter tuning attempted for best model
- [ ] Best model saved to `models/` directory
- [ ] You can explain why one model outperforms others

---

## Expected Results

Approximate performance you should see (may vary slightly):

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | ~89% | ~88% | ~89% | ~88% |
| Decision Tree | ~96% | ~96% | ~96% | ~96% |
| Random Forest | ~97% | ~97% | ~97% | ~97% |

If your numbers are very different, check your data preparation.

---

## Next Phase

**[Phase 4: Real-Time Detection →](../phase-4-realtime-detection/)**
