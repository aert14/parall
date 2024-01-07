from asyncio import Task
from typing import Any, Callable, Coroutine


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    """Await for the result of the function or coroutine."""
    if isinstance(f, Callable):
        return await f()
    elif isinstance(f, (Coroutine, Task)):
        return await f
    else:
        raise ValueError("invalid argument")

if __name__ == "__main_":
    pass
