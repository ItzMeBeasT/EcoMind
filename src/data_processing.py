import pandas as pd

def load_data(path="data/energy_data.csv"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df

def prepare_features(df):
    df = df.copy()
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    df["hour"] = df["timestamp"].dt.hour
    return df
