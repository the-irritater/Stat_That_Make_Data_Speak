import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols


def fit_ols_regression(df, formula, cov_type=None):
    """Fits an Ordinary Least Squares (OLS) linear regression model.

    Args:
        df (pd.DataFrame): Input DataFrame
        formula (str): Patsy formula string (e.g. 'Total_Spend ~ Session_Duration')
        cov_type (str, optional): Covariance estimator type. Use 'HC3' for
            heteroscedasticity-robust standard errors. Defaults to None (classical OLS).

    Returns:
        statsmodels.regression.linear_model.RegressionResultsWrapper: Fit model object
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if cov_type is not None:
        model = ols(formula, data=df).fit(cov_type=cov_type)
    else:
        model = ols(formula, data=df).fit()
    return model


def run_chi_square_test(df, col1, col2):
    """Performs a Chi-Square Test of Independence between two categorical columns.

    Args:
        df (pd.DataFrame): Input DataFrame
        col1 (str): First categorical column name
        col2 (str): Second categorical column name

    Returns:
        dict: Results dictionary containing chi2, p_value, dof, and expected matrix.
    """
    if col1 not in df.columns or col2 not in df.columns:
        raise KeyError(f"Columns '{col1}' or '{col2}' not found in DataFrame.")

    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

    return {"chi2": chi2, "p_value": p_val, "dof": dof, "expected": expected, "contingency_table": contingency_table}


def calculate_correlation(df, col1, col2, method="pearson"):
    """Calculates correlation coefficient and p-value between two numerical columns.

    Args:
        df (pd.DataFrame): Input DataFrame
        col1 (str): First numerical column name
        col2 (str): Second numerical column name
        method (str): Correlation method ('pearson' or 'spearman')

    Returns:
        tuple: (correlation_coefficient, p_value)
    """
    if col1 not in df.columns or col2 not in df.columns:
        raise KeyError(f"Columns '{col1}' or '{col2}' not found in DataFrame.")

    # Drop rows with NaN in the selected columns
    clean_df = df[[col1, col2]].dropna()

    if len(clean_df) < 2:
        raise ValueError("At least 2 non-null observations are required to compute correlation.")

    if method.lower() == "pearson":
        coef, p_val = stats.pearsonr(clean_df[col1], clean_df[col2])
    elif method.lower() == "spearman":
        coef, p_val = stats.spearmanr(clean_df[col1], clean_df[col2])
    else:
        raise ValueError("Method must be either 'pearson' or 'spearman'")

    return coef, p_val
