# Day 55: Assumptions in Statistics

*Every statistical method has rules. Break them, and the results may be meaningless.*

---

## Learning Objective

Understand that statistical tests have assumptions that must be checked, and know the consequences of violating them.

---

## The Concept

**Assumptions** are conditions that should be reasonably satisfied for a statistical method to produce valid results.

### Common assumptions by method:

| Method | Key Assumptions |
|--------|----------------|
| **t-test** | Normality, equal variance, independence |
| **ANOVA** | Normality, homogeneity of variance, independence |
| **Linear Regression** | Linearity, normality of residuals, homoscedasticity, independence, no multicollinearity |
| **Chi-square** | Expected frequencies ≥ 5, independence |
| **Correlation (Pearson)** | Linearity, normality, no outliers |

### What happens when assumptions are violated:

- p-values become unreliable
- Confidence intervals are too narrow or too wide
- Type I/II error rates change
- Conclusions may be wrong

### The practical approach:

1. **Check assumptions** before running a test
2. **Use robust alternatives** when assumptions are violated (e.g., Welch's t-test instead of Student's t-test)
3. **Report assumption checks** — it shows methodological rigor
4. **Don't demand perfection** — "approximately satisfied" is usually enough

---

## Real-World Example

Before running a t-test to compare salaries across gender, check:
- Are salaries approximately normal? (Histogram — likely right-skewed → use Mann-Whitney instead)
- Are variances similar? (Levene's test → use Welch's t-test if not)

Skipping these checks could produce a misleading p-value.

---

## 🔑 Key Takeaway

> Statistics is not just applying formulas. It is checking whether the formula is suitable for your data. Assumptions are the guardrails.

---

[← Day 54: Effect Size](day-54-effect-size.md) · [Next: Day 56 – Normality Assumption →](day-56-normality-assumption.md)
