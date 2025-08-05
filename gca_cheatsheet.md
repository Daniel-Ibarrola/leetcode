# GCA Algorithmic Techniques Cheatsheet

## Prefix Sums
Used for range sum problems and subarray sum calculations.

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

---

## Sliding Window
For problems involving contiguous subarrays or substrings.

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

---

## Two Pointers
Common in sorted arrays for pair or triplet problems.

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

---

## Hash Map Lookup
Efficient index/value lookup, e.g., Two Sum.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return []
```

---

## Set for Uniqueness
Track unique items, e.g., longest substring without repeats.

```python
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## Backtracking (DFS)
Used for exploring paths with constraints, e.g., Word Search.

```python
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        temp, board[r][c] = board[r][c], '#'
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False
```

---

## Greedy
Pick best local option, e.g., meeting rooms.

```python
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
```

---

## Monotonic Stack
Used for "next greater element" problems.

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = nums[i]
        stack.append(i)

    return result
```
