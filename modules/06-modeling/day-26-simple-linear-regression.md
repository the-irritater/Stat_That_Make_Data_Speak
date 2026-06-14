# Day 26: Simple Linear Regression

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand simple linear regression, interpret the regression coefficients (intercept and slope), and explain the value of R-squared in modeling outcomes.

---

## The Concept
While correlation measures the strength of a relationship, **regression** allows us to predict the value of one variable based on another:
- **Dependent Variable (Y):** The outcome we want to predict (e.g., sales).
- **Independent Variable (X):** The predictor variable (e.g., advertising spend).

**Simple Linear Regression** models the relationship with a straight line:
$$Y = \beta_0 + \beta_1 X + \epsilon$$
- **Intercept ($\beta_0$):** The predicted value of Y when X is 0.
- **Slope ($\beta_1$):** The change in Y for a 1-unit increase in X.
- **R-squared ($R^2$):** Measures the proportion of variance in Y explained by X (ranges from 0 to 1). An $R^2 = 0.60$ means 60% of the fluctuations in your outcome are captured by your predictor.

---

## Key Formulas
```
Simple Linear Regression Equation: y_hat = beta_0 + beta_1 * x

Slope: beta_1 = sum( (x_i - x_bar)*(y_i - y_bar) ) / sum( (x_i - x_bar)^2 )

Intercept: beta_0 = y_bar - beta_1 * x_bar
```

---

## Real-World Example
An e-commerce business models the relationship between site speed optimization (load time decrease in seconds, X) and average cart spend (Y).
- **Calculated Equation:** `y_hat = 35.00 + 4.50 * X`
- **Calculated R-squared ($R^2$):** `0.58`

**Interpreting the Coefficients:**
- **Intercept ($\beta_0 = 35.00$):** If speed optimization is 0 (current baseline speed), the average cart spend is predicted to be $35.00.
- **Slope ($\beta_1 = 4.50$):** For every 1-second improvement in load speed, average cart spend is predicted to increase by **$4.50**.
- **R-squared ($R^2 = 0.58$):** Site speed explains 58% of the variance in customer cart spend.

**Business Decision:** If optimization costs $2.00 per second per customer, the $4.50 predicted return makes this speed optimization highly profitable.

---

## Why This Step Matters
- **Predictive Capability:** Forecasts financial performance under different scenarios (e.g., predicting sales given ad budgets).
- **Quantifies Influence:** Determines exactly how much impact a change in X has on Y.
- **Goal Alignment:** Connects operational targets (e.g., reducing page weight) directly to bottom-line revenue outcomes.

---

## Key Takeaway
> **Takeaway:** Simple linear regression turns a scatter of data points into a mathematical formula, allowing you to estimate how changing your input (X) changes your output (Y).

---

## See It Applied
→ [Predicting customer spend](../../applied/notebooks/04-predicting-customer-spend.ipynb) — Fitting a simple regression line to website sessions.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 25: A/B Testing and Chi-Square Test](../05-inference/day-25-ab-testing-chi-square.md) · [Next: Day 27 – Multiple Linear Regression →](day-27-multiple-linear-regression.md)
