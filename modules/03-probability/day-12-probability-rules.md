# Day 12: Probability Rules

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand and apply the addition and multiplication rules of probability to calculate the likelihood of multiple events occurring together or separately.

---

## The Concept
In business, we rarely look at events in isolation. We want to know the odds of multiple things happening:
- **Mutually Exclusive Events:** Events that cannot happen at the same time (e.g., a customer cannot pay with *only* credit card and *only* PayPal for the same order).
- **Independent Events:** The occurrence of one event does not affect the probability of the other (e.g., Customer A buying does not affect Customer B buying).
- **Dependent Events:** The occurrence of one event affects the probability of the next (e.g., a customer putting an item in their cart increases their probability of buying).

---

## Key Formulas
```
Addition Rule (OR):
- Mutually Exclusive: P(A or B) = P(A) + P(B)
- General Rule: P(A or B) = P(A) + P(B) - P(A and B)

Multiplication Rule (AND):
- Independent: P(A and B) = P(A) * P(B)
- Dependent: P(A and B) = P(A) * P(B|A)
```
Where `P(B|A)` represents the conditional probability of B given that A has occurred.

---

## Real-World Example
Suppose you run an e-commerce website where:
- The probability of a customer checking out using a credit card is `P(Card) = 0.60`.
- The probability of checking out using PayPal is `P(PayPal) = 0.30`.
- (These are mutually exclusive: they choose only one at checkout).

Using the Addition Rule:
- The probability that a customer pays with card OR PayPal is:
  - `P(Card or PayPal) = 0.60 + 0.30 = 0.90` (90% probability).
  - The remaining 10% represent other payment methods (like bank transfer).

Now suppose the checkout page has two independent servers, A and B. The crash rate of Server A is `0.01` and Server B is `0.02`.
Using the Multiplication Rule, the probability of **both** servers crashing at the same time is:
- `P(A and B crash) = P(A) * P(B) = 0.01 * 0.02 = 0.0002` (0.02% chance).

This calculation justifies why redundant backup servers are critical for operational stability.

---

## Why This Step Matters
- **Avoids Double Counting:** The general addition rule subtracts `P(A and B)` so you don't count overlapping users twice.
- **Redundancy & Reliability Planning:** Multiplication rules help calculate system failure rates.
- **Funnel Analysis:** Multiplication rules for dependent events model multi-step conversion funnels.

---

## Key Takeaway
> **Takeaway:** Use the addition rule (add probabilities) when evaluating "either/or" choices, and the multiplication rule (multiply probabilities) when evaluating "both/and" scenarios.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Visualizing cross-probabilities of groups.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 11: Introduction to Probability](day-11-intro-to-probability.md) · [Next: Day 13 – Conditional Probability →](day-13-conditional-probability.md)
