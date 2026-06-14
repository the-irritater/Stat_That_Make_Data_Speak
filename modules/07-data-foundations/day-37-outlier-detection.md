# Day 37: Outlier Detection

*Not every extreme value is wrong. Some are your most important findings.*

---

## Learning Objective

Understand what outliers are, how to detect them, and when to keep vs remove them.

---

## The Concept

An **outlier** is a value that is unusually high or low compared to the rest of the data.

### Common Detection Methods

| Method | How It Works | Best For |
|--------|-------------|----------|
| **IQR Rule** | Values below Q1−1.5×IQR or above Q3+1.5×IQR | General use |
| **Z-Score** | Values more than 2–3 standard deviations from mean | Normal distributions |
| **Box Plot** | Visual identification of points beyond whiskers | Quick exploration |
| **Domain Knowledge** | Is this value possible in context? | Always applicable |

### The Decision Framework

Before removing any outlier, ask:

1. **Is it a data entry error?** → Fix or remove
2. **Is it a measurement error?** → Investigate the source
3. **Is it a genuine extreme value?** → Keep it — it may be your most important finding
4. **Does it affect your analysis significantly?** → Report results with and without it

A very high transaction might be fraud. A sudden sales spike might be a festival offer. A very high test score might indicate exceptional performance.

---

## Real-World Example

Salaries: ₹25K, ₹28K, ₹30K, ₹32K, ₹5,00,000

The ₹5,00,000 is an outlier. It pulls the mean to ₹1,23,000 — far from what any typical employee earns. The median (₹30K) tells the real story.

But the outlier might be the CEO's salary — a legitimate data point that shouldn't be deleted.

---

## 🔑 Key Takeaway

> Do not delete outliers blindly. First check whether they are errors or meaningful signals. Sometimes the outlier IS the story.

---

[← Day 36: Missing Values](day-36-missing-values.md) · [Next: Day 38 – Data Cleaning →](day-38-data-cleaning.md)
