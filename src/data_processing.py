"""
Data processing module for EcoMind AI.
Handles data loading, cleaning, validation, time feature engineering, and ML data prep.
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

REQUIRED_COLUMNS = [
    "timestamp",
    "building",
    "energy_kwh",
    "temperature_c",
    "occupancy",
    "ac_units",
    "equipment_count",
    "day_of_week",
    "hour",
]

NUMERICAL_COLUMNS = [
    "energy_kwh",
    "temperature_c",
    "occupancy",
    "ac_units",
    "equipment_count",
    "day_of_week",
    "hour",
]

def load_data(path: str = "data/energy_data.csv") -> pd.DataFrame:
    """
    Load raw energy dataset from CSV file, validate required schema, and parse timestamps.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset file not found at path: {path}")

    df = pd.read_csv(path)
    
    # Check required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns in dataset: {missing_cols}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = clean_data(df)
    df = create_time_features(df)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset: remove exact duplicates, handle missing values safely, filter invalid values.
    """
    df = df.copy()
    
    # Drop exact duplicates
    df = df.drop_duplicates()

    # Sort chronologically
    df = df.sort_values(by="timestamp").reset_index(drop=True)

    # Handle potential missing values safely
    for col in NUMERICAL_COLUMNS:
        if col in df.columns and df[col].isnull().any():
            # Fill missing numericals with median per building if available
            df[col] = df.groupby("building")[col].transform(lambda x: x.fillna(x.median()))
            df[col] = df[col].fillna(df[col].median())

    # Ensure energy_kwh is non-negative
    if "energy_kwh" in df.columns:
        df["energy_kwh"] = df["energy_kwh"].clip(lower=0.0)

    return df

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract temporal features from timestamp without data leakage.
    """
    df = df.copy()
    if "timestamp" in df.columns:
        df["day_of_week"] = df["timestamp"].dt.dayofweek
        df["hour"] = df["timestamp"].dt.hour
        df["is_weekend"] = df["day_of_week"].apply(lambda d: 1 if d >= 5 else 0)
        df["month"] = df["timestamp"].dt.month
    return df

def encode_building(df: pd.DataFrame, encoder: LabelEncoder = None) -> tuple[pd.DataFrame, LabelEncoder]:
    """
    Encode categorical 'building' column into numerical labels for ML models.
    Returns modified DataFrame with 'building_code' and the LabelEncoder object.
    """
    df = df.copy()
    if encoder is None:
        encoder = LabelEncoder()
        df["building_code"] = encoder.fit_transform(df["building"].astype(str))
    else:
        # Handle unseen building labels safely
        known_classes = set(encoder.classes_)
        df["building_clean"] = df["building"].astype(str).apply(
            lambda x: x if x in known_classes else encoder.classes_[0]
        )
        df["building_code"] = encoder.transform(df["building_clean"])
        if "building_clean" in df.columns:
            df = df.drop(columns=["building_clean"])
            
    return df, encoder

def get_ml_feature_names() -> list[str]:
    """
    Return the list of feature column names used for training ML models.
    """
    return [
        "building_code",
        "temperature_c",
        "occupancy",
        "ac_units",
        "equipment_count",
        "day_of_week",
        "hour",
    ]

def prepare_features(df: pd.DataFrame, encoder: LabelEncoder = None) -> tuple[pd.DataFrame, pd.Series, LabelEncoder]:
    """
    Prepare feature matrix X and target y for forecasting models.
    """
    df_encoded, encoder = encode_building(df, encoder)
    feature_cols = get_ml_feature_names()
    
    X = df_encoded[feature_cols]
    y = df_encoded["energy_kwh"] if "energy_kwh" in df_encoded.columns else None
    
    return X, y, encoder
