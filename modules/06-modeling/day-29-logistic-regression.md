# Day 29: Logistic Regression Basics

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the basics of logistic regression, learn why linear regression fails for binary classification, and interpret odds ratios and probabilities.

---

## The Concept
Linear regression is designed to predict continuous variables (like sales amounts). If you try to use it to predict a **binary outcome** (Yes/No, 1/0, Churn/Retain), it fails:
- It can predict values greater than 1 or less than 0 (which are impossible probabilities).
- The assumptions of linear regression (normality of residuals) are violated.

Instead, we use **Logistic Regression**:
- It models the probability ($p$) that a binary event occurs.
- It uses the **logistic (sigmoid) function** to map any real-valued number into a value between `0` and `1`.
- It models the **log-odds** of the outcome:
$$\log\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots$$
- **Odds Ratio (OR):** Exp($\beta_1$). Represents the factor by which the odds of the outcome increase for a 1-unit increase in X.

---

## Key Formulas
```
Sigmoid Function: p = 1 / (1 + e^-z)

Log-odds (Logit): log( p / (1 - p) ) = beta_0 + beta_1 * x
```
Where `p` is the probability of the success event (1).

---

## Real-World Example
A subscription software company wants to predict whether a customer will churn next month (1 = Churn, 0 = Active) based on how many support tickets they file (X).
- **Calculated Logistic Regression Model:** `log( p / (1-p) ) = -3.5 + 0.69 * X`
- The odds ratio for support tickets is: `exp(0.69) = 2.0`.

**Interpretation:**
- **Odds Ratio = 2.0:** For every additional support ticket a customer files, the **odds of them churning double** (2× increase).
- **Probability Estimation:** If a customer files 5 support tickets:
  - `z = -3.5 + 0.69 * 5 = -3.5 + 3.45 = -0.05`
  - `p = 1 / (1 + e^-(-0.05)) = 1 / (1 + 1.051) = 0.487` (48.7% chance of churning).

**Business Decision:** Customer support can flag accounts reaching 5+ tickets for immediate proactive outreach.

---

## Why This Step Matters
- **Classification Modeling:** The standard statistical framework for customer churn prediction, credit risk scoring, and conversion forecasting.
- **Explainable Predictions:** Unlike complex "black box" machine learning models, logistic regression provides explicit odds ratios that business stakeholders can easily understand.
- **Risk Indexing:** Scores customer behavior in real-time.

---

## Key Takeaway
> **Takeaway:** For predicting quantities, use linear regression. For predicting probabilities of binary outcomes (1/0), use logistic regression.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Setting up frameworks for binary customer conversions.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 28: Correlation vs Causation](day-28-correlation-vs-causation.md) · [Next: Day 30 – Statistics Roadmap →](day-30-statistics-roadmap.md)
