#!/usr/bin/env python
# ---
# jupyter:
#   title: "Case Study: Screen Time vs Productivity"
#   purpose: "Analyze correlation between daily screen time and employee productivity"
#   dataset: "../../datasets/screen_time.csv"
# ---

# %% [markdown]
# # Case Study: Screen Time vs Productivity
# 
# **Business Question:** Does higher daily screen time correlate with lower productivity scores? 
# Should our organization implement strict policies or guide employees toward healthier screen limits?
# 
# **Why This Matters:** In a remote and digital-first work culture, screen time is at an all-time high. 
# While digital tools are essential for work, excessive screen time is often linked to fatigue, distraction, and cognitive overload. 
# This analysis checks if there is a statistical threshold where screen time starts negatively impacting productivity.
# 
# **Dataset:** Tech-firm employee screen tracking & self-reported productivity index (150 employees)  
# **Tools:** pandas, seaborn, scipy, matplotlib  
# **Key Skill:** Correlation Analysis (Pearson & Spearman), Segmented Binning, Data Visualization, Business Recommendations

# %% [markdown]
# ## Step 1: Load and Preview the Data

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

# Load screen time dataset
df = pd.read_csv('../../datasets/screen_time.csv')
print(f"Loaded records for {len(df)} employees.")
df.head()

# %% [markdown]
# ## Step 2: Correlation Analysis (Overall Relationship)
# 
# Let's run Pearson and Spearman correlation tests between screen time and productivity score.

# %%
pearson_r, p_val_p = stats.pearsonr(df['Screen_Time_Hours'], df['Productivity_Score'])
spearman_r, p_val_s = stats.spearmanr(df['Screen_Time_Hours'], df['Productivity_Score'])

print("Correlation Coefficients:")
print("=" * 40)
print(f"  Pearson correlation (r):  {pearson_r:.4f}  (p-value: {p_val_p:.4g})")
print(f"  Spearman correlation (r): {spearman_r:.4f}  (p-value: {p_val_s:.4g})")

# %% [markdown]
# ### Observation:
# - There is a **strong negative correlation** of ~$r = -0.74$.
# - The p-value is extremely close to 0, which means this relationship is highly statistically significant.
# - As daily screen time goes up, productivity scores tend to go down.
# 
# Let's visualize this using a scatterplot with a trend line.

# %%
fig, ax = plt.subplots(figsize=(10, 6))

sns.regplot(
    x='Screen_Time_Hours', 
    y='Productivity_Score', 
    data=df, 
    scatter_kws={'alpha':0.6, 'color': '#2B6CB0'},
    line_kws={'color': '#E53E3E', 'lw': 3},
    ax=ax
)

ax.set_title('Impact of Screen Time on Employee Productivity Score', fontweight='bold', fontsize=14)
ax.set_xlabel('Daily Screen Time (Hours)', fontsize=12)
ax.set_ylabel('Productivity Score (1-100)', fontsize=12)

# Annotate correlation coefficient
ax.text(
    7, 85, 
    f"Pearson's r = {pearson_r:.2f}\np-value < 0.001", 
    bbox=dict(boxstyle="round,pad=0.3", fc="#FFF5F5", ec="#FEB2B2", lw=1),
    fontsize=11, fontweight='bold', color='#C53030'
)

