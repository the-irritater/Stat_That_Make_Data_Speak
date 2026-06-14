# Day 57: Homogeneity of Variance

*When comparing groups, don't just compare averages. Compare spread too.*

---

## Learning Objective

Understand the homogeneity of variance assumption, how to test it, and what to do when it is violated.

---

## The Concept

**Homogeneity of variance** (homoscedasticity) means different groups have similar variability (spread).

### Why it matters:

When comparing group means (t-test, ANOVA), the test assumes groups have similar variance. If one group is tightly clustered and another is widely scattered, the test's p-value may be unreliable.

### How to check:

| Method | Description |
|--------|------------|
| **Box plots** | Visual — compare box widths |
| **Levene's test** | Formal test; p < 0.05 → variances differ |
| **Bartlett's test** | More powerful but assumes normality |
| **Rule of thumb** | Largest variance < 4× smallest variance |

### What to do when violated:

- **t-test** → Use **Welch's t-test** (does not assume equal variance)
- **ANOVA** → Use **Welch's ANOVA** or **Games-Howell** post-hoc test
- **Regression** → Use **robust standard errors**

---

## Real-World Example

Comparing exam marks across three teaching methods:

| Method | Mean | Std Dev |
|--------|------|---------|
| Traditional | 72 | 8 |
| Online | 68 | 15 |
| Hybrid | 75 | 9 |

Online has nearly double the standard deviation. Levene's test p = 0.01. Variances are not equal. Use Welch's ANOVA instead of standard ANOVA.

---

## 🔑 Key Takeaway

> When comparing group means, also compare spread. Unequal variances require adjusted methods like Welch's test.

---

[← Day 56: Normality Assumption](day-56-normality-assumption.md) · [Next: Day 58 – Multicollinearity →](day-58-multicollinearity.md)
