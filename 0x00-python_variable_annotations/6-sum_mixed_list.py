#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum
as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return a sum of all int and floats in the list"""
    s: float = float(sum(mxd_lst))
    return s
