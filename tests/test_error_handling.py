import pytest
from gacha import gacha_draw

def test_return_type():
    result = gacha_draw()
    assert isinstance(result, str)
    assert len(result) == 1

def test_only_valid_items():
    valid = {"A", "B", "C", "D"}
    for _ in range(10000):
        assert gacha_draw() in valid
