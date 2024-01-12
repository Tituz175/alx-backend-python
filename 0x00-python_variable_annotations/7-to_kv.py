#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str,  v: Union[float, int]) -> Tuple[str, float]:
    """
    This function takes a list mxd_lst of floats as argument
    and returns their sum as a float.
    """
    return (k, v**2)
