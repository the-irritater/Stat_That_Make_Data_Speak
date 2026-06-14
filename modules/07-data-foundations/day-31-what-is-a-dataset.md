# Day 31: What Is a Dataset?

*Every data project starts with the same thing: a table of rows and columns. But what do they actually mean?*

---

## Learning Objective

Understand the basic structure of a dataset — rows as observations, columns as variables — and why this matters before any analysis.

---

## The Concept

A dataset is a collection of data arranged in a structured form, typically a table.

**Rows** represent individual observations — each person, transaction, event, or record.
**Columns** represent variables — the characteristics being measured (age, salary, city, score).

Think of it this way:

- A student survey with 500 responses and 10 questions → **500 rows × 10 columns**
- A sales report with 10,000 transactions and 8 fields → **10,000 rows × 8 columns**

Before creating any chart, dashboard, model, or test, you need to understand the dataset's structure:

| Question | Why It Matters |
|----------|---------------|
| How many rows? | Size of your data |
| How many columns? | Number of variables |
| What data types? | Determines which methods work |
| Any missing values? | Affects accuracy |

---

## Real-World Example

Imagine you receive a CSV file with customer data. Before running any analysis, you check:

- 5,000 rows → 5,000 customers
- 12 columns → name, email, city, age, purchase_amount, date, etc.
- 3 columns have missing values → need investigation

This 2-minute check saves hours of debugging later.

---

## 🔑 Key Takeaway

> A dataset is not just a table. It is the starting point of every data-driven decision. Understanding its structure is always step one.

---

## See It Applied

→ [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb) — First step: understand the data structure

---

[← Back to Module 7](README.md) · [Next: Day 32 – Structured vs Unstructured Data →](day-32-structured-vs-unstructured-data.md)
