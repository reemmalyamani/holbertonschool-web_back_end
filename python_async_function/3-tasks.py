#!/usr/bin/env python3
"""Async tasks module"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a function that returns an asyncio Task."""
    return asyncio.create_task(wait_random(max_delay))
