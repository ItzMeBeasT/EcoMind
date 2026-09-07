# EcoMind AI — 3–5 Minute Presentation & Demo Script

**Project Title**: EcoMind AI: An AI-Powered Campus Energy Optimization and Sustainability Agent  
**Presenter**: [YOUR NAME] ([YOUR COLLEGE NAME])  
**Target Duration**: 4 Minutes  

---

## Presentation Script & Stage Directions

### 0:00 – 0:35 | Step 1 & 2: Introduction & Problem Statement
**[Action: Display Title Slide / Dashboard Header]**  
> "Hello judges and audience. My name is **[YOUR NAME]** from **[YOUR COLLEGE NAME]**. Today, I am excited to present **EcoMind AI**, an AI-powered campus energy optimization and sustainability agent developed for the 1M1B AI for Sustainability Virtual Internship in collaboration with IBM SkillsBuild and AICTE.
>
> Educational campuses consume vast amounts of electricity across classrooms, computer labs, libraries, and hostels. However, administrators lack real-time visibility into energy waste, unusual consumption spikes, and peak demand patterns. EcoMind AI solves this by combining machine learning regression, unsupervised anomaly detection, explainable insights, and a grounded conversational AI assistant."

---

### 0:35 – 1:15 | Step 3, 4 & 5: Dashboard Overview & Analytics
**[Action: Switch to Dashboard Overview Tab]**  
> "Here is the EcoMind AI Streamlit Dashboard. At a glance, administrators can see key top-level metrics: total energy consumption, average hourly load, highest-consuming facility, and active anomalies flagged.
>
> Scrolling down, our interactive line chart displays real-time energy consumption trends across campus buildings. Looking at the building comparison chart, we immediately identify that the **Computer Lab** accounts for the largest share of total energy usage. The 24-hour demand profile shows clear consumption peaks during afternoon hours between 14:00 and 16:00."

---

### 1:15 – 1:55 | Step 6: Anomaly Detection Center
**[Action: Switch to Anomaly Center Tab & Select Demo Scenario 3 or 4]**  
> "Next, let's explore our **Anomaly Detection Center**. Using an `IsolationForest` model, EcoMind AI automatically scans multivariate features—including temperature, occupancy, AC units, and device counts—to catch irregular patterns.
>
> For example, in **Scenario 4**, the system flags an anomaly where energy usage remains high during off-hours despite near-zero building occupancy. The insight engine explains this using clear advisory language, identifying idle equipment and un-isolated baseload as possible contributing factors."

---

### 1:55 – 2:35 | Step 7 & 8: ML Forecaster & Recommendations
**[Action: Switch to ML Energy Forecaster Tab, enter inputs, then switch to Recommendations Tab]**  
> "Moving to the **ML Energy Forecaster**, we use a `RandomForestRegressor` trained with chronological split validation (achieving an R² score of 0.935). Facility managers can input custom outdoor temperatures or occupancy levels to predict future energy demand accurately.
>
> Based on these findings, our **Recommendation Engine** delivers non-destructive, actionable advisories—such as setting standardized HVAC thermostat setpoints to 24°C–26°C and scheduling automated nighttime standby shutdowns."

---

### 2:35 – 3:15 | Step 9: Ask EcoMind Conversational Agent
**[Action: Switch to Ask EcoMind Agent Tab and click 'Which building consumes the most energy?']**  
> "To make insights accessible to non-technical staff, we built **Ask EcoMind**, a conversational AI assistant. Crucially, our architecture decouples data analytics calculations from language generation. When I ask, *'Which building consumes the most energy?'*, the agent retrieves verified pandas outputs first, ensuring the answer is 100% grounded without numerical hallucinations."

---

### 3:15 – 4:00 | Step 10, 11 & 12: Responsible AI, Impact & Closing
**[Action: Show Responsible AI Panel & Estimated Impact Calculator]**  
> "Under **Responsible AI Principles**, our smart meter data contains zero PII, recommendations are purely advisory for human oversight, and all data is explicitly labeled as synthetic demo data. Under a hypothetical 5% reduction scenario, EcoMind AI projects over 6 tons of avoided CO2 emissions.
>
> In conclusion, EcoMind AI advances **SDG 7: Affordable and Clean Energy** by turning raw institutional data into intelligent, actionable sustainability decisions. Thank you!"
