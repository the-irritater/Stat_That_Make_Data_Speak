# Day 35: Clean Data vs Messy Data

*Most real-world analysis time is spent cleaning data, not building models. Here's why.*

---

## Learning Objective

Understand the characteristics of clean vs messy data, and recognize common data quality problems.

---

## The Concept

**Clean data** is organized, consistent, complete, and ready for analysis.

**Messy data** contains problems that can silently ruin your analysis:

| Problem | Example |
|---------|---------|
| Missing values | Blank income field |
| Duplicates | Same customer appears twice |
| Inconsistent naming | "Mumbai", "mumbai", "Mum", "Bombay" |
| Wrong data types | Age stored as text instead of number |
| Mixed formats | Dates as "15/06/2025" and "June 15, 2025" |
| Extreme values | Age = 999 |
| Unclear columns | Column named "col1", "var_x" |

### The 80/20 Rule of Data Work

In most data projects, **~80% of time goes to data cleaning** and only ~20% to actual analysis and modeling. This is not wasted time — it is where trustworthy analysis begins.

---

## Real-World Example

In a student dataset, the "city" column contains: "Mumbai", "mumbai", "Mum", "MUMBAI", and "Bombay".

A computer treats each as a different city. Without cleaning, a frequency count shows 5 cities instead of 1.

Every chart, model, and conclusion built on this data would be wrong.

---

## 🔑 Key Takeaway

> Clean data makes analysis reliable. Messy data makes even advanced methods useless. Always inspect data quality before starting analysis.

---

[← Day 34: Cross-Sectional vs Time Series](day-34-cross-sectional-vs-time-series.md) · [Next: Day 36 – Missing Values →](day-36-missing-values.md)
