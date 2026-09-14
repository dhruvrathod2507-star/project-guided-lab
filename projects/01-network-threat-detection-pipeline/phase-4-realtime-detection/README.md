# Phase 4: Real-Time Threat Detection

**Duration:** 1.5 weeks
**Objective:** Build a system that simulates incoming network traffic, classifies each connection using your trained ML model, and raises alerts for detected threats.

**Prerequisite:** Complete Phase 3 (trained and saved model).

---

## What You Will Learn

- Loading and using saved ML models in production-like settings
- Simulating streaming data from batch datasets
- Building a real-time classification engine
- Implementing alert/notification logic
- Structured logging for security events
- Thinking about detection speed vs. accuracy tradeoffs

---

## Real-World Context

In a real Security Operations Center (SOC):
- Network traffic flows in continuously (millions of packets per second)
- An Intrusion Detection System (IDS) analyzes each connection in real-time
- Suspicious connections trigger alerts for human analysts to review
- Speed matters — a slow detector lets attacks through

You will build a simplified version of this pipeline.

---

## Step-by-Step Guide

### Step 1: Set Up

```
phase-4-realtime-detection/
├── src/
│   ├── simulator.py       <- Simulates streaming network traffic
│   ├── detector.py        <- Loads model and classifies connections
│   ├── alerter.py         <- Handles threat alerts
│   └── monitor.py         <- Main loop: simulate → detect → alert
├── logs/                  <- Detection logs
└── config.py              <- Configuration settings
```

```bash
mkdir -p src logs
```

### Step 2: Configuration (`config.py`)

```python
"""
Configuration for the real-time detection system.

TODO: Review and customize these settings.
"""

import os

# Path to your trained model from Phase 3
MODEL_PATH = '../phase-3-ai-ml-model/models/best_random_forest.joblib'

# Path to test data (simulates incoming traffic)
TEST_DATA_PATH = '../phase-1-data-engineering/data/raw/KDDTest+.txt'

# Detection settings
ALERT_THRESHOLD = 0.5       # Probability threshold to flag as attack
BATCH_SIZE = 10             # Number of connections to process per tick
TICK_INTERVAL = 1.0         # Seconds between batches (simulates real-time)

# Logging
LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'detections.log')
ALERT_LOG = os.path.join(LOG_DIR, 'alerts.log')
```

### Step 3: Traffic Simulator (`src/simulator.py`)

**TODO:** Simulate incoming network connections by streaming from the test dataset.

```python
"""
Network Traffic Simulator
=========================
Reads the test dataset and yields records one-by-one (or in batches)
to simulate real-time network traffic arriving at the detector.

YOUR TASKS:
1. Implement load_test_data() to load and preprocess the test set
2. Implement stream_connections() as a generator that yields batches
3. Add random delays to simulate realistic traffic patterns
"""

import pandas as pd
import numpy as np
import time


def load_test_data(filepath):
    """
    Load and preprocess the test dataset.

    This must apply the SAME preprocessing as Phase 1:
    - Load with correct column names
    - Clean the data
    - Engineer features
    - Return the preprocessed DataFrame

    IMPORTANT: The test data must be transformed identically to training data.
    If you used LabelEncoder in Phase 1, use the SAME encoder here.

    Returns:
        tuple: (X_features DataFrame, y_true labels, raw_df for display)
    """
    # TODO: Implement
    pass


def stream_connections(X, y, batch_size=10, delay=1.0):
    """
    Generator that yields batches of connections, simulating real-time traffic.

    This is a Python generator (uses 'yield' instead of 'return').
    Each call to next() gives the next batch of connections.

    Steps:
    1. Iterate through the dataset in chunks of batch_size
    2. For each chunk, yield (X_batch, y_true_batch, batch_index)
    3. Sleep for 'delay' seconds between batches (simulates real-time)
    4. Print a status update every 10 batches

    Yields:
        tuple: (X_batch, y_true_batch, batch_number)
    """
    # TODO: Implement
    pass
```

### Step 4: Threat Detector (`src/detector.py`)

**TODO:** Load the trained model and classify connections.

```python
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


def load_model(model_path):
    """
    Load the trained model from disk.

    Steps:
    1. Use joblib.load() to load the model
    2. Print model type and configuration
    3. Return the model

    Returns:
        trained sklearn model
    """
    # TODO: Implement
    pass


def classify(model, X_batch):
    """
    Classify a batch of network connections.

    Steps:
    1. Use model.predict() to get class labels (0 or 1)
    2. Use model.predict_proba() to get confidence scores
    3. Return both predictions and probabilities

    Returns:
        tuple: (predictions array, probabilities array)
    """
    # TODO: Implement
    pass


def get_threat_level(probability):
    """
    Map prediction probability to a human-readable threat level.

    Levels:
    - probability < 0.3:  "LOW"    (likely normal)
    - probability < 0.6:  "MEDIUM" (suspicious)
    - probability < 0.85: "HIGH"   (likely attack)
    - probability >= 0.85: "CRITICAL" (almost certain attack)

    Returns:
        str: threat level
    """
    # TODO: Implement
    pass
```

