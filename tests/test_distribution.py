import pytest
from gacha import gacha_draw
from settings import gacha_probs
from collections import Counter

def test_all_items_appear():
    results = set()
    for _ in range(10000):
        results.add(gacha_draw())
    assert set(gacha_probs.keys()) == results

def test_distribution():
    N = 100000
    results = [gacha_draw() for _ in range(N)]
    counter = Counter(results)
    for item, prob in gacha_probs.items():
        observed = counter[item] / N * 100
        # 許容誤差±1.5%
        assert abs(observed - prob) < 1.5
