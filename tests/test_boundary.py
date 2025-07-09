import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings import gacha_probs

def test_probabilities_are_int():
    print("\n[境界値テスト] 確率値が整数かどうか")
    try:
        for v in gacha_probs.values():
            assert isinstance(v, int)
        print("[テスト成功] 確率値がすべて整数です")
    except AssertionError:
        print("[テスト失敗] 整数でない確率値があります")
        raise

def test_probabilities_in_range():
    print("[境界値テスト] 確率値が0より大きく100未満か")
    try:
        for v in gacha_probs.values():
            assert 0 < v < 100
        print("[テスト成功] すべての確率値が0より大きく100未満です")
    except AssertionError:
        print("[テスト失敗] 範囲外の確率値があります")
        raise