### Step 5: Alert System (`src/alerter.py`)

**TODO:** Generate and log alerts for detected threats.

```python
"""
Alert System
============
Generates alerts when threats are detected and logs them.

YOUR TASKS:
1. Implement format_alert() to create a structured alert message
2. Implement log_alert() to write alerts to a log file
3. Implement print_alert() for console output with color coding
4. Implement AlertManager class to track alert statistics
"""

import json
import os
from datetime import datetime


class AlertManager:
    """
    Manages threat alerts — formats, logs, and tracks statistics.

    TODO: Implement all methods below.
    """

    def __init__(self, log_dir='logs'):
        """
        Initialize the alert manager.

        Create:
        - self.alerts: list to store all alerts
        - self.stats: dict to count alerts by threat level
        - self.log_file: path to the alert log file
        """
        # TODO: Implement
        pass

    def create_alert(self, batch_num, connection_index, prediction, probability, threat_level):
        """
        Create a structured alert dictionary.

        Alert should include:
        - timestamp (current datetime as ISO string)
        - alert_id (auto-incrementing)
        - batch_number
        - connection_index
        - prediction (0 or 1)
        - probability (float)
        - threat_level (LOW/MEDIUM/HIGH/CRITICAL)

        Returns:
            dict: structured alert
        """
        # TODO: Implement
        pass

    def log_alert(self, alert):
        """
        Write alert to the log file as a JSON line.

        Each alert is one line of JSON in the log file.
        This format (JSON Lines) is easy to parse programmatically.
        """
        # TODO: Implement
        pass

    def print_alert(self, alert):
        """
        Print alert to console with color-coded threat level.

        Colors (ANSI codes):
        - LOW:      green  (\\033[92m)
        - MEDIUM:   yellow (\\033[93m)
        - HIGH:     red    (\\033[91m)
        - CRITICAL: red bold (\\033[1;91m)
        - Reset:    \\033[0m

        Format:
        [TIMESTAMP] [THREAT_LEVEL] Alert #ID — Connection #INDEX flagged
        (probability: X.XX%)
        """
        # TODO: Implement
        pass

    def get_summary(self):
        """
        Return a summary of all alerts generated.

        Returns:
            dict: {total_alerts, alerts_by_level, detection_rate}
        """
        # TODO: Implement
        pass
```

### Step 6: Main Monitor Loop (`src/monitor.py`)

**TODO:** Tie everything together into a running detection system.

```python
"""
Real-Time Monitor
=================
Main loop that simulates, detects, and alerts.

YOUR TASKS:
1. Initialize all components (simulator, detector, alerter)
2. Run the detection loop
3. Print real-time statistics
4. Generate a final report
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulator import load_test_data, stream_connections
from detector import load_model, classify, get_threat_level
from alerter import AlertManager
from config import MODEL_PATH, TEST_DATA_PATH, BATCH_SIZE, TICK_INTERVAL


def run_monitor(max_batches=100):
    """
    Run the real-time threat detection monitor.

    Steps:
    1. Load the trained model
    2. Load and preprocess test data
    3. Initialize the AlertManager
    4. For each batch from the stream:
       a. Classify all connections in the batch
       b. For each connection predicted as attack:
          - Get the threat level
          - Create and log an alert
       c. Print batch summary (connections processed, threats found)
    5. After all batches, print final statistics

    Expected console output:
    ─────────────────────────────────────────
     REAL-TIME NETWORK THREAT MONITOR
     Press Ctrl+C to stop
    ─────────────────────────────────────────
    [Batch 001] Processed 10 connections | Threats: 3 | Normal: 7
    [Batch 002] Processed 10 connections | Threats: 5 | Normal: 5
    ...
    ─────────────────────────────────────────
     FINAL REPORT
     Total connections analyzed: 1000
     Threats detected: 423 (42.3%)
     Alerts by level: CRITICAL: 89, HIGH: 134, MEDIUM: 112, LOW: 88
     True detection rate: 94.2% (compared to actual labels)
    ─────────────────────────────────────────
    """
    # TODO: Implement
    pass


if __name__ == '__main__':
    run_monitor()
```

---

## Checkpoint: How to Know You're Done

- [ ] `python src/monitor.py` runs and processes test data in batches
- [ ] Threats are detected and classified by severity level
- [ ] Alerts are printed to console with color coding
- [ ] Alerts are logged to `logs/alerts.log` as JSON Lines
- [ ] Final report shows detection statistics
- [ ] True detection rate is printed (comparing predictions to actual labels)

---

## Bonus Challenges

1. **Speed benchmark:** How many connections per second can your system process? Print a throughput metric.
2. **Sliding window:** Instead of fixed batches, implement a time-based sliding window.
3. **Email/Slack alert:** Send a notification when a CRITICAL threat is detected (use a mock/print for the assignment).

---

## Next Phase

**[Phase 5: Dashboard & Reporting →](../phase-5-dashboard-reporting/)**
