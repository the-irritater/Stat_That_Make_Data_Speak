# Day 18: Normal Distribution

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the properties of the normal distribution (bell curve), apply the empirical rule (68-95-99.7 rule), and learn how to standardize data using z-scores.

---

## The Concept
The **Normal Distribution** is a continuous, symmetric, bell-shaped distribution. It is characterized entirely by its mean ($\mu$) and standard deviation ($\sigma$).

Key properties:
- **Symmetry:** The mean, median, and mode are all equal and located in the center.
- **Empirical Rule (68-95-99.7 Rule):**
  - **68%** of the data falls within $\pm 1$ standard deviation of the mean.
  - **95%** of the data falls within $\pm 2$ standard deviations of the mean.
  - **99.7%** of the data falls within $\pm 3$ standard deviations of the mean.
- **Standardization (z-score):** Converts any normal distribution into the **Standard Normal Distribution** (mean = 0, std dev = 1) to compare values.

---

## Key Formulas
```
Normal PDF: f(x) = (1 / (sigma * sqrt(2 * pi))) * e^(-(x - mu)^2 / (2 * sigma^2))

Z-score Formula: Z = (X - mu) / sigma
```
Where `X` is the raw data value, `mu` is the population mean, and `sigma` is the population standard deviation. A z-score measures how many standard deviations a data point is from the mean.

---

## Real-World Example
Suppose you run a delivery logistics company. The delivery times are normally distributed with a **mean of 30 minutes** and a **standard deviation of 5 minutes**.

- **Empirical Rule Application:**
  - 68% of deliveries take between `25 and 35 minutes` ($30 \pm 5$).
  - 95% of deliveries take between `20 and 40 minutes` ($30 \pm 10$).
- **Business Question:** What is the probability of a delivery taking **longer than 40 minutes**?
  - A delivery of 40 minutes has a z-score of: `Z = (40 - 30) / 5 = 2.0`.
  - Since 95% of data is between $Z = -2$ and $Z = 2$, the remaining 5% is split equally in the tails.
  - Therefore, the probability of a delivery taking longer than 40 minutes ($Z > 2$) is `5% / 2 = 2.5%`.

**Business Decision:** If you offer a "guaranteed delivery in 40 minutes or your money back" promo, you will have to issue refunds on approximately 2.5% of your orders, which helps you calculate the financial cost of the campaign.

---

## Why This Step Matters
- **Benchmark Analysis:** Standardizing metrics with z-scores lets you compare different units (e.g., comparing user activity score vs. revenue per user).
- **Inference Foundation:** Parametric tests like t-tests assume data follows a normal distribution.
- **Anomaly Detection:** Outliers can be flagged mathematically if their z-score is greater than 3 or less than -3.

---

## Key Takeaway
> **Takeaway:** The normal distribution is the default model for natural and human processes. Standardizing with z-scores allows you to map any raw value to a global probability.

---

## See It Applied
→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Checking skewness and checking normal overlays on bills.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 17: Binomial Distribution](day-17-binomial-distribution.md) · [Next: Day 19 – Central Limit Theorem →](day-19-central-limit-theorem.md)
