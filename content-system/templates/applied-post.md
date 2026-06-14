# Template: Applied Post (Python + Data)

Use this when sharing a notebook analysis. Goal: show you can DO, not just teach.

---

## Structure

### 1. Hook (results-first)

```
I analyzed [dataset/topic] using Python.

[One-line key finding — the shareable insight]
```

**The insight sentence is everything.** If it's not interesting enough to screenshot, rewrite it.

Good: *"Customers who spend more than ₹2,000/month are 3× more likely to return."*
Bad: *"I calculated the correlation coefficient."*

### 2. Context (2–3 lines)

```
Dataset: [what it is, where it's from]
Question: [the business question you answered]
```

### 3. Method (brief)

```
Tools used:
• Python (pandas, seaborn)
• [Statistical method: correlation / regression / hypothesis test]
• [Visualization type]
```

### 4. Key Visual

**Attach the chart from your notebook.** This is what stops the scroll.

Requirements:
- Clean, readable (not default matplotlib gray)
- Title that states the finding, not the chart type
  - "Higher Spend Correlates With Higher Retention"
  -  "Scatter Plot of Spend vs Retention"

### 5. Insight (the LinkedIn-shareable line)

```
 [One sentence that a non-technical person would understand and find interesting]
```

### 6. CTA + Visibility Loop

```
Full notebook with code: [GitHub link to specific notebook]

I'm building a public stats + Python resource.
📂 github.com/the-irritater/Stat_That_Make_Data_Speak

#DataAnalytics #Python #Statistics #DataScience
```

---

## Example: Full Post

```
I analyzed restaurant tipping data to find what actually predicts tip size.

Key finding: Total bill explains 46% of tip variation — but party size barely matters.

Dataset: 244 restaurant transactions (seaborn tips dataset)
Question: What drives tipping behavior?

Tools used:
• Python (pandas, seaborn, scipy)
• Correlation analysis
• Scatter plot with regression line

 If you're a restaurant owner: focus on increasing order value, not table size.

Full notebook: github.com/the-irritater/Stat_That_Make_Data_Speak/blob/main/applied/notebooks/03-what-drives-sales.ipynb

#DataAnalytics #Python #Statistics
```
