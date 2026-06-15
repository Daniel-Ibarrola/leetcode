# Graph

**DFS on Adjacency List**
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