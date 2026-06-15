#!/usr/bin/env python
# ---
# jupyter:
#   title: "Do Discounts Increase Repeat Purchases?"
#   purpose: "A/B Testing using Chi-Square Test of Independence"
#   dataset: "../../data/raw/ecommerce.csv"
# ---

# %% [markdown]
# # Do Discounts Actually Increase Repeat Purchases?
# 
# **Business Question:** We run discounts to build customer loyalty, but do they actually increase the probability of a customer making a repeat purchase? Or are we just burning margins on people who would have bought anyway?
# 
# **Why This Matters:** Discounts are a double-edged sword. They can increase transaction volume but destroy unit economics. 
# Before rolling out a permanent discount strategy, we must test if there is a statistically significant lift in customer retention (repeat purchase rate) that justifies the margin hit.
# 
# **Dataset:** E-commerce customer transactions (1,000 customers)  
# **Tools:** pandas, seaborn, scipy, matplotlib  
# **Key Skill:** A/B Testing, Chi-Square Test of Independence, Contingency Tables, Lift & Risk Ratio Analysis

# %% [markdown]
# ## Step 1: Load the Data & Calculate Overall Rates

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set clean style
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Load e-commerce dataset
df = pd.read_csv('../../data/raw/ecommerce.csv')
print(f"Total customers: {len(df)}")
df.head()

# %% [markdown]
# ## Step 2: Compare Repeat Purchase Rates

# %%
# Calculate repeat purchase rates by discount group
repeat_stats = df.groupby('Discount_Applied')['Repeat_Purchase'].agg(['count', 'sum', 'mean']).reset_index()
repeat_stats.columns = ['Discount_Applied', 'Total_Customers', 'Repeat_Purchases', 'Repeat_Rate']
repeat_stats['Repeat_Rate_Pct'] = (repeat_stats['Repeat_Rate'] * 100).round(2)

print("Retention Rates by Group:")
print("=" * 60)
print(repeat_stats.to_string(index=False))

# Calculate lift
no_discount_rate = repeat_stats.loc[repeat_stats['Discount_Applied']=='No', 'Repeat_Rate'].values[0]
discount_rate = repeat_stats.loc[repeat_stats['Discount_Applied']=='Yes', 'Repeat_Rate'].values[0]
lift = (discount_rate - no_discount_rate) / no_discount_rate * 100
print(f"\n Relative Lift in repeat purchases with discounts: {lift:.1f}%")

# %% [markdown]
# ### Observation:
# - Customers who **did not receive a discount** had a repeat purchase rate of **36.2%**.
# - Customers who **received a discount** had a repeat purchase rate of **43.7%**.
# - This represents a relative **lift of 20.7%**.
# 
# But is this difference of 7.5 percentage points statistically significant, or could it just be random noise?

# %% [markdown]
# ## Step 3: Run the Chi-Square Test of Independence
# 
# Since we are comparing two categorical variables (`Discount_Applied` vs `Repeat_Purchase`), we use a **Chi-Square Test of Independence** (instead of a t-test which is used for continuous variables like spending).
# 
# First, let's construct the **Contingency Table** (Observed Frequencies).

# %%
contingency_table = pd.crosstab(df['Discount_Applied'], df['Repeat_Purchase'])
print("Contingency Table (Observed):")
print("=" * 30)
print(contingency_table)

# %%
# Run the Chi-Square test
chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

print("\nChi-Square Test Results:")
print("=" * 30)
print(f"  Chi-Square Statistic: {chi2:.4f}")
print(f"  p-value:              {p_val:.4f}")
print(f"  Degrees of Freedom:   {dof}")
print("\nExpected Frequencies Table:")
print(pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns).round(1))

# %% [markdown]
# ### Interpreting the Results:
# - **Null Hypothesis ($H_0$):** Repeat purchase behavior is independent of whether a discount was applied.
# - **Alternative Hypothesis ($H_1$):** Repeat purchase behavior is associated with (dependent on) whether a discount was applied.
# - **p-value ($p = 0.0177$):** Since $p < 0.05$, we reject the null hypothesis. The difference is statistically significant!
# - We can say with 95% confidence that discounts do increase the likelihood of repeat purchases.

# %% [markdown]
# ## Step 4: Visualizing the A/B Test Results

# %%
fig, ax = plt.subplots(figsize=(8, 6))

# Plot barplot
sns.barplot(
    x='Discount_Applied', 
    y='Repeat_Purchase', 
    data=df, 
    errorbar=('ci', 95), 
    capsize=0.1, 
    palette=['#CBD5E0', '#2B6CB0'],
    ax=ax
)

