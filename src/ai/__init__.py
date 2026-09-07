"""
EcoMind AI Abstraction Module.
Supports IBM Granite via watsonx.ai REST API with automatic Local Demo fallback.
"""

from src.ai.provider import BaseAIProvider
from src.ai.granite import IBMGraniteProvider
from src.ai.fallback import LocalDemoAIProvider
from src.ai.guardrails import check_input_safety, check_output_grounding
from src.ai.factsheet import get_ecomind_factsheet
from src.ai.evaluation import get_ai_evaluation_report

def get_ai_provider() -> BaseAIProvider:
    """
    Factory function: returns IBMGraniteProvider if watsonx.ai credentials are set,
    otherwise returns LocalDemoAIProvider.
    """
    granite_provider = IBMGraniteProvider()
    if granite_provider.is_live_integration():
        return granite_provider
    return LocalDemoAIProvider()
