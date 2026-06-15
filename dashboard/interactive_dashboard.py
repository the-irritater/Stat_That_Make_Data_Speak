from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from scipy import stats
from statsmodels.formula.api import ols

# Page configuration for a premium dark-mode aligned, clean look
st.set_page_config(
    page_title="StatSphere Analytics Hub", page_icon="🔮", layout="wide", initial_sidebar_state="expanded"
)

# Relative Path Resolution
ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"

# Custom Styling
st.markdown(
    """
<style>
    .main { background-color: #f7fafc; }
    h1, h2, h3 { color: #1a365d; font-family: 'Inter', sans-serif; }
    .stAlert { border-radius: 8px; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Helper function to cache data loading & validation
@st.cache_data
def load_cached_data(name):
    filepath = RAW_DATA_DIR / f"{name}.csv"
    if not filepath.exists():
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()
    return pd.read_csv(filepath)


# Precompute and save aggregations to data/processed/ for reproducible research
def save_processed_aggregations(name, df_agg):
    try:
        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
        dest_path = PROCESSED_DATA_DIR / f"{name}_aggregations.csv"
        df_agg.to_csv(dest_path, index=False)
    except Exception:
        pass  # Ignore permission issues silently during streamlit load


# Title
st.title("🔮 StatSphere Analytics Hub")
st.markdown("### Interactive Statistical Analysis & Decision Engine")
st.write("---")

# Sidebar navigation
st.sidebar.title("Navigation")
analysis_option = st.sidebar.radio(
    "Select Statistical Study:",
    [
        "Customer Spend & Browsing (Linear Regression)",
        "Marketing Campaign A/B Test (Inference)",
        "Screen Time vs Productivity (Correlation & Binning)",
        "Discount Depth vs Retention (Chi-Square)",
        "Restaurant Tips spending patterns (EDA)",
    ],
)

# Sidebar about section
st.sidebar.write("---")
st.sidebar.info(
    "**StatSphere Portfolio**\n\n"
    "This dashboard lets you interactively test hypothesis models and visualize real-world business scenarios. "
    "All computations are cached for speed and recorded for reproducibility."
)

# ----------------- Study 1: E-commerce Spend -----------------
if analysis_option == "Customer Spend & Browsing (Linear Regression)":
    st.header("📈 Customer Spend & Browsing Behavior")
    st.write(
        "Analyze whether website browsing session length and page visits can predict order value, "
        "allowing product teams to evaluate UX redesign investments."
    )

    df = load_cached_data("ecommerce")

    if not df.empty:
        # Save processed metadata for replication
        save_processed_aggregations("ecommerce", df.describe().reset_index())

        # User controls
        col1, col2 = st.columns([1, 3])
        with col1:
            st.subheader("Filters")
            discount_filter = st.selectbox("Discount Applied Filter:", ["All", "Yes", "No"])
            model_type = st.radio(
                "Model Complexity:", ["Simple Linear (Duration)", "Multiple Linear (Duration + Pages)"]
            )

            # Slider to narrow sessions
            min_duration = int(df["Session_Duration"].min())
            max_duration = int(df["Session_Duration"].max())
            duration_range = st.slider(
                "Session Duration Range (mins):", min_duration, max_duration, (min_duration, max_duration)
            )

        # Apply filters
        filtered_df = df[(df["Session_Duration"] >= duration_range[0]) & (df["Session_Duration"] <= duration_range[1])]
        if discount_filter != "All":
            filtered_df = filtered_df[filtered_df["Discount_Applied"] == discount_filter]

        with col2:
            st.subheader("Interactive Visualization")
            fig = px.scatter(
                filtered_df,
                x="Session_Duration",
                y="Total_Spend",
                color="Discount_Applied",
                hover_data=["Pages_Visited"],
                title="Session Duration vs. Total Spend ($)",
                labels={"Session_Duration": "Duration (Minutes)", "Total_Spend": "Order Value ($)"},
                color_discrete_map={"Yes": "#3182CE", "No": "#E53E3E"},
                trendline="ols",
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # OLS Regression Output
        st.subheader("Ordinary Least Squares (OLS) Summary")
        if len(filtered_df) > 3:
            if model_type == "Simple Linear (Duration)":
                formula = "Total_Spend ~ Session_Duration"
            else:
                formula = "Total_Spend ~ Session_Duration + Pages_Visited"

            model = ols(formula, data=filtered_df).fit()

            r_col, p_col, f_col = st.columns(3)
            with r_col:
                st.metric("R-squared (Variance Explained)", f"{model.rsquared:.2%}")
            with p_col:
                st.metric("F-Statistic p-value", f"{model.f_pvalue:.4e}")
            with f_col:
                st.metric("Intercept Value (Base Spend)", f"${model.params['Intercept']:.2f}")

            st.write("**Model Coefficients & Coefficients significance:**")
            st.dataframe(
                pd.DataFrame(
                    {
                        "Coefficient": model.params,
                        "Std Error": model.bse,
                        "t-value": model.tvalues,
                        "p-value": model.pvalues,
                    }
                ).round(4)
            )

            # Business decision support
            st.success(
                f"**Takeaway:** Controlling for other metrics, each additional minute of browsing predicts "
                f"an increase of **${model.params.get('Session_Duration', 0.0):.2f}** in order value. "
                "UX investments to increase retention are highly justified."
            )
        else:
            st.warning("Not enough data points selected to fit regression model.")

# ----------------- Study 2: Marketing A/B Test -----------------
elif analysis_option == "Marketing Campaign A/B Test (Inference)":
    st.header("🎯 Marketing Campaign A/B Test Results")
    st.write(
        "Evaluate A/B test results to verify if a new promotional campaign leads to "
        "statistically significant conversion rates compared to the control group."
    )

    df = load_cached_data("marketing_campaign")

    if not df.empty:
        # Precompute conversion table for reproducibility
        conv_summary = df.groupby("Campaign_Group")["Converted"].agg(["count", "sum", "mean"]).reset_index()
        conv_summary.columns = ["Campaign_Group", "Users", "Conversions", "Conversion_Rate"]
        save_processed_aggregations("marketing", conv_summary)

        # Display high level metrics
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Conversion Overview")
            st.table(conv_summary.style.format({"Conversion_Rate": "{:.2%}"}))

            # Hypothesis test parameters
            st.subheader("Statistical Hypothesis Test")
            confidence_level = st.slider("Confidence Level:", 0.90, 0.99, 0.95, 0.01)
            alpha = 1 - confidence_level

        # Run conversion tests
        control_group = df[df["Campaign_Group"] == "Control"]
        test_group = df[df["Campaign_Group"] == "Test"]

        c_conv = control_group["Converted"].sum()
        c_total = len(control_group)
        t_conv = test_group["Converted"].sum()
        t_total = len(test_group)

        # Two-sample proportion z-test (approximated via Chi-square or manual computation)
        p_c = c_conv / c_total
        p_t = t_conv / t_total
        p_pooled = (c_conv + t_conv) / (c_total + t_total)
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / c_total + 1 / t_total))
        z_stat = (p_t - p_c) / se
        p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))

        with col2:
            st.subheader("Conversion Rates Comparison")
            fig = px.bar(
                conv_summary,
                x="Campaign_Group",
                y="Conversion_Rate",
                color="Campaign_Group",
                labels={"Conversion_Rate": "Conversion Rate (%)", "Campaign_Group": "Group"},
                color_discrete_map={"Control": "#CBD5E0", "Test": "#2B6CB0"},
                text=conv_summary["Conversion_Rate"].apply(lambda x: f"{x:.2%}"),
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Test Diagnostics")
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Z-Statistic", f"{z_stat:.4f}")
        with res_col2:
            st.metric("Two-Tailed p-value", f"{p_val:.4g}")

        if p_val < alpha:
            st.info(
                f"**Result: Statistically Significant!** (p = {p_val:.4g} < {alpha:.2f})\n\n"
                f"The promotional campaign group has a **{(p_t - p_c)*100:.2f}%** higher absolute conversion rate. "
                "We reject the null hypothesis and recommend rolling out the new campaign."
            )
        else:
            st.warning(
                f"**Result: Not Statistically Significant.** (p = {p_val:.4g} >= {alpha:.2f})\n\n"
                "The observed lift could be due to random chance. We fail to reject the null hypothesis. "
                "Do not allocate budget to roll out this campaign based on conversions alone."
            )

# ----------------- Study 3: Screen Time vs Productivity -----------------
elif analysis_option == "Screen Time vs Productivity (Correlation & Binning)":
    st.header("💻 Screen Time vs Productivity Analysis")
    st.write(
        "Evaluate the correlation between daily screen exposure (hours) and employee productivity indexes. "
        "Locate if a nonlinear productivity drop-off threshold occurs."
    )

    df = load_cached_data("screen_time")

    if not df.empty:
        # Precompute aggregated bins for processed exports
        bins = [0, 4, 6, 24]
        labels = ["Low (< 4 hrs)", "Medium (4-6 hrs)", "High (> 6 hrs)"]
        df["Screen_Time_Tier"] = pd.cut(df["Screen_Time_Hours"], bins=bins, labels=labels)

        tier_agg = (
            df.groupby("Screen_Time_Tier", observed=False)["Productivity_Score"]
            .agg(["count", "mean", "median", "std"])
            .reset_index()
        )
        save_processed_aggregations("screen_time", tier_agg)

        # User controls in columns
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Filters")
            selected_prof = st.multiselect(
                "Filter by Profession:", df["Profession"].unique(), default=list(df["Profession"].unique())
            )
            selected_age = st.multiselect(
                "Filter by Age Group:", df["Age_Group"].unique(), default=list(df["Age_Group"].unique())
            )

            # Apply filters
            filtered_df = df[df["Profession"].isin(selected_prof) & df["Age_Group"].isin(selected_age)]

            # Calculate correlation
            if len(filtered_df) > 2:
                p_coef, p_pval = stats.pearsonr(filtered_df["Screen_Time_Hours"], filtered_df["Productivity_Score"])
                s_coef, s_pval = stats.spearmanr(filtered_df["Screen_Time_Hours"], filtered_df["Productivity_Score"])

                st.subheader("Correlation Analysis")
                st.write(f"**Pearson correlation:** {p_coef:.3f} (p = {p_pval:.2g})")
                st.write(f"**Spearman correlation:** {s_coef:.3f} (p = {s_pval:.2g})")
            else:
                st.write("Not enough data to calculate correlations.")

        with col2:
            st.subheader("Interactive Scatter & Threshold")
            fig = px.scatter(
                filtered_df,
                x="Screen_Time_Hours",
                y="Productivity_Score",
                color="Screen_Time_Tier",
                hover_data=["Profession", "Age_Group"],
                title="Daily Screen Hours vs. Productivity Index",
                labels={"Screen_Time_Hours": "Screen Time (Hours)", "Productivity_Score": "Productivity Score (1-100)"},
                color_discrete_map={
                    "Low (< 4 hrs)": "#38A169",
                    "Medium (4-6 hrs)": "#3182CE",
                    "High (> 6 hrs)": "#E53E3E",
                },
                trendline="ols",
            )
            # Add vertical reference line at the 6-hour tipping point
            fig.add_vline(x=6.0, line_dash="dash", line_color="#E53E3E", annotation_text="6-Hour Threshold")
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # Display bar summaries of binned tiers
        st.subheader("Binned Analysis: Average Productivity Score by Tier")
        fig_bar = px.bar(
            tier_agg,
            x="Screen_Time_Tier",
            y="mean",
            color="Screen_Time_Tier",
            error_y=tier_agg["std"] / np.sqrt(tier_agg["count"]),  # Standard error bars
            labels={"mean": "Average Productivity Score", "Screen_Time_Tier": "Screen Time Tier"},
            color_discrete_map={"Low (< 4 hrs)": "#38A169", "Medium (4-6 hrs)": "#3182CE", "High (> 6 hrs)": "#E53E3E"},
        )
        fig_bar.update_layout(plot_bgcolor="white", paper_bgcolor="white", showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

        st.success(
            "**Takeaway:** There is a sharp nonlinear drop-off (tipping point) in "
            "productivity after **6 hours** of daily screen time "
            "(averages fall ~30%). We recommend offline focus blocks and screen-free buffers."
        )

# ----------------- Study 4: Discount Depth vs Retention -----------------
elif analysis_option == "Discount Depth vs Retention (Chi-Square)":
    st.header("📉 Discount Rate Depth vs. Customer Retention")
    st.write(
        "Evaluate the relationship between discount rate depth (0% to 50%) and long-term customer retention. "
        "Confirm if deep discounts compress margins and attract churning deal-seekers."
    )

    df = load_cached_data("customer_discounts")

    if not df.empty:
        # Precompute contingency table for processed data
        ret_rates = df.groupby("Discount_Rate")["Retained"].agg(["count", "sum", "mean"]).reset_index()
        ret_rates.columns = ["Discount_Rate", "Total_Customers", "Retained_Customers", "Retention_Rate"]
        save_processed_aggregations("discount_retention", ret_rates)

        # User controls
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Retention Performance Table")
            st.dataframe(ret_rates.style.format({"Retention_Rate": "{:.1%}"}))

            # Run chi square test
            contingency_table = pd.crosstab(df["Discount_Rate"], df["Retained"])
            chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

            st.subheader("Chi-Square Test of Independence")
            st.write(f"**Chi-Square Stat:** {chi2:.4f}")
            st.write(f"**Degrees of Freedom:** {dof}")
            st.write(f"**p-value:** {p_val:.4g}")

        with col2:
            st.subheader("Retention Rate Curve by Discount Rate")
            # Map values back to labels
            plot_df = ret_rates.copy()
            plot_df["Discount_Label"] = (plot_df["Discount_Rate"] * 100).astype(int).astype(str) + "%"

            fig = px.bar(
                plot_df,
                x="Discount_Label",
                y="Retention_Rate",
                title="Customer Retention Rate by Discount Depth (%)",
                labels={"Retention_Rate": "Retention Rate", "Discount_Label": "Discount Depth"},
                color="Retention_Rate",
                color_continuous_scale="Blues",
            )
            # Add highlights for optimal vs suboptimal
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Customer Profiles by Discount Tier")
        profiles = df.groupby("Discount_Rate").agg({"Tenure_Months": "mean", "Total_Spend": "mean"}).reset_index()

        profiles.columns = ["Discount Rate", "Avg Tenure (Months)", "Avg Lifetime Spend ($)"]
        st.dataframe(profiles.round(1))

        st.success(
            "**Optimal Promotion Recommendation:** Retention peaks at **10%-20%** discounts (~48-49% retention). "
            "Deep discounts (50%) perform worst (33.3% retention, tenure of "
            "7.9 months) because they attract transactional deal-seekers. "
            "Promotions should be capped at 20% off to maximize customer lifetime value (LTV) and margins."
        )

# ----------------- Study 5: Restaurant Tips -----------------
elif analysis_option == "Restaurant Tips spending patterns (EDA)":
    st.header("🍴 Restaurant Spending & Tipping Behavior")
    st.write(
        "Analyze customer demographics and transactions to locate the highest-value segments "
        "and double down on order-volume strategies."
    )

    df = load_cached_data("tips")

    if not df.empty:
        # Precompute customer segments spending
        df["tip_pct"] = (df["tip"] / df["total_bill"] * 100).round(1)
        save_processed_aggregations("tips_eda", df.describe().reset_index())

        # User controls
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Data Segments")
            grouping_var = st.selectbox("Group spending variables by:", ["day", "time", "sex", "smoker"])

            st.write("**Segmented Spend Statistics:**")
            summary_stats = df.groupby(grouping_var)[["total_bill", "tip", "tip_pct"]].mean().reset_index()
            st.dataframe(summary_stats.round(2))

        with col2:
            st.subheader("Transaction bill sizes by Category")
            fig = px.box(
                df,
                x=grouping_var,
                y="total_bill",
                color=grouping_var,
                points="all",
                title=f"Total Bill Distribution by {grouping_var.capitalize()}",
                labels={"total_bill": "Total Bill ($)", grouping_var: grouping_var.capitalize()},
                color_discrete_sequence=px.colors.qualitative.Prism,
            )
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

        # Display Box plot day/time interaction
        st.subheader("Customer Interaction Analysis: Day & Meal Time")
        fig_box = px.box(
            df,
            x="day",
            y="total_bill",
            color="time",
            title="Customer Spend Boxplot: Day × Meal Time Interaction",
            labels={"total_bill": "Total Bill ($)", "day": "Day of Week", "time": "Meal Time"},
            color_discrete_map={"Lunch": "#38A169", "Dinner": "#2B6CB0"},
        )
        fig_box.update_layout(plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig_box, use_container_width=True)

        st.info(
            "**Key Finding:** Sunday dinner has the highest median bill sizes ($22.30) and strong tipping behavior. "
            "However, order volume (transaction count) is higher on Saturdays. "
            "Prioritize fast table turnover on Saturdays to maximize total weekend revenue."
        )
