import asyncio
from typing import Coroutine


async def limit_execution_time(
    coro: Coroutine, max_execution_time: float
) -> None:
    """Cancel the coroutine after timeout."""
    task = asyncio.create_task(coro)
    try:
        await asyncio.wait_for(task, timeout=max_execution_time)
    except asyncio.TimeoutError:
        pass


async def limit_execution_time_many(
    *coros: Coroutine, max_execution_time: float
) -> None:
    """Cancel the coroutines after timeout."""
    tasks = []
    for coro in coros:
        tasks.append(asyncio.create_task(coro))

    try:
        await asyncio.wait_for(
            asyncio.gather(*tasks), timeout=max_execution_time
        )
    except asyncio.TimeoutError:
        pass

if __name__ == "__main_":
    pass