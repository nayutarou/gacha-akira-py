import pytest

from gacha import gacha_draw
from settings import gacha_probs


class TestErrorHandling:
    """エラーハンドリングテスト"""

    def test_return_type(self):
        """gacha_drawの返り値が文字列であることをテスト"""
        print("\n[エラーテスト] 返り値の型")
        result = gacha_draw()
        assert isinstance(
            result, str
        ), f"返り値の型が文字列ではありません: {type(result)}"
        assert len(result) == 1, f"返り値の長さが1ではありません: {len(result)}"
        print("[テスト成功] 返り値の型が正しく、長さが1です")

    def test_only_valid_items(self):
        """gacha_drawがsettings.pyで定義された有効なアイテムのみを返すことをテスト"""
        print("\n[エラーテスト] 有効なアイテムしか出ない")
        valid_items = set(gacha_probs.keys())
        num_trials = 10000
        for _ in range(num_trials):
            result = gacha_draw()
            assert result in valid_items, f"無効なアイテム'{result}'が出現しました"
        print(f"[テスト成功] {num_trials}回の試行で有効なアイテムのみが出現しました")

    def test_empty_gacha_probs(self, original_gacha_probs):
        """gacha_probsが空の場合にエラーが発生することを確認"""
        print("\n[エラーテスト] gacha_probsが空の場合")
        gacha_probs.clear()  # gacha_probsを空にする
        with pytest.raises(ValueError) as excinfo:
            gacha_draw()
        assert "Total probability must be 100" in str(excinfo.value)
        print("[テスト成功] gacha_probsが空の場合に正しくValueErrorが発生しました")
