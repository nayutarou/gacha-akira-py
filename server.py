
from fastapi import FastAPI
from gacha import gacha_draw

app = FastAPI()


@app.get("/gacha")
def get_gacha():
    result = gacha_draw()
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    port = 8000
    print(f"[INFO] APIサーバーを起動します。使用ポート: {port}")
    # 一般的な開発用APIサーバーのポートは8000番が推奨されます
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
