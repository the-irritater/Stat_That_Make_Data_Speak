# Day 28: Correlation vs Causation

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the difference between correlation and causation, learn how confounding variables create spurious relationships, and understand methods to establish causality.

---

## The Concept
One of the most famous rules in statistics is: **Correlation does not imply causation.**
- **Correlation:** Two variables move together (e.g., when X goes up, Y goes up).
- **Causation:** A change in X *causes* a change in Y.

spurious correlation (a false relationship) is almost always created by a **Confounding Variable** — a third factor that influences both variables.

```
       [Confounding Variable: Z]
             /           \
            v             v
       [Variable: X] <---> [Variable: Y]
                        (Spurious Correlation)
```

To establish causality, researchers use specific frameworks:
1. **Temporal Precedence:** X must occur before Y.
2. **Covariation:** X and Y must move together.
3. **No Alternative Explanation:** Confounding variables must be ruled out (usually via randomization in A/B testing).

---

## Real-World Example
A city database shows a strong positive correlation between ice cream sales (X) and drowning incidents (Y).
- **The Spurious Correlation:** Does buying ice cream cause people to drown? No.
- **The Confounding Variable (Z):** Temperature / Summer.
  - Hot weather causes ice cream sales to go up.
  - Hot weather also causes more people to go swimming, leading to higher drowning rates.

In business: a data analyst notices that users who view the "FAQ Page" (X) have a higher customer churn rate (Y).
- **Spurious Claim:** Viewing the FAQ page causes users to churn. Let's delete the FAQ page!
- **Confounding Variable:** Software issues. Customers experiencing problems visit the FAQ page to troubleshoot, and if their issue isn't resolved, they churn. Deleting the FAQ page will actually increase churn by removing help resources.

---

## Why This Step Matters
- **Prevents Costly Mistakes:** Stops companies from launching counter-productive strategies based on raw correlations (like deleting the FAQ page).
- **Justifies A/B Testing:** Randomization in A/B tests spreads confounding variables evenly across groups, neutralizing them and proving causality.
- **Ensures Analytical Integrity:** Ensures that you provide stakeholders with true drivers of outcomes, not just coincidental metrics.

---

## Key Takeaway
> **Takeaway:** Never assume that because two variables move together, one causes the other. Always search for the third hidden variable (confounder) or run a randomized experiment to prove causation.

---

## See It Applied
→ [Do Discounts Drive Retention?](../../applied/case-studies/discount-vs-retention/) — Realizing that discount depth correlates with high churn because of the consumer segment confounder.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 27: Multiple Linear Regression](day-27-multiple-linear-regression.md) · [Next: Day 29 – Logistic Regression Basics →](day-29-logistic-regression.md)
