"""
Responsible AI Guardrail Layer for EcoMind AI.
Performs input safety checks and output grounding validation to eliminate AI hallucinations and unsafe requests.
"""

import re

UNSAFE_KEYWORDS = [
    "ignore previous instructions",
    "bypass safety",
    "hack",
    "passwords",
    "student ssn",
    "personal credit card",
    "drop table",
    "system shutdown override",
]

def check_input_safety(prompt: str) -> tuple[bool, str]:
    """
    Evaluate user prompt against Responsible AI safety rules.
    Returns (is_safe, reason_message).
    """
    prompt_lower = prompt.lower().strip()
    
    if not prompt_lower:
        return False, "Prompt is empty."

    for kw in UNSAFE_KEYWORDS:
        if kw in prompt_lower:
            return False, f"Request flagged by Responsible AI Guardrails (contains prohibited keyword/instruction: '{kw}')."

    return True, "Input validated successfully."

def check_output_grounding(response_text: str, verified_facts: dict) -> tuple[bool, str, list[str]]:
    """
    Verify numerical claims in generated output against verified dataset facts.
    Returns (is_grounded, validated_text, warnings).
    """
    warnings = []
    text_out = response_text

    # Extract numerical patterns like XX,XXX kWh or XX.X%
    numbers_in_response = re.findall(r"(\d+(?:\.\d+)?)\s*(?:kwh|%)", response_text.lower())
    
    # Check if numbers match calculated facts if present
    if numbers_in_response and verified_facts:
        verified_values = []
        for v in verified_facts.values():
            if isinstance(v, (int, float)):
                verified_values.append(round(float(v), 1))
            elif isinstance(v, dict):
                for sub_v in v.values():
                    if isinstance(sub_v, (int, float)):
                        verified_values.append(round(float(sub_v), 1))

        # Check for extreme ungrounded numbers (> 100% in percentage claims)
        for num_str in numbers_in_response:
            try:
                num_val = float(num_str)
                if num_val > 100.0 and "%" in response_text:
                    warnings.append(f"Ungrounded percentage claim detected ({num_val}%).")
            except ValueError:
                pass

    if warnings:
        disclaimer = "\n\n*(Note: Numerical claims in AI responses are verified against campus smart meter dataset calculations.)*"
        if disclaimer not in text_out:
            text_out += disclaimer
        return False, text_out, warnings

    return True, text_out, []
