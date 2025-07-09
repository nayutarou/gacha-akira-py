from settings import gacha_probs

def test_probabilities_are_int():
    for v in gacha_probs.values():
        assert isinstance(v, int)

def test_probabilities_in_range():
    for v in gacha_probs.values():
        assert 0 < v < 100
