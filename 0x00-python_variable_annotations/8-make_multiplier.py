#!/usr/bin/env python3
""" Write a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function thatt will mulitply the paramenter """
    def multiply(number: float) -> float:
        """ multiplies the parameter  """
        return multiplier * number
    return multiply
