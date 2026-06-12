from typing import Generic, TypeVar

T = TypeVar("T")
LinkedListTV = TypeVar("LinkedListTV", bound="LinkedList")


class ListNode(Generic[T]):
    def __init__(self, val: T, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"ListNode({self.val})"


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

    def remove_nth_from_end(self, nth: int) -> None:
        fast = self.head
        for _ in range(nth):
            fast = fast.next

        if fast is None:
            self.head = self.head.next
            return

        slow = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

    def reverse(self) -> None:
        """
        Reverses the list
        """
        prev = None
        current = self.head

        while current is not None:
            next_ = current.next
            current.next = prev

            prev = current
            current = next_

        self.head = prev

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

    def swap_pairs(self):
        """
        Given a reference head of type ListNode that is the head of a singly linked list,
        write a function to swap every two adjacent nodes and return its head.

        You must solve the problem without modifying the values in the list's nodes
        (i.e., only nodes themselves may be changed.)
        """
        dummy = ListNode(0)
        dummy.next = self.head

        tail = dummy
        first = self.head

        while first and first.next:
            second = first.next

            tail.next = second
            first.next = second.next
            second.next = first

            tail = first
            first = first.next

        self.head = dummy.next
