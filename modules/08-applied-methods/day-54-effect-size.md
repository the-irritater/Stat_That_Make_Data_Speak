# Day 54: Effect Size

*The p-value tells you IF there is a difference. Effect size tells you HOW MUCH.*

---

## Learning Objective

Understand effect size as a complement to p-values, and why reporting it makes analysis more honest and useful.

---

## The Concept

**Effect size** measures the magnitude of a difference or relationship, independent of sample size.

### Common measures:

| Measure | What It Compares | Interpretation |
|---------|-----------------|---------------|
| **Cohen's d** | Difference between two means | Small: 0.2, Medium: 0.5, Large: 0.8 |
| **Pearson's r** | Correlation strength | Small: 0.1, Medium: 0.3, Large: 0.5 |
| **Eta-squared (η²)** | Variance explained (ANOVA) | Small: 0.01, Medium: 0.06, Large: 0.14 |
| **Odds Ratio** | Relative odds between groups | 1 = no difference |

### Why effect size matters:

- **p-value** depends on sample size — large samples make tiny differences significant
- **Effect size** is independent of sample size — it measures actual magnitude
- Together they give the complete picture: "Is there a difference?" + "How big?"

### Reporting standard:

Modern research guidelines (APA) recommend reporting both p-values AND effect sizes.

---

## Real-World Example

Two teaching methods compared: Method B scores higher (p = 0.03, Cohen's d = 0.15).

The difference is statistically significant but the effect size is small (d = 0.15). Switching all courses to Method B would be costly for a trivial improvement.

Compare with: Method C (p = 0.02, Cohen's d = 0.85). Same significance level, but a large effect. This one is worth implementing.

---

## 🔑 Key Takeaway

> p-value answers: Is there evidence of a difference? Effect size answers: How much difference is there? Both are needed for honest analysis.

---

[← Day 53: Statistical vs Practical Significance](day-53-statistical-vs-practical-significance.md) · [Next: Day 55 – Assumptions in Statistics →](day-55-assumptions-in-statistics.md)
