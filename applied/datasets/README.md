# Datasets

All datasets used in the applied notebooks and case studies.

## Sources

| Dataset | Source | Used In | Description |
|---------|--------|---------|-------------|
| `tips.csv` | [seaborn built-in](https://github.com/mwaskom/seaborn-data) | Notebooks 1, 2, 3 | Restaurant tips data: total bill, tip, day, time, party size |
| `ecommerce.csv` | [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) | Notebooks 4, 5, 6 | Online retail transactions with customer IDs and purchase amounts |
| `marketing_campaign.csv` | Synthetic | Notebook 7 | A/B test data for marketing campaign effectiveness |
| `screen_time.csv` | Synthetic | Case Study 1 | Screen time hours vs productivity scores |
| `customer_discounts.csv` | Synthetic | Case Study 2 | Discount rates vs customer retention |

## Loading Data

```python
import pandas as pd

# From the datasets directory
tips = pd.read_csv("../datasets/tips.csv")

# Or use seaborn's built-in
import seaborn as sns
tips = sns.load_dataset("tips")
```

## Notes

- Synthetic datasets are generated with realistic distributions and documented seed values for reproducibility
- Large datasets (>10MB) are not stored in the repo — download scripts are provided instead
- All datasets are used for educational purposes only
