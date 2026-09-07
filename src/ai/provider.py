"""
Abstract AI Provider interface for EcoMind AI.
Supports IBM Granite via watsonx.ai as well as local demo fallback mode.
"""

from abc import ABC, abstractmethod
from typing import Optional, Any

class BaseAIProvider(ABC):
    @abstractmethod
    def is_live_integration(self) -> bool:
        """Return True if connected to live IBM watsonx.ai API, False if operating in Demo/Local mode."""
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """Return human-readable provider name (e.g. 'IBM Granite (watsonx.ai)' or 'EcoMind Local Demo Provider')."""
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Return model identifier (e.g. 'ibm/granite-13b-chat-v2' or 'Deterministic Local Engine')."""
        pass

    @abstractmethod
    def generate_text(self, prompt: str, role: str = "Sustainability Analyst", temperature: float = 0.2) -> str:
        """Generate text response using specified role prompt."""
        pass

    @abstractmethod
    def explain_anomaly(self, building: str, energy_kwh: float, baseline_avg: float, factors: list[str]) -> str:
        """Generate an explainable advisory explanation for a detected anomaly."""
        pass

    @abstractmethod
    def generate_executive_brief(self, summary_metrics: dict, top_bld: dict, recs: list[dict]) -> str:
        """Generate executive sustainability briefing report."""
        pass

    @abstractmethod
    def analyze_document(self, document_name: str, document_text: str) -> dict[str, Any]:
        """Extract key sustainability findings, energy recommendations, and campus relevance from uploaded document."""
        pass
