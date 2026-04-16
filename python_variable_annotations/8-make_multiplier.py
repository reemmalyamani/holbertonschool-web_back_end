#!/usr/bin/env python3
"""Create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies by multiplier."""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
