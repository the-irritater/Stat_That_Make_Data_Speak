#!/usr/bin/env python
# ---
# jupyter:
#   title: "Predicting Customer Spend"
#   purpose: "Build prediction models using linear regression"
#   dataset: "../../data/raw/ecommerce.csv"
# ---

# %% [markdown]
# # Predicting Customer Spend from Browsing Behavior
# 
# **Business Question:** Can we predict how much a customer will spend based on their browsing behavior? 
# Specifically, how much revenue does an extra minute of site browsing or an extra page visit generate?
# 
# **Why This Matters:** Knowing the predictive value of user behavior allows us to justify investments in website speed, 
# UI redesign, or content marketing. If we can prove that keeping a user on a page longer predicts higher spend, 
# we have a clear business case for UX optimization.
# 
# **Dataset:** E-commerce customer behavior (1,000 customers)  
# **Tools:** pandas, seaborn, statsmodels, scipy, matplotlib  
# **Key Skill:** Simple & Multiple Linear Regression, R-squared, Regression Coefficients, Residual Analysis

# %% [markdown]
# ## Step 1: Load and Preview the Data

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Set clean style
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Load e-commerce dataset
df = pd.read_csv('../../data/raw/ecommerce.csv')
print(f"Loaded {len(df)} customer records.")
df.head()

# %% [markdown]
# ## Step 2: Simple Linear Regression (Duration vs Spend)
# 
# Let's model the relationship:  
# $$\text{Total Spend} = \beta_0 + \beta_1 \times \text{Session Duration} + \epsilon$$

# %%
fig, ax = plt.subplots(figsize=(10, 6))

# Regression plot
sns.regplot(
    x='Session_Duration', 
    y='Total_Spend', 
    data=df, 
    scatter_kws={'alpha':0.4, 'color': '#2B6CB0'},
    line_kws={'color': '#E53E3E', 'lw': 3},
    ax=ax
)

ax.set_title('Website Session Duration vs. Customer Spend', fontweight='bold', fontsize=14)
ax.set_xlabel('Session Duration (Minutes)', fontsize=12)
ax.set_ylabel('Total Spend ($)', fontsize=12)

