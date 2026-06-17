import numpy as np
import pandas as pd
import pytest

from stats_series.analysis_pipeline import calculate_correlation, fit_ols_regression, run_chi_square_test


def test_fit_ols_regression():
    # Generate mock data: Y = 3 * X + 10 + small_noise
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    noise = np.random.normal(0, 0.1, 100)
    y = 3.0 * x + 10.0 + noise
    df = pd.DataFrame({"X": x, "Y": y})

    model = fit_ols_regression(df, "Y ~ X")

    # Verify model outputs
    assert hasattr(model, "params")
    assert hasattr(model, "pvalues")
    assert hasattr(model, "rsquared")

    # Use tolerance checks
    intercept = model.params["Intercept"]
    slope = model.params["X"]

    assert abs(intercept - 10.0) < 0.1
    assert abs(slope - 3.0) < 0.05
    assert model.rsquared > 0.95
    assert model.pvalues["X"] < 0.001


def test_run_chi_square_test():
    # Create strongly dependent categorical variables
    # Category A: mostly Val1
    # Category B: mostly Val2
    data = []
    for _ in range(100):
        data.append({"cat1": "A", "cat2": "Val1"})
    for _ in range(10):
        data.append({"cat1": "A", "cat2": "Val2"})
    for _ in range(10):
        data.append({"cat1": "B", "cat2": "Val1"})
    for _ in range(100):
        data.append({"cat1": "B", "cat2": "Val2"})

    df = pd.DataFrame(data)

    results = run_chi_square_test(df, "cat1", "cat2")

    assert "chi2" in results
    assert "p_value" in results
    assert results["dof"] == 1
    assert results["p_value"] < 0.001

    # Expected table check: shapes must match contingency table
    assert results["expected"].shape == (2, 2)
    # Check shape of contingency table
    assert results["contingency_table"].shape == (2, 2)


def test_calculate_correlation():
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    # Positive correlation
    y_pos = 2 * x + np.random.normal(0, 1, 50)
    # Negative correlation
    y_neg = -2 * x + np.random.normal(0, 1, 50)

    df = pd.DataFrame({"X": x, "Y_pos": y_pos, "Y_neg": y_neg})

    # Test positive correlation
    coef_pos, p_pos = calculate_correlation(df, "X", "Y_pos", method="pearson")
    assert coef_pos > 0.8
    assert p_pos < 0.001

    # Test negative correlation
    coef_neg, p_neg = calculate_correlation(df, "X", "Y_neg", method="pearson")
    assert coef_neg < -0.8
    assert p_neg < 0.001

    # Test spearman method
    coef_sp, p_sp = calculate_correlation(df, "X", "Y_pos", method="spearman")
    assert coef_sp > 0.8
    assert p_sp < 0.001


def test_calculate_correlation_exceptions():
    df = pd.DataFrame({"X": [1.0], "Y": [2.0]})  # Only 1 row

    with pytest.raises(ValueError, match="At least 2 non-null observations"):
        calculate_correlation(df, "X", "Y")

    with pytest.raises(KeyError):
        calculate_correlation(df, "X", "Z")


def test_fit_ols_regression_exceptions_and_cov():
    # Test TypeError for non-DataFrame input
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        fit_ols_regression("not a dataframe", "Y ~ X")

    # Test fit with robust standard errors (cov_type="HC3")
    df = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [2, 4, 5, 4, 5]})
    model = fit_ols_regression(df, "Y ~ X", cov_type="HC3")
    assert model.cov_type == "HC3"


def test_run_chi_square_exceptions():
    df = pd.DataFrame({"cat1": ["A", "B"], "cat2": ["Val1", "Val2"]})
    # Test KeyError for missing columns
    with pytest.raises(KeyError, match="not found in DataFrame"):
        run_chi_square_test(df, "cat1", "missing_col")


def test_calculate_correlation_invalid_method():
    df = pd.DataFrame({"X": [1.0, 2.0, 3.0], "Y": [2.0, 4.0, 5.0]})
    # Test ValueError for invalid method
    with pytest.raises(ValueError, match="Method must be either 'pearson' or 'spearman'"):
        calculate_correlation(df, "X", "Y", method="invalid_method")
