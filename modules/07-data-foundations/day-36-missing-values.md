# Day 36: Missing Values

*Missing values are not just empty cells. They are signals that need investigation.*

---

## Learning Objective

Understand why data goes missing, the different types of missingness, and common strategies for handling it.

---

## The Concept

Missing values occur when data points are not recorded. They appear as blank cells, NA, NULL, NaN, or empty strings.

### Types of Missingness

| Type | Meaning | Example |
|------|---------|---------|
| **MCAR** (Missing Completely At Random) | No pattern to what's missing | Sensor randomly fails |
| **MAR** (Missing At Random) | Missingness depends on other observed data | High-income people skip income question |
| **MNAR** (Missing Not At Random) | Missingness depends on the missing value itself | Depressed people skip mental health survey |

### Common Handling Strategies

1. **Remove** rows with missing values (if few and MCAR)
2. **Fill** with mean, median, or mode (simple but can distort distributions)
3. **Use domain knowledge** (e.g., missing payment = no purchase)
4. **Statistical imputation** (KNN, regression, multiple imputation)

### The Rule

Before filling any missing value, ask: **Why is this value missing?**

Blindly filling without understanding the reason can introduce bias.

---

## Real-World Example

In a student survey, 30% of respondents skip the family income question. This is likely not random — students from lower-income families may avoid the question. Filling these with the average income would overestimate and create misleading analysis.

---

## 🔑 Key Takeaway

> Missing values are not just gaps to fill. They carry information about why data was not collected. Understanding the reason determines the right handling strategy.

---

[← Day 35: Clean Data vs Messy Data](day-35-clean-data-vs-messy-data.md) · [Next: Day 37 – Outlier Detection →](day-37-outlier-detection.md)