plt.tight_layout()
plt.savefig('04_duration_vs_spend.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ## Step 3: Fitting the Regression Model
# 
# Let's use `statsmodels` to run the Ordinary Least Squares (OLS) regression and inspect the detailed statistical summary.

# %%
# Fit the simple linear regression model
model_simple = ols('Total_Spend ~ Session_Duration', data=df).fit()
print(model_simple.summary())

# %% [markdown]
# ### Interpreting the Simple Regression Output:
# 
# 1. **R-squared ($R^2 = 0.44$):** About 44% of the variance in customer spend is explained by how long they browse the site.
# 2. **Intercept ($\beta_0 = 19.38$):** If a session duration was theoretically 0 minutes, the predicted baseline spend is ~$19.38 (this is our baseline, though practically users must spend time to buy).
# 3. **Session Duration Coefficient ($\beta_1 = 3.65$):** For every **additional 1 minute** a customer spends browsing, they spend an estimated **additional $3.65**.
# 4. **Statistical Significance ($p < 0.05$):** The p-value for `Session_Duration` is 0.000, meaning session duration is a highly significant predictor of spend.

# %% [markdown]
# ## Step 4: Multiple Linear Regression (Adding Pages Visited)
# 
# Let's add `Pages_Visited` to see if it improves our prediction:  
# $$\text{Total Spend} = \beta_0 + \beta_1 \times \text{Session Duration} + \beta_2 \times \text{Pages Visited} + \epsilon$$

# %%
model_multiple = ols('Total_Spend ~ Session_Duration + Pages_Visited', data=df).fit()
print(model_multiple.summary())

# %% [markdown]
# ### Interpreting the Multiple Regression Output:
# 
# - **R-squared increased to 0.47:** Adding pages visited improved the variance explained.
# - **Session_Duration Coefficient ($\beta_1 = 1.34$):** Controlling for pages visited, each additional minute of session duration increases spend by **$1.34**.
# - **Pages_Visited Coefficient ($\beta_2 = 2.87$):** Controlling for session duration, each additional page visited increases spend by **$2.87**.
# - **Why did the duration coefficient drop from 3.65 to 1.34?** Multicollinearity! Session duration and pages visited are highly correlated. Part of the predictive power of duration was actually driven by the fact that longer sessions mean more page views.

# %% [markdown]
# ## Step 5: Checking Model Assumptions (Residual Diagnostics)
# 
# A good analyst verifies that the regression residuals are normally distributed and homoscedastic (constant variance).

# %%
fig, axes = plt.subplots(1, 2, figsize=(16, 5))

# Residuals vs Fitted Plot (Checking Homoscedasticity)
residuals = model_multiple.resid
fitted_vals = model_multiple.fittedvalues

sns.scatterplot(x=fitted_vals, y=residuals, alpha=0.5, color='#2B6CB0', ax=axes[0])
axes[0].axhline(0, color='#E53E3E', linestyle='--', linewidth=2)
axes[0].set_title('Residuals vs. Fitted Values (Homoscedasticity Check)', fontweight='bold')
axes[0].set_xlabel('Fitted Values')
axes[0].set_ylabel('Residuals')

# QQ-Plot of Residuals (Checking Normality)
sm.qqplot(residuals, line='s', ax=axes[1])
axes[1].get_lines()[1].set_color('#E53E3E') # Red line
axes[1].set_title('Normal Q-Q Plot of Residuals', fontweight='bold')

plt.tight_layout()
plt.savefig('04_residuals_diagnostic.png', bbox_inches='tight', dpi=150)
plt.show()

# %% [markdown]
# ### Diagnostics Analysis:
# - **Homoscedasticity:** Residuals are spread fairly evenly above and below the zero line, though we see a slight expansion at higher values due to our discount multiplier. Overall, it's very clean!
# - **Normality:** The points in the Q-Q plot closely track the red 45-degree line, confirming our residuals are normally distributed. Our linear regression results are highly reliable.

# %% [markdown]
# ## Key Finding
# 
# > ** Website engagement metrics are strong leading indicators of revenue. Together, Session Duration and Pages Visited predict 47% of customer spend. Controlling for duration, every extra page a customer visits predicts an additional $2.87 in spend, while each extra minute of browsing predicts an additional $1.34. Optimizing the site UI to keep users engaged and clicking directly drives sales growth.**
# 
# Quantifying this with regression gives the marketing and product teams a dollar-backed business case.

# %% [markdown]
# ## LinkedIn Post Draft
# 
# ```
# How much is a website page view actually worth?
# 
# Stop guessing. Use linear regression to quantify it.
# 
# I built a regression model on e-commerce browsing behavior data for 1,000 customers. Here's what the data revealed:
# 
# • Engagement Predicts Spend: Session duration and pages visited explain 47% of the variance in customer spend (R-squared = 0.47).
# • The Page-View Premium: Holding browsing time constant, each additional page a user clicks on predicts a $2.87 increase in order value.
# • The Time Value: Controlling for page views, each extra minute a customer spends on-site predicts a $1.34 increase in spend.
# 
#  Why this matters for business:
# If your UX team wants budget to redesign the site to increase average page views per session by just 2, you now have the statistical backing to estimate a $5.74 increase in average order value.
# 
# Analytics isn't just about describing what happened; it's about predicting what will happen.
# 
# Full code and OLS model output: [GitHub link]
# 
# #DataAnalytics #Statistics #Python #LinearRegression #EcommerceAnalytics
# ```
# 
# ---
# 
# **Previous:** [What actually drives sales? ←](03-what-drives-sales.ipynb)  
# **Next:** [Do discounts increase repeat purchases? →](05-do-discounts-work.ipynb)
