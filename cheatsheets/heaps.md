# Heaps

**Top K frequent elements**
```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []

    counts = Counter(nums)
    # Use a min-heap to keep track of the k largest elements
    min_heap = []
    for num, freq in counts.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        elif freq > min_heap[0][0]:
            heapq.heapreplace(min_heap, (freq, num))

    return [num for freq, num in min_heap]
```
