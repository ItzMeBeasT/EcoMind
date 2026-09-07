"""
Unit tests for data processing module.
"""

import pytest
import pandas as pd
import numpy as np
from src.data_processing import load_data, clean_data, create_time_features, prepare_features

def test_load_data():
    df = load_data("data/energy_data.csv")
    assert not df.empty
    assert "timestamp" in df.columns
    assert "building" in df.columns
    assert "energy_kwh" in df.columns

def test_clean_data_no_negatives():
    raw_df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-01-01 00:00:00", "2026-01-01 01:00:00"]),
        "building": ["Library", "Library"],
        "energy_kwh": [-5.0, 10.0],
        "temperature_c": [20.0, 21.0],
        "occupancy": [5, 10],
        "ac_units": [2, 2],
        "equipment_count": [10, 10],
        "day_of_week": [3, 3],
        "hour": [0, 1],
    })
    cleaned = clean_data(raw_df)
    assert (cleaned["energy_kwh"] >= 0.0).all()

def test_create_time_features():
    df = pd.DataFrame({"timestamp": pd.to_datetime(["2026-01-01 14:00:00"])})
    feat_df = create_time_features(df)
    assert "hour" in feat_df.columns
    assert "day_of_week" in feat_df.columns
    assert feat_df["hour"].iloc[0] == 14

def test_prepare_features():
    df = load_data("data/energy_data.csv")
    X, y, encoder = prepare_features(df)
    assert "building_code" in X.columns
    assert "temperature_c" in X.columns
    assert len(X) == len(y)
    assert encoder is not None
