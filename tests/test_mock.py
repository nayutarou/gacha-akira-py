import sys
import os
import pytest
import random

# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import gacha


class TestMocking:
    """モックテスト"""

    @pytest.mark.parametrize(
        "mock_probs,majority_key,desc",
        [
            ({"A": 97, "B": 1, "C": 1, "D": 1}, "A", "Aが圧倒的に多い場合"),
            ({"A": 1, "B": 97, "C": 1, "D": 1}, "B", "Bが圧倒的に多い場合"),
            ({"A": 1, "B": 1, "C": 97, "D": 1}, "C", "Cが圧倒的に多い場合"),
            ({"A": 1, "B": 1, "C": 1, "D": 97}, "D", "Dが圧倒的に多い場合"),
        ],
    )
    def test_mocked_probability_all_patterns(
        self, monkeypatch, mock_probs, majority_key, desc
    ):
        """gacha_probsをモックして、設定された確率分布が反映されることをテスト"""
        print(f"\n[モックテスト] {desc}")
        monkeypatch.setattr(gacha, "gacha_probs", mock_probs)

        # 全てのアイテムが出現することを確認
        results = set(gacha.gacha_draw() for _ in range(1000))
        assert results == set(
            mock_probs.keys()
        ), f"モックされた確率で全てのアイテム({set(mock_probs.keys())})が出現しませんでした: {results}"

        # 多数派のアイテムが期待通りに出現することを確認
        counts = {k: 0 for k in mock_probs}
        num_trials = 10000
        for _ in range(num_trials):
            counts[gacha.gacha_draw()] += 1

        # 多数派のアイテムが90%以上出現することを確認
        expected_majority_count = num_trials * (mock_probs[majority_key] / 100)
        # 許容誤差を考慮
        assert counts[majority_key] > (
            expected_majority_count * 0.9
        ), f"多数派のアイテム'{majority_key}'の出現回数({counts[majority_key]})が期待値({expected_majority_count})の90%を下回りました"
        print(
            f"[テスト成功] {majority_key}が期待通りに多数出現しました (出現回数: {counts[majority_key]}) "
        )

    def test_mock_random_choices(self, monkeypatch):
        """random.choicesをモックして、特定のアイテムが返されることをテスト"""
        print("\n[モックテスト] random.choicesのモック")
        expected_item = "S"

        # random.choicesが常にexpected_itemを返すようにモック
        def mock_choices(population, weights=None, k=1):
            return [expected_item]

        monkeypatch.setattr(random, "choices", mock_choices)

        result = gacha.gacha_draw()
        assert (
            result == expected_item
        ), f"モックされたrandom.choicesが期待値'{expected_item}'を返しませんでした: {result}"
        print(
            f"[テスト成功] random.choicesが正しくモックされ、'{expected_item}'が返されました"
        )
