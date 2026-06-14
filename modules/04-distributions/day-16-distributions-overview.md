# Day 16: Discrete vs Continuous Distributions

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the difference between discrete and continuous random variables and distributions, and know how to choose the correct model for your data type.

---

## The Concept
A **probability distribution** is a mathematical function that describes the likelihood of different outcomes for a variable. We classify distributions into two categories based on the variable type:

| Attribute | Discrete Distributions | Continuous Distributions |
|---|---|---|
| **Data Type** | Countable values (integers, whole numbers) | Uncountable values (real numbers, decimals) |
| **Examples** | Number of purchases, active users, email clicks | Order spend, page load speed, delivery time |
| **Key Function** | **Probability Mass Function (PMF)**: Gives the exact probability of a value, `P(X = x)` | **Probability Density Function (PDF)**: Gives the density; probability is calculated over a range, `P(a < X < b)` |
| **Visual representation** | Bar chart (distinct spikes) | Smooth line/curve (area under curve) |

---

## Key Formulas
```
Discrete: Sum of all P(X = x) = 1

Continuous: Integral from -infinity to +infinity of f(x) dx = 1 (Total area under the curve is 1)
```

---

## Real-World Example
Suppose you run a mobile app:
- **Discrete Metric:** The number of daily active sessions a single user starts. Since a user can start 1, 2, or 5 sessions (not 2.37 sessions), this is a discrete variable. You would model this using a PMF (e.g., Poisson distribution).
- **Continuous Metric:** The total minutes a user spends active in the app daily. Since a user can spend 12.45 minutes (and any decimal between), this is a continuous variable. You would model this using a PDF (e.g., Normal or Exponential distribution).

**Business Decision:** Choosing the correct distribution prevents statistical software from generating nonsensical predictions, such as estimating a 15.6% chance of a customer making exactly `2.5` purchases.

---

## Why This Step Matters
- **Model Selection:** Determines which formulas and libraries (e.g., `scipy.stats.binom` vs `scipy.stats.norm`) you must use.
- **Hypothesis Testing Assumptions:** Many parametric tests assume the outcome is a continuous variable following a specific distribution.
- **Simulation Modeling:** Essential for running realistic Monte Carlo simulations of business outcomes.

---

## Key Takeaway
> **Takeaway:** Countable data uses discrete distributions (PMF). Measurable data uses continuous distributions (PDF). Never mix up the two.

---

## See It Applied
→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Categorizing and plotting numerical vs. categorical customer variables.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Back to Module 4](README.md) · [Next: Day 17 – Binomial Distribution →](day-17-binomial-distribution.md)
