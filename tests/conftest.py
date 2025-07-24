"""Pytest a shared fixture file."""

import pytest
from settings import gacha_probs


@pytest.fixture
def probs():
    """Provides the gacha probability settings as a fixture."""
    return gacha_probs


@pytest.fixture
def original_gacha_probs():
    """A fixture to restore gacha_probs after a test."""
    original = gacha_probs.copy()
    yield
    gacha_probs.clear()
    gacha_probs.update(original)
