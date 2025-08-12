from typing import Generic, TypeVar

T = TypeVar("T")
LinkedListTV = TypeVar("LinkedListTV", bound="LinkedList")


class ListNode(Generic[T]):
    def __init__(self, val: T, next_=None):
        self.val = val
        self.next = next_


class LinkedList(Generic[T]):

    def __init__(self, head: ListNode[T] = None):
        self.head = head

    @classmethod
    def from_list(cls: type[LinkedListTV], lst: list[T]) -> LinkedListTV:
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


NumericT = TypeVar("NumericT", int, float)


class NumericLinkedList(LinkedList[NumericT]):
    def __init__(self, head: ListNode[NumericT] = None):
        super().__init__(head)

    def is_palindrome(self) -> bool:
        # Find middle
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse middle
        prev = None
        current = slow
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Check palindrome
        left = self.head
        right = prev
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
