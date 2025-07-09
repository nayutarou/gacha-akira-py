import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gacha import gacha_draw
from settings import gacha_probs
from collections import Counter


def test_all_items_appear():
    print("\n[分布テスト] すべてのアイテムが出現する")
    results = set()
    try:
        for _ in range(10000):
            results.add(gacha_draw())
        assert set(gacha_probs.keys()) == results
        print("[テスト成功] すべてのアイテムが出現します")
    except AssertionError:
        print("[テスト失敗] すべてのアイテムが出現しません")
        raise


def test_distribution():
    print("\n[分布テスト] 確率分布が正しい")
    N = 100000
    results = [gacha_draw() for _ in range(N)]
    counter = Counter(results)
    try :
        for item, prob in gacha_probs.items():
            observed = counter[item] / N * 100
            # 許容誤差±1.5%
            assert abs(observed - prob) < 1.5
            print("[テスト成功] 確率分布が正しく出現します")
    except AssertionError:
        print("[テスト失敗] 確率分布が正しく出現しません")
        raise
        
