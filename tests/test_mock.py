import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import gacha



@pytest.mark.parametrize("mock_probs,majority_key,desc", [
    ({"A": 97, "B": 1, "C": 1, "D": 1}, "A", "Aが圧倒的に多い場合"),
    ({"A": 1, "B": 97, "C": 1, "D": 1}, "B", "Bが圧倒的に多い場合"),
    ({"A": 1, "B": 1, "C": 97, "D": 1}, "C", "Cが圧倒的に多い場合"),
    ({"A": 1, "B": 1, "C": 1, "D": 97}, "D", "Dが圧倒的に多い場合"),
])
def test_mocked_probability_all_patterns(monkeypatch, mock_probs, majority_key, desc):
    print(f"\n[モックテスト] {desc}")
    try:
        monkeypatch.setattr(gacha, "gacha_probs", mock_probs)
        results = set(gacha.gacha_draw() for _ in range(1000))
        assert results == set(mock_probs.keys())
        counts = {k: 0 for k in mock_probs}
        for _ in range(10000):
            counts[gacha.gacha_draw()] += 1
        assert counts[majority_key] > 9000
        print(f"[テスト成功] {majority_key}が9000回以上出現")
    except AssertionError:
        print(f"[テスト失敗] {majority_key}が9000回以上出現しませんでした")
        raise
    
