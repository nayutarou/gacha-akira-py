# ガチャの抽選ロジックを定義するモジュール
import random
from typing import List
from settings import gacha_probs


def gacha_draw() -> str:
    """
    Performs a gacha draw based on predefined probabilities.

    Raises:
        ValueError: If the total probability is not 100 or if the item list is empty.

    Returns:
        str: The result of the gacha draw.
    """
    if sum(gacha_probs.values()) != 100:
        raise ValueError("Total probability must be 100")
    items: List[str] = list(gacha_probs.keys())
    weights: List[int] = list(gacha_probs.values())
    if not items:
        raise ValueError("Item list is empty")
    result = random.choices(items, weights=weights, k=1)[0]
    return result
