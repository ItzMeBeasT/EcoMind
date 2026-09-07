# EcoMind AI — Campus Energy Intelligence Platform
### IBM AI for Sustainability Showcase Edition

Submitted for the **1M1B AI for Sustainability Virtual Internship** in collaboration with **IBM SkillsBuild** and **AICTE**.

---

## 📌 Problem Statement

Educational institutions consume significant electricity across classrooms, computer laboratories, libraries, hostels, and administrative buildings. Campus administrators often lack automated, intelligent tools to:
- Identify unusual energy spikes or off-hour baseload waste in real time.
- Understand multivariate demand patterns driven by ambient weather and facility occupancy.
- Forecast future energy demand accurately to optimize HVAC and equipment schedules.
- Receive grounded, explainable sustainability recommendations without hallucinated claims.

---

## 💡 Core Solution

**EcoMind AI** is an integrated, production-ready campus sustainability intelligence platform that combines energy analytics, machine learning regression, unsupervised anomaly detection, grounded RAG knowledge retrieval, and IBM Granite foundation models via watsonx.ai. 

EcoMind AI provides decision support for institutional sustainability teams to track, predict, and reduce campus energy waste.

---

## 🤖 AI Architecture & IBM Technologies

1. **IBM Granite Foundation Model Integration (`IBMGraniteProvider`)**:
   - Integrates `ibm/granite-13b-chat-v2` via watsonx.ai REST APIs.
   - Provides AI prompt template workflows (Prompt Lab experience) for energy analysis, anomaly explanations, and executive briefings.
   - **Zero-Crash Fallback**: Operates in `DEMO / LOCAL MODE` when IBM credentials are missing, utilizing a deterministic, zero-hallucination local engine.
2. **Supervised Demand Forecasting (`RandomForestRegressor`)**:
   - Predicts building energy consumption (kWh) based on ambient temperature, occupancy, active AC units, equipment count, and temporal features ($R^2 = 0.9356$, $\text{MAE} = 1.36\text{ kWh}$).
3. **Unsupervised Anomaly Detection (`IsolationForest`)**:
   - Scans multivariate feature space to detect off-hour standby power waste, HVAC anomalies, and abnormal load spikes.
4. **Document Intelligence & Multimodal Capability**:
   - Extracts and summarizes uploaded PDF/TXT sustainability policies, identifying campus-relevant energy efficiency recommendations.
5. **Grounded Agentic Workflow & RAG**:
   - "Ask EcoMind" conversational agent routes intents to deterministic tools (pandas data lookups, ML forecasters, anomaly engines, RAG search) to eliminate numerical hallucinations.

---

## 🎯 Sustainable Development Goal (SDG) Alignment

- **Primary Alignment**: **SDG 7 — Affordable and Clean Energy** (Target 7.3: Double the global rate of improvement in energy efficiency by 2030).
- **Secondary Alignments**:
  - **SDG 11 — Sustainable Cities and Communities** (Smart green campus infrastructure).
  - **SDG 13 — Climate Action** (Quantifiable CO2 emissions mitigation).

---

## 🛠️ Technology Stack

- **Frontend & UX**: Streamlit 1.25+, Custom Light Pastel SaaS CSS Design System (Inter typography, soft mint/blue cards)
- **Machine Learning**: Scikit-Learn (`RandomForestRegressor`, `IsolationForest`), Joblib
- **Data Engine**: Pandas, NumPy
- **AI & RAG**: IBM Granite (`watsonx.ai`), Custom TF-IDF Knowledge Base Retriever
- **Testing & QA**: Pytest (21 passed unit tests)
- **Containerization**: Docker, Google Cloud Run Ready

---

## 📊 Dataset & Responsible AI Disclosure

> [!IMPORTANT]
> **Synthetic Demonstration Dataset**: EcoMind AI uses a synthetic campus energy dataset (`data/energy_data.csv`, 8,640 hourly records) modeled on institutional energy behavior. All findings, forecasts, and impact simulations serve decision-support purposes. EcoMind AI provides recommendations and does not autonomously alter physical campus infrastructure.

---

## ✨ Application Navigation & Modules

The platform features 15 modular pages logically structured into 6 operational areas:

- **OVERVIEW**: Dashboard Overview (KPI cards, sparklines, energy trends)
- **INTELLIGENCE**: Energy Analytics, Anomaly Center, Energy Forecast
- **AI**: Ask EcoMind (Agent), AI Studio (Prompt Lab), Knowledge Hub (RAG & Document Intelligence), AI Evaluation & Factsheet, Executive Brief
- **ACTION**: Recommendations & Action Plan, Impact Simulator
- **TRUST**: Responsible AI Panel, EcoMind AI Factsheet
- **SHOWCASE**: IBM Technology Map & Architecture, Demo Scenarios, SDLC & Engineering

---

## 🚀 Installation & Local Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ItzMeBeasT/EcoMind.git
   cd EcoMind
   ```

2. **Configure Environment Variables**:
   ```bash
   cp .env.example .env
   ```
   *(Optionally add `IBM_WATSONX_API_KEY`, `IBM_WATSONX_PROJECT_ID`, and `IBM_WATSONX_URL` for live IBM Granite model access).*

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Unit Tests**:
   ```bash
   pytest
   ```

5. **Launch Application**:
   ```bash
   streamlit run dashboard/app.py
   ```

---

## 🐳 Dockerization & Cloud Run Deployment

1. **Build Container Image**:
   ```bash
   docker build -t ecomind-ai .
   ```

2. **Run Container Locally**:
   ```bash
   docker run -d -p 8080:8080 -e PORT=8080 ecomind-ai
   ```
   Access the dashboard at `http://localhost:8080`.

3. **Deploy to Google Cloud Run**:
   ```bash
   # Tag image for Google Artifact Registry
   gcloud auth configure-docker
   docker tag ecomind-ai gcr.io/[PROJECT-ID]/ecomind-ai:latest
   docker push gcr.io/[PROJECT-ID]/ecomind-ai:latest

   # Deploy container
   gcloud run deploy ecomind-ai \
     --image gcr.io/[PROJECT-ID]/ecomind-ai:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8080 \
     --memory 2Gi \
     --cpu 1
   ```

---

## 📄 License & Attribution

Submitted as part of the 1M1B / IBM SkillsBuild & AICTE Virtual Internship. Built using IBM Granite foundation model abstractions and open-source machine learning frameworks.
