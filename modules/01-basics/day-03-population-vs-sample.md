# Day 3: Population vs Sample

*You almost never have all the data. And that's fine — if you sample correctly.*

---

## Learning Objective

Understand the critical difference between population and sample, and why getting this wrong leads to misleading conclusions.

---

## The Concept

This is the concept that separates people who *use* data from people who *understand* data.

### The Core Distinction

| Term | Definition | Example |
|------|-----------|---------|
| **Population** | The *entire* group you want to learn about | All customers of your company (500,000) |
| **Sample** | A *subset* of the population you actually study | 2,000 customers you surveyed |

**Why does this matter?**

Because in the real world, you almost never have access to the full population.

- You can't survey every customer
- You can't test every product
- You can't analyze every transaction in real-time

So you take a **sample** and use it to **infer** things about the population.

The entire field of inferential statistics exists because of this gap.

### The Notation Difference

This trips up many beginners:

| Measure | Population (parameter) | Sample (statistic) |
|---------|----------------------|-------------------|
| Mean | μ (mu) | x̄ (x-bar) |
| Standard Deviation | σ (sigma) | s |
| Size | N | n |

When you see μ vs x̄ in a formula, that's telling you: "Are we talking about everyone, or just the people we measured?"

### What Can Go Wrong

**Sampling bias** = when your sample doesn't represent the population.

Classic example:
- You want to know if customers like your new app feature
- You survey only customers who contacted support
- Result: 80% are unhappy
- Reality: You only sampled the frustrated ones — the happy majority never reached out

Your data was technically correct. Your conclusion was completely wrong.

---

## Real-World Example

**Scenario:** An online retailer wants to know the average customer spend.

| Approach | What They Did | Result | Problem |
|----------|--------------|--------|---------|
| **Population** | Analyzed all 500K transactions | Mean = ₹1,847 | Took 3 days to process |
| **Random Sample** | Randomly picked 2,000 transactions | Mean = ₹1,832 | 99% as accurate, done in 10 seconds |
| **Biased Sample** | Only looked at premium tier customers | Mean = ₹4,200 | Completely misleading |

The random sample got them 99% of the accuracy in 0.001% of the time.

That's the power of good sampling — and the danger of bad sampling.

---

## 🔑 Key Takeaway

> A well-chosen sample of 2,000 tells you more truth than a biased dataset of 200,000. Statistics isn't about having all the data — it's about having the *right* data.

---

## See It Applied

→ [Analyzing customer spending patterns](../../applied/notebooks/02-customer-spending-patterns.ipynb) — Watch how sample statistics approximate population parameters

---

[← Day 2: Types of Data](day-02-types-of-data.md) · [Next: Day 4 – Levels of Measurement →](day-04-levels-of-measurement.md)
