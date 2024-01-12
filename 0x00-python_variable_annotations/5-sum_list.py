#!/usr/bin/env python3
"""5. Complex types - list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
