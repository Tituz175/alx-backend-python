#!/usr/bin/env python3
"""Module Documentation"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Fuction Documentation"""
    for _ in range(10):
        await asyncio.sleep(1.0)
        yield (random.uniform(0, 10))
