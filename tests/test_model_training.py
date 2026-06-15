import numpy as np
import pandas as pd
import pytest

from src.analysis_pipeline import calculate_correlation, fit_ols_regression, run_chi_square_test


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
