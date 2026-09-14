# Project 01: Network Threat Detection Pipeline

Build an end-to-end pipeline that ingests raw network traffic data, processes it, trains an AI model to classify threats, and visualizes results on a live dashboard — just like a real Security Operations Center (SOC).

---

## What You Will Learn

By completing this project, you will gain hands-on experience in:

- **Data Engineering** — Building ETL pipelines, data cleaning, storage, and transformation
- **AI/ML Engineering** — Training, evaluating, and deploying machine learning models
- **Cyber Security** — Understanding network attacks, intrusion detection, and threat analysis

---

## Project Overview

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Phase 1   │───▶│   Phase 2   │───▶│   Phase 3   │───▶│   Phase 4   │───▶│   Phase 5   │
│    Data      │    │  Explore &  │    │   Train AI  │    │  Real-Time  │    │  Dashboard  │
│ Engineering  │    │  Analyze    │    │    Model    │    │  Detection  │    │ & Reporting │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     2 weeks           1 week            2 weeks           1.5 weeks          1.5 weeks
```

---

## Prerequisites

Before starting, make sure you have:

- [x] Python 3.9 or higher installed
- [x] Git installed and configured
- [x] A code editor (VS Code recommended)
- [x] Basic Python knowledge (functions, loops, file I/O)
- [x] Basic networking knowledge (IP addresses, TCP/UDP, ports)

---

## Initial Setup

### 1. Create Your Python Virtual Environment

```bash
cd projects/01-network-threat-detection-pipeline

# Create virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Verify
python --version
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Follow the instructions in [datasets/README.md](../../datasets/README.md) to download the NSL-KDD dataset.

---

## Dataset: NSL-KDD

You will work with the **NSL-KDD** dataset — a benchmark dataset for network intrusion detection.

- **125,973 training records** with 41 network features
- **22,544 test records**
- **5 traffic classes:** Normal, DoS, Probe, R2L, U2R

Each record represents a network connection with features like duration, protocol type, bytes transferred, error rates, and a label indicating if it's normal or a specific attack type.

---

## Phase Breakdown

### [Phase 1: Data Engineering](phase-1-data-engineering/) (Week 1-2)
Build the data foundation — ingest, clean, transform, and store network traffic data.

**You will build:**
- Data ingestion script to load raw CSV/TXT files
- Data cleaning pipeline (handle missing values, fix data types, remove noise)
- Feature engineering (encode categorical variables, normalize numeric features)
- Data storage layer (SQLite database + Parquet files)
- A reusable ETL pipeline that ties it all together

### [Phase 2: Exploratory Analysis](phase-2-exploratory-analysis/) (Week 3)
Understand the data through visualization and statistical analysis.

**You will build:**
- Statistical summary of traffic patterns
- Visualizations of attack type distributions
- Correlation analysis between features
- Feature importance analysis
- Attack pattern identification

### [Phase 3: AI/ML Model](phase-3-ai-ml-model/) (Week 4-5)
Train machine learning models to classify network traffic as normal or malicious.

**You will build:**
- Data preprocessing pipeline for ML
- Multiple ML models (Logistic Regression, Decision Tree, Random Forest)
- Model evaluation framework (accuracy, precision, recall, F1-score, confusion matrix)
- Hyperparameter tuning
- Model serialization (save/load trained models)

### [Phase 4: Real-Time Detection](phase-4-realtime-detection/) (Week 5-6)
Simulate real-time network traffic and classify it using your trained model.

**You will build:**
- Network traffic simulator
- Real-time classification engine
- Alert system for detected threats
- Logging and monitoring

### [Phase 5: Dashboard & Reporting](phase-5-dashboard-reporting/) (Week 7-8)
Visualize threats and generate security reports on an interactive dashboard.

**You will build:**
- Streamlit-based security dashboard
- Real-time threat visualization
- Attack statistics and trends
- Automated incident report generator

---

## Tech Stack

| Tool | Version | Purpose | Install |
|------|---------|---------|---------|
| Python | 3.9+ | Programming language | [python.org](https://www.python.org/downloads/) |
| Pandas | 2.0+ | Data manipulation | `pip install pandas` |
| NumPy | 1.24+ | Numerical computing | `pip install numpy` |
| Matplotlib | 3.7+ | Static visualizations | `pip install matplotlib` |
| Seaborn | 0.12+ | Statistical visualizations | `pip install seaborn` |
| Scikit-learn | 1.3+ | Machine learning | `pip install scikit-learn` |
| Streamlit | 1.28+ | Interactive dashboard | `pip install streamlit` |
| SQLite3 | built-in | Database | Comes with Python |
| Jupyter | latest | Interactive notebooks | `pip install jupyter` |
| Joblib | latest | Model serialization | Comes with scikit-learn |

---

## Submission Checklist

After completing all phases, verify:

- [ ] Phase 1: ETL pipeline runs end-to-end and produces clean data
- [ ] Phase 2: Jupyter notebook with all visualizations and analysis
- [ ] Phase 3: At least 2 trained models with evaluation metrics
- [ ] Phase 4: Real-time simulator detects and alerts on threats
- [ ] Phase 5: Dashboard displays live threat data
- [ ] All code is well-organized and runs without errors
- [ ] Each phase has its own meaningful git commits

---

## Grading Criteria

| Component | Weight | What We Look For |
|-----------|--------|-----------------|
| Data Engineering (Phase 1) | 20% | Clean pipeline, proper data types, storage |
| Analysis (Phase 2) | 15% | Depth of analysis, meaningful visualizations |
| ML Model (Phase 3) | 25% | Model performance, evaluation rigor |
| Real-Time (Phase 4) | 20% | Working detection, alert logic |
| Dashboard (Phase 5) | 15% | Usability, visual clarity |
| Code Quality | 5% | Clean code, git usage, documentation |

---

## Getting Help

- Read the phase-specific READMEs — they contain detailed instructions
- Check the `hints/` section in each phase if you're stuck
- Google error messages — debugging is a core engineering skill
- Ask your instructor during lab sessions

**Start with Phase 1 →** [phase-1-data-engineering/](phase-1-data-engineering/)
