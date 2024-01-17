#!/usr/bin/env python3
"""Module Documentation"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Fuction Documentation"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
