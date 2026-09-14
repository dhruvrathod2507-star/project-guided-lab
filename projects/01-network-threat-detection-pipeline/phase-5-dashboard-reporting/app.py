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
