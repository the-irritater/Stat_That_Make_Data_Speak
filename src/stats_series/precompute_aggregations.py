from pathlib import Path

import pandas as pd

from stats_series.analysis_pipeline import fit_ols_regression, run_chi_square_test
from stats_series.data_loader import DataLoader


def main():
    print("Starting precomputation of analytical aggregates...")

    loader = DataLoader()
    processed_dir = Path(__file__).resolve().parents[2] / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    # 1. Restaurant Tips EDA summaries
    try:
        df_tips = loader.load_dataset("tips")
        # Tip percent
        df_tips["tip_pct"] = (df_tips["tip"] / df_tips["total_bill"] * 100).round(1)

        # Summary statistics by Day and Meal Time
        tips_summary = (
            df_tips.groupby(["day", "time"], observed=False)[["total_bill", "tip", "tip_pct"]]
            .agg(["count", "mean", "median", "std"])
            .reset_index()
        )

        # Flatten multi-index columns
        tips_summary.columns = [f"{col[0]}_{col[1]}" if col[1] else col[0] for col in tips_summary.columns]
        tips_summary.to_csv(processed_dir / "tips_aggregations.csv", index=False)
        print("  ✓ tips_aggregations.csv precomputed.")
    except Exception as e:
        print(f"  ✗ Failed to precompute tips: {e}")

    # 2. E-commerce Regression coefficients
    try:
        df_ecom = loader.load_dataset("ecommerce")
        # Fit models
        model_simple = fit_ols_regression(df_ecom, "Total_Spend ~ Session_Duration")
        model_multiple = fit_ols_regression(df_ecom, "Total_Spend ~ Session_Duration + Pages_Visited")

        # Save coefficients
        ecom_results = pd.DataFrame(
            {
                "Model": ["Simple Linear", "Simple Linear", "Multiple Linear", "Multiple Linear", "Multiple Linear"],
                "Parameter": ["Intercept", "Session_Duration", "Intercept", "Session_Duration", "Pages_Visited"],
                "Coefficient": [
                    model_simple.params["Intercept"],
                    model_simple.params["Session_Duration"],
                    model_multiple.params["Intercept"],
                    model_multiple.params["Session_Duration"],
                    model_multiple.params["Pages_Visited"],
                ],
                "p_value": [
                    model_simple.pvalues["Intercept"],
                    model_simple.pvalues["Session_Duration"],
                    model_multiple.pvalues["Intercept"],
                    model_multiple.pvalues["Session_Duration"],
                    model_multiple.pvalues["Pages_Visited"],
                ],
                "R_squared": [
                    model_simple.rsquared,
                    model_simple.rsquared,
                    model_multiple.rsquared,
                    model_multiple.rsquared,
                    model_multiple.rsquared,
                ],
            }
        )
        ecom_results.to_csv(processed_dir / "ecommerce_regression_summary.csv", index=False)
        print("  ✓ ecommerce_regression_summary.csv precomputed.")
    except Exception as e:
        print(f"  ✗ Failed to precompute ecommerce: {e}")

    # 3. Marketing A/B Test conversions
    try:
        df_mkt = loader.load_dataset("marketing_campaign")
        mkt_agg = df_mkt.groupby("Campaign_Group")["Converted"].agg(["count", "sum", "mean"]).reset_index()
        mkt_agg.columns = ["Campaign_Group", "Users", "Conversions", "Conversion_Rate"]

        # Run hypothesis test parameters
        results = run_chi_square_test(df_mkt, "Campaign_Group", "Converted")
        mkt_agg["Chi2_Statistic"] = results["chi2"]
        mkt_agg["p_value"] = results["p_value"]

        mkt_agg.to_csv(processed_dir / "marketing_conversions_summary.csv", index=False)
        print("  ✓ marketing_conversions_summary.csv precomputed.")
    except Exception as e:
        print(f"  ✗ Failed to precompute marketing: {e}")

    # 4. Screen Time vs Productivity Tiers
    try:
        df_screen = loader.load_dataset("screen_time")
        bins = [0, 4, 6, 24]
        labels = ["Low (< 4 hrs)", "Medium (4-6 hrs)", "High (> 6 hrs)"]
        df_screen["Screen_Time_Tier"] = pd.cut(df_screen["Screen_Time_Hours"], bins=bins, labels=labels)

        screen_agg = (
            df_screen.groupby("Screen_Time_Tier", observed=False)["Productivity_Score"]
            .agg(["count", "mean", "median", "std"])
            .reset_index()
        )

        screen_agg.to_csv(processed_dir / "screen_time_productivity_summary.csv", index=False)
        print("  ✓ screen_time_productivity_summary.csv precomputed.")
    except Exception as e:
        print(f"  ✗ Failed to precompute screen time: {e}")

    # 5. Customer Discount Retention Tiers
    try:
        df_disc = loader.load_dataset("customer_discounts")
        disc_agg = df_disc.groupby("Discount_Rate")["Retained"].agg(["count", "sum", "mean"]).reset_index()
        disc_agg.columns = ["Discount_Rate", "Total_Customers", "Retained_Customers", "Retention_Rate"]

        profiles = df_disc.groupby("Discount_Rate").agg({"Tenure_Months": "mean", "Total_Spend": "mean"}).reset_index()
        profiles.columns = ["Discount_Rate", "Avg_Tenure_Months", "Avg_Total_Spend"]

        disc_summary = pd.merge(disc_agg, profiles, on="Discount_Rate")
        disc_summary.to_csv(processed_dir / "customer_discounts_retention_summary.csv", index=False)
        print("  ✓ customer_discounts_retention_summary.csv precomputed.")
    except Exception as e:
        print(f"  ✗ Failed to precompute customer discounts: {e}")

    print("Aggregations precomputation finished successfully!")


if __name__ == "__main__":
    main()
