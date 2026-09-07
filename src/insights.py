"""
Explainable insight engine for EcoMind AI.
Extracts analytical summaries, peak consumption periods, building usage patterns,
and anomaly contextual factors using non-causal advisory language.
"""

import pandas as pd
import numpy as np

def get_overall_summary(df: pd.DataFrame) -> dict:
    """
    Get top-level KPI metrics for the dataset.
    """
    total_energy = float(df["energy_kwh"].sum())
    avg_energy = float(df["energy_kwh"].mean())
    max_record = df.loc[df["energy_kwh"].idxmax()]
    
    return {
        "total_records": len(df),
        "total_energy_kwh": total_energy,
        "avg_energy_kwh": avg_energy,
        "max_energy_record": {
            "building": max_record["building"],
            "timestamp": str(max_record["timestamp"]),
            "energy_kwh": float(max_record["energy_kwh"]),
            "temperature_c": float(max_record["temperature_c"]),
            "occupancy": int(max_record["occupancy"]),
        },
        "num_buildings": df["building"].nunique(),
        "buildings": list(df["building"].unique()),
    }

def get_building_insights(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize energy metrics grouped by building.
    """
    building_stats = df.groupby("building").agg(
        total_energy_kwh=("energy_kwh", "sum"),
        avg_energy_kwh=("energy_kwh", "mean"),
        max_energy_kwh=("energy_kwh", "max"),
        avg_occupancy=("occupancy", "mean"),
        avg_temperature=("temperature_c", "mean"),
    ).reset_index()

    building_stats = building_stats.sort_values(by="total_energy_kwh", ascending=False)
    highest_building = building_stats.iloc[0]["building"]
    
    building_stats["share_percent"] = (
        building_stats["total_energy_kwh"] / building_stats["total_energy_kwh"].sum() * 100
    )
    return building_stats

def get_highest_consuming_building(df: pd.DataFrame) -> dict:
    """
    Identify the building with the highest total and average energy consumption.
    """
    stats = get_building_insights(df)
    top_row = stats.iloc[0]
    return {
        "building": top_row["building"],
        "total_energy_kwh": float(top_row["total_energy_kwh"]),
        "avg_energy_kwh": float(top_row["avg_energy_kwh"]),
        "share_percent": float(top_row["share_percent"]),
    }

def get_hourly_demand_profile(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate average energy consumption by hour of the day.
    """
    hourly = df.groupby("hour").agg(
        avg_energy_kwh=("energy_kwh", "mean"),
        total_energy_kwh=("energy_kwh", "sum"),
        avg_occupancy=("occupancy", "mean"),
        avg_temperature=("temperature_c", "mean"),
    ).reset_index().sort_values(by="hour")

    return hourly

def get_peak_hours(df: pd.DataFrame, top_n: int = 3) -> list[dict]:
    """
    Identify the top N highest-demand hours across the campus dataset.
    """
    hourly = get_hourly_demand_profile(df)
    top_hours = hourly.sort_values(by="avg_energy_kwh", ascending=False).head(top_n)
    
    result = []
    for _, row in top_hours.iterrows():
        result.append({
            "hour": int(row["hour"]),
            "hour_label": f"{int(row['hour']):02d}:00",
            "avg_energy_kwh": float(row["avg_energy_kwh"]),
            "avg_occupancy": float(row["avg_occupancy"]),
        })
    return result

def analyze_anomaly_context(anomaly_row: pd.Series, df_baseline: pd.DataFrame) -> list[str]:
    """
    Analyze an anomalous row and generate contextual advisory explanations.
    Uses non-causal language ('possible contributing factor').
    """
    factors = []
    building = anomaly_row.get("building", "Selected building")
    building_df = df_baseline[df_baseline["building"] == building] if "building" in df_baseline.columns else df_baseline

    avg_occupancy = building_df["occupancy"].mean() if not building_df.empty else 10
    avg_temp = building_df["temperature_c"].mean() if not building_df.empty else 20
    avg_kwh = building_df["energy_kwh"].mean() if not building_df.empty else 15

    curr_kwh = anomaly_row["energy_kwh"]
    curr_occ = anomaly_row["occupancy"]
    curr_temp = anomaly_row["temperature_c"]
    curr_ac = anomaly_row.get("ac_units", 0)
    curr_eq = anomaly_row.get("equipment_count", 0)
    curr_hour = anomaly_row.get("hour", 0)

    if curr_kwh > avg_kwh * 1.4:
        factors.append(f"Energy consumption ({curr_kwh:.1f} kWh) is significantly above building baseline average ({avg_kwh:.1f} kWh).")

    if curr_occ < avg_occupancy * 0.5 and curr_kwh > avg_kwh * 1.2:
        factors.append(f"Low occupancy ({curr_occ} occupants vs avg {avg_occupancy:.0f}) paired with high consumption indicates possible off-hour equipment/HVAC operation.")

    if curr_temp > avg_temp + 3.0:
        factors.append(f"High ambient temperature ({curr_temp:.1f}°C vs avg {avg_temp:.1f}°C) is a possible contributing factor increasing cooling demand.")

    if curr_ac >= 6 and curr_temp > 24.0:
        factors.append(f"Multiple active AC units ({curr_ac} units) combined with elevated temperature are potential contributing factors.")

    if curr_eq >= 30:
        factors.append(f"High operational equipment load ({curr_eq} devices active) is a possible contributing factor.")

    if curr_hour in [22, 23, 0, 1, 2, 3, 4, 5]:
        factors.append(f"Observation occurs during non-operational late hours ({curr_hour:02d}:00), suggesting unmitigated baseload or idle equipment operation.")

    if not factors:
        factors.append("Consumption deviates significantly from multivariate statistical baseline patterns.")

    return factors
