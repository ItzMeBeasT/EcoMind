"""
Unit tests for EcoMind AI Agent module.
"""

import pytest
import pandas as pd
from src.data_processing import load_data
from src.agent import EcoMindAgent

def test_agent_queries():
    df = load_data("data/energy_data.csv")
    agent = EcoMindAgent(df)

    res1 = agent.query("Which building consumes the most energy?")
    assert "answer" in res1
    assert "highest_consuming_building" in res1["intent"]

    res2 = agent.query("What are today's major anomalies?")
    assert "answer" in res2

    res3 = agent.query("What can we do to reduce energy waste?")
    assert "answer" in res3
    assert "REC-" in res3["answer"] or "Recommendations" in res3["answer"]

    res4 = agent.query("Explain the current energy situation simply.")
    assert "answer" in res4
