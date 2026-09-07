"""
Anomaly detection module for EcoMind AI.
Uses IsolationForest to detect unusual campus energy consumption patterns.
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

ANOMALY_FEATURE_NAMES = [
    "energy_kwh",
    "temperature_c",
    "occupancy",
    "ac_units",
    "equipment_count",
    "hour",
]

def train_anomaly_detector(
    df: pd.DataFrame,
    contamination: float = 0.03,
    random_state: int = 42,
    n_estimators: int = 100,
) -> tuple[IsolationForest, list[str], dict[str, float]]:
    """
    Train IsolationForest model to identify energy consumption anomalies.
    """
    X = df[ANOMALY_FEATURE_NAMES].copy()

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_estimators=n_estimators,
        n_jobs=-1,
    )
    model.fit(X)

    predictions = model.predict(X)
    anomaly_count = int((predictions == -1).sum())
    normal_count = int((predictions == 1).sum())

    metrics = {
        "total_records": len(X),
        "anomalies_detected": anomaly_count,
        "normal_records": normal_count,
        "anomaly_percentage": float(anomaly_count / len(X) * 100),
    }

    return model, ANOMALY_FEATURE_NAMES, metrics

def detect_anomalies(
    df: pd.DataFrame,
    model: IsolationForest,
) -> pd.DataFrame:
    """
    Annotate DataFrame with anomaly classification and decision scores.
    """
    df_out = df.copy()
    X = df_out[ANOMALY_FEATURE_NAMES].copy()

    # IsolationForest decision_function: lower/negative means more anomalous
    scores = model.decision_function(X)
    predictions = model.predict(X)

    df_out["anomaly_score"] = scores
    df_out["is_anomaly"] = predictions == -1
    df_out["anomaly_status"] = df_out["is_anomaly"].map({True: "ANOMALY", False: "NORMAL"})

    return df_out

def predict_single_anomaly(
    model: IsolationForest,
    energy_kwh: float,
    temperature_c: float,
    occupancy: int,
    ac_units: int,
    equipment_count: int,
    hour: int,
) -> tuple[str, float]:
    """
    Predict anomaly status ('NORMAL' or 'ANOMALY') and score for a single input record.
    """
    sample = pd.DataFrame([{
        "energy_kwh": float(energy_kwh),
        "temperature_c": float(temperature_c),
        "occupancy": int(occupancy),
        "ac_units": int(ac_units),
        "equipment_count": int(equipment_count),
        "hour": int(hour),
    }])[ANOMALY_FEATURE_NAMES]

    score = float(model.decision_function(sample)[0])
    pred = int(model.predict(sample)[0])
    status = "ANOMALY" if pred == -1 else "NORMAL"

    return status, score

def save_anomaly_pipeline(
    model: IsolationForest,
    feature_names: list[str] = ANOMALY_FEATURE_NAMES,
    filepath: str = "models/anomaly_detector.joblib",
) -> str:
    """
    Save trained IsolationForest model to disk using joblib.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    payload = {
        "model": model,
        "features": feature_names,
    }
    joblib.dump(payload, filepath)
    return filepath

def load_anomaly_pipeline(
    filepath: str = "models/anomaly_detector.joblib",
) -> tuple[IsolationForest, list[str]]:
    """
    Load saved IsolationForest pipeline from disk.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Anomaly detector model file not found at: {filepath}")

    payload = joblib.load(filepath)
    return payload["model"], payload["features"]
