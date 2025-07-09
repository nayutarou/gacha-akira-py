import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gacha

def test_mocked_probability(monkeypatch):
    mock_probs = {"A": 1, "B": 1, "C": 1, "D": 97}
    monkeypatch.setattr(gacha, "gacha_probs", mock_probs)
    results = set(gacha.gacha_draw() for _ in range(1000))
    assert results == set(mock_probs.keys())
    # Dが圧倒的に多い
    counts = {k: 0 for k in mock_probs}
    for _ in range(10000):
        counts[gacha.gacha_draw()] += 1
    assert counts["D"] > 9000
