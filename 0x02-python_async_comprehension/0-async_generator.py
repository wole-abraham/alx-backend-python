#!/usr/bin/env python3
""" Python script using async functions"""
import asyncio
import random

async def random_number_generator():
    """
    Coroutine that loops 10 times, each time asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Yield a random integer between 0 and 10
