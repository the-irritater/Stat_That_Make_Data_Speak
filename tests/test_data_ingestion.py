from pathlib import Path

import pandas as pd
import pytest

from stats_series.data_loader import DataLoader


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


def test_validate_primary_key_duplicates():
    loader = DataLoader()
    # Create invalid ecommerce df with duplicate Customer_ID
    invalid_ecommerce = pd.DataFrame(
        {
            "Customer_ID": [1, 1],
            "Session_Duration": [12.5, 14.2],
            "Pages_Visited": [8, 10],
            "Discount_Applied": ["Yes", "No"],
            "Total_Spend": [120.50, 150.00],
            "Repeat_Purchase": [1, 0],
            "Recency": [15, 30],
            "Frequency": [4, 5],
            "Monetary": [480.0, 750.0],
        }
    )
    with pytest.raises(ValueError, match="contains duplicate primary keys"):
        loader.validate_dataframe(invalid_ecommerce, "ecommerce")


def test_validate_categorical_outliers():
    loader = DataLoader()
    # Create invalid marketing df with categorical outliers
    invalid_marketing = pd.DataFrame(
        {
            "User_ID": [101, 102],
            "Campaign_Group": ["Control", "SuperTest"],  # 'SuperTest' is not valid
            "Converted": [0, 1],
            "Purchase_Amount": [0.0, 45.0],
        }
    )
    with pytest.raises(ValueError, match="contains unexpected values"):
        loader.validate_dataframe(invalid_marketing, "marketing_campaign")


def test_dashboard_data_loading_utility(tmp_path, monkeypatch):
    from dashboard.interactive_dashboard import load_cached_data

    # Set the RAW_DATA_DIR to a temporary directory for testing
    monkeypatch.setattr("dashboard.interactive_dashboard.RAW_DATA_DIR", tmp_path)

    # Test handling of missing file
    df_missing = load_cached_data("non_existent_dataset")
    assert df_missing.empty

    # Test loading of valid file
    temp_df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    temp_df.to_csv(tmp_path / "valid_dataset.csv", index=False)

    df_valid = load_cached_data("valid_dataset")
    assert not df_valid.empty
    assert list(df_valid.columns) == ["col1", "col2"]


def test_dataloader_validation_edge_cases(tmp_path):
    import json

    # 1. Non-existent schema file -> FileNotFoundError
    with pytest.raises(FileNotFoundError, match="Schema file not found"):
        DataLoader(schema_path=tmp_path / "non_existent_schema.json")

    # Write a custom valid schema to a temporary file
    custom_schema = {
        "custom_dataset": {
            "columns": {
                "id": {"type": "integer", "primary_key": True, "nullable": False},
                "val_int": {"type": "integer", "options": [0, 1]},
                "val_float": {"type": "float", "nullable": False},
            }
        }
    }

    schema_file = tmp_path / "schema.json"
    with open(schema_file, "w") as f:
        json.dump(custom_schema, f)

    # Initialize loader with custom schema
    # Override get_raw_data_path to return a path in tmp_path
    class TestLoader(DataLoader):
        def get_raw_data_path(self, dataset_name):
            return tmp_path / f"{dataset_name}.csv"

    loader = TestLoader(schema_path=schema_file)

    # 2. Dataset not defined in schema -> ValueError
    with pytest.raises(ValueError, match="not defined in the schema"):
        loader.load_dataset("unregistered_dataset")

    # 3. Dataset file not found -> FileNotFoundError
    with pytest.raises(FileNotFoundError, match="Dataset file not found"):
        loader.load_dataset("custom_dataset")

    # Create base valid dataframe
    valid_df = pd.DataFrame({"id": [1, 2], "val_int": [0, 1], "val_float": [1.5, 2.5]})
    csv_path = tmp_path / "custom_dataset.csv"
    valid_df.to_csv(csv_path, index=False)

    # Verify valid load
    df_loaded = loader.load_dataset("custom_dataset")
    assert not df_loaded.empty

    # 4. Nullability check: id is non-nullable but has NaN
    invalid_null_df = pd.DataFrame({"id": [1, None], "val_int": [0, 1], "val_float": [1.5, 2.5]})
    with pytest.raises(ValueError, match="contains 1 null values but is marked non-nullable"):
        loader.validate_dataframe(invalid_null_df, "custom_dataset")

    # 5. Exact integer check: non-integer numeric values
    invalid_int_df = pd.DataFrame({"id": [1.5, 2.0], "val_int": [0, 1], "val_float": [1.5, 2.5]})  # 1.5 is float
    with pytest.raises(TypeError, match="expected integer values, got non-integer numeric values"):
        loader.validate_dataframe(invalid_int_df, "custom_dataset")

    # 6. Integer check: non-numeric type (e.g. object/string)
    invalid_type_df = pd.DataFrame({"id": ["one", "two"], "val_int": [0, 1], "val_float": [1.5, 2.5]})
    with pytest.raises(TypeError, match="expected integer, got"):
        loader.validate_dataframe(invalid_type_df, "custom_dataset")

    # 7. Allowed values options check: options is not category, val_int has value 2 (not in [0, 1])
    invalid_opt_df = pd.DataFrame({"id": [1, 2], "val_int": [0, 2], "val_float": [1.5, 2.5]})
    with pytest.raises(ValueError, match="has values outside allowed set"):
        loader.validate_dataframe(invalid_opt_df, "custom_dataset")

    # 8. Minimum/maximum numeric validation checks
    custom_schema_minmax = {
        "custom_dataset_minmax": {
            "columns": {
                "id": {"type": "integer", "primary_key": True, "nullable": False},
                "val_float": {"type": "float", "nullable": False, "minimum": 1.0, "maximum": 5.0},
            }
        }
    }
    schema_file_minmax = tmp_path / "schema_minmax.json"
    with open(schema_file_minmax, "w") as f:
        json.dump(custom_schema_minmax, f)

    loader_minmax = TestLoader(schema_path=schema_file_minmax)

    # Valid dataframe
    valid_minmax_df = pd.DataFrame({"id": [1, 2], "val_float": [1.5, 4.5]})
    assert loader_minmax.validate_dataframe(valid_minmax_df, "custom_dataset_minmax") is True

    # Below minimum
    invalid_min_df = pd.DataFrame({"id": [1, 2], "val_float": [0.5, 4.5]})
    with pytest.raises(ValueError, match="has values below minimum limit 1.0"):
        loader_minmax.validate_dataframe(invalid_min_df, "custom_dataset_minmax")

    # Above maximum
    invalid_max_df = pd.DataFrame({"id": [1, 2], "val_float": [1.5, 5.5]})
    with pytest.raises(ValueError, match="has values above maximum limit 5.0"):
        loader_minmax.validate_dataframe(invalid_max_df, "custom_dataset_minmax")
