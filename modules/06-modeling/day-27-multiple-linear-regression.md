# Day 27: Multiple Linear Regression

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand multiple linear regression, learn how to interpret coefficients when multiple variables are controlled, and understand multicollinearity.

---

## The Concept
In the real world, an outcome is rarely influenced by only one factor. **Multiple Linear Regression** models the relationship between a single dependent variable (Y) and multiple independent variables ($X_1, X_2, \dots$):

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \epsilon$$

Key concepts:
- **Partial Coefficients ($\beta_i$):** Represents the change in Y for a 1-unit increase in $X_i$, **holding all other variables constant** (controlling for other factors).
- **Adjusted R-squared:** A modified version of $R^2$ that adjusts for the number of predictors in the model. Standard $R^2$ always goes up when you add features, even if they are useless. Adjusted $R^2$ penalizes adding irrelevant features.
- **Multicollinearity:** Occurs when two or more independent variables are highly correlated with each other (e.g., page views and time on site). This makes it hard for the model to isolate the individual impact of each variable.

---

## Key Formulas
```
Multiple Linear Regression Model: y_hat = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ... + beta_k * x_k
```

---

## Real-World Example
An analyst models customer spend (Y) using:
- $X_1$: Session duration (minutes)
- $X_2$: Pages visited

**Calculated Regression Model:** `y_hat = 15.00 + 1.30 * X_1 + 2.80 * X_2`

**Interpreting the Coefficients:**
- **Intercept ($\beta_0 = 15.00$):** Baseline predicted spend is $15.00.
- **Session Duration ($\beta_1 = 1.30$):** Controlling for pages visited, each additional minute a user spends on site increases predicted spend by **$1.30**.
- **Pages Visited ($\beta_2 = 2.80$):** Controlling for session duration, each additional page view increases predicted spend by **$2.80**.

**Why this matters:** In a simple regression of duration vs. spend, the slope was $3.65. By controlling for page views, the impact of time dropped to $1.30. This reveals that simply keeping users idling on a page does not generate as much value as keeping them actively clicking to new pages.

---

## Why This Step Matters
- **Realistic Scenario Modeling:** Reflects real-world business scenarios where multiple factors act simultaneously.
- **Confounding Variable Control:** Prevents attribution errors by controlling for background factors.
- **Model Optimization:** Helps select the combination of variables that yields the highest predictive power with the least complexity.

---

## Key Takeaway
> **Takeaway:** Multiple regression is about control. It allows you to isolate the impact of a single factor (like pricing) while holding all other factors (like season or traffic source) constant.

---

## See It Applied
→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Building and diagnosing multiple regression models in python.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 26: Simple Linear Regression](day-26-simple-linear-regression.md) · [Next: Day 28 – Correlation vs Causation →](day-28-correlation-vs-causation.md)
