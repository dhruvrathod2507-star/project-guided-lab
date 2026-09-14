# Phase 1: Data Engineering

**Duration:** 2 weeks
**Objective:** Build a complete ETL (Extract, Transform, Load) pipeline that ingests raw network traffic data, cleans it, engineers useful features, and stores it in a structured format.

---

## What You Will Learn

- How to load and inspect raw data files
- Data cleaning techniques (missing values, duplicates, type casting)
- Feature engineering for network security data
- Encoding categorical variables (Label Encoding)
- Data storage formats (CSV, Parquet, SQLite)
- Building reusable data pipelines

---

## Step-by-Step Guide

### Step 1: Set Up Project Structure

Create the following folder structure inside `phase-1-data-engineering/`:

```
phase-1-data-engineering/
├── data/
│   ├── raw/           <- Place downloaded datasets here
│   ├── processed/     <- Cleaned data goes here
│   └── features/      <- Engineered features go here
├── src/
│   ├── ingest.py      <- Data loading functions
│   ├── clean.py       <- Data cleaning functions
│   ├── features.py    <- Feature engineering
│   ├── store.py       <- Data storage functions
│   └── pipeline.py    <- Ties everything together
├── notebooks/
│   └── 01_explore_raw_data.ipynb
└── README.md          <- You are here
```

Run this to create the folders:

```bash
mkdir -p data/{raw,processed,features} src notebooks
```

### Step 2: Download and Place the Data

1. Download `KDDTrain+.txt` and `KDDTest+.txt` (see [datasets/README.md](../../../datasets/README.md))
2. Place them in `data/raw/`

### Step 3: Data Ingestion (`src/ingest.py`)

Start with the provided `ingest.py` starter code. Your task:

**TODO items:**
1. Load the raw TXT file using `pandas.read_csv()`
2. Assign the correct column names (41 features + label + difficulty)
3. Verify the shape of the loaded DataFrame
4. Add basic logging to track what was loaded

**Key concepts to learn:**
- `pd.read_csv()` — loading data with custom headers
- `.shape`, `.dtypes`, `.head()` — inspecting DataFrames
- The NSL-KDD file has no header row, so you must provide column names

**Expected output:**
```
Loaded KDDTrain+.txt: 125973 rows, 43 columns
Columns: ['duration', 'protocol_type', 'service', ..., 'label', 'difficulty_level']
```

### Step 4: Data Cleaning (`src/clean.py`)

Your task is to clean the raw data. Implement these cleaning steps:

**TODO items:**
1. Check for and report missing values per column
2. Check for and remove duplicate rows
3. Fix data types (numeric columns should be int/float, categorical should be string)
4. Remove the `difficulty_level` column (not needed for our model)
5. Map the specific attack types to their 5 categories (Normal, DoS, Probe, R2L, U2R)
6. Create a binary label column: `is_attack` (0 = normal, 1 = attack)

**Attack type mapping:**

```python
ATTACK_CATEGORY_MAP = {
    'normal': 'Normal',

    'back': 'DoS', 'land': 'DoS', 'neptune': 'DoS', 'pod': 'DoS',
    'smurf': 'DoS', 'teardrop': 'DoS', 'apache2': 'DoS',
    'udpstorm': 'DoS', 'processtable': 'DoS', 'mailbomb': 'DoS',

    'ipsweep': 'Probe', 'nmap': 'Probe', 'portsweep': 'Probe',
    'satan': 'Probe', 'mscan': 'Probe', 'saint': 'Probe',

    'ftp_write': 'R2L', 'guess_passwd': 'R2L', 'imap': 'R2L',
    'multihop': 'R2L', 'phf': 'R2L', 'spy': 'R2L',
    'warezclient': 'R2L', 'warezmaster': 'R2L',
    'snmpgetattack': 'R2L', 'named': 'R2L', 'xlock': 'R2L',
    'xsnoop': 'R2L', 'sendmail': 'R2L', 'httptunnel': 'R2L',

    'buffer_overflow': 'U2R', 'loadmodule': 'U2R', 'perl': 'U2R',
    'rootkit': 'U2R', 'sqlattack': 'U2R', 'xterm': 'U2R', 'ps': 'U2R',

    # Additional types found in KDDTest+ (not in KDDTrain+)
    'snmpguess': 'R2L', 'worm': 'R2L',
}
```

**Expected output:**
```
Missing values: 0
Duplicates removed: 0
Columns after cleaning: 44
Attack categories: ['Normal', 'DoS', 'Probe', 'R2L', 'U2R']
Binary labels — Normal: 67343, Attack: 58630
```

### Step 5: Feature Engineering (`src/features.py`)

