# Changelog

All notable changes to the "Stats Series" project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to Semantic Versioning.

---

## [v1.0.0-2026Q2-analysis] - 2026-06-16

### Added
- **Centralized Data Directory:** Created a root `data/` folder containing subdirectories `data/raw/` for raw immutable data and `data/processed/` for reproducible precomputed aggregations.
- **Data Documentation:** Introduced `data/DATA_README.md` to detail dataset sources, parameters, licensing, and privacy constraints.
- **Data Validation Schema:** Added `data/data-schema.json` mapping columns, options, units, and descriptions for validation checks.
- **Modular Data Loader:** Added `src/data_loader.py` defining the `DataLoader` class to fetch and validate data schemas dynamically.
- **Refactored Analysis Library:** Created `src/analysis_pipeline.py` containing modular functions for regression fitting, Chi-Square independence tests, and correlation metrics.
- **Comprehensive Testing Suite:** Added pytest test files `tests/test_data_ingestion.py` and `tests/test_model_training.py` with tolerance-based comparisons.
- **CI/CD Integration:** Implemented GitHub Actions CI in `.github/workflows/tests.yml` to run checks on code quality, format, and tests under Python 3.11.
- **Code Quality Controls:** Integrated configurations for `black`, `isort`, and `flake8` within `pyproject.toml` and `.flake8`.
- **Streamlit Interactive Dashboard:** Created `dashboard/interactive_dashboard.py` implementing parameter control, visual outputs, and cached computations for data exploration.
- **Standards & Code of Conduct:** Added `CODE_OF_CONDUCT.md` based on the Contributor Covenant.
- **Collaborative Validation:** prototyped `applied/notebooks/collaborative_peer_validation.ipynb` template for peer review replication.

### Changed
- **Path Restructuring:** Migrated dataset directories. Replaced all references from `../datasets/` or `../../datasets/` to the root-level `data/raw/` folder in notebooks, case studies, and Python scripts.
- **Ignores and Safeguards:** Updated `.gitignore` to prevent committing strategy spreadsheets, LinkedIn captions, monetization planning, and virtualenv artifacts to public repositories.
- **Dependency Management:** Configured Poetry (`pyproject.toml` and `poetry.lock`) to maintain reproducible package states alongside a convenience `requirements.txt` fallback file.
