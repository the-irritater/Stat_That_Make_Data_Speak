# Day 34: Cross-Sectional vs Time Series Data

*Some data compares different things at one moment. Other data tracks one thing over many moments. The analysis is completely different.*

---

## Learning Objective

Distinguish between cross-sectional and time series data structures, and understand how this affects analysis methods.

---

## The Concept

**Cross-sectional data** is collected at a single point in time across many subjects.

Examples: A survey of 1,000 people today. A snapshot of all employees' salaries this month.

**Time series data** is collected over a period of time, usually at regular intervals.

Examples: Monthly sales figures. Daily stock prices. Hourly website traffic.

| Feature | Cross-Sectional | Time Series |
|---------|----------------|-------------|
| Time dimension | One snapshot | Multiple time points |
| Focus | Comparing units | Tracking trends |
| Analysis | Group comparisons, distributions | Trends, seasonality, forecasting |
| Examples | Survey data, census | Stock prices, sales, weather |

### A Third Type: Panel Data

When you track multiple subjects over time, you get **panel data** (also called longitudinal data) — the most information-rich but also the most complex to analyze.

---

## Real-World Example

- **Cross-sectional**: Income data from 1,000 people surveyed today → compare income across demographics
- **Time series**: Monthly revenue from January to December → identify growth trends, seasonal patterns
- **Panel**: Quarterly sales for 50 stores over 3 years → compare stores AND track trends

---

## 🔑 Key Takeaway

> Cross-sectional data compares different units at one time. Time series data tracks change over time. Choosing the wrong analysis for your data type leads to wrong conclusions.

---

[← Day 33: Primary vs Secondary Data](day-33-primary-vs-secondary-data.md) · [Next: Day 35 – Clean Data vs Messy Data →](day-35-clean-data-vs-messy-data.md)
