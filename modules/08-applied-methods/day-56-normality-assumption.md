# Day 56: Normality Assumption

*Perfect bell curves are rare in real data. The question is: is it close enough?*

---

## Learning Objective

Understand the normality assumption, how to check it, and when it matters most.

---

## The Concept

The **normality assumption** requires that the data (or residuals) follow an approximately normal (bell-shaped) distribution.

### How to check:

| Method | What to Look For |
|--------|-----------------|
| **Histogram** | Roughly bell-shaped |
| **Q-Q Plot** | Points follow the diagonal line |
| **Shapiro-Wilk test** | p > 0.05 suggests normality |
| **Skewness & Kurtosis** | Both near 0 |

### When normality matters most:

- **Small samples** (n < 30) — the Central Limit Theorem hasn't kicked in
- **t-tests and ANOVA** — especially with small groups
- **Confidence intervals** — rely on normal distribution

### When normality matters less:

- **Large samples** (n > 30) — CLT makes means approximately normal regardless
- **Regression** — normality of residuals matters, not the variables themselves
- **Non-parametric tests** — don't assume normality at all

---

## Real-World Example

Student marks: histogram shows a roughly bell-shaped pattern with slight left skew. Shapiro-Wilk p = 0.12 (not significant → normality not rejected). The t-test is appropriate.

But income data: heavily right-skewed, Shapiro-Wilk p < 0.001. Here, use median instead of mean, and consider a non-parametric test.

---

## 🔑 Key Takeaway

> Normality is not about perfection. It is about whether the data is close enough for the method to work reasonably. Always check, especially with small samples.

---

[← Day 55: Assumptions in Statistics](day-55-assumptions-in-statistics.md) · [Next: Day 57 – Homogeneity of Variance →](day-57-homogeneity-of-variance.md)
