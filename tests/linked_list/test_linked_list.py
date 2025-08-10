from leetcode.linked_list.linked_list import LinkedList
import pytest


class TestLinkedList:

    def test_from_list(self):
        linked_list = LinkedList.from_list([1, 2, 3])

        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 2
        assert linked_list.head.next.next.val == 3

    def test_iter(self):
        items = [1, 2, 3]
        linked_list = LinkedList.from_list(items)
        ii = 0
        for item in linked_list:
            assert item == items[ii]
            ii += 1

    @staticmethod
    def _build_linked_list_with_cycle(values: list[int], pos: int) -> LinkedList[int]:
        """
        Builds a LinkedList with optional cycle.
        If pos >= 0, creates a cycle by connecting the tail to the node at index pos.
        """
        linked_list = LinkedList.from_list(values)

        if not values or pos < 0:
            return linked_list

        # Get references to nodes for cycle creation
        current = linked_list.head
        cycle_node = None
        index = 0
        while current.next:
            if index == pos:
                cycle_node = current
            current = current.next
            index += 1

        # Close the loop
        if index == pos:
            cycle_node = current
        current.next = cycle_node

        return linked_list

    @pytest.mark.parametrize(
        "values, pos, expected",
        [
            # ✅ Cycles present
            ([3, 2, 0, -4], 1, True),  # Tail connects to node index 1
            ([1, 2], 0, True),  # Tail connects to first node
            ([1], 0, True),  # Single node cycle to itself
            ([1, 2, 3, 4, 5], 2, True),  # Tail connects to middle node
            # ❌ No cycles
            ([1], -1, False),  # Single node, no cycle
            ([1, 2], -1, False),  # Two nodes, no cycle
            ([], -1, False),  # Empty list
            ([1, 2, 3, 4], -1, False),  # Multi-node, no cycle
        ],
    )
    def test_has_cycle(self, values: list[int], pos: int, expected: bool):
        linked_list = self._build_linked_list_with_cycle(values, pos)
        assert linked_list.has_cycle() == expected
