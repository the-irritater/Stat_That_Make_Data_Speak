# Day 23: Z-test vs t-test

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand when to use a Z-test vs. a t-test to compare sample means, understand degrees of freedom, and run these tests on continuous variables.

---

## The Concept
To test a hypothesis about a continuous variable (like order spend or session length), we compare the sample mean to a target value or compare two sample means. We choose between two classical tests:

| Attribute | Z-test | t-test |
|---|---|---|
| **Population Standard Deviation ($\sigma$)** | Known | **Unknown** (highly common in real life) |
| **Sample Size ($n$)** | Large ($n \geq 30$) | Can be small ($n < 30$), though works for large samples too |
| **Critical Distribution** | Standard Normal ($Z$) | Student's $t$ (fatter tails to account for uncertainty) |
| **Business Usage** | Rare (we almost never know the true population standard deviation) | **Standard practice** for comparing A/B groups |

---

## Key Formulas
```
z-statistic: z = (x_bar - mu_0) / (sigma / sqrt(n))

t-statistic: t = (x_bar - mu_0) / (s / sqrt(n))
```
Where `x_bar` is the sample mean, `mu_0` is the hypothesized mean under H0, `sigma` is the population standard deviation, `s` is the sample standard deviation, and `n` is the sample size.

---

## Real-World Example
An analyst wants to test if a new feature increases the time users spend in an app.
- **H0:** The mean app session time is 15 minutes ($\mu = 15$).
- **Ha:** The mean app session time is greater than 15 minutes ($\mu > 15$).
- **Sample ($n = 25$ sessions):** Mean spend is **16.5 minutes** with a sample standard deviation of **3.0 minutes**.
- **Test Choice:** Since the population standard deviation is unknown and the sample is small ($n = 25$), we use a **t-test**.

Using the t-statistic formula:
- `t = (16.5 - 15.0) / (3.0 / sqrt(25)) = 1.5 / (3.0 / 5) = 1.5 / 0.6 = 2.5`
- The calculated t-statistic is **2.5**.
- Comparing this to a t-distribution with 24 degrees of freedom ($n - 1$) at $\alpha = 0.05$: the critical t-value is `1.71`.
- Since our t-statistic (`2.5`) is greater than the critical value (`1.71`), we reject H0.

**Business Decision:** The new feature statistically significantly increases app session time.

---

## Why This Step Matters
- **A/B Testing Implementation:** Used to verify if test conversion spending outperforms control conversion spending.
- **Scientific Rigor:** Prevents false confidence in small sample sizes by using the wider t-distribution instead of the z-distribution.
- **Financial Validation:** Compares average customer lifetime value across acquisition channels.

---

## Key Takeaway
> **Takeaway:** In real-world data analysis, you almost never know the true population standard deviation. Always defaults to using a t-test instead of a Z-test.

---

## See It Applied
→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Executing two-sample t-tests to evaluate average purchase amounts.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 22: Introduction to Hypothesis Testing](day-22-intro-to-hypothesis-testing.md) · [Next: Day 24 – Type I and Type II Errors →](day-24-type-i-ii-errors.md)
