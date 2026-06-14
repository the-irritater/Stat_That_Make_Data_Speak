# Day 13: Conditional Probability

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how conditional probability measures the likelihood of an event occurring given that another event has already occurred, and use it to model dependencies.

---

## The Concept
In the real world, events are rarely completely independent. Knowing that one thing has happened changes the odds of another:
- **Unconditional Probability:** The probability of an event on its own, `P(A)` (e.g., probability of a user converting).
- **Conditional Probability:** The probability of event B occurring *given* that event A has already occurred, written as `P(B|A)` (read as: "probability of B given A").

If `P(B|A) = P(B)`, then events A and B are **independent** (knowing A happened gives zero new info about B). Otherwise, they are **dependent**.

---

## Key Formulas
```
Conditional Probability: P(B|A) = P(A and B) / P(A)
```
Where `P(A) > 0`. This is the probability that both events A and B happen, scaled relative to the probability of the given event A.

---

## Real-World Example
A digital marketer analyzes website traffic:
- The overall probability that any visitor makes a purchase is `P(Purchase) = 0.03` (3% conversion rate).
- The probability that a visitor signs up for the newsletter is `P(Newsletter) = 0.10` (10%).
- The probability that a visitor signs up for the newsletter **and** makes a purchase is `P(Newsletter and Purchase) = 0.02` (2%).

Using the conditional probability formula:
- The probability that a visitor makes a purchase **given** they signed up for the newsletter is:
  - `P(Purchase | Newsletter) = P(Newsletter and Purchase) / P(Newsletter)`
  - `P(Purchase | Newsletter) = 0.02 / 0.10 = 0.20` (20% conversion rate).

**Business Decision:** Visitors who subscribe to your newsletter are **6.6× more likely to buy** (20% vs. 3% overall). Marketing should heavily prioritize newsletter signups!

---

## Why This Step Matters
- **Identifies Crucial Behaviors:** Quantifies which micro-conversions (e.g., viewing a demo) lead to actual macro-conversions (buying).
- **Enables Recommendation Engines:** Calculates the odds of a user buying Product B given they bought Product A (association rules).
- **Risk Assessment:** Estimates credit default risk given credit score history.

---

## Key Takeaway
> **Takeaway:** Conditional probability allows you to update risk and opportunity assessments based on context rather than relying on raw averages.

---

## See It Applied
→ [Who are our best buyers?](../../applied/notebooks/06-who-are-best-buyers.ipynb) — Calculating likelihood of high spending based on customer segments.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 12: Probability Rules](day-12-probability-rules.md) · [Next: Day 14 – Bayes' Theorem →](day-14-bayes-theorem.md)
