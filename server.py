import logging

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPIライブラリをインポート
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gacha import gacha_draw
from settings import API_PORT


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("APIサーバーを起動します。使用ポート: %s", API_PORT)
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
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to Gacha World!"}


@app.get("/gacha")
def get_gacha() -> dict:
    """
    Performs a gacha draw and returns the result.

    Returns:
        dict: A dictionary containing the gacha draw result.
    """
    result: str = gacha_draw()
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    port = API_PORT
    logger.info("APIサーバーを起動します。使用ポート: %s", port)
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)
