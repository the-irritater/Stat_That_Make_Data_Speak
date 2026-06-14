# Day 48: Confounding Variable

*Just because two things move together does not mean one causes the other.*

---

## Learning Objective

Understand confounding variables — hidden factors that create spurious relationships — and how to identify them.

---

## The Concept

A **confounding variable** (confounder) is a variable that influences both the independent and dependent variable, creating a false impression of a direct relationship.

### The classic example:

| Observation | Real Cause |
|-------------|-----------|
| Ice cream sales ↑ and drowning ↑ | Summer (heat) drives both |
| Countries with more TVs have higher life expectancy | Wealth drives both |
| Students with bigger feet read better | Age drives both |

### How to handle confounders:

| Method | How |
|--------|-----|
| **Control for it** | Add the confounder to regression |
| **Stratification** | Analyze within subgroups |
| **Randomization** | Experimental design (RCT) |
| **Domain knowledge** | Ask: what else could explain this? |

### The key question:

Before claiming "X causes Y", always ask: **Is there a third variable influencing both X and Y?**

---

## Real-World Example

A marketing team finds: customers who receive emails spend more. But the confounder is customer loyalty — loyal customers both opt into emails AND spend more. The emails may not be causing higher spending at all.

---

## 🔑 Key Takeaway

> Before saying "X causes Y", check whether a third variable is influencing both. Confounders are the most common source of wrong conclusions in data analysis.

---

[← Day 47: Simpson's Paradox](day-47-simpsons-paradox.md) · [Next: Day 49 – Bias in Data →](day-49-bias-in-data.md)
