# Executive Summary: End-to-End Customer Analytics

**Date:** June 16, 2026  
**Audience:** Executive Leadership Team  
**Author:** MSc Statistics & Analytics Lead  

---

## 1. Key Business Insights

We conducted a comprehensive end-to-end customer analytics study on e-commerce transactions ($N = 1,000$ customers) to determine how site engagement drives order values, how to categorize our buyers, and whether segment-wide re-engagement strategies are commercially viable.

### 📈 Engagement vs. Order Values (OLS Regression)
- **Variance Explained:** Browsing time and page view density together explain **71.0%** of customer order values ($R^2 = 0.710$), outperforming our baseline model by **44.8%** in predictive accuracy.
- **The Page View Association:** Holding session duration constant, customers with one additional page view had an estimated **$3.48** higher order value (95% CI: [$2.91$, $4.04$], $p < 0.001$). HC3-robust standard errors were computed alongside classical OLS to account for mild heteroscedasticity.
- **The Duration Association:** Holding pages visited constant, customers with one extra minute of session duration had an estimated **$1.11** higher order value (95% CI: [$0.63$, $1.59$], $p < 0.001$).
- **Relative Importance (caveat):** Standardized coefficients indicate that Pages Visited (Beta: 0.620) had a larger coefficient than Session Duration (Beta: 0.234), but these predictors are highly correlated (VIF ≈ 7.26), so their independent effects should be interpreted cautiously.

### 🏷️ RFM Customer Segmentation (Recency, Frequency, Monetary)
We classified customers into three distinct value segments based on Recency, Frequency, and Monetary scores:
1. **Champions (22.4% of base):** Highly engaged, high-spending frequent buyers. (Average tenure: 11.2 months, Mean lifetime spend: **$671.30**).
2. **Loyal Customers (54.8% of base):** Regular shoppers with moderate lifetime spend. (Average tenure: 11.0 months, Mean lifetime spend: **$245.05**).
3. **At-Risk / Lost (22.8% of base):** Churned or low-value transient shoppers. (Average tenure: 7.9 months, Mean lifetime spend: **$104.70**).

---

## 2. Hypothesis Testing: Segment Retention Associations

We evaluated if segment membership predicts a customer's repeat purchase rate using a Chi-Square Test of Independence.
- **Hypothesis Result:** We failed to reject the null hypothesis ($p = 0.551$, Cramer's V = 0.0345).
- **Interpretation:** There is **no statistically significant difference** in repeat purchase rates among Champions (37.9%), Loyal Customers (40.3%), and At-Risk shoppers (43.0%) in this dataset.

---

## 3. Executive Business Recommendations

Based on our empirical models, we propose three core interventions:

1. **Prioritize a Controlled UX Experiment:** Since page views show the strongest predictive association with order value (Beta: 0.620, $p < 0.001$), specific page-speed or navigation changes should be tested through a randomized A/B experiment before allocating engineering budget. The regression coefficient is a predictive association from observational data — high-spending customers may simply browse more pages (reverse causality). The association warrants investigation but not direct investment without experimental validation.
2. **Individualized Loyalty Strategy:** Do not launch segment-wide loyalty campaigns under the assumption that "Champions" have a higher repeat purchase rate than others (the difference is statistically negligible, $p = 0.55$). Re-engagement campaigns should instead be triggered by individualized customer purchase intervals.
3. **Targeted Coupon Distributions:** A separate analysis on the binary discount variable ([notebook 05](../../applied/notebooks/05-do-discounts-work.ipynb)) found that while discounts show a statistically significant association with repeat purchases ($p = 0.018$), the expected profit per customer drops by approximately 39.6% due to margin compression. Coupon distributions should be restricted to price-sensitive churned shoppers, not applied site-wide.
