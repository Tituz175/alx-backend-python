#!/usr/bin/env python3
"""Module Documentation"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function Documentation"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*coroutines)
    return sorted(result)
