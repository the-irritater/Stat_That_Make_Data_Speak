# Day 11: Introduction to Probability

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the core definitions of probability, outcomes, sample spaces, and events, and learn how to quantify uncertainty in business environments.

---

## The Concept
Probability is the mathematical study of uncertainty. It quantifies the likelihood that a particular event will occur, ranging from `0` (impossible event) to `1` (certain event).

Key terms you need to know:
- **Experiment:** An action or process that results in one of several outcomes (e.g., a customer visiting a website).
- **Outcome:** A single result of an experiment (e.g., the customer buys, or the customer leaves).
- **Sample Space (S):** The set of all possible outcomes.
- **Event (A):** A subset of the sample space we want to measure.
- **Complement (A'):** The probability of an event *not* occurring.

---

## Key Formulas
```
Classical Probability: P(A) = Number of Favorable Outcomes / Total Outcomes in S

Complement Rule: P(A') = 1 - P(A)
```
Where `P(A)` represents the probability of event A.

---

## Real-World Example
Suppose you run an email campaign sending product newsletters to 1,000 subscribers.
- **Sample Space (S):** All 1,000 subscribers.
- **Event (A):** A subscriber clicks the link in the email.
- **Outcomes:** 80 subscribers click the link.

Using the classical probability formula:
- `P(Click) = 80 / 1000 = 0.08` (8% click-through rate)
- Using the Complement Rule, the probability that a subscriber **does not click** is:
  - `P(No Click) = 1 - 0.08 = 0.92` (92%)

This simple ratio is the foundation of all digital marketing analytics.

---

## Why This Step Matters
- **Quantifies Risk:** Allows businesses to estimate success or failure rates before launching initiatives.
- **Establishes Baselines:** Provides the probability boundaries needed to measure if a new strategy creates a "lift."
- **Forms the Basis of Inference:** All hypothesis tests and machine learning predictions are built on top of probability.

---

## Key Takeaway
> **Takeaway:** Probability is the language of risk. By expressing outcomes as numbers between 0 and 1, we replace intuition with measurement.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Calculating empirical probability of repeat purchases.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Back to Module 3](README.md) · [Next: Day 12 – Probability Rules →](day-12-probability-rules.md)
