"""
Overview Dashboard
==================
Shows high-level threat statistics and KPIs.

YOUR TASKS:
1. Display KPI metrics in a row (total connections, threats detected, detection rate, etc.)
2. Create a time-series chart of threats over time (simulated)
3. Show attack category breakdown as a donut chart
4. Display a table of recent alerts
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import sys

_UTILS_DIR = str(Path(__file__).resolve().parent.parent / 'utils')
if _UTILS_DIR not in sys.path:
    sys.path.insert(0, _UTILS_DIR)

from data_loader import load_processed_data, load_detection_logs

st.header("Threat Overview")

# TODO: Load data
# df = load_processed_data()
# alerts = load_detection_logs()

# TODO: KPI Row — use st.columns() and st.metric()
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Connections", "125,973")
# col2.metric("Threats Detected", "58,630", delta="-2.1%")
# col3.metric("Detection Rate", "97.2%")
# col4.metric("Active Alerts", "23", delta="5")

# TODO: Attack Category Breakdown — use st.bar_chart() or plotly
# Show count of each attack category

# TODO: Recent Alerts Table — use st.dataframe()
# Show the most recent 20 alerts from the log
