# Day 15: Permutations and Combinations

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how permutations and combinations count potential outcomes in a sample space, and apply them to audit possibilities or calculate probability denominators.

---

## The Concept
Before calculating the probability of an event, you need to know: *How many total ways can things happen?* We use counting principles:
- **Factorial (n!):** The number of ways to arrange `n` items in a line (e.g. 3! = 3 * 2 * 1 = 6).
- **Permutation:** The number of ways to choose and arrange `r` items from a group of `n` items **where order matters** (e.g. creating passwords, ranking top 3 employees).
- **Combination:** The number of ways to choose `r` items from a group of `n` items **where order does not matter** (e.g. choosing a committee, selecting items for a bundle).

---

## Key Formulas
```
Permutations (Order Matters): nPr = n! / (n - r)!

Combinations (Order Doesn't Matter): nCr = n! / [r! * (n - r)!]
```
Where `n` is the total pool size, and `r` is the number of items being selected.

---

## Real-World Example
Suppose a retail store has **10 products** and wants to design a promotional "bundle of 3 products." How many unique bundles can they create?
- Since order does not matter in a bundle (Product A, B, and C is the same bundle as B, C, and A), we use **Combinations (nCr)**.

Using the Combination formula:
- `n = 10` (total products)
- `r = 3` (selected size)
- `10C3 = 10! / [3! * (10 - 3)!] = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120` unique bundles.

If the store wanted to arrange these 3 products in a specific layout on their homepage banner (Top 1, Top 2, Top 3), order **would** matter. They would use **Permutations (nPr)**:
- `10P3 = 10! / (10 - 3)! = 10 * 9 * 8 = 720` unique layouts.

**Business Decision:** Counting the unique options (120 bundles) helps the operations team estimate inventory setup costs before committing to a campaign.

---

## Why This Step Matters
- **Denominator Calculation:** Provides the total possible outcomes (sample space size) for classical probability calculations.
- **A/B Testing Randomization:** Helps calculate how many ways users can be split into groups.
- **Complexity Assessment:** Crucial for estimating the time required to run brute-force optimization codes.

---

## Key Takeaway
> **Takeaway:** Permutations are for arrangements (order matters), and combinations are for selections (order doesn't matter).

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Setting up proper A/B test contingency sizes.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 14: Bayes' Theorem](day-14-bayes-theorem.md) · [Next: Day 16 – Discrete vs Continuous Distributions →](../04-distributions/day-16-distributions-overview.md)
