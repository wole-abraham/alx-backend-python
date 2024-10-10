#!/usr/bin/env python3
""" complex types """
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """ funtion to kv cjecke out """
    return (k, v ** 2)
