# アプリケーション全体の設定を定義するモジュール
from typing import Dict

# ガチャの排出確率を定義
gacha_probs: Dict[str, int] = {"A": 5, "B": 10, "C": 20, "D": 65}
# APIサーバーのポート番号
API_PORT: int = 8000
