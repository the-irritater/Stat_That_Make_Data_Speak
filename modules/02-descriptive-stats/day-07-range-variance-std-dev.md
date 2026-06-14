# Day 7: Range, Variance, and Standard Deviation

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand how to measure the spread (dispersion) of your data using range, variance, and standard deviation to assess consistency and risk.

---

## The Concept
Knowing the center of your data (mean/median) is only half the story. You also need to know how "spread out" the numbers are. Two datasets can have the exact same mean but completely different behaviors.

| Measure | What It Is | Pros | Cons |
|---|---|---|---|
| **Range** | The difference between Maximum and Minimum | Extremely simple to calculate | Highly sensitive to a single outlier |
| **Variance** | The average squared distance from the Mean | Great for mathematical modeling | Hard to interpret because the units are squared |
| **Standard Deviation** | The square root of the variance | In the original units of your data; highly interpretable | Influenced by outliers |

---

## Key Formulas
```
Range = Max - Min

Sample Variance: s^2 = sum(x_i - x_bar)^2 / (n - 1)

Sample Standard Deviation: s = sqrt(s^2)
```
Where `x_bar` is the sample mean, `x_i` is each data point, and `n` is the sample size. We divide by `n - 1` (Bessel's correction) to get an unbiased estimate of the population variance.

---

## Real-World Example
You are evaluating two shipping companies (A and B) to deliver e-commerce packages. Both companies have an **average delivery time of 3 days**.

- **Company A:** Delivery times are `2.9, 3.0, 3.1, 3.0, 3.0 days`. (Std Dev = 0.07 days)
- **Company B:** Delivery times are `1.0, 5.0, 1.0, 4.0, 4.0 days`. (Std Dev = 1.73 days)

Even though both have the same mean, **Company A is highly consistent**, while **Company B is highly unpredictable**. If consistency matters to your customers, you should choose Company A.

---

## Why This Step Matters
- **Risk Assessment:** Helps quantify volatility in financial investments or sales forecasts.
- **Quality Control:** Essential in manufacturing and operations to detect inconsistent processes.
- **Data Auditing:** A high standard deviation relative to the mean flags potential issues or outliers.

---

## Key Takeaway
> **Takeaway:** The mean tells you where your data lands on average, but the standard deviation tells you how reliable that average actually is.

---

## See It Applied
→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Visualizing distributions and calculating baseline spread.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Day 6: Mean, Median, and Mode](day-06-mean-median-mode.md) · [Next: Day 8 – Percentiles and Quartiles →](day-08-percentiles-quartiles.md)
