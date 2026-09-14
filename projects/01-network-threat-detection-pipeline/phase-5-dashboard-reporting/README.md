# Phase 5: Dashboard & Reporting

**Duration:** 1.5 weeks
**Objective:** Build an interactive web dashboard using Streamlit that visualizes network threats in real-time and generates incident reports.

**Prerequisite:** Complete Phases 1-4.

---

## What You Will Learn

- Building interactive web apps with Streamlit (no HTML/CSS needed)
- Real-time data visualization for security monitoring
- Designing a SOC (Security Operations Center) analyst dashboard
- Automated report generation

---

## What You Will Build

A Streamlit dashboard with 4 pages:

1. **Overview** — High-level threat statistics and KPIs
2. **Live Monitor** — Real-time threat detection feed
3. **Analysis** — Deep-dive into attack patterns and trends
4. **Reports** — Generate and download incident reports

---

## Step-by-Step Guide

### Step 1: Set Up

```
phase-5-dashboard-reporting/
├── app.py                  <- Main Streamlit app
├── pages/
│   ├── 1_overview.py       <- Overview dashboard
│   ├── 2_live_monitor.py   <- Real-time feed
│   ├── 3_analysis.py       <- Attack analysis
│   └── 4_reports.py        <- Report generator
├── utils/
│   ├── data_loader.py      <- Load data from previous phases
│   └── report_generator.py <- Generate PDF/text reports
└── assets/                 <- Images, CSS overrides
```

```bash
mkdir -p pages utils assets
```

### Step 2: Data Loader (`utils/data_loader.py`)

**TODO:** Create functions to load data from all previous phases.

```python
"""
Data Loader for the Dashboard
==============================
Loads processed data, model results, and detection logs.

YOUR TASKS:
1. Implement load_processed_data() — loads cleaned data from Phase 1
2. Implement load_model_results() — loads evaluation metrics from Phase 3
3. Implement load_detection_logs() — loads alert logs from Phase 4
4. Implement load_model() — loads the trained model for live predictions
"""

import pandas as pd
import json
import joblib
import os
import sqlite3


def load_processed_data():
    """
    Load the cleaned and feature-engineered dataset.

    Try Parquet first (faster), fall back to CSV.

    Returns:
        pd.DataFrame
    """
    # TODO: Implement
    pass


def load_detection_logs(log_path='../phase-4-realtime-detection/logs/alerts.log'):
    """
    Load alert logs from Phase 4.

    The log file contains one JSON object per line (JSON Lines format).

    Steps:
    1. Read the file line by line
    2. Parse each line as JSON
    3. Convert to a DataFrame
    4. Parse timestamps as datetime objects

    Returns:
        pd.DataFrame: Alert log entries
    """
    # TODO: Implement
    pass


def load_model():
    """
    Load the trained ML model for live predictions.

    Returns:
        trained sklearn model
    """
    # TODO: Implement
    pass


def get_database_connection():
    """
    Connect to the SQLite database from Phase 1.

    Returns:
        sqlite3.Connection
    """
    # TODO: Implement
    pass
```

### Step 3: Main App (`app.py`)

**TODO:** Create the Streamlit app entry point.

```python
"""
Network Threat Detection Dashboard
====================================
Main Streamlit application.

Run with: streamlit run app.py

YOUR TASKS:
1. Set up the page config (title, icon, layout)
2. Create the sidebar navigation
3. Display a welcome page with project overview
"""

import streamlit as st

# Page config — must be the first Streamlit command
st.set_page_config(
    page_title="Network Threat Monitor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Network Threat Detection Dashboard")

st.markdown("""
Welcome to the **Network Threat Detection Dashboard**.

This dashboard provides real-time monitoring and analysis of network traffic
to detect and visualize cyber security threats.

### Pages

- **Overview** — High-level threat statistics and key performance indicators
- **Live Monitor** — Watch threats being detected in real-time
- **Analysis** — Deep-dive into attack patterns and feature analysis
- **Reports** — Generate and download incident reports

---

*Select a page from the sidebar to get started.*
""")

# TODO: Add sidebar with:
# - System status indicator (model loaded? data available?)
# - Quick stats (total records, total alerts, detection rate)
# - Filter controls (date range, threat level)
```

### Step 4: Overview Page (`pages/1_overview.py`)

