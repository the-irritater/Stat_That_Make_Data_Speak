# Day 6: Mean, Median, and Mode

*Your path to becoming a data-driven decision maker.*

---

## Learning Objective
Understand the three measures of central tendency, know when each one lies, and choose the correct one for real-world business datasets.

---

## The Concept
When summarizing a dataset, you want a single number that represents the "center" or "typical value." We use central tendency:

| Measure | What It Is | Best Used For | Weakness |
|---|---|---|---|
| **Mean** | The mathematical average (sum divided by count) | Symmetric, continuous data without outliers | Easily distorted by extreme values (outliers) |
| **Median** | The exact middle value (50th percentile) | Skewed data (e.g., salaries, house prices) | Ignores the actual values of extreme data points |
| **Mode** | The most frequently occurring value | Categorical data (e.g., shirt sizes, payment methods) | Can have multiple modes (multimodal) or no mode at all |

---

## Key Formulas
```
Mean: x_bar = (sum of all x_i) / n
Median: Middle value of sorted data
Mode: Value with highest count
```
Where `x_i` represents each data point and `n` represents the sample size.

---

## Real-World Example
Imagine you manage a team of 5 software engineers. Their annual salaries are:
`$50k, $52k, $55k, $58k, and $450k (the CEO/Founder)`

- **Mean salary:** `($50k + $52k + $55k + $58k + $450k) / 5 = $133,000`
- **Median salary:** `$55,000` (sorted middle)

If a recruiter claims "the average salary on this team is $133k," they are technically correct but practically misleading. The founder's high salary inflates the mean. The **median ($55k)** is a far more honest representation of a typical engineer's salary.

---

## Why This Step Matters
- **Avoids misleading metrics:** Prevents you from reporting an "average" that is heavily skewed by a single outlier.
- **Improves business forecasting:** Ensures inventory or staffing is planned around typical customer behaviors, not extreme exceptions.
- **Refines targeting:** Helps identify the most common customer choices (mode) for marketing campaigns.

---

## Key Takeaway
> **Takeaway:** Never trust a single "average." If your data has outliers or is skewed, the median is your best friend.

---

## See It Applied
→ [Analyzing customer spending patterns](../../applied/notebooks/02-customer-spending-patterns.ipynb) — Using mean and median to understand order values.

---

**Author:** StatSphere (Sanman Kadam) | MSc Statistics | Data Analytics | Making Data Make Sense

[← Back to Module 2](README.md) · [Next: Day 7 – Range, Variance, and Standard Deviation →](day-07-range-variance-std-dev.md)
