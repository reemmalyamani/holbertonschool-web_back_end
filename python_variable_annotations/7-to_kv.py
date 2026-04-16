#!/usr/bin/env python3
"""Return a tuple with string and square of number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return (k, v squared as float)."""
    return (k, float(v * v))
