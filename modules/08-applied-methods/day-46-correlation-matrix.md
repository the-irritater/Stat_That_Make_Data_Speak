# Day 46: Correlation Matrix

*See all relationships at once — but remember, correlation is not causation.*

---

## Learning Objective

Understand how correlation matrices efficiently reveal relationships across multiple variables, and their limitations.

---

## The Concept

A **correlation matrix** is a table showing correlation coefficients between every pair of numerical variables.

### Reading the matrix:

| Value | Meaning |
|-------|---------|
| +1.0 | Perfect positive correlation |
| +0.7 to +0.9 | Strong positive |
| +0.4 to +0.6 | Moderate positive |
| 0 to +0.3 | Weak or no relationship |
| Negative values | Same scale, inverse direction |

### Uses:

- **EDA** — quickly find which variables relate
- **Feature selection** — for ML, remove highly correlated features
- **Regression planning** — identify potential predictors
- **Multicollinearity check** — predictors correlated with each other

### Critical limitation:

Correlation measures **linear** relationships only. A perfect curve with r ≈ 0 is still a strong relationship — just not a linear one.

And always: **correlation ≠ causation**.

---

## Real-World Example

In a student dataset, the correlation matrix shows study hours and marks have r = 0.65 (moderate positive), while screen time and marks have r = -0.45 (moderate negative). But attendance and marks show r = 0.72 — strongest of all.

This suggests attendance may be a better predictor than study hours alone.

---

## 🔑 Key Takeaway

> A correlation matrix helps find relationships quickly across many variables. But interpretation still needs logic — high correlation does not prove causation.

---

[← Day 45: Scatter Plot](day-45-scatter-plot.md) · [Next: Day 47 – Simpson's Paradox →](day-47-simpsons-paradox.md)
