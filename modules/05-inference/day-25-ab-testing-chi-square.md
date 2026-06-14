# Day 25: A/B Testing and Chi-Square Test

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how A/B testing maps to statistical hypotheses, learn how to use a Chi-Square test of independence to compare categorical outcomes, and interpret contingency tables.

---

## The Concept
An **A/B Test** is a randomized experiment where you compare a baseline version (Control, A) against a modified version (Treatment, B) to measure impact.

When the outcome metric is **categorical** (e.g. converted vs. not converted, clicked vs. ignored), we cannot use a t-test. Instead, we use a **Chi-Square Test of Independence**:
- It tests whether the outcome (conversion) is independent of the group (Control vs. Treatment).
- It compares the **observed frequencies** in our data against the **expected frequencies** if the null hypothesis were true.
- If the difference between observed and expected is large, the Chi-Square statistic will be high, resulting in a low p-value.

---

## Key Formulas
```
Chi-Square Statistic: X^2 = sum[ (O_i - E_i)^2 / E_i ]

Expected Frequency: E = (Row Total * Column Total) / Grand Total
```
Where `O_i` is the observed count in cell `i`, and `E_i` is the expected count.

---

## Real-World Example
You run an A/B test comparing a green signup button (Control) vs. a red signup button (Test).
- **Observed Data:**
  - Control: 40 signed up, 160 did not. (200 total)
  - Test: 60 signed up, 140 did not. (200 total)
- **H0:** Signup rate is independent of button color.
- **Ha:** Signup rate depends on button color.

Expected conversion if color had zero effect (overall conversion rate is `100 / 400 = 25%`):
- Expected signed up for Control: `200 * 0.25 = 50`
- Expected signed up for Test: `200 * 0.25 = 50`

Using the Chi-Square formula:
- `X^2 = (40-50)^2/50 + (160-150)^2/150 + (60-50)^2/50 + (140-150)^2/150`
- `X^2 = 100/50 + 100/150 + 100/50 + 100/150 = 2.0 + 0.67 + 2.0 + 0.67 = 5.33`
- Comparing `X^2 = 5.33` to a Chi-Square distribution with 1 degree of freedom: the p-value is **0.021**.

**Business Decision:** Since $p < 0.05$, we reject the Null Hypothesis. The red button drove a statistically significant conversion lift.

---

## Why This Step Matters
- **Conversion Rate Optimization (CRO):** Standard analysis framework for website updates, pricing tier changes, and email subjects.
- **User Segmentation Auditing:** Checks if different demographic groups exhibit statistically different product behaviors.
- **Reliability:** Prevents team bias from declaring a "winner" based on a few extra conversions.

---

## Key Takeaway
> **Takeaway:** For continuous outcomes (e.g. revenue), use a t-test. For categorical outcomes (e.g. click-through rate), use a Chi-Square test of independence.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Using Chi-Square tests to evaluate coupon effectiveness.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 24: Type I and Type II Errors](day-24-type-i-ii-errors.md) · [Next: Day 26 – Simple Linear Regression →](../06-modeling/day-26-simple-linear-regression.md)
