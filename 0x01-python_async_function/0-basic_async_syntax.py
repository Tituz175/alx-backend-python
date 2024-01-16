#!/usr/bin/env python3
"""Module documentation"""
import random
import asyncio


async def wait_random(max_delay:int=10) -> float:
    """Function Documentation"""
    sleep_val = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_val)
    return sleep_val
