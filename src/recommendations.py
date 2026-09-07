"""
Sustainability recommendation engine for EcoMind AI.
Generates actionable, non-destructive, advisory recommendations based on analytical insights.
"""

import pandas as pd
from src.insights import get_highest_consuming_building, get_peak_hours

def generate_sustainability_recommendations(df: pd.DataFrame, anomalies_df: pd.DataFrame = None) -> list[dict]:
    """
    Generate actionable sustainability recommendations based on overall campus data and detected anomalies.
    """
    recommendations = []

    # 1. Peak building analysis
    top_bld = get_highest_consuming_building(df)
    recommendations.append({
        "id": "REC-01",
        "category": "Facility Optimization",
        "building": top_bld["building"],
        "title": f"Target Energy Audit for {top_bld['building']}",
        "description": f"{top_bld['building']} accounts for {top_bld['share_percent']:.1f}% of total campus energy usage. Conduct a focused HVAC and lighting efficiency review.",
        "action": "Inspect thermostat setpoints, air filter cleanliness, and scheduled building shutdown routines.",
        "priority": "HIGH",
    })

    # 2. Peak hour analysis
    peak_hours = get_peak_hours(df, top_n=2)
    peak_labels = ", ".join([h["hour_label"] for h in peak_hours])
    recommendations.append({
        "id": "REC-02",
        "category": "Demand Peak Management",
        "building": "Campus-wide",
        "title": "Peak Load Shifting During High-Demand Window",
        "description": f"Peak energy demand consistently concentrates around {peak_labels}.",
        "action": "Schedule high-power laboratory tasks, water pumping, or heavy computing batches outside the peak window.",
        "priority": "HIGH",
    })

    # 3. Off-hour / Low occupancy recommendation
    off_hour_mask = (df["hour"].isin([22, 23, 0, 1, 2, 3, 4, 5])) & (df["occupancy"] <= 10) & (df["energy_kwh"] > 15)
    off_hour_count = off_hour_mask.sum()
    if off_hour_count > 0:
        recommendations.append({
            "id": "REC-03",
            "category": "Baseload Reduction",
            "building": "Multiple Facilities",
            "title": "Automate Nighttime Off-Hour Standby Shutdown",
            "description": f"Identified {off_hour_count} instances of elevated energy usage during night hours despite minimal occupancy.",
            "action": "Configure smart plugs and automated power strips to disconnect idle computing workstations and laboratory displays overnight.",
            "priority": "MEDIUM",
        })

    # 4. Temperature & HVAC recommendation
    high_temp_ac = df[(df["temperature_c"] > 25.0) & (df["ac_units"] >= 4)]
    if not high_temp_ac.empty:
        recommendations.append({
            "id": "REC-04",
            "category": "HVAC Management",
            "building": "Academic & Lab Blocks",
            "title": "Optimize HVAC Temperature Setpoints to 24°C–26°C",
            "description": "High ambient outdoor temperatures drive increased AC compressor cycles.",
            "action": "Standardize air conditioning thermostat setpoints to 24°C and ensure windows remain closed during cooling cycles.",
            "priority": "MEDIUM",
        })

    # 5. Anomaly-specific recommendation if anomalies exist
    if anomalies_df is not None and not anomalies_df.empty:
        anom_count = len(anomalies_df)
        af_bld = anomalies_df["building"].mode().iloc[0] if "building" in anomalies_df.columns else "Campus"
        recommendations.append({
            "id": "REC-05",
            "category": "Anomaly Mitigation",
            "building": af_bld,
            "title": f"Physical Inspection for Detected Anomalies in {af_bld}",
            "description": f"Detected {anom_count} anomalous energy readings requiring advisory attention.",
            "action": "Perform physical maintenance check for stuck dampers, malfunctioning sensors, or un-isolated electrical loads.",
            "priority": "HIGH",
        })

    return recommendations

def calculate_estimated_impact(
    df: pd.DataFrame,
    reduction_percentage: float = 5.0,
    cost_per_kwh: float = 8.0,  # INR per kWh assumption
    co2_kg_per_kwh: float = 0.82,  # kg CO2e per kWh standard assumption
) -> dict:
    """
    Calculate scenario-based estimated savings based on explicit user assumptions.
    Clearly labeled as hypothetical scenario estimates, not measured institutional results.
    """
    total_kwh = float(df["energy_kwh"].sum())
    saved_kwh = total_kwh * (reduction_percentage / 100.0)
    saved_cost = saved_kwh * cost_per_kwh
    saved_co2_kg = saved_kwh * co2_kg_per_kwh
    saved_co2_tons = saved_co2_kg / 1000.0

    return {
        "scenario_reduction_pct": reduction_percentage,
        "total_baseline_kwh": total_kwh,
        "estimated_saved_kwh": saved_kwh,
        "estimated_cost_saved": saved_cost,
        "estimated_co2_avoided_kg": saved_co2_kg,
        "estimated_co2_avoided_tons": saved_co2_tons,
        "assumptions": {
            "cost_per_kwh_currency": "INR 8.0 / kWh (configurable estimate)",
            "emissions_factor": f"{co2_kg_per_kwh} kg CO2e / kWh grid baseline",
            "disclaimer": "Scenario estimate based on user-defined reduction target — not measured campus results.",
        },
    }
