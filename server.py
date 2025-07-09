
from fastapi import FastAPI
from gacha import gacha_draw

app = FastAPI()

@app.get("/gacha")
def get_gacha():
    result = gacha_draw()
    return {"result": result}

# サーバー起動例: uvicorn server:app --reload
