import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gacha import gacha_draw


def test_performance():
    print("\n[性能テスト] 処理速度")
    try:
        start = time.time()
        for _ in range(100000):
            gacha_draw()
        elapsed = time.time() - start
        # 100,000回で2秒以内を目安
        assert elapsed < 2.0
        print("[テスト成功] 処理速度は問題ありません")
    except: 
        print("[テスト失敗] 処理速度は問題あります")
        raise
    
