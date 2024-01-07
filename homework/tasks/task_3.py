import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    """Return execution order of coroutines as a string."""
    results = await asyncio.gather(*coros)

    sorted_results = sorted(results, key=lambda ticket: ticket.number)

    return "".join(ticket.key for ticket in sorted_results)

if __name__ == "__main_":
    pass
