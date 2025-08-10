from typing import Generic, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, val: T, next_=None):
        self.val = val
        self.next = next_


class LinkedList(Generic[T]):

    def __init__(self, head: ListNode[T] = None):
        self.head = head

    @classmethod
    def from_list(cls, lst: list[T]) -> "LinkedList[T]":
        head = None
        for item in reversed(lst):
            head = ListNode(item, head)
        return cls(head)

    def has_cycle(self) -> bool:
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next
