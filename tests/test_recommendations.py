"""
Unit tests for recommendations and impact module.
"""

import pytest
import pandas as pd
from src.data_processing import load_data
from src.recommendations import generate_sustainability_recommendations, calculate_estimated_impact

def test_generate_recommendations():
    df = load_data("data/energy_data.csv")
    recs = generate_sustainability_recommendations(df)
    assert isinstance(recs, list)
    assert len(recs) > 0
    first_rec = recs[0]
    assert "id" in first_rec
    assert "title" in first_rec
    assert "action" in first_rec
    assert "priority" in first_rec

def test_calculate_estimated_impact():
    df = load_data("data/energy_data.csv")
    impact = calculate_estimated_impact(df, reduction_percentage=5.0)
    assert impact["scenario_reduction_pct"] == 5.0
    assert impact["estimated_saved_kwh"] > 0
    assert impact["estimated_cost_saved"] > 0
    assert impact["estimated_co2_avoided_kg"] > 0
    assert "disclaimer" in impact["assumptions"]
