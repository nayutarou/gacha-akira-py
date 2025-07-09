import random
from settings import gacha_probs

def gacha_draw():
    items = list(gacha_probs.keys())
    weights = list(gacha_probs.values())
    result = random.choices(items, weights=weights, k=1)[0]
    return result

if __name__ == "__main__":
    result = gacha_draw()
    print(f"ガチャの結果: {result}")
