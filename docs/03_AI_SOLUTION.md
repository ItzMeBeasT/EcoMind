# EcoMind AI — Technical AI Solution Architecture

## Solution Overview

EcoMind AI is an integrated campus sustainability intelligence platform that combines supervised regression, unsupervised anomaly detection, explainable insight generation, RAG document search, and a conversational AI agent.

---

## Technical Components

```text
Raw Campus Data (CSV)
   ↓
Data Processing & Feature Engineering (src/data_processing.py)
   ↓
┌──────────────────────────────┬──────────────────────────────┐
│  Energy Forecasting Model    │  Anomaly Detection Model     │
│  (RandomForestRegressor)     │  (IsolationForest)           │
└──────────────────────────────┴──────────────────────────────┘
   ↓                               ↓
Explainable Insight Engine (src/insights.py)
   ↓
Sustainability Recommendation Engine (src/recommendations.py)
   ↓
RAG Knowledge Base & Conversational Agent ("Ask EcoMind")
   ↓
Interactive Streamlit Dashboard (dashboard/app.py)
```

### 1. Machine Learning Forecasting (`src/forecasting.py`)
- **Algorithm**: `RandomForestRegressor`
- **Features**: `building_code`, `temperature_c`, `occupancy`, `ac_units`, `equipment_count`, `day_of_week`, `hour`
- **Split Protocol**: Chronological train/test split (80/20) to eliminate temporal data leakage.
- **Performance Achieved**: MAE = 1.36 kWh | RMSE = 1.71 kWh | $R^2$ = 0.9356

### 2. Anomaly Detection (`src/anomaly_detection.py`)
- **Algorithm**: `IsolationForest`
- **Goal**: Identify abnormal multivariate energy consumption patterns.
- **Output**: Decision scores and explicit classification (`NORMAL` vs `ANOMALY`).

### 3. Explainable Insight & Recommendation Engines
- **Non-Causal Language**: Advisory explanations framing findings as "possible contributing factors".
- **Actionable Output**: Target energy audits, peak load shifting, standby shutdown, and HVAC setpoint adjustments.

### 4. Conversational AI Agent ("Ask EcoMind")
- **Hallucination Prevention**: Decouples deterministic analytics calculations from natural language generation.
- **RAG Integration**: Retrieves policy guidelines from `data/knowledge_base/` for regulatory/guideline queries.
