# Day 17: Binomial Distribution

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the assumptions of the binomial distribution, calculate the probability of a specific number of successes in a fixed number of trials, and apply it to conversions and click-through rates.

---

## The Concept
The **Binomial Distribution** is a discrete distribution that models the number of "successes" in a fixed number of independent trials, where each trial has only two possible outcomes: success or failure (often called Bernoulli trials).

Assumptions for a binomial experiment:
1. Fixed number of trials, `n`.
2. Each trial has only two outcomes (Success/Failure).
3. The probability of success, `p`, is constant across all trials.
4. The trials are independent.

---

## Key Formulas
```
Binomial Probability: P(X = k) = (n choose k) * p^k * (1 - p)^(n - k)

Mean (Expected Value): E(X) = n * p
Variance: Var(X) = n * p * (1 - p)
```
Where `n` is the number of trials, `k` is the number of successes, and `p` is the probability of success on a single trial.

---

## Real-World Example
Suppose you run a Facebook ad campaign.
- **Conversion Probability (p):** 5% (`0.05`) click-through rate.
- **Audience Sample (n):** 100 users see the ad.
- **Business Question:** What is the probability that **exactly 8 users** click the ad?

Using the Binomial formula:
- `P(X = 8) = (100 choose 8) * (0.05)^8 * (0.95)^92`
- Calculating this yields: `P(X = 8) = 0.065` (6.5% chance).
- The expected average clicks is: `100 * 0.05 = 5` clicks.

**Business Decision:** If your operations team needs at least 8 clicks to break even on the campaign cost, knowing there is only a 6.5% chance of hitting that target tells you that you need to increase your ad spend (n) or improve your ad copy (p) to make the campaign viable.

---

## Why This Step Matters
- **Digital Marketing ROI:** Models conversions, click-through rates, and email opens.
- **Quality Assurance:** Estimates the probability of finding `k` defective products in a batch of `n` items.
- **Risk Assessment:** Calculates the probability of credit card fraud occurrences within a set of transactions.

---

## Key Takeaway
> **Takeaway:** When outcomes are strictly binary (yes/no, convert/churn, click/ignore) and trials are independent, the binomial distribution is the correct statistical tool.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Modeling customer purchase rates under A/B test splits.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 16: Discrete vs Continuous Distributions](day-16-distributions-overview.md) · [Next: Day 18 – Normal Distribution →](day-18-normal-distribution.md)
