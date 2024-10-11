#!/usr/bin/env python3
""" sum mixed list takes a list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ sums the values in the list"""
    return sum(mxd_list)
