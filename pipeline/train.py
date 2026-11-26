"""Stage 4: train -- fit a model on the training split."""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def train_model(X: pd.DataFrame, y: pd.Series, max_depth: int) -> DecisionTreeRegressor:
    """Fit and return a decision-tree regressor with the given max_depth."""
    model = DecisionTreeRegressor(max_depth=max_depth, random_state=0)
    model.fit(X, y)
    return model
