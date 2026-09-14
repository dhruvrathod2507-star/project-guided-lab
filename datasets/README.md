# Datasets

This guide covers how to download and prepare the datasets used across projects.

---

## 01 — Network Threat Detection Pipeline

### Primary Dataset: NSL-KDD

The NSL-KDD dataset is an improved version of the original KDD Cup 1999 dataset. It is widely used for benchmarking network intrusion detection systems.

**Why NSL-KDD?**
- No duplicate records (unlike the original KDD99)
- Manageable size (~150K records) — great for learning
- Well-documented with labeled attack types
- Industry-standard benchmark

**Download:**

1. Go to the [UNB Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/nsl.html)
2. Download the following files:
   - `KDDTrain+.txt` — Training set (125,973 records)
   - `KDDTest+.txt` — Test set (22,544 records)
   - `KDDTrain+_20Percent.txt` — 20% subset for quick experiments
   - `KDDTest-21.txt` — Test set without difficulty level

**Alternative direct download (if UNB site is slow):**

```bash
# From the official mirror
wget https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt
wget https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest%2B.txt
```

**Column Names (41 features + label + difficulty):**

```
duration, protocol_type, service, flag, src_bytes, dst_bytes, land,
wrong_fragment, urgent, hot, num_failed_logins, logged_in,
num_compromised, root_shell, su_attempted, num_root,
num_file_creations, num_shells, num_access_files,
num_outbound_cmds, is_host_login, is_guest_login, count,
srv_count, serror_rate, srv_serror_rate, rerror_rate,
srv_rerror_rate, same_srv_rate, diff_srv_rate,
srv_diff_host_rate, dst_host_count, dst_host_srv_count,
dst_host_same_srv_rate, dst_host_diff_srv_rate,
dst_host_same_src_port_rate, dst_host_srv_diff_host_rate,
dst_host_serror_rate, dst_host_srv_serror_rate,
dst_host_rerror_rate, dst_host_srv_rerror_rate,
label, difficulty_level
```

**Attack Categories:**

| Category | Attack Types | Description |
|----------|-------------|-------------|
| Normal | normal | Legitimate traffic |
| DoS | back, land, neptune, pod, smurf, teardrop, apache2, udpstorm, processtable, mailbomb | Denial of Service |
| Probe | ipsweep, nmap, portsweep, satan, mscan, saint | Surveillance/Scanning |
| R2L | ftp_write, guess_passwd, imap, multihop, phf, spy, warezclient, warezmaster, snmpgetattack, named, xlock, xsnoop, sendmail, httptunnel | Remote to Local |
| U2R | buffer_overflow, loadmodule, perl, rootkit, sqlattack, xterm, ps | User to Root |

---

### Bonus Dataset: CICIDS2017 (Advanced)

For students who want a more modern and larger dataset.

**Download:** [CICIDS2017 on UNB](https://www.unb.ca/cic/datasets/ids-2017.html)

- Contains 2.8M+ flow records
- Covers modern attacks: Brute Force, DDoS, Web Attacks, Infiltration, Botnet
- Captured over 5 days (Monday–Friday) with different attack scenarios each day
- CSV files per day, ~1GB total

---

### Where to Place the Data

After downloading, place the files in your project's `data/raw/` folder:

```
projects/01-network-threat-detection-pipeline/
└── phase-1-data-engineering/
    └── data/
        └── raw/
            ├── KDDTrain+.txt
            └── KDDTest+.txt
```

**Note:** Data files are gitignored — do NOT commit large datasets to the repo.
