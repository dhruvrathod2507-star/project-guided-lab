"""
Real-Time Monitor
=================
Main loop that ties everything together: simulate → detect → alert.

YOUR TASKS:
1. Initialize all components (simulator, detector, alerter)
2. Run the detection loop over batches
3. Print real-time statistics per batch
4. Generate a final report with detection accuracy
"""

import sys
from pathlib import Path

# Add parent directory (phase-4-realtime-detection/) to the path so we can
# import config.py, and add the current directory for sibling module imports.
_PHASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PHASE_DIR))
sys.path.insert(0, str(_PHASE_DIR / 'src'))

from simulator import load_test_data, stream_connections
from detector import load_model, classify, get_threat_level
from alerter import AlertManager
from config import MODEL_PATH, ALERT_THRESHOLD, BATCH_SIZE, TICK_INTERVAL


def run_monitor(max_batches=100):
    """
    Run the real-time threat detection monitor.

    Steps:
    1. Load the trained model using load_model(MODEL_PATH)
    2. Load test data using load_test_data()
    3. Create an AlertManager instance
    4. For each batch from stream_connections():
       a. Classify all connections using classify()
       b. For each connection where attack probability > ALERT_THRESHOLD:
          - Determine the threat level with get_threat_level()
          - Create an alert with alert_manager.create_alert()
          - Log and print the alert
       c. Update alert_manager.total_processed
       d. Print batch summary: connections processed, threats found, normal
       e. Stop after max_batches
    5. Print final report: total analyzed, threats detected, alerts by level,
       and true detection rate (compare predictions to actual y labels)

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

    Args:
        max_batches (int): Maximum number of batches to process before stopping
    """
    # TODO: Implement this function
    pass


if __name__ == '__main__':
    run_monitor()
