"""
Configuration for the real-time detection system.
Customize these settings for your environment.
"""

import os

MODEL_PATH = '../phase-3-ai-ml-model/models/best_random_forest.joblib'

TEST_DATA_PATH = '../phase-1-data-engineering/data/raw/KDDTest+.txt'

ALERT_THRESHOLD = 0.5
BATCH_SIZE = 10
TICK_INTERVAL = 1.0

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'detections.log')
ALERT_LOG = os.path.join(LOG_DIR, 'alerts.log')

os.makedirs(LOG_DIR, exist_ok=True)