Transform raw features into ML-ready format.

**TODO items:**
1. **Label Encode** categorical columns: `protocol_type`, `service`, `flag`
2. **Create new features** (BEFORE normalization, so they use raw-scale values):
   - `bytes_ratio` = `src_bytes / (dst_bytes + 1)` — ratio of sent vs received bytes
   - `error_rate` = `(serror_rate + rerror_rate) / 2` — combined error rate
   - `is_privileged` = 1 if `root_shell == 1` or `su_attempted >= 1`, else 0
   - `traffic_intensity` = `count * srv_count` — measures connection busyness
3. **Normalize** numeric columns to 0-1 range using Min-Max scaling (LAST step)
4. **Save fitted encoders and scaler** using `joblib.dump()` to `data/features/` — Phase 4 needs these to transform new data identically
5. Save the feature-engineered data to `data/features/`

**IMPORTANT:** The order matters! Create derived features BEFORE normalizing.
If you normalize first, `bytes_ratio` will be computed on [0,1] values instead of actual byte counts — producing meaningless results.

**Key concepts to learn:**
- `sklearn.preprocessing.LabelEncoder` — converting text to numbers
- `sklearn.preprocessing.MinMaxScaler` — normalizing numeric ranges
- `joblib.dump()` / `joblib.load()` — saving and reloading fitted transformers
- Feature engineering — creating new meaningful features from existing ones

### Step 6: Data Storage (`src/store.py`)

Store the processed data in multiple formats.

**TODO items:**
1. Save to **CSV** — universal format, easy to inspect
2. Save to **Parquet** — compressed columnar format, fast for analytics
3. Save to **SQLite** — queryable database, useful for Phase 4 and 5

**SQLite schema:**

```sql
CREATE TABLE IF NOT EXISTS network_traffic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    duration REAL,
    protocol_type INTEGER,
    service INTEGER,
    flag INTEGER,
    src_bytes REAL,
    dst_bytes REAL,
    -- ... (all feature columns)
    label TEXT,
    attack_category TEXT,
    is_attack INTEGER
);
```

**Key concepts to learn:**
- `df.to_csv()`, `df.to_parquet()` — file-based storage
- `sqlite3` module — Python's built-in database
- `df.to_sql()` — writing DataFrames directly to SQL databases

### Step 7: Build the Pipeline (`src/pipeline.py`)

Tie everything together into a single executable pipeline.

**TODO items:**
1. Import functions from `ingest.py`, `clean.py`, `features.py`, `store.py`
2. Chain them: Ingest → Clean → Feature Engineer → Store
3. Add timing to measure how long each step takes
4. Add logging to track pipeline progress
5. Make it runnable from command line: `python src/pipeline.py`

**Expected output when running the pipeline:**
```
[Pipeline] Starting ETL pipeline...
[Step 1/4] Ingesting data... Done (1.2s) — 125973 rows loaded
[Step 2/4] Cleaning data... Done (0.8s) — 125973 rows, 0 dropped
[Step 3/4] Engineering features... Done (2.1s) — 46 features created
[Step 4/4] Storing data... Done (3.4s)
  → CSV: data/processed/train_clean.csv
  → Parquet: data/features/train_features.parquet
  → SQLite: data/processed/network_traffic.db
[Pipeline] Complete! Total time: 7.5s
```

---

## Checkpoint: How to Know You're Done

- [ ] `python src/pipeline.py` runs without errors
- [ ] `data/processed/train_clean.csv` exists and has clean data
- [ ] `data/features/train_features.parquet` exists with engineered features
- [ ] `data/processed/network_traffic.db` exists and is queryable
- [ ] You can explain what each step of your pipeline does

---

## Hints (Try on Your Own First!)

<details>
<summary>Hint 1: Loading data without headers</summary>

```python
df = pd.read_csv('data/raw/KDDTrain+.txt', header=None, names=COLUMN_NAMES)
```
</details>

<details>
<summary>Hint 2: Mapping attack types to categories</summary>

```python
df['attack_category'] = df['label'].map(ATTACK_CATEGORY_MAP)
# Handle any unknown attack types
df['attack_category'] = df['attack_category'].fillna('Unknown')
```
</details>

<details>
<summary>Hint 3: Saving to SQLite</summary>

```python
import sqlite3
conn = sqlite3.connect('data/processed/network_traffic.db')
df.to_sql('network_traffic', conn, if_exists='replace', index=False)
conn.close()
```
</details>

---

## Next Phase

Once your ETL pipeline works end-to-end, move on to:
**[Phase 2: Exploratory Analysis →](../phase-2-exploratory-analysis/)**
