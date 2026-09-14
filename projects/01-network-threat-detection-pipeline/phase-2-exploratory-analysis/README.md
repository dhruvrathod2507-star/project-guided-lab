# Phase 2: Exploratory Data Analysis (EDA)

**Duration:** 1 week
**Objective:** Understand the network traffic data through statistical analysis and visualization. Identify patterns that distinguish normal traffic from attacks.

**Prerequisite:** Complete Phase 1 (you need the cleaned data).

---

## What You Will Learn

- Statistical analysis of network datasets
- Data visualization with Matplotlib and Seaborn
- Identifying attack signatures in data
- Correlation analysis between features
- Communicating findings through visualizations

---

## Step-by-Step Guide

### Step 1: Set Up Your Notebook

Create the file `notebooks/02_eda.ipynb` (Jupyter Notebook).

```bash
cd phase-2-exploratory-analysis
mkdir -p notebooks
jupyter notebook
```

Load your cleaned data from Phase 1:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CLEANED (pre-encoded) data from Phase 1
# IMPORTANT: Use the CSV, NOT the Parquet — the Parquet has label-encoded
# categorical columns (protocol_type becomes 0/1/2 instead of tcp/udp/icmp)
# which makes categorical analysis meaningless.
df = pd.read_csv('../phase-1-data-engineering/data/processed/train_clean.csv')
# NOTE: Do NOT use train_features.parquet for EDA — that file has encoded values

print(f"Dataset shape: {df.shape}")
df.head()
```

---

### Step 2: Basic Statistical Summary

**TODO:** Create a statistical profile of the dataset.

```python
# 1. Overall statistics
df.describe()

# 2. Class distribution — how many normal vs attack records?
# TODO: Print value counts for 'attack_category' and 'is_attack'
# TODO: Calculate the percentage of each class

# 3. Protocol distribution
# TODO: What protocols are in the data? What percentage is each?

# 4. Top 10 services by frequency
# TODO: Which network services appear most often?
```

**Questions to answer in your notebook:**
- Is the dataset balanced (equal normal and attack records) or imbalanced?
- Which attack category is most common? Least common?
- What percentage of traffic uses TCP vs UDP vs ICMP?

---

### Step 3: Visualize Class Distribution

**TODO:** Create these visualizations.

#### 3a. Attack Category Distribution (Bar Chart)

```python
# TODO: Create a bar chart showing the count of each attack category
# Use seaborn's countplot or matplotlib's bar chart
# Add title, labels, and value annotations on each bar
# Color-code: green for Normal, different shades of red for attack types
```

#### 3b. Binary Classification Distribution (Pie Chart)

```python
# TODO: Create a pie chart showing Normal vs Attack percentage
# Show percentages on the chart
```

#### 3c. Top 15 Specific Attack Types (Horizontal Bar Chart)

```python
# TODO: Show the 15 most frequent specific attack types
# Use a horizontal bar chart for readability
```

---

### Step 4: Feature Distribution Analysis

**TODO:** Analyze how features differ between normal and attack traffic.

#### 4a. Duration Distribution

```python
# TODO: Create overlapping histograms of 'duration' for Normal vs Attack
# Use alpha (transparency) to show overlap
# What do you notice? Are attacks typically shorter or longer?
```

#### 4b. Bytes Transferred

```python
# TODO: Create box plots comparing src_bytes and dst_bytes across attack categories
# Box plots show median, quartiles, and outliers
# Which attack types transfer the most data?
```

#### 4c. Error Rates by Attack Category

```python
# TODO: Create a grouped bar chart showing average serror_rate and rerror_rate
# for each attack category
# Which attack types have the highest error rates? Why does that make sense?
```

---

### Step 5: Correlation Analysis

**TODO:** Find relationships between features.

#### 5a. Correlation Heatmap

```python
# TODO: Create a correlation heatmap of all numeric features
# Use seaborn's heatmap with a diverging color palette
# Focus on features with high correlation (> 0.7 or < -0.7)

# Hint:
# numeric_df = df.select_dtypes(include=[np.number])
# corr_matrix = numeric_df.corr()
# plt.figure(figsize=(20, 16))
# sns.heatmap(corr_matrix, cmap='RdBu_r', center=0, vmin=-1, vmax=1)
```

#### 5b. Highly Correlated Feature Pairs

```python
# TODO: Find and list all feature pairs with correlation > 0.9
# These might be redundant — we may drop one from each pair later
# Print them in a readable format
```

**Questions to answer:**
- Which features are most correlated with the attack label?
- Are there features that are nearly identical (redundant)?
- Which features might be most useful for the ML model?

---

### Step 6: Attack Pattern Analysis

**TODO:** Deep-dive into what makes each attack category unique.

#### 6a. Feature Comparison Table

```python
# TODO: For each attack category, calculate the mean of key features:
# duration, src_bytes, dst_bytes, count, srv_count, serror_rate
# Present as a clean table

# Hint:
# key_features = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'serror_rate']
# df.groupby('attack_category')[key_features].mean().round(2)
```

#### 6b. Protocol Usage by Attack Type

```python
# TODO: Create a stacked bar chart showing which protocols each attack type uses
# Do DoS attacks prefer TCP? Do Probe attacks use ICMP?
```

#### 6c. Service Targeting

```python
# TODO: For each attack category, find the top 5 targeted services
# This reveals which services attackers focus on
```

---

### Step 7: Key Findings Summary

At the end of your notebook, write a markdown cell summarizing:

1. **Dataset Overview** — Size, balance, key statistics
2. **Attack Landscape** — Which attacks are most/least common
3. **Distinguishing Features** — Which features best separate normal from attack traffic
4. **Redundant Features** — Which features are highly correlated and could be removed
5. **Recommendations for ML** — Based on your analysis, what features and approach do you recommend for Phase 3?

---

## Checkpoint: How to Know You're Done

- [ ] Notebook runs top-to-bottom without errors
- [ ] All visualizations have titles, axis labels, and legends
- [ ] At least 8 distinct visualizations created
- [ ] Correlation analysis identifies redundant features
- [ ] Key findings section with actionable recommendations for Phase 3
- [ ] You can explain what makes each attack category unique in the data

---

## Starter Code

Use the provided `eda_starter.py` for function templates, or work directly in a Jupyter notebook.

---

## Next Phase

**[Phase 3: AI/ML Model →](../phase-3-ai-ml-model/)**
