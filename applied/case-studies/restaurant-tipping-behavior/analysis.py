#!/usr/bin/env python
# ---
# jupyter:
#   title: "Case Study: Restaurant Tipping Behavior (Real-world Dataset)"
#   purpose: "Analyze factors associated with tipping percentage using t-tests and OLS regression"
#   dataset: "../../../data/raw/tips.csv"
# ---

# %% [markdown]
# # Case Study: Restaurant Tipping Behavior
# 
# **Business Question:** What factors are most strongly associated with restaurant tip amounts and percentages? Specifically, do dinner patrons tip at a higher rate than lunch patrons? Does party size or bill size predict the absolute tip value?
# 
# **Why This Matters:** In the hospitality industry, understanding server compensation and customer behavior is critical for staffing, pricing, and point-of-sale tipping prompt designs.
# 
# **Dataset:** Bryant & Smith (1995) Restaurant Tips Dataset (244 transactions)  
# **Tools:** pandas, seaborn, scipy, statsmodels, matplotlib  
# **Key Skill:** Two-Sample t-test, Multiple Linear Regression, Residual Diagnostics, Associative Wording
# 
# ---

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.gofplots import qqplot

# Set clean style
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# %% [markdown]
# ## Step 1: Load the Data & Calculate Tip Percentage

# %%
# Load dataset
df = pd.read_csv('../../../data/raw/tips.csv')
df['tip_pct'] = (df['tip'] / df['total_bill'] * 100).round(2)
print(f"Loaded records for {len(df)} restaurant visits.")
df.head()

# %% [markdown]
# ## Step 2: Hypothesis Testing — Lunch vs. Dinner Tipping
# 
# Let's test if there is a significant difference in the tip percentage between Lunch and Dinner visits.
# * **Null Hypothesis ($H_0$):** There is no difference in mean tipping percentage between lunch and dinner.
# * **Alternative Hypothesis ($H_1$):** There is a significant difference in mean tipping percentage between lunch and dinner.

# %%
lunch_tips = df[df['time'] == 'Lunch']['tip_pct']
dinner_tips = df[df['time'] == 'Dinner']['tip_pct']

print(f"Lunch Tip Pct - Mean: {lunch_tips.mean():.2f}%, Median: {lunch_tips.median():.2f}%, N: {len(lunch_tips)}")
print(f"Dinner Tip Pct - Mean: {dinner_tips.mean():.2f}%, Median: {dinner_tips.median():.2f}%, N: {len(dinner_tips)}")

# Run independent t-test (Welch's t-test for unequal variances)
t_stat, p_val = stats.ttest_ind(lunch_tips, dinner_tips, equal_var=False)
print(f"\nt-test results: t-statistic = {t_stat:.4f}, p-value = {p_val:.4f}")

# %% [markdown]
# ### Statistical Interpretation:
# * Since $p = 0.4435 > 0.05$, we fail to reject the null hypothesis.
# * There is no statistically significant difference in tipping rates (%) between lunch and dinner patrons in this dataset. The slight observed difference could easily be due to random variation.

# %% [markdown]
# ## Step 3: Predictive Modeling — Multiple Linear Regression
# 
# Let's build a multiple linear regression model to predict the absolute `tip` based on `total_bill` and party `size`.
# $$\text{Tip} = \beta_0 + \beta_1 \times \text{Total Bill} + \beta_2 \times \text{Party Size} + \epsilon$$

# %%
model = ols('tip ~ total_bill + size', data=df).fit()
print(model.summary())

# %% [markdown]
# ### Model Interpretation:
# * **R-squared ($R^2 = 0.468$):** The model predicts approximately 46.8% of the variance in tip amounts.
# * **Total Bill Coefficient ($\beta_1 = 0.0927$):** Controlling for party size, each additional dollar on the total bill is associated with an expected increase of ~$0.09 in the tip amount (p < 0.001).
# * **Party Size Coefficient ($\beta_2 = 0.1926$):** Controlling for the bill amount, each additional person in the party is associated with an expected increase of ~$0.19 in the tip amount (p = 0.025).

# %% [markdown]
# ## Step 4: Residual Diagnostics

# %%
residuals = model.resid
fitted = model.fittedvalues

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Residuals vs Fitted
sns.scatterplot(x=fitted, y=residuals, alpha=0.7, ax=axes[0])
axes[0].axhline(0, color='red', linestyle='--', lw=2)
axes[0].set_title('Residuals vs. Fitted Values', fontweight='bold')
axes[0].set_xlabel('Fitted Values')
axes[0].set_ylabel('Residuals')

# Normal Q-Q Plot
qqplot(residuals, line='s', ax=axes[1])
axes[1].get_lines()[1].set_color('red')
axes[1].set_title('Normal Q-Q Plot of Residuals', fontweight='bold')

plt.tight_layout()
plt.savefig('residual_diagnostics.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ### Diagnostics Takeaway:
# * **Homoscedasticity:** The residuals vs. fitted plot shows a slight expansion (fan shape) at higher fitted values, suggesting mild heteroscedasticity (which is common in tipping data, as larger bills yield wider variations in tips).
# * **Normality:** The normal Q-Q plot shows some deviation at the upper tail, indicating slight right skewness. The residual plots do not show severe violations, so the model is acceptable for an educational analysis.

# %% [markdown]
# ## Key Finding
# 
# > ** Absolute tips are strongly associated with bill size and party size. Together, they explain 46.8% of the variance in tips, with each dollar increase in bill size predicting an extra $0.09 in tips (p < 0.001), and each extra party member predicting an extra $0.19 (p = 0.025). Tipping rates (%), however, do not significantly differ between lunch and dinner times (p = 0.44), showing that dining period is not a strong differentiator of tipping percentages in this dataset.**
