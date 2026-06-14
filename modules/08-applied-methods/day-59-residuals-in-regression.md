# Day 59: Residuals in Regression

*The regression equation is not the end. Residuals tell you whether the equation is trustworthy.*

---

## Learning Objective

Understand what residuals are, how to analyze residual plots, and why they are essential for validating regression models.

---

## The Concept

A **residual** is the difference between the actual value and the predicted value:

**Residual = Actual − Predicted**

### What residual plots reveal:

| Pattern | Problem | Action |
|---------|---------|--------|
| Random scatter | ✅ Good fit | None needed |
| Funnel shape | Unequal variance (heteroscedasticity) | Log transform or robust SE |
| Curved pattern | Non-linearity | Add polynomial terms |
| Clusters | Subgroups in data | Investigate grouping variable |
| Extreme points | Outliers/influential points | Check leverage and Cook's distance |

### The diagnostic checklist:

1. **Residuals vs Fitted** → check linearity and homoscedasticity
2. **Q-Q plot of residuals** → check normality
3. **Scale-Location plot** → check constant variance
4. **Residuals vs Leverage** → identify influential observations

### Key rule:

A model with a high R² but patterned residuals may still be wrong. Residuals should look like **random noise** — no patterns, no trends.

---

## Real-World Example

A house price model gives R² = 0.75. Looks good. But the residual plot shows a curve — the model underpredicts cheap houses and expensive houses, while overpredicting mid-range. A polynomial term or log transform is needed.

Predicted: ₹80 lakh. Actual: ₹85 lakh. Residual: ₹5 lakh.

---

## 🔑 Key Takeaway

> Regression does not end after getting an equation. Residuals tell you whether the model can be trusted. Always check residual plots.

---

[← Day 58: Multicollinearity](day-58-multicollinearity.md) · [Next: Day 60 – Practical Statistics Recap →](day-60-practical-statistics-recap.md)
