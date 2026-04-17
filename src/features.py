import pandas as pd

def create_features(df):
    df = df.sort_values(["product_id", "date"])

    # Lag features (past demand)
    df["lag_1"] = df.groupby("product_id")["qty_sold"].shift(1)
    df["lag_7"] = df.groupby("product_id")["qty_sold"].shift(7)

    # Rolling mean (trend)
    df["rolling_mean_7"] = df.groupby("product_id")["qty_sold"].shift(1).rolling(7).mean()

    # Rolling std (volatility)
    df["rolling_std_7"] = df.groupby("product_id")["qty_sold"].shift(1).rolling(7).std()

    return df.dropna()
