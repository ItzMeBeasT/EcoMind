"""
Energy forecasting module for EcoMind AI.
Builds, trains, evaluates, persists, and serving machine learning regression models
for predicting campus energy consumption (kWh).
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

from src.data_processing import prepare_features, get_ml_feature_names

def train_forecaster(
    df: pd.DataFrame,
    test_ratio: float = 0.2,
    random_state: int = 42,
    n_estimators: int = 100,
) -> tuple[RandomForestRegressor, LabelEncoder, dict[str, float]]:
    """
    Train a RandomForestRegressor to predict energy consumption (energy_kwh).
    Uses a chronological split to prevent temporal data leakage.
    """
    df_sorted = df.sort_values(by="timestamp").reset_index(drop=True)
    X, y, encoder = prepare_features(df_sorted)

    # Chronological train/test split
    n_samples = len(df_sorted)
    split_idx = int(n_samples * (1.0 - test_ratio))

    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    model = RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    # Evaluate on test set
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics = {
        "mae": float(mae),
        "rmse": float(rmse),
        "r2": float(r2),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
    }

    return model, encoder, metrics

def predict_energy(
    model: RandomForestRegressor,
    encoder: LabelEncoder,
    building: str,
    temperature_c: float,
    occupancy: int,
    ac_units: int,
    equipment_count: int,
    day_of_week: int,
    hour: int,
) -> float:
    """
    Predict energy consumption in kWh for a single building configuration.
    """
    # Safe categorical encoding
    known_classes = set(encoder.classes_)
    clean_building = building if building in known_classes else encoder.classes_[0]
    building_code = int(encoder.transform([clean_building])[0])

    feature_values = pd.DataFrame([{
        "building_code": building_code,
        "temperature_c": float(temperature_c),
        "occupancy": int(occupancy),
        "ac_units": int(ac_units),
        "equipment_count": int(equipment_count),
        "day_of_week": int(day_of_week),
        "hour": int(hour),
    }])[get_ml_feature_names()]

    pred = model.predict(feature_values)[0]
    return float(max(0.0, pred))

def save_forecasting_pipeline(
    model: RandomForestRegressor,
    encoder: LabelEncoder,
    filepath: str = "models/energy_forecaster.joblib",
) -> str:
    """
    Save trained forecasting model and categorical encoder to disk using joblib.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    pipeline_payload = {
        "model": model,
        "encoder": encoder,
        "features": get_ml_feature_names(),
    }
    joblib.dump(pipeline_payload, filepath)
    return filepath

def load_forecasting_pipeline(
    filepath: str = "models/energy_forecaster.joblib",
) -> tuple[RandomForestRegressor, LabelEncoder]:
    """
    Load saved forecasting pipeline from disk.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Forecasting model file not found at: {filepath}")

    payload = joblib.load(filepath)
    return payload["model"], payload["encoder"]
