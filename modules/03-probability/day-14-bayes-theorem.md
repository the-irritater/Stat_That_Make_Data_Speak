# Day 14: Bayes' Theorem

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand Bayes' Theorem, learn how to update prior probabilities (beliefs) with new evidence, and apply Bayesian thinking to classify emails or evaluate tests.

---

## The Concept
Bayes' Theorem is one of the most powerful tools in statistics. It allows us to update the probability of a hypothesis (H) given new evidence (E).

Key components of the formula:
- **Prior Probability, P(H):** Our baseline belief about the probability of the hypothesis before seeing the evidence.
- **Likelihood, P(E|H):** The probability of observing the evidence if the hypothesis is true.
- **Posterior Probability, P(H|E):** The updated probability of our hypothesis *after* observing the evidence.
- **Marginal Probability, P(E):** The total probability of observing the evidence under all possible hypotheses.

---

## Key Formulas
```
Bayes' Theorem: P(H|E) = [P(E|H) * P(H)] / P(E)
```
Where `P(E) = P(E|H)*P(H) + P(E|not H)*P(not H)`.

---

## Real-World Example
Suppose you run a spam filter. 
- You know that **5%** of all incoming emails are spam: `P(Spam) = 0.05`.
- Therefore, `P(Ham/Legit) = 0.95`.
- The word "FREE" appears in **80%** of spam emails: `P("FREE" | Spam) = 0.80`.
- The word "FREE" appears in **10%** of clean/legit emails: `P("FREE" | Ham) = 0.10`.

If a new email arrives containing the word "FREE", what is the probability that it is actually spam?
Using Bayes' Theorem:
- `P(Spam | "FREE") = [P("FREE" | Spam) * P(Spam)] / P("FREE")`
- `P("FREE") = P("FREE" | Spam)*P(Spam) + P("FREE" | Ham)*P(Ham)`
- `P("FREE") = (0.80 * 0.05) + (0.10 * 0.95) = 0.04 + 0.095 = 0.135` (13.5% of all emails contain "FREE").
- `P(Spam | "FREE") = (0.04) / 0.135 = 0.296` (29.6% probability).

**Business Insight:** Even though the word "FREE" appears in 80% of spam, if an email has the word "FREE", there is only a **29.6% chance it is spam**, because legit emails containing "FREE" are much more common overall (since 95% of your mail is legit). This prevents your filter from accidentally blocking important customer emails!

---

## Why This Step Matters
- **Classification Algorithms:** Forms the core of "Naive Bayes" classifiers used in sentiment analysis and spam filters.
- **Diagnostics Verification:** Essential for medical tests or fraud detection systems to understand "false positives."
- **A/B Testing Updates:** Allows continuous updating of campaign success probabilities as new clicks roll in (Bayesian A/B testing).

---

## Key Takeaway
> **Takeaway:** Bayes' Theorem teaches us that new evidence doesn't stand alone. To calculate the true probability of an event, you must always combine new evidence with prior baseline rates.

---

## See It Applied
→ [Do discounts increase repeat purchases?](../../applied/notebooks/05-do-discounts-work.ipynb) — Estimating likelihood of discount success based on baseline customer behaviors.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 13: Conditional Probability](day-13-conditional-probability.md) · [Next: Day 15 – Permutations and Combinations →](day-15-permutations-combinations.md)
