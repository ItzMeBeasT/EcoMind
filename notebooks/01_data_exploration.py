
### `notebooks/01_data_exploration
"""
EcoMind AI
Phase 1 — Data Exploration

This script explores the campus energy dataset
before developing the AI models.
"""

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATA
# ============================================================

DATA_PATH = "../data/energy_data.csv"

df = pd.read_csv(
    DATA_PATH,
    parse_dates=["timestamp"]
)

print("=" * 60)
print("ECOMIND AI — PHASE 1: DATA EXPLORATION")
print("=" * 60)


# ============================================================
# 2. DATASET OVERVIEW
# ============================================================

print("\n[1] DATASET SHAPE")
print("-" * 40)

print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]}")


print("\n[2] FIRST 5 RECORDS")
print("-" * 40)

print(df.head())


print("\n[3] COLUMN TYPES")
print("-" * 40)

print(df.dtypes)


# ============================================================
# 3. DATA QUALITY
# ============================================================

print("\n[4] MISSING VALUES")
print("-" * 40)

print(df.isnull().sum())


print("\n[5] DUPLICATE RECORDS")
print("-" * 40)

print(f"Duplicate rows: {df.duplicated().sum()}")


print("\n[6] BASIC STATISTICS")
print("-" * 40)

print(df.describe())


# ============================================================
# 4. ENERGY BY BUILDING
# ============================================================

print("\n[7] ENERGY CONSUMPTION BY BUILDING")
print("-" * 40)

building_energy = (
    df.groupby("building")["energy_kwh"]
    .agg(
        total_energy="sum",
        average_energy="mean",
        maximum_energy="max"
    )
    .sort_values(
        "total_energy",
        ascending=False
    )
)

print(building_energy)

highest_building = building_energy.index[0]

print(
    f"\nHighest total energy consumer: "
    f"{highest_building}"
)


# ============================================================
# 5. ENERGY BY HOUR
# ============================================================

print("\n[8] AVERAGE ENERGY BY HOUR")
print("-" * 40)

hourly_energy = (
    df.groupby("hour")["energy_kwh"]
    .mean()
    .sort_values(ascending=False)
)

print(hourly_energy)

peak_hour = hourly_energy.index[0]

print(
    f"\nHighest average-demand hour: "
    f"{peak_hour}:00"
)


# ============================================================
# 6. CORRELATION ANALYSIS
# ============================================================

print("\n[9] CORRELATION WITH ENERGY")
print("-" * 40)

correlation = (
    df[
        [
            "energy_kwh",
            "temperature_c",
            "occupancy",
            "ac_units",
            "equipment_count"
        ]
    ]
    .corr()["energy_kwh"]
    .sort_values(ascending=False)
)

print(correlation)


# ============================================================
# 7. TEMPERATURE RELATIONSHIP
# ============================================================

print("\n[10] TEMPERATURE VS ENERGY")
print("-" * 40)

temperature_correlation = (
    df["temperature_c"]
    .corr(df["energy_kwh"])
)

print(
    f"Correlation: "
    f"{temperature_correlation:.3f}"
)


# ============================================================
# 8. OCCUPANCY RELATIONSHIP
# ============================================================

print("\n[11] OCCUPANCY VS ENERGY")
print("-" * 40)

occupancy_correlation = (
    df["occupancy"]
    .corr(df["energy_kwh"])
)

print(
    f"Correlation: "
    f"{occupancy_correlation:.3f}"
)


# ============================================================
# 9. HIGHEST ENERGY RECORDS
# ============================================================

print("\n[12] TOP 10 HIGHEST ENERGY RECORDS")
print("-" * 40)

top_records = (
    df.nlargest(
        10,
        "energy_kwh"
    )
    [
        [
            "timestamp",
            "building",
            "energy_kwh",
            "temperature_c",
            "occupancy"
        ]
    ]
)

print(
    top_records.to_string(
        index=False
    )
)


# ============================================================
# 10. EXPLORATORY ANOMALY CHECK
# ============================================================

print("\n[13] HIGH-CONSUMPTION RECORDS")
print("-" * 40)

threshold = df["energy_kwh"].quantile(0.95)

possible_anomalies = df[
    df["energy_kwh"] > threshold
]

print(
    f"95th percentile threshold: "
    f"{threshold:.2f} kWh"
)

print(
    f"Records above threshold: "
    f"{len(possible_anomalies)}"
)

print(
    possible_anomalies[
        [
            "timestamp",
            "building",
            "energy_kwh",
            "temperature_c",
            "occupancy"
        ]
    ]
    .sort_values(
        "energy_kwh",
        ascending=False
    )
    .head(20)
    .to_string(index=False)
)


# ============================================================
# 11. GRAPH — ENERGY OVER TIME
# ============================================================

campus_energy = (
    df.groupby("timestamp")["energy_kwh"]
    .sum()
)

plt.figure(figsize=(12, 5))

plt.plot(
    campus_energy.index,
    campus_energy.values
)

plt.title(
    "Campus Energy Consumption Over Time"
)

plt.xlabel("Time")
plt.ylabel("Energy Consumption (kWh)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()


# ============================================================
# 12. GRAPH — BUILDING COMPARISON
# ============================================================

building_average = (
    df.groupby("building")["energy_kwh"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 5))

building_average.plot(
    kind="bar"
)

plt.title(
    "Average Energy Consumption by Building"
)

plt.xlabel("Building")
plt.ylabel("Average Energy Consumption (kWh)")

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()


# ============================================================
# 13. GRAPH — HOURLY DEMAND
# ============================================================

hourly_average = (
    df.groupby("hour")["energy_kwh"]
    .mean()
)

plt.figure(figsize=(10, 5))

hourly_average.plot(
    kind="line",
    marker="o"
)

plt.title(
    "Average Energy Consumption by Hour"
)

plt.xlabel("Hour of Day")
plt.ylabel("Average Energy Consumption (kWh)")

plt.xticks(range(24))

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 14. GRAPH — OCCUPANCY VS ENERGY
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["occupancy"],
    df["energy_kwh"],
    alpha=0.25
)

plt.title(
    "Occupancy vs Energy Consumption"
)

plt.xlabel("Occupancy")

plt.ylabel(
    "Energy Consumption (kWh)"
)

plt.tight_layout()

plt.show()


# ============================================================
# 15. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PHASE 1 SUMMARY")
print("=" * 60)

print(
    f"Highest energy-consuming building : "
    f"{highest_building}"
)

print(
    f"Peak average-demand hour          : "
    f"{peak_hour}:00"
)

print(
    f"Temperature correlation            : "
    f"{temperature_correlation:.3f}"
)

print(
    f"Occupancy correlation              : "
    f"{occupancy_correlation:.3f}"
)

print(
    f"Exploratory high-consumption threshold : "
    f"{threshold:.2f} kWh"
)

print("\nPhase 1 data exploration completed.")
print("Next step: Energy forecasting.")
