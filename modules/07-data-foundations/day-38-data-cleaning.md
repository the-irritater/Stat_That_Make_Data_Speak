# Day 38: Data Cleaning

*A beautiful dashboard built on dirty data is still a bad dashboard.*

---

## Learning Objective

Understand the data cleaning process and common techniques for preparing raw data for reliable analysis.

---

## The Concept

Data cleaning is the process of detecting and fixing problems in raw data before analysis.

### Common Cleaning Steps

| Step | What You Do | Why |
|------|------------|-----|
| Remove duplicates | Drop repeated rows | Avoid inflated counts |
| Handle missing values | Impute or remove | Prevent biased results |
| Fix spelling/naming | Standardize categories | "mumbai" ≠ "Mumbai" to a computer |
| Correct data types | Convert strings to numbers/dates | Enable calculations |
| Fix date formats | Standardize to one format | Allow time-based analysis |
| Remove irrelevant columns | Drop unused variables | Reduce noise |
| Validate ranges | Check for impossible values | Age = -5 or 999 |

### The Data Cleaning Mindset

1. **Never modify the original data** — always work on a copy
2. **Document every change** — what you removed and why
3. **Check your work** — verify row counts and distributions after cleaning
4. **Be conservative** — when in doubt, investigate rather than delete

---

## Real-World Example

A sales dataset has 10,000 rows. After cleaning:
- 200 duplicate entries removed → 9,800 rows
- 150 rows had missing product names → investigated and filled from order IDs
- "Bangalore", "Bengaluru", "BLR" standardized to "Bengaluru"
- 5 transactions with negative amounts → flagged as refunds, not errors

The cleaned dataset tells a more accurate story.

---

## 🔑 Key Takeaway

> Data cleaning is not boring work. It is where reliable analysis begins. Every decision made during cleaning affects every conclusion downstream.

---

[← Day 37: Outlier Detection](day-37-outlier-detection.md) · [Next: Day 39 – Data Transformation →](day-39-data-transformation.md)
