
import sys
import os
from fastapi.testclient import TestClient

# プロジェクトのルートディレクトリをsys.pathに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server import app
from settings import gacha_probs

client = TestClient(app)


def test_read_main():
    """ルートエンドポイントのテスト"""
    print("\n[APIテスト] GET /")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Gacha World!"}
    print("[テスト成功] ルートエンドポイントが正常にレスポンスを返しました")


def test_gacha_endpoint():
    """ガチャエンドポイントのテスト"""
    print("\n[APIテスト] GET /gacha")
    response = client.get("/gacha")
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], str)
    assert len(data["result"]) == 1
    assert data["result"] in gacha_probs.keys()
    print("[テスト成功] ガチャエンドポイントが正常なレスポンスを返しました")
