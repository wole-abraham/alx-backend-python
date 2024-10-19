#!/usr/bin/env python3
"""
Import wait_random from the previous python file
that you’ve written and write an async
wait_n should return the list of all the delays
(float values).
The list of the delays should be in FLOAT VLAUES

"""

import asyncio
from typing import List
wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ retunrs a list  """
    delays = []
    tasks = [wait(max_delay) for x in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
