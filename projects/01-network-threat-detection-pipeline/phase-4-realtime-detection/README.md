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

Starter code files are provided in `src/` — open them and implement the TODO sections.

```bash
mkdir -p logs
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

Open the provided `src/simulator.py` starter code and implement the TODO functions.

**Key design decision:** Instead of re-processing raw `KDDTest+.txt` (which would require
saving and reloading LabelEncoders from Phase 1), the simulator loads the **already-processed
Parquet file** from Phase 1. This avoids encoder mismatch issues where test data gets different
integer encodings than training data.

**New concept — Python Generators:**

The `stream_connections()` function uses `yield` instead of `return`. This makes it a
*generator* — a function that produces values one at a time instead of all at once.

```python
# Normal function — returns everything at once (uses lots of memory)
def get_all():
    return [1, 2, 3, 4, 5]

# Generator — produces one value at a time (memory efficient)
def stream():
    for i in [1, 2, 3, 4, 5]:
        yield i  # pauses here, resumes on next call

# Usage:
for value in stream():
    print(value)  # prints 1, then 2, then 3...
```

This is essential for real-time systems — you can't load millions of network packets into
memory at once. Generators let you process them one batch at a time.

> New to generators? Read the [Python docs on generators](https://docs.python.org/3/howto/functional.html#generators).

### Step 4: Threat Detector (`src/detector.py`)

**TODO:** Open the provided `src/detector.py` and implement the TODO functions.

Key functions to implement:
- `load_model(model_path)` — Load the trained model using `joblib.load()`
- `classify(model, X_batch)` — Run `model.predict()` and `model.predict_proba()`
- `get_threat_level(probability)` — Map probability to LOW/MEDIUM/HIGH/CRITICAL

### Step 5: Alert System (`src/alerter.py`)

**TODO:** Open the provided `src/alerter.py` and implement the TODO methods.

Key class to implement: `AlertManager` with methods:
- `create_alert()` — Create a structured alert dict with timestamp, ID, threat level
- `log_alert()` — Write alert as JSON line to the log file
- `print_alert()` — Print color-coded alert to console (uses ANSI color codes)
- `get_summary()` — Return alert statistics

### Step 6: Main Monitor Loop (`src/monitor.py`)

**TODO:** Open the provided `src/monitor.py` and implement the `run_monitor()` function.

This ties everything together:
1. Load the trained model
2. Load and preprocess test data
3. Initialize the AlertManager
4. Loop through batches from the stream:
   - Classify each connection
   - Only raise an alert if the attack probability exceeds `ALERT_THRESHOLD` (from config)
   - Log and print alerts for detected threats
5. Print final statistics

**Expected output:**
```
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
