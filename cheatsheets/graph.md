# Graph

**DFS on Adjacency List**
```python
def dfs(adj_list):
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

**BFS on Adjacency List**
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
**DFS on Matrix**
```python
def dfs(matrix):
  visited = set()
  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  def dfs_helper(r, c):
    if (r, c) in visited:
      return
    # check if the cell is out of bounds
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
      return
    visited.add((r, c))
    for dr, dc in directions:
      dfs_helper(r + dr, c + dc)
    return
   dfs_helper(0, 0)

```

**Cycle Detection — Directed Graph (3-state DFS)**
```python
# UNVISITED → VISITING → VISITED
# Cycle exists if DFS reaches a VISITING node (back edge)
def has_cycle(node):
    if state[node] == VISITING: return True
    if state[node] == VISITED:  return False

    state[node] = VISITING
    for neighbor in adj_list[node]:
        if has_cycle(neighbor): return True
    state[node] = VISITED
    return False
```

**DFS + Memoization on DAG**
```python
# Cache the result for each node to avoid recomputation
# Use when subproblems overlap (e.g. longest path, number of paths)
memo = {}
def dfs(node):
    if node in memo: return memo[node]

    best = 0
    for neighbor in adj_list[node]:
        best = max(best, dfs(neighbor) + 1)

    memo[node] = best
    return best

# Try every node as a starting point (no guaranteed single source)
answer = max(dfs(node) for node in range(n))
```

**Topological Sort**
```python
def topological_sort(adj_list, n):
  # calculate indegree of each node
  indegree = [0] * n
  for u in adj_list:
      for v in adj_list[u]:
          indegree[v] += 1
  # enqueue nodes with indegree 0
  queue = deque([u for u in range(n) if indegree[u] == 0])
  order = []
  while queue:
      u = queue.popleft()
      order.append(u)
      
      for v in adj_list.get(u, []):
          indegree[v] -= 1
          if indegree[v] == 0:
              queue.append(v)
  return order if len(order) == n else []
```