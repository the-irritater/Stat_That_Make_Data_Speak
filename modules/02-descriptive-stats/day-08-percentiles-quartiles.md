# Day 8: Percentiles and Quartiles

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how percentiles, deciles, and quartiles divide your data, and use them to identify thresholds, outliers, and relative standings.

---

## The Concept
Percentiles divide a sorted dataset into 100 equal parts. If a value is at the 80th percentile, it means 80% of the observations fall below it, and 20% fall above.

We frequently use specific divisions:
- **Quartiles:** Divide data into 4 equal quarters (25%, 50%, 75%).
  - **Q1 (25th percentile):** The boundary for the bottom quarter.
  - **Q2 (50th percentile):** The Median.
  - **Q3 (75th percentile):** The boundary for the top quarter.
- **Interquartile Range (IQR):** `Q3 - Q1`. Represents the middle 50% of the data. IQR is crucial for box plots and identifying outliers.

---

## Key Formulas
```
Percentile Position: L = (P / 100) * (n + 1)
Interquartile Range: IQR = Q3 - Q1
Outlier Thresholds: 
  Lower Bound = Q1 - 1.5 * IQR
  Upper Bound = Q3 + 1.5 * IQR
```
Where `P` is the target percentile, and `n` is the sample size.

---

## Real-World Example
An e-commerce company monitors website page load speed. The average speed is **1.2 seconds**. 
However, checking the percentiles reveals:
- **50th percentile (Median):** 0.8 seconds
- **90th percentile:** 1.5 seconds
- **99th percentile:** 4.5 seconds

This shows that while 90% of your users experience fast load times (<1.5s), 1% of your users experience an unacceptably slow page load of 4.5+ seconds. Looking at the "average" of 1.2s hid this bad experience. Service Level Agreements (SLAs) are almost always set using the 95th or 99th percentile for this exact reason.

---

## Why This Step Matters
- **SLA & Performance Monitoring:** Measures extreme user experiences rather than average ones.
- **Customer Segmentation:** Helps bin customers (e.g., top 10% spenders vs. bottom 25%).
- **Outlier Detection:** Provides a mathematically rigorous way (1.5 * IQR rule) to isolate anomalies.

---

## Key Takeaway
> **Takeaway:** Percentiles allow you to see the distribution of experiences, ensuring you don't ignore the extremes that averages hide.

---

## See It Applied
→ [Who are our best buyers?](../../applied/notebooks/06-who-are-best-buyers.ipynb) – Binning customer recency, frequency, and monetary values into behavioral quartiles.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 7: Range, Variance, and Standard Deviation](day-07-range-variance-std-dev.md) · [Next: Day 9 – Skewness and Kurtosis →](day-09-skewness-kurtosis.md)
