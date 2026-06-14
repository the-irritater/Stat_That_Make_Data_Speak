# Day 22: Introduction to Hypothesis Testing

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the logic of hypothesis testing, learn how to set up Null and Alternative hypotheses, and understand p-values and significance levels.

---

## The Concept
In data analytics, we frequently compare groups or look for changes (e.g., does a new web design increase sales?). Before claiming success, we must verify that the difference isn't just a random fluke. We use **Hypothesis Testing**:

1. **Null Hypothesis (H0):** The status quo. The claim that there is *no effect*, no difference, or no change (e.g., the new design has the same sales as the old one). We assume H0 is true unless we have strong evidence to reject it.
2. **Alternative Hypothesis (Ha or H1):** The challenger. The claim that there *is* an effect, a difference, or a change (e.g., the new design increases sales).
3. **Significance Level (alpha, $\alpha$):** The threshold for rejection, typically set at `0.05` (5%). It is the probability of accidentally rejecting H0 when it was actually true.
4. **p-value:** The probability of obtaining a test statistic at least as extreme as the one observed, assuming the Null Hypothesis is true.
   - **p-value < $\alpha$ (usually 0.05):** Reject H0. The result is "statistically significant."
   - **p-value >= $\alpha$:** Fail to reject H0. There is not enough evidence to support the change.

---

## Key Formulas
```
Null Hypothesis: H0: mu_1 = mu_2  (or mu = mu_0)

Alternative Hypothesis: Ha: mu_1 != mu_2  (or mu > mu_0)
```
Where `mu` represents the true population mean.

---

## Real-World Example
A product manager wants to test a new checkout layout to increase conversion rates.
- **H0:** The conversion rate of the new layout is equal to the old layout.
- **Ha:** The conversion rate of the new layout is higher than the old layout.
- **$\alpha$ (Significance Level):** `0.05` (5%).

After running the test with 1,000 visitors, the data shows a conversion lift, and the statistical software returns a **p-value of 0.02**.
- **Interpretation:** Since the p-value (`0.02`) is less than alpha (`0.05`), we **reject the Null Hypothesis**.
- **Conclusion:** The conversion rate lift is statistically significant. The new layout is launched.

If the p-value was **0.18**, we would **fail to reject the Null Hypothesis**. Even though the sample conversion rate looked slightly higher, the difference was likely due to random chance. We would keep the old layout.

---

## Why This Step Matters
- **Objective Decision-Making:** Removes subjective "opinions" and "gut feelings" from business choices.
- **Saves Resources:** Prevents companies from deploying campaigns or features that have no measurable impact.
- **Protects Against Flukes:** Quantifies the chance of a false positive result.

---

## Key Takeaway
> **Takeaway:** Hypothesis testing is a conservative process. We always start by assuming nothing changed (Null Hypothesis) and demand strong, statistical proof (p-value < 0.05) to believe otherwise.

---

## See It Applied
→ [Is this campaign actually working?](../../applied/notebooks/07-is-campaign-working.ipynb) — Setting up tests for marketing conversion lifts.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 21: Confidence Intervals](day-21-confidence-intervals.md) · [Next: Day 23 – Z-test vs t-test →](day-23-z-test-vs-t-test.md)
