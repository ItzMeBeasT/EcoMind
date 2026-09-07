"""
Multimodal Document Intelligence module for EcoMind AI.
Extracts text from uploaded sustainability policies, energy reports, and documents,
and analyzes findings, recommendations, and campus relevance.
"""

from typing import Any
from src.ai import get_ai_provider

def analyze_sustainability_document(document_name: str, document_text: str) -> dict[str, Any]:
    """
    Process and analyze uploaded sustainability document text.
    """
    provider = get_ai_provider()
    return provider.analyze_document(document_name, document_text)
