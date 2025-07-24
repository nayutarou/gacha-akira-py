# FastAPIライブラリをインポート
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gacha import gacha_draw


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[INFO] APIサーバーを起動します。使用ポート: 8000")
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to Gacha World!"}


@app.get("/gacha")
def get_gacha() -> dict:
    result: str = gacha_draw()
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    port = 8000
    print(f"[INFO] APIサーバーを起動します。使用ポート: {port}")
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
