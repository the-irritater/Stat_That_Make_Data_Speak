# Day 24: Type I and Type II Errors

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the difference between Type I (false positive) and Type II (false negative) errors, learn how they impact business decisions, and understand statistical power.

---

## The Concept
No statistical test is 100% perfect. Because we rely on samples, there is always a small chance we draw the wrong conclusion. We face two types of errors:

| Actual Truth | We Reject H0 (Claim an Effect) | We Fail to Reject H0 (Claim No Effect) |
|---|---|---|
| **H0 is True** (No real effect) | **Type I Error (False Positive)**<br>Probability = $\alpha$ (Significance Level) | Correct Decision<br>Probability = $1 - \alpha$ |
| **Ha is True** (Real effect exists) | Correct Decision<br>Probability = $1 - \beta$ (Statistical Power) | **Type II Error (False Negative)**<br>Probability = $\beta$ |

- **Type I Error (Alpha, $\alpha$):** You declare a winner when there isn't one (e.g., launching a new landing page that actually has no impact on conversions).
- **Type II Error (Beta, $\beta$):** You fail to detect a real change (e.g., discarding a new landing page that actually *would* have boosted conversions).
- **Statistical Power ($1 - \beta$):** The probability of correctly rejecting the Null Hypothesis when there is a real effect (typically targeted at 80%).

---

## Real-World Example
Suppose you run a fraud detection system:
- **H0:** The transaction is legitimate.
- **Ha:** The transaction is fraudulent.

If the system flags a legitimate purchase and blocks the customer's card:
- This is a **Type I Error (False Positive)**.
- **Business Cost:** Customer frustration and support tickets.

If the system fails to flag a stolen card and allows the transaction to go through:
- This is a **Type II Error (False Negative)**.
- **Business Cost:** Chargeback fees and financial loss.

**Business Decision:** Depending on the business context, you must adjust your thresholds. A high-security bank will accept more false positives (Type I) to minimize false negatives (Type II).

---

## Why This Step Matters
- **Risk Mitigation:** Helps businesses balance the cost of acting on a false alarm vs. the cost of missing an opportunity.
- **Sample Size Planning:** To increase statistical power (reduce Type II errors), you must increase your sample size.
- **Decision Criteria Design:** Helps set the significance level ($\alpha$) based on the severity of a Type I error.

---

## Key Takeaway
> **Takeaway:** You cannot eliminate errors completely. Decreasing the chance of a Type I error (false positive) naturally increases the chance of a Type II error (false negative). You must balance these based on the cost of being wrong.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Setting sample size thresholds to control error risk.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 23: Z-test vs t-test](day-23-z-test-vs-t-test.md) · [Next: Day 25 – A/B Testing and Chi-Square Test →](day-25-ab-testing-chi-square.md)
