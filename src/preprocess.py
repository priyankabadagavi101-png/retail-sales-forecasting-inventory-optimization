import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def basic_checks(df):
    print("Shape:", df.shape)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())
    print("\nNegative values:", (df["qty_sold"] < 0).sum())


def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove negative sales
    df = df[df["qty_sold"] >= 0]

    return df


def add_time_features(df):
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["week"] = df["date"].dt.isocalendar().week.astype(int)

    return df