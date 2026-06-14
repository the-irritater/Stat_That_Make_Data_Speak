# Day 9: Skewness and Kurtosis

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how skewness and kurtosis describe the shape, symmetry, and tail behavior of your data distributions to anticipate risks and model errors.

---

## The Concept
While mean tells you the center and standard deviation tells you the spread, **Skewness** and **Kurtosis** describe the shape of the distribution:

- **Skewness:** Measures the lack of symmetry.
  - **Symmetric (Skew = 0):** Balanced on both sides (e.g., normal distribution).
  - **Right-skewed / Positive (Skew > 0):** Tail extends to the right (e.g., income, house prices, tips).
  - **Left-skewed / Negative (Skew < 0):** Tail extends to the left (e.g., age of retirement, GPA scores).
- **Kurtosis:** Measures the "tailedness" (heavy tails vs. light tails).
  - **Mesokurtic (Kurtosis = 3):** Normal distribution.
  - **Leptokurtic (Kurtosis > 3):** Fat tails, sharp peak. Higher likelihood of extreme outliers (black swans).
  - **Platykurtic (Kurtosis < 3):** Thin tails, flat peak. Outliers are rare.

---

## Key Formulas
```
Skewness: g_1 = E[(X - mu)^3] / sigma^3

Kurtosis: g_2 = E[(X - mu)^4] / sigma^4
```
Where `mu` is the mean and `sigma` is the standard deviation.

---

## Real-World Example
Consider two financial portfolios, A and B, both returning an **average of 8% annually**.
- **Portfolio A (Skew = -1.2, Kurtosis = 5):** Return distribution is left-skewed with fat tails. This means that while most years it returns exactly 8% or more, there is a risk of occasional massive, negative returns (market crashes).
- **Portfolio B (Skew = 0.1, Kurtosis = 2.8):** Symmetric, thin-tailed. It is highly predictable, and extreme crashes are statistically highly unlikely.

An investor looking only at average returns (8%) would treat these portfolios as identical, missing the tail risk modeled by skewness and kurtosis.

---

## Why This Step Matters
- **Risk Management:** Essential in insurance and finance to prepare for extreme events (fat-tails).
- **Assumption Checking:** Many statistical tests assume a normal distribution (Skew ~ 0, Kurtosis ~ 3). Checking these values prevents wrong test selections.
- **Data Understanding:** Explains why the mean is pulled away from the median.

---

## Key Takeaway
> **Takeaway:** The mean and variance only describe the size and width of your data; skewness and kurtosis describe the shape and the risk hidden in the tails.

---

## See It Applied
→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Inspecting right-skewed sales distributions.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 8: Percentiles and Quartiles](day-08-percentiles-quartiles.md) · [Next: Day 10 – Covariance and Correlation →](day-10-covariance-correlation.md)
