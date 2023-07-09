#!/usr/bin/env python3
'''Creates a multiplier function.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
