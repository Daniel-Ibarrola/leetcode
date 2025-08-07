import heapq
from typing import TypeVar, Generic

T = TypeVar("T")


class MinHeap(Generic[T]):

    def __init__(self, items: list[T]):
        self._items = items[::]
        heapq.heapify(self._items)

    def pop(self) -> T:
        return heapq.heappop(self._items)

    def push(self, item: T) -> None:
        heapq.heappush(self._items, item)

    def peek(self) -> T:
        return self._items[0]

    def __len__(self) -> int:
        return len(self._items)
