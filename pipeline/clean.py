"""Stage 2: clean -- fix types and drop rows we cannot trust."""
import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw sales.

    Guarantees for the next stage:
      * sold_date is a datetime column
      * sqft has no missing values
      * rows with an obviously wrong price (<= 10,000) are removed
    """
    df = df.copy()
    # The 2026 export writes dates as ISO 8601 with a time and timezone
    # ("2026-02-23T10:30:00+07:00"); 2025 has plain dates ("2025-08-25").
    # ISO8601 reads both; utc=True puts the mixed offsets on one timeline.
    df["sold_date"] = pd.to_datetime(df["sold_date"], format="ISO8601", utc=True)
    # sqft is the strongest predictor of price, so a row without it cannot be
    # trusted; drop it rather than invent a value (12 of 650 rows in 2026 Q1).
    df = df.dropna(subset=["sqft"])
    df = df[df["price"] > 10_000]           # drop obvious data-entry errors (price typos)
    return df
