"""
Single pipeline execution script for EcoMind AI.
Loads dataset, trains ML forecasting & anomaly detection models, evaluates metrics,
and persists artifacts into models/ directory.
"""

import sys
import os

from src.data_processing import load_data
from src.forecasting import train_forecaster, save_forecasting_pipeline
from src.anomaly_detection import train_anomaly_detector, save_anomaly_pipeline

def main():
    print("EcoMind AI Model Training")
    print("--------------------------")

    data_path = "data/energy_data.csv"
    if not os.path.exists(data_path):
        print(f"Error: Dataset file not found at {data_path}")
        sys.exit(1)

    # 1. Load and process data
    print(f"Loading data from {data_path}...")
    df = load_data(data_path)
    print(f"Dataset records: {len(df)}")
    print(f"Buildings present: {list(df['building'].unique())}")
    print()

    # 2. Train Forecasting Model
    print("Training Energy Forecasting Model (RandomForestRegressor)...")
    forecaster_model, encoder, forecaster_metrics = train_forecaster(
        df, test_ratio=0.2, random_state=42
    )

    print("Forecasting Performance:")
    print(f"  MAE:  {forecaster_metrics['mae']:.4f} kWh")
    print(f"  RMSE: {forecaster_metrics['rmse']:.4f} kWh")
    print(f"  R2:   {forecaster_metrics['r2']:.4f}")
    print(f"  Train samples: {forecaster_metrics['train_samples']} | Test samples: {forecaster_metrics['test_samples']}")
    print()

    # 3. Train Anomaly Detection Model
    print("Training Anomaly Detection Model (IsolationForest)...")
    anomaly_model, feature_names, anomaly_metrics = train_anomaly_detector(
        df, contamination=0.03, random_state=42
    )

    print("Anomaly Detector:")
    print(f"  Training completed.")
    print(f"  Anomalies detected in dataset: {anomaly_metrics['anomalies_detected']} ({anomaly_metrics['anomaly_percentage']:.2f}%)")
    print()

    # 4. Save Models
    print("Saving models to models/ directory...")
    fc_path = save_forecasting_pipeline(forecaster_model, encoder, "models/energy_forecaster.joblib")
    anom_path = save_anomaly_pipeline(anomaly_model, feature_names, "models/anomaly_detector.joblib")

    print(f"Saved forecasting model to: {fc_path}")
    print(f"Saved anomaly detector model to: {anom_path}")
    print()
    print("Models saved successfully.")

if __name__ == "__main__":
    main()
