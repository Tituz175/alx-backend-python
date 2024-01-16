#!/usr/bin/env python3
"""Module Documentation"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*coroutines)
    return sorted(result)
