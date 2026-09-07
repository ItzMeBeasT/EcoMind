"""
IBM Granite AI Provider for EcoMind AI via IBM watsonx.ai REST APIs.
Supports live Granite foundation models (e.g. ibm/granite-13b-chat-v2) with automatic fallback to LocalDemoAIProvider.
"""

import os
import requests
from typing import Optional, Any
from src.ai.provider import BaseAIProvider
from src.ai.fallback import LocalDemoAIProvider

class IBMGraniteProvider(BaseAIProvider):
    def __init__(self):
        self.url = os.environ.get("IBM_WATSONX_URL", "https://us-south.ml.cloud.ibm.com").strip()
        self.api_key = os.environ.get("IBM_WATSONX_API_KEY", "").strip()
        self.project_id = os.environ.get("IBM_WATSONX_PROJECT_ID", "").strip()
        self.model_id = os.environ.get("IBM_GRANITE_MODEL", "ibm/granite-13b-chat-v2").strip()
        
        self.fallback_provider = LocalDemoAIProvider()
        self._iam_token: Optional[str] = None

    def is_live_integration(self) -> bool:
        """Returns True only if all required IBM watsonx credentials are set."""
        return bool(self.api_key and self.project_id)

    def get_provider_name(self) -> str:
        if self.is_live_integration():
            return "IBM Granite (watsonx.ai)"
        return self.fallback_provider.get_provider_name()

    def get_model_name(self) -> str:
        if self.is_live_integration():
            return self.model_id
        return self.fallback_provider.get_model_name()

    def _get_iam_token(self) -> Optional[str]:
        if self._iam_token:
            return self._iam_token
        if not self.api_key:
            return None
        
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={self.api_key}"
            resp = requests.post("https://iam.cloud.ibm.com/identity/token", headers=headers, data=data, timeout=5)
            if resp.status_code == 200:
                self._iam_token = resp.json().get("access_token")
                return self._iam_token
        except Exception:
            pass
        return None

    def generate_text(self, prompt: str, role: str = "Sustainability Analyst", temperature: float = 0.2) -> str:
        if not self.is_live_integration():
            return self.fallback_provider.generate_text(prompt, role, temperature)

        token = self._get_iam_token()
        if not token:
            return self.fallback_provider.generate_text(prompt, role, temperature)

        try:
            endpoint = f"{self.url.rstrip('/')}/ml/v1/text/generation?version=2023-05-29"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            system_instruction = f"You are EcoMind AI, an expert {role} specializing in campus energy sustainability and SDG 7 alignment. Ground all answers strictly in verified factual data."
            
            payload = {
                "input": f"{system_instruction}\n\nUser Question:\n{prompt}\n\nResponse:",
                "parameters": {
                    "decoding_method": "greedy" if temperature == 0 else "sample",
                    "temperature": temperature,
                    "max_new_tokens": 512,
                    "repetition_penalty": 1.1,
                },
                "model_id": self.model_id,
                "project_id": self.project_id,
            }

            resp = requests.post(endpoint, headers=headers, json=payload, timeout=10)
            if resp.status_code == 200:
                results = resp.json().get("results", [])
                if results:
                    return results[0].get("generated_text", "").strip()
        except Exception:
            pass

        return self.fallback_provider.generate_text(prompt, role, temperature)

    def explain_anomaly(self, building: str, energy_kwh: float, baseline_avg: float, factors: list[str]) -> str:
        if not self.is_live_integration():
            return self.fallback_provider.explain_anomaly(building, energy_kwh, baseline_avg, factors)
        
        prompt = f"Explain an anomaly in {building}: Recorded {energy_kwh:.2f} kWh vs baseline average {baseline_avg:.1f} kWh. Factors: {', '.join(factors)}."
        return self.generate_text(prompt, role="Insight Explainer")

    def generate_executive_brief(self, summary_metrics: dict, top_bld: dict, recs: list[dict]) -> str:
        if not self.is_live_integration():
            return self.fallback_provider.generate_executive_brief(summary_metrics, top_bld, recs)
        
        prompt = f"Generate an executive briefing report for campus energy: Total energy {summary_metrics.get('total_energy_kwh', 0):,.0f} kWh, Top consumer {top_bld.get('building', 'Hostel A')}."
        return self.generate_text(prompt, role="Report Generator")

    def analyze_document(self, document_name: str, document_text: str) -> dict[str, Any]:
        return self.fallback_provider.analyze_document(document_name, document_text)
