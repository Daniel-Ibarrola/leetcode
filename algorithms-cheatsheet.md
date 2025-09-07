# Arrays

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
# Binary Tree

**DFS**
```python
def dfs(node):
    # base case
    if node is None:
        return some value
    
    ...
    
    left = dfs(node.left)
    right = dfs(node.right)
    return value based on left and right
```

**BFS**
```python
def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        curr_node = queue.popleft()
        result.append(curr_node.val)
        
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return result
```

# Graph

**DFS**

```python
def dfs(adj_list):
    if not adj_list:
        return
    visited = set()

    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        for neighbor in adj_list[node]:
            dfs_helper(neighbor)
        return

    # Handle disconnected components
    for node in adj_list:
        if node not in visited:
            dfs_helper(node)
```

**BFS**
```python
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
```

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

# Binary Search

```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # Target not found
```

# Dynamic Programming

```cpp
int Knapsack::maxProfit() const
{
    // Returns the optimal profit for the knapsack

    // Create a table of zeros with shape (num items, knapsack weight + 1)
    int numItems {static_cast<int>(m_weights.size())};
    std::vector<int> row (m_weight, 0);
    std::vector<std::vector<int>> table (numItems, row);

    // Fill the table
    for (auto item {1}; item < numItems + 1; ++item)
    {
        for (auto wt {1}; wt < m_weight + 1; ++wt)
        {
            // If the item weight is greater than the current weight skip it
            if (m_weights[item - 1] > wt)
                table[item][wt] = table[item - 1][wt];
            // Take the max of including vs excluding the item
            else
                table[item][wt] = std::max(table[item - 1][wt],
                                            m_profits[item - 1] + table[item - 1][wt - m_weights[item - 1]]);
        }
    }

    return table[numItems][m_weight];
}
```