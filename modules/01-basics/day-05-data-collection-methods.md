# Day 5: Data Collection Methods

*Garbage in, garbage out. How you collect data decides whether your analysis is trustworthy or misleading.*

---

## Learning Objective

Understand the main methods of data collection, their trade-offs, and how collection bias can silently ruin your analysis.

---

## The Concept

You can have the best analysis tools in the world. If your data was collected poorly, your conclusions are worthless.

**Data collection** is the first step in any statistical study — and it's where most errors are introduced.

### Primary vs Secondary Data

| Type | What It Is | Pros | Cons |
|------|-----------|------|------|
| **Primary** | Data you collect yourself | Designed for your question, high control | Expensive, time-consuming |
| **Secondary** | Data someone else collected | Cheap, fast, often large-scale | May not fit your exact question |

As a data analyst, you'll mostly work with **secondary data** (company databases, APIs, public datasets). But understanding primary collection helps you spot problems in any dataset.

### Common Collection Methods

| Method | How It Works | Best For | Watch Out For |
|--------|-------------|----------|---------------|
| **Survey** | Ask people questions | Opinions, preferences | Response bias (people lie or don't respond) |
| **Observation** | Watch and record behavior | User behavior, processes | Observer effect (people act differently when watched) |
| **Experiment** | Control conditions, test outcomes | Causal relationships | Expensive, ethical constraints |
| **Existing Data** | Use databases, logs, APIs | Large-scale analysis | May be messy, incomplete, or biased |

### The Sampling Methods That Matter

When collecting from a population, **how** you choose your sample is critical:

| Method | How It Works | When To Use |
|--------|-------------|-------------|
| **Simple Random** | Everyone has equal chance of being selected | General purpose, unbiased |
| **Stratified** | Divide population into groups, sample from each | When subgroups matter (e.g., sample from each age group) |
| **Convenience** | Sample whoever is easiest to reach | Quick insights (but often biased) |
| **Systematic** | Pick every nth item | Large datasets, production lines |

### The Bias Problem

Every collection method introduces potential bias:

- **Selection bias** → Your sample doesn't represent the population
- **Response bias** → People answer what they think you want to hear
- **Survivorship bias** → You only see the data that "survived" (e.g., only analyzing successful companies)
- **Measurement bias** → Your tool measures incorrectly (e.g., broken sensor, ambiguous survey question)

---

## Real-World Example

**Scenario:** A food delivery app wants to know customer satisfaction.

| Method | What They Did | Result | Hidden Bias |
|--------|--------------|--------|-------------|
| In-app popup | Asked right after delivery | 4.5/5 stars | Only reached customers who opened the app again |
| Email survey | Sent survey 2 days later | 3.8/5 stars | Only engaged users open emails |
| Support ticket analysis | Analyzed complaint tickets | 2.1/5 stars | Only captured unhappy customers |
| Random phone survey | Called 500 random customers | 4.0/5 stars | Most representative, but expensive |

**Same company. Same question. Four different answers.**

The "right" answer depends on which bias you can tolerate.

---

## 🔑 Key Takeaway

> Before trusting any dataset, ask: "How was this data collected?" and "Who is missing from this data?" The answers tell you more about the reliability of your conclusions than any statistical test ever will.

---

## Module Complete!

You've finished the foundations. You now understand:

- What statistics is and why it matters
- How to identify data types
- The difference between population and sample
- Which statistics are valid for which measurement levels
- How data collection affects analysis quality

**Next step:** See these concepts in action →

- [What does our sales data actually look like?](../../applied/notebooks/01-what-does-sales-data-look-like.ipynb)
- [Module 2: Descriptive Statistics →](../02-descriptive-stats/)

---

[← Day 4: Levels of Measurement](day-04-levels-of-measurement.md) · [Back to Module 1](README.md)
