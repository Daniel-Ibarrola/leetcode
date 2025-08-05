from leetcode.heap.max_heap import MaxHeap


class TestMaxHeap:

    def test_peak_returns_max(self):
        heap = MaxHeap([3, 1, 4, 1, 5, 9, 2])
        assert heap.peek() == 9

    def test_pop_returns_max_and_removes_it(self):
        heap = MaxHeap([3, 1, 4, 5, 9, 2])
        assert heap.pop() == 9
        assert heap.peek() == 5

    def test_support_duplicate_elements(self):
        heap = MaxHeap([5, 1, 3, 1, 5])
        assert heap.pop() == 5
        assert heap.pop() == 5
        assert heap.pop() == 3

    def test_pushing_a_new_max_element_to_the_heap_becomes_the_largest(self):
        heap = MaxHeap([2, 8, 7, 9])
        heap.push(10)
        assert heap.peek() == 10
