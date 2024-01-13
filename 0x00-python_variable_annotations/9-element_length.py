#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Any, List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.
    """
    return [(i, len(i)) for i in lst]
