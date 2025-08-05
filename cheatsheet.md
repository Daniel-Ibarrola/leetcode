**Prefix Sums**
```python
def subarray_sum(nums: list[int], target: int) -> int:
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1

    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        count += prefix_sums[current_sum - target]
        prefix_sums[current_sum] += 1

    return count
```

**Sliding Window**
```python
def fruits_into_baskets(fruits: list[int]) -> int:
    state: dict[int, int] = {}
    current_max = 0
    start = 0
    for end in range(len(fruits)):
        fruit = fruits[end]
        state[fruit] = state.get(fruit, 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start += 1

        current_max = max(current_max, end - start + 1)
    return current_max
```

**Two Pointers**
```python
def triangle_number(nums: list[int]) -> int:
    num_triplets = 0
    nums.sort()

    for ii in range(len(nums) - 1, 1, -1):
        left, right = 0, ii - 1

        while left < right:
            if nums[left] + nums[right] > nums[ii]:
                num_triplets += right - left
                right -= 1
            else:
                left += 1

    return num_triplets
```