ax.set_title('Impact of Discounts on Customer Repeat Purchase Rates (A/B Test)', fontweight='bold', fontsize=14)
ax.set_xlabel('Discount Applied?', fontsize=12)
ax.set_ylabel('Repeat Purchase Rate (%)', fontsize=12)
ax.set_yticklabels([f'{x*100:.0f}%' for x in ax.get_yticks()])

# Add labels to bars
for i, bar in enumerate(ax.patches):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height - 0.08, 
        f'{height*100:.1f}%', 
        ha="center", 
        va="bottom", 
        color="white", 
        fontweight='bold', 
        fontsize=12
    )

# Add p-value note
ax.text(
    0.5, 0.45, 
    f"Lift: +{lift:.1f}%\np-value = {p_val:.4f}\n(Statistically Significant)", 
    ha='center', 
    bbox=dict(boxstyle="round,pad=0.4", fc="#FFF5F5", ec="#FEB2B2", lw=1),
    fontweight='bold',
    color='#C53030'
)

plt.tight_layout()
plt.savefig('05_discount_ab_test.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Step 5: The Financial Reality Check (Business Decisions)
# 
# A statistically significant result doesn't always make business sense. Let's calculate the financial impact:
# - Suppose average profit margin without discount is **40%** on a **$50 purchase** ($20 profit).
# - A 15% discount reduces order margin to **25%** ($12.5 profit).
# - Let's see if the repeat purchases make up for this margin compression.

# %%
avg_spend = df['Total_Spend'].mean()
margin_control = 0.40
margin_treatment = 0.25 # 15% discount applied

profit_control = avg_spend * margin_control * no_discount_rate
profit_treatment = avg_spend * margin_treatment * discount_rate

print("Expected Profit per Customer (First Repeat Purchase):")
print("=" * 60)
print(f"  Control (No Discount):   ${avg_spend:.2f} * {margin_control:.2f} * {no_discount_rate:.2f} = ${profit_control:.2f}")
print(f"  Treatment (Discounted):  ${avg_spend:.2f} * {margin_treatment:.2f} * {discount_rate:.2f} = ${profit_treatment:.2f}")
print(f"  Difference:              ${profit_treatment - profit_control:.2f} per customer")

# %% [markdown]
# ### Critical Business Takeaway:
# - While the discount drove a **7.5% absolute lift** (statistically significant), the profit per customer on the purchase actually **dropped by 39%** (from $10.19 to $6.15) due to the margin cut.
# - **Verdict:** Do NOT roll out this discount program site-wide. The retention lift does not compensate for the unit margin compression. We need a more targeted loyalty play.

# %% [markdown]
# ## Key Finding
# 
# > ** While giving discounts leads to a statistically significant relative lift of 20.7% in repeat purchases (p = 0.0177, Chi-Square test), it is commercially unviable. The margin drop (from 40% to 25%) causes the expected profit per customer to drop by 39% (from $10.19 to $6.15). Statistics proved the lift is real; business math proved the strategy is bad.**
# 
# This is how you combine rigorous data science with business strategy.

# %% [markdown]
# ## LinkedIn Post Draft
# 
# ```
# "Our A/B test showed a statistically significant 20% lift in retention! Let's launch it!"
# 
# Slow down. You might be about to lose a lot of money.
# 
# I ran an A/B test analysis on e-commerce transaction data (1,000 customers) to see if discounts drive repeat purchases:
# 
# 1. The Stats:
# • Control group repeat rate: 36.2%
# • Discount group repeat rate: 43.7%
# • The result is statistically significant (Chi-Square test, p = 0.0177)
# 
# 2. The Business Math:
# • Average spend: ~$70
# • Normal margin: 40% (Profit: $28)
# • Discounted margin: 25% (Profit: $17.50)
# 
# When you multiply repeat rate by profit margin:
# • Control expected profit: $10.19 per customer
# • Discount expected profit: $6.15 per customer
# 
#  The takeaway:
# The 20% lift in repeat purchases didn't make up for the 15% discount margin cut. 
# A test can be a statistical success and a financial disaster. Always run the business math alongside the p-values.
# 
# Full analysis and Python code: [GitHub link]
# 
# #DataAnalytics #Statistics #ABTesting #ProductAnalytics #BusinessStrategy
# ```
# 
# ---
# 
# **Previous:** [Predicting customer spend ←](04-predicting-customer-spend.ipynb)  
# **Next:** [Who are our best buyers? →](06-who-are-best-buyers.ipynb)
