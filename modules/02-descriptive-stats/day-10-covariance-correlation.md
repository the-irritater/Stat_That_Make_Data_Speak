# Day 10: Covariance and Correlation

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how covariance and correlation quantify the direction and strength of linear relationships between variables, and know how to interpret correlation coefficients.

---

## The Concept
When analyzing two variables, we want to know: *Do they move together?*
- **Covariance:** Measures the direction of a linear relationship.
  - Positive covariance: As X increases, Y tends to increase.
  - Negative covariance: As X increases, Y tends to decrease.
  - **The Problem:** The magnitude of covariance depends on the units of measurement (e.g., height in meters vs. centimeters), making it hard to interpret the strength.
- **Correlation (Pearson's r):** Standardizes covariance into a value between `-1` and `+1`.
  - `+1`: Perfect positive relationship.
  - `-1`: Perfect negative relationship.
  - `0`: No linear relationship.
  - **The Advantage:** Unitless. A correlation of 0.8 is strong whether you measure in miles, kilometers, or dollars.

---

## Key Formulas
```
Sample Covariance: Cov(X, Y) = sum(x_i - x_bar)(y_i - y_bar) / (n - 1)

Pearson's r = Cov(X, Y) / (s_x * s_y)
```
Where `s_x` and `s_y` are the sample standard deviations of X and Y.

---

## Real-World Example
An online retail business compares marketing spend (X) vs. monthly revenue (Y).
- **Calculated Covariance:** `+125,000` (shows a positive relationship, but we don't know if it's strong).
- **Calculated Correlation (r):** `0.85` (standardized).

Because $r = 0.85$, we have statistical proof of a **very strong positive linear relationship**. Marketing spend and revenue move together closely, which helps justify marketing investments.

---

## Why This Step Matters
- **Feature Selection:** Helps select variables for predictive machine learning models.
- **Root Cause Analysis:** Identifies key drivers of business outcomes (e.g., what variables associate with churn?).
- **Portfolio Diversification:** Investors look for assets with low or negative correlation to spread risk.

---

## Key Takeaway
> **Takeaway:** Covariance shows direction, but correlation shows strength. Always use correlation (r) to compare relationships across different variables.

---

## See It Applied
→ [What actually drives sales?](../../applied/notebooks/03-what-drives-sales.ipynb) — Building correlation heatmaps on sales transactions.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 9: Skewness and Kurtosis](day-09-skewness-kurtosis.md) · [Next: Day 11 – Introduction to Probability →](../03-probability/day-11-intro-to-probability.md)
