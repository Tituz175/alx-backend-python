#!/usr/bin/env python3
"""Module Documentation"""
import random


async def async_generator() -> float:
    """Fuction Documentation"""
    for i in range(10):
        await asyncio.sleep(1.0)
        yield (random.uniform(0, 10))
