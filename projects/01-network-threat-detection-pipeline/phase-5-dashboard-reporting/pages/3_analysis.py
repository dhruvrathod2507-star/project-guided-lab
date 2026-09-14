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
from pathlib import Path
import sys

_UTILS_DIR = str(Path(__file__).resolve().parent.parent / 'utils')
if _UTILS_DIR not in sys.path:
    sys.path.insert(0, _UTILS_DIR)

from data_loader import load_processed_data, load_model

st.header("Attack Analysis")

# TODO: Sidebar filters
# selected_category = st.selectbox("Attack Category", ["All", "DoS", "Probe", "R2L", "U2R"])

# TODO: Feature importance chart
# Load from Phase 3 results or recompute from loaded model

# TODO: Interactive scatter plot
# Let users pick X and Y features, color by attack category
# Use st.selectbox() for feature selection

# TODO: Confusion matrix heatmap
# Load model, predict on test set, show confusion matrix

# TODO: Per-category stats table
# For the selected attack category, show:
# - Count, percentage, top features, common services targeted
