# Day 21: Confidence Intervals

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how confidence intervals provide a range of plausible values for a population parameter, learn how to calculate them, and understand the trade-off between precision and confidence.

---

## The Concept
When we take a sample from a population, the sample mean ($\bar{x}$) is a **point estimate** of the true population mean ($\mu$). However, because of sampling error, the sample mean is almost never exactly equal to the population mean.

Instead of reporting a single number, we calculate a **Confidence Interval (CI)** — a range of values that we are confident contains the true population parameter:
- **Confidence Level (e.g., 95%):** If we repeated our sampling process 100 times, 95 of the calculated intervals would contain the true population mean.
- **Margin of Error:** The range above and below the point estimate (determined by standard error and critical z-score).
- **The Trade-off:** If you want to be *more* confident (e.g., 99% CI), your interval must be wider (less precise). If you want a narrower interval (more precise), you must accept lower confidence or increase your sample size.

---

## Key Formulas
```
Confidence Interval: CI = x_bar +/- Margin of Error

Margin of Error: ME = Z* * (sigma / sqrt(n))
```
Where `x_bar` is the sample mean, `Z*` is the critical z-value corresponding to the target confidence level (for 95% confidence, `Z* = 1.96`), `sigma` is the population standard deviation, and `n` is the sample size. If `sigma` is unknown, we use the sample standard deviation `s` and a t-distribution critical value.

---

## Real-World Example
A digital analyst takes a random sample of **100 orders** and finds an average spend of **$45.00** with a standard deviation of **$10.00**.
- **Point Estimate:** $45.00.
- **Standard Error (SE):** `10 / sqrt(100) = $1.00`.
- **95% Confidence Interval calculation:**
  - `ME = 1.96 * $1.00 = $1.96`.
  - `CI = $45.00 +/- $1.96 = ($43.04, $46.96)`.

**Business Decision:** Instead of telling the CEO "our average customer spend is exactly $45," the analyst reports: *"We are 95% confident that the true average customer spend is between $43.04 and $46.96."* This sets realistic boundaries for financial modeling.

---

## Why This Step Matters
- **Communicates Uncertainty:** Prevents stakeholders from building models around a single, potentially noisy point estimate.
- **Sample Size Planning:** Tells you how many surveys/samples you need to collect to reach a desired level of precision (margin of error).
- **Quality Control Limits:** Defines standard operating ranges for manufacturing or server performance.

---

## Key Takeaway
> **Takeaway:** A point estimate is just a guess, but a confidence interval quantifies how precise that guess actually is. Never report a sample average without its interval.

---

## See It Applied
→ [Analyzing customer spending patterns](../../applied/notebooks/02-customer-spending-patterns.ipynb) — Estimating population spending metrics with margin boundaries.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 20: Poisson and Exponential Distributions](../04-distributions/day-20-poisson-exponential.md) · [Next: Day 22 – Introduction to Hypothesis Testing →](day-22-intro-to-hypothesis-testing.md)
