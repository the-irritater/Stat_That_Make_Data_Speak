import json
from pathlib import Path

import pandas as pd


class DataLoader:
    def __init__(self, schema_path=None):
        self.root_dir = Path(__file__).resolve().parents[2]

        if schema_path is None:
            schema_path = self.root_dir / "data" / "data-schema.json"

        self.schema_path = Path(schema_path)
        self.schema = self._load_schema()

    def _load_schema(self):
        """Loads and parses the data schema JSON file."""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found at: {self.schema_path}")
        with open(self.schema_path, "r") as f:
            return json.load(f)

    def get_raw_data_path(self, dataset_name):
        """Returns the absolute path to a raw dataset file."""
        filename = f"{dataset_name}.csv"
        return self.root_dir / "data" / "raw" / filename

    def load_dataset(self, name):
        """Loads a dataset by name, performs column schema validation, and returns a DataFrame.

        Args:
            name (str): Name of the dataset (e.g., 'tips', 'ecommerce')

        Returns:
            pd.DataFrame: Validated DataFrame
        """
        if name not in self.schema:
            raise ValueError(f"Dataset '{name}' is not defined in the schema.")

        file_path = self.get_raw_data_path(name)
        if not file_path.exists():
            raise FileNotFoundError(f"Dataset file not found at: {file_path}")

        df = pd.read_csv(file_path)
        self.validate_dataframe(df, name)
        return df

    def validate_dataframe(self, df, name):
        """Validates that a DataFrame conforms to the specified schema."""
        dataset_schema = self.schema[name]
        expected_cols = dataset_schema["columns"]

        # 1. Column presence verification
        missing_cols = [col for col in expected_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Validation failed for dataset '{name}': missing expected columns: {missing_cols}")

        # 2. Per-column validation
        for col_name, col_meta in expected_cols.items():
            expected_type = col_meta["type"]

            # 2a. Check for duplicates in primary keys
            if col_meta.get("primary_key") is True:
                if df[col_name].duplicated().any():
                    duplicated_keys = df[col_name][df[col_name].duplicated()].unique().tolist()
                    raise ValueError(
                        f"Validation failed for dataset '{name}': column '{col_name}' "
                        f"contains duplicate primary keys: {duplicated_keys}"
                    )

            # 2b. Nullability check (default: nullable unless explicitly set to false)
            if col_meta.get("nullable") is False:
                if df[col_name].isnull().any():
                    null_count = df[col_name].isnull().sum()
                    raise ValueError(
                        f"Validation failed for dataset '{name}': column '{col_name}' "
                        f"contains {null_count} null values but is marked non-nullable"
                    )

            # 2c. Categorical options validation
            if expected_type == "category" and "options" in col_meta:
                invalid_entries = [
                    val for val in df[col_name].unique() if val not in col_meta["options"] and pd.notna(val)
                ]
                if invalid_entries:
                    raise ValueError(
                        f"Validation failed for dataset '{name}': column '{col_name}' "
                        f"contains unexpected values: {invalid_entries}. Expected options: {col_meta['options']}"
                    )

            # 2d. Integer type validation (strict: must be integer dtype, not float)
            elif expected_type == "integer":
                if not pd.api.types.is_integer_dtype(df[col_name]):
                    # Allow numeric columns that happen to be all whole numbers
                    if pd.api.types.is_numeric_dtype(df[col_name]):
                        non_int_vals = df[col_name].dropna()
                        if not (non_int_vals == non_int_vals.astype(int)).all():
                            raise TypeError(
                                f"Validation failed for dataset '{name}': column '{col_name}' "
                                f"expected integer values, got non-integer numeric values"
                            )
                    else:
                        raise TypeError(
                            f"Validation failed for dataset '{name}': column '{col_name}' "
                            f"expected integer, got {df[col_name].dtype}"
                        )

            # 2e. Float type validation
            elif expected_type == "float":
                if not pd.api.types.is_numeric_dtype(df[col_name]):
                    raise TypeError(
                        f"Validation failed for dataset '{name}': column '{col_name}' "
                        f"expected float, got {df[col_name].dtype}"
                    )

            # 2f. Allowed values validation (for non-category types with 'options', e.g. binary integers)
            if "options" in col_meta and expected_type != "category":
                non_null_vals = df[col_name].dropna()
                invalid = non_null_vals[~non_null_vals.isin(col_meta["options"])]
                if len(invalid) > 0:
                    raise ValueError(
                        f"Validation failed for dataset '{name}': column '{col_name}' "
                        f"has values outside allowed set {col_meta['options']}: "
                        f"{invalid.unique().tolist()[:5]}"
                    )

        return True
