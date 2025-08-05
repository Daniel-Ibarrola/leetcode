from leetcode.heap.max_heap import MaxHeap


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = MaxHeap(nums)

    kth_largest = None
    for _ in range(k):
        kth_largest = heap.pop()

    return kth_largest