**TODO:** Build the main KPI dashboard.

```python
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
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from data_loader import load_processed_data, load_detection_logs

st.header("Threat Overview")

# TODO: Load data
# df = load_processed_data()
# alerts = load_detection_logs()

# TODO: KPI Row — use st.columns() and st.metric()
# Example:
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Connections", "125,973")
# col2.metric("Threats Detected", "58,630", delta="-2.1%")
# col3.metric("Detection Rate", "97.2%")
# col4.metric("Active Alerts", "23", delta="5")

# TODO: Attack Category Breakdown — use st.bar_chart() or plotly
# Show count of each attack category

# TODO: Recent Alerts Table — use st.dataframe()
# Show the most recent 20 alerts from the log
```

### Step 5: Live Monitor Page (`pages/2_live_monitor.py`)

**TODO:** Build a simulated live threat feed.

```python
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
```

### Step 6: Analysis Page (`pages/3_analysis.py`)

**TODO:** Deep-dive into attack patterns.

```python
"""
Attack Analysis
===============
Interactive analysis of attack patterns and model performance.

YOUR TASKS:
1. Feature importance visualization (from Phase 3)
2. Attack category deep-dive (select a category, see its patterns)
3. Confusion matrix display
4. Model performance comparison chart
5. Interactive feature explorer (select features, see distributions)
"""

import streamlit as st
import pandas as pd

st.header("Attack Analysis")

# TODO: Sidebar filters
# selected_category = st.selectbox("Attack Category", ["All", "DoS", "Probe", "R2L", "U2R"])

# TODO: Feature importance chart
# Load from Phase 3 results or recompute

# TODO: Interactive scatter plot
# Let users pick X and Y features, color by attack category
# Use st.selectbox() for feature selection

# TODO: Confusion matrix heatmap
# Load model, predict on test set, show confusion matrix

# TODO: Per-category stats table
# For the selected attack category, show:
# - Count, percentage, top features, common services targeted
```

### Step 7: Reports Page (`pages/4_reports.py`)

**TODO:** Generate downloadable incident reports.

```python
"""
Report Generator
================
Generate and download security incident reports.

YOUR TASKS:
1. Let user select report type (daily summary, incident detail, full analysis)
2. Generate the report as formatted text
3. Provide a download button
"""

import streamlit as st
from datetime import datetime

st.header("Incident Reports")

# TODO: Report type selection
# report_type = st.selectbox("Report Type", [
#     "Daily Summary",
#     "Threat Analysis Report",
#     "Model Performance Report"
# ])

# TODO: Generate report content based on type
# Include:
# - Header with date and report type
# - Executive summary (2-3 sentences)
# - Key statistics
# - Detailed findings
# - Recommendations

# TODO: Display report preview
# st.text_area("Report Preview", report_content, height=400)

# TODO: Download button
# st.download_button(
#     label="Download Report",
#     data=report_content,
#     file_name=f"threat_report_{datetime.now().strftime('%Y%m%d')}.txt",
#     mime="text/plain"
# )
```

### Step 8: Run the Dashboard

```bash
# From the phase-5-dashboard-reporting directory:
streamlit run app.py

# The dashboard will open in your browser at http://localhost:8501
```

---

## Checkpoint: How to Know You're Done

- [ ] `streamlit run app.py` launches without errors
- [ ] Overview page shows KPI metrics and charts
- [ ] Live Monitor page simulates real-time detection
- [ ] Analysis page has interactive visualizations
- [ ] Reports page generates and downloads reports
- [ ] Dashboard loads data from all previous phases
- [ ] All pages are navigable from the sidebar

---

## Bonus Challenges

1. **Dark mode:** Style the dashboard with a dark security-themed look
2. **Map visualization:** If data has IP geolocation, plot attacks on a world map
3. **Email report:** Add a button to email the report (use a mock function)
4. **Auto-refresh:** Make the overview page refresh every 30 seconds

---

## Congratulations!

If you've completed all 5 phases, you've built a full **Network Threat Detection Pipeline** that covers:

- **Data Engineering** — ETL pipeline, data cleaning, storage
- **AI/ML** — Model training, evaluation, tuning
- **Cyber Security** — Intrusion detection, threat analysis, SOC dashboard

This is a portfolio-worthy project that demonstrates real-world skills employers look for in cybersecurity and data engineering roles.