plt.tight_layout()
plt.savefig('screen_time_vs_productivity_scatter.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Step 3: Segmented Analysis (Finding the Threshold)
# 
# Let's segment employees into screen time tiers:
# - **Low Screen Time:** < 4 hours
# - **Medium Screen Time:** 4 to 6 hours
# - **High Screen Time:** > 6 hours
# 
# Let's see if the negative relationship holds in every tier, or if there is a "tipping point."

# %%
# Define bins and labels
bins = [0, 4, 6, 24]
labels = ['Low (< 4 hrs)', 'Medium (4-6 hrs)', 'High (> 6 hrs)']
df['Screen_Time_Tier'] = pd.cut(df['Screen_Time_Hours'], bins=bins, labels=labels)

# Group by tier
tier_stats = df.groupby('Screen_Time_Tier')['Productivity_Score'].agg(['count', 'mean', 'median', 'std']).reset_index()
print("Productivity Stats by Screen Time Tier:")
print("=" * 60)
print(tier_stats.round(1).to_string(index=False))

# %% [markdown]
# Let's check the correlation *within* each tier to see where the drop kicks in.

# %%
for tier in labels:
    tier_data = df[df['Screen_Time_Tier'] == tier]
    r, p = stats.pearsonr(tier_data['Screen_Time_Hours'], tier_data['Productivity_Score'])
    print(f"  {tier:18s} correlation: r = {r:.2f} (p-value: {p:.4f})")

# %% [markdown]
# ### Crucial Business Insight:
# - **Low Screen Time (<4 hrs):** No significant correlation ($r = 0.06$).
# - **Medium Screen Time (4-6 hrs):** Weak negative correlation ($r = -0.19$, not highly significant).
# - **High Screen Time (>6 hrs):** Strong negative correlation ($r = -0.52$, $p < 0.05$).
# - **The Tipping Point:** Employee productivity is relatively stable up to 6 hours of daily screen time (averaging ~72-74 points). However, once screen time exceeds 6 hours, productivity scores drop sharply to an average of **50.6 points** (a **30%+ drop**).

# %% [markdown]
# ## Step 4: Visualizing Productivity by Tier

# %%
fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(
    x='Screen_Time_Tier', 
    y='Productivity_Score', 
    data=df, 
    errorbar=('ci', 95), 
    capsize=0.1, 
    palette=['#38A169', '#3182CE', '#E53E3E'],
    ax=ax
)

ax.set_title('Average Productivity Score by Screen Time Tier', fontweight='bold', fontsize=14)
ax.set_xlabel('Daily Screen Time Tier', fontsize=12)
ax.set_ylabel('Average Productivity Score (95% CI)', fontsize=12)

# Annotate heights
for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2., 
        height - 8, 
        f'{height:.1f}', 
        ha="center", va="bottom", color="white", fontweight='bold', fontsize=12
    )

plt.tight_layout()
plt.savefig('productivity_by_tier_barplot.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Key Finding
# 
# > ** Screen time is not inherently bad for productivity, but there is a clear tipping point. Below 6 hours, daily screen time has minimal correlation with productivity (scores average ~73). However, for employees with more than 6 hours of daily screen time, productivity scores drop by 31% to an average of 50.6 (correlation r = -0.52, highly significant). Focus on screen time management rather than complete screen reduction policies.**
# 
# This threshold analysis provides actionable workspace design guidance (e.g. promoting walking meetings, structured offline focus blocks, and screen-free lunches).

# %% [markdown]
# ## LinkedIn Post Draft
# 
# ```
# Does more screen time kill productivity?
# 
# Stop making assumptions. Look at the threshold.
# 
# I analyzed daily screen tracking and productivity data for 150 employees. Here is the statistical truth:
# 
# 1. The Overall Picture:
# • Strong negative correlation overall (r = -0.74). More screens = lower productivity.
# 
# 2. The Nuance (Segmented Analysis):
# • Low Screen Time (<4 hrs): Correlation is basically zero (r = 0.06).
# • Medium Screen Time (4-6 hrs): Minimal negative impact (r = -0.19).
# • High Screen Time (>6 hrs): Productivity drops by 31% (averaging 50.6 vs 73.5 in lower tiers).
# 
#  Key Takeaway:
# Screens aren't the enemy — overload is. The negative impact doesn't scale linearly; it kicks in hard after 6 hours.
# 
# What we can do:
# • Promote offline focus blocks (no Slack, no browser)
# • Introduce walking/phone meetings instead of Zoom
# • Encourage screen-free lunches
# 
# Full analysis and code: [GitHub link]
# 
# #DataAnalytics #Statistics #Productivity #Python #WorkplaceDesign
# ```
# 
# ---
# 
# **Previous:** [Is this campaign actually working? →](../../applied/notebooks/07-is-campaign-working.ipynb)  
# **Next:** [Do discounts drive retention? →](../discount-vs-retention/README.md)
