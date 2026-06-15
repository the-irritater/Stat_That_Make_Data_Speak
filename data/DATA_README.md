# Data Management & Provenance

This directory contains the datasets used across all modules, case studies, and notebooks in the Stats Series project. 

---

## Folder Structure

```text
data/
├── DATA_README.md        # This document
├── data-schema.json      # Machine-readable schema definitions
├── raw/                  # Immutable raw source data
│   ├── customer_discounts.csv
│   ├── ecommerce.csv
│   ├── marketing_campaign.csv
│   ├── screen_time.csv
│   └── tips.csv
└── processed/            # Reproducible aggregations and processed outputs
    └── .gitkeep
```

---

## Dataset Catalog & Provenance

### 1. Restaurant Tips (`tips.csv`)
* **Source:** Originally collected by Bryant & Smith (1995) in their book *Practical Data Analysis: Case Studies in Business Statistics*. Also standard in `seaborn.load_dataset('tips')`.
* **Description:** Details restaurant tipping behavior based on total bill, gender, day of week, time of day, smoking status, and party size.
* **Metadata:** 244 records, 7 columns.
* **Licensing:** Public Domain / CC0.

### 2. E-commerce Customer Spend (`ecommerce.csv`)
* **Source:** Derived structure from the UCI Machine Learning Online Retail dataset with synthetic extensions to support multi-variable modeling.
* **Description:** Charts customer session behaviors (duration, page views, discount usage) and monetary outcomes (spend, recency, frequency).
* **Metadata:** 1,000 records, 9 columns.
* **Licensing:** CC-BY-4.0 (UCI Repository) / MIT Educational.

### 3. Marketing Campaign A/B Test (`marketing_campaign.csv`)
* **Source:** Synthetically generated in 2024 to mimic standard digital marketing A/B tests.
* **Description:** Logs user interaction and conversion behavior under control vs test conditions (promotional campaign vs baseline).
* **Metadata:** 2,500 records, 4 columns.
* **Licensing:** MIT / Synthetic.

### 4. Screen Time vs Productivity (`screen_time.csv`)
* **Source:** Synthetically generated in 2024 based on normal and negative exponential distributions.
* **Description:** Correlates daily screen time hours with self-reported employee productivity index, along with demographic parameters (age, profession).
* **Metadata:** 150 records, 5 columns.
* **Licensing:** MIT / Synthetic.

### 5. Customer Discount Retention (`customer_discounts.csv`)
* **Source:** Synthetically generated in 2024 to model retention behavior.
* **Description:** Records discount rate depth (0% to 50%) alongside customer retention outcome (retained vs churned), tenure, and spend.
* **Metadata:** 301 records, 5 columns.
* **Licensing:** MIT / Synthetic.

---

## Ethical & Legal Statement

> [!NOTE]
> **Data Privacy & GDPR Wording:**
> The project follows GDPR-inspired data minimization principles and avoids storing personally identifiable information. This project uses synthetic/public datasets and does not contain personally identifiable information (PII). All user IDs, purchase amounts, and demographic markers are simulated or pre-anonymized.
