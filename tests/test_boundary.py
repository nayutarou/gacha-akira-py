import pytest
from gacha import gacha_draw
from settings import gacha_probs


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

    def test_no_items(self, original_gacha_probs):
        """アイテムが1つもない場合にエラーを発生させることをテスト"""
        print("[境界値テスト] アイテムが空の場合")
        gacha_probs.clear()
        with pytest.raises(ValueError):
            gacha_draw()
        print("[テスト成功] アイテムが空の場合にValueErrorが発生しました")

    def test_single_item(self, original_gacha_probs):
        """アイテムが1つだけの場合にそのアイテムを返すことをテスト"""
        print("[境界値テスト] アイテムが1つの場合")
        gacha_probs.clear()
        gacha_probs["A"] = 100
        assert gacha_draw() == "A"
        print("[テスト成功] アイテムが1つの場合に正しく排出されました")

    def test_zero_probability_item(self, original_gacha_probs):
        """確率が0のアイテムが排出されないことをテスト"""
        print("[境界値テスト] 確率0のアイテムが排出されないか")
        gacha_probs.clear()
        gacha_probs["A"] = 100
        gacha_probs["B"] = 0
        for _ in range(100):
            assert gacha_draw() == "A"
        print("[テスト成功] 確率0のアイテムは排出されませんでした")

    def test_total_probability_over_100(self, original_gacha_probs):
        """確率の合計値が100を超える場合にエラーを発生させることをテスト"""
        print("[境界値テスト] 確率の合計値が100を超える場合")
        gacha_probs["E"] = 10
        with pytest.raises(ValueError):
            gacha_draw()
        print("[テスト成功] 確率の合計値が100を超える場合にValueErrorが発生しました")

    def test_total_probability_under_100(self, original_gacha_probs):
        """確率の合計値が100未満の場合にエラーを発生させることをテスト"""
        print("[境界値テスト] 確率の合計値が100未満の場合")
        gacha_probs["A"] = 50
        with pytest.raises(ValueError):
            gacha_draw()
        print("[テスト成功] 確率の合計値が100未満の場合にValueErrorが発生しました")
