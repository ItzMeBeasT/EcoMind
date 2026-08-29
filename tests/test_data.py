from src.data_processing import load_data

def test_dataset_loads():
    df = load_data()
    assert len(df) > 0
    assert "energy_kwh" in df.columns
