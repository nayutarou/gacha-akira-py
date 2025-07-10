import sys
import os
import time
import pytest

# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gacha import gacha_draw


class TestPerformance:
    """性能テスト"""

    @pytest.mark.parametrize(
        "num_draws, max_time_sec",
        [
            (10000, 0.1),  # 1万回で0.1秒以内
            (100000, 1.0),  # 10万回で1.0秒以内
            (1000000, 10.0),  # 100万回で10.0秒以内
        ],
    )
    def test_gacha_draw_performance(self, num_draws, max_time_sec):
        """gacha_draw関数の性能をテスト"""
        print(
            f"\n[性能テスト] {num_draws}回のガチャ処理速度 (目標: {max_time_sec}秒以内)"
        )
        start_time = time.time()
        for _ in range(num_draws):
            gacha_draw()
        elapsed_time = time.time() - start_time

        assert (
            elapsed_time < max_time_sec
        ), f"{num_draws}回のガチャ処理が遅すぎます: {elapsed_time:.4f}秒 (目標: {max_time_sec:.4f}秒)"
        print(
            f"[テスト成功] {num_draws}回のガチャ処理が{elapsed_time:.4f}秒で完了しました (目標: {max_time_sec:.4f}秒以内)"
        )
