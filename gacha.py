import random
from settings import gacha_probs


def gacha_draw():
    items: List[str] = list(gacha_probs.keys())
    weights: List[int] = list(gacha_probs.values())
    result = random.choices(items, weights=weights, k=1)[0]
    return result
