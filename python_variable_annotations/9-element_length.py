#!/usr/bin/env python3
"""Return list of tuples with element and its length."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples (element, length)."""
    return [(i, len(i)) for i in lst]
