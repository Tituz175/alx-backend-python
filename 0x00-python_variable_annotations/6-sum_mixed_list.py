#!/usr/bin/env python3
"""6. Complex types - mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list mxd_lst of floats as argument
    and returns their sum as a float.
    """
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
