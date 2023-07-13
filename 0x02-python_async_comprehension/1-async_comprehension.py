#!/usr/bin/env python3
"""async comprehensions over async_generator, then return the 10 random numbers."""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """This function returns 10 random numbers."""
    return [i async for i in async_generator()]
