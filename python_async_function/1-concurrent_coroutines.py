#!/usr/bin/env python3
"""Execute multiple coroutines concurrently"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create an asynchronous coroutine that spawns wait_random n times
    and returns delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
