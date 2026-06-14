# Stats That Make Data Speak

**I turn statistical concepts into real-world data decisions using Python and analytics.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![pandas](https://img.shields.io/badge/pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![seaborn](https://img.shields.io/badge/seaborn-Visualization-4C72B0?style=for-the-badge)](https://seaborn.pydata.org)
[![scipy](https://img.shields.io/badge/scipy-Statistics-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*A structured, hands-on statistics resource — from foundational concepts to applied data analysis with Python.*

---

## What You'll Learn From This Repo

- **How to analyze real-world datasets** using statistics — not textbook exercises
- **How to translate statistical output into business decisions** that stakeholders actually care about
- **How Python is used in real data analysis workflows** — pandas, seaborn, scipy, and more
- **How to build insights that actually matter** — every analysis ends with a clear, shareable finding

> This isn't a stats textbook. It's a working portfolio that shows how statistics drives real decisions.

---

## Learning Path

### Part 1: Theory — Stats Foundations

The concepts behind every data decision. Each module = 5 days of focused learning.

| Module | Topic | Days | Status |
|--------|-------|------|--------|
| 1 | [**Basics**](modules/01-basics/) — What statistics is, types of data, how we collect it | Day 1–5 | Complete |
| 2 | [**Descriptive Stats**](modules/02-descriptive-stats/) — Summarizing data, central tendency, spread | Day 6–10 | Complete |
| 3 | [**Probability**](modules/03-probability/) — Chance, conditional probability, Bayes | Day 11–15 | Complete |
| 4 | [**Distributions**](modules/04-distributions/) — Normal, binomial, CLT | Day 16–20 | Complete |
| 5 | [**Inference**](modules/05-inference/) — Confidence intervals, hypothesis testing | Day 21–25 | Complete |
| 6 | [**Modeling**](modules/06-modeling/) — Regression, correlation, ANOVA | Day 26–30 | Complete |

### Part 2: Applied — Python + Real Data

Theory means nothing without application. These notebooks answer **real business questions** using real datasets.

| # | Notebook | Business Question | Key Skill |
|---|----------|-------------------|-----------|
| 1 | [What does our sales data actually look like?](applied/notebooks/01-what-does-sales-data-look-like.ipynb) | Understanding data before making decisions | EDA, Distributions |
| 2 | [Analyzing customer spending patterns](applied/notebooks/02-customer-spending-patterns.ipynb) | Where does the money come from? | Mean, Median, Grouping |
| 3 | [What actually drives sales?](applied/notebooks/03-what-drives-sales.ipynb) | Which factors matter most? | Correlation Analysis |
| 4 | [Predicting customer spend](applied/notebooks/04-predicting-customer-spend.ipynb) | Can we forecast revenue? | Linear Regression |
| 5 | [Do discounts increase repeat purchases?](applied/notebooks/05-do-discounts-work.ipynb) | Should we keep running promos? | A/B Testing |
| 6 | [Who are our best buyers?](applied/notebooks/06-who-are-best-buyers.ipynb) | How do we target the right people? | Customer Segmentation |
| 7 | [Is this campaign actually working?](applied/notebooks/07-is-campaign-working.ipynb) | Are we wasting marketing budget? | Hypothesis Testing |

### Part 3: Case Studies — Proof of Work

Complete analyses that show the full pipeline: question → data → analysis → business insight.

| Case Study | Key Finding |
|------------|-------------|
| [Screen Time vs Productivity](applied/case-studies/screen-time-vs-productivity/) | Higher screen time (>6 hrs) shows negative correlation with productivity scores |
| [Do Discounts Drive Retention?](applied/case-studies/discount-vs-retention/) | Discount depth doesn't predict customer return rate |

### Signature Project

| Project | Description |
|---------|-------------|
| [End-to-End Customer Analytics](applied/signature-project/) | Full pipeline: data cleaning → EDA → correlation → regression → segmentation → business recommendations |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/the-irritater/Stat_That_Make_Data_Speak.git
cd stats-that-make-data-speak

# Install dependencies
pip install -r requirements.txt

# Launch notebooks
jupyter notebook applied/notebooks/
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **pandas** | Data manipulation |
| **NumPy** | Numerical computation |
| **matplotlib** | Base visualizations |
| **seaborn** | Statistical visualizations |
| **scipy** | Statistical tests |
| **statsmodels** | Regression & modeling |
| **scikit-learn** | Segmentation & ML basics |
| **Jupyter** | Interactive analysis |

---

## About

**Author:** StatSphere (Sanman Kadam)

I am building this resource as part of my journey into data analytics — learning in public, applying statistics to real-world business problems, and sharing data-driven insights.

**Find me on LinkedIn:** [Sanman Kadam](https://www.linkedin.com/in/sanman-kadam-7a4990374/)

*If this repo helped you, give it a star — it helps others find it too.*

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
