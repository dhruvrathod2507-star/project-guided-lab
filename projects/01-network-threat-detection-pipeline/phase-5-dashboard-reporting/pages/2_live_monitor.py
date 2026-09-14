"""
Live Monitor
============
Simulates real-time threat detection with auto-refreshing display.

YOUR TASKS:
1. Load the trained model
2. Stream test data in batches
3. Classify each batch and display results
4. Show a running feed of detections
5. Use st.empty() and time.sleep() for live updates
"""

import streamlit as st
import pandas as pd
import time
from pathlib import Path
import sys

_UTILS_DIR = str(Path(__file__).resolve().parent.parent / 'utils')
if _UTILS_DIR not in sys.path:
    sys.path.insert(0, _UTILS_DIR)

from data_loader import load_model, load_processed_data

st.header("Live Threat Monitor")

# TODO: Add start/stop controls
# started = st.button("Start Monitoring")
# stop = st.button("Stop")

# TODO: Create placeholder containers for live updates
# status_placeholder = st.empty()
# feed_placeholder = st.empty()
# chart_placeholder = st.empty()

# TODO: When started, loop through test data batches:
# 1. Load next batch
# 2. Classify with model
# 3. Update the feed with new detections
# 4. Update the running chart
# 5. Sleep briefly for visual effect

# Hint: Use st.status() for a live status indicator
# Hint: Use st.dataframe() with highlighting for the feed
# Hint: Color-code rows by threat level
