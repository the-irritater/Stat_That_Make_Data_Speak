from pathlib import Path

import pandas as pd
import pytest

from src.data_loader import DataLoader


def test_data_loader_init():
    loader = DataLoader()
    assert loader.root_dir.exists()
    assert loader.schema_path.exists()
    assert "tips" in loader.schema


def test_raw_data_path():
    loader = DataLoader()
    path = loader.get_raw_data_path("tips")
    assert isinstance(path, Path)
    assert path.name == "tips.csv"


def test_validate_valid_dataframe():
    loader = DataLoader()
    # Create a valid tips df
    valid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    # This should complete without exceptions
    assert loader.validate_dataframe(valid_tips, "tips") is True


def test_validate_missing_columns():
    loader = DataLoader()
    # Missing 'size' column
    invalid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
        }
    )
    with pytest.raises(ValueError, match="missing expected columns"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_validate_invalid_categorical():
    loader = DataLoader()
    # Invalid 'sex' option 'Unknown'
    invalid_tips = pd.DataFrame(
        {
            "total_bill": [15.20, 22.40],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Unknown"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    with pytest.raises(ValueError, match="contains unexpected values"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_validate_invalid_type():
    loader = DataLoader()
    # 'total_bill' is text/string instead of numeric float
    invalid_tips = pd.DataFrame(
        {
            "total_bill": ["fifteen", "twenty-two"],
            "tip": [2.50, 4.00],
            "sex": ["Male", "Female"],
            "smoker": ["No", "Yes"],
            "day": ["Thur", "Sat"],
            "time": ["Lunch", "Dinner"],
            "size": [2, 4],
        }
    )
    with pytest.raises(TypeError, match="expected float"):
        loader.validate_dataframe(invalid_tips, "tips")


def test_load_real_tips_dataset():
    loader = DataLoader()
    df = loader.load_dataset("tips")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "total_bill" in df.columns
