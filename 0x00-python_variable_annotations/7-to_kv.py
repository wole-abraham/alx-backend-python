#!/usr/bin/env python3
""" complex types """
from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple[str, float]:
    return (k, v ** 2)
