# Template: Case Study Post (Proof of Work)

Use this when sharing a complete analysis. Goal: prove you can think like an analyst, not just run code.

---

## Structure

### 1. Hook (the finding, not the process)

```
[Surprising or counterintuitive finding]

Here's how I found out.
```

**Lead with the result, not the method.** Nobody clicks "I ran a regression." People click "Discounts DON'T increase retention."

### 2. The Question (1–2 lines)

```
Business question: [What were you trying to figure out?]
Why it matters: [What decision depends on this?]
```

### 3. The Data (brief)

```
Dataset: [Source, size, time period]
Variables: [What you looked at]
```

### 4. The Method (brief — analysts care, but keep it short)

```
Approach:
1. [Data cleaning step]
2. [Analysis method]
3. [Validation/test]

Tools: Python (pandas, seaborn, scipy)
```

### 5. The Finding (this is the star of the post)

```
Key finding:

[1–2 sentences with a specific number/metric]
```

**Attach the key visualization.**

### 6. Business Takeaway (this is what separates analysts from coders)

```
What this means:

[1–2 sentences translating the finding into a business recommendation]
```

### 7. CTA + Visibility Loop

```
Full analysis with code and data:
📂 [GitHub link to case study folder]

This is how statistics helps avoid wrong business decisions.

#DataAnalytics #CaseStudy #Python #Statistics
```

---

## Example: Full Post

```
Higher discount rates don't increase customer retention.

I analyzed 2,000 customer transactions to test whether bigger discounts drive repeat purchases.

Business question: Should we increase discount depth to improve retention?

Dataset: 2,000 transactions over 6 months (simulated e-commerce data)

Approach:
1. Grouped customers by discount tier (0%, 5-10%, 15-25%, 30%+)
2. Measured return rate for each tier
3. Ran chi-square test for significance

Key finding:
No statistically significant relationship between discount depth and return rate (p = 0.34).
Customers in the 30%+ discount tier had the LOWEST return rate (22%).

What this means:
Deep discounts attract deal-seekers, not loyal customers. If your goal is retention, invest in experience — not price cuts.

Full analysis: github.com/the-irritater/Stat_That_Make_Data_Speak/tree/main/applied/case-studies/discount-vs-retention

#DataAnalytics #Statistics #Python #BusinessIntelligence
```
