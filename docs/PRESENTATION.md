# EcoMind AI — 12-Slide Pitch Deck Structure

**Project Title**: EcoMind AI: An AI-Powered Campus Energy Optimization and Sustainability Agent  
**Presenter**: [YOUR NAME] ([YOUR COLLEGE NAME])  
**Submission**: 1M1B AI for Sustainability Virtual Internship (IBM SkillsBuild & AICTE)  

---

## Slide 1: Title & Introduction
- **Header**: EcoMind AI — Campus Sustainability Intelligence
- **Subtitle**: An AI-Powered Campus Energy Optimization and Sustainability Agent
- **Presenter**: [YOUR NAME] | [YOUR COLLEGE NAME]
- **Primary SDG**: SDG 7 — Affordable & Clean Energy

---

## Slide 2: The Core Problem
- **Context**: Educational institutions consume massive electricity across academic blocks, labs, libraries, hostels, and admin offices.
- **Key Challenges**:
  - Facility managers lack real-time visibility into unusual energy waste.
  - Energy waste is discovered weeks later when utility bills arrive.
  - Unpredictable weather and schedule fluctuations complicate manual load planning.

---

## Slide 3: Why It Matters
- **Institutional Cost**: High electrical utility bills drain administrative educational budgets.
- **Carbon Footprint**: Grid electricity dependence drives significant indirect CO2 emissions.
- **Sustainability Mandate**: Educational campuses must lead by example in energy conservation.

---

## Slide 4: Proposed Solution — EcoMind AI
- **Overview**: An end-to-end campus sustainability management platform combining machine learning analytics, automated anomaly detection, actionable advisories, and grounded AI chat.
- **Core Pillars**:
  - Supervised Demand Forecasting
  - Unsupervised Anomaly Detection
  - Explainable Insight Engine
  - Grounded Conversational AI Assistant

---

## Slide 5: SDG Alignment
- **Primary SDG 7**: Affordable & Clean Energy (Target 7.3: Double energy efficiency improvement rate).
- **Secondary SDG 11**: Sustainable Cities & Communities (Smart green campus infrastructure).
- **Secondary SDG 13**: Climate Action (Quantifiable CO2 emissions reduction).

---

## Slide 6: System Architecture & Workflow
- **Pipeline Flow**:
  - Data Processing & Feature Engineering
  - ML Forecasting (`RandomForestRegressor`) & Anomaly Detection (`IsolationForest`)
  - Rule-Based Advisory Recommendation Engine
  - RAG Knowledge Base & Conversational AI Agent ("Ask EcoMind")
  - Streamlit Web Dashboard Interface

---

## Slide 7: Core AI & Machine Learning Components
- **Energy Forecaster**: Predicts kWh consumption based on temp, occupancy, AC units, equipment count, hour. Achieved $R^2 = 0.9356$.
- **Anomaly Detector**: `IsolationForest` identifies off-hour baseload waste and abnormal spikes.
- **Grounded AI Agent**: Decouples numerical calculations from LLM text generation to prevent hallucinations.

---

## Slide 8: Interactive Dashboard Features
- **Live KPI Metrics**: Total kWh, average load, peak building, and active anomaly count.
- **4 Interactive Demo Scenarios**: Normal operation, high temp/occupancy, high lab usage, low occupancy off-hour waste.
- **Interactive ML Forecasting Tool**: Custom parameter input for instant load predictions.

---

## Slide 9: Responsible AI & Governance
- **Privacy First**: Zero PII collected; data aggregated per facility block.
- **Fairness & Non-Discrimination**: Objective physical and environmental metrics only.
- **Human Oversight**: Advisory recommendations; facility managers retain final authority.
- **Transparent Claims**: Synthetic demo dataset clearly labeled; non-causal language used.

---

## Slide 10: Expected Impact & Scenario Modeling
- **Hypothetical 5% Reduction Scenario**:
  - Energy Saved: ~7,500 kWh (Demo dataset baseline)
  - Financial Saved: ~₹60,000 (INR 8.0/kWh tariff assumption)
  - CO2 Avoided: ~6.15 Tons CO2e
- **Disclaimer**: Scenario estimate based on explicit user assumptions — not measured campus results.

---

## Slide 11: Limitations & Future Scope
- **Current Limitations**: Synthetic dataset; offline batch analytics model.
- **Future Roadmap**:
  - Real-time IoT smart meter integration.
  - Weather API & solar renewable energy integration.
  - Carbon-intensity dynamic grid optimization.
  - Automated alert notifications via SMS/Email.

---

## Slide 12: Conclusion & Thank You
- **Summary**: EcoMind AI transforms raw campus electricity data into actionable, responsible sustainability intelligence.
- **Closing**: Thank you to 1M1B, IBM SkillsBuild, and AICTE for this opportunity.
- **Q&A**: Open for judges' questions.
