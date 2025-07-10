import sys
import os
import pytest

# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from settings import gacha_probs


@pytest.fixture
def probs():
    """ガチャの確率設定をフィクスチャとして提供"""
    return gacha_probs


class TestBoundary:
    """境界値テスト"""

    def test_probabilities_are_int(self, probs):
        """確率設定の値が整数であることをテスト"""
        print("\n[境界値テスト] 確率値が整数かどうか")
        for item, prob in probs.items():
            assert isinstance(
                prob, int
            ), f"アイテム'{item}'の確率({prob})が整数ではありません"
        print("[テスト成功] 確率値がすべて整数です")

    def test_probabilities_in_range(self, probs):
        """確率設定の値が0より大きく100未満であることをテスト"""
        print("[境界値テスト] 確率値が0より大きく100未満か")
        for item, prob in probs.items():
            assert (
                0 < prob < 100
            ), f"アイテム'{item}'の確率({prob})が0から100の範囲外です"
        print("[テスト成功] すべての確率値が0より大きく100未満です")

    def test_total_probability_is_100(self, probs):
        """確率の合計値が100であることをテスト"""
        print("[境界値テスト] 確率の合計値が100であるか")
        total_prob = sum(probs.values())
        assert total_prob == 100, f"確率の合計値({total_prob})が100ではありません"
        print("[テスト成功] 確率の合計値が100です")
