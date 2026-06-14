# Day 39: Data Transformation

*Raw data is not always in the best form. Sometimes you need to reshape it before it can speak clearly.*

---

## Learning Objective

Understand common data transformation techniques and when to apply them to improve analysis quality.

---

## The Concept

Data transformation means converting data into a more useful format for analysis, visualization, or modeling.

### Common Transformations

| Technique | What It Does | When to Use |
|-----------|-------------|-------------|
| **Binning** | Group continuous values into categories | Age → Age groups (18–25, 26–35) |
| **Log transform** | Compress highly skewed data | Income, population data |
| **Encoding** | Convert categories to numbers | Gender → 0/1 for models |
| **Scaling** | Standardize variable ranges | Before ML algorithms |
| **Aggregation** | Summarize detail to higher level | Daily → Monthly totals |
| **Feature creation** | Create new columns from existing | Revenue = Price × Quantity |
| **Date extraction** | Pull month, year, day of week | Time-based patterns |

### Why Transform?

- **Visualization**: Grouped data is easier to chart than raw continuous values
- **Modeling**: Many algorithms need scaled or encoded inputs
- **Interpretation**: "25–34 age group spends 40% more" is clearer than raw age numbers
- **Reporting**: Stakeholders think in categories, not raw numbers

---

## Real-World Example

Instead of analyzing exact customer ages (23, 27, 31, 45, 52...), a company creates groups:

| Age Group | Count | Avg Spend |
|-----------|-------|-----------|
| 18–25 | 1,200 | ₹800 |
| 26–35 | 2,400 | ₹1,500 |
| 36–45 | 1,800 | ₹2,100 |
| 46+ | 900 | ₹1,900 |

Now the insight is clear: the 36–45 group has the highest average spend.

---

## 🔑 Key Takeaway

> Raw data is not always in the best form. Transformation reshapes data to reveal patterns, improve models, and support clearer decisions.

---

[← Day 38: Data Cleaning](day-38-data-cleaning.md) · [Next: Day 40 – Exploratory Data Analysis →](day-40-exploratory-data-analysis.md)
