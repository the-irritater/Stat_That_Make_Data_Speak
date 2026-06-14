# Day 53: Statistical vs Practical Significance

*A p-value below 0.05 does not mean the result matters in real life.*

---

## Learning Objective

Distinguish between statistical significance (unlikely due to chance) and practical significance (useful in the real world).

---

## The Concept

**Statistical significance** means there is enough evidence that the result is unlikely due to random chance (typically p < 0.05).

**Practical significance** means the result is large enough to matter in a real-world context.

### The critical difference:

| Scenario | Stat Significant? | Practically Useful? |
|----------|-------------------|-------------------|
| Button color change: conversion 10.00% → 10.05%, p = 0.03 | ✅ Yes | ❌ Too small to matter |
| New drug reduces hospital stay by 0.1 days, p = 0.001 | ✅ Yes | ❌ Not clinically meaningful |
| Training program increases sales by 25%, p = 0.04 | ✅ Yes | ✅ Large business impact |

### Why this happens:

With a very large sample, even tiny differences become statistically significant. A sample of 1 million can detect a 0.01% difference — but that doesn't make the difference important.

### The fix:

Always ask two questions:
1. Is the result statistically significant? (p-value)
2. Is the effect large enough to matter? (effect size, business context)

---

## Real-World Example

A website A/B test shows the new design increases click rate from 2.10% to 2.12% (p = 0.01). Statistically significant? Yes. Worth the engineering cost of deploying the new design? Probably not.

---

## 🔑 Key Takeaway

> A result can be statistically significant and still practically useless. Never stop at p-value — always ask: is the effect large enough to matter?

---

[← Day 52: Margin of Error](day-52-margin-of-error.md) · [Next: Day 54 – Effect Size →](day-54-effect-size.md)
