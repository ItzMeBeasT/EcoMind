"""
Unit tests for forecasting module.
"""

import pytest
import os
import pandas as pd
from src.data_processing import load_data
from src.forecasting import (
    train_forecaster,
    predict_energy,
    save_forecasting_pipeline,
    load_forecasting_pipeline,
)

def test_train_forecaster():
    df = load_data("data/energy_data.csv")
    model, encoder, metrics = train_forecaster(df, test_ratio=0.2, random_state=42)
    assert model is not None
    assert encoder is not None
    assert "mae" in metrics
    assert "rmse" in metrics
    assert "r2" in metrics
    assert metrics["r2"] > 0.5  # Expect reasonable performance

def test_predict_energy():
    df = load_data("data/energy_data.csv")
    model, encoder, _ = train_forecaster(df)
    pred_kwh = predict_energy(
        model=model,
        encoder=encoder,
        building="Academic Block",
        temperature_c=25.0,
        occupancy=20,
        ac_units=4,
        equipment_count=20,
        day_of_week=2,
        hour=14,
    )
    assert isinstance(pred_kwh, float)
    assert pred_kwh >= 0.0

def test_model_persistence(tmp_path):
    df = load_data("data/energy_data.csv")
    model, encoder, _ = train_forecaster(df)
    save_path = os.path.join(tmp_path, "test_forecaster.joblib")
    save_forecasting_pipeline(model, encoder, save_path)
    assert os.path.exists(save_path)

    loaded_model, loaded_encoder = load_forecasting_pipeline(save_path)
    assert loaded_model is not None
    assert loaded_encoder is not None
