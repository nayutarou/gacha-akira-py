import sys
import os
import pytest
from collections import Counter
import random

# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gacha import gacha_draw
from settings import gacha_probs


@pytest.fixture
def probs():
    """ガチャの確率設定をフィクスチャとして提供"""
    return gacha_probs


class TestDistribution:
    """分布テスト"""

    def test_all_items_appear(self, probs):
        """すべてのアイテムが十分な試行回数で出現することを確認"""
        print("\n[分布テスト] すべてのアイテムが出現する")
        results = set()
        # 試行回数を増やして、全てのアイテムが出現する確率を高める
        num_trials = 100000
        for _ in range(num_trials):
            results.add(gacha_draw())
        expected_items = set(probs.keys())
        assert (
            expected_items == results
        ), f"期待されるアイテム({expected_items})と実際に出現したアイテム({results})が異なります"
        print(
            f"[テスト成功] {num_trials}回の試行で全てのアイテム({expected_items})が出現しました"
        )

    def test_distribution_accuracy(self, probs):
        """ガチャの確率分布が設定値に近いことを統計的にテスト"""
        print("\n[分布テスト] 確率分布が正しい")
        N = 100000  # 試行回数
        results = [gacha_draw() for _ in range(N)]
        counter = Counter(results)

        print(f"  試行回数: {N}")
        for item, prob in probs.items():
            observed_percentage = (counter[item] / N) * 100
            # 許容誤差を±1.5%に設定
            tolerance = 1.5
            assert (
                abs(observed_percentage - prob) < tolerance
            ), f"アイテム'{item}': 期待値 {prob:.2f}%, 観測値 {observed_percentage:.2f}% (許容誤差±{tolerance}%) "
            print(
                f"  アイテム'{item}': 期待値 {prob:.2f}%, 観測値 {observed_percentage:.2f}% (許容誤差±{tolerance}%) -> OK"
            )
        print("[テスト成功] 確率分布が設定値に統計的に近いことを確認しました")

    def test_distribution_reproducibility(self, probs):
        """乱数シードを固定した際のガチャ結果の再現性をテスト"""
        print("\n[分布テスト] 乱数シード固定時の再現性")
        seed_value = 42
        num_draws = 100

        # 1回目の試行
        random.seed(seed_value)
        results1 = [gacha_draw() for _ in range(num_draws)]

        # 2回目の試行
        random.seed(seed_value)
        results2 = [gacha_draw() for _ in range(num_draws)]

        assert results1 == results2, "乱数シードを固定しても結果が再現されません"
        print(
            f"[テスト成功] 乱数シード({seed_value})を固定した際に、{num_draws}回のガチャ結果が再現されました"
        )
