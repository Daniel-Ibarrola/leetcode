# Hash Maps

**Complement Lookup (Two Sum family)**
For each element, check if its complement has already been seen. For modular problems, use `(k - x % k) % k` as the complement.
```python
# Standard: find pair summing to target
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

# Modular variant: count pairs where (a + b) % k == 0
def pairs_divisible_by_k(nums: list[int], k: int) -> int:
    count = 0
    freq: dict[int, int] = defaultdict(int)
    for num in nums:
        complement = (k - num % k) % k
        count += freq[complement]
        freq[num % k] += 1
    return count
```

**Frequency Map + Symmetric Matching**
Count frequencies, sort by a key (often `abs(x)`), then greedily consume pairs.
```python
# Check if array can be split into (x, 2x) pairs
def can_reorder_doubled(arr: list[int]) -> bool:
    freq = Counter(arr)
    for num in sorted(freq, key=abs):
        if freq[num] == 0:
            continue
        if freq[num * 2] < freq[num]:
            return False
        freq[num * 2] -= freq[num]
        freq[num] = 0
    return True
```

**HashSet Sequence Building**
Only start counting from sequence "heads" — elements with no left neighbor in the set.
```python
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:       # sequence head
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

**Group by Derived Key**
Map each element to a computed key; aggregate or query by that key.
```python
# Max sum of pair sharing the same digit sum
def max_sum_equal_digit_sum(nums: list[int]) -> int:
    best_in_group: dict[int, int] = {}
    result = -1
    for num in nums:
        key = sum(int(d) for d in str(num))
        if key in best_in_group:
            result = max(result, best_in_group[key] + num)
        best_in_group[key] = max(best_in_group.get(key, 0), num)
    return result

# Store indices by value for positional queries
def find_occurrences(nums: list[int], queries: list[list[int]]) -> list[int]:
    indices: dict[int, list[int]] = defaultdict(list)
    for i, num in enumerate(nums):
        indices[num].append(i)
    result = []
    for val, k in queries:
        idx_list = indices[val]
        result.append(idx_list[k - 1] if k <= len(idx_list) else -1)
    return result
```

**Incremental Dual-Map (Query Processing)**
Use two complementary maps (`item→property` and `property→count`) to answer each query in O(1).
```python
def query_distinct_colors(queries: list[list[int]]) -> list[int]:
    ball_color: dict[int, int] = {}
    color_count: dict[int, int] = defaultdict(int)
    result = []
    for ball, color in queries:
        if ball in ball_color:
            old = ball_color[ball]
            color_count[old] -= 1
            if color_count[old] == 0:
                del color_count[old]
        ball_color[ball] = color
        color_count[color] += 1
        result.append(len(color_count))
    return result
```
