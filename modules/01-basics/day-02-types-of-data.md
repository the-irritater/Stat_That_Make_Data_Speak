# Day 2: Types of Data

*Not all data is created equal. The type of data you have determines what you can do with it.*

---

## Learning Objective

Learn to identify whether your data is qualitative or quantitative — and why this distinction changes everything about your analysis.

---

## The Concept

Before you calculate a single number, you need to answer one question:

**What kind of data am I looking at?**

Get this wrong, and your entire analysis breaks.

### The Two Main Types

| Type | What It Is | Examples |
|------|-----------|----------|
| **Qualitative (Categorical)** | Describes qualities or categories | Gender, product category, city, color |
| **Quantitative (Numerical)** | Measures quantities with numbers | Revenue, age, temperature, order count |

### Going Deeper

Each type splits further:

**Qualitative:**
- **Nominal** → No natural order (e.g., product categories: Electronics, Clothing, Food)
- **Ordinal** → Has a natural order (e.g., customer rating: Poor, Average, Good, Excellent)

**Quantitative:**
- **Discrete** → Countable values (e.g., number of orders: 1, 2, 3…)
- **Continuous** → Measurable values on a scale (e.g., revenue: ₹1,204.50)

```
Data
├── Qualitative (Categorical)
│   ├── Nominal    → no order (colors, names, categories)
│   └── Ordinal    → ordered (ratings, rankings)
│
└── Quantitative (Numerical)
    ├── Discrete   → countable (orders, clicks, items)
    └── Continuous  → measurable (revenue, time, weight)
```

---

## Real-World Example

You're analyzing an e-commerce dataset. Here's what you see:

| Column | Example Value | Data Type | Why It Matters |
|--------|--------------|-----------|----------------|
| `customer_id` | C-10042 | Nominal | Can't average this — it's a label |
| `satisfaction` | "Good" | Ordinal | Can rank but can't do math on it |
| `num_orders` | 7 | Discrete | Can calculate average orders per customer |
| `total_spend` | ₹4,320.50 | Continuous | Can calculate mean, median, run regression |

**The mistake people make:** treating categorical data like numbers.

If customer satisfaction is coded as 1, 2, 3, 4 — it's tempting to average it. But "average satisfaction = 2.7" doesn't actually mean anything concrete. The gap between "Poor" (1) and "Average" (2) isn't necessarily the same as between "Good" (3) and "Excellent" (4).

---

## 🔑 Key Takeaway

> Always identify your data type before choosing an analysis method. The wrong method on the wrong data type gives you a confident but completely wrong answer.

---

## See It Applied

→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — See how we identify data types in a real dataset using Python

---

[← Day 1: What Is Statistics?](day-01-what-is-statistics.md) · [Next: Day 3 – Population vs Sample →](day-03-population-vs-sample.md)
