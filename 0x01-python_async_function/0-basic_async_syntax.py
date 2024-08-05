#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.

Use the random module.
"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """wait a random a certain amountof time between 0 and max_delay"""
    delay: float = random.uniform(0, max_delay)
    time.sleep(delay)
    return delay

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
