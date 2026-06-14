# Day 40: Exploratory Data Analysis

*Don't jump to modeling. First understand what the data is telling you.*

---

## Learning Objective

Understand the purpose and process of Exploratory Data Analysis (EDA) — the essential first step in any data project.

---

## The Concept

**Exploratory Data Analysis (EDA)** means systematically examining data to understand its structure, patterns, anomalies, and relationships before applying any formal models or tests.

### The EDA Checklist

| Question | How to Answer |
|----------|-------------|
| What variables exist? | `.info()`, `.columns` |
| What are the data types? | `.dtypes` |
| Are there missing values? | `.isnull().sum()` |
| What do distributions look like? | Histograms, box plots |
| Are there outliers? | Box plots, IQR, z-scores |
| Which variables are related? | Scatter plots, correlation matrix |
| Is the data balanced? | Value counts, class distribution |
| What are the summary statistics? | `.describe()` |

### EDA Is Not Optional

Without EDA, you risk:
- Building models on data you don't understand
- Missing obvious errors or patterns
- Choosing inappropriate statistical methods
- Presenting misleading conclusions

### The Order

1. **Structure** → shape, types, missing values
2. **Univariate** → distribution of each variable alone
3. **Bivariate** → relationships between pairs of variables
4. **Multivariate** → patterns across multiple variables

---

## Real-World Example

Before predicting house prices, you first explore:
- Price distribution → right-skewed, may need log transform
- Area vs price → positive relationship in scatter plot
- Location → some neighborhoods have much higher prices
- Outliers → a ₹50 crore mansion in a ₹30 lakh neighborhood

This 30-minute EDA prevents hours of debugging a bad model.

---

## 🔑 Key Takeaway

> Good analysis starts with asking what the data is saying. EDA is not a step you skip — it is the step that makes everything else work.

---

## See It Applied

→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — Full EDA in action

---

[← Day 39: Data Transformation](day-39-data-transformation.md) · [Back to Module 7](README.md)
