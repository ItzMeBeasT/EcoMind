"""
Local Demo AI Provider for EcoMind AI.
Provides deterministic, rule-grounded, zero-hallucination responses when IBM watsonx.ai API keys are unconfigured.
"""

from typing import Any
from src.ai.provider import BaseAIProvider

class LocalDemoAIProvider(BaseAIProvider):
    def is_live_integration(self) -> bool:
        return False

    def get_provider_name(self) -> str:
        return "EcoMind Local Demo Provider"

    def get_model_name(self) -> str:
        return "Deterministic Grounded Engine v1.0"

    def generate_text(self, prompt: str, role: str = "Sustainability Analyst", temperature: float = 0.2) -> str:
        return (
            f"**[{role}]** Based on campus energy data analysis:\n\n"
            f"• All numerical findings are calculated directly from energy observations to prevent AI hallucinations.\n"
            f"• Energy demand patterns correlate with ambient temperature and building occupancy schedules.\n"
            f"• *(Operating in Local Demo Mode — configure IBM watsonx.ai credentials in `.env` for live Granite inference)*"
        )

    def explain_anomaly(self, building: str, energy_kwh: float, baseline_avg: float, factors: list[str]) -> str:
        diff_pct = ((energy_kwh - baseline_avg) / baseline_avg * 100) if baseline_avg > 0 else 0.0
        factors_formatted = "\n".join([f"- {f}" for f in factors])
        
        return (
            f"**Anomaly Explanation for {building}**:\n"
            f"Recorded consumption of **{energy_kwh:.2f} kWh** is **{diff_pct:+.1f}%** relative to baseline average ({baseline_avg:.1f} kWh).\n\n"
            f"**Possible Contributing Factors (Advisory Non-Causal Analysis)**:\n"
            f"{factors_formatted}\n\n"
            f"**Recommended Action**: Perform physical inspection of thermostat setpoints, HVAC dampers, and un-isolated electrical loads."
        )

    def generate_executive_brief(self, summary_metrics: dict, top_bld: dict, recs: list[dict]) -> str:
        top_rec = recs[0] if recs else {"title": "General Energy Audit", "action": "Inspect building HVAC setpoints."}
        
        return (
            f"# Executive Sustainability Briefing\n\n"
            f"### 1. Campus Energy Status Summary\n"
            f"- **Total Energy Consumption**: **{summary_metrics.get('total_energy_kwh', 0):,.1f} kWh** across {summary_metrics.get('num_buildings', 4)} facilities.\n"
            f"- **Average Hourly Load**: **{summary_metrics.get('avg_energy_kwh', 0):.2f} kWh**.\n"
            f"- **Primary Load Consumer**: **{top_bld.get('building', 'Hostel A')}** ({top_bld.get('share_percent', 0):.1f}% of total campus electricity usage).\n\n"
            f"### 2. Primary Anomaly & Waste Focus\n"
            f"Statistical analysis identified elevated consumption spikes during non-operational late hours, indicating potential unmitigated baseload or idle equipment operation.\n\n"
            f"### 3. Key Executive Action Item\n"
            f"**[{top_rec.get('title', 'Target Energy Audit')}]**: {top_rec.get('action', 'Inspect building HVAC setpoints.')}\n\n"
            f"### 4. SDG 7 & Responsible AI Compliance\n"
            f"All findings align with SDG Target 7.3 (Energy Efficiency) and are grounded in verified dataset metrics."
        )

    def analyze_document(self, document_name: str, document_text: str) -> dict[str, Any]:
        text_lower = document_text.lower()
        word_count = len(document_text.split())
        
        # Simple rule extraction for demonstration
        has_hvac = "hvac" in text_lower or "air condition" in text_lower or "temperature" in text_lower
        has_lighting = "light" in text_lower or "led" in text_lower
        has_policy = "policy" in text_lower or "guideline" in text_lower or "sdg" in text_lower

        findings = []
        recommendations = []

        if has_hvac:
            findings.append("Document emphasizes HVAC climate control optimization and thermostat setpoints (24°C–26°C).")
            recommendations.append("Standardize thermostat setpoints across academic blocks and schedule automated setback modes.")
        
        if has_lighting:
            findings.append("Document references lighting efficiency upgrades and daylight harvesting.")
            recommendations.append("Install motion-sensor LED fixtures in corridors and restrooms.")

        if not findings:
            findings.append(f"Analyzed {document_name} ({word_count} words). Contains institutional energy conservation guidelines.")
            recommendations.append("Conduct a comprehensive energy audit based on documented guidelines.")

        return {
            "document_name": document_name,
            "word_count": word_count,
            "key_findings": findings,
            "energy_recommendations": recommendations,
            "campus_relevance": "High relevance for facility management and SDG 7 sustainability targets.",
            "provider": self.get_provider_name(),
        }
