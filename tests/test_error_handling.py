import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gacha import gacha_draw


def test_return_type():
    print("\n[エラーテスト] 返り値の型")
    try:
        result = gacha_draw()
        assert isinstance(result, str)
        assert len(result) == 1
        print("[テスト成功] 返り値の型が正しく出現します")
    except AssertionError:
        print("[テスト失敗] 返り値の型が正しく出現しません")
        raise
    


def test_only_valid_items():
    print("\n[エラーテスト] 有効なアイテムしか出ない")
    try:        
        valid = {"A", "B", "C", "D"}
        for _ in range(10000):
            assert gacha_draw() in valid
        print("[テスト成功] 有効なアイテムしか出ない")
    except:
        print("[テスト失敗] 有効なアイテムしか出ない")
        raise
