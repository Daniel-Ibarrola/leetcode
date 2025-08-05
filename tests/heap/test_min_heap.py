from leetcode.heap.min_heap import MinHeap


class TestMinHeap:

    def test_peak_returns_min(self):
        heap = MinHeap([3, 1, 4, 1, 5, 9, 2])
        assert heap.peek() == 1

    def test_pop_returns_min_and_removes_it(self):
        heap = MinHeap([3, 1, 4, 5, 9, 2])
        assert heap.pop() == 1
        assert heap.peek() == 2

    def test_support_duplicate_elements(self):
        heap = MinHeap([5, 1, 3, 1])
        assert heap.pop() == 1
        assert heap.pop() == 1
        assert heap.pop() == 3

    def test_pushing_a_new_min_element_to_the_heap_becomes_the_smallest(self):
        heap = MinHeap([2, 8, 7, 9])
        heap.push(1)
        assert heap.peek() == 1
