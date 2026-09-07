"""
EcoMind AI Factsheet Module.
Provides enterprise-grade model metadata, governance, data lineage, risk assessment, and human oversight specs.
"""

def get_ecomind_factsheet() -> dict:
    """
    Generate structured EcoMind AI Factsheet metadata.
    """
    return {
        "system_name": "EcoMind AI — Campus Energy Intelligence Platform",
        "version": "v1.0 (showcase edition)",
        "intended_domain": "Educational Campus Sustainability & Facilities Energy Optimization",
        "primary_sdg_target": "SDG 7 — Affordable and Clean Energy (Target 7.3)",
        "models_used": [
            {
                "name": "IBM Granite 13B / watsonx.ai Foundation Model",
                "role": "Generative Reasoning, Narrative Explanation, Report Generation & Agentic Interaction",
                "provider": "IBM Cloud / watsonx.ai REST API (Fallback: Local Deterministic Engine)",
            },
            {
                "name": "RandomForestRegressor",
                "role": "Supervised Energy Demand Forecasting (kWh)",
                "validation_performance": "MAE: 1.36 kWh | RMSE: 1.71 kWh | R²: 0.9356",
            },
            {
                "name": "IsolationForest",
                "role": "Unsupervised Multivariate Anomaly Detection",
                "contamination_rate": "3.01% (260 anomalous records in evaluation dataset)",
            },
        ],
        "data_lineage": {
            "dataset_type": "Synthetic Campus Smart Meter Data (8,640 hourly observations across 4 facilities)",
            "privacy_rating": "Zero Personally Identifiable Information (PII) — Facility-level aggregation only",
            "features_evaluated": ["building_code", "temperature_c", "occupancy", "ac_units", "equipment_count", "hour", "day_of_week"],
        },
        "risk_and_governance": {
            "risk_classification": "Low Risk / Advisory Decision Support System",
            "human_in_the_loop": "Mandatory — Facility managers retain sole authority over physical HVAC & electrical controls",
            "guardrail_layers": ["Input Prompt Safety Filter", "Output Numerical Grounding Verification", "Non-Causal Language Formatting"],
        },
        "system_capabilities": [
            "Supervised Energy Load Forecasting",
            "Multivariate Isolation Anomaly Detection",
            "Explainable Contributing Factor Analysis",
            "Actionable Sustainability Advisories",
            "RAG Knowledge Retrieval over Campus Policies",
            "Multimodal Sustainability Document Intelligence",
            "Interactive Impact Scenario Simulator",
        ],
    }
