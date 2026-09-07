"""
Unit tests for anomaly detection module.
"""

import pytest
import os
import pandas as pd
from src.data_processing import load_data
from src.anomaly_detection import (
    train_anomaly_detector,
    detect_anomalies,
    predict_single_anomaly,
    save_anomaly_pipeline,
    load_anomaly_pipeline,
)

def test_train_anomaly_detector():
    df = load_data("data/energy_data.csv")
    model, features, metrics = train_anomaly_detector(df, contamination=0.03)
    assert model is not None
    assert "anomalies_detected" in metrics
    assert metrics["anomalies_detected"] > 0

def test_detect_anomalies_df():
    df = load_data("data/energy_data.csv")
    model, _, _ = train_anomaly_detector(df, contamination=0.03)
    df_annotated = detect_anomalies(df, model)
    assert "anomaly_status" in df_annotated.columns
    assert "anomaly_score" in df_annotated.columns
    assert set(df_annotated["anomaly_status"].unique()).issubset({"NORMAL", "ANOMALY"})

def test_predict_single_anomaly():
    df = load_data("data/energy_data.csv")
    model, _, _ = train_anomaly_detector(df, contamination=0.03)
    status, score = predict_single_anomaly(
        model=model,
        energy_kwh=100.0,  # Extreme kWh value
        temperature_c=35.0,
        occupancy=5,
        ac_units=10,
        equipment_count=50,
        hour=2,
    )
    assert status in ["NORMAL", "ANOMALY"]
    assert isinstance(score, float)

def test_anomaly_model_persistence(tmp_path):
    df = load_data("data/energy_data.csv")
    model, features, _ = train_anomaly_detector(df)
    save_path = os.path.join(tmp_path, "test_anomaly.joblib")
    save_anomaly_pipeline(model, features, save_path)
    assert os.path.exists(save_path)

    loaded_model, loaded_features = load_anomaly_pipeline(save_path)
    assert loaded_model is not None
    assert loaded_features == features
