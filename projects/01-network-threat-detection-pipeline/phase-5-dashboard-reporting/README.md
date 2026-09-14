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

Starter code files are provided — open them and implement the TODO sections.

### Step 2: Data Loader (`utils/data_loader.py`)

**TODO:** Open the provided `utils/data_loader.py` and implement the TODO functions.

All file paths in the starter code use `pathlib.Path(__file__).resolve()` to build
paths relative to the file location — this means `streamlit run app.py` works
regardless of which directory you run it from.

### Step 3: Main App (`app.py`)

**TODO:** The provided `app.py` already has a working skeleton. Open it and add the sidebar TODO items.

### Step 4: Overview Page (`pages/1_overview.py`)

**TODO:** Open the provided `pages/1_overview.py` and implement the KPI dashboard.

Key Streamlit features to use:
- `st.columns(4)` + `st.metric()` — for the KPI row
- `st.bar_chart()` — for attack category breakdown
- `st.dataframe()` — for the recent alerts table

### Step 5: Live Monitor Page (`pages/2_live_monitor.py`)

**TODO:** Open the provided `pages/2_live_monitor.py` and implement the live feed.

Key Streamlit features to use:
- `st.button()` — start/stop controls
- `st.empty()` — placeholder containers that update in-place
- `st.status()` — live status indicator
- `time.sleep()` — brief delay for visual effect between batches

### Step 6: Analysis Page (`pages/3_analysis.py`)

**TODO:** Open the provided `pages/3_analysis.py` and implement the analysis visualizations.

Key features to implement:
- `st.selectbox()` — filter by attack category
- Feature importance chart (from Phase 3 model)
- Interactive scatter plot (user picks X/Y features)
- Confusion matrix heatmap
- Per-category statistics table

### Step 7: Reports Page (`pages/4_reports.py`)

**TODO:** Open the provided `pages/4_reports.py` and implement the report generator.

Key features to implement:
- `st.selectbox()` — select report type (Daily Summary, Threat Analysis, Model Performance)
- `st.text_area()` — preview the generated report
- `st.download_button()` — download as `.txt` file

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
