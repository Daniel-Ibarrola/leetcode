import heapq
from typing import TypeAlias

Number: TypeAlias = int | float


class MaxHeap:

    def __init__(self, items: list[Number]):
        self._items = [-item for item in items]
        heapq.heapify(self._items)

    def pop(self) -> Number:
        return -heapq.heappop(self._items)

    def push(self, item: Number) -> None:
        heapq.heappush(self._items, -item)

    def peek(self) -> Number:
        return -self._items[0]
