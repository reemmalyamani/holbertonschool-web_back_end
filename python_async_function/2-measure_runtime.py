#!/usr/bin/env python3
"""Measure runtime of async operations"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Create a function that measures total execution time
    and returns the average per coroutine."""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()
    total_time = end - start

    return total_time / n
