# EcoMind AI — Phase 1: Data Exploration

## Project
EcoMind AI: An AI-Powered Campus Energy Optimization and Sustainability Agent

## Primary SDG
SDG 7 — Affordable and Clean Energy

---

## 1. Objective

The purpose of Phase 1 is to understand the campus energy dataset before developing the AI components of EcoMind AI.

We will analyze energy consumption patterns and identify useful relationships between energy consumption, temperature, occupancy, and other factors.

The findings from this phase will be used to design:

- Energy forecasting
- Anomaly detection
- Sustainability recommendations
- AI-powered decision support

---

## 2. Dataset

The prototype uses a synthetic campus energy dataset created for development and demonstration.

Each record represents the energy consumption of a campus building at a particular time.

### Features

| Feature | Description |
|---|---|
| `timestamp` | Date and time of the observation |
| `building` | Campus building |
| `energy_kwh` | Energy consumption in kWh |
| `temperature_c` | Temperature in Celsius |
| `occupancy` | Estimated number of occupants |
| `ac_units` | Number of AC units |
| `equipment_count` | Number of electrical devices |
| `day_of_week` | Day of the week |
| `hour` | Hour of the day |

---

## 3. Questions to Answer

### Question 1 — Which building consumes the most energy?

We will calculate the total, average, and maximum energy consumption for each building.

This helps identify buildings that may require greater attention during energy optimization.

---

### Question 2 — What hours have the highest demand?

We will calculate average energy consumption for every hour of the day.

This helps identify peak-demand periods and possible opportunities for energy optimization.

---

### Question 3 — How does temperature relate to energy consumption?

We will investigate the relationship between temperature and energy consumption using correlation analysis and visualization.

This may help determine whether temperature should be used as a feature in the forecasting model.

---

### Question 4 — How does occupancy relate to energy consumption?

We will investigate the relationship between occupancy and energy consumption.

Higher occupancy may affect cooling, lighting, computing equipment, and other electrical loads.

The data will determine whether occupancy is useful for prediction rather than assuming a relationship.

---

### Question 5 — Where do abnormal consumption patterns appear?

The synthetic dataset contains intentionally injected high-consumption patterns.

We will identify unusually high energy observations and investigate:

- Building
- Timestamp
- Energy consumption
- Temperature
- Occupancy

These observations will later help us test the anomaly-detection component.

---

## 4. Data Quality Checks

Before developing machine-learning models, we will check:

- Dataset dimensions
- Column types
- Missing values
- Duplicate records
- Basic statistics
- Minimum and maximum values

---

## 5. Visualizations

Phase 1 will generate:

1. Campus energy consumption over time
2. Average energy consumption by building
3. Average energy consumption by hour
4. Occupancy versus energy consumption

---

## 6. AI Connection

The findings from Phase 1 will be used in the following pipeline:

```text
Raw Data
   ↓
Data Exploration
   ↓
Feature Understanding
   ↓
Energy Forecasting
   ↓
Anomaly Detection
   ↓
Recommendation Engine
   ↓
AI Sustainability Agent
   ↓
Dashboard