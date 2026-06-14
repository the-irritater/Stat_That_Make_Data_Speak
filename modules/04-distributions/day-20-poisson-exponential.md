# Day 20: Poisson and Exponential Distributions

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the Poisson and Exponential distributions, learn how they model events over time, and apply them to customer arrivals and service times.

---

## The Concept
When modeling time-based events (queues, system crashes, or customer arrivals), we use two closely related distributions:

| Distribution | Variable Type | What It Models | Example |
|---|---|---|---|
| **Poisson** | **Discrete** (Count) | The number of times an event occurs in a fixed interval of time or space. | How many customers walk into a store per hour? |
| **Exponential** | **Continuous** (Time) | The amount of time *between* consecutive events. | How many minutes pass between customer arrivals? |

These distributions are mathematically linked: if customer arrivals follow a Poisson distribution with an average rate of $\lambda$ arrivals per hour, then the time between those arrivals follows an Exponential distribution with a mean time of $1 / \lambda$.

---

## Key Formulas
```
Poisson Probability: P(X = k) = (lambda^k * e^(-lambda)) / k!

Exponential Probability (Cumulative): P(T <= t) = 1 - e^(-lambda * t)
```
Where `lambda` ($\lambda$) is the average rate of occurrence, `k` is the target count of events, and `t` is the target time limit.

---

## Real-World Example
Suppose you run a customer support call center:
- **Poisson Arrival Rate ($\lambda$):** Average of **12 calls per hour** (which is `12 / 60 = 0.2 calls per minute`).
- **Poisson Question:** What is the probability of receiving **exactly 15 calls** in a given hour?
  - `P(X = 15) = (12^15 * e^-12) / 15! = 0.072` (7.2% chance).
- **Exponential Question:** What is the probability that the time between two calls is **5 minutes or less**?
  - Here, $\lambda = 0.2$ calls per minute, $t = 5$ minutes.
  - `P(T <= 5) = 1 - e^(-0.2 * 5) = 1 - e^-1 = 1 - 0.368 = 0.632` (63.2% chance).

**Business Decision:** If you want to guarantee that a support agent is available with a wait time of less than 5 minutes, knowing there is a 63.2% chance of the next call coming in under 5 minutes allows you to staff the shift correctly to prevent queue build-up.

---

## Why This Step Matters
- **Queueing Theory & Staffing:** Essential for staffing retail registers, teller lines, or customer support lines.
- **Server Load Planning:** Models server network requests per second to scale cloud servers.
- **Equipment Reliability:** Exponential distribution models the "time to failure" for machinery or software servers.

---

## Key Takeaway
> **Takeaway:** Poisson counts the events in a time block; Exponential measures the time between those events. Together, they model the operational flow of any business.

---

## See It Applied
→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Visualizing transactional arrival counts.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 19: Central Limit Theorem](day-19-central-limit-theorem.md) · [Next: Day 21 – Confidence Intervals →](../05-inference/day-21-confidence-intervals.md)
