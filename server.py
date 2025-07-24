# FastAPIライブラリをインポート
from fastapi import FastAPI

# gacha.pyからgacha_draw関数をインポート
from gacha import gacha_draw

# FastAPIのCORSミドルウェアをインポート
from fastapi.middleware.cors import CORSMiddleware

# FastAPIインスタンスを作成
app = FastAPI()

# CORSミドルウェアを追加
# これにより、異なるオリジンからのリクエストを許可します
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"] は全てのオリジンからのリクエストを許可します。
    # 本番環境では、特定のオリジン（例: ["http://localhost:5173"]）に制限することが推奨されます。
    allow_origins=["*"],
    # allow_credentials=True はクッキーなどの資格情報を含むリクエストを許可します。
    allow_credentials=True,
    # allow_methods=["*"] は全てのHTTPメソッド（GET, POSTなど）を許可します。
    allow_methods=["*"],
    # allow_headers=["*"] は全てのリクエストヘッダーを許可します。
    allow_headers=["*"],
)


# "/"エンドポイント（GETリクエスト）
@app.get("/")
def read_root():
    return {"message": "Welcome to Gacha World!"}





# "/gacha"エンドポイント（GETリクエスト）
@app.get("/gacha")
def get_gacha():
    # gacha_draw関数を呼び出してガチャの結果を取得
    result = gacha_draw()
    # 結果をJSON形式で返す
    return {"result": result}


# このファイルが直接実行された場合にのみ以下のコードを実行
if __name__ == "__main__":
    import uvicorn

    port = 8000
    print(f"[INFO] APIサーバーを起動します。使用ポート: {port}")
    # uvicornサーバーを起動
    # host="0.0.0.0" は全てのネットワークインターフェースでリッスンします
    # reload=True はコードが変更されたときにサーバーを自動的に再起動します
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
