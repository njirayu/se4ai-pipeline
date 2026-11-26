"""Stage 3: features -- turn cleaned sales into the model's inputs.

Training and prediction must both call this one function, so the model
always sees features encoded the same way (no training-serving skew).
"""
import pandas as pd


def encode(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return (X, y): feature matrix and target price.

    X columns: sqft, bedrooms, age, and one 0/1 column per region.
    """
    df = df.copy()
    df["age"] = df["sold_date"].dt.year - df["year_built"]
    X = pd.get_dummies(df[["sqft", "bedrooms", "age", "region"]], columns=["region"], dtype=int)
    y = df["price"]
    return X, y
