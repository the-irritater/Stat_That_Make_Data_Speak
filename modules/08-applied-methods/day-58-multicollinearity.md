# Day 58: Multicollinearity

*When predictors are too similar, the model cannot tell them apart.*

---

## Learning Objective

Understand multicollinearity in regression, how to detect it with VIF, and strategies for handling it.

---

## The Concept

**Multicollinearity** occurs when predictor variables in a regression model are highly correlated with each other.

### Why it is a problem:

- Regression coefficients become **unstable** — small data changes cause large coefficient swings
- Standard errors **inflate** — making significant predictors appear insignificant
- **Interpretation breaks** — "holding other variables constant" is impossible when they move together

### How to detect:

| Method | How |
|--------|-----|
| **Correlation matrix** | Pairs with r > 0.7–0.8 |
| **VIF (Variance Inflation Factor)** | VIF > 5 = concern, VIF > 10 = serious |
| **Coefficient instability** | Coefficients change sign when variables are added/removed |

### How to handle:

1. **Remove one** of the correlated predictors
2. **Combine them** into a single composite variable (PCA)
3. **Use regularization** (Ridge, Lasso regression)
4. **Accept it** — if prediction is the goal, not interpretation

---

## Real-World Example

Predicting house price using house area (sq ft) and number of rooms. These are highly correlated (VIF = 8.2). The model can't determine if an extra room or extra square footage drives price — because they move together.

Solution: Remove "number of rooms" (since area captures it) and the model becomes interpretable.

---

## 🔑 Key Takeaway

> When predictors are too similar, the regression model becomes harder to interpret. Always check VIF before trusting regression coefficients.

---

[← Day 57: Homogeneity of Variance](day-57-homogeneity-of-variance.md) · [Next: Day 59 – Residuals in Regression →](day-59-residuals-in-regression.md)
