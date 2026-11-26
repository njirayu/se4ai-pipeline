"""Stage 1: collect -- load raw sales from one or more CSV files."""
from pathlib import Path

import pandas as pd


def load_sales(paths: list[Path]) -> pd.DataFrame:
    """Read every CSV in `paths` and return one DataFrame with all rows.

    Input:  list of CSV paths, each with columns
            sqft, bedrooms, year_built, region, sold_date, price
    Output: a single DataFrame (raw, uncleaned)
    """
    return pd.concat([pd.read_csv(p) for p in paths], ignore_index=True)
