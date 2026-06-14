# Day 32: Structured vs Unstructured Data

*Not all data comes in neat tables. Knowing the difference changes how you approach analysis.*

---

## Learning Objective

Distinguish between structured and unstructured data, and understand why this distinction matters for choosing analysis methods.

---

## The Concept

**Structured data** is organized in rows and columns with a defined schema.

Examples: Excel sheets, SQL tables, CSV files, survey responses, transaction logs.

**Unstructured data** does not follow a fixed table format.

Examples: Images, videos, audio, emails, PDFs, social media posts, customer reviews, chat logs.

| Type | Format | Ready for Analysis? | Tools |
|------|--------|-------------------|-------|
| Structured | Rows & columns | Yes — directly | pandas, SQL, Excel |
| Unstructured | Free-form | No — needs processing | NLP, computer vision, AI |

### Why This Matters

Most traditional analytics tools (SQL, Excel, pandas) work with structured data. Unstructured data requires additional steps — text processing, image recognition, or AI models — before it becomes analyzable.

In the real world, an estimated 80% of data is unstructured.

---

## Real-World Example

A company's **sales table** (date, product, quantity, revenue) → structured data, ready for dashboards.

**Customer support emails** describing complaints → unstructured data, needs NLP to extract sentiment and topics.

---

## 🔑 Key Takeaway

> Structured data is ready for analysis. Unstructured data first needs to be converted into useful information. Knowing which type you have determines your entire approach.

---

[← Day 31: What Is a Dataset?](day-31-what-is-a-dataset.md) · [Next: Day 33 – Primary vs Secondary Data →](day-33-primary-vs-secondary-data.md)
