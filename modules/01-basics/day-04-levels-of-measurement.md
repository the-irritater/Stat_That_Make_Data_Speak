# Day 4: Levels of Measurement

*The measurement scale of your data decides which statistics you're allowed to use. Break this rule and your results mean nothing.*

---

## Learning Objective

Understand the four levels of measurement (NOIR) and how each level determines what operations and analyses are valid.

---

## The Concept

This is the rule most people skip — and then wonder why their analysis looks off.

Every variable in your dataset falls into one of **four measurement levels**. Each level allows different mathematical operations.

### The Four Levels (NOIR)

| Level | What It Measures | Can You... | Example |
|-------|-----------------|------------|---------|
| **Nominal** | Categories only | Count, mode | Product category, gender, city |
| **Ordinal** | Categories with order | + Rank, median | Customer rating (1-5), education level |
| **Interval** | Order + equal gaps, no true zero | + Add, subtract, mean | Temperature (°C), dates |
| **Ratio** | Order + equal gaps + true zero | + Multiply, divide, all stats | Revenue, age, weight, distance |

### The Key Insight

Each level **builds on** the previous:

```
Nominal  →  Can only count and categorize
   ↓
Ordinal  →  + Can rank and order
   ↓
Interval →  + Can measure exact differences
   ↓
Ratio    →  + Can say "twice as much" meaningfully
```

### Why This Matters in Practice

**The mistake:** "Our average product category is 2.3"

If you code categories as Electronics = 1, Clothing = 2, Food = 3, the average is technically 2.3. But that number is meaningless — you can't be "between Clothing and Food."

**The rule:** You can only use operations valid for your measurement level.

| Operation | Nominal | Ordinal | Interval | Ratio |
|-----------|:-------:|:-------:|:--------:|:-----:|
| Frequency count | Yes | Yes | Yes | Yes |
| Mode | Yes | Yes | Yes | Yes |
| Median | No | Yes | Yes | Yes |
| Mean | No | No | Yes | Yes |
| Ratios ("2× more") | No | No | No | Yes |

---

## Real-World Example

You're analyzing employee survey data:

| Column | Values | Level | Valid Analysis |
|--------|--------|-------|---------------|
| `department` | Sales, Engineering, HR | Nominal | "Most responses came from Sales" (mode) |
| `satisfaction` | Very Low, Low, Medium, High, Very High | Ordinal | "Median satisfaction is Medium" |
| `years_at_company` | 0.5, 1, 3, 7, 15 | Ratio | "Average tenure is 5.3 years; senior employees have 3× the tenure of juniors" |

If someone reports *"average satisfaction = 3.4"* — ask them what 3.4 means on a scale of "Very Low" to "Very High." It doesn't mean anything. The median is the right measure here.

---

## 🔑 Key Takeaway

> Before analyzing any variable, check its measurement level. Using the wrong statistic on the wrong level gives you numbers that look right but mean nothing.

---

[← Day 3: Population vs Sample](day-03-population-vs-sample.md) · [Next: Day 5 – Data Collection Methods →](day-05-data-collection-methods.md)